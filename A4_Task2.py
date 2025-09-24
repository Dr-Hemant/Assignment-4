'''Taking input from user in a file and give output back'''
with open("output.txt","w") as f:
   contentadd = input("Enter text to write to the file :")
   f.write(contentadd)
   print("Data Sucessfully written to output.txt.\n")
   addmorecontent = input("Enter additional text to append:")
   f.write("\n")
   f.write(addmorecontent)
   print("Data Sucessfully Appended.\n")
with open("output.txt","r") as f:
   data = f.read()
   print(f"Final content of output.txt is:\n{data}")
