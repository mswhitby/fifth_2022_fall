import string

# 1. Must be 15 or more characters 
# 2. Must have at least one punctuation mark
# 3. Must not have any numbers
# 4. Must not have any capital letters
# 5. Must have an accented letter

password = str(input(
  """
  1. Must be 15 or more characters 
  2. Must have at least one punctuation mark
  3. Must not have any numbers
  4. Must not have any capital letters
  5. Must have an accented letter
  
  """
  
  'Please create a password:'))
  
good_password = False
  
print(len(password))

if len(password) >= 15:
  good_password = True
  # print('not good')
  
for char in password:
  if char in string.punctuation:
    good_password = True