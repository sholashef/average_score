#To calculate Average Score
#Here is source code of the Python Program to Calculate the Average score
student_population =int(input("Enter the total number of students: "))
score_list=[]
for i in range(0,student_population):
    score=int(input("Enter score: "))
    score_list.append(score)
    average=sum(score_list)/student_population
    if i == student_population:
        break
print("Average score for the student Population is :",round(average,2))
