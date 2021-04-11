from dialogue_system.diseases.constants import diseases_list, conversation_states_dict, transitions_dict
from typing import Tuple


class DialogueSystem:
    def __init__(self):
        self.__diseases_list = diseases_list
        self.__transitions_dict = transitions_dict
        self.__conversation_states_dict = conversation_states_dict

    @property
    def get_diseases_list(self) -> list:
        return self.__diseases_list

    @property
    def get_conversation_states_dict(self) -> dict:
        return self.__conversation_states_dict

    @property
    def get_transitions_dict(self) -> dict:
        return self.__transitions_dict

    def respond(self, disease: str, message: Tuple[int, str]) -> Tuple[int, str]:
        return self.__transitions_dict[disease][message]
