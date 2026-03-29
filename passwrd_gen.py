import random
n=int(input("How many characters do u need?: "))
alphabets= "qwertyuiopasdfghjklzxcvbnmQRTYUIOPASDFGHJKLZCVBNM[]{|;':,./<>?1234567890!@#$%^&*()"
a= random.sample(alphabets, k=n)
x="".join(a)
print("The generated password: ", x)
