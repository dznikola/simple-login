

username = "nikola"
password = "12345678"

while username:
    #asking to input username and password
     name = input("input username: ")
     pass1 = input("input password: ")

     #if password and username are correct
     if name == username and pass1 == password:
         print("Login succesful!")
         break

     #if password is incorrect
     elif name == username and pass1 != password:
         print("Wrong password, please try again")
         pass2 = input("input password: ")
         if pass2 == password:
             print("Login succesful")
             break
         else:
             pass2
             

     #wrong username
     elif name != username and pass1 == password:
         print("wrong username")

     else:
         print("wrong username and password")
         break
