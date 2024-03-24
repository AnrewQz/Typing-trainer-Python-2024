class Checker:

    def __init__(self, text):
        self.number_of_written_symbols = 0
        self.text = text

    def is_correct(self, event):
        if self.number_of_written_symbols == len(self.text) or\
                event.char != self.text[self.number_of_written_symbols]:
            return "break"
        self.number_of_written_symbols += 1
