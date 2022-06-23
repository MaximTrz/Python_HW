class CompareClass():
    def compare(self, s1, s2):
        ngrams = [s1[i:i+3] for i in range(len(s1))]

        count = 0
        for ngram in ngrams:        
            count += s2.count(ngram)
        
        return count

#Класс с конструктором
class CompareClassWithConstructor():
    
    #похожесть
    similarity = 0
    
    def __init__(self, s1, s2):        
        self.similarity = self.compare(s1, s2)        

    def getSimilarity(self):
        return self.similarity

    def compare(self, s1, s2):
        ngrams = [s1[i:i+3] for i in range(len(s1))]

        count = 0
        for ngram in ngrams:        
            count += s2.count(ngram)
        
        return count

if (__name__=='__main__'):
    s1 = "Автомобиль"
    s2 = "Автомат"
    compareTest1 = CompareClass()
    print('Проверка класса без конструктора:', s1, ", ", s2, "| Cтепень похожести: ", compareTest1.compare(s1, s2))

if (__name__=='__main__'):
    s1 = "Автомобиль"
    s2 = "Автомат"
    compareTest2 = CompareClassWithConstructor(s1, s2)
    print('Проверка класса c конструктором:', s1, ", ", s2, "| Cтепень похожести: ", compareTest2.getSimilarity())