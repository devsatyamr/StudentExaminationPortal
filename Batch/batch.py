import csv


a = open("batch.csv","a")
b=csv.writer(a)
# if written already, comment out the heading
# b.writerow(["Batch ID","Batch Name","Department Name"])
bchID = str(input("Enter Batch ID: "))
name = input("Enter Batch Name: ")
dept = input("Enter Department Name: ")
l = [bchID,name,dept]
b.writerow(l)

c = open("viewcourses.csv",'a')
d = csv.writer(c)
# if written already, comment out the heading
# d.writerow(["Batch","Courses"])


  
print("STORING COURSES LIST IN A BATCH")
bchname = input("Enter batch name: ")
n = int(input("Enter number of courses you want to add : "))
  
for i in range(0, n):
    crs =input("Enter course name: ")
    lst = [bchname,crs]
    d.writerow(lst)
      

print("STORING STUDENT LIST IN A BATCH")
e = open("viewstudents.csv",'a')
f = csv.writer(e)
# if written already, comment out the heading
f.writerow(["Batch","Students"])
bch2name = input("Enter batch name: ")
n = int(input("Enter number of students you want to add : "))
  
for i in range(0, n):
    std =input("Enter student name: ")
    lst2 = [bch2name,std]
    f.writerow(lst2)
print("Batch Details Added Successfully!")

