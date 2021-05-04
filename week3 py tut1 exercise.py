student_name = str(input("enter name:"))
homework_mark = int(input("enter mark out of 25:"))
assement_mark = int(input("enter mark/50:"))
exam_mark = int(input("enter out of 100:"))
print(student_name)
total_mark = (homework_mark + assement_mark + exam_mark)/3
def outcome(homework_mark,assement_mark,exam_mark):
    if total_mark < 45 and total_mark > 25:
        return "pass" 
    elif total_mark > 45:
        return "distinction"
    else :
        return "fail"
    

print(outcome(homework_mark, assement_mark, exam_mark))
