from points_class import Points


while True:
    word = input('Please enter a word to calcuate your score. Enter "0" if you would like to exit.')
    if word == str(0):
        break
    points_object = Points()
    print(f'The word "{word}" yielded you {points_object.count_score(word)} points. Well done!')
    continue
