import sys


class Contact(object):

    def __init__(self, name: str, phonenumber: str, email: str, notes: str):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email
        self.notes = notes

    def __str__(self):
        return self.name + self.phonenumber + self.email + self.notes

    def updateName(self, newName):
        self.name = newName

    def updatePhonenumber(self,newPhonenumber):
        self.name=newPhonenumber

    def updateEmail(self,newEmail):
        self.email=newEmail

    def updateNotes(self,newNotes):
        self.notes=newNotes



def loadFile():
    try:
        with open('contactFile.txt',"r") as fp:
            for line in fp:
                if line.strip():
                    txt = line.split(";")
                    person.append(Contact(txt[0], txt[1], txt[2], txt[3]))
    except FileNotFoundError:
        print('This file does not exist')


person = []


def showContact():
    print("List of contacts: ")
    for p in person:
        # print("* " + str(p))
        print(p.name + ";" + p.phonenumber + ";" + p.email + ";" + p.notes)
    print('---end---')
    startMenu()


def addContact():
    print("Enter name: ")
    new_name = sys.stdin.readline().rstrip()
    print("Enter phone number: ")
    new_phonenumber = sys.stdin.readline().rstrip()
    print("Enter email: ")
    new_email = sys.stdin.readline().rstrip()
    print("Enter notes: ")
    new_notes = sys.stdin.readline().rstrip()
    person.append(Contact(new_name, new_phonenumber, new_email, new_notes))
    saveChanges()
    print("New Contact added.")
    startMenu()


def searchContact():
    print("Search for who?")
    searched_person = sys.stdin.readline().rstrip()
    for p in person:
        if searched_person == p.name:
            print("Contact found")
            print("* " + str(p))
            print('---end---')
            startMenu()



def deleteContact():
    print("Delete who?")
    delete_person = sys.stdin.readline().rstrip()
    for p in person:
        if delete_person == p.name:
            person.remove(p)
            saveChanges()
            startMenu()




def updateContact():
    print("What would you like to update? Type 'name'/'phonenumber'/'email'/'notes' to update")
    update_service = sys.stdin.readline().rstrip()

    if update_service == 'name':
        print("Who's name?")
        update_person = sys.stdin.readline().rstrip()
        for p in person:
            if update_person == p.name:
                print("Enter new name: ")
                new_name1 = sys.stdin.readline().rstrip()
                p.updateName(new_name1)
            # person.append(Contact.updateName(p.name,new_name1))
                saveChanges()
                print("New name has been updated.")
                startMenu()



    if update_service == 'phonenumber':
        print("Who's phonenumber?")
        update_phone = sys.stdin.readline().rstrip()
        for p in person:
            if update_phone == p.name:
                print("Enter new phone number: ")
                new_phone = sys.stdin.readline().rstrip()
                p.updatePhonenumber(new_phone)
                # person.append(Contact.updateName(p.name,new_name1))
                saveChanges()
                print("Phone number has been updated.")
                startMenu()


    if update_service == 'email':
        print("Who's email?")
        update_email = sys.stdin.readline().rstrip()
        for p in person:
            if update_email == p.name:
                print("Enter new email: ")
                new_email = sys.stdin.readline().rstrip()
                p.updateEmail(new_email)
                # person.append(Contact.updateName(p.name,new_name1))
                saveChanges()
                print("Email has been updated.")
                startMenu()


    if update_service == 'notes':
        print("Who's notes?")
        update_notes = sys.stdin.readline().rstrip()
        for p in person:
            if update_notes == p.name:
                print("Enter new notes: ")
                new_notes = sys.stdin.readline().rstrip()
                p.updateEmail(new_notes)
                # person.append(Contact.updateName(p.name,new_name1))
                saveChanges()
                print("Notes has been updated.")
                startMenu()


    else:
        print("Please only type in the following commands: 'name'/'phonenumber'/'email'/'notes' to update")
        updateContact()


def saveChanges():
    with open("contactFile.txt", "w") as fp:
        for p in person:
            fp.write(p.name + ";" + p.phonenumber + ";" + p.email + ";" + p.notes + "\n")


def startMenu():
    print("Hello!Welcome for using this contact list app!")
    print(
        "Type 'add' for adding a contact, 'show' for showing existing contact, 'search' for searching a contact in list, 'delete' to delete a contact,'updatecontact' to change an existing contact,'exit' to exit program. ")
    command = sys.stdin.readline().rstrip()
    if command == 'add':
        addContact()
    if command == 'show':
        showContact()
    if command == 'search':
        searchContact()
    if command == 'delete':
        deleteContact()
    if command == 'updatecontact':
        updateContact()
    if command == 'exit':
        sys.exit('Bye')
    else:
        print("No such command.")
        startMenu()

loadFile()
startMenu()
