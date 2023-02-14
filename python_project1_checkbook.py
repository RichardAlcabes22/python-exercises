#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Python Project #1: Checkbook App
    -14 Feb 2023 Rich Alcabes
Goal:
    Create an Application that will allow users to track finances via a command line interface.

Current Functionality:
    - view current balance
    - add a credit transaction
    - add a debit transaction
    - view entire transaction history

Planned Functionality:
    - Create User README Doc
    - Prettify View All Transaction Output
    - modify existing transaction
    - view last N transactions
    - view Top N transactions filtered by Amount, Date, Type, etc...
    - view transaction history filtered by date, type, amount, description keywords,etc...
    - import .csv for use in Excel, Tableau, Power BI, QuickBooks, TurboTax, Farmville, etc...
    - option to re-initialize database while maintaining access to previous .csv iterations
    - admin maintanence access via special code like '99' or similar when entered as selection

Code Flow:
    1. Import required MODULES/PACKAGES/LIBRARIES
    2. Define GLOBAL Variables
    3. Define required FUNCTIONS
        Each FUNCTION will check to see if .csv exists and if not, shall create .csv
    4. Design and Implement INITIALIZATION of .csv (currently handled within each function) 
        Future iterations may consolidate .csv checks and utilize a one-time initialization feature
        outside of FUNCTION scripts to consolidate code.
    5. Design and Implement UI

Actual Flow in Typical Use Case:
    1. User opens .py file
    2. User makes a selection
    3. .csv file will be initialzed when user makes first_ever selection
    4. Functionality associated with selection will be performed
    5. User can close .py file and data will remain intact so long as .csv file exists
    
NB:
    1. Database will initialize with a 0.01 deposit for a total beginning balance of 0.01. The bank is
       apparently running a sign-up promo.
    2. Date_Time_Group is in YYYY.MM.DD.HH.MM. format GMT

'''

# 1. IMPORT REQ'd ModPackLib's

import os
import csv
import time
import sys

# 2. DEFINE GLOBAL VARIABLES (these are also local within each function)

local = time.gmtime()[0:5]
dtg = ''.join([str(i) + '.' for i in local]).strip('.')

cols = ['TRANS_ID','CATEGORY','AMOUNT','DESCR','DATETIME','BALANCE']
initialization_values = {
    'TRANS_ID': 1001,
    'CATEGORY': 'Initial Deposit',
    'AMOUNT': 0.01,
    'DESCR': 'DB Initialization',
    'DATETIME': dtg,
    'BALANCE': 0.01
}

# 3. DEFINE REQ'd FUNCTIONS

# FUNCTION for INITIALIZE .csv

def init_csv():
    print('initializing database...')
    with open('checkbook_data_prod.csv','w') as f:
        writer = csv.DictWriter(f,fieldnames=cols)
        writer.writeheader()
        writer.writerow(initialization_values)

# FUNCTION for CURRENT BALANCE

def curr_bal():
    if os.path.exists('checkbook_data_prod.csv'):
        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print('accessing database...')
        print('Your Current Balance: ' + '$' + lines[-1]['BALANCE'])
    else:
        init_csv()
        
    # prompt user to continue or quit
    go_again = input(f'Continue?: y/n?:  ')
    if go_again.lower() != 'y':
        cont = False
        print(f'Have a Wonderful Day')
        sys.exit('Goodbye!')
        

# FUNCTION for VIEW ALL TRANSACTIONS (the output is not pretty yet)

def all_trans():
    if os.path.exists('checkbook_data_prod.csv'):
        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print('accessing database...')
        print(lines[1:])
    else:
        init_csv()
        
    # prompt user to continue or quit    
    go_again = input(f'Continue?: y/n?:  ')
    if go_again.lower() != 'y':
        cont = False
        print(f'Have a Wonderful Day')
        sys.exit('Goodbye!')
            
# FUNCTION for ADDING CREDITS

def add_credit():
    if os.path.exists('checkbook_data_prod.csv'):
        print('accessing database.')
        print('accessing database..')
        
        cols = ['TRANS_ID','CATEGORY','AMOUNT','DESCR','DATETIME','BALANCE']
        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print('accessing database...')

        user_amount = input('Enter a Credit Amount: ')
        try:
            credit_flt = float(user_amount)
        except:
            credit_flt = str(user_amount)
            print('\n\nI don\'t have time to waste...  Next time, just enter a number.  Good Day to You!')
            #sys.exit('Goodbye!')
        if type(credit_flt) == str:
            sys.exit()
        user_descr = input('Enter a Short Description: ')
        local = time.gmtime()[0:5]
        dtg = ''.join([str(i) + '.' for i in local]).strip('.')

        values = dict(TRANS_ID = (int(lines[-1]['TRANS_ID']) + 1), CATEGORY = 'credit', AMOUNT = user_amount, 
                  DESCR = user_descr, DATETIME = dtg, 
                  BALANCE = round((float(lines[-1]['BALANCE']) + float(user_amount)),2)
                 )

        with open('checkbook_data_prod.csv','a') as f:
            writer = csv.DictWriter(f,fieldnames=cols)
            writer.writerow(values)

        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print(f'Succesfully ADDED ${user_amount} to your account.')
    else:
        init_csv()
        
    # prompt user to continue or quit   
    go_again = input(f'Continue?: y/n?:  ')
    if go_again.lower() != 'y':
        cont = False
        print(f'Have a Wonderful Day')
        sys.exit('Goodbye!')
            
# FUNCTION for SUBTRACTING DEBITS

def subtract_debit():
    if os.path.exists('checkbook_data_prod.csv'):
        print('accessing database.')
        print('accessing database..')
        
        cols = ['TRANS_ID','CATEGORY','AMOUNT','DESCR','DATETIME','BALANCE']
        with open('checkbook_data_test2.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print('accessing database...')
        
        user_amount = input('Enter a Debit Amount: ')
        try:
            debit_flt = float(user_amount)
        except:
            debit_flt = str(user_amount)
            
            print('\n\nI don\'t have time to waste...  Next time, just enter a number.  Good Day to You!')
            #sys.exit('Goodbye!')
        if type(debit_flt) == str:
            sys.exit()
        user_descr = input('Enter a Short Description: ')
        local = time.gmtime()[0:5]
        dtg = ''.join([str(i) + '.' for i in local]).strip('.')

        values = dict(TRANS_ID = (int(lines[-1]['TRANS_ID']) + 1), CATEGORY = 'debit', AMOUNT = user_amount, 
                  DESCR = user_descr, DATETIME = dtg, 
                  BALANCE = round((float(lines[-1]['BALANCE']) - float(user_amount)),2)
                 )

        with open('checkbook_data_prod.csv','a') as f:
            writer = csv.DictWriter(f,fieldnames=cols)
            writer.writerow(values)

        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print(f'Succesfully SUBTRACTED ${user_amount} from your account.')
    else:
        init_csv()
        
    # prompt user to continue or quit    
    go_again = input(f'Continue?: y/n?:  ')
    if go_again.lower() != 'y':
        cont = False
        print(f'Have a Wonderful Day')
        sys.exit('Goodbye!')

# FUNCTION for MODIFY ENTRY                
def mod_entry():
    if os.path.exists('checkbook_data_prod.csv'):
        with open('checkbook_data_prod.csv','r') as f:
            content = csv.DictReader(f,fieldnames=cols)
            lines = []
            for line in content:
                lines.append(line)
        print(f'\nFunctionality Under Construction...\nPlease Contact Your Local Customer Service for Further Assistance.')

    else:
        init_csv()
        
    # prompt user to continue or quit
    go_again = input(f'Continue?: y/n?:  ')
    if go_again.lower() != 'y':
        cont = False
        print(f'Have a Wonderful Day')
        sys.exit('Goodbye!')


# 4 INITIALIZE .csv FILE

if os.path.exists('checkbook_data_prod.csv'):
    print('accessing database...')
    cols = ['TRANS_ID','CATEGORY','AMOUNT','DESCR','DATETIME','BALANCE']
    with open('checkbook_data_prod.csv','r') as f:
        content = csv.DictReader(f,fieldnames=cols)
        lines = []
        for line in content:
            lines.append(line)
else:
    print('initializing database..')
    print('initializing database....')
    print('initializing database......')
    print('database initialized')
    with open('checkbook_data_prod.csv','w') as f:
        writer = csv.DictWriter(f,fieldnames=cols)
        writer.writeheader()
        writer.writerow(initialization_values)

# 5 DESIGN/IMPLEMENT UI
cont = True
while cont == True:
    print('\n\nWelcome to your Python Checkbook!' + '\n' +
          'What would you like to do today?')
    print(
          '\n' +
          '1 - View Current Balance' + '\n' +
          '2 - Record a Debit (- $)' + '\n' +
          '3 - Record a Credit (+ $)' + '\n' +
          '4 - View Transaction History' + '\n' +
          '5 - Modify a Transaction' + '\n' +
          '6 - Exit\n'
    )

    valid_choice = [1,2,3,4,5,6]
    num = 7
    while num not in valid_choice:
        user_choice = input('Enter a Selection:  ')
        try:
            num = int(user_choice)
        except ValueError:
            print('Please Try Again: Visualize Your Goal, and Be The Number!')
        if num > 6:
            print('Please Enter a Single Digit, 6 or Less:')
        elif num == 1:
            curr_bal()
        elif num == 2:
            subtract_debit()
        elif num == 3:
            add_credit()
        elif num == 4:
            all_trans()
        elif num == 5:
            print(f'\n************************\n********Functionality Under Construction...\nPlease Contact Your Local Customer Service for Further Assistance.***********\n****************')
        elif num == 6:
            print(f'Have a Fantastic Day')
            sys.exit('Goodbye!')
        

