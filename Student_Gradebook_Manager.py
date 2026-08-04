print('\n--WELCOME TO GRADEBOOK MANAGER--\n')

data_container={}

def print_menu():
    '''Print Menu of the System'''
    print('\n1. Add a New Student',
          '\n2. Enroll a Student in a Course',
          '\n3. Drop a Course',
          '\n4. View Student Details',
          '\n5. View All Students',
          '\n6. Search for a Student by Name',
          '\n7. Remove a Student (Delete Entire Record)',
          '\n8. Generate Course Enrollment Report',
          '\n9. Backup System',
          '\n10. Exit')

def add_student(current_data): #system is handed to the function to work with it..
    '''prompt user student id and name to add a student if not already exist'''
    id=int(input('\nEnter Student ID: '))
    if id in current_data:
            print('\nStudent Already Exist --------👈')
    else:
        name=input('Enter Student Name: ').title().strip()
        current_data[id]={'name':name, 'course':[]} #to insert name and empty course list as a dictionary
        print('\nAdded Succesfully --------👈')
    return current_data #system is returned with the updation it got..
    
def enroll_student(current_data):
    '''prompt user student id and course name to enroll if not enrolled already'''
    id=int(input('\nEnter Id of the Student: '))
    if id in current_data:
        course_name=input('Enter Course Name to Enroll in: ').strip().title()
        if course_name in current_data[id]['course']: #to make names lowercase of courses
            print('\nAlready Enrolled --------👈')
        else:
            current_data[id]['course'].append(course_name)
            print('\nEnrolled Succesfully --------👈')
    else:
        print('\nStudent not exist --------👈')
    return current_data
    
def drop_course(current_data):
    '''prompt user student id and course name to drop it from their enrolled courses'''
    id=int(input('\nEnter Id of the Student: '))
    if id in current_data:
        course_name=input('Enter Course Name to Drop: ').strip().title()
        if course_name in current_data[id]['course']:
            current_data[id]['course'].remove(course_name)
            print('\nCourse Dropped Succesfully --------👈')
        else:
            print('\nStudent is not enrolled in that course --------👈')
    else:
        print('\nStudent not exist --------👈')
    return current_data
    
def view_student_details(current_data):
    '''prompt user student id and print the student details'''
    id=int(input('Enter Id of the Student: '))
    if id in current_data:
        print(f'\nID: {id} --------👈',
              f'\nName: {current_data[id]['name']}',
              f'\nNumber of courses enrolled: {len(current_data[id]['course'])} \n',
              f'{f'List of all Courses: {current_data[id]['course']}' if current_data[id]['course'] != [] else 'List of all Courses: No courses enrolled'}',
               '--------👆')
    else:
        print('\nStudent not exist --------👈')
    return current_data

def view_all_students(current_data):
    '''print all students details'''
    if current_data != {}:
        count=0
        for id,value in current_data.items(): #FOR ID, picks up the id and dictionary in value
            print(f'\nID: {id}')
            for nested_key,nested_value in value.items(): #FOR NAME ONLY, picks up whole item from the dictionary in value
                print(f'{nested_key.capitalize()} : {nested_value}')
                for item in current_data[id]['course']: #FOR NUMBER COURSES, iterate into list items and incrementing into count to get total courses in list, and break the loop to not iterate for 2nd key of the nested dictionary
                    count=count+1
                print('Number of Courses: ',count)              
                count=0 #reset count for next student
                break #to stop the loop for the next iteration to course key
    else:
        print('\nNo students in the system. --------👈')
    return current_data

def search_student_by_name(current_data):
    '''prompt user student partial or full name and search matching then print all similar stuudents details'''
    name=input('\nEnter Full/Partial Name [e.g Ali or Ali kamran]: ')
    print('\nSimilar:')
    found=False
    for id,value in current_data.items(): #to get nested dictionary, one by one according to id
        if name.lower() in value['name'].lower(): #to get the only name key's value and check if input contains in the value (by iterate into string)
            print(f"Name: {value['name']}, ID: {id}, Courses: {value['course']}")
            found=True
    if not found: #if found = True, the 'not' will make it false, and will not print the statement, but if found = False then 'not' will make it True and print statement
        print('\nNo students found. --------👈')
    return current_data

def remove_student(current_data):
    '''prompt user student id and remove student after confirmation'''
    id=int(input('\nEnter ID of the Student: '))  
    if id in current_data:
        confirmation=input('Are you Sure? [yes or no]: ')
        if confirmation=='yes':
            del current_data[id]
            print('\nDeleted Succesfully --------👈')
        elif confirmation=='no':
            print('\nCancelled --------👈')
    else:
        print('\nStudent not exist --------👈')
    return current_data

def generate_course_enrollment_report(current_data):
    '''print complete details of all courses enrollment'''
    if current_data != {}:
        course_count={}
        for id,dict in current_data.items():
            for course in dict['course']:
                if course in course_count:
                    course_count[course]+=1 #IF COURSE IS ALREADY IN COURSE COUNT DICT, JUST INCREMENT IN ITS VALUE
                else:
                    course_count[course]=1 #ADDING THE COURSE IN COURSE COUNT DICT AND SET TO 1
        for key,value in course_count.items(): #to print the course count dict
            print(f'\n{key}: {value} students')
    else:
        print('\nNo students in the system. --------👈')
    return current_data

def backup_system(current_data):
    '''make a copy of the system (data dictionary) as backup'''
    backup=current_data.copy()
    print('\nBackup Created Succesfully --------👈')   
    return current_data

def exit():
    print('\nGoodBye --------👈')

while True:
    print_menu()
    opt=int(input('\nPlease Select an Option 🙂: '))
    
    if opt==1:
        data_container=add_student(data_container) #to give the system to work on it or work with
    elif opt==2:
        data_container=enroll_student(data_container)
    elif opt==3:
        data_container=drop_course(data_container)
    elif opt==4:
        data_container=view_student_details(data_container)
    elif opt==5:
        data_container=view_all_students(data_container)
    elif opt==6:
        data_container=search_student_by_name(data_container)
    elif opt==7:
        data_container=remove_student(data_container)
    elif opt==8:
        data_container=generate_course_enrollment_report(data_container)
    elif opt==9:
        data_container=backup_system(data_container)
    elif opt==10:
        exit()
        break
    else:
        print('\nInvalid selection, Please try again --------👈')