# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.  
# Any code taken from other sources is referenced within my code solution.
#Student ID : 20200870
#UoW ID : w1837849
#Date: 29.04.2021
#beginning variables
credits_pass=0
credits_defer=0
credits_fail=0
total=120
value_1=True
value_2=True
outcome=''

print('Student Version(Validation)') #Disply the question name

while(value_1): #Loop for restart when there is a ivalid value

    try:
        while(value_2): #Loop for the restart program if there is a value error or a range error

            #prompt for credit_pass
            credits_pass=int(input('Please enter your credits at pass:'))
            if credits_pass not in[0,20,40,60,80,100,120]: #check the entered value invalid 
                print('Out of range.')
                continue 
            

            #prompt for credits_defer
            credits_defer=int(input('Please enter your credits at defer:' ))
            if credits_defer not in[0,20,40,60,80,100,120]:
                print('Out of range.')
                continue
            

            #prompt for credits_fail
            credits_fail=int(input('Please enter your credits at fail:'))
            if credits_fail not in[0,20,40,60,80,100,120]:
                print('Out of range.')
                continue
            

            elif (credits_pass+credits_defer+credits_fail !=total): #check the total is correcet
                print('Total Incorrect.') #Display the massage, If total incorrect
                continue 

            #Starts the loop which examine the Prograss outcome
            if credits_pass==120:
                print('Prograss')
                value_2=False

            elif credits_pass==100:
                print('Prograss  (module trailer)')
                value_2=False

            elif credits_fail>=80:
                print('Exclude')
                value_2=False
            else:
                print('Do not Prograss - Module retriver')
                value_2=False  #False the while loop which examine value 2

        value_1=False  #False the while loop which exemine value 1
        

    except ValueError: #If there is a value error, This will loop again and again until user input right intigers
            print('Integer required')


