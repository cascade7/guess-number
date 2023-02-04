import random
r = random.randint(1,100)
count=0
while True :
	count += 1
	n = input('請輸入一個數字: ')
	n = int(n)
	if n == r:
		print('答對了')
		print('這是你猜的', count, '次')
		break
	elif n > r:
		print('比答案大')
	elif n < r:
		print('比答案小')
	print('這是你猜的', count, '次')
