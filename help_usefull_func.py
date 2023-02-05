import itertools
from collections import Counter

alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                    'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                    'X': 23, 'Y': 24, 'Z': 25, 'a': 0.1, 'b': 1.1, 'c': 2.1, 'd': 3.1, 'e': 4.1, 'f': 5.1, 'g': 6.1,
                    'h': 7.1, 'i': 8.1, 'j': 9.1, 'k': 10.1, 'l': 11.1, 'm': 12.1, 'n': 13.1, 'o': 14.1, 'p': 15.1,
                    'q': 16.1, 'r': 17.1, 's': 18.1, 't': 19.1, 'u': 20.1, 'v': 21.1, 'w': 22.1, 'x': 23.1, 'y': 24.1,
                    'z': 25.1}


def check(lst, lst_length):
    """Вспомогательная функция, нужна для корректной работы функции 'f2_universal_found'
    принимает лист из нескольких гамет и длину этого листа, возвращает True/False взависимости от того,
    повторяються там гаметы или нет"""
    for i in range(0, lst_length):
        if i == lst_length - 1:
            if list(lst)[i] == list(lst)[0]:
                return False
        else:
            if list(lst)[i] == list(lst)[i + 1]:
                return False
    return True


def genetic_sort(a: list):
    """Вспомогаительная функция, которая сортирует список пар гамет так, что все ошибки в порядке букв
    убирается, возвращает готовый отсортированный список
    Принцип сортировки заключается в том, что цикл for пробегается по заранее созданному словарю alphabet и
    смотрит, какой вес имеет буква, взависимости от её веса он меняет букву местами, если нужно"""

    def bubble_sort(b: list):
        """Вспомогательная функция, производящая дополнительную сортировку методом пузырька"""
        N = len(b)

        for bypass in range(1, N):
            for k in range(0, N - bypass):
                if b[k][1] > b[k + 1][1]:
                    b[k], b[k + 1] = b[k + 1], b[k]
        return b

    s2 = []
    for j in list(a):
        for n in alphabet.keys():
            if n == j:
                s2.append((n, alphabet[j]))
    ok = []
    k = 0
    finish = bubble_sort(s2)
    for o in finish:
        ok.append(finish[k][0])
        k += 1
    h = ''.join(ok)
    return h  # list


def counter_of_repeated_gamets(list_of_one_parent_gamets: list):
    """
    Вспомотгательная функция считающая есть ли похожие буквы в списке гамет и подсчитывает их количество.
    На вход: гаметы родителя
    На выход: количество повторов, длинна общего количества разных букв
    """
    new = [i.lower() for i in list_of_one_parent_gamets if True]
    c = Counter(new)
    counter = 0
    finally_count_of_repeat_gamets = 0
    for key in c.values():
        if counter == 0 and key != 1:
            counter = key
        elif counter != 0:
            if counter == key and key != 1:
                finally_count_of_repeat_gamets = counter
            else:
                pass  # не знаю пока что тут делать
    return finally_count_of_repeat_gamets, len(c.keys())


def f2_universal_found(gamets_1: list, gamets_2: list, len_of_gamet: int):
    """
    Функция по универсальному нахождению второго поколения
    На вход: гаметы первого родителя, гаметы второго родителя, длину одного списка гамет
    На выход: список всех возможных вариантов второго поколения
    """
    all_gamets = list(set(gamets_1 + gamets_2))

    # Циклы для случая AaBb и AaBb, AaBbCc и AaBbCc и других подобных
    counter_p1, len_of_pair1 = counter_of_repeated_gamets(gamets_1)
    counter_p2, len_of_pair2 = counter_of_repeated_gamets(gamets_2)

    if counter_p1 == counter_p2 and counter_p1 != 0 and counter_p2 != 0:
        gamets = list(itertools.combinations(all_gamets, r=len_of_pair1))
    elif counter_p1 == 0 and counter_p1 == 0:
        gamets = list(itertools.combinations(all_gamets, r=len_of_gamet))

    new_gamets = []
    for i in gamets:
        pair = list(i)
        for p in pair:
            pair[pair.index(p)] = p.lower()
        if check(pair, len(pair)):
            new_gamets.append(''.join(genetic_sort(i)))
        elif not check(pair, len(pair)):
            pass

    finally_f2 = []
    for i in new_gamets:
        for j in new_gamets:
            finally_f2.append(''.join(genetic_sort(i + j)))

    finally_f2.sort()

    return finally_f2, new_gamets  # Возвращает списки


def pairs_found(f1: str, length_of_pair: int):
    """Алгоритм нахождения всех возможных пар для группы признаков"""
    pairs = []  # Временный список пар
    result = []  # Сюда поместиться финальный список пар

    # Создаём все возможные комбинации пар
    for combos in itertools.product(f1, repeat=length_of_pair):
        pairs.append(''.join(combos))

    for i in pairs:
        if len(set(list(i.lower()))) == length_of_pair:
            result.append(i)

    # Процесс финальной сортировки итогового списка
    pairs = result.copy()
    result.clear()
    for i in pairs:
        result.append(genetic_sort(i))
    result = list(set(result))
    result.sort()

    return result  # list


def universal_f2_found(f1: str, length_of_pair: int):
    """Поиск второго поколения для случаев AA и aa, AABB и aabb, и тд."""
    f2 = []
    pairs = pairs_found(f1, length_of_pair)

    for i in pairs:
        for j in pairs:
            f2.append(i + j)

    result = f2.copy()
    f2.clear()
    for i in result:
        f2.append(genetic_sort(i))
    f2.sort()

    return f2  # list