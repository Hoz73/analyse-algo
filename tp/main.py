from question_one import problem_one
from question_two import min_livraison_plusieurs_villes
from question_two import problem_two

if __name__ == '__main__':
    # question 1 :
    # problem_one('Cities10.txt')

    # question 2 :
    villes = [1,2,3,4,5,6,7]
    start = 0
    end = 9
    # res = min_livraison_plusieurs_villes(start, end, villes)
    # print(res)
    problem_two(start, end, villes)
