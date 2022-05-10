class Contact:
    def __init__(self, name, lastname, number,):
        self.name = name
        self.lastname = lastname
        self.number = number

    def __str__(self):
        return self.name + " " + self.lastname + " " + self.number
