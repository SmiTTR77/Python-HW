import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        choise = input(text.input_choise)
        if choise.isdigit() and 0 < int(choise) < 9:
            return int(choise)


def print_message(message: str):
    print('\n' + '=' * len(message))
    print(message)
    print('=' * len(message) + '\n')


def print_contact(pb: list[dict[str, str]], error: str):
    if pb:
        print('\n' + '=' * 72)
        for i, contact in enumerate(pb, 1):
            print(
                f"{i :>3}. {contact.get('name'):<20} | {contact.get('phone'):<20} | {contact.get('comment'):<20}")
        print('=' * 72)
    else:
        print_message(error)


def find_contact(pb: list[dict[str, str]]):
    find_list = []
    seach_value = input(text.find_choise)
    for contact in pb:
        for value in contact.values():
            if seach_value.lower() in value.lower():
                find_list.append(contact)
    return find_list


def change_contact(pb: list[dict[str, str]], index: int):
    pass


def input_contact(message: str, cancel: str) -> dict:
    contact = {}
    print(message)
    for key, value in text.input_contact.items():
        data = input(value)
        if data:
            contact[key] = data
        else:
            print_message(cancel)
    return contact


def input_index(message: str, pb: list, error: str) -> int:
    print_contact(pb, error)
    while True:
        index = input(message)
        if index.isdigit() and 0 < int(index) < len(pb) + 1:
            return int(index)
