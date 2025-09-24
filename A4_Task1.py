'''Read a file (`sample.txt`) and handle exceptions if the file does not exist'''
try :
   f = open('sample.txt','r')
   line1 = f.readline()
   line2 = f.readline()
   print(f"Line 1 : {line1.strip()}")
   print(f"Line 2 : {line2.strip()}")
   f.close()
except FileNotFoundError :
   print(f"The File 'sample.txt' was not found.")