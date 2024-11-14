student = 0
grade = []
passed = 0


for x in range(5):
    x = int(input("Enter your grade: "))
    if x < 40 or x > 100:
        print("Invalid! Number must be between 40 ")
        break
    else:
        grade.append(x)
    y= float(x)
    if y < 40 or y > 100:
        if x == "Done" :
            print("No Grades Input.")
            break
    
    if x >= 75:
        student += 1
        passed += 1
    else:
        student += 1
    if student == 5:
        print ()
        SumX = sum(grade)
        average = SumX/5
        average = round(average, 2)
            
        Student_passed = (passed/len(grade))*100 
        Student_passed = round(Student_passed, 2)
            
        print ("Grades Input: " + str(grade))
        print ("Student Average: " + str(average))