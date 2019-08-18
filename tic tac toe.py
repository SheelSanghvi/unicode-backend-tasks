
def play(p1,p2):
	d={'1':' ','2':' ','3':' ','4':' ','5':' ','6':' ','7':' ','8':' ','9':' '}
	win=False
	flag=True
	while(win==False):		#to run till game doesnt end or someone wins
		while(True):		#to take position and check if ok
			a=input('choose your next position (1-9): ')
			if d[a]!=' ':
				print(' position already occupied, print other position: ')
			else:
				break

		if flag==True:		#to enter p1 and p2 alternate
			d[a]=p1
			s1={}
		else:
			d[a]=p2
		print('        |     |     ')
		print('     {}  |  {}  |  {}  '.format(d['7'],d['8'],d['9']))
		print('        |     |     ')
		print('   -----------------')
		print('        |     |     ')
		print('     {}  |  {}  |  {}  '.format(d['4'],d['5'],d['6']))
		print('        |     |     ')
		print('   -----------------')
		print('        |     |     ')
		print('     {}  |  {}  |  {}  '.format(d['1'],d['2'],d['3']))
		print('        |     |     ')
		flag= not flag

		#CHECK WIN CONDITION
		if d['1']==d['2']==d['3']!=' ' or d['4']==d['5']==d['6']!=' ' or d['7']==d['8']==d['9']!=' ' or d['1']==d['4']==d['7']!=' ' or d['2']==d['5']==d['8']!=' ' or d['3']==d['6']==d['9']!=' ' or d['1']==d['5']==d['9']!=' ' or d['3']==d['5']==d['7']!=' ':
			if flag==False:
					print(' Winner is Player 1: {}'.format(p1))
			else:
					print('Winner is Player 2: {}'.format(p2))
			win=True
		elif ' ' not in d.values():
			print('its a tie')
			win=True
		else:
			pass		

def main():
	p1=input("Enter your choice Player 1: 'X' or 'O'")
	while(True):
		if p1=='X' or p1=='x':
			p2='O'
			break
		elif p1=='o' or p1=='O':
			p2='X'
			break
		else:
			print("invalid input: please enter either 'X' or 'O'")
			p1=input("Enter your choice Player 1: 'X' or 'O'")
	p1=p1.upper()		
	print('Player 1 is {} and Player 2 is {}'.format(p1,p2))
	print('Player 1 plays first')
	play(p1,p2)


main()
while(True):
	again=input("Do you want to play again? 'Y' for yes and 'N' for no ")
	if again=='Y' or again=='y':
		main()
	else:
		print('Thanks for playing!')
		break