#Write a script that does the following:

#Ask for user input 3 times. Once for a list of names, once for a list of missing assignment counts, and once for a list of grades. Use this input to create lists for names, assignments, and grades.
#Use a loop to print the message for each student with the correct values. The potential grade is simply the current grade added to two times the number of missing assignments.
#Template code for your script:
def school_list():
    names =  input('Enter Your Full Name: ')# get and process input for a list of names
    assignments = int(input('List Of Numbers Of Missing Assignments: ')) # get and process input for a list of the number of assignments
    grades =int(input('Grades Of Missing Assignments: '))  # get and process input for a list of grades
    list_of_names=[]
    list_of_assignments= []
    list_of_grades=[]
    list_of_names.append(names)
    list_of_assignments.append(assignments)
    list_of_grades.append(grades)
    name=0
    assignment=0
    grade=0
    potential_grade= int(grade + 2*((assignments)) )
    # message string to be used for each student
    # HINT: use .format() with this string in your for loop
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
    submit before you can graduate. You're current grade is {} and can increase \
    to {} if you submit all assignments before the due date.\n\n"

    # write a for loop that iterates through each set of names, assignments, and grades to print each student's message
    for i, names in enumerate(list_of_names):
        print(message.format(names,int(list_of_assignments[i]), int(potential_grade[i])))


school_list()
