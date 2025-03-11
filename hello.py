def square(z):
	print("{} 的平方為 {}".format(z, z*z)) 



X = int(input("請輸入一個數字"))

print("您輸入的是",X)

if(X<0):
	print("您輸入的值為負數")

elif(X==0):
	print("您輸入的值等於0")

else:
	for i in range(3,X+1):
		square(i)

