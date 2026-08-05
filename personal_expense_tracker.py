
def print_menu():
    '''Print Menu of the System'''
    print('\n1. Add a Transaction',
          '\n2. View All Transactions',
          '\n3. View Summary of Expenses',
          '\n4. View Monthly Summary',
          '\n5. Delete Transaction',
          '\n6. Search a Transaction',
          '\n7. Set Monthly Budget',
          '\n8. Check Budget Status',
          '\n9. Exit')

def add_transaction(transactions_list):
    '''prompts user all details to add a transaction in dictionary'''
    desc=input('\nWrite Description: ').strip().capitalize()
    categ=input('Enter Category: ').strip().title()
    amt=abs(float(input('Enter Amount: ')))
    typ=input('Enter Type [Expense/Income]: ').strip().title()
    date=input('Enter Date [YYYY-MM-DD]: ')
    id=len(transactions_list)+1 #dynamically incrementing in the total transactions in the list
    t={
        'id':id,
        'description':desc,
        'category':categ,
        'amount':amt,
        'type':typ,
        'date':date
    }
    transactions_list.append(t)
    print('\nNew Transaction ----------')
    return transactions_list

def view_all_transactions(transaction_list):
    if transaction_list != []:
        for dict in transaction_list:
            print('------------')
            for key,value in dict.items():
                print(key,':',value)
    else:
        print('\nNo Transactions Recorded Yet ---------')
    return transaction_list

def view_summary_expenses(transaction_list):
    
    if transaction_list != []:
        summary_report={}
        for dict in transaction_list:
            if dict['type']=='Expense':
                if dict['category'] in summary_report:
                    summary_report[dict['category']]+=dict['amount']
                else:
                    summary_report[dict['category']]=dict['amount']
        for k,v in summary_report.items():
            print(k.title(),':',v)
    else:
        print('\nNo Transactions Recorded Yet ---------')
    return transaction_list

def monthly_summary(transaction_list):
    '''prompts user month and year and prints that month's summary of expenes and income'''
    if transaction_list != []:
        month=input('\nEnter a Month [MM]: ')
        year=input('Enter Year [YYYY]: ')
        my=year+'-'+month
        total_expenses=0
        total_income=0
        found=False
        for dict in transaction_list:
            date=dict['date']
            if date.startswith(my):
                found=True
                if dict['type']=='Income':
                    total_income+=dict['amount']
                else:
                    total_expenses+=dict['amount']
            else:
                continue
        if found:
            if total_income>total_expenses:
                net_savings=total_income-total_expenses
                print(f'\nTotal Income: {total_income}',
                      f'Total Expenses: {total_expenses}',
                      f'Net Savings: {net_savings}')
            else:
                print(f'\nTotal Income: {total_income}',
                      f'Total Expenses: {total_expenses}',
                       'Net Savings: 0')
        if not found:
            print('\nNo transactions for this month----------------')
        
    else:
        print('\nNo Transactions Recorded Yet ---------')
    return transaction_list

def delete_transaction(transaction_list):
    '''prompts user id and deletes that transaction'''
    id=int(input('\nTransaction ID: '))
    found=False
    for dict in transaction_list:
        if id==dict['id']:
            found=True
            conf=input('Are you sure [y/n]? ')
            if conf=='y':
                transaction_list.remove(dict) #if id matched, the index number in the list is used to delete the dict
                print('\nTransaction Deleted ---------')
                break
            elif conf=='n':
                print('\nCancelled ----------')
        
    if not found:
        print('\nTransaction not Found ----------')
    return transaction_list

def search_transaction(transaction_list):
    '''prompts user term to search transaction'''
    search=input('\nSearch [e.g Lunch/Food/Shopping etc]: ')
    found=False
    print('\nMatchings:')
    for dict in transaction_list:
        categ=dict['category'] 
        disc=dict['description']
        if search.lower() in categ.lower() or search.lower() in disc.lower():
            found=True
            print('-------------')
            for k,v in dict.items():
                print(k,':',v)
    if not found:
        print('\nNo Transaction with this term ----------')
    return transaction_list

def monthly_budget(transaction_list,budget_dict):
    '''prompts user category, month and budget and sets a budget for that category for that month'''
    categ=input('\nCategory? [e.g food/transport/shhopping] ').strip().capitalize()
    month=input('Month [e.g YYYY-MM] ').strip()
    bg=int(input('Budget: '))
    key=categ+'_'+month
    budget[key]=bg
    print('\nBudget Setted Succesfully-----------')
    return transaction_list,budget_dict

def check_budget_status(transaction_list,budget_dict):
    '''Prompt user specific month and outputs that months spents with respect to its budget'''
    if transaction_list!=[]:
        month=input('\nMonth [e.g YYYY-MM] ').strip()
        sum={}
        found=False
        for dict in transaction_list:
            if dict['type']=='Expense' and month in dict['date']:
                found=True
                key=dict['category']+'_'+month #making key for sum dict like food_2025-02
                if key in sum:
                    sum[key]+=dict['amount'] #check if it is already in sum dict, useful for 2nd iteration in summing
                else:
                    sum[key]=dict['amount'] #create a key and place the amount, the 2nd interation will increment in its  value
                
                
        if found:         
            for k,v in sum.items():
                print('\n-------------------')
                bg_found=False
                x=k.split('_')
                if month in x: # user's month is in sum dict (spent is calculated)
                    sp=v
                    print(f'\n{x[0]}',':',f'{sp} spent ',end='')
                for k2,v2 in budget_dict.items():
                    bg=v2
                    if k==k2: # user's month is in budget dict (has budget setted)
                        bg_found=True
                        print(f' out of {bg} Budget ',end='')
                        if sp>v2:
                            print('(Over Budget!)')
                        else:
                            print('(Under Budget)')
                if not bg_found:   
                    print('(No Budget set for this category)')
                        
                
        if not found:
            print('\nNo Transaction this Category ---------')
    else:
        print('\nNo Transaction recorded yet ---------')
    
    return transaction_list,budget_dict

def exit():
    print('\nGood Buy--------')

transactions=[]
budget={}

while True:
    print_menu()
    opt=int(input('\nPlease select an option: '))
    
    if opt==1:
        transactions=add_transaction(transactions)
    elif opt==2:
        transactions=view_all_transactions(transactions)
    elif opt==3:
        transactions=view_summary_expenses(transactions)
    elif opt==4:
        transactions=monthly_summary(transactions)
    elif opt==5:
        transactions=delete_transaction(transactions)
    elif opt==6:
        transactions=search_transaction(transactions)
    elif opt==7:
        transactions,budget=monthly_budget(transactions,budget)
    elif opt==8:
        transactions,budget=check_budget_status(transactions,budget)
    elif opt==9:
        exit()
        break
    else:
        print('\nInvalid Selection Plz Try Again-----------')