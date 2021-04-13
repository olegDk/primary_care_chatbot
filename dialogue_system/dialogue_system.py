from typing import Tuple
from dialogue_system.diseases.constants import diseases_list,\
    transitions_dict, DONE, INIT, QUESTIONING


class DialogueSystem:
    def __init__(self):
        self.__diseases_list = diseases_list
        self.__transitions_dict = transitions_dict

    @property
    def get_diseases_list(self) -> list:
        return self.__diseases_list

    @property
    def done(self) -> int:
        return DONE

    @property
    def init(self) -> int:
        return INIT

    @property
    def questioning(self) -> int:
        return QUESTIONING

    @property
    def get_transitions_dict(self) -> dict:
        return self.__transitions_dict

    def respond(self, disease: str,
                message: Tuple[int, str]) -> Tuple[int, str]:
        return self.__transitions_dict[disease][message]
