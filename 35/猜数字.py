import random
import easygui as ui

while 1:
	result=random.randint(1,10)
	
	while 1:
		number=ui.integerbox('猜一猜当前产生的随机数是多少？')
		if number == result:
			ui.msgbox('猜对了')
			break
		elif number < result:
			ui.msgbox('小了')
		else:
			ui.msgbox('大了')
	if ui.ynbox('是否继续游戏'):
		pass
	else:
		break
