
def hello ():
    print('hello')

def display_name(name):
    print(f"hello {name}")
    
def addition(a,b):
    sum = a + b
    print(sum)

def addition1(a,b):
    sum = a + b
    return sum
    
#x = addition1(2,4)
#print(x)

def command(cmd):
    import os
    os.system(cmd)
    
#command('ls')

# ***Local and global variable ***

b = "today"
def hello1():
    a = "monday"
    print('hello')
    

# *** Constructor ****

def main():
    my_value = addition1(2,7)
    print(my_value)
        
if __name__=='__main__':
    main()
    