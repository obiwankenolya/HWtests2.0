documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;

def get_document_owner(people):
    user_input = input('Введите номер документа: ')
    name = 0
    for person in people:
        if user_input == person['number']:
            name += 1
            print(person['name'])
    if name == 0:
        print('Документ не найден')


# get_document_owner(documents)


# l– list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";

def get_documents_info(people):
    info = []
    for person in people:
        person_info = []
        person_info.append(person["type"])
        person_info.append(person["number"])
        person_info.append(person["name"])
        info.append(person_info)
    return info


# get_documents_info(documents)


# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;

def get_shelf_number_by_document_number(shelves):
    shelf = 0
    user_input = input('Введите номер документа: ')
    for shelf_num, document in shelves.items():
        if user_input in document:
            shelf += 1
            print(shelf_num)
    if shelf == 0:
        print('Документ не найден ни на одной из полок')


# get_shelf_number_by_document_number(directories)


# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца
# и номер полки, на котором он будет храниться.

def add_document_and_shelf():
    doc_num = input('Введите номер документа: ')
    doc_type = input('Введите тип документа: ')
    owners_name = input('Введите имя владельца документа: ')
    shelf_num = input('Введите номер полки: ')
    documents.append({"type": doc_type, "number": doc_num, "name": owners_name})
    if shelf_num in directories.keys():
        directories[shelf_num].append(doc_num)
    else:
        directories[shelf_num] = list()
        directories[shelf_num].append(doc_num)
    print(documents)
    print()
    print(directories)


# add_document_and_shelf()

def main():
    user_input = input('Введите команду: ')
    if user_input == 'p':
        get_document_owner(documents)
    elif user_input == 'l':
        get_documents_info(documents)
    elif user_input == 's':
        get_shelf_number_by_document_number(directories)
    elif user_input == 'a':
        add_document_and_shelf()
    else:
        print('Несуществующая команда')


# main()
