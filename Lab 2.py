##1
print("\n Question 1")
str="hi,apple,up,down"
vowels=0
for letter in str:
    if letter =='a' or letter =='e' or letter =='u' or letter =='i' or letter =='o':
        vowels+=1
print ("no.of vowels: ",vowels)

##2
print("\n Question 2")
number =int(input("enter number: "))
if (number%2)==0:
    print("even")
else :
    print ("odd")

##3
print("\n Question 3")
natural=0
while natural<=10:
    print(natural)
    natural+=1

##4
print("\n Question 4")
for i in range (1,7):
    for j in range(1,i):
        print(j,end=" ")
    print('\n')

##5
print("\n Question 5")
target_num= int(input("enter number"))
sum=0
for i in range(1,target_num+1):
    sum+=i
print("sum till number: ",sum)

##6
print("\n Question 6")
num=5
for i in range (13):
    print(num,' X ',i,'= ',i*num)

##7
print("\n Question 7")
lst1=[1,2,3,4,5]
lst2=[10,20,30,40,50,60]
lst3=[]
if len(lst2)> len(lst1):
    min_size=len(lst1)
    biglst=lst2
else:
    min_size=len(lst2)
    biglst=lst1
for i in range(min_size):
    lst3.append(lst1[i])
    lst3.append(lst2[i])
for i in range(min_size,len(biglst)):
    lst3.append(biglst[i])
print(lst3)


##8
print("\n Question 8")
stri="JhonDipBaba"
size=round((len(stri)-3)/2)
print(stri[size:size+3])

##9
print("\n Question 9")
tuple1= ("Orange",[10,20,30],(5,15,25))
for i in range(len(tuple1[1])) :
    if tuple1[1][i] == 20:
        print("number:",tuple1[1][i],"\n index: ",i)

##10
print("\n Question 10")
sample_dict={
    'a':100,
    'b':200,
    'c':300
}
found=False
for i in sample_dict.values():
    if i==200:
        found = True
print("number is found") if (found) else print("number not found")

##11
print("\n Question 11")
def info(age,name):
    print("name:",name," ,age:",age)
info(19,"Haneen")

##12
print("\n Question 12")
size= int(input("enter size of list:"))
print("enter numbers in list")
list=[]
for i in range(size):
    list.append(input())
mx_num=list[0]
for i in list:
    if i>mx_num:
        mx_num=i
print("max num: ",mx_num)

##13
print("\n Question 13")
file1= open("new_file.txt","a")
file1.write("\nHello World")
file1= open("new_file.txt","r")
print(file1.read())
file1.close()