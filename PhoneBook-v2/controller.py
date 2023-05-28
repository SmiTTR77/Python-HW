import view
import model
import text


def start():
    while True:
        choise = view.main_menu()
        match choise:
            case 1:
                # открыть файл
                model.open_pb()
                view.print_message(text.load_succesful)
            case 2:
                # записать файл
                model.save_pb()
                view.print_message(text.save_succesful)
            case 3:
                # показать контакт
                pb = model.get_pb()
                view.print_contact(pb, text.load_error)
            case 4:
                # добавить контакт
                contact = view.input_contact(
                    text.new_contact, text.cancel_input)
                name = model.add_contact(contact)
                view.print_message(text.new_contact_succesful(name))
            case 5:
                # найти контакт
                pb = model.get_pb()
                fl = view.find_contact(pb)
                view.print_contact(fl, text.find_error)
            case 6:
                # изменить контакт
                pb = model.get_pb()
                index = view.input_index(
                    text.index_change_contact, pb, text.load_error)
                change_contact = view.input_contact(
                    text.new_change_contact, text.cancel_input)
                name = model.change_contact(index, change_contact)
                view.print_message(text.change_contact(name))
            case 7:
                # удалить контакт
                pb = model.get_pb()
                index = view.input_index(
                    text.index_del_contact, pb, text.load_error)
                name = model.del_contact(index)
                view.print_message(text.del_contact(name))
            case 8:
                # выход
                break
