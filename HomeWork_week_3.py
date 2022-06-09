from ngrams_module import compare

pareList = ("тест", "текст", "тесть", "тесто")
mainStr = "грусть"

for str in pareList:
    print(mainStr, str, compare(str, mainStr))