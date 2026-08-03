data_container={101:{'name':'Areesha',
                     'course':['Probability',
                               'Database',
                               'Operating System']
                     }
                }
while True:
    
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
    opt=int(input('\nPlease Select an Option 🙂: '))
    
    if opt==1:
        id=int(input('Enter Student ID: '))
        name=input('\nEnter Student Name: ').title().strip()
        if id in data_container:
            print('\nStudent Already Exist --------👈')
        else:
            data_container[id]={'name':name, 'course':[]} #to insert name and empty course list as a dictionary
            print('\nAdded Succesfully --------👈')
    elif opt==2:
        id=int(input('\nEnter Id of the Student: '))
        if id in data_container:
            course_name=input('Enter Course Name to Enroll in: ').strip().title()
            if course_name in data_container[id]['course']: #to make names lowercase of courses
                print('\nAlready Enrolled --------👈')
            else:
                data_container[id]['course'].append(course_name)
                print('\nEnrolled Succesfully --------👈')
        else:
            print('\nStudent not exist --------👈')
    elif opt==3:
        id=int(input('\nEnter Id of the Student: '))
        if id in data_container:
            course_name=input('Enter Course Name to Drop: ').strip().title()
            if course_name in data_container[id]['course']:
                data_container[id]['course'].remove(course_name)
                print('\nCourse Dropped Succesfully --------👈')
            else:
                print('\nStudent is not enrolled in that course --------👈')
        else:
            print('\nStudent not exist --------👈')
    elif opt==4:
        id=int(input('Enter Id of the Student: '))
        if id in data_container:
            print(f'\nID: {id} --------👈',
                  f'\nName: {data_container[id]['name']}',
                  f'\nNumber of courses enrolled: {len(data_container[id]['course'])} \n',
                  f'{f'List of all Courses: {data_container[id]['course']}' if data_container[id]['course'] != [] else 'List of all Courses: No courses enrolled'}',
                  '--------👆')
        else:
            print('\nStudent not exist --------👈')   
    elif opt==5:
        if data_container != {}:
            count=0
            for id,value in data_container.items(): #FOR ID, picks up the id and dictionary in value
                print(f'\nID: {id}')
                for nested_key,nested_value in value.items(): #FOR NAME ONLY, picks up whole item from the dictionary in value
                    print(f'{nested_key.capitalize()} : {nested_value}')
                    for item in data_container[id]['course']: #FOR NUMBER COURSES, iterate into list items and incrementing into count to get total courses in list, and break the loop to not iterate for 2nd key of the nested dictionary
                        count=count+1
                    print('Number of Courses: ',count)
                    
                    count=0 #reset count for next student
                    break #to stop the loop for the next iteration to course key
        else:
            print('\nNo students in the system. --------👈')
    elif opt==6:
        name=input('\nEnter Full/Partial Name [e.g Ali or Ali kamran]: ')
        print('\nSimilar:')
        found=False
        for id,value in data_container.items(): #to get nested dictionary, one by one according to id
            if name.lower() in value['name'].lower(): #to get the only name key's value and check if input contains in the value (by iterate into string)
                 print(f"Name: {value['name']}, ID: {id}, Courses: {value['course']}")
                 found=True
        if not found: #if found = True, the 'not' will make it false, and will not print the statement, but if found = False then 'not' will make it True and print statement
            print('\nNo students found. --------👈')
    elif opt==7:
        id=int(input('\nEnter ID of the Student: '))
        if id in data_container:
            confirmation=input('Are you Sure? [yes or no]: ')
            if confirmation=='yes':
                del data_container[id]
                print('\nDeleted Succesfully --------👈')
            elif confirmation=='no':
                print('\nCancelled --------👈')
        else:
            print('\nStudent not exist --------👈')
    elif opt==8:
        if data_container != {}:
            course_count={}
            for id,dict in data_container.items():
                for course in dict['course']:
                    if course in course_count:
                        course_count[course]+=1 #IF COURSE IS ALREADY IN COURSE COUNT DICT, JUST INCREMENT IN ITS VALUE
                    else:
                        course_count[course]=1 #ADDING THE COURSE IN COURSE COUNT DICT AND SET TO 1
            for key,value in course_count.items(): #to print the course count dict
                print(f'\n{key}: {value} students')
        else:
            print('\nNo students in the system. --------👈')
    elif opt==9:
        backup=data_container.copy()
        print('\nBackup Created Succesfully --------👈')   
    elif opt==10:
        print('\nGoodBye --------👈')
        break
    else:
        print('\nInvalid selection, Please try again --------👈')