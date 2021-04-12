from enum import Enum
import emoji

red_circle_sign = emoji.emojize(":red_circle:")
apple_sign = emoji.emojize(":green_apple:")
checkmark_sign = emoji.emojize(":round_pushpin:")

# transitions dict - dictionary with all diseases states transition dictionaries
# as values and diseases strings as keys
transitions_dict = {}

# List of all diseases
diseases_list = ["Алергія", "Біль у горлі", "Кашель", "Діарея", "Опік",
                 "Тютюнопаління", "Закрита травма",
                 "Відкрита рана", "Стрес", "Підозра на туберкульоз",
                 "Підозра на ВІЛ/СНІД", "Безсоння",
                 "Біль у м'язах", "Біль у спині", "Ураження губ",
                 "Головний біль", "Запор", "Короста",
                 "Педикульоз", "Печія", "Підвищення температури тіла",
                 "Остеопороз", "Риніт", "Грип", "Остеоартроз",
                 "Дефіцит йоду", "Вугрова хвороба", "Зубний біль",
                 "Недостатність підшлункової залози",
                 "Порушення функції жовчного міхура",
                 "Захворювання нирок і сечовивідних шляхів",
                 "Клімактеричні розлади", "Контрацепція",
                 "Біль органів травлення та сечових шляхів",
                 "Варикозне розширення вен", "Сечокам'яна хвороба",
                 "Коронавірус"]


# Define done, initial and questioning state
class ConversationStates(Enum):
    DONE = 0
    INIT = 1
    QUESTIONING = 2


# Allergy states
class AllergyStates(Enum):
    ALLERGY_SYMPTOMS = 3
    ALLERGY_ALLERGENES_CONTACT = 4


allergy_dict = {
    (ConversationStates.INIT.value, "Алергія"): (
        AllergyStates.ALLERGY_SYMPTOMS.value,
        "Чи наявні один або декілька симптомів алергії:\n\n"
        "{red_circle_sign}чхання,\n"
        f"{red_circle_sign}свербіж і почервоніння очей,\n"
        f"{red_circle_sign}водянисті виділення з носа,\n"
        f"{red_circle_sign}шкірні висипи,\n"
        f"{red_circle_sign}шкірний свербіж"),
    (AllergyStates.ALLERGY_SYMPTOMS.value, "Так"): (
        AllergyStates.ALLERGY_ALLERGENES_CONTACT.value,
        "Чи наявний зв'язок симптомів із можливим контактом "
        "з алергенами:\n\n"
        f"{red_circle_sign}домашні тварини, сухий корм для риб,\n"
        f"{red_circle_sign}період цвітіння рослин,\n"
        f"{red_circle_sign}контакт із хімічними речовинами,\n"
        f"{red_circle_sign}прийом лікарських засобів,\n"
        f"{red_circle_sign}уживання деяких продуктів харчування,\n"
        f"{red_circle_sign}укуси комах,\n"
        f"{red_circle_sign}сонячне опромінення, холод"),
    (AllergyStates.ALLERGY_SYMPTOMS.value, "Ні"): (
        ConversationStates.DONE.value,
        "Необхідно звернутися до лікаря для уточнення діагнозу"),
    (AllergyStates.ALLERGY_ALLERGENES_CONTACT.value, "Так"): (
        ConversationStates.DONE.value,
        "Необхідно звернутися до лікаря "
        "для уточнення діагнозу\n\n"
        "Для полегшення симптомів алергії:\n"
        f"{apple_sign}намагатися уникати контакту "
        "з потенційними алергенами,\n"
        f"{apple_sign}проводити елімінаційні заходи "
        "стосовно зовнішніх алергенів:\n"
        f"{checkmark_sign}частіше приймати душ, провітрювати"
        " приміщення,\n"
        f"{checkmark_sign}робити вологе прибирання,\n"
        f"{checkmark_sign}застосовувати гіпоалергенну,"
        " елімінаційну дієту"),
    (AllergyStates.ALLERGY_ALLERGENES_CONTACT.value, "Ні"): (
        ConversationStates.DONE.value,
        "Необхідно звернутися до лікаря "
        "для уточнення діагнозу\n\n"
        "Для тимчасового полегшення симптомів "
        "алергії можна приймати:\n"
        f"{apple_sign}антигістамінні препарати для "
        "системного і місцевого застосування,\n"
        f"{apple_sign}засоби елімінаційної терапії,\n"
        f"{apple_sign}симпатоміметики для"
        " місцевого застосування")
}
transitions_dict['Алергія'] = allergy_dict


# Sore throat states
class SoreThroatStates(Enum):
    SORE_THROAT_PRESSURE = 5
    SORE_THROAT_REASON = 6
    SORE_THROAT_SYMPTOMS = 7
    SORE_THROAT_DIABETES = 8


sore_throat_dict = {
    (ConversationStates.INIT.value, "Біль у горлі"):
        (SoreThroatStates.SORE_THROAT_PRESSURE.value,
         "Біль у горлі виник після надмірного тривалого "
         "навантаження на голосові зв'язки або тривалого "
         "перебування у прокуреному приміщенні, "
         "вдиханні хімічних речовин?"),
    (SoreThroatStates.SORE_THROAT_PRESSURE.value, "Ні"):
        (SoreThroatStates.SORE_THROAT_REASON.value,
         "Біль у горлі виник:\n\n"
         f"{red_circle_sign}після переохолодження (та/або "
         "контакту з хворим на ГРВІ) і супроводжується "
         "іншими симптомами застуди (головний біль, риніт, "
         "лихоманка, і т.д.),\n"
         f"{red_circle_sign}під час вдихання холодного повітря,\n"
         f"{red_circle_sign}через хронічний тонзиліт"),
    (SoreThroatStates.SORE_THROAT_PRESSURE.value, "Так"):
        (ConversationStates.DONE.value,
         "Для полегшення стану можна "
         "рекомендувати препарат, який містить "
         "місцевий анестетик"),
    (SoreThroatStates.SORE_THROAT_REASON.value, "Так"):
        (SoreThroatStates.SORE_THROAT_SYMPTOMS.value,
         "Чи є у вас скарги на:\n\n"
         f"{red_circle_sign}відчуття болю під час ковтання,\n"
         f"{red_circle_sign}осиплість,\n"
         f"{red_circle_sign}виражене почервоніння горла,\n"
         f"{red_circle_sign}видиме збільшення піднебінних "
         "мигдаликів та поява нальоту на мигдаликах,\n"
         f"{red_circle_sign}припухлість, болісність лімфатичних "
         "вузлів,\n"
         f"{red_circle_sign}супутні шкірні висипання,\n"
         f"{red_circle_sign}появу головного болю, болю у вухах, "
         "животі, грудній клітці,\n"
         f"{red_circle_sign}лихоманку (вище 39 градусів), "
         "різку загальну слабкість, нездужання, блювання,\n"
         f"{red_circle_sign}ви вагітні (жінкам)?"),
    (SoreThroatStates.SORE_THROAT_REASON.value, "Ні"):
        (ConversationStates.DONE.value,
         "Необхідно звернутися до лікаря "
         "для уточнення діагнозу"),
    (SoreThroatStates.SORE_THROAT_SYMPTOMS.value, "Так"):
        (ConversationStates.DONE.value,
         "Необхідно звернутися до лікаря "
         "для уточнення діагнозу"),
    (SoreThroatStates.SORE_THROAT_SYMPTOMS.value, "Ні"):
        (SoreThroatStates.SORE_THROAT_DIABETES.value,
         "Чи хворієте ви на цукровий діабет?"),
    (SoreThroatStates.SORE_THROAT_DIABETES.value, "Ні"):
        (ConversationStates.DONE.value,
         "Вам можна рекомендувати препарати для симптоматичного "
         "лікування болю в горлі (таблетки, льодяники для "
         "розсмоктуваання, аерозолі, спреї, розчини та ін.). "
         "Сучасні комплексні препарати на основі "
         "фітонірингових технологій"),
    (SoreThroatStates.SORE_THROAT_DIABETES.value, "Так"):
        (ConversationStates.DONE.value,
         "Вам можна рекомендувати препарати у спеціальних "
         "лікарських формах для розсмоктування для хворих "
         "із цукровим діабетом, таблетки, аерозолі, спреї, "
         "полоскання без вмісту цукру")

}
transitions_dict['Біль у горлі'] = sore_throat_dict


# Cough states
class CoughStates(Enum):
    COUGH_LASTING = 9
    COUGH_DRY = 10
    COUGH_SMOKING = 11
    COUGH_SYMPTOMS = 12
    COUGH_SORE_THROAT = 13
    COUGH_FLU = 14
    COUGH_ITCH = 15
    COUGH_IRRITATION = 16


cough_dict = {
    (ConversationStates.INIT.value, "Кашель"):
        (CoughStates.COUGH_LASTING.value,
         "У вас кашель триває більше 3 днів?"),
    (CoughStates.COUGH_LASTING.value, "Ні"):
        (CoughStates.COUGH_DRY.value,
         "У вас кашель сухий?"),
    (CoughStates.COUGH_LASTING.value, "Так"):
        (ConversationStates.DONE.value,
         "Необхідно звернутися до лікаря!"),
    (CoughStates.COUGH_DRY.value, "Ні"):
        (CoughStates.COUGH_SYMPTOMS.value,
         "Чи є загрозливі симптоми:\n\n"
         f"{red_circle_sign}інтенсивність кашлю зростає,\n"
         f"{red_circle_sign}висока (вище 38 градусів) температура,\n"
         f"{red_circle_sign}задишка, біль у грудній клітці при диханні,\n"
         f"{red_circle_sign}виділення густого зеленуватого мокротиння,\n"
         f"{red_circle_sign}виділення мокротиння з прожилками крові,\n"
         f"{red_circle_sign}утруднення дихання, напади ядухи"),
    (CoughStates.COUGH_DRY.value, "Так"):
        (CoughStates.COUGH_SMOKING.value,
         "Чи ви курите?"),
    (CoughStates.COUGH_SMOKING.value, "Ні"):
        (CoughStates.COUGH_IRRITATION.value,
         "Чи мало місце вдихання пилу або подразнюючої "
         "хімічної речовини?"),
    (CoughStates.COUGH_SMOKING.value, "Так"):
        (ConversationStates.DONE.value,
         "Тютюновий дим подразнює дихальні шляхи та призводить "
         "до розвитку багатьох захворювань. Якщо кашель турбує більше "
         "тижня, необхідно звернутися до лікаря!"),
    (CoughStates.COUGH_IRRITATION.value, "Так"):
        (ConversationStates.DONE.value,
         "Якщо подібний кашель не зникає протягом години, "
         "необхідно звернутися до лікаря!"),
    (CoughStates.COUGH_IRRITATION.value, "Ні"):
        (CoughStates.COUGH_FLU.value,
         "Ви нещодавно хворіли на ГРВІ?"),
    (CoughStates.COUGH_SYMPTOMS.value, "Ні"):
        (CoughStates.COUGH_SORE_THROAT.value,
         "Чи є у вас біль у горлі, свербіння у носі, чхання, "
         "закладеність носа?"),
    (CoughStates.COUGH_SYMPTOMS.value, "Так"):
        (ConversationStates.DONE.value,
         "Необхідно терміново звернутися до лікаря!"),
    (CoughStates.COUGH_SORE_THROAT.value, "Ні"):
        (CoughStates.COUGH_FLU.value,
         "Ви нещодавно хворіли на ГРВІ?"),
    (CoughStates.COUGH_SORE_THROAT.value, "Так"):
        (ConversationStates.DONE.value,
         "Можливо, у вас ГРВІ. Вам показані "
         "постільний режим, вживання теплих напоїв, "
         "прийом протикашльових лікарських засобів. "
         "Для комплексного впливу на патологію кашлю прийміть "
         "комбінований фітоніринговий препарат. Якщо протягом доби "
         "вам не полегшає, необхідно звернутися до лікаря."),
    (CoughStates.COUGH_FLU.value, "Так"):
        (ConversationStates.DONE.value,
         "Можливо, кашель є проявом залишкових явищ респіраторного "
         "захворювання. Вам показані протикашльові лікарські засоби "
         "центральної або периферійної дії. У зв'язку з тим, "
         "що деякі з них належать до рецептурних, необхідно звернутися "
         "до лікаря. "),
    (CoughStates.COUGH_FLU.value, "Ні"):
        (CoughStates.COUGH_ITCH.value,
         "Чи є у вас свербіж шкіри?"),
    (CoughStates.COUGH_ITCH.value, "Так"):
        (ConversationStates.DONE.value,
         "Можливо, кашель є проявом алергічної реакції"),
    (CoughStates.COUGH_ITCH.value, "Ні"):
        (ConversationStates.DONE.value,
         "Сухий кашель, який зберігається тривалий час, "
         "може бути симптомом багатьох захворювань. "
         "Необхідно звернутися до лікаря"),
}
transitions_dict["Кашель"] = cough_dict
