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

def searchByDict(mark, model):
    markPosition = -1
    modelPostion = -1
    res = []
    
    for key_i in cars_dict:
        key = str(key_i)            
        if (key==mark):                  
            res.append(key)
        for key_j in cars_dict[key_i]:
            key = str(key_j)
            if (key == model):
                res.append(key)
                res.append(cars_dict[key_i][key_j])
    return(res)

print(searchByDict("Honda", "Civic"))