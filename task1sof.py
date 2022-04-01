x = input("Введите целое число: ")
u = 0
Y_CONST = 2
def check_int(n):
    try:
        int(n)
        
        return True
    except ValueError:

        return False
if check_int(x) == False:
    print("invalid input")
else:
    result = int(x) + Y_CONST
    print(x,"+", Y_CONST,"=",result) # the programm is taking input and the combining the input and a const and printing the result
    for z in range(15):
        print("instance:",z)
    while u != 3:
        print("hello this is gonna repeat 3 times")
        u += 1
