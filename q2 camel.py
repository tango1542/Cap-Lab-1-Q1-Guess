phrase = input(str("Enter a word to turn it into camel case: \n"))

lphrase = (phrase.lower())  #making the whole phrase lower case

tphrase = lphrase.title()  #Capitalizing the first letter of each word

def downcase(x):           #making a function that lowercases only first char in string
    return x[0].lower() + x[1:]

fphrase = downcase(tphrase)  #running function

sphrase = fphrase.replace(" ","")  #removing white spaces from string

print (sphrase)


