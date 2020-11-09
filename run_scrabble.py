# importing Points class
from points_class import Points


# While loop to keep prompting the user for a word
while True:
    word = input('Please enter a word to calcuate your score. Enter "0" if you would like to exit.')
    if word == str(0):
        break
    # instantiating the class so we can utilise the count method
    points_object = Points()

    # printing the score in a nice way for the user
    print(f'The word "{word}" yielded you {points_object.count_score(word)} points. Well done!')
    continue
