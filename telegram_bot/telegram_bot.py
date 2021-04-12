import os
import logging

import emoji
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, \
    ConversationHandler, CallbackContext

from dialogue_system.dialogue_system import DialogueSystem

# Setting logger config
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Setting emoji to use during conversation
emoji_doctor = emoji.emojize(":woman_health_worker:")
emoji_noting = emoji.emojize(":clipboard:")


class TelegramBot:
    def __init__(self):
        # State of chatbot client either INIT or QUESTIONING or DONE
        self.__current_state = None

        # Selected disease to conduct questioning
        self.__selected_disease = None

        # State of doctors questioning, given previous
        # state and text, isolated from chatbot client,
        # obtained from dialogue system in REST manner
        self.__questioning_state = None

        # Initialize dialogue system
        self.__dialogue_system = DialogueSystem()

        # All possible conversation states which are known to chatbot client
        self.__conversation_states = \
            self.__dialogue_system.get_conversation_states

        # Change to comprehension from diseases list
        self.__reply_keyboard = [
            [disease] for disease in self.__dialogue_system.get_diseases_list
        ]

        self.__yes_no_keyboard = [
            ["Так"],
            ["Ні"]
        ]

        self.__done_keyboard = [
            ["Завершити"]
        ]
        self.__markup = ReplyKeyboardMarkup(self.__reply_keyboard)
        self.__yes_no_markup = \
            ReplyKeyboardMarkup(self.__yes_no_keyboard, resize_keyboard=True)
        self.__done_markup = \
            ReplyKeyboardMarkup(self.__done_keyboard, resize_keyboard=True)

    def start(self, update: Update, _: CallbackContext) -> int:
        update.message.reply_text(
            f"{emoji_doctor}"
        )
        update.message.reply_text(
            "Доброго дня! Що вас турбує?",
            reply_markup=self.__markup,
        )
        self.__current_state = self.__conversation_states.INIT.value

        return self.__current_state

    def initialize_dialogue(self, update: Update,
                            context: CallbackContext) -> int:
        text = update.message.text
        context.user_data['choice'] = text
        # TODO Handle errors
        self.__selected_disease = text
        print(self.__selected_disease)
        reply = self.__dialogue_system.respond(disease=self.__selected_disease,
                                               message=(self.__current_state,
                                                        text))
        self.__current_state = self.__conversation_states.QUESTIONING.value
        self.__questioning_state = reply[0]
        update.message.reply_text(f"{emoji_doctor}Обрана проблема: "
                                  f"{text.lower()}"
                                  f"\n\n{emoji_noting}Будь ласка, "
                                  "дай відповідь на декілька "
                                  "запитань щоб уточнити проблему")
        update.message.reply_text(f"{emoji_doctor}{reply[1]}",
                                  reply_markup=self.__yes_no_markup)

        return self.__current_state

    def regular_choice(self, update: Update, context: CallbackContext) -> int:
        text = update.message.text
        context.user_data['choice'] = text

        reply = self.__dialogue_system. \
            respond(disease=self.__selected_disease,
                    message=(self.__questioning_state, text))

        self.__questioning_state = reply[0]

        if self.__questioning_state == self.__conversation_states.DONE.value:
            self.__current_state = self.__questioning_state
            update.message.reply_text(f"{emoji_doctor}{reply[1]}",
                                      reply_markup=self.__done_markup)
            return self.__current_state

        update.message.reply_text(f"{emoji_doctor}{reply[1]}",
                                  reply_markup=self.__yes_no_markup)

        return self.__current_state

    def done(self, update: Update, context: CallbackContext) -> int:
        user_data = context.user_data

        update.message.reply_text(
            f"{emoji_doctor}Будьте здорові! "
            "Для початку діалогу, натисніть будь ласка /start",
            reply_markup=ReplyKeyboardRemove(),
        )

        user_data.clear()
        return ConversationHandler.END

    def main(self) -> None:
        # Create the Updater and pass it your bot's token.
        token = os.environ["PMC_TOKEN"]

        updater = Updater(token=token)

        # Get the dispatcher to register handlers
        dispatcher = updater.dispatcher

        joined_diseases_list = \
            '|'.join(
                disease for disease in self.__dialogue_system.get_diseases_list
            )

        diseases_regex = \
            f"^({joined_diseases_list})$"

        # Add conversation handler with the states INPUTTING_PROBLEM,
        # TYPING_CHOICE and TYPING_REPLY
        conv_handler = ConversationHandler(
            entry_points=[CommandHandler("start", self.start)],
            states={
                self.__conversation_states.INIT.value: [
                    MessageHandler(
                        Filters.regex(diseases_regex), self.initialize_dialogue
                    ),
                ],
                self.__conversation_states.QUESTIONING.value: [
                    MessageHandler(
                        Filters.regex("^(Так|Ні)$"), self.regular_choice
                    ),
                ]
            },
            fallbacks=[MessageHandler(Filters.regex("^Завершити"), self.done)],
        )

        dispatcher.add_handler(conv_handler)

        # Start the Bot
        updater.start_polling()

        # Run the bot until you press Ctrl-C or the process receives SIGINT,
        # SIGTERM or SIGABRT. This should be used most of the time, since
        # start_polling() is non-blocking and will stop the bot gracefully.
        updater.idle()
