"""for 'i' in  'robert'
 print('i')
 """
 
 
"""
for col in ['red', 'black', 'orange', 'yellow', 'ted', 'liz']:
    if len(col) < 4:
         winning_color=col
         print(winning_color)
print('done')
"""

# Given the list of string 'aws','terraform','python' , write a program that 
# will generate a list of these item in upper letters

"""
R= ['terraform', 'python', 'aws']
T = []
for i in R:
     T.append(i.upper())
print(T)
"""

# **** While is use when the boolean is respected ***

count = 0
while count < 6:
    print("hello")
    if count == 2:
        break
    count+=1
