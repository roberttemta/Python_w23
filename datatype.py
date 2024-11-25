# ******Number************
a= 20 #Int
b= 2.4 #float
c= 3+7j #Complex number

# Arithmetic operators are for number ( + , - , /, *.  , %, //)

# In Python, the % symbol is used as the modulus (or mod) operator. It returns the remainder of a division between two numbers.

# // operator performs integer division (also known as floor division).
# It works with both integers and floating-point numbers.
# The result will always be an integer (for integers) or a floating-point number (if any of the inputs are floats).


# *******String******
s='serge'
la= "smith brown"
_s = """I am learning python"""

# String methods len(), .upper(), .lower(), .isdigit(), .isalpha(), .stip(), .title() and more 
# String indexing and slicing 
# String concatenation

# ******Membership operator****  in, not in,

'a' in 'serge'
'@' not in 'kserge@gmail.com'
'ellys' in ['serge','john','smith','jude']

#  *****Boolean*****
is_student=True
is_current=False


#  *****List []*****
courses = ['terraform','aws','linux','devops', 2, 5.6, True, 2, 1 , 1]

#List Methods .append() , .pop(), .clear(), .copy() , change item, len(), extend(), insert(), .count()

# Tuple () Tuples in Python are immutable sequences, which means their elements cannot be changed or modified after the tuple is created
t=(2,4,6,True)
#tuple methods .count(), index()
#set {} Sets in Python are unordered collections of unique elements
s_set={2 ,2 ,3 ,4 ,5 , True}
#set methods add(), update(), remove(), pop(), clear(), discard()
#Dictionary {}Dictionaries in Python are a collection of key-value pairs. They are highly flexible and WIDELY used for data manipulation
d={'name':'Serge', 'age': 30, 'profession': 'DevOps Engineer', 'courses':['aws','linux','terraform']}
#Dict methods .clear(), .copy(), .get() items(), keys(), values(), pop(), popitem(), update(dict), del(dict[key])
 #- Create or activate a virtual env for python
  
# create and activate a virtual env for python
# pip3 install virtualenv
# virtualenv env		#create the virtual env if not yet created
# source env/Scripts/activate  ( for windows)
# source env/bin/activate  (for mac or linux)