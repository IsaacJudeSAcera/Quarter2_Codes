students=int(input("Enter number of students:"))
subjects=int(input("Enter number of subjects:"))
class_av=0
for i in range (1,students+1):
    average=0
    print("Student",i)
    for x in range(1,subjects+1):
        grade = int(input(f"  Enter score {x}: "))
        average += grade
    average=average/subjects
    class_av += average
    print("Average for Student ",i," = ",average)
class_av/=students
print("Class average = ",class_av)