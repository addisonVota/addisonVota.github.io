situation = ['burn', 'laceration']
print('\nWelcome to first aid simulator.\nPlease select a situation\n')

for i in situation:
  print('{} '.format(i), end='')
print('\n')

selection = input('Enter your situation: ')

if selection == "burn":
   print('okay now  you check if the area is safe.')
   
   print('okay now you put on gloves.')
   
   print('okay now you send frends to go get help.') 
   
   print('okay now  you bandage the burn and wait for help to arrive. ')
             

elif selection == "laceration":
  print('okay now you check if the area is safe.')
  
  print('okay now you put on gloves.')
  
  print('okay now you send frends to go get help.')
  
  print('okay now you bandage the laceration and wait for help to arrive and do not use a turnekit unless absolutly nessecary.  ')
             
    
    
    
    
    
