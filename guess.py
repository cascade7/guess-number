import random
start = input('請輸入起始值: ')
end = input('請輸入結束值: ')
start = int(start)
end = int(end)
r = random.randint(start,end)
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
