cars_dict = {
    "Honda": {
        "Civic":{
            "Value": 1.8,
            "Body_type":  "Sedan",
            "Power": 140,                        
        },
        "CR-V":{
            "Value": 2.0,
            "Body_type":  "Station wagon",
            "Power": 150,     
        } 
    },
    "Toyota":{
        "Corolla":{
            "Value": 1.6,
            "Body_type":  "Sedan",
            "Power": 120,   
        },
        "RAV-4":{
            "Value": 2.0,
            "Body_type":  "Station wagon",
            "Power": 152,     
        } 
    }
}

cars_list = [
    ["Honda Civic", 1.8, "Sedan", 140],
    ["Honda CR-V", 2.0, "Station wagon", 150],
    ["Toyota RAV-4", 2.0,  "Station wagon", 152],
    ["Toyota Corolla", 1.8, "Sedan", 120]
]

cars_set = {
    ("Honda Civic", 1.8, "Sedan", 140),
    ("Honda CR-V", 2.0, "Station wagon", 150),
    ("Toyota RAV-4", 2.0,  "Station wagon", 152),
    ("Toyota Corolla", 1.8, "Sedan", 120)
}

# Функция поиска автомобиля по словарю
def searchByDict(cars_dict, mark, model):
    markPosition = -1
    modelPostion = -1
    res = []
    
    # Обходим "верхние" эелементы словаря
    for key_i in cars_dict:
        key = str(key_i)            
        if (key==mark):                  
            res.append(key)
        # Обходим вложенные элементы
        for key_j in cars_dict[key_i]:
            key = str(key_j)
            if (key == model):
                res.append(key)
                res.append(cars_dict[key_i][key_j])
    return(res)

print(searchByDict(cars_dict, "Honda", "Civic"))

# Поиск автомобиля в списке или множеству (по наименованию)
def searchByList(cars_list, carName):
    for elem in cars_list:
        for car in elem:
            if car==carName:
                return elem

print(searchByList(cars_list, "Honda Civic"))

'''
В словаре хранить информацию об автомобилях удобнее, струтуру можно описать более детально, но для реализации поиска надо знать точную стрктуру словаря.
Списки и множества менее удобны, т.к. информация не так хорошо структурирована.
'''