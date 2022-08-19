import string

# 1. Must be 15 or more characters 
# 2. Must have at least one punctuation mark
# 3. Must not have any numbers
# 4. Must not have any capital letters
# 5. Must have an accented letter

def user_password():
  password = str(input(
    """
    1. Must be 15 or more characters 
    2. Must have at least one punctuation mark
    3. Must not have any numbers
    4. Must not have any capital letters
    5. Must have an accented letter
    
    """
    
    'Please create a password:'))
    
  return password
  
def check_length(password):
  good_password = True 
  if len(password) < 15:
    good_password = False
    print("must be 15")
  return good_password
  
def check_punctuation(password):
  good_password = False 
  for char in password:
    if char in string.punctuation:
      good_password = True
      break
    
  if not good_password:
    print("must have a punctuation")
    
  return good_password
    
def check_numbers(password):
  good_password = True
  for char in password:
    if char.isdigit():
      good_password = False
      print("must not have numbers")
      break
      
  return good_password
    
def check_capital_letters(password):
  goodpassword = True
  for char in password:
    if char.isupper():
      goodpassword = False
      print("must not include capital letter")
      break
    
  return goodpassword
  
def check_accented_letters(password):
  goodpassword = False
  for char in password:
    if char not in string.printable:
      goodpassword = True
      break
    
  if not goodpassword:
    print("must include accented letter")
    
  return goodpassword
    
password = user_password()
rule_1 = check_length(password)
rule_2 = check_punctuation(password)
rule_3 = check_numbers(password)
rule_4 = check_capital_letters(password)
rule_5 = check_accented_letters(password)


