# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def problem1(file_name):
    file = open(file_name, "r")
    nb_loop = int(file.readline())
    lines = file.readlines()
    while (nb_loop != 0):
        parms = lines.pop(0).split(' ')
        nb_elem = int(parms[0])
        amount = int(parms[1])
        elems = lines.pop(0).split(' ')
        if elems[len(elems) - 1] == '\n':
            elems.pop()
        elems = sorted(list(map(int, elems)))
        possible = True
        res = []
        print(f'amount = {amount}')
        for i in elems:
            if ((amount - i) >= 0):
                res.append(i)
                amount -= i
            else:
                continue
        print(elems)
        print(f' res = {res}')
        verif = 0
        for i in res:
            verif += i
        print(f'verif = {verif}')
        nb_loop -= 1


def problem2(file_name: str):  # TODO to redo with the prof's version
    file = open(file_name, "r")
    h = int(file.readline())
    lines = file.readlines()
    tab = []
    print(len(tab))
    mod = 123456789
    tab.append(1)
    tab.append(1)
    tab.append(2)
    for i in range(2, file.readlines()):
        tab.append((tab[i - 1] + tab[i - 2]) % mod)
    print(tab)


def problem3(file_name: str): #TODO ne maaaaarche paaaaaas, le tri du fichier marche
    file = open(file_name, "r")
    nb_test = int(file.readline())
    lines = file.readlines()
    res = {}
    result = []
    for i in range(0, nb_test):
        tab = list(map(int,lines.pop(0).split(' ')))
        nb_distributeurs = tab[0]
        nb_objects = tab[1]
        amount_euro = tab[2]
        print(f'nb_dist = {nb_distributeurs}, nb_objects = {nb_objects}, amount = {amount_euro}')
        distributeurs = {}
        for j in range(0,nb_distributeurs):
            objects = list(map(int,lines.pop(0).split(' ')))
            distributeurs[j] = objects
        res[i] = distributeurs
        print(res[i])
        print('')
    print(res)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    # problem1("small_input.txt")
    # problem1("test100.txt")
    # problem1("test100000.txt")
    # problem2("inputs.txt")
    #problem3("small_input_problem3.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
