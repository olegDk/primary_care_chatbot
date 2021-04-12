from typing import Tuple, Type
from dialogue_system.diseases.constants import diseases_list,\
    ConversationStates, transitions_dict


class DialogueSystem:
    def __init__(self):
        self.__diseases_list = diseases_list
        self.__transitions_dict = transitions_dict
        self.__conversation_states = ConversationStates

    @property
    def get_diseases_list(self) -> list:
        return self.__diseases_list

    @property
    def get_conversation_states(self) -> Type[ConversationStates]:
        return self.__conversation_states

    @property
    def get_transitions_dict(self) -> dict:
        return self.__transitions_dict

    def respond(self, disease: str,
                message: Tuple[int, str]) -> Tuple[int, str]:
        return self.__transitions_dict[disease][message]
