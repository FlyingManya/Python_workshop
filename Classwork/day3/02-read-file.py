# file_name= '/Users/manysing/Desktop/python_workshop/Classwork/day3/sample2.txt'
# with open(file_name,'r') as file:
#     text=file.read()
#     print(text)

# file1='/Users/manysing/Desktop/python_workshop/Classwork/day3/sample.txt'
# file2='/Users/manysing/Desktop/python_workshop/Classwork/day3/sample2.txt'

# # read from one file and write to another
# with open(file1,'r')as f1:
#     text1=f1.read()
#     print(text1)

# with open(file2,'w')as f2:
#     f2.write(text1)

# #read to verfy if it has been written
# with open(file2,'r')as f2:
#     text2=f2.read()
#     print(text2)
    
#reading file line by line
file_name='/Users/manysing/Desktop/python_workshop/Classwork/day3/sample.txt'

with open(file_name,'r') as f1:
    for line in f1:
        if line.strip()=='Singh':
            continue
        print(line.strip())
