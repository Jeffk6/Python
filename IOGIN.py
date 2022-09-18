password = "123456789"
email = "killed-jeff@gmail.com"

Imail = (input("mail: "))
Ipass = (input("pass: "))

if Ipass == password and Imail == email:
    print("Wait to go to the page")
    
if Ipass != password and Imail != email:
    print("the email and password error")
    
if Ipass == password and Imail != email:
    print("the email error")
    
if Ipass != password and Imail == email:
    print("the password error")