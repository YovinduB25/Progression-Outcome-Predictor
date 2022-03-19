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

print('Student Version') #Disply the question name

#Get the value for Credit Pass
credits_pass=int(input('Please enter your credits at pass:'))
#Get the value for Credit Defer
credits_defer=int(input('Please enter your credits at defer:' ))
#Get the value for Credit Fail
credits_fail=int(input('Please enter your credits at fail:'))
            
if credits_pass==120:
    print('Progress')#Display Prograss
    
elif credits_pass==100:
    print('Progress (module trailer)')#Display (module trailer)
        

elif credits_fail>=80:
    print('Exclude')#Display Exclude
        
else:
    print('Do not Prograss - Module retriver')#Display Do not prograss- Module retriver
        
        
       


