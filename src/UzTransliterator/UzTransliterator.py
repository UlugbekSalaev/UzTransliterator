# from .Data import Mapping   # use on pypi upload publishing   .Data version
# from src.src.Data import Mapping    # use on local running
import re

class _CharMapping:
    cyr_lat = {}  # Mapping dictionary for Cyrillic to Latin
    cyr_nlt = {}  # Mapping dictionary for Cyrillic to New Latin
    lat_cyr = {}  # Mapping dictionary for Latin to Cyrillic
    lat_nlt = {}  # Mapping dictionary for Latin to New Latin
    nlt_cyr = {}  # Mapping dictionary for New Latin to Cyrillic
    nlt_lat = {}  # Mapping dictionary for New Latin Latin
    cyr_vowel = []  # Cyrillic vowels list
    lat_vowel = []  # Latin vowels list
    nlt_vowel = []  # NewLatin vowels list

    def __init__(self):
        self.__initial_data()

    def __initial_data(self):
        self.cyr_vowel = ["а", "и", "э", "у", "ў", "о", "е", "ё", "ю", "я", "А", "И", "Э", "У", "Ў", "О", "Е", "Ё", "Ю",
                          "Я"]
        self.lat_vowel = ["a", "i", "e", "u", "o‘", "o", "A", "I", "E", "U", "O‘", "O"]
        self.nlt_vowel = ["a", "i", "e", "u", "ō", "o", "A", "I", "E", "U", "Ō" "O"]

        self.cyr_lat = {
            'А': 'A',
            'Б': 'B',
            'Д': 'D',
            'Э': 'E',
            'Ф': 'F',
            'Г': 'G',
            'Ҳ': 'H',
            'И': 'I',
            'Ж': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Қ': 'Q',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'В': 'V',
            'Х': 'X',
            'Й': 'Y',
            'З': 'Z',
            'Ў': 'O‘',
            'Ғ': 'G‘',
            'Ш': 'Sh',
            'Ч': 'Ch',
            'Нг': 'Ng',
            'НГ': 'NG',

            'ЙЮ': 'YYU',
            'Йю': 'Yyu',
            'ЙЁ': 'YYO',
            'Йё': 'Yyo',

            # Uzbek tildia ish yuritish 47-bet
            # 'Ё': 'Yo',
            # 'Ю': 'Yu',
            # 'Я': 'Ya',

            'а': 'a',
            'б': 'b',
            'д': 'd',
            'э': 'e',
            'ф': 'f',
            'г': 'g',
            'ҳ': 'h',
            'и': 'i',
            'ж': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'қ': 'q',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'в': 'v',
            'х': 'x',
            'й': 'y',
            'з': 'z',
            'ў': 'o‘',
            'ғ': 'g‘',
            'ш': 'sh',
            'ч': 'ch',
            'нг': 'ng',
            'ъ': '’',

            'йю': 'yyu',
            'йё': 'yyo',

            # Uzbek tildia ish yuritish 47-bet
            # 'ё': 'yo',
            # 'ю': 'yu',
            # 'я': 'ya',
            'ь': '',  # independent of upper/lower case

            # rule объект [Kitob: o'zbek adabiy tili ish yuritish daftari 43,47-bet]
            'ЪЕ': 'YE',
            'ЪЁ': 'YO',
            'ЪЯ': 'YA',
            'ЪЮ': 'YU',
            'ЬЕ': 'YE',
            'ЬЁ': 'YO',
            'ЬЯ': 'YA',
            'ЬЮ': 'YU',
            'ъе': 'ye',
            'ъё': 'yo',
            'ъя': 'ya',
            'ъю': 'yu',
            'ье': 'ye',
            'ьё': 'yo',
            'ья': 'ya',
            'ью': 'yu',

            # 'Е': 'E, Ye', cyr_rule1 qoidasi asosida 47-bet
            # 'е': 'e, ye', cyr_rule1 qoidasi asosida 47-bet

            # 'Ц': 'S, TS', cyr_rule2 qoidasi asosida 48-bet
            # 'ц': 's, ts', cyr_rule2 qoidasi asosida 48-bet
        }

        self.cyr_nlt = {
            'А': 'A',
            'Б': 'B',
            'Д': 'D',
            'Э': 'E',
            'Ф': 'F',
            'Г': 'G',
            'Ҳ': 'H',
            'И': 'I',
            'Ж': 'J',
            'К': 'K',
            'Л': 'L',
            'М': 'M',
            'Н': 'N',
            'О': 'O',
            'П': 'P',
            'Қ': 'Q',
            'Р': 'R',
            'С': 'S',
            'Т': 'T',
            'У': 'U',
            'В': 'V',
            'Х': 'X',
            'Й': 'Y',
            'З': 'Z',
            'Ў': 'Ō',
            'Ғ': 'Ḡ',
            'Ш': 'Ş',
            'Ч': 'Ç',
            # 'Нг': 'Ng',

            'ЙЮ': 'YYU',
            'Йю': 'Yyu',
            'ЙЁ': 'YYO',
            'Йё': 'Yyo',

            # Uzbek tildia ish yuritish 47-bet
            # 'Ё': 'Yo',
            # 'Ю': 'Yu',
            # 'Я': 'Ya',

            'а': 'a',
            'б': 'b',
            'д': 'd',
            'э': 'e',
            'ф': 'f',
            'г': 'g',
            'ҳ': 'h',
            'и': 'i',
            'ж': 'j',
            'к': 'k',
            'л': 'l',
            'м': 'm',
            'н': 'n',
            'о': 'o',
            'п': 'p',
            'қ': 'q',
            'р': 'r',
            'с': 's',
            'т': 't',
            'у': 'u',
            'в': 'v',
            'х': 'x',
            'й': 'y',
            'з': 'z',
            'ў': 'ō',
            'ғ': 'ḡ',
            'ш': 'ş',
            'ч': 'ç',
            # 'нг': 'ng',
            'ъ': '’',
            'йю': 'yyu',
            'йё': 'yyo',

            # Uzbek tildia ish yuritish 47-bet
            # 'ё': 'yo',
            # 'ю': 'yu',
            # 'я': 'ya',
            'ь': '',  # independent of upper/lower case

            # rule объект [Kitob: o'zbek adabiy tili ish yuritish daftari 43,47-bet]
            'ЪЕ': 'YE',
            'ЪЁ': 'YO',
            'ЪЯ': 'YA',
            'ЪЮ': 'YU',
            'ЬЕ': 'YE',
            'ЬЁ': 'YO',
            'ЬЯ': 'YA',
            'ЬЮ': 'YU',
            'ъе': 'ye',
            'ъё': 'yo',
            'ъя': 'ya',
            'ъю': 'yu',
            'ье': 'ye',
            'ьё': 'yo',
            'ья': 'ya',
            'ью': 'yu',

            # 'Е': 'E, Ye', cyr_rule1 qoidasi asosida 47-bet
            # 'е': 'e, ye', cyr_rule1 qoidasi asosida 47-bet

            # 'Ц': 'S, TS', cyr_rule2 qoidasi asosida 48-bet
            # 'ц': 's, ts', cyr_rule2 qoidasi asosida 48-bet
        }

        self.lat_cyr = {
            'A': 'А',
            'B': 'Б',
            'D': 'Д',
            'F': 'Ф',
            'G': 'Г',
            'H': 'Ҳ',
            'I': 'И',
            'J': 'Ж',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'Q': 'Қ',
            'R': 'Р',
            'S': 'С',
            'T': 'Т',
            'U': 'У',
            'V': 'В',
            'X': 'Х',
            'Y': 'Й',
            'Z': 'З',
            'O‘': 'Ў',
            'G‘': 'Ғ',
            'SH': 'Ш',
            'Sh': 'Ш',
            'CH': 'Ч',
            'Ch': 'Ч',
            'NG': 'НГ',
            'Ng': 'Нг',
            'NG‘': 'НҒ',
            'Ng‘': 'Нғ',
            # 47-bet qodiasi
            'YE': 'Е',
            'YO': 'Ё',
            'YU': 'Ю',
            'YA': 'Я',
            'YO‘': 'ЙЎ',
            'Ye': 'Е',
            'Yo': 'Ё',
            'Yu': 'Ю',
            'Ya': 'Я',
            'Yo‘': 'Йў',

            'a': 'а',
            'b': 'б',
            'd': 'д',
            'f': 'ф',
            'g': 'г',
            'h': 'ҳ',
            'i': 'и',
            'j': 'ж',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'q': 'қ',
            'r': 'р',
            's': 'с',
            't': 'т',
            'u': 'у',
            'v': 'в',
            'x': 'х',
            'y': 'й',
            'z': 'з',
            'o‘': 'ў',
            'g‘': 'ғ',
            'sh': 'ш',
            'ch': 'ч',
            'ng': 'нг',
            'ng‘': 'нғ',
            '’': 'ъ',
            # 47-bet qoidasi
            'ye': 'е',
            'yo': 'ё',
            'yu': 'ю',
            'ya': 'я',
            'yo‘': 'йў',

            # 'E': 'Э', # lat_rule1 qoidasi asosida 47-bet
            # 'e': 'э', # lat_rule1 qoidasi asosida 47-bet
        }

        self.lat_nlt = {
            'A': 'A',
            'B': 'B',
            'D': 'D',
            'F': 'F',
            'G': 'G',
            'H': 'H',
            'I': 'I',
            'J': 'J',
            'K': 'K',
            'L': 'L',
            'M': 'M',
            'N': 'N',
            'O': 'O',
            'P': 'P',
            'Q': 'Q',
            'R': 'R',
            'S': 'S',
            'T': 'T',
            'U': 'U',
            'V': 'V',
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
            'O‘': 'Ō',
            'G‘': 'Ḡ',
            'SH': 'Ş',
            'Sh': 'Ş',
            'CH': 'Ç',
            'Ch': 'Ç',

            'E': 'E',

            # 'Ng': 'Нг',
            # 47-bet qodiasi
            # 'Ye': 'Е',
            # 'Yo': 'Ё',
            # 'Yu': 'Ю',
            # 'Ya': 'Я',
            # 'Yo‘': 'Йў',
            # 'YO‘': 'ЙЎ',

            'a': 'a',
            'b': 'b',
            'd': 'd',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'i': 'i',
            'j': 'j',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'o': 'o',
            'p': 'p',
            'q': 'q',
            'r': 'r',
            's': 's',
            't': 't',
            'u': 'u',
            'v': 'v',
            'x': 'x',
            'y': 'y',
            'z': 'z',
            'o‘': 'ō',
            'g‘': 'ḡ',
            'sh': 'ş',
            'ch': 'ç',

            'e': 'e',

            # 'ng': 'нг',
            # 'ʼ': 'ъ',
            # 47-bet qoidasi
            # 'ye': 'е',
            # 'yo': 'ё',
            # 'yu': 'ю',
            # 'ya': 'я',
            # 'yoʻ': 'йў',
            # 'E': 'Э', # lat_rule1 qoidasi asosida 47-bet
            # 'e': 'э', # lat_rule1 qoidasi asosida 47-bet
        }

        self.nlt_cyr = {
            'A': 'А',
            'B': 'Б',
            'D': 'Д',
            'F': 'Ф',
            'G': 'Г',
            'H': 'Ҳ',
            'I': 'И',
            'J': 'Ж',
            'K': 'К',
            'L': 'Л',
            'M': 'М',
            'N': 'Н',
            'O': 'О',
            'P': 'П',
            'Q': 'Қ',
            'R': 'Р',
            'S': 'С',
            'T': 'Т',
            'U': 'У',
            'V': 'В',
            'X': 'Х',
            'Y': 'Й',
            'Z': 'З',
            'Ō': 'Ў',
            'Ḡ': 'Ғ',
            'Ş': 'Ш',
            'Ç': 'Ч',
            # 'Ng': 'Нг',
            # 47-bet qodiasi
            'YE': 'Е',
            'YO': 'Ё',
            'YU': 'Ю',
            'YA': 'Я',
            'YŌ': 'ЙЎ',

            'Ye': 'Е',
            'Yo': 'Ё',
            'Yu': 'Ю',
            'Ya': 'Я',
            'Yō': 'Йў',

            'a': 'а',
            'b': 'б',
            'd': 'д',
            'f': 'ф',
            'g': 'г',
            'h': 'ҳ',
            'i': 'и',
            'j': 'ж',
            'k': 'к',
            'l': 'л',
            'm': 'м',
            'n': 'н',
            'o': 'о',
            'p': 'п',
            'q': 'қ',
            'r': 'р',
            's': 'с',
            't': 'т',
            'u': 'у',
            'v': 'в',
            'x': 'х',
            'y': 'й',
            'z': 'з',
            'ō': 'ў',
            'ḡ': 'ғ',
            'ş': 'ш',
            'ç': 'ч',
            # 'ng': 'нг',
            '’': 'ъ',
            # 47-bet qoidasi
            'ye': 'е',
            'yo': 'ё',
            'yu': 'ю',
            'ya': 'я',
            'yō': 'йў',

            # 'E': 'Э', # lat_rule1 qoidasi asosida 47-bet
            # 'e': 'э', # lat_rule1 qoidasi asosida 47-bet
        }

        self.nlt_lat = {
            'A': 'A',
            'B': 'B',
            'D': 'D',
            'F': 'F',
            'G': 'G',
            'H': 'H',
            'I': 'I',
            'J': 'J',
            'K': 'K',
            'L': 'L',
            'M': 'M',
            'N': 'N',
            'O': 'O',
            'P': 'P',
            'Q': 'Q',
            'R': 'R',
            'S': 'S',
            'T': 'T',
            'U': 'U',
            'V': 'V',
            'X': 'X',
            'Y': 'Y',
            'Z': 'Z',
            'Ō': 'O‘',
            'Ḡ': 'G‘',
            'Ş': 'Sh',
            'Ç': 'Ch',
            # 'Ng': 'Нг',
            # 47-bet qodiasi
            # 'Ye': 'Е',
            # 'Yo': 'Ё',
            # 'Yu': 'Ю',
            # 'Ya': 'Я',
            # 'Yoʻ': 'Йў',
            # 'YOʻ': 'ЙЎ',

            'a': 'a',
            'b': 'b',
            'd': 'd',
            'f': 'f',
            'g': 'g',
            'h': 'h',
            'i': 'i',
            'j': 'j',
            'k': 'k',
            'l': 'l',
            'm': 'm',
            'n': 'n',
            'o': 'o',
            'p': 'p',
            'q': 'q',
            'r': 'r',
            's': 's',
            't': 't',
            'u': 'u',
            'v': 'v',
            'x': 'x',
            'y': 'y',
            'z': 'z',
            'ō': 'o‘',
            'ḡ': 'g‘',
            'ş': 'sh',
            'ç': 'ch',
            # 'ng': 'нг',
            # 'ʼ': 'ъ',
            # 47-bet qoidasi
            # 'ye': 'е',
            # 'yo': 'ё',
            # 'yu': 'ю',
            # 'ya': 'я',
            # 'yoʻ': 'йў',
            # 'E': 'Э', # lat_rule1 qoidasi asosida 47-bet
            # 'e': 'э', # lat_rule1 qoidasi asosida 47-bet
        }

import os

class UzTransliterator:
    __cmap = {}
    __cyr_vowel = []
    __lat_vowel = []
    __nlt_vowel = []
    __cyr_exwords = {}  # Dict from cyr_exwords.csv  for cyrillic exception words
    __lat_exwords = {}  # Dict from lat_exwords.csv  for latin exception words

    def __init__(self):
        __data = _CharMapping()  # create object from char_mapping class
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['cyr_nlt'] = __data.cyr_nlt
        self.__cmap['lat_cyr'] = __data.lat_cyr
        self.__cmap['lat_nlt'] = __data.lat_nlt
        self.__cmap['nlt_cyr'] = __data.nlt_cyr
        self.__cmap['nlt_lat'] = __data.nlt_lat
        self.__cyr_vowel = __data.cyr_vowel
        self.__lat_vowel = __data.lat_vowel
        self.__nlt_vowel = __data.nlt_vowel

        dirname = os.path.dirname(__file__) + "/"
        cyr_exword_file = os.path.join(dirname + "cyr_exwords.csv")
        lat_exword_file = os.path.join(dirname + "lat_exwords.csv")
        # cyr_exword_file = cyr_exword_file.replace("//", "/")
        # lat_exword_file = lat_exword_file.replace("//", "/")

        # get cyrillic ex words as a dict
        with open(cyr_exword_file, encoding="utf8") as file:
            for line in file:
                x = line.rstrip().split(",", 1)
                self.__cyr_exwords[x[0]] = x[1]
        # get latin ex words as a dict
        with open(lat_exword_file, encoding="utf8") as file:
            for line in file:
                x = line.rstrip().split(",", 1)
                self.__lat_exwords[x[0]] = x[1]

    def __cyr_rule1(self, word: str, i: int):  # 2ta undosh orasida kelgan е harfi e harfi shaklida buladi
        word, i = self.__remove_symbols_starting(word, i)

        e_map1 = {'е': 'e', 'Е': 'E'}
        e_map2 = {'е': 'ye', 'Е': 'Ye'}
        if i == len(word) - 1:  # last char alifbe->алифбэ->алифбе
            return e_map1[word[i]]

        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] not in self.__cyr_vowel and word[i + 1] not in self.__cyr_vowel and \
                    word[i - 1] not in ['(', '"', '-', '-', '.', ',', '?', '!']:
                return e_map1[word[i]]

        if i - 1 >= 0:  # археолог->arxyeolog xatoni yuqatish uchun
            if word[i - 1] not in self.__cyr_vowel and word[i - 1] not in ['(', '"', '-', '-', '.', ',', '?', '!']:
                return e_map1[word[i]]

        return e_map2[word[i]]

    def __cyr_rule2(self, word: str, i: int):  # 2ta unli orasida kelgan ц harfi ts harfi shaklida o'giriladi
        word, i = self.__remove_symbols_starting(word, i)

        s_map1 = {'ц': 'ts', 'Ц': 'TS'}
        s_map2 = {'ц': 's', 'Ц': 'S'}
        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] in self.__cyr_vowel and word[i + 1] in self.__cyr_vowel and word[i - 1] not in ['(', '"',
                                                                                                           '-', '-',
                                                                                                           '.', ',',
                                                                                                           '?', '!']:
                return s_map1[word[i]]
        return s_map2[word[i]]

    def __cyr_rule3(self, word: str, i: int):  # [е,ё,ю,я] harflari undosh tovushlardan keyin kelganda [e,o,u,a] shaklida o'giriladi, masalan sentabr, istisno holatlar mavjud:samalyot
        word, i = self.__remove_symbols_starting(word, i)

        y_map1 = {
            'е': 'е', 'Е': 'E',
            'ё': 'o', 'Ё': 'O',
            'ю': 'u', 'Ю': 'U',
            'я': 'a', 'Я': 'A',
        }
        y_map2 = {
            'е': 'yе', 'Е': 'Ye',
            'ё': 'yo', 'Ё': 'Yo',
            'ю': 'yu', 'Ю': 'Yu',
            'я': 'ya', 'Я': 'Ya',
        }

        if i == len(word) - 1:  # last char alifbe->алифбэ->алифбе
            return y_map2[word[i]]

        if i - 1 >= 0 and i != len(word) - 1:
            if word[i - 1] not in self.__cyr_vowel and word[i - 1] not in ['(', '"', '-', '-', '.', ',', '?',
                                                                           '!']:  # bulardan oldingi harf undosh bulsa
                return y_map1[word[i]]
        return y_map2[word[i]]

    def __lat_rule1(self, word: str, i: int):  # latin -> kiril # 2ta undosh orasida kelgan е harfi e harfi shaklida buladi
        word, i = self.__remove_symbols_starting(word, i)

        e_map1 = {'e': 'е', 'E': 'Е'}  # latin -> kiril
        e_map2 = {'e': 'э', 'E': 'Э'}  # latin -> kiril

        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] not in self.__lat_vowel and word[i + 1] not in self.__lat_vowel:
                return e_map1[word[i]]
            if word[i + 1] in self.__lat_vowel:  # arxeolog(lat)->архэолог(cyr)->археолог(cyr)
                return e_map1[word[i]]
        if i == len(word) - 1:  # if e stands in the last character then
            return e_map1[word[i]]

        return e_map2[word[i]]

    def __check_change_date_to_lat(self, cnv_words: list):  # kirill->latin da date larga chiziqcha quyish
        dates = (
            'yil', 'asr', 'yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentabr', 'oktabr',
            'noyabr', 'dekabr')
        for i in range(1, len(cnv_words)):
            if cnv_words[i].lower().startswith(dates) and cnv_words[i - 1].isdigit():
                cnv_words[i] = "\*-" + cnv_words[i]  # "\*-" quyib keyin " \*" ni o'chirib tashaymiz
        # return cnv_words       #list is a mutable object, so it is sent as a refrence to the object

    def __check_change_date_to_cyr(self, cnv_words: list):  # latin->cyril da date larga chiziqcni quymaslik
        dates = (
            'йил', 'аср', 'январ', 'феврал', 'март', 'апрел', 'май', 'июн', 'июл', 'август', 'сентябр', 'октябр',
            'ноябр', 'декабр')

        for i in range(len(cnv_words)):
            if "-" in cnv_words[i]:
                # remove starting symbols
                ni = cnv_words[i].find("-")
                if ni > 0 and ni + 1 < len(cnv_words[i]):
                    if cnv_words[i][ni - 1].isdigit():
                        if cnv_words[i].lower().startswith(dates, ni + 1):
                            cnv_words[i] = cnv_words[i][:ni] + " " + cnv_words[i][ni + 1:]  # chiziqchani uchirbaramiz
        # return cnv_words       #list is a mutable object, so it is sent as a refrence to the object

    def __check_change_second_uppercase(self, cnv_words: list):  # SHamol ->Shamol
        twoletters = {'SH': 'Sh', 'CH': 'Ch', 'YE': 'Ye', 'YO': 'Yo', 'YU': 'Yu', 'YA': 'Ya'}
        for i in range(0, len(cnv_words)):
            ind = 0
            while ind < len(cnv_words[i]):
                if not cnv_words[i][ind].isalpha():
                    ind += 1
                else:
                    break

            if cnv_words[i][ind:ind + 2] in twoletters and cnv_words[i][ind + 2:].islower():
                cnv_words[i] = cnv_words[i][:ind] + twoletters[cnv_words[i][ind:ind + 2]] + cnv_words[i][
                                                                                            ind + 2:]  # SHamol ->Shamol
        # return cnv_words

    def __remove_symbols_starting(self, word: str, i: int):  # delete starting symbols to correctly convert of (endi  -> (энди
        ni = i  # temp variable
        for ind in range(ni):
            if not word[ind].isalpha():
                i -= 1
                word = word[1:]
            else:
                break
        for ind in range(len(word)-1, i,  -1):
            if not word[ind].isalpha():
                word = word[:-1]
            else:
                break

        return word, i
        # edn of deleting symbols from start of the word

    def __check_global_rules(self, word: str):
        # global rule 1: whether Roman number
        if word.isupper():  # check whether token is Roman number {I, V, X, L, C, D, M}
            if 0 not in [c in {'I', 'V', 'X', 'L', 'C', 'D', 'M'} for c in word]:
                return True

        # global rule 2: whether url

        # if word.lower().startswith(("http", "www")):
        #     return True
        url = ('.org', '.com', '.net', 'http', 'www')
        if any(ext in word.lower() for ext in url):
            return True

        return False

    def transliterate(self, text, from_: str = 'cyr', to: str = 'lat'):
        # kirildan lotinga o'tilganda cyr_exwords.csv dagi bazadan foydalanamiz, chunki qoidalarga buysunmaydigan joylari bor
        # lotindan kirilga o'tilganda cyr_exwords.csv dagi bazadan foydalanamiz, chunki bularni qoida bilan chiqarib bo'lmaydi, ц,ь,ъ,я belgilarini qo'yishni iloji yuq

        sc_map = self.__cmap[from_ + '_' + to]  # selected script mapping

        if from_ == "lat":  # latinchadagi o' va g' ni ustilarini bir xilga keltirish
            text = text.replace("g'", "g‘")
            text = text.replace("o'", "o‘")
            text = text.replace("g`", "g‘")
            text = text.replace("o`", "o‘")
            text = text.replace("g’", "g‘")
            text = text.replace("o’", "o‘")
            text = text.replace("gʻ", "g‘")
            text = text.replace("oʻ", "o‘")

            text = text.replace("G'", "G‘")
            text = text.replace("O'", "O‘")
            text = text.replace("G`", "G‘")
            text = text.replace("O`", "O‘")
            text = text.replace("G’", "G‘")
            text = text.replace("O’", "O‘")
            text = text.replace("Gʻ", "G‘")
            text = text.replace("Oʻ", "O‘")

            text = text.replace("'", "’")  # boshqa belgilarni ъ ni kodiga utirish
            text = text.replace("ʼ", "’")  # boshqa belgilarni ъ ni kodiga utirish
            text = text.replace("’", "’")  # boshqa belgilarni ъ ni kodiga utirish

        # tokens = text.split()  # list of words from text
        # tokens = re.split('; |, |\*|\n |-|!|', text) # list of words from text
        tokens = re.findall(r'\S+|\n|\t', text)
        # print(tokens)
        cnv_words = []  # list of converted words
        for word in tokens:
            cnv_word = ""  # converted version of the current word

            if self.__check_global_rules(word):
                cnv_words.append(word)  # add itself to converted words list
                continue  # skip converted process if current word is Roman number

            i = 0
            wl = len(word)
            # found = False
            # search_ex = True

            for c in range(wl):  # check token is start by symbols, add it to converted string
                i = c
                if word[c].isalpha():
                    break
                else:
                    cnv_word += word[c]

            if i < wl-1:
                for j in range(wl, 2, -1):  # search starting chunk of the string from exword
                    chunk = word[i:j]   # word[i:i+j]
                    # print(i, j, "chunk=", chunk)

                    # latin->kirilda character_mapping qilmasdan oldin, ushbu suzni exwords dan qidirib, topilsa shunga o'giramiz
                    if to == "cyr":  # i==0 bu suzni boshidagi qismini csv dan qidirish
                        if chunk.lower() in self.__cyr_exwords:
                            res = self.__cyr_exwords[chunk.lower()]
                            if chunk != chunk.lower():
                                cnv_word += res.capitalize()
                            else:
                                cnv_word += res
                            # print("cnv="+cnv_word)
                            found = True
                            i += j
                            break
                        # if chunk[0].isalpha() and chunk[-1].isalpha():
                        #     search_ex = False
                    if to in ["lat", "nlt"]:  # i==0 bu suzni boshidagi qismini csv dan qidirish
                        if chunk.lower() in self.__lat_exwords:
                            res = self.__lat_exwords[chunk.lower()]
                            if chunk != chunk.lower():
                                cnv_word += res.capitalize()
                            else:
                                cnv_word += res
                            found = True
                            i += j
                            break
                        # if chunk[0].isalpha() and chunk[-1].isalpha():
                        #     search_ex = False

                while i < wl:
                    found = False
                    # for j in range(wl - i, 0, -1):
                    for j in range(3, 0, -1):   # chunk made from 3 character
                        chunk = word[i:i+j]
                        # print(i, j, "chunk1=", chunk)

                        if chunk in sc_map:
                            cnv_word += sc_map[chunk]
                            # print("cnv2="+cnv_word)
                            found = True
                            i += j
                            break

                    if not found:
                        catch_in_rule = False
                        if from_ == "cyr":
                            if word[i] in ['е', 'Е']:  # cyr_rule1
                                cnv_word += self.__cyr_rule1(word, i)
                                catch_in_rule = True
                            if word[i] in ['ц', 'Ц']:  # cyr_rule2
                                cnv_word += self.__cyr_rule2(word, i)
                                catch_in_rule = True
                            if word[i] in ['Ё', 'Ю', 'Я', 'ё', 'ю', 'я']:  # cyr_rule3 //'Е', 'е',
                                cnv_word += self.__cyr_rule3(word, i)
                                catch_in_rule = True
                        if from_ == "lat":
                            if word[i] in ['e', 'E']:  # lat_rule1
                                cnv_word += self.__lat_rule1(word, i)
                                catch_in_rule = True

                        if not catch_in_rule:
                            cnv_word += word[i]

                        i += 1

            cnv_words.append(cnv_word)

        if to in ["cyr"]:
            self.__check_change_date_to_cyr(
                cnv_words)  # latin->cyrill o'girilganda sanalar oldiga chiziq o'chiriladi: 2021-yil 10-mart -> 2021 йил 10 март

        if to in ["lat", "nlt"]:
            self.__check_change_date_to_lat(
                cnv_words)  # kiril->latin o'girilganda sanalar oldiga chiziqcha qo'yiladi: 2021 йил 10 март -> 2021-yil 10-mart
            self.__check_change_second_uppercase(
                cnv_words)  # latin va newLatinda Birinchidagi harf katta bulsa SHamol shaklida qaytganda Shamol qilib yuborish uchun

        text = ' '.join(cnv_words)  # return as a list // return cnv_words

        if to in ["lat", "nlt"]:
            text = text.replace(" \*-", "-")  # date dagi uzgarihslar uchun

        return text
