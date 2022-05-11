from model.Contact import Contact


class PhoneBook:
        def __init__(self):
            self.contacts = list()

        def __str__(self):
            return ", ".join(str(contact) for contact in self.contacts)

        def addContact(self, name, lastname, number):
            self.contacts.append(Contact(name, lastname, number))

        def deleteContact(self, position):
            self.contacts.pop(position)

        def contactList(self):
            return "(" + str(self) + ")"

        def searchContact(self, key):
            for contact in self.contacts:
                if contact.name == key or contact.lastname == key or contact.number == key :
                    return str(contact)

