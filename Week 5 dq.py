class Keyboard:
    def type_text(self):
        print("Keyboard is typing...")


class Computer:
    def __init__(self):
        self.keyboard = Keyboard()

    def start_work(self):
        self.keyboard.type_text()
        print("Computer is ready for work.")


# Creating a computer object
computer = Computer()

computer.start_work()
