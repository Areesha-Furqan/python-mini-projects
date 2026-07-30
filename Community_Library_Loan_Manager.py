coll=['Don Quixote',
      'A Tale of Two Cities',
      'The Little Prince',
      'The Alchemist',
      'The Harry Potter Series',
      'The Lord of the Rings',
      'The Hobbit',
      'Dream of the Red Chamber',
      'And Then There Were None',
      'The Lion, the Witch and the Wardrobe']
add=''

while True:
    print('\nCurrent Books Collection\n')
    for i in coll:
        print('-> ',i)
    print('\n1. Borrow a Book',
          '\n2. Return a Book',
          '\n3. Add a New Book',
          '\n4. Check Specific Book Availability',
          '\n5. Check total Available Books',
          '\n6. Check Recently Added Book',
          '\n7. Reorganize Coolection',
          '\n8. Clear the Collection (IF NEEDED)')
    opt=int(input('\nPlease select an option: '))
    
    if opt==1:
        bor=input('\nPS: make sure to write exact name 🙂 \nwhich Book?: ').lower().strip()
        l=[n.lower() for n in coll]
        if bor in l: #used list comprehension to make books names lowercase
            r=coll.pop(l.index(b)) #index of b in lower case version list will be index of original Book 
            print('\nBorrowed succesfully------')
        else:
            print('\ninvalid book name------\n')
    if opt==2:
        coll.append(r)
        print('\nReturned Succesfully------')
    if opt==3:
        add=input('enter the Book: ').strip()
        coll.append(add)
        print('\nAdded Succesfully------')
    if opt==4:
        av=input('\nPS: make sure to write exact name 🙂 \nwhich Book?: ').lower().strip()
        l=[n.lower() for n in coll]
        if av in l:
            print('\nYes, Available------')
        else:
            print('\nNot Available------')
    if opt==5:
        print('Total Books: ',len(coll),'-------')
    if opt==6:
        if add !='':
            print('\n',add,'------')
        else:
            print('\nNo recently added book-------')
    if opt==7:
        coll.sort()
        print('Reorganized Succesfully-------')
    if opt==8:
        coll.clear()
        print('Cleared Collection Succesfully-------')