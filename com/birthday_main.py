import sys
from com import base


def main():
    # print("Welcome")
    if (len(sys.argv) == 1):
        print("Please use below keywords to use this program")
        print("for getting all the entries inside the diary Use : list")
        print("for adding an entry to the diary use:")
        # print command help
        """
        Please use below keywords to use this program
        for getting all the entries inside the diary Use : list
        for adding an entry to the diary use:
        print("No command passed")
        """
    else:
        command = sys.argv[1]
        if command == "list":
            birthday_dairy = base.BirthdayDiary()
            birthday_dairy.list_entries()
        elif command == "add" or command == "update":
            if len(sys.argv) == 4:
                name = sys.argv[2]
                date = sys.argv[3]
                birthday_dairy = base.BirthdayDiary()
                birthday_dairy.add_entry(name, date)
            else:
                print("Incorrect details provided for adding entry")
        elif command == "delete":
            if len(sys.argv) == 3:
                name = sys.argv[2]
                birthday_dairy = base.BirthdayDiary()
                birthday_dairy.delete_entry(name)
            else:
                print("Incorrect details provided for Deleting entry")
        else:
            print("Command not in the format.\n Please enter proper details next time")


if __name__ == '__main__':
    main()
