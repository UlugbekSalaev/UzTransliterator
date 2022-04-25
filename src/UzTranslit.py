import data


class UzTranslit:
    __cmap = {}

    def __init__(self):
        # self.__initial_data()
        __data = data.Mapping()
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['cyr_nlt'] = __data.cyr_nlt
        self.__cmap['lat_cyr'] = __data.lat_cyr
        self.__cmap['lat_nlt'] = __data.lat_nlt
        self.__cmap['nlt_cyr'] = __data.nlt_cyr
        self.__cmap['nlt_lat'] = __data.nlt_lat

    def __initial_data(self):
        return ""
        # print(d.cyr_lat)
        # print(d.cyr_lat['a'])
        # print(d.cyr_lat['b'])
        # print( isinstance(d.cyr_lat['a'], list))

        # people = {'cyrlat': {'a': 'аа', 'б': 'b', '#': '-'},
        #          'lat': {'a': 'аа', 'б': 'аа', 'sex': 'Female'}}
        # print(people['cyr'+'lat']['#'])

    def translit(self, text, from_: str = 'cyr', to: str ='lat'):
        sc_map = self.__cmap[from_ + '_' + to]  # selected script mapping
        print(sc_map)
        N = 4
        words = text.split()    # list of words from text
        cnv_words = []          # list of converted words
        for word in words:
            # print(word)
            grams = [word[i:i + N] for i in range(len(word) - N + 1)]
            # print(grams)

            cnv_word = ""   # converted version of the current word
            i = 0
            wl = len(word)
            while i < wl:
                found = False
                for j in range(wl - i, 0, -1):
                    chunk = word[i: i + j]
                    #print(chunk)
                    if chunk in sc_map:
                        cnv_word += sc_map[chunk]
                        found = True
                        i += j
                        break
                if not found:
                    cnv_word += word[i]
                    i += 1
            cnv_words.append(cnv_word)
        return ' '.join(cnv_words)    # return as a list // return cnv_words

obj = UzTranslit()
print(obj.translit("Салом хуш кел, бахор! Bizlarni maktabimiz yoradigan xili#$$", 'lat', 'cyr'))
