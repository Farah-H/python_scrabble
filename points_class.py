from scrabble_class import Scrabble

class Points(Scrabble):
    def __init__(self):
        super().__init__()
    

    def count_score(self, string_input):
        score = 0 
        for letter in string_input.upper():
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
            else:
                return 'You have entered an invalid character, please try again.'
        return score

# #testing that the class works
# word = Points()
# input = 'words'
# print(word.count_score(input))
# print(input)