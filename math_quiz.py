#trybyme
#input information
print("--------------")
name = input("Your Name :")
Birth_Year = int(input("Birth Year :"))
currentyear = 2569
age = currentyear-Birth_Year
occupation = input("Occupation :")


print("--------------")#output information
print("Name =",name)
print("Age =",age)
print("Occupation =",occupation)

#print(type(name))
#print(type(age))
#print(type(occupation))

print("--------------")
question = input("Are you ready for a math challenge?(yes/no) :")
if question.lower()=="yes":
    print("Sound Great!")
elif question.lower()=="no":
    print("Maybe next time",name,"!")
    exit()  
else:
    print("Error baby",name,"!")
    exit()

print("Let's get started with a math problem.")

print("--------------")
x = 25
y = 10
print("x = ",x)
print("y = ",y)
print("8x+2y = ...")
answer = int(input("Ans :"))
correct = (8*x) +   (2*y)

if answer==correct:
    print("Great Job! That's the correct answer.")
elif abs(answer-correct)<=10:
    print("So close!!!",)
    print("The correct answer is",correct)
else:
    print("Wrong Bro!!!")
    print("The correct answer is",correct)
print("See you later",name)
print("--------------")
