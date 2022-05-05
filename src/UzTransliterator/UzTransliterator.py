# from .Data import Mapping   # use on pypi upload publishing   .Data version
# from src.src.Data import Mapping    # use on local running

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
            'Ў': 'Oʻ',
            'Ғ': 'Gʻ',
            'Ш': 'SH',
            'Ч': 'CH',
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
            'ў': 'oʻ',
            'ғ': 'gʻ',
            'ш': 'sh',
            'ч': 'ch',
            'нг': 'ng',
            'ъ': 'ʼ',

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
            'ъ': 'ʼ',
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
            'Oʻ': 'Ў',
            'Gʻ': 'Ғ',
            'SH': 'Ш',
            'Sh': 'Ш',
            'CH': 'Ч',
            'Ch': 'Ч',
            'NG': 'НГ',
            'Ng': 'Нг',
            'NGʻ': 'НҒ',
            'Ngʻ': 'Нғ',
            # 47-bet qodiasi
            'YE': 'Е',
            'YO': 'Ё',
            'YU': 'Ю',
            'YA': 'Я',
            'YOʻ': 'ЙЎ',
            'Ye': 'Е',
            'Yo': 'Ё',
            'Yu': 'Ю',
            'Ya': 'Я',
            'Yoʻ': 'Йў',

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
            'oʻ': 'ў',
            'gʻ': 'ғ',
            'sh': 'ш',
            'ch': 'ч',
            'ng': 'нг',
            'ngʻ': 'нғ',
            'ʼ': 'ъ',
            # 47-bet qoidasi
            'ye': 'е',
            'yo': 'ё',
            'yu': 'ю',
            'ya': 'я',
            'yoʻ': 'йў',

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
            'Oʻ': 'Ō',
            'Gʻ': 'Ḡ',
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
            'oʻ': 'ō',
            'gʻ': 'ḡ',
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
            'ʼ': 'ъ',
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
            'Ō': 'Oʻ',
            'Ḡ': 'Gʻ',
            'Ş': 'SH',
            'Ç': 'CH',
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
            'ō': 'oʻ',
            'ḡ': 'gʻ',
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
        __data = _CharMapping() # create object from char_mapping class
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['cyr_nlt'] = __data.cyr_nlt
        self.__cmap['lat_cyr'] = __data.lat_cyr
        self.__cmap['lat_nlt'] = __data.lat_nlt
        self.__cmap['nlt_cyr'] = __data.nlt_cyr
        self.__cmap['nlt_lat'] = __data.nlt_lat
        self.__cyr_vowel = __data.cyr_vowel
        self.__lat_vowel = __data.lat_vowel
        self.__nlt_vowel = __data.nlt_vowel

        dirname = os.path.dirname(__file__) +"/"
        cyr_exword_file = os.path.join(dirname + "cyr_exwords.csv")
        lat_exword_file = os.path.join(dirname + "lat_exwords.csv")
        #cyr_exword_file = cyr_exword_file.replace("//", "/")
        #lat_exword_file = lat_exword_file.replace("//", "/")

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
        e_map1 = {'е': 'e', 'Е': 'E'}
        e_map2 = {'е': 'ye', 'Е': 'YE'}
        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] not in self.__cyr_vowel and word[i + 1] not in self.__cyr_vowel:
                return e_map1[word[i]]
        if i - 1 >= 0: # археолог->arxyeolog xatoni yuqatish uchun
            if word[i - 1] not in self.__cyr_vowel:
                return e_map1[word[i]]
        if i == len(word) - 1: # last char alifbe->алифбэ->алифбе
            return e_map1[word[i]]
        return e_map2[word[i]]

    def __cyr_rule2(self, word: str, i: int):  # 2ta unli orasida kelgan ц harfi ts harfi shaklida o'giriladi
        s_map1 = {'ц': 'ts', 'Ц': 'TS'}
        s_map2 = {'ц': 's',  'Ц': 'S'}
        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] in self.__cyr_vowel and word[i + 1] in self.__cyr_vowel:
                return s_map1[word[i]]
        return s_map2[word[i]]

    def __cyr_rule3(self, word: str,
                    i: int):  # [е,ё,ю,я] harflari undosh tovushlardan keyin kelganda [e,o,u,a] shaklida o'giriladi, masalan sentabr, istisno holatlar mavjud:samalyot
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

        if i - 1 >= 0:
            if word[i - 1] not in self.__cyr_vowel and word[i - 1] not in ['-','-','.',',','?','!']:  # bulardan oldingi harf undosh bulsa
                return y_map1[word[i]]
        return y_map2[word[i]]

    def __lat_rule1(self, word: str, i: int): # latin -> kiril # 2ta undosh orasida kelgan е harfi e harfi shaklida buladi
        e_map1 = {'e': 'е', 'E': 'Е'}  # latin -> kiril
        e_map2 = {'e': 'э', 'E': 'Э'}  # latin -> kiril
        if i - 1 >= 0 and i + 1 < len(word):
            if word[i - 1] not in self.__lat_vowel and word[i + 1] not in self.__lat_vowel:
                return e_map1[word[i]]
            if word[i + 1] in self.__lat_vowel: #arxeolog(lat)->архэолог(cyr)->археолог(cyr)
                return e_map1[word[i]]
        if i == len(word) - 1: # if e stands in the last character then
            return e_map1[word[i]]

        return e_map2[word[i]]

    def __check_change_date(self, cnv_words: list):  # kirill->latin da date larga chiziqcha quyish
        dates = (
        'yil', 'asr', 'yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentabr', 'oktabr', 'noyabr', 'dekabr')
        for i in range(1, len(cnv_words)):
            if cnv_words[i].lower().startswith(dates) and cnv_words[i - 1].isdigit():
                cnv_words[i] = "\*-" + cnv_words[i]  # "\*-" quyib keyin " \*" ni o'chirib tashaymiz
        # return cnv_words       #list is a mutable object, so it is sent as a refrence to the object

    def __check_change_second_uppercase(self, cnv_words: list):  # SHamol ->Shamol
        twoletters = {'SH': 'Sh', 'CH': 'Ch'}
        for i in range(0, len(cnv_words)):
            if cnv_words[i][:2] in twoletters and cnv_words[i][2:].islower():
                cnv_words[i] = twoletters[cnv_words[i][:2]] + cnv_words[i][2:]  # SHamol ->Shamol
        # return cnv_words

    def transliterate(self, text, from_: str = 'cyr', to: str = 'lat'):
        # kirildan lotinga o'tilganda cyr_exwords.csv dagi bazadan foydalanamiz, chunki qoidalarga buysunmaydigan joylari bor
        # lotindan kirilga o'tilganda cyr_exwords.csv dagi bazadan foydalanamiz, chunki bularni qoida bilan chiqarib bo'lmaydi, ц,ь,ъ,я belgilarini qo'yishni iloji yuq

        sc_map = self.__cmap[from_ + '_' + to]  # selected script mapping

        if from_ == "lat":  # latinchadagi o' va g' ni ustilarini bir xilga keltirish
            text = text.replace("g'", "gʻ")
            text = text.replace("o'", "oʻ")
            text = text.replace("g`", "gʻ")
            text = text.replace("o`", "oʻ")
            text = text.replace("g’", "gʻ")
            text = text.replace("o’", "oʻ")

            text = text.replace("'", "ʼ") #boshqa belgilarni ъ ni kodiga utirish

        words = text.split()  # list of words from text
        #words = re.split('; |, |\*|\n |-|!|', text) # list of words from text
        cnv_words = []  # list of converted words
        for word in words:
            cnv_word = ""  # converted version of the current word
            i = 0
            wl = len(word)
            while i < wl:
                found = False
                for j in range(wl - i, 0, -1):
                    chunk = word[i: i + j]
                    # print("chunk="+chunk)
                    # latin->kirilda character_mapping qilmasdan oldin, ushbu suzni exwords dan qidirib, topilsa shunga o'giramiz
                    if to == "cyr" and i == 0: # i==0 bu suzni boshidagi qismini csv dan qidirish
                        if chunk in self.__cyr_exwords:
                            cnv_word += self.__cyr_exwords[chunk]
                            # print("cnv="+cnv_word)
                            found = True
                            i += j
                            break
                    if to in ["lat", "nlt"] and i == 0: # i==0 bu suzni boshidagi qismini csv dan qidirish
                        if chunk in self.__lat_exwords:
                            cnv_word += self.__lat_exwords[chunk]
                            found = True
                            i += j
                            break

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

        if to in ["lat", "nlt"]:
            self.__check_change_date(cnv_words)  # kiril->latin o'girilganda sanalar oldiga chiziqcha qo'yiladi: 2021 йил 10 март -> 2021-yil 10-mart
            self.__check_change_second_uppercase(cnv_words)  # latin va newLatinda Birinchidagi harf katta bulsa SHamol shaklida qaytganda Shamol qilib yuborish uchun

        text = ' '.join(cnv_words)  # return as a list // return cnv_words

        if to in ["lat", "nlt"]:
            text = text.replace(" \*-", "-")    #date dagi uzgarihslar uchun

        return text

obj = UzTransliterator()
# coding=utf-8
tt=['авиамодель','автомобиль','акварель','алкоголь','альбом','альманах','альпинизм','альпинист','ангьор','ансамбль','апельсин','апрель','артель','артикль','асфальт','ателье','бандероль','батальон','билль','бильярд','большевик','брильянт','бульдозер','валерьянка',
    'фильм','фильмоскоп','фильмотека','фильтр','фольклор','фонарь','фортепьяно','фотоальбом','фьючерс','цельсий','циркуль','честь','шинель','шпатель','шпиндель','шуьла','эмаль','эмульция','юрисконсульт','якорь','январь']
#for i in tt:
#    print(obj.transliterate(i)+","+
'''
with open("lotin.txt", encoding="utf8") as file:
    lotin = file.readlines()
    lotin = [line.rstrip() for line in lotin]
with open("kirill.txt", encoding="utf8") as file:
    kiril = file.readlines()
    kiril = [line.rstrip() for line in kiril]

with open("latcyr.txt", "w", encoding="utf8") as file:
  for item in kiril:
    cyr = obj.transliterate(item, "cyr", "nlt")
    if cyr not in lotin:
      file.write(item+"\t"+cyr+"\n")
'''
while True:
    lang1 = input("lang1=")
    lang2 = input("lang2=")
    w = ""
    while w != "stop":
        w = input('Suz=')
        print(obj.transliterate(w, from_=lang1, to=lang2))

#qoida: lotin->kiril e oxorda kelsa e buladi, Э емас alifbe