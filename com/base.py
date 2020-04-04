# birthdays = {
#     "John": "01/01/1992",
#     "Peter": "22/04/1992",
#     "Mark": "11/11/1982",
#     "Darcy": "21/08/1987",
#     "Jane": "12/06/1999",
#     "Kevin": "18/01/1972"
# }
import json

directory_path = "/tmp/Birthday/birthday.txt"


class BirthdayDiary:

    def add_entry(self, name, date):
        birthdays = self.get_data_from_file()
        birthdays[name] = date
        print("The name :{} and his birthday {} has been successfully added".format(name, date))
        self.send_data_to_file(birthdays)

    def delete_entry(self, name):
        birthdays = self.get_data_from_file()
        if name in birthdays.keys():
            birthdays.pop(name, None)
            print("Birth day details have been updated/deleted as requested \n")
            self.send_data_to_file(birthdays)
        else:
            print("Entered name :{} not found inside the diary ".format(name))

    def list_entries(self):
        """ Printing all the entries from Birthday diary"""
        birthdays = self.get_data_from_file()
        for key in birthdays:
            print("Name :{}\t\tBirth Date:{}".format(key, birthdays[key]))

    def get_data_from_file(self):
        with open(directory_path) as file_data:
            file_content = file_data.read()
            json_content = json.loads(file_content)
            return json_content

    def send_data_to_file(self, input_dict):
        with open(directory_path, 'w') as to_data:
            to_data.write(str(json.dumps(input_dict)))
            print("Done writing details to file")


# diary = BirthdayDiary()
# # diary.list_entries()
# # diary.send_data_to_file()
# # diary.get_data_from_file()
#
# # diary.add_entry("Tom", "14/02/2000")
# diary.list_entries()
#
# diary.delete_entry('Tom')
# diary.list_entries()
