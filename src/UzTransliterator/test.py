import UzTransliterator
import os
import time

obj = UzTransliterator.UzTransliterator()

# while True:
#     lang1 = input("lang1=")
#     lang2 = input("lang2=")
#     w = ""
#     while w != "stop":
#         w = input('Suz=')
#         print(obj.transliterate(w, from_=lang1, to=lang2))

total_char, total_time = 0, 0
total_wrong, total_correct = 0, 0
for i in range(0,106):
    from_ = "cyr"
    to = "nlt"
    with open(os.path.dirname(__file__)+'/../../test/'+str(i)+'_'+from_+'.txt', encoding='utf8') as f:
        text = f.read().rstrip()
        # print(text)
        tokens = text.split()
        # print(len(text))
        # print(len(tokens))

    with open(os.path.dirname(__file__)+'/../../test/'+str(i)+'_'+to+'.txt', encoding='utf8') as f:
        text_to = f.read().rstrip()
        tokens_to = text_to.split()
        # print(len(text_to))
        # print(len(tokens_to))
        # print(tokens_to)

    start_time = time.time()
    result = obj.transliterate(text, from_=from_, to=to)
    # print("--- %s seconds ---" % (time.time() - start_time))
    total_time += time.time() - start_time
    # print(result)
    tokens_result = result.split()
    wrong, correct = 0, 0
    # print("--------Error tokens----------")
    for token in tokens_result:
        x = token.replace("‘", "ʻ")
        y = token.replace("“", "«")
        z = token.replace("”", "»")
        y1 = token.replace("«", "“")
        z1 = token.replace("»", "”")
        k =  token.replace("ь", "")
        if token in tokens_to or x in tokens_to or y in tokens_to or z in tokens_to or y1 in tokens_to or z1 in tokens_to or k in tokens_to:
            correct += 1
        else:
            wrong += 1
            # print(token, x)
            # tokens_to.remove(token)

        # if token in tokens_to:
        #     correct += 1
        #     tokens_to.remove(token)
        # elif x in tokens_to:
        #         correct += 1
        #         tokens_to.remove(x)
        # elif y in tokens_to:
        #     correct += 1
        #     tokens_to.remove(y)
        # elif z in tokens_to:
        #     correct += 1
        #     tokens_to.remove(z)
        # elif y1 in tokens_to:
        #     correct += 1
        #     tokens_to.remove(y1)
        # elif z1 in tokens_to:
        #     correct += 1
        #     tokens_to.remove(z1)
        # else:
        #     wrong += 1
        #     # print(token, x)
        #     # tokens_to.remove(token)

        total_char += len(token)

    total_wrong += wrong
    total_correct += correct

    # print(i, "\t", len(result), "\t", wrong, "\t", correct, "\t", len(tokens_result), "\t", round(wrong/len(tokens_result)*100,2), "\t", round(correct/len(tokens_result)*100,2))
    # print(i, "\t", "\t", round(wrong/len(tokens_result)*100,2), "\t", round(correct/len(tokens_result)*100,2))
    print(round(correct/len(tokens_result)*100,2))

print(from_, to);
print("Time execution", round(total_time, 4), 'seconds')
print("Total wrong token", total_wrong)
print("Total correct token", total_correct)
print(round(total_wrong/(total_wrong+total_correct)*100, 2), '%')
print(round(total_correct/(total_wrong+total_correct)*100, 2), '%')
print("Total characters ", total_char)