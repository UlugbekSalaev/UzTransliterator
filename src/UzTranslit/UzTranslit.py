# bu pypi upload uchun ishlaydi .Data varianti
#from .Data import Mapping
from src.UzTranslit.Data import Mapping

class UzTranslit:
    __cmap = {}
    __cyr_vowel = []
    __lat_vowel = []
    __nlt_vowel = []
    __cyr_exwords = {}  # Dict from cyr_exwords.csv  for cyrillic exception words
    __lat_exwords = {}  # Dict from lat_exwords.csv  for latin exception words
    def __init__(self):
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

        # get cyrillic ex words as a dict
        with open("cyr_exwords.csv", encoding="utf8") as file:
            for line in file:
                x = line.rstrip().split(",", 1)
                self.__cyr_exwords[x[0]] = x[1]
        # get latin ex words as a dict
        with open("lat_exwords.csv", encoding="utf8") as file:
            for line in file:
                x = line.rstrip().split(",", 1)
                self.__lat_exwords[x[0]] = x[1]


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

    def __lat_rule1(self, word: str, i: int):    # 2ta undosh orasida kelgan е harfi e harfi shaklida buladi
        e_map1 = {'e': 'е', 'E': 'Е'} # latin -> kiril
        e_map2 = {'e': 'э', 'E': 'Э'}  # latin -> kiril
        if i-1 >= 0 and i+1 < len(word):
            if word[i-1] not in self.__lat_vowel and word[i+1] not in self.__lat_vowel:
                return e_map1[word[i]]
        return e_map2[word[i]]

    def __check_change_date(self, cnv_words: list): # kirill->latin da date larga chiziqcha quyish
        dates = ('yil', 'asr', 'yanvar', 'fevral', 'mart', 'aprel', 'may', 'iyun', 'iyul', 'avgust', 'sentabr', 'oktabr', 'noyabr', 'dekabr')
        for i in range(1,len(cnv_words)):
            if cnv_words[i].lower().startswith(dates) and cnv_words[i-1].isdigit():
                cnv_words[i] = "\*-"+cnv_words[i]   # "\*-" quyib keyin " \*" ni o'chirib tashaymiz
        #return cnv_words       #list is a mutable object, so it is sent as a refrence to the object

    def __check_change_second_uppercase(self, cnv_words: list): # SHamol ->Shamol
        twoletters = {'SH': 'Sh', 'CH': 'Ch'}
        for i in range(0,len(cnv_words)):
            if cnv_words[i][:2] in twoletters and cnv_words[i][2:].islower():
                cnv_words[i] = twoletters[cnv_words[i][:2]] + cnv_words[i][2:]   # SHamol ->Shamol
        #return cnv_words


    def translit(self, text, from_: str = 'cyr', to: str = 'lat'):
        # kirildan lotinga o'tilganda xech qanday baza (exception words) dan foydalanmaymiz, faqat mapping va qoidalar asosida
        # lotindan kirilga o'tilganda cyr_exwords.csv dagi bazadan foydalanamiz, chunki bularni qoida bilan chiqarib bo'lmaydi, ц,ь,ъ,я belgilarini qo'yishni iloji yuq

        sc_map = self.__cmap[from_ + '_' + to]  # selected script mapping

        if from_ == "lat":  # latinchadagi o' va g' ni ustilarini bir xilga keltirish
            text = text.replace("g'", "gʻ")
            text = text.replace("o'", "oʻ")
            text = text.replace("g`", "gʻ")
            text = text.replace("o`", "oʻ")
            text = text.replace("g’", "gʻ")
            text = text.replace("o’", "oʻ")

        words = text.split()  # list of words from text
        cnv_words = []  # list of converted words
        for word in words:
            cnv_word = ""  # converted version of the current word
            i = 0
            wl = len(word)
            while i < wl:
                found = False
                for j in range(wl - i, 0, -1):
                    chunk = word[i: i + j]
                    # latin->kirilda character_mapping qilmasdan oldin, ushbu suzni exwords dan qidirib, topilsa shunga o'giramiz
                    if to == "cyr":
                        if chunk in self.__cyr_exwords:
                            cnv_word += self.__cyr_exwords[chunk]
                            found = True
                            i += j
                            break
                    if to == "lat":
                        if chunk in self.__lat_exwords:
                            cnv_word += self.__lat_exwords[chunk]
                            found = True
                            i += j
                            break

                    if chunk in sc_map:
                        cnv_word += sc_map[chunk]
                        found = True
                        i += j
                        break
                if not found:
                    catch_in_rule = False
                    if from_ == "cyr":
                        if word[i] in ['е', 'Е']:   #cyr_rule1
                            cnv_word += self.__cyr_rule1(word, i)
                            catch_in_rule = True
                        if word[i] in ['ц', 'Ц']:   #cyr_rule2
                            cnv_word += self.__cyr_rule2(word, i)
                            catch_in_rule = True
                        if word[i] in ['Ё', 'Ю', 'Я', 'ё', 'ю', 'я']:   #cyr_rule3 //'Е', 'е',
                            cnv_word += self.__cyr_rule3(word, i)
                            catch_in_rule = True
                    if from_ == "lat":
                        if word[i] in ['e', 'E']:   #lat_rule1
                            cnv_word += self.__lat_rule1(word, i)
                            catch_in_rule = True

                    if not catch_in_rule:
                        cnv_word += word[i]
                    i += 1
            cnv_words.append(cnv_word)

        if to in ["lat", "nlt"]:
            self.__check_change_date(cnv_words) # kiril->latin o'girilganda sanalar oldiga chiziqcha qo'yiladi: 2021 йил 10 март -> 2021-yil 10-mart
            self.__check_change_second_uppercase(cnv_words) # latin va newLatinda Birinchidagi harf katta bulsa SHamol shaklida qaytganda Shamol qilib yuborish uchun

        text = ' '.join(cnv_words)  # return as a list // return cnv_words

        if to == "lat":
            text = text.replace(" \*-", "-")

        return text

obj = UzTranslit()
while True:
    lang1 = input("lang1=")
    lang2 = input("lang2=")
    w = ""
    while w != "stop":
        w = input('Suz=')
        print(obj.translit(w, lang1, lang2))