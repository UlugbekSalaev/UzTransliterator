# bu pypi upload uchun ishlaydi .Data varianti
#from .Data import Mapping
from src.UzTranslit.Data import Mapping

class UzTranslit:
    __cmap = {}
    __cyr_vowel = []
    __lat_vowel = []
    __nlt_vowel = []

    def __init__(self):
        # self.__initial_data()
        __data = Mapping()
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['cyr_nlt'] = __data.cyr_nlt
        self.__cmap['lat_cyr'] = __data.lat_cyr
        self.__cmap['lat_nlt'] = __data.lat_nlt
        self.__cmap['nlt_cyr'] = __data.nlt_cyr
        self.__cmap['nlt_lat'] = __data.nlt_lat
        self.__cyr_vowel = __data.cyr_vowel
        self.__lat_vowel = __data.lat_vowel
        self.__nlt_vowel = __data.nlt_vowel

    def __initial_data(self):
        return ""
        # print(d.cyr_lat)
        # print(d.cyr_lat['a'])
        # print(d.cyr_lat['b'])
        # print( isinstance(d.cyr_lat['a'], list))

        # people = {'cyrlat': {'a': 'аа', 'б': 'b', '#': '-'},
        #          'lat': {'a': 'аа', 'б': 'аа', 'sex': 'Female'}}
        # print(people['cyr'+'lat']['#'])

    def __cyr_rule1(self, word: str, i: int):    # 2ta undosh orasida kelgan е harfi e harfi shaklida buladi
        if i-1 >= 0 and i+1 < len(word):
            if word[i-1] not in self.__cyr_vowel and word[i+1] not in self.__cyr_vowel:
                if word[i].islower():
                    return 'e'
                else:
                    return 'E'
        if word[i].islower():
            return 'ye'
        else:
            return 'Ye'

    def __cyr_rule2(self, word: str, i: int):  # 2ta unli orasida kelgan ц harfi ts harfi shaklida o'giriladi
        if i-1 >= 0 and i+1 < len(word):
            if word[i-1] in self.__cyr_vowel and word[i+1] in self.__cyr_vowel:
                if word[i].islower():
                    return 'ts'
                else:
                    return 'TS'
        if word[i].islower():
            return 's'
        else:
            return 'S'

    def __cyr_rule3(self, word: str, i: int):  #[е,ё,ю,я] harflari undosh tovushlardan keyin kelganda [e,o,u,a] shaklida o'giriladi, masalan sentabr, istisno holatlar mavjud:samalyot
        y_map1 = {
            'е': 'е',  'Е': 'E',
            'ё': 'o',  'Ё': 'O',
            'ю': 'u',  'Ю': 'U',
            'я': 'a',  'Я': 'A',
        }
        y_map2 = {
            'е': 'yе',  'Е': 'Ye',
            'ё': 'yo',  'Ё': 'Yo',
            'ю': 'yu',  'Ю': 'Yu',
            'я': 'ya',  'Я': 'Ya',
        }
        if i-1 >= 0:
            if word[i-1] not in self.__cyr_vowel: #bulardan oldingi harf undosh bulsa
                return y_map1[word[i]]
        return y_map2[word[i]]


    def translit(self, text, from_: str = 'cyr', to: str = 'lat'):
        sc_map = self.__cmap[from_ + '_' + to]  # selected script mapping
        # print(sc_map)
        # N = 4
        words = text.split()  # list of words from text
        cnv_words = []  # list of converted words
        for word in words:
            # print(word)
            # grams = [word[i:i + N] for i in range(len(word) - N + 1)]
            # print(grams)

            cnv_word = ""  # converted version of the current word
            i = 0
            wl = len(word)
            while i < wl:
                found = False
                for j in range(wl - i, 0, -1):
                    chunk = word[i: i + j]
                    # print(chunk)
                    if chunk in sc_map:
                        cnv_word += sc_map[chunk]
                        found = True
                        i += j
                        break
                if not found:
                    catch_in_rule = False
                    if word[i] in ['е', 'Е']:   #cyr_rule1
                        cnv_word += self.__cyr_rule1(word, i)
                        catch_in_rule = True
                    if word[i] in ['ц', 'Ц']:   #cyr_rule2
                        cnv_word += self.__cyr_rule2(word, i)
                        catch_in_rule = True
                    if word[i] in ['Ё', 'Ю', 'Я', 'ё', 'ю', 'я']:   #cyr_rule3 //'Е', 'е',
                        cnv_word += self.__cyr_rule3(word, i)
                        catch_in_rule = True

                    if not catch_in_rule:
                        cnv_word += word[i]
                    i += 1
            cnv_words.append(cnv_word)
        return ' '.join(cnv_words)  # return as a list // return cnv_words

obj = UzTranslit()
while True:
    w = input('Suz=')
    print(obj.translit(w, 'cyr', 'lat'))
