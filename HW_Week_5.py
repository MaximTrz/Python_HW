class CompareClass():
    def compare(self, str1, str2):
        ngrams = [str1[i:i+3] for i in range(len(s1))]

        count = 0
        for ngram in ngrams:
            count += str2.count(ngram)
        return count


class CompareClassWithConstructor():

    similarity = 0

    def __init__(self, str1, str2):
        self.similarity = self.compare(s1, s2)

    def getSimilarity(self):
        return self.similarity

    def compare(self, str1, str2):
        ngrams = [str1[i:i+3] for i in range(len(s1))]

        count = 0
        for ngram in ngrams:
            count += str2.count(ngram)
        return count

if __name__ == '__main__':
    s1 = "Автомобиль"
    s2 = "Автомат"
    compareTest1 = CompareClass()
    print('Проверка класса без конструктора:', s1, ", ", s2,
          "| Cтепень похожести: ", compareTest1.compare(s1, s2))

if __name__ == '__main__':
    s1 = "Автомобиль"
    s2 = "Автомат"
    compareTest2 = CompareClassWithConstructor(s1, s2)
    print('Проверка класса c конструктором:', s1, ", ", s2,
          "| Cтепень похожести: ", compareTest2.getSimilarity())


"""
Код небольшой, поэтому большую выгоду от применения PEP8 увидеть сложно. 
Но код, стал читаться лучше. Убрал лишние пустые строки и личшние пробелы.
Проверил что, отступы соответсвуют 4 пробелам. Перенес некоторые строки(строки 33 и 34, а также 40 и 41).
Для проверки использовал "PyLint", затем проверял код на http://pep8online.com/ 
"""