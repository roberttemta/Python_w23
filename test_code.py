Eml= input ("please inter your email_address ").strip()
while "@" not in  Eml or (len(Eml))<7 or "." not in Eml:
   print("Emailaddress incorect: Please enter a correct emailaddress: ")
   Eml= input ("please inter your email_address ").strip()
print("valide emailaddress")