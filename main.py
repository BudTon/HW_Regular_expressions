import csv
import re

def read_file(name_file):
    with open(name_file, encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list

# Task 1
def rename(contacts_list):
    contacts_list_rename = []
    contacts_list_rename.append(contacts_list[0])
    pattern = r'\w+'
    for contact in contacts_list:
        if contact != contacts_list[0]:
            for n in range(3):
                result_name = re.findall(pattern, contact[n])
                if len(result_name) > 1 and n < 2:
                    for el in range(len(result_name)):
                        contact[el+n] = result_name[el]
                elif len(result_name) > 1 and n == 2:
                    for el in range(len(result_name)):
                        contact[el+1] = result_name[el]
            contacts_list_rename.append(contact)
    contacts_list_rename_sorted = sorted(contacts_list_rename)
    return contacts_list_rename_sorted

# Task 3
def removing_duplicates(contacts_list_rename_sorted):
    finish_contacts_list = []
    finish_contacts_list.append(contacts_list_rename_sorted[0])
    i = 1
    while i < len(contacts_list_rename_sorted):
        if (i != len(contacts_list_rename_sorted)-1
                and contacts_list_rename_sorted[i][0] == contacts_list_rename_sorted[i + 1][0]
                and contacts_list_rename_sorted[i][1] == contacts_list_rename_sorted[i + 1][1]):
            for j in range(len(contacts_list_rename_sorted[i])):
                if contacts_list_rename_sorted[i][j] != contacts_list_rename_sorted[i+1][j] and contacts_list_rename_sorted[i+1][j] != '':
                    contacts_list_rename_sorted[i][j] = contacts_list_rename_sorted[i+1][j]
            finish_contacts_list.append(contacts_list_rename_sorted[i])
            i += 2
        else:
            finish_contacts_list.append(contacts_list_rename_sorted[i])
            i += 1
    return finish_contacts_list

# Task 2
def format_phone_number(finish_contacts_list):
    pattern = r"(\+7|8)?[\s*]?[(]?(\d{3})[)]?[-\s*]?(\d{3})[-\s*]?(\d{2})[-\s*]?(\d{2})[\s*]?[(]?(доб.)?\s*(\d{4})?[)]?"
    for contact in finish_contacts_list:
        if 'доб.' in contact[5]:
            substitute = r"+7(\2)\3-\4-\5 \6\7"
        else:
            substitute = r"+7(\2)\3-\4-\5"
        result = re.sub(pattern, substitute, contact[5])
        contact[5] = result
    return finish_contacts_list


def writing_to_a_file(format_finish_contacts_list):
    with open("phonebook.csv", "w", encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(format_finish_contacts_list)


if __name__ == '__main__':
    name_file = 'phonebook_raw.csv'
    contacts_list = read_file(name_file)
    contacts_list_rename_sorted = rename(contacts_list)
    finish_contacts_list = removing_duplicates(contacts_list_rename_sorted)
    format_finish_contacts_list = format_phone_number(finish_contacts_list)
    writing_to_a_file(format_finish_contacts_list)
    for cont in format_finish_contacts_list:
        print(cont)




