#------FOLLOW THE INSTRUCTIONS TO RUN SAFELY WITHOUT ANY ERROR
#program is almost error free but better if you follow the program needs while running 🙂

cart=[]
while True:
    print('\n1. add item to cart \n2. insert item at specific position \n3. remove a item \n4. Undo purchase (remove recently added item \n5. show current cart \n6. empty the entire cart \n7. count total items in cart \n8. exit)')
    ch=int(input('\nplz select an option?: '))
    if ch==1:
        i=0
        while i==0:
            item=input('\nwhat item?: ')
            cart.append(item)
            i=int(input('\n(0) -> keep Add \n(9) -> Stop adding: '))
            if i==9:
                break
        print('-----------')
    if ch==2:
        item=input('\nwhat item to insert: ')
        posi=int(input('position?: '))
        if posi>len(cart):
            cart.insert(posi,item)
            print('\nsorry posi is exceeding the cart size \nINSERTED ITEM at the end---------')
        else:
            print('  INSERTED SUCCESFULLY ----------')
    if ch==3:
        item=input('\nitem to remove?: ')
        if item in cart:
            cart.remove(item)
            print('\n  REMOVED ITEM SUCCESFULLY ----------')
        else:
            print('\nitem not in cart ----------')
    if ch==4:
        if cart!=[]:
            cart.pop()
            print('\n UNDO PURCHASE SUCCESFULY--------')
        else:
            print('\nEmpty cart! please add item first----------')
    if ch==5:
        print('\n',cart,' <- CURRENT CART VIEW--------')
    if ch==6:
        cart.clear()
        print('EMPTY CART SUCCESFULLY----------')
    if ch==7:
        print('\n',len(cart),' <- TOTAL ITEM IN CART--------')
    if ch==8:
        break
    else:
        print('PLEASE SELECT CORRECT OPTION NUMBER---------')
