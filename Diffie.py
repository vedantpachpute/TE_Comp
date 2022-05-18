p=int(input("Enter Prime Number P:"))
q=int(input("Enter Prime Number Q:"))
a=int(input("Enter Private Key of Vedant:"))
b=int(input("Enter Private Key of ICEM:"))
V=(q^a)%p
I=(q^b)%p
print("Exchange of Keys")
V_Key=(V^a)%p
I_Key=(I^b)%p
print("Vedants Secret Key is",V_Key)
print("ICEMs Secret Key is",I_Key)