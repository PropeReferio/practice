#Hello, Bo. Enjoy my first script.
attempts1=0
attempts2=0
name=(input("\n\n       Hello. What is your name? "))
hundred=100
age=(float(input("       Welcome, "+name+". How old are you? ")))
# Other option: f"Welcome, {name}. How old are you?"
while not 1<=age<=99:
    try:
        age=(float(input("       Please enter a correct age. ")))
        attempts1+=1
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
else: #Else statements only follow if or elif statements. Were you trying to have this happen if the
    #while loop failed?
    if attempts1>=1: #What is the purpose here?
        print("       Thanks you. ")
    prepost=(input("       Has you birthday passed this year? (y/n) ")) #Comment this out,
    #add it back in once the basic functionality is working. Alternatively, use the datetime
    #module (most professional) and take their birthday to determine if their birthday has passed
    #or not.

while prepost!='y'and prepost!='Y'and prepost!='yes'and prepost!='YES'and prepost!='n'and prepost!='N'and prepost!='no'and prepost!='NO':
    attempts2+=1  #try while prepost.lower() != 'y'. Will make user input not case sensitive.
                #You could accept only 'y' and 'n.' Those are the values listed in your prompt.
    prepost=(input("       Has you birthday passed this year? (y/n) "))
else:
    if attempts2>=1: #What is the purpose of this variable?
        print("       Thanks you. ")
    if prepost =='n'and prepost=='N'and prepost=='no'and prepost=='NO': #Where is the block of code for
        # 'y' responses?
        prepost = True
if prepost:
    hundred=hundred-1
age=round(age)
wait=hundred-age
date=(str(wait+2020))
print("       You will be 100 by " + date + ".")
print("       Have a beautiful life.\n")