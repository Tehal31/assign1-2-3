
def checking_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good') #added 4 bcz we have to delete poor also since we are excluding it in range
    return str1
  else:
    return str1
print(checking_poor('The lyrics is not that poor!'))
print(checking_poor('The lyrics is poor!'))