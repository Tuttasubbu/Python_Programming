car = {}
for i in range(10):
    key = input("enter brand name ")
    value = input("enter car color ")
    

    car.update({key: value})

print(car)
n = open("Dictionary.txt","w")
print(car,file=n)
n.close()