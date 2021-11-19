from question_one import problem_one
from question_two import problem_two

if __name__ == '__main__':
    print(" 1 - first question \n"
          " 2 - second question")
    choix = input("chose your exercise : ")
    if choix == '1':
        # question 1 :
        problem_one('Cities10.txt')
    elif choix == '2':
        # question 2 :
        villes = [1, 2, 3, 4, 5]
        start = 0
        end = 9
        problem_two(start, end, villes)
    else:
        print('invalid choice')
