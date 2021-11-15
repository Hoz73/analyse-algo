import math


class Drone:
    power = 0


class Ville:
    cord_x: int = 0
    cord_y: int = 0
    id = None


class Node:
    nom = None
    voisins = []


class Arbre:
    racine = None
    nodes = []


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
    result = {'addresses': addresses, 'nb_villes': id}
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
    res = []
    voisins = [''] * nb_villes
    tab_pointeur = [None] * nb_villes
    for i in villes:
        plus_grand = max(i['ville_a'], i['ville_b'])
        plus_petit = min(i['ville_a'], i['ville_b'])
        if (tab_pointeur[plus_grand] == plus_petit and tab_pointeur[plus_grand] is not None) or \
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
            voisins[i["ville_a"]] = voisins[i["ville_a"]] + str(i["ville_b"]) + "/"
            voisins[i["ville_b"]] = voisins[i["ville_b"]] + str(i["ville_a"]) + "/"
            res.append(i)

    for i in range(0, len(res)):
        print(f' ville_a : {res[i]["ville_a"]}, '
              f'ville_b : {res[i]["ville_b"]},'
              f' distance: {res[i]["distance"]}')
    print("***********************")
    arbre = creer_arbre(voisins)
    visited = [None] * nb_villes
    result = []
    parcour_profondeur(res, arbre, 0, visited, result)
    print(result)


def creer_arbre(voisins):
    arbre = Arbre()
    arbre.racine = 0
    for i in range(0, len(voisins)):
        node = Node()
        node.voisins = []
        node.nom = i
        elem = voisins[i].split(('/'))
        for j in range(0, len(elem) - 1):
            node.voisins.append(elem[j])
        arbre.nodes.append(node)
    return arbre



def parcour_profondeur(res, arbre: Arbre, racine, visited, result):
    if None in visited:
        if visited[racine] is None:
            result.append(racine)
            visited[racine] = 'visited'
            for i in range(0, len(arbre.nodes[racine].voisins)):
                parcour_profondeur(res, arbre, int(arbre.nodes[racine].voisins[i]), visited, result)


if __name__ == '__main__':
    problem_one('Cities10.txt')
