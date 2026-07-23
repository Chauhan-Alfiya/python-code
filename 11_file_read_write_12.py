#file write 
file = open("hello.py","w")
file.write("Hello,Welcome to python!\n")
file.write("this is a file write exmple.")
file.close()

#file read

file = open("hello.py","r")
data= file.read()
print("\nfile content:")
print(data)
file.close()

