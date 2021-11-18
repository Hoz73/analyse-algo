from question_one import get_distance
from question_one import distances_between_cities
from math import factorial
from itertools import combinations
from itertools import permutations

file_name = 'Cities10.txt'
VILLES, res = distances_between_cities(file_name)
NB_VILLE = res['nb_villes']

VILLES_CALCULEES = []


def print_villes():
    for i in VILLES:
        print(i)


def min_livraison_non_ville(start, end):
    distance = get_distance(VILLES, start, end)
    print(f'the distance between {start} and {end} is {distance}')
    return {'start': start, 'end': end, 'passing_by': [], 'distance': distance}


def min_livraison_une_ville_OK(start, end, villes):
    min_distance = get_distance(VILLES, start, villes[0]) + get_distance(VILLES, villes[0], end)
    print(
        f'you start at {start}, you pass by {villes[0]} with distance {get_distance(VILLES, start, villes[0])}'
        f' and you finish at {end} with a total distance {min_distance} ')
    return {'start': start, 'end': end, 'passing_by': [villes[0]], 'distance': min_distance}


def min_livraison_une_ville(start, end, villes):
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
    return {'start': start, 'end': end, 'villes': chosen_city}


def check_if_calculated(start, end, villes):
    for element in VILLES_CALCULEES:
        if len(element['passing_by']) == len(villes):
            if element['start'] == start and element['end'] == end:
                flag = True
                for i in range(0, len(element['passing_by'])):
                    if element['passing_by'][i] != villes[i]:
                        flag = False
                if flag:
                    return element
    return None


def min_livraison_plusieurs_villes(start, end, villes):
    if len(villes) == 1:
        print(start,end,villes)
        result = check_if_calculated(start, end, villes)
        if result is not None:
            print(f'already exist : {result}')
            return result['distance']
        else:
            result = min_livraison_une_ville_OK(start, end, villes)
            VILLES_CALCULEES.append(result)
            print(f'{result}')
            return result['distance']
    else:
        result = check_if_calculated(start, end, villes)
        if result is not None:
            distance = result['distance']
        else:
            res = min_livraison_non_ville(villes[-1], end)
            VILLES_CALCULEES.append(res)
            distance = res['distance']
        print(start, end , villes)
        print(start, villes[-1] , villes[0:-1])
        return distance + min_livraison_plusieurs_villes(start, villes[-1], villes[0:-1])

def problem_two(start,end,villes):
    result = list(permutations(villes))
    final_reults = []
    cities = []
    for villes in result:
        v=[]
        for ville in villes:
            v.append(ville)
        cities.append(v)
    len(cities)
    for tab in cities:
        res = min_livraison_plusieurs_villes(start, end, tab)
        final_reults.append({
            'start': start,
            'end' : end,
            'ordre_passing_by': tab,
            'distance': res
        })
    print('##########################')
    min_result = min(final_reults,key=lambda x:x['distance'])
    print(f'and the minimal distance is {min_result["distance"]}, by passing by {min_result["ordre_passing_by"]}')
