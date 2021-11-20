from itertools import permutations
from question_one import distances_between_cities
from question_one import get_distance

file_name = 'Cities10.txt'
VILLES, nb_villes = distances_between_cities(file_name)
NB_VILLE = nb_villes

VILLES_CALCULEES = []


# complexity O(size(n)) worst scenario
# complexity O(1) best scenario
def min_livraison_non_ville(start, end):
    distance = get_distance(VILLES, start, end)
    print(f'the distance between {start} and {end} is {distance}')
    return {'start': start, 'end': end, 'passing_by': [], 'distance': distance}


# complexity O(size(n)) worst scenario
# complexity O(1) best scenario
def min_livraison_une_ville(start, end, villes):
    min_distance = get_distance(VILLES, start, villes[0]) + get_distance(VILLES, villes[0], end)
    print(
        f'you start at {start}, you pass by {villes[0]} with distance {get_distance(VILLES, start, villes[0])}'
        f' and you finish at {end} with a total distance {min_distance} ')
    return {'start': start, 'end': end, 'passing_by': [villes[0]], 'distance': min_distance}


# complexity O(n log n)
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

# complexity factorial
def min_livraison_plusieurs_villes(start, end, villes):
    if len(villes) == 1:
        print(start, end, villes)
        result = check_if_calculated(start, end, villes)  # O(n log n)
        if result is not None:
            print(f'already exist : {result}')
            return result['distance']
        else:
            result = min_livraison_une_ville(start, end, villes)  # O(size(n))
            VILLES_CALCULEES.append(result)
            print(f'{result}')
            return result['distance']
    else:
        result = check_if_calculated(start, end, villes) # O(n log n)
        if result is not None:
            distance = result['distance']
        else:
            res = min_livraison_non_ville(villes[-1], end) # O(size(n))
            VILLES_CALCULEES.append(res)
            distance = res['distance']
        print(f'start : {start}, end : {end}, villes :{villes}')
        print(f'start : {start}, end : {villes[-1]}, villes :{villes[0:-1]}')
        return distance + min_livraison_plusieurs_villes(start, villes[-1], villes[0:-1])


# Complexity factorial
def problem_two(start, end, villes):
    if len(villes) == 0:
        return min_livraison_non_ville(start, end)
    result = list(permutations(villes))
    final_reults = []
    cities = []
    for villes in result:
        v = []
        for ville in villes:
            v.append(ville)
        cities.append(v)
    for tab in cities:
        res = min_livraison_plusieurs_villes(start, end, tab)
        final_reults.append({
            'start': start,
            'end': end,
            'ordre_passing_by': tab,
            'distance': res
        })
    print('##########################')
    min_result = min(final_reults, key=lambda x: x['distance'])
    print(f'and the minimal distance is {min_result["distance"]}, by passing by {min_result["ordre_passing_by"]}')
