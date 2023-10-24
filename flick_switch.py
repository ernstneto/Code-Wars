def flick_switch(list):
    bool = True
    bool_list = []
    for item in list:
        if item == "flick":
            bool = not bool
            
        bool_list.append(bool)
        #print(f"{bool}")
    return bool_list
        
results = flick_switch(['codewars', 'flick', 'code', 'wars'])
print(f"{results}")