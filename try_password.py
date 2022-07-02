i = 3
psw = 'a123456'
while True:
	guess = input('請輸入密碼 : ')
	if guess != psw:
		print('密碼錯誤! 還有', i-1, '次機會')
		i-=1
		if i == 0:
			break
	else:
		print('登入成功!')
		break