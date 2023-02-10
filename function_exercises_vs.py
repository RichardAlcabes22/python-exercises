# 1 define is_two which checks that input == 2 or '2'

def is_two(n):
    if n == 2:
        return True
    elif n == '2':
        return True
    else:
        return False

is_two(3)

# 2 define is_vowel check if char is vowel or not

def is_vowel(x):
    vowels = ['a','e','i','o','u']
    if x.lower() in vowels:
        return True
    else:
        return False
    
    

is_vowel('i')

# 3 is_consonant checks if char is a consonant MUST USE is-vowel function

def is_consonant(x):
    return not is_vowel(x)

is_consonant('r')

# 4 define function that accepts a string as a word...it should capitalize 1st letter if word NOT is_vowel

def capitalz(stringy):
    if is_vowel(stringy[0]) == False:
        return stringy.capitalize()
    else:
        return stringy

capitalz('error')

capitalz('terror')

# 5 define calc_tip to accept a tip_pct and bill_amt and RETURN tip_amt

def calc_tip(tip_pct,bill_amt):
    tip_amt = tip_pct * bill_amt
    return round(tip_amt,2)

calc_tip(0.2,56)

# 6 define apply_disc accept original price, disc_pct RETURN new_price
def apply_disc(org_price,disc_pct):
    new_price = org_price - (org_price * disc_pct)
    return round(new_price,2)

apply_disc(74,0.14)

# 7 define handle_commas accepts a String that is numerical and contains commas-RETURN a number: no commas
import re
def handle_commas(num_string):
    char_list = num_string.split(',')
    new_num = ''.join(char_list)
    return new_num

handle_commas('121,222,001')

handle_commas('12,001')

num = '120,000,001'
char_list = num.split(',')
char_list
new_num = ''.join(char_list)
new_num

# 8 define function get_letter_grade accept a number RETURN letter grade

def get_letter_grade(n):
    if n >= 94:
        return 'A'
    elif n >= 84:
        return 'B'
    elif n >= 74:
        return 'C'
    elif n >= 64:
        return 'D'
    else:
        return 'F'
    

get_letter_grade(67)

#9 define remove_vowels accept String RETURN string with no vowels
import re
def remove_vowels(st):
    new_st = re.sub('[aeiouAEIOU]','',st)
    return new_st

remove_vowels('hjkdhewilhuweliu')

remove_vowels('iiiiooooouuuuuwwwwiiii')

# 10 Define normalize_name acept String RETURN valid python operator:
import re

def normalize_name(st):
    st2 = st.lower().strip()
    st3 = re.sub(' ','_',st2)
    st4 = st3.replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('%', '').replace('^', '').replace('&', '').replace('*', '').replace('.', '').replace(',', '')
    return st4

# normalize_name(string)

string = '    rtrurytridn.@!!& , 23AA    '  
strung = string.lower().strip()
strung

str3 = re.sub(' ','_',strung)
str3

# 11 define cm_sum accepts list of numbers RETURN list of running totals
def cm_sum(l_nums):
    new_nums = []
    counter = 0
    for n in l_nums:
        counter += n
        new_nums.append(counter)
# run_sums = [l_nums[n] + l_nums[n] for n in range(len(l_nums))]
    return new_nums

xl = list(range(3,15,2))
xl

cm_sum(xl)

