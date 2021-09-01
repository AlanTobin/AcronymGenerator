userinput = input('Put in a phrase which you want converted into an acronym. ')
listt = userinput.split()
acronym = ''

for i in listt:
  acronym = acronym + i[0].upper()
print (acronym)