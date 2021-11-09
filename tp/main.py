# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math


class Drone:
    power = 0


class CartePostal:
    address = 0
    km = 0


class Ville:
    cord_x: int = 0
    cord_y: int = 0
    id = None
    voisins = []


def distance(ville_a: Ville, ville_b: Ville) -> float:
    return math.sqrt(pow(ville_b.cord_x - ville_a.cord_x, 2) + pow(ville_b.cord_y - ville_a.cord_y, 2))


def read_cities(file_name):
    file = open(file_name, "r")
    addresses = []
    id = 0
    for line in file.readlines():
        address = line.split(' ')
        ville: Ville = Ville()
        ville.cord_x = int(address[1])
        ville.cord_y = int(address[2].split('\n')[0])
        ville.id = id
        id += 1
        addresses.append(ville)
    result = {'addresses': addresses, 'nb_villes' : id}
    return result


def problem_one(file_name):
    res = read_cities(file_name)
    villes = res['addresses']
    villes_calculees = []

    for ville_a in villes:
        for ville_b in villes:
            if ville_a is not ville_b:
                villes_calculees.append(
                    {'ville_a': ville_a.id,
                     'ville_b': ville_b.id,
                     'distance': distance(ville_a, ville_b)})

    villes_calculees = sorted(villes_calculees, key=lambda dct: dct['distance'])
    result = []
    for i in range(0, len(villes_calculees)):
        if i % 2 == 0:
            result.append(villes_calculees[i])
    kruskal(result, res['nb_villes'])


def kruskal(villes, nb_villes):
    res_a = []
    res_b = []
    res = []
    tab_pointeur = [None] * nb_villes
    for element in villes:
        plus_grand = max(element['ville_a'], element['ville_b'])
        plus_petit = min(element['ville_a'], element['ville_b'])
        if (tab_pointeur[plus_grand] == plus_petit and tab_pointeur[plus_grand] is not None) or\
                (tab_pointeur[plus_grand] == tab_pointeur[plus_petit] and tab_pointeur[plus_grand] is not None):
            pass
        else:
            if tab_pointeur[plus_grand] is None:
                if tab_pointeur[plus_petit] is None:
                    tab_pointeur[plus_grand] = plus_petit
                    tab_pointeur[plus_petit] = plus_petit
                else:
                    tab_pointeur[plus_grand] = plus_petit
                if tab_pointeur[plus_petit] is not None:
                    tab_pointeur[plus_grand] = tab_pointeur[plus_petit]
            else:
                if tab_pointeur[plus_petit] is None:
                    tab_pointeur[plus_petit] = tab_pointeur[plus_grand]
                else:

                    min_p = min(tab_pointeur[plus_grand], tab_pointeur[plus_petit])
                    max_p = max(tab_pointeur[plus_grand], tab_pointeur[plus_petit])
                    index = tab_pointeur[plus_grand]
                    for val in range(0, len(tab_pointeur)):
                        if tab_pointeur[val] == max_p:
                            tab_pointeur[val] = min_p
                    tab_pointeur[index] = min_p
    print(tab_pointeur)
        # if (element['ville_a'] not in res_a) or (element['ville_b'] not in res_a):
        #     res_a.append(element['ville_a'])
        #     res_a.append(element['ville_b'])
        #     res.append(element)
            # print(f' ville_a : {element["ville_a"]}, '
            #       f'ville_b : {element["ville_b"]},'
            #       f' distance: {element["distance"]}')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    problem_one('Cities10.txt')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
