import random
from enum import Enum
from typing import Generator


class Gender(Enum):
    MALE = 'male'
    FEMALE = 'female'
    UNKNOWN = 'unknown'


GENDER_THRESHOLDS = {
    'gender unknown': 255,
    'female': 254,
    'male_to_female_1_7': 225,
    'male_to_female_1_3': 191,
    'male_to_female_1_1': 127,
    'male_to_female_3_1': 63,
    'male_to_female_7_1': 31,
    'male': 0
}


NATURES = {
    'hardy': 0, 'lonely': 1, 'brave': 2, 'adamant': 3, 'naughty': 4,
    'bold': 5, 'docile': 6, 'relaxed': 7, 'impish': 8, 'lax': 9,
    'timid': 10, 'hasty': 11, 'serious': 12, 'jolly': 13, 'naive': 14,
    'modest': 15, 'mild': 16, 'quiet': 17, 'bashful': 18, 'rash': 19,
    'calm': 20, 'gentle': 21, 'sassy': 22, 'careful': 23, 'quirky': 24
}


def random_pid(tid: int, sid: int, shiny_only: bool, square_only: bool, star_only: bool) -> Generator[int, None, None]:
    if not shiny_only:
        threshold_range = (0x0, 0xFFFF)
    elif square_only:
        threshold_range = (0, 0)
    elif star_only:
        threshold_range = (1, 7)
    else:
        threshold_range = (0, 7)
    while True:
        pid_upper = random.randint(0x0, 0xFFFF)
        threshold = random.randint(*threshold_range)
        pid_lower = tid ^ sid ^ pid_upper ^ threshold
        yield pid_upper << 16 | pid_lower


def read_nature(pid: int) -> str:
    LOOKUP_TABLE = {v: k for k, v in NATURES.items()}
    return LOOKUP_TABLE[pid % 25]


def read_ability(pid: int) -> int:
    return pid & 1


def read_gender(pid: int, gender_threshold: int) -> Gender:
    encoded_gender = pid % 256
    LOOKUP_TABLE = {v: k for k, v in GENDER_THRESHOLDS.items()}
    if LOOKUP_TABLE.get(gender_threshold) == 'male':
        return Gender.MALE
    if LOOKUP_TABLE.get(gender_threshold) == 'female':
        return Gender.FEMALE
    if LOOKUP_TABLE.get(gender_threshold) == 'gender unknown':
        return Gender.UNKNOWN
    if encoded_gender >= gender_threshold:
        return Gender.MALE
    else:
        return Gender.FEMALE


def id_prompt(prompt: str) -> int:
    while True:
        try:
            id_number = int(input(prompt))
        except ValueError:
            print("Invalid value entered.")
            continue
        if not 0 <= id_number <= 65535:
            print("Invalid value entered.")
            continue
        else:
            return id_number


def natures_prompt() -> str:
    while True:
        nature = input("Nature: ").strip().lower()
        if nature in NATURES:
            return nature
        elif not nature:
            return ""
        else:
            print("Not a nature.")
            continue


def gender_ratio_prompt() -> int:
    OPTIONS = {
        7: 'gender unknown',
        6: 'female',
        5: 'male_to_female_1_7',
        4: 'male_to_female_1_3',
        3: 'male_to_female_1_1',
        2: 'male_to_female_3_1',
        1: 'male_to_female_7_1',
        0: 'male'
    }
    print(f"""Choose gender ratio (♂:♀)
Male - 0
7:1 - 1
3:1 - 2
1:1 - 3
1:3 - 4
1:7 - 5
Female - 6
Gender unknown - 7\
""")
    while True:
        answer = input("Option: ") or "7"
        try:
            choice = int(answer)
        except ValueError:
            print("Invalid value entered.")
            continue
        if not choice in OPTIONS:
            print("Invalid value entered.")
            continue
        else:
            return GENDER_THRESHOLDS[OPTIONS[choice]]


def gender_prompt(gender_ratio) -> Gender:
    if gender_ratio == GENDER_THRESHOLDS['male']:
        return Gender.MALE
    if gender_ratio == GENDER_THRESHOLDS['female']:
        return Gender.FEMALE
    if gender_ratio == GENDER_THRESHOLDS['gender unknown']:
        return Gender.UNKNOWN
    while True:
        wanted_gender = input("Male (M) or Female (F)? ").strip().lower()
        if wanted_gender == "M":
            return Gender.MALE
        if wanted_gender == "F":
            return Gender.FEMALE
        print("Invalid value entered.")
        continue


def ability_prompt() -> int | None:
    while True:
        option = input("Ability (0/1): ") or ""
        try:
            if option:
                answer = int(option)
        except ValueError:
            print("Invalid value entered.")
            continue
        if option == "":
            return None
        if answer == 0:
            return 0
        if answer == 1:
            return 1
        print("Invalid value entered.")
        continue


def shiny_prompt() -> bool:
    while True:
        answer = input("Search for shinies only? (Y/n)").strip().lower() or "y"
        if answer == "y":
            return True
        if answer == "n":
            return False
        print("Invalid value entered.")
        continue


def shiny_type_prompt() -> tuple[bool, bool]:
    print(f"""Choose shiny type:
Square - 0
Star - 1
Star/Square - 2\
""")
    while True:
        option = input("Option: ") or "2"
        try:
            answer = int(option)
        except ValueError:
            print("Invalid value entered.")
            continue
        if answer == 0:
            return (True, False)
        if answer == 1:
            return (False, True)
        if answer == 2:
            return (False, False)
        print("Invalid value entered.")
        continue


def main() -> None:
    tid = id_prompt("TID: ")
    sid = id_prompt("SID: ")
    nature = natures_prompt()
    ability = ability_prompt()
    gender_ratio = gender_ratio_prompt()
    gender = gender_prompt(gender_ratio)
    shiny_only = shiny_prompt()
    if shiny_only:
        square_only, star_only = shiny_type_prompt()
    pids = random_pid(tid, sid, shiny_only, square_only, star_only)
    for pid in pids:
        if nature != read_nature(pid) and nature:
            continue
        if ability != read_ability(pid) and ability:
            continue
        if gender is not read_gender(pid, gender_ratio):
            continue
        found_pid = pid
        break
    print(f"""A PID has been found!
TID/SID: {tid:05d}/{sid:05d}
PID: {found_pid:08X}
Gender: {read_gender(found_pid, gender_ratio).name.title()}
Nature: {read_nature(found_pid).title()}
Ability: {read_ability(found_pid)}""")


if __name__ == "__main__":
    main()