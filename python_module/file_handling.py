
import csv




"""f = open('file', 'w') # 'W', 'r', 'a',  # t(text) of b(for byte)


f.close()
"""

"""with open('text.txt' , 'r') as f:
    #f.write("\nHello Delano\n")
    content = f.read()
    print(content)
"""

with open('jenkins.csv', 'w',newline='') as j:
    pen = csv.writer(j)
    
    pen.writerow(["USER_NAME", "CELL_PHONE", "INSTANCE_TYPE", "REGION"])
    pen.writerow(["Robert T", "555-555-5555", "t2.xlarge", "us-east-1"])
    
