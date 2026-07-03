"""
Алгорит для:
 - Перевода ДНК в РНК(иРНК, тРНК) и обратно
 - Расшифровка ДНК и РНК
"""

sample_dnk = {'А': 'Т', 'Г': 'Ц', 'У': 'А', 'Ц': 'Г'}
sample_info_rnk = {'А': 'У', 'Г': 'Ц', 'Т': 'А', 'Ц': 'Г'}
sample_transport_rnk = {'А': 'У', 'Г': 'Ц', 'У': 'А', 'Ц': 'Г'}

proteins_rnk = {"УУУ": "Фен", "УУЦ": "Фен", "УУА": "Лей", "УУГ": "Лей", "УЦУ": "Сер", "УЦЦ": "Сер", "УЦА": "Сер",
                "УЦГ": "Сер", "УАУ": "Тир", "УАЦ": "Тир", "УГУ": "Цис", "УГЦ": "Цис", "УГГ": "Три", "ЦУУ": "Лей",
                "ЦУЦ": "Лей", "ЦУА": "Лей", "ЦУГ": "Лей", "АУУ": "Иле", "АУЦ": "Иле", "АУА": "Иле", "АУГ": "Мет",
                "ГУУ": "Вал", "ГУЦ": "Вал", "ГУА": "Вал", "ГУГ": "Вал", "ЦЦУ": "Про", "ЦЦЦ": "Про", "ЦЦА": "Про",
                "ЦЦГ": "Про", "ЦАУ": "Гис", "ЦАЦ": "Гис", "ЦАА": "Глн", "ЦАГ": "Глн", "ЦГУ": "Арг", "ЦГЦ": "Арг",
                "ЦГА": "Арг", "ЦГГ": "Арг", "АЦУ": "Тре", "АЦЦ": "Тре", "АЦА": "Тре", "АЦГ": "Тре", "ААУ": "Асн",
                "ААЦ": "Асн", "ААА": "Лиз", "ААГ": "Лиз", "АГУ": "Сер", "АГЦ": "Сер", "АГА": "Арг", "АГГ": "Арг",
                "ГЦЦ": "Ала", "ГЦУ": "Ала", "ГЦА": "Ала", "ГЦГ": "Ала", "ГАУ": "Асп", "ГАЦ": "Асп", "ГАА": "Глу",
                "ГАГ": "Глу", "ГГЦ": "Гли", "ГГУ": "Гли", "ГГА": "Гли", "ГГГ": "Гли", "УАГ": "Стоп-кодон",
                "УАА": "Стоп-кодон", "УГА": "Стоп-кодон"}

proteins_dnk = {"ТТТ": "Фен", "ТТЦ": "Фен", "ТТА": "Лей", "ТТГ": "Лей", "ТЦТ": "Сер", "ТЦЦ": "Сер", "ТЦА": "Сер",
                "ТЦГ": "Сер", "ТАТ": "Тир", "ТАЦ": "Тир", "ТГТ": "Цис", "ТГЦ": "Цис", "ТГГ": "Три", "ЦТТ": "Лей",
                "ЦТЦ": "Лей", "ЦТА": "Лей", "ЦТГ": "Лей", "АТТ": "Иле", "АТЦ": "Иле", "АТА": "Иле", "АТГ": "Мет",
                "ГТТ": "Вал", "ГТЦ": "Вал", "ГТА": "Вал", "ГТГ": "Вал", "ЦЦТ": "Про", "ЦЦЦ": "Про", "ЦЦА": "Про",
                "ЦЦГ": "Про", "ЦАТ": "Гис", "ЦАЦ": "Гис", "ЦАА": "Глн", "ЦАГ": "Глн", "ЦГТ": "Арг", "ЦГЦ": "Арг",
                "ЦГА": "Арг", "ЦГГ": "Арг", "АЦТ": "Тре", "АЦЦ": "Тре", "АЦА": "Тре", "АЦГ": "Тре", "ААТ": "Асн",
                "ААЦ": "Асн", "ААА": "Лиз", "ААГ": "Лиз", "АГТ": "Сер", "АГЦ": "Сер", "АГА": "Арг", "АГГ": "Арг",
                "ГЦЦ": "Ала", "ГЦТ": "Ала", "ГЦА": "Ала", "ГЦГ": "Ала", "ГАТ": "Асп", "ГАЦ": "Асп", "ГАА": "Глу",
                "ГАГ": "Глу", "ГГЦ": "Гли", "ГГТ": "Гли", "ГГА": "Гли", "ГГГ": "Гли", "ТАГ": "Стоп-кодон",
                "ТАА": "Стоп-кодон", "ТГА": "Стоп-кодон"}


def dnk_convertor_in_rnk(dnk: str) -> str:
    "" "Конвертор из ДНК в иРНК, а после в тРНК """
    dnk = dnk.upper()
    if '-' in dnk:
        dnk = str(dnk.split('-'))
        info_rnk = ''
        transport_rnk = ''
        for protein in dnk:
            if protein in sample_info_rnk:
                info_rnk += f'-{sample_info_rnk[protein]}'
        info_rnk = info_rnk[1:]
        for protein in info_rnk:
            if protein in sample_transport_rnk:
                transport_rnk += f'-{sample_transport_rnk[protein]}'
        transport_rnk = transport_rnk[1:]
        return info_rnk, transport_rnk
    else:
        dnk = list(dnk)
        info_rnk = ''
        transport_rnk = ''
        for protein in dnk:
            if protein in sample_info_rnk:
                info_rnk += f'{sample_info_rnk[protein]}'
        for protein in info_rnk:
            if protein in sample_transport_rnk:
                transport_rnk += f'{sample_transport_rnk[protein]}'
        return info_rnk, transport_rnk


def rnk_convertor_in_dnk(rnk: str) -> str:
    """ Конвертор из иРНК в ДНК """
    rnk = rnk.upper()
    dnk = ''
    if '-' in rnk:
        rnk_new = str(rnk.split('-'))
        for protein in rnk_new:
            if protein in sample_dnk:
                dnk += f'-{sample_dnk[protein]}'
        dnk = dnk[1:]
        return dnk
    else:
        rnk_new = list(rnk)
        for protein in rnk_new:
            if protein in sample_dnk:
                dnk += f'{sample_dnk[protein]}'
        return dnk

def protein_search_for_rnk(rnk: str) -> str:
    """ Расшифровка РНК """
    rnk = rnk.replace('-', '')
    rnk = rnk.replace(' ', '')
    proteins = []
    if len(rnk) % 3 == 0:
        if rnk[:3] == 'УАГ' or rnk[:3] == 'УАА' or rnk[:3] == 'УГА':
            raise ValueError('РНК не может начинаться со стоп-кодона')
        else:
            lst = [rnk[i:i + 3] for i in range(0, len(rnk), 3)]
            for i in lst:
                proteins.append(proteins_rnk[i])
            return '-'.join(proteins)
    elif len(rnk) % 3 != 0:
        if rnk[:3] == 'УАГ' or rnk[:3] == 'УАА' or rnk[:3] == 'УГА':
            raise ValueError('РНК не может начинаться со стоп-кодона')
        else:
            n = len(rnk) % 3
            extra_letter = rnk[-n:]
            rnk = rnk[:-n]
            lst = [rnk[i:i + 3] for i in range(0, len(rnk), 3)]
            for i in lst:
                proteins.append(proteins_rnk[i])
            return '-'.join(proteins), extra_letter


def protein_search_for_dnk(dnk: str) -> str:
    """ Расшифровка ДНК """
    dnk = dnk.upper()
    dnk = dnk.replace('-', '')
    dnk = dnk.replace(' ', '')
    proteins = []
    if len(dnk) % 3 == 0:
        if dnk[:3] == 'ТАГ' or dnk[:3] == 'ТАА' or dnk[:3] == 'ТГА':
            raise ValueError('ДНК не может начинаться со стоп-кодона')
        else:
            lst = [dnk[i:i + 3] for i in range(0, len(dnk), 3)]
            for i in lst:
                proteins.append(proteins_dnk[i])
            return '-'.join(proteins)
    elif len(dnk) % 3 != 0:
        if dnk[:3] == 'ТАГ' or dnk[:3] == 'ТАА' or dnk[:3] == 'ТГА':
            raise ValueError('ДНК не может начинаться со стоп-кодона')
        else:
            n = len(dnk) % 3
            extra_letter = dnk[-n:]
            dnk = dnk[:-n]
            lst = [dnk[i:i + 3] for i in range(0, len(dnk), 3)]
            for i in lst:
                proteins.append(proteins_dnk[i])
            return '-'.join(proteins), extra_letter


# === Тесты === 
if __name__ == '__main__':
    # Конвертируем ДНК в РНК
    print(f"Конвертируем ДНК в РНК: {dnk_convertor_in_rnk('АТЦГГТАГТГГЦАТ')}")

    # Конвертируем ДНК в РНК
    print(f"Конвертируем ДНК в РНК: {rnk_convertor_in_dnk('ГУАГЦЦАУЦАЦЦГУА')}")

    # Производим расшифровку РНК
    print(protein_search_for_rnk('АУЦГГУАГУГГЦАУ'))

    # Демонстрация работы исключения
    print(protein_search_for_rnk('УАГЦЦАУЦАЦЦГУА'))
