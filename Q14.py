# Take marks of a student of four different subject find average depending on average find Grade(if marks >=75 i.e,’A’ or >=60 but <=75 i.e,’B’ or >=40 but <=60 i.e,’C’ or <=40 i.e,’D’).
def calculate_average(marks):
    return sum(marks) / len(marks)

def determine_grade(average):
    if average >= 75:
        return 'A'
    elif 60 <= average < 75:
        return 'B'
    elif 40 <= average < 60:
        return 'C'
    else:
        return 'D'

def main():
    subjects = ['Math', 'Science', 'English', 'History']
    marks = []
    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)
    average = calculate_average(marks)
    grade = determine_grade(average)
    print(f"Average marks: {average:.2f}")
    print(f"Grade: {grade}")

if __name__ == "__main__":
    main()
