"""Версия: Python 3.6.8
"""
import itertools
import math
from collections import Counter
from home_bot.help_files import genetic_tables

def genetic_programme(parent_one: str, parent_two: str):
    """Программа, для определения количества гамет, выведения первого поколения, выведения воторого покодения
    Программа должна быть универсальной, пока что готовы только: определение первого поколения и гамет, нахождение
    второго поколения вызывает затруднение в некоторых редких случаях
    """
    status = 'normal'
    try:
        gamet_parent_one, gamet_parent_two = [], []  # гаметы первого и второго родителя
        gibrids_two = []  # result, второе поколение поколение

        # Словарь со всеми буквами англиского алфавита и их весом для корректной работы функции genetic_sorted2
        alphabet = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
                    'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21, 'W': 22,
                    'X': 23, 'Y': 24, 'Z': 25, 'a': 0.1, 'b': 1.1, 'c': 2.1, 'd': 3.1, 'e': 4.1, 'f': 5.1, 'g': 6.1,
                    'h': 7.1, 'i': 8.1, 'j': 9.1, 'k': 10.1, 'l': 11.1, 'm': 12.1, 'n': 13.1, 'o': 14.1, 'p': 15.1,
                    'q': 16.1, 'r': 17.1, 's': 18.1, 't': 19.1, 'u': 20.1, 'v': 21.1, 'w': 22.1, 'x': 23.1, 'y': 24.1,
                    'z': 25.1}

        eng_alphabet = list(alphabet.keys())
        # Проверка на то, написаны ли родители латинскими буквами
        for i in parent_one:
            if i not in eng_alphabet:
                print('Error, родители должны быть записаны латинскими буквами')
                status = 'error'
                return status
        for i in parent_two:
            if i not in eng_alphabet:
                print('Error, родители должны быть записаны латинскими буквами')
                status = 'error'
                return status

        """------------------------------------Вспомогательные функции------------------------------------"""
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
            return h # list

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

            return finally_f2, new_gamets # Возвращает списки

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
        """-----------------------------------------------------------------------------------------------"""

        # Выведение гамет первого родителя
        H = set([char for char in parent_one])
        d = ''
        for j in H:
            gamet_parent_one.append(j)
        gamet_parent_one.sort()
        for i in gamet_parent_one:
            d = f"{d}, " + str(i)
        gamet_parent_one = d[2:]

        # Выведение гамет второго родителя
        H = set([char for char in parent_two])
        d = ''
        for j in H:
            gamet_parent_two.append(j)
        gamet_parent_two.sort()
        for i in gamet_parent_two:
            d = f"{d}, " + str(i)
        gamet_parent_two = d[2:]

        # Эта переменная нужна только тогда, когда родители длиной всего две буквы, например AA и aa
        S = list(set((gamet_parent_one.replace(' ', '').replace(',', ''))
                     + (gamet_parent_two.replace(' ', '').replace(',', ''))))

        if len(gamet_parent_one) == len(gamet_parent_two): # проверяет, одинаковое ли количество гамет у разных
            # родителей
            gibrids_one = ''.join(S)
            num = 0

            # подразумеваеться что в родителях количество гамет равное
            """---Алгоритм нахождения второго поколения"""
            gamets_1 = list((gamet_parent_one.replace(' ', '').replace(',', '')))
            gamets_2 = list((gamet_parent_two.replace(' ', '').replace(',', '')))

            if len(S) <= 2:
                for j in S:  # Нахождение пар для второго поколения(если родители состоят из 2 букв)
                    gibrids_two.append(j + S[num])
                    gibrids_two.append(j + S[num + 1])
            elif len(S) >= 4:  # Нахождение пар для второго поколения(если родители состоят из 4 букв)
                gibrids_two, pairs = f2_universal_found(gamets_1, gamets_2, len(gamets_1))
            d = ''
            gibrids_two.sort()

            # Финальный алгоритм сортировки готовых гамет второго поколения
            x = False
            num = 0
            result = []
            while not x:
                if num >= len(gibrids_two):
                    break
                elif num < len(gibrids_two):
                    z = genetic_sort(gibrids_two[num])
                    result.append(z)
                    num += 1

            for i in result:
                d = f"{d}, " + str(i)

            if parent_one == parent_two:
                if len(parent_one) >= 4 and len(parent_two) >= 4: # Случаи типа AaBb, AaBbCc и тд.
                    f1 = d[2:]  # первое поколение
                    g1 = gamet_parent_one  # Гаметы первого родителя
                    g2 = gamet_parent_two  # Гаметы второго родителя
                    return f1, g1, g2, pairs
                elif len(parent_one) == 2 and len(parent_two) == 2: # Случай типа Aa
                    fg1 = gamet_parent_one
                    fg2 = gamet_parent_two
                    gamet_parent_one = list(str(gamet_parent_one.replace(' ', '')).replace(',', ''))# Гаметы родителя 1
                    gamet_parent_two = list(str(gamet_parent_two.replace(' ', '')).replace(',', ''))# Гаметы родителя 2

                    # Создание второго поколения
                    F2 = [gamet_parent_one[0] + gamet_parent_two[1], gamet_parent_one[0] + gamet_parent_two[0],
                          gamet_parent_one[1] + gamet_parent_two[1], gamet_parent_one[1] + gamet_parent_two[0]]

                    # Получение второго поколения
                    result = []
                    for i in F2:
                        a = genetic_sort(i)
                        result.append(a)
                    result.sort()
                    F2 = ', '.join(result)
                    return F2, fg1, fg2
            else:
                f = ''.join(sorted(gibrids_one))
                f1 = genetic_sort(f)  # первое поколение
                if len(parent_one) == 2 and len(parent_two) == 2:
                    f2 = universal_f2_found(f1, math.ceil(len(gamet_parent_one) / 2))
                    # mendel_table = table_maker(f1, math.ceil(len(gamet_parent_one) / 2), f2)
                else:
                    f2 = universal_f2_found(f1, len(gamet_parent_one.split(', ')))
                    # mendel_table = genetic_tables.table_maker(f1, len(gamet_parent_one.split(', ')), f2)
                f3 = gamet_parent_one  # Гаметы первого родителя
                f4 = gamet_parent_two  # Гаметы второго родителя
                return f1, f2, f3, f4 #, mendel_table

        elif len(gamet_parent_one) != len(gamet_parent_two):  # Случай, если количество гамет разное
            gamets_1 = list((gamet_parent_one.replace(' ', '').replace(',', '')))
            gamets_2 = list((gamet_parent_two.replace(' ', '').replace(',', '')))
            f1 = [] # Список первого поколения
            # Выискваем родителя с минимальным количеством гамет
            if len(gamets_1) > len(gamets_2):
                min_gamet = gamets_2 # Список для самого маленького списка гамет
                if len(min_gamet) == 1:
                    for i in range(len(gamets_1)):
                        f1.append(genetic_sort(min_gamet[0] + gamets_1[i]))
            else:
                min_gamet = gamets_1 # Список для самого маленького списка гамет
                if len(min_gamet) == 1:
                    for i in range(len(gamets_2)):
                        f1.append(genetic_sort(min_gamet[0] + gamets_2[i]))
            f1.sort()

            return ', '.join(f1), gamet_parent_one, gamet_parent_two
    except Exception as e:
        print(f"Ошибка: {e}\n")
        print("Возможно, вы что-то сделали не так, проверте, все ли данные введены корректно, та ли раскладка"
              " у вас включена")


if __name__ == '__main__':
    # Тесты
    # print(f"1. {genetic_programme('AaBb', 'AaBb')}") # f2, g1, g2, pairs
    # print(f"2. {genetic_programme('AABB', 'aabb')}") # f1, f2, g1, g2
    # print(f"3. {genetic_programme('aaBB', 'AAbb')}") # f1, f2, g1, g2, pairs
    # print(f"4. {genetic_programme('Aa', 'Aa')}") # f2, g1, g2
    # print(f"5. {genetic_programme('AA', 'aa')}") # f1, f2, g1, g2
    # print(f"6. {genetic_programme('Aa', 'aa')}") # f1, g1, g2
    # print(f"7. {genetic_programme('Aa', 'AA')}") # f1, g1, g2
    # print(f"8. {genetic_programme('AABBCC', 'aabbcc')}") # f1, f2, g1, g2
    # print(f"9. {genetic_programme('AABBcc', 'aabbCC')}") # f1, f2, g1, g2, pairs
    # print(f"10. {genetic_programme('AaBbCc', 'AaBbCc')}") # f2, g1, g2, pairs
    # print(f"11. {genetic_programme('AABBCCDDEE', 'aabbccddee')}") # f1, f2, g1, g2, pairs
    pass