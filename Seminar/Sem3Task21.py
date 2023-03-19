# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": "S005 "}, {" V ":"S009 "}, {" VIII 
# ":"S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {" V ":"S009"}, {" VIII ":"S007"}]
my_set = set()

for item in list_1: 
    for value in item.values(): 
        my_set.add(value)
print(my_set)