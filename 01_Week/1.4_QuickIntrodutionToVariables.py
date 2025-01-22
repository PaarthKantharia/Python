# We can assign values to any variables.
a = 10
b = 20

# We can print the value of the varibale withe a simple print command stating the variable.
print(a)  ## 10    
print(b)  ## 20

# We can apply aritmatic operations on the values by stating the variables.
print(a+b)
print(a*b)
print(a-b)

# one common unconventional mathematical expression which is not appropriate in mathematics but a commonly uses one in programming
a = a+1
# This term prints as the value of "a" applied arethematic operation to "The number stated" which in this case is "add a" 
print(a)  ## 11

# Once this is done the value of variable is permatantly changed to the value of the the variable with applied arethematic operation with the number given. Which in this case is stated as "a+1". Unless the  arethmatic operation syntax is stated again with the same or different operation multiple print() commands will also result in value equired by the last arethematic operation overshadowing even the orignal given value , which in this case the print(a) command states the valur of last atheticamtic operation stated in line 15 instead of the orignal given value stated in line 2.
print(a)  ## 11
print(a)  ## 11

# Only to apple the same operation or another on the variable the syntax of the arethmatic operation has to be written again to run the athetmatic opetation.
a = a+1 # here IN CASE OF THE SAME VARIABLE. the arethmatic opertaion will be acted on the value result of line 15 rather than taking the orignal value stated in line 2, proving the eariler agreed point arethematic operation permantaly changing the value of the variable for furture refrence in upcoming code.
print(a) ## 12
a = a+1 # here again IN CASE OF THE SAME VARIABLE. the value resets to result of line 26 ignoring both values stated by line 15 and line 2. Concluding the while doing  arethamatic operations the value considered is the value of resulted by the last arethmatic operations in the case of the same vaiable.
print(a) ## 13



