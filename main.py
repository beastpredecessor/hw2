#Author: xuanyi shen xjs5065@psu.edu
def  getGradePoint (grade):
  if grade == "A":
    gradepoint = 4.0
  elif grade == "A-":
    gradepoint = 3.67
  elif grade == "B+":
    gradepoint = 3.33
  elif grade == "B":
    gradepoint = 3.0
  elif grade == "B-":
    gradepoint = 2.67
  elif grade == "C+":
    gradepoint = 2.33
  elif grade == "C":
    gradepoint= 2.0
  elif grade == "D":
    gradepoint = 1.0
  else:
    gradepoint = 0.0
  return gradepoint

def run():
  grade1 = input("Enter your course 1 letter grade: ")
  credit1 = input("Enter your course 1 credit: ")
  credit1 = float(credit1)
  print(f"Grade point for course 1 is: {getGradePoint(grade1)}")
  grade2 = input("Enter your course 2 letter grade: ")
  credit2 = input("Enter your course 2 credit: ")
  credit2 = float(credit2)
  print(f"Grade point for course 2 is: {getGradePoint(grade2)}")
  grade3 = input("Enter your course 3 letter grade: ")
  credit3 = input("Enter your course 3 credit: ")
  credit3 = float(credit3)
  print(f"Grade point for course 3 is: {getGradePoint(grade3)}")

  gpa = (getGradePoint(grade1) * credit1 + getGradePoint(grade2) * credit2 + getGradePoint(grade3) * credit3) / (credit1 + credit2 + credit3)
  print(f"Your GPA is : {gpa}")

if __name__ == "__main__":
  run()