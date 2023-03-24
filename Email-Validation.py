# Email-Validation using string functions

email = input("Enter Your Email:")

t,a=0,0
if len(email)>=6:                           #g@g.in
    if email[0].isalpha():
        temp=email.rfind(".")
        back_index=temp-len(email)
        if back_index==-4:
            temp1=email.count("@")
            if temp1==1:
                temp2=email.count(" ")
                if temp2==0:
                    if email.islower():
                        for i in email:
                            if i.isalnum() or i=="_" or i=="." or i=="@":
                                continue
                            else:
                                a=1
                        if a==1:
                            print("Wrong email(No use of special Characters)")
                        else:
                            print("Wright email")
                    else:
                        print("Wrong email(email must be in lowercase)")
                else:
                    print("Wrong email(No spaces in between)")
            else:
                print("Wrong email(their should be only one @)")
        else:
            print("Wrong email(position of dot is not correct)")
    else:
        print("Wrong email(must be started with alphabets)")
else:
    print("Wrong email(length is too short)")