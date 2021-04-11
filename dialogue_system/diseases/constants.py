import emoji

red_circle_sign = emoji.emojize(":red_circle:")
apple_sign = emoji.emojize(":green_apple:")
checkmark_sign = emoji.emojize(":round_pushpin:")

# transitions dict - dictionary with all diseases states transition dictionaries as values
# and diseases strings as keys
transitions_dict = {}

# List of all diseases
diseases_list = ["Алергія", "Біль у горлі", "Кашель", "Діарея", "Опік", "Тютюнопаління", "Закрита травма",
                 "Відкрита рана", "Стрес", "Підозра на туберкульоз", "Підозра на ВІЛ/СНІД", "Безсоння",
                 "Біль у м'язах", "Біль у спині", "Ураження губ", "Головний біль", "Запор", "Короста",
                 "Педикульоз", "Печія", "Підвищення температури тіла", "Остеопороз", "Риніт", "Грип", "Остеоартроз",
                 "Дефіцит йоду", "Вугрова хвороба", "Зубний біль", "Недостатність підшлункової залози",
                 "Порушення функції жовчного міхура", "Захворювання нирок і сечовивідних шляхів",
                 "Клімактеричні розлади", "Контрацепція", "Біль органів травлення та сечових шляхів",
                 "Варикозне розширення вен", "Сечокам'яна хвороба", "Коронавірус"]

# Define done and initial state
conversation_states_dict = {
    "DONE": 0,
    "INIT": 1,
    "QUESTIONING": 2
}

# Allergy states and dict
allergy_states_str = ["ALLERGY_SYMPTOMS", "ALLERGY_ALLERGENES_CONTACT"]
allergy_states_dict = dict(zip(allergy_states_str, range(3, 5)))
allergy_dict = {
    (conversation_states_dict["INIT"], "Алергія"): (allergy_states_dict["ALLERGY_SYMPTOMS"],
                                                    f"Чи наявні один або декілька симптомів алергії:\n\n"
                                                    f"{red_circle_sign}чхання,\n"
                                                    f"{red_circle_sign}свербіж і почервоніння очей,\n"
                                                    f"{red_circle_sign}водянисті виділення з носа,\n"
                                                    f"{red_circle_sign}шкірні висипи,\n"
                                                    f"{red_circle_sign}шкірний свербіж"),
    (allergy_states_dict["ALLERGY_SYMPTOMS"], "Так"): (allergy_states_dict["ALLERGY_ALLERGENES_CONTACT"],
                                                       f"Чи наявний зв'язок симптомів із можливим контактом "
                                                       f"з алергенами:\n\n"
                                                       f"{red_circle_sign}домашні тварини, сухий корм для риб,\n"
                                                       f"{red_circle_sign}період цвітіння рослин,\n"
                                                       f"{red_circle_sign}контакт із хімічними речовинами,\n"
                                                       f"{red_circle_sign}прийом лікарських засобів,\n"
                                                       f"{red_circle_sign}уживання деяких продуктів харчування,\n"
                                                       f"{red_circle_sign}укуси комах,\n"
                                                       f"{red_circle_sign}сонячне опромінення, холод"),
    (allergy_states_dict["ALLERGY_SYMPTOMS"], "Ні"): (conversation_states_dict["DONE"],
                                                      f"Необхідно звернутися до лікаря для уточнення діагнозу"),
    (allergy_states_dict["ALLERGY_ALLERGENES_CONTACT"], "Так"): (conversation_states_dict["DONE"],
                                                                 f"Необхідно звернутися до лікаря "
                                                                 f"для уточнення діагнозу\n\n"
                                                                 f"Для полегшення симптомів алергії:\n"
                                                                 f"{apple_sign}намагатися уникати контакту "
                                                                 f"з потенційними алергенами,\n"
                                                                 f"{apple_sign}проводити елімінаційні заходи "
                                                                 f"стосовно зовнішніх алергенів:\n"
                                                                 f"{checkmark_sign}частіше приймати душ, провітрювати"
                                                                 f" приміщення,\n"
                                                                 f"{checkmark_sign}робити вологе прибирання,\n"
                                                                 f"{checkmark_sign}застосовувати гіпоалергенну,"
                                                                 f" елімінаційну дієту"),
    (allergy_states_dict["ALLERGY_ALLERGENES_CONTACT"], "Ні"): (conversation_states_dict["DONE"],
                                                                f"Необхідно звернутися до лікаря "
                                                                f"для уточнення діагнозу\n\n"
                                                                f"Для тимчасового полегшення симптомів "
                                                                f"алергії можна приймати:\n"
                                                                f"{apple_sign}антигістамінні препарати для "
                                                                f"системного і місцевого застосування,\n"
                                                                f"{apple_sign}засоби елімінаційної терапії,\n"
                                                                f"{apple_sign}симпатоміметики для"
                                                                f" місцевого застосування")
}
transitions_dict['Алергія'] = allergy_dict


# Sore throat states and dict
sore_throat_states_str = ["SORE_THROAT_PRESSURE", "SORE_THROAT_REASON",
                          "SORE_THROAT_SYMPTOMS", "SORE_THROAT_DIABETES"]
sore_throat_states_dict = dict(zip(sore_throat_states_str, range(5, 9)))
sore_throat_dict = {
    (conversation_states_dict["INIT"], "Біль у горлі"): (sore_throat_states_dict["SORE_THROAT_PRESSURE"],
                                                         f"Біль у горлі виник після надмірного тривалого "
                                                         f"навантаження на голосові зв'язки або тривалого "
                                                         f"перебування у прокуреному приміщенні, "
                                                         f"вдиханні хімічних речовин?"),
    (sore_throat_states_dict["SORE_THROAT_PRESSURE"], "Ні"): (sore_throat_states_dict["SORE_THROAT_REASON"],
                                                              f"Біль у горлі виник:\n\n"
                                                              f"{red_circle_sign}після переохолодження (та/або "
                                                              f"контакту з хворим на ГРВІ) і супроводжується "
                                                              f"іншими симптомами застуди (головний біль, риніт, "
                                                              f"лихоманка, і т.д.),\n"
                                                              f"{red_circle_sign}під час вдихання холодного повітря,\n"
                                                              f"{red_circle_sign}через хронічний тонзиліт"),
    (sore_throat_states_dict["SORE_THROAT_PRESSURE"], "Так"): (conversation_states_dict["DONE"],
                                                               f"Для полегшення стану можна "
                                                               f"рекомендувати препарат, який містить "
                                                               f"місцевий анестетик"),
    (sore_throat_states_dict["SORE_THROAT_REASON"], "Так"): (sore_throat_states_dict["SORE_THROAT_SYMPTOMS"],
                                                             f"Чи є у вас скарги на:\n\n"
                                                             f"{red_circle_sign}відчуття болю під час ковтання,\n"
                                                             f"{red_circle_sign}осиплість,\n"
                                                             f"{red_circle_sign}виражене почервоніння горла,\n"
                                                             f"{red_circle_sign}видиме збільшення піднебінних "
                                                             f"мигдаликів та поява нальоту на мигдаликах,\n"
                                                             f"{red_circle_sign}припухлість, болісність лімфатичних "
                                                             f"вузлів,\n"
                                                             f"{red_circle_sign}супутні шкірні висипання,\n"
                                                             f"{red_circle_sign}появу головного болю, болю у вухах, "
                                                             f"животі, грудній клітці,\n"
                                                             f"{red_circle_sign}лихоманку (вище 39 градусів), "
                                                             f"різку загальну слабкість, нездужання, блювання,\n"
                                                             f"{red_circle_sign}ви вагітні (жінкам)?"),
    (sore_throat_states_dict["SORE_THROAT_REASON"], "Ні"): (conversation_states_dict["DONE"],
                                                            f"Необхідно звернутися до лікаря "
                                                            f"для уточнення діагнозу"),
    (sore_throat_states_dict["SORE_THROAT_SYMPTOMS"], "Так"): (conversation_states_dict["DONE"],
                                                               f"Необхідно звернутися до лікаря "
                                                               f"для уточнення діагнозу"),
    (sore_throat_states_dict["SORE_THROAT_SYMPTOMS"], "Ні"): (sore_throat_states_dict["SORE_THROAT_DIABETES"],
                                                              f"Чи хворієте ви на цукровий діабет?"),
    (sore_throat_states_dict["SORE_THROAT_DIABETES"], "Ні"): (conversation_states_dict["DONE"],
                                                              f"Вам можна рекомендувати препарати для симптоматичного "
                                                              f"лікування болю в горлі (таблетки, льодяники для "
                                                              f"розсмоктуваання, аерозолі, спреї, розчини та ін.). "
                                                              f"Сучасні комплексні препарати на основі "
                                                              f"фітонірингових технологій"),
    (sore_throat_states_dict["SORE_THROAT_DIABETES"], "Так"): (conversation_states_dict["DONE"],
                                                               f"Вам можна рекомендувати препарати у спеціальних "
                                                               f"лікарських формах для розсмоктування для хворих "
                                                               f"із цукровим діабетом, таблетки, аерозолі, спреї, "
                                                               f"полоскання без вмісту цукру")

}
transitions_dict['Біль у горлі'] = sore_throat_dict


# Cough states
cough_states_str = ["COUGH_LASTING", "COUGH_DRY", "COUGH_SMOKING", "COUGH_SYMPTOMS",
                    "COUGH_SORE_THROAT", "COUGH_FLU", "COUGH_ITCH", "COUGH_IRRITATION"]
cough_states_dict = dict(zip(cough_states_str, range(9, 17)))

# Stress states
stress_states_str = ["STRESS_COMPLICATIONS", "STRESS_SYMPTOMS", "STRESS_REASONS", "STRESS_MEDICINES"]
stress_states_dict = dict(zip(stress_states_str, range(17, 21)))
