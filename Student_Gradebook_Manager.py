print('\n--WELCOME TO GRADEBOOK MANAGER--\n')

gb={}

while True:
    print('\n1. View all students and grades',
      '\n2. Add a new student',
      '\n3. Update a student grade',
      '\n4. Delete a student (by name)',
      '\n5. Get a student grade (safe lookup)',
      '\n6. Check if a student exists',
      '\n7. Add a student ONLY if they dont already exist (setdefault)',
      '\n8. Remove the last added student',
      '\n9. Count total students',
      '\n10. Copy the gradebook (backup)',
      '\n11. Clear all grades',
      '\n12. Exit')
    opt=int(input('\nplease select an option: '))
    
    if opt==1:
        if gb != {}:
            for key,value in gb.items():
                print(key,':',value)
        else:
            print('\nEmpty GradeBook-------')
            
    elif opt==2:
        name=input('Enter student name: ')
        grade=int(input('Enterr student grade: '))
        
        gb.update({name:grade})
        
        print('\nAdded Succesfully-------')
        
    elif opt==3:        
        if gb != {}:
            name=input('PS: names are capitalized, no whitespaces alowed  \nwhich Student?: ').lower().strip()
            upgrade=int(input('Updated Grade: '))
            safegb={k.lower():v for k,v in gb.items()}
            if name in safegb:      #to check if key is in dict
                for k in gb:    #to access keys in dict
                    if name==k.lower():     #to get exact required key in original dict
                        gb.update({k:upgrade})      #to update the value of required key in original dict
                        print('\nUpdated Grade Succesfully------')
            else:
                print('\nStudent Not Found------')
        else:
            print('\nEmpty GradeBook-------')
            
    elif opt==4:   
        if gb != {}:
            name=input('PS: names are capitalized, no whitespaces alowed \nwhich student?: ').lower().strip()  
            safegb={k.lower():v for k,v in gb.items()}   
            if name in safegb:
                for k in gb.keys():
                    if name==k.lower():
                        del gb[k]
                        print('\nDeleted Succesfully------')
                        break
            else:
                print('\nStudent Not Fouund------')
        else:
            print('\nEmpty GradeBook-------')
                    
    elif opt==5:
        name=input('PS: names are capitalized, no whitespaces alowed \nwhich student?: ')
        print(gb.get(name,'\nN/A-------'))
        
    elif opt==6:
        name=input('PS: names are capitalized, no whitespaces alowed \nwhich student?: ')
        print(('\nYes-----' if name in gb else '\nNo------'))
        
    elif opt==7:
        name=input('enter student name (capitalized & No whitespaces): ')
        g=int(input('enter grade: '))
        gb.setdefault(name,g)
        print('\nAdded Successfully--------')
        
    elif opt==8:
        if gb != {}:
            gb.popitem()
            print('\nRemoved the most recently added student------')
        else:
            print('\nEmpty GradeBook-------')
        
    elif opt==9:
        print('Total Students: ',len(gb))
        
    elif opt==10:
        if gb != {}:
            backup=gb.copy()
            print('\nBackup Ready------')
        else:
            print('\nEmpty GradeBook------')    
            
    elif opt==11:
        if gb != {}:
            gb.clear()
            print('\nCleared GradeBook Succesfully-------')
        else:
            print('\nAlready Empty GradeBook--------')
        
    elif opt==12:
        break
    
    else:
        print('\nPlease select valid option------')