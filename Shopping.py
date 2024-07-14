print("\t**Welcome To Reliance**\n")
print("Products are:\n")
print("1)Telivision\n2)Sports\n3)Mobiles\n4)Exit\n")


a=0
b=0
c=0
u=0
y=0
z=0
j=0
k=0
q=0
w=0
e=0
i=0
o=0
p=0

while b!=4:
    a=int(input("select Option:\n"))
    if a==1:
        print("\n1)Samsung\n2)Sony\n3)LG\n4)Back to Menu\n")
        while c!=4:
            c=int(input("\nSelect One:\n"))
            if c==1:
                print("\n1)SAMSUNG\n2)55inches\n3)price : 80000\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while z<2:
                    z=int(input("\nSelect one:\n"))
                    if z==1:
                        print("\nOrder is Placed\n")
                        print("\nSelect Option:\n1)Samsung\n2)Sony\n3)LG\n4)Back To Menu\n")
                        break
                    else:
                        print("\nBack To Menu!!\n1)Samsung\n2)Sony\n3)LG\n4)Back To Menu\n")
            elif c==2:
                print("\n1)SONY\n2)35 inches\n3)price : 67000\n4)Back to menu\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while j<2:
                    j=int(input("\nSelect One:\n"))
                    if j==1:
                        print("\norder is Placed\n\nSelect Option:\n1)Samsung\n2)Sony\n3)LG\n4)Back to Menu\n")
                        break
                    else:
                        print("\nback to Menu\n")
                        print("\nSelect Option:\n1)Samsung\n2)Sony\n3)LG\n4)Back to Menu\n")
                    
            elif c==3:
                print("\n1)LG\n2)50 inches\n3)price : 75000\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while k<2:
                    k=int(input("Select One:\n"))
                    if k==1:
                        print("\norder is Placed\nSamsung\n2)Sony\n3)LG\n4)Back to Menu\n")
                    else:
                        print("\nBack To Menu!!\nSamsung\n2)Sony\n3)LG\n4)Back to Menu\n")    
            else:
                print("\nback to Main Page!!\n")
                
        print("\n1)Telivision\n2)Sports\n3)Mobiles\n4)Exit\n") 
        
    elif a==2:
        print("***Sports***")
        print("\n1)Cricket\n2)Soccer\n3)Badminton\n4)Back To menu\n")
        while u!=4:
            u=int(input("\nselect one:\n"))
            if u==1:
                print("\n1)JERSEY :5000\n2)Kit : 3000\n3)discount :400\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while q<2:
                    q=int(input("\nSelect one:\n"))
                    if q==1:
                        print("\nOrder is Placed\n1)Cricket\n2)Soccer\n3)Badminton\n4)Back To Menu\n")
                        break
                    else:
                        print("\nBack To Menu!!\n")
                        print("\n1)Cricket\n2)Soccer\n3)Badminton\n4)Back To Menu\n")
                   
            elif u==2:
                print("\n1)Ball price : 6000\n2)jersey : 2800\n3)discount : 500\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while w<2:
                    w=int(input("Select one:"))
                    if w==1:
                        print("\norder is Placed!\n1)cricket\n2)Soccer\n3)Badminton\n4)Back To Menu\n")
                        break
                    else:
                        print("Back To Menu!!\n1)cricket\n2)Soccer\n3)Badminton\n4)Back To menu\n")
            elif u==3:
                print("\n1)Bat and Ball : 9000\n2)discount : 600\n")
                print("\n1)Place Your Order\n2)Back To Menu\n")
                while e<2:
                    e=int(input("Select one:"))
                    if e==1:
                        print("\nOrder is Placed\n1)cricket\n2)Soccer\n3)Badminton\n4)Back To Menu\n")
                        break
                    else:
                        print("\nBack to Menu!!\ncricket\n2)Soccer\n3)Badminton\n4)Back To Menu\n")
            else:
                print("\nBack To Main Page!!")
                       
        print("\n1)Telivision\n2)Sports\n3)Mobiles\n4)Exit\n")  
        
    elif a==3:
        print("**Mobiles**")
        print("\n1)Oneplus Nord\n2iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back to Menu\n")
        while y<4:
            y=int(input("Select One:"))
            if y==1:
                print("\n1)OnePlus Nord\n2)price : 29000\n3)discount : 4000\n")
                print("\n1)place Your Order\n2)Back To Menu\n")
                while i<2:
                    i=int(input("Select One:\n"))
                    if i==1:
                        print("\nOrder is Placed\n1)Oneplus\n2)iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back to Menu\n")
                        break
                    else:
                        print("\nBack to Menu\n1)Oneplus\n2)iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back To menu\n")
                        
            elif y==2:
                print("\n1)iqoo Neo 7 pro\n2)price : 38000\n3)discount : 5000\n")
                print("\n1)place your Order\n2)Back To Menu\n")
                while o<2:
                    o=int(input("Select one:"))
                    if o==1:
                        print("\nOrder is Placed\n1)Oneplus\n2)iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back To Menu")
                        break
                    else:
                        print("\nBack to Menu\n1)Oneplus\n2)iqoo Neao7pro\n3)Samsung s23Ultra\n")
            elif y==3:
                print("\n1)Samsung s23ultra\n2)Price : 124000\n3)Discount : 14000\n")
                print("\n1)place your Order\n2)Back To Menu\n")
                while p<2:
                    p=int(input("select One:"))
                    if p==1:
                        print("\nOrder is Placed\n1)Oneplus\n2iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back To Menu\n")
                        break
                    else:
                        print("\nBack to Menu\n1)Oneplus\n2iqoo Neao7pro\n3)Samsung s23Ultra\n4)Back to Menu\n")
                        
        print("\n1)Telivision\n2)Sports\n3)Mobiles\n4)Exit\n")  
        
    elif a==4:
        print("***Thank You For Visiting***")
    else:    
        print("invalid Choose Correct Option!!")
