# def count():
#     f=input("Enter the file name: ")
#     file=open(f,'r')
#     fileContent=file.readlines()
   
#     a=0
#     y=0
#     for i in fileContent:
#         a= i.split()
#         y=y+len(a)

#     print(y)

#count()

file=open("text.txt","r")
fileContent=file.read()

list=fileContent.split(". ")
print(list)