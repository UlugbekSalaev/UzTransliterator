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
total_token, total_char, total_time = 0, 0, 0
for i in range(20,21):
    from_ = "lat"
    to = "cyr"
    with open(os.path.dirname(__file__)+'/../../test/'+str(i)+'_'+from_+'.txt', encoding='utf8') as f:
        text = f.read().rstrip()
        tokens = text.split()
        # print(len(text))
        # print(len(tokens))
        total_token += len(tokens)
        total_char += len(text)

    with open(os.path.dirname(__file__)+'/../../test/'+str(i)+'_'+to+'.txt', encoding='utf8') as f:
        text_to = f.read().rstrip()
        tokens_to = text_to.split()
        # print(len(text_to))
        # print(len(tokens_to))

    start_time = time.time()
    result = obj.transliterate(text, from_=from_, to=to)
    # print("--- %s seconds ---" % (time.time() - start_time))
    total_time += time.time() - start_time
    tokens_result = result.split()
    wrong, correct = 0, 0
    for token in tokens_result:
        if token not in tokens_to:
            print(token)
            wrong += 1
        else:
            tokens_to.remove(token)
            correct += 1

    print(i, len(result), wrong, correct, len(tokens_result), round(wrong/len(tokens_result)*100,2), round(correct/len(tokens_result)*100,2))
print(total_time)
print(total_token)
print(total_char)

