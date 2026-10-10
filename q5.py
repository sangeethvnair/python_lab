def frequency(str, char):
    return str.count(char)
def replace_(str,old,new):
    return str.replace(old,new)
def removeFirst(str,char):
    return str.replace(char,"",1)
def removeAll(str,char):
    return str.replace(char,"")
while True:
    print("\nmenu")
    print("1.frequency of char in string\n2.replace character in string\n3.remove the first occurance of the character\n4.remove all occurance of charcter in string\n5.exit")
    option = int(input("Enter the option number :  "))
    if option == 1:
        print(frequency(input("enter a string : "),input("enter the character : ")))
    elif option == 2:
        print(replace_(input("enter a string : "), input("enter the character to replace : "),input("enter the character to repalce with : ")))
    elif option == 3:
        print(removeFirst(input("enter a string : "), input("enter the character to replace : ")))
    elif option == 4:
        print(removeAll(input("enter a string : "), input("enter the character to replace : ")))
    else:
            break