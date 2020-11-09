# importing the Scrabble class
from scrabble_class import Scrabble

# creating a points class to contain point-counting method
class Points(Scrabble):
    # initialising this child class
    def __init__(self):
        super().__init__()
    

    # this function creates and increases a score based on which list each character falls into
    def count_score(self, string_input):
        score = 0 
        for letter in string_input.upper():
            # control flow for each letter
            if letter in self.one_point:
                score += 1 
            elif letter in self.two_point:
                score += 2
            elif letter in self.three_point:
                score += 3
            elif letter in self.four_point:
                score += 4
            elif letter in self.five_point:
                score += 5
            elif letter in self.eight_point:
                score += 8 
            elif letter in self.ten_point:
                score += 10 
            # if they enter a character that is not allowed, they get penalised
            else:
                score = 0
                return 'You have entered an invalid character, please try again.'
        return score

# #testing that the class works
# word = Points()
# input = 'words'
# print(word.count_score(input))
# print(input)