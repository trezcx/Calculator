# num1= 2
# num2 = 4

# summa = num1 + num2

# print("summa {0} + {1} = {2}" .format(num1, num2, summa))

def add(a,b):
       return a + b
 #сложение

def substarct(a,b): #вычитание
       return a - b

def multiply(a,b): #умножить
       return a * b

def devide(a, b): #делить
       return a / b

print("Choose one of this operations") #выбор оператора
print("1.Add") #  сложение
print("2.Substract") #  вычитание
print("3.Multiply") #  умножение
print("4.Devide") #  деление

while True:
       variant = input("Input your choise(1,2, 3, 4)")
       if variant in ('1', '2', '3', '4'):
              try:
                     Number1 = float(input("First number: "))
                     Number2 = float(input("Second number: "))
              except ValueError:
                     print("Please input number")
                     continue

              if variant == "1":
                     print(Number1, "+", Number2, "=", add(Number1, Number2))

              elif variant == '2':
                  print(Number1, "-", Number2, "=", substarct(Number1, Number2))          
              elif variant == '3':
                  print(Number1, "*", Number2, "=",multiply(Number1, Number2))          
              elif variant == '4':
                  print(Number1, "/", Number2, "=",devide(Number1, Number2))    

              next_operation = input("Do you want one more? (Yes/No): ")      
              if next_operation == "No":
                     break

       else:
              print("Wrong number")