import re


class ValidCarNumber:

    def __init__(self, number = input('Введите номер:')):
        self.number = number

    def isvalid(self):
        is_valid = re.search(r"([0-9]{2})KG([0-9]{3})([A-Z]{3})", self.number)
        try:
            if self.number[is_valid.start():is_valid.end()] == self.number:
                return 'Is Valid number '
        except:
            return 'Is Invalid number!'


number = ValidCarNumber()
print(number.isvalid())

