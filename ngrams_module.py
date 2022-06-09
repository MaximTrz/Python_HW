def compare(s1, s2):
    ngrams = [s1[i:i+3] for i in range(len(s1))]

    count = 0
    for ngram in ngrams:        
        count += s2.count(ngram)
    
    return count

if __name__ == '__main__':
    print(compare("тест", "тесто"))