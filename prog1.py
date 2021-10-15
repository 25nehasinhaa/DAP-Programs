import tensorflow as tf
#Initialize two constants
x1=tf.constant([10,18,6,40])
x2=tf.constant([5,6,7,8])

#Multiply
a=tf.add(x1,x2)
b=tf.subtract(x1,x2)
c=tf.multiply(x1,x2)
d=tf.divide(x1,x2)

#Print the result
print(a)
print(b)
print(c)
print(d)

name=input("Enter your name: ")
print(name)
USN=input("Enter your USN: ")
print(USN)