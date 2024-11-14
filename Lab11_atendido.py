grades = []
student_passed = []
valid_input = True

while True:
    grade = input("Enter your grade ( type 'done' to stop): ")
    
    if grade.lower() == 'done':
        break
    if not grade.isdigit():
        print("Error: Please enter a number grade.")
    else:
        grade = int (grade)
        if grade <= 40 or grade> 100:
            print("Invalid Data")
            valid_input = False
            break
        else:
            grades.append(grade)
            if grade >= 75:
                student_passed.append(grade)
                
if valid_input:
    if grades:
        
        average = sum(grades) / len(grades)
        passing_rate = (len(student_passed) / len(grades)) * 100
        print(f"The student average is: {average:.2f}")
        print(f"The passing rate is: {passing_rate:.2f}%")
        print(f"The number of students who passed: {len(student_passed)}")
        print(f"Grades: {grades}")
else:
    print("No grades input")