import data
class UzTranslit:
    __cmap= {}

    def __init__(self):
        #self.__initial_data()
        __data = data.Mapping()
        self.__cmap['cyr_lat'] = __data.cyr_lat
        self.__cmap['cyr_nlt'] = __data.cyr_nlt
        self.__cmap['lat_cyr'] = __data.lat_cyr
        self.__cmap['lat_nlt'] = __data.lat_nlt
        self.__cmap['nlt_cyr'] = __data.nlt_cyr
        self.__cmap['nlt_lat'] = __data.nlt_lat

    def __initial_data(self):
        return ""
        #print(d.cyr_lat)
        #print(d.cyr_lat['a'])
        #print(d.cyr_lat['b'])
        #print( isinstance(d.cyr_lat['a'], list))

        #people = {'cyrlat': {'a': 'аа', 'б': 'b', '#': '-'},
        #          'lat': {'a': 'аа', 'б': 'аа', 'sex': 'Female'}}
        #print(people['cyr'+'lat']['#'])

    def translit(self, text, from_='cyr', to='lat'):
        sc = self.__cmap[from_+'_'+to] #selected script mapping
        print(sc)
        N = 4
        words = text.split()
        for word in words:
            grams = [word[i:i + N] for i in range(len(word) - N + 1)]
            print(grams)

            #words_cnv =



obj = UzTranslit()
obj.translit("Салом хуш келибсиз!")
