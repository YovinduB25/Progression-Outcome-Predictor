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
value3=True
outcome=''
progress=0
trailer=0
retriever=0
exclude=0
run_selection=''

print('--------------------------------------------------------------------------------')
print('Staff Version with Histogram') #Disply the question name
while(run_selection != 'q'):   #loops until user enters the value 'q'
    while(value_1): 

        try:
            while(value_2): #Loop for the restart program if there is a value error or a range error

                #prompt for credit_pass
                credits_pass=int(input('Enter your total PASS credits:'))
                if credits_pass not in[0,20,40,60,80,100,120]: #check the entered value invalid 
                    print('Out of range.')
                    continue 
                
                #prompt for credits_defer
                credits_defer=int(input('Enter your total DEFER credits:' ))
                if credits_defer not in[0,20,40,60,80,100,120]:
                    print('Out of range.')
                    continue
                

                #prompt for credits_fail
                credits_fail=int(input('Enter your total FAIL credits:'))
                if credits_fail not in[0,20,40,60,80,100,120]:
                    print('Out of range.')
                    continue
                
                elif (credits_pass+credits_defer+credits_fail !=total): #check the total is correcet
                    print('Total Incorrect.') #Display the massage, If total incorrect
                    continue 

                #Starts the loop which examine the Prograss outcome
                if credits_pass==120:
                    progress=progress+1
                    print('Prograss')
                    value_2=False
            
                elif credits_pass==100:
                    trailer=trailer+1
                    print('Prograss  (module trailer)')
                    value_2=False

                elif credits_fail>=80:
                    exclude=exclude+1
                    print('Exclude')
                    value_2=False
                else:
                    retriever=retriever+1
                    print('Do not Prograss - Module retriver')
                    value_2=False  #False the while loop which examine value 2

                value3=True
                while(value3):  #ask user for the choice whether to continue or quit
                    print()
                    run_selection=str(input('Would you like to enter another set of data?\n Enter y for yes or q to quit and view results:'))
                            
                    run_selection=run_selection.lower()   #converts the input value to lower case 
                    print(run_selection)
                    if (run_selection=='y'):
                        value_1=True
                        value_2=True
                        value3=False
                    elif (run_selection=='q'):
                        value_1=False
                        value_2=False
                        value3=False
                        

                    else:
                        print('Invalid choice. Enter a valid value(Press y or q)')

        except ValueError: #If there is a value error, This will loop again and again until user input right intigers
                print('Integer required')


#histogram.horizontal_histogram(progress,trailer,retriever,exclude)  #executes the histogram from the file
print('--------------------------------------------------------------------------------')
print('Horizontal Histogram')
print('Progress   ',progress,':','*'*progress)
print('Trailing   ',trailer,':','*'*trailer)
print('Retrieving ',retriever,':','*'*retriever)
print('Excluded   ',exclude,':','*'*exclude)

print()
print((progress+trailer+retriever+exclude),'outcomes in total.')
print('--------------------------------------------------------------------------------')
