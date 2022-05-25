
# 1. Посчитать сумму ряда 0-88888888
print(sum(range(0, 88888888)))

print(X)

# 2. Среднее арифметическое ряда [3, 4, 56, 100, 2, 2, 2]
lst = [3, 4, 56, 100, 2, 2, 2]
average = sum(lst)/len(lst)
print(average)

# 3. Заменить в строке "asdsxfghyxyx" все буквы "x" на "y"
i = 0
originalString = "asdxfghyxyx"
newSring = ""

while i < len(originalString):
    el = originalString[i] 
    if (originalString[i]=="x"):    
        el = "y"
    newSring = newSring+str(el)
    i = i + 1

print(newSring)

# 4. Сосчитать произведение чисел [3, 4, 56, 100, 15, 2, 20, 30] кратных 3 и 5
lst = [3, 4, 56, 100, 15, 2, 20, 30]
res = 1
for element in lst:
    if ( (element%3==0) and (element%5==0) ):
        res = res*element
if (res!=1):
    msg = "Прозведение числел кратных 3 и 5 равно "+str(res)
else:
     msg= "Числе кратных 3 и 5 в списке не обнаружено"

print(msg)

#Заменить все буквы "x" на "у" в исходной строке без использования дополнительной.
originalString = "asdxfghyxyx"
originalString = originalString.replace("x", "y")
print(originalString)