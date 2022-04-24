class Mapping:
    cyr_lat = {}  # Mapping dictionary for Cyrillic to Latin
    cyr_nlt = {}  # Mapping dictionary for Cyrillic to New Latin
    lat_cyr = {}  # Mapping dictionary for Latin to Cyrillic
    lat_nlt = {}  # Mapping dictionary for Latin to New Latin
    nlt_cyr = {}  # Mapping dictionary for New Latin to Cyrillic
    nlt_lat = {}  # Mapping dictionary for New Latin Latin

    def __init__(self):
        self.__initial_data()

    def __initial_data(self):
        self.cyr_lat = {
            'А':'A',
            'Б':'B',
            'Д':'D',
            'Э':'E',
            'Ф':'F',
            'Г':'G',
            'Ҳ':'H',
            'И':'I',
            'Ж':'J',
            'К':'K',
            'Л':'L',
            'М':'M',
            'Н':'N',
            'О':'O',
            'П':'P',
            'Қ':'Q',
            'Р':'R',
            'С':'S',
            'Т':'T',
            'У':'U',
            'В':'V',
            'Х':'X',
            'Й':'Y',
            'З':'Z',
            'Ў':'Oʻ',
            'Ғ':'Gʻ',
            'Ш':'Sh',
            'Ч':'Ch',
            'Нг':'Ng',

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
            'ъ':'ʼ',
        }
        self.cyr_nlt = {

        }

        self.lat_cyr = {
            'A': 'А',
            'B': 'Б',
            'D': 'Д',
            'E': 'Э',
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
            'Sh': 'Ш',
            'Ch': 'Ч',
            'Ng': 'Нг',

            'a': 'а',
            'b': 'б',
            'd': 'д',
            'e': 'э',
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
            'ʼ': 'ъ',
        }

        self.lat_nlt = {

        }

        self.nlt_cyr = {

        }
        self.nlt_lat = {

        }