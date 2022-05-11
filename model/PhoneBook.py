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

        def getContacts(self):
            for contact in self.contacts:
                text = f"({contact.name}, {contact.lastname}, {contact.number}"
                print(text)


