## Progam to split even and odd

##predefine values
list = [10,501,22,37,100,999,87,351]
# Declare empty list to store values
even = []
odd = []
for num in list:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
        
print("Given List:",list)
print("even num :",even)
print("odd num :",odd)
