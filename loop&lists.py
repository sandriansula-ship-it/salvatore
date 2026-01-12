number = 3
while number < 10:
    print("this is an finite loop")
    number = number + 1
    for i in range (0,10,3):
        print("This is iteration",i)
        #Break and continue
        for i in range(6):
            if i == 3:
                break
                print("Inside loop, iteration", i)
                print("Outside loop")

                #Lists
                numbers = {1,2,3,4,5,6}
                print(numbers)
                print(numbers[2])
                print(numbers[-1])
                #add and remove items from lists
                #Append
                numbers.append(7)
                print(numbers)
                #Insert
                numbers.insert(_index:2, _object:10)
                print(numbers)
                del numbers[2]
                numbers = []
                print(numbers)
