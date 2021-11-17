from question_one import get_distance
from question_one import distances_between_cities

file_name = 'Cities10.txt'
VILLES, res = distances_between_cities(file_name)
NB_VILLE = res['nb_villes']


def print_villes():
    for i in VILLES:
        print(i)


def min_livraison(start, end, villes = None):
    if villes is None:
        print(f'the distance between {start} and {end} is {get_distance(VILLES, start, end)}')
    else:
        min_distance = get_distance(VILLES, start, villes[0]) + get_distance(VILLES, villes[0], end)
        chosen_city = villes[0]
        print(
            f'distance from {start} passing by {villes[0]} tel {end} is :'
            f' {get_distance(VILLES, start, villes[0]) + get_distance(VILLES, villes[0], end)}')
        for i in range(1, len(villes)):
            new_disance = get_distance(VILLES, start, villes[i]) + get_distance(VILLES, villes[i], end)
            if new_disance < min_distance:
                min_distance = new_disance
                chosen_city = villes[i]
            print(
                f'distance from {start} passing by {villes[i]} tel {end} is :'
                f' {get_distance(VILLES, start, villes[i]) + get_distance(VILLES, villes[i], end)}')
        print(f'the minimal distance is to pass by {chosen_city}')
        print(
            f'you start at {start}, you pass by {chosen_city} with distance {get_distance(VILLES, start, chosen_city)}'
            f' and you finish at {end} with a total distance {min_distance} ')
