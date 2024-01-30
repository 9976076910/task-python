#happy numbers

#given python list
list = [10,501,22,37,100,999,87,351]
#declaring empty list
b = []

def is_happy(list):
    
   for i in range (len(list)):
        sum = list[i]
        while sum!=1 and sum !=4:
#initializing the value 
            tempsum = 0
            for digit in str(sum):
                tempsum += int(digit) ** 2   
            sum = tempsum
        if sum == 1:
            b.append(list[i])
            return b
print(is_happy(list))
