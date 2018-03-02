result = []
town_list = []
town_num = 0
pick_num = 0
distance = 0

try:
	temp_input = raw_input().split(" ")
	town_num = int(temp_input[0])
	pick_num = int(temp_input[1])
	distance = int(temp_input[2])
	for i in range(town_num):
		temp_input = raw_input().split(" ")
		town_list.append(
			{
			'x': int(temp_input[0]),
			'y': int(temp_input[1]),
			'person_num': int(temp_input[2]),
			}
		)
except NameError as e:
	print 'input value is not defined'
except ValueError as e:
	print 'input value is not value type error'
except Exception as e:
	print e
else:
	pass
