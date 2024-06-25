
 
class bank_account():  
    def __init__(self):
            self.dictionary={"Sriphalya":[40834 ,4455 ,25890 ],"Satya":[141204 ,1984 , 29890 ],
                        "Jai":[40834 ,2266 ,35890 ],"Safreen ruhi":[140403 ,5599 ,15890 ]}       
    def passcheck(self,q):
        if (len(q)<8):
            return False
        else:
            l,u,s,d=0,0,0,0
            for i in q:
                if(i.islower()):
                    l+=1
                elif(i.isupper()):
                    u+=1
                elif (i.isdigit()):
                    d+=1
                else:
                    s+=1
            if l>=1 and u>=1 and d>=1 and s>=1:
                return True
            else:
                return False
            

    def displaybalance(self,name,t):
        name=name
        t=t
        print("would you like to display balance ? enter 1-for yes 2-for no")
        b=int(input())
        if b==1:
            print(self.dictionary[name][2]-t)
            print("thankyou. your session is expired ")
        else:
            print("thankyou. your session is expired ")
            
    def withdrawl(self,name):
        name=name
        print("enter the amount :")
        amount=int(input())
        print("enter pin")
        pin=int(input())
        if self.dictionary[name][1]==pin :
            print("checking balance")
            if amount<self.dictionary[name][2]:
                print("collect the cash")
                self.displaybalance(name,amount)
            else:
                print("insufficient balance")
                print("end")

        else:
            print("pin is wrong")
            print("end")
        
        
        
    def changepassword(self,name):
        name=name
        print("enter current password :")
        p=int(input())
        if self.dictionary[name][0]==p:
            print("enter new password :")
            q=input()
            print("re-enter password :")
            r=input()
            if q==r:
                if self.passcheck(q):
                    print("password is strong and changed successfully")
                else:
                    print("password is not strong!, Please make sure password is greater tha 7 chars and include 1 lowercase 1 uppercase and 1 digit ")
                    self.changepassword(name)
            else:
                print("new password is not matched with re-entered password")
                self.changepassword(name)
        else:
            print("password is wrong")
            print("end")
            
            
    def balance(self,name):
        name=name
        print("enter pin")
        pin=int(input())
        if self.dictionary[name][1]==pin :
            print("the balance is ",self.dictionary[name][2])
        else:
            print("pin is wrong")
            print("end")


    def deposit(self,name):
        name=name
        print("enter the amount :")
        amount=int(input())
        print("enter pin")
        pin=int(input())
        if self.dictionary[name][1]==pin :
            print("cash is deposited")
            print("would you like to display balance ? enter 1-for yes 2-for no")
            b=int(input())
            if b==1:
                print(self.dictionary[name][2]+amount)
            else:
                print("thankyou. your session is expired ")
        else:
            print("pin is wrong")
            print("end")
            
    def activity(self,name):
        name=name
        print("select the activity you want to perform")
        print("1-withdrawl 2-deposit 3-balance 4-change password")
        act=int(input())
        if act == 1:
            self.withdrawl(name)
        elif act==2:
            self.deposit(name)
        elif act==3:
            self.balance(name)
        elif act==4:
            self.changepassword(name)
        else:
            print("invalid input")
            self.activity(name)


    def ps(self,name):
        name=name
        print("enter password")
        password=int(input())
        p=self.dictionary[name][0]
        if  p==password:
            print('password is correct')
            self.activity(name)
            
        else:
            for i in range(2,0,-1):
                print("password entered is wrong only",i,'attempts are left')
                password1=int(input())
                print(self.dictionary[name][0],password1)
                if self.dictionary[name][0]==password1:
                    print('password is correct')
                    self.activity(name)
                    
            print("password is wrong. Account is blocked")


    def user_name(self):
        print("enter username :")
        name=input()
        if name in self.dictionary.keys():
            self.ps(name)
            
        else:
            print("user not existing")
            print('end')
            
    def user(self):
        print("enter username :")
        name=input()
        if name in self.dictionary.keys():
            # ps(name)
            print("True")
            
        else:
            print("user not existing")
            print('end')

A=bank_account()       
A.user_name()