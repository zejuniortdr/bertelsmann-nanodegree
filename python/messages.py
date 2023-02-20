elnames =  input("Enter names separated by comas: ").split(",")
assignments =  input("Enter assignment count separated by comas: ").split(",")
grades =  input("Enter grades separated by comas: ").split(",")

print(elnames)
print(assignments)
print(grades)

# message string to be used for each student
# HINT: use .format() with this string in your for loop
message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for i in range(len(elnames)):
    print(message.format(elnames[i], int(assignments[i]), int(grades[i]), int(grades[i]) + 2*int(assignments[i])))