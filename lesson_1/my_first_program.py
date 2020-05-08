## Thushara Lakshmanan
## 02 May 2020
## Title -->My first Python Program


import time 

print("Hi")
time.sleep(2)
print("I am Ms.Robot!")
time.sleep(2)
print("Let's chat for a bit,shall we?")
time.sleep(2)
name=input("What's your name:")
print(f"Welcome, {name}. It is very nice to meet you!")
time.sleep(2)
print("Shall we do some fun challenge!")
time.sleep(2)
print("Preparing")
print("---"*10)   
time.sleep(2)
print("Let's make a mnemonic to remember the order of planets in the solar system")
time.sleep(1)
print("Here is an example")
print(" M-My","V-Very","E-Excellent","M-Mother","J-Just","S-Served","U-Us","N-Noodles",sep='\n ')
print("---"*10)
time.sleep(1)
print("Now its your turn!")
time.sleep(1)
print("Please type your answer")
time.sleep(1)
print("Good Luck!")
mylist=[]
for i in "MVEMJSUN":
    w=input(f"Enter a word starts with {i}:")
    if w[0].upper()!=i:
        print(f"oops!Word is not starting with '{i}'")
        w=input(f"Enter a word for {i}:")   
    mylist.append(w)
time.sleep(1)
print("Let's put together the words you entered..")
time.sleep(2)
temp=""
for i in mylist:
    temp=temp+i+" "
print(f"Congratulation {name}!")
time.sleep(1)
print("The sentence is: ",temp)
time.sleep(1)
print(f"Thank you for your time {name}, I hope you come visit me again soon. Takecare!")


    
    

