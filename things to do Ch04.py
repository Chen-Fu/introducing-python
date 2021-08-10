'''
4.1 Choose a number between 1 and 10 and assign it to the variable secret. Then,
select another number between 1 and 10 and assign it to the variable guess. Next,
write the conditional tests (if, else, and elif) to print the string 'too low' if guess
is less than secret, 'too high' if greater than secret, and 'just right' if equal to
secret.
'''
secret = 7
x = input('select another number between 1 and 10:')
try:
  if int(x) < secret:
    print('Too low!')
  elif int(x) > secret:
    print('Too high!')
  else:
    print('just right!')
except:
  print('There are some problems in your inputs!')
    
'''
4.2 Assign True or False to the variables small and green. Write some if/else state‐
ments to print which of these matches those choices: cherry, pea, watermelon,
pumpkin
'''
small = True
green = False

if small:
    if green:
      print('pea') #small and green
    else:
      print('cherry') #small but not green
else:
    if green:
      print('watermelon') #big and green
    else:
      print('pumpkin') #big but not green
