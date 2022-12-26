
simbol_arry=["+","-","*","/"]
x=input("input logic:")

print(type(x))

print(x)

list1= list(x)
print(list1)

for s in simbol_arry:
   
   if s in list1:
       
       simbol_index= list1.index(s)
       print(simbol_index)
       print(list1[simbol_index])
       
       left= list1[:simbol_index]
       print(left)
       
       right= list1[simbol_index+1:]
       print(right)

left_number=""
for i in left:
 left_number=left_number+i
 print(i)
 print(left_number)
 right_number=""
for i in right:
 right_number=right_number+i
 print(i)
 print(right_number)
 



if list1[simbol_index] == simbol_arry[0]:
    
   itog= int(left_number)+int(right_number)
   print("itog+:", itog)
    
if list1[simbol_index] == simbol_arry[1]:
    
   itog= int(left_number)-int(right_number)
   print("itog-:", itog)   
   
if list1[simbol_index] == simbol_arry[2]:

    itog= int(left_number)*int(right_number)
    print("itog*:", itog) 
    
if list1[simbol_index] == simbol_arry[3]:

    itog= int(left_number)/int(right_number)
    print("itog/:", itog)             