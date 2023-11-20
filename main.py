import random as r
print("Let's start! -> ok/no")
start = input('>>>')

if start == 'ok':
    def number_find(n):
        x = r.randint(1,n) # Number is thought by Computer
        print(f"I thought a from {1} to {n} number try to find")
        i = 0 # Attemp(s)
        while True:
            i += 1
            a = int(input('>>>')) # Your number
            if a > x:
                print('Please enter a small number')
            elif a < x:
                print('Please enter a bigger number')
            else:
                break
        print(f"Cangratulations! You find {i} attemp(s).")
        return i
    
    def number_findPC(n):
        input(f"Please think random number from {1} to {n} and click any button. I will try to find!") # You will think
        j = 0 # Atemps
        b = 1 # Lower limit
        t = n # Upper limit
        while True:
            j+=1
            if b != t:
                x = r.randint(b,t) # Computer thought
                print(f"You thought {x}")
            else:
                x = b
            a = input("If it is right enter (T), if bigger enter (+) if smaller enter (-)")
            if a == "+":
                b = x + 1
            elif a == '-':
                t = x - 1
            else:
                break
        print(f"I find {j} attemp(s)")
        return j
else:
    print('Thanks!')

def game():
    con = 1 # Continue or not
    while con:
        me = number_find(10) # Sum of attemp(s) from me
        com = number_findPC(10) # Sum of attemp(s) from pc
        if me < com:
            print("Congratulations you won!!!")
        elif me == com:
            print("DRAW!!!")
        else:
            print("Sorry I won!!!")
        con = int(input("Let's continue!  1 / 0 >>>"))
    return print("Thank you!!!")

game()

    