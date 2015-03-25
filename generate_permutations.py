import itertools


def feature_maker(filename,train):

	file_in = open(filename,'rt')
	file_out = open('filtered_'+filename,'wt')
	counter = 0
	#discard old header
	header = file_in.readline()
	print(header,file=file_out)
	for line in file_in:
		##get cards from the csv
		line = line.rstrip()
		row = line.split(',')
		row = [int(i) for i in row]
		card1 = row[0:2]
		card2 = row[2:4]
		card3 = row[4:6]
		card4 = row[6:8]
		card5 = row[8:10]
		poker_cat = row[10]
		
		##sort cards by the card value not suit
		orig_hand = [card1,card2,card3,card4,card5]
		orig_hand.sort(key=lambda x:x[1],reverse=True)
		all_hands = itertools.permutations(orig_hand)

		for hand in all_hands:
			for j in range(len(hand)):
				print(','.join([str(i) for i in hand[j]]),file=file_out,end=',')
			print(str(poker_cat),file=file_out)
		counter+=1
		print(counter)
	file_in.close()
	file_out.close()

feature_maker('train.csv',True)