import random
r = random.randint(1,100)
while True :
	n = input('請輸入一個數字: ')
	n = int(n)
	if n == r:
		print('答對了')
		break
	elif n > r:
		print('比答案大')
	elif n < r:
		print('比答案小')
