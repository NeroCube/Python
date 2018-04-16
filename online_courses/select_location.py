import math
import copy
# Parser string "town_num pick_num distance" to dict
def base_station_settings_info(input_str):
	names = ['town_num', 'pick_num', 'distance']
	valus = [int(x) for x in input_str.split(" ")]

	if len(valus) != 3:
		raise Exception('input format error')
	if not (2 <= valus[0] <= 100):
		raise Exception('input n need between 2 ~ 1000 (include)')
	if not (2 <= valus[1] <= valus[0]):
		raise Exception('input p need between 2 ~ n (include)')

	return dict(zip(names, valus))
# Parser string "position_x position_y person_num" to dict
def town_info(input_str):
	names = ['x', 'y', 'person']
	valus = [int(x) for x in input_str.split(" ")]

	if len(valus) != 3:
		raise Exception('input format error')
	if not (-100 <= valus[0] <= 100):
		raise Exception('input position_x need between -100 ~ 100 (include)')
	if not (-100 <= valus[1] <= 100):
		raise Exception('input position_y need between -100 ~ 100 (include)')
	if not (1 <= valus[2] <= 100):
		raise Exception('input person_num need between -100 ~ 100 (include)')

	return dict(zip(names, valus))
# Calculate the distance between two points
def distance(p0, p1):

    return math.sqrt((p0['x'] - p1['x'])**2 + (p0['y'] - p1['y'])**2)

town_list = []
result = {'pick_town_list': [], 'cover_person': 0}

try:
	select_info = base_station_settings_info(raw_input())

	for i in range(select_info['town_num']):
		town = town_info(raw_input())
		town.update({'order': (i + 1),'cover_town_list': [],'cover_person': 0})
		town_list.append(town)

except ValueError as e:
	print 'input value is value type error'
except Exception as e:
	print e
else:
	# Calculate the number of towns and people covered by each base station
	for selected_town in town_list:
		for compare_town in town_list:
			if distance(selected_town, compare_town) <= select_info['distance']:
				selected_town['cover_town_list'].append(compare_town['order'])
				selected_town['cover_person'] += compare_town['person']

	for pick_order in range(select_info['pick_num']):
		# We need deepcopy to avoid changing this variable along with the original object
		max_cover_town = copy.deepcopy(max(town_list, key=lambda x:x['cover_person']))
		result['pick_town_list'].append(max_cover_town['order'])
		result['cover_person'] += max_cover_town['cover_person']
		
		for update_town in town_list:
			# Keep in update_town covered but not in max_cover_town,
			update_town['cover_town_list'] = list(set(update_town['cover_town_list']) - set(max_cover_town['cover_town_list']))
			update_town['cover_person'] = 0

			for town_order in update_town['cover_town_list']:
				# index start with 0
				update_town['cover_person'] += town_list[town_order - 1]['person']
	
	print ' '.join(map(str, result['pick_town_list'])), result['cover_person']


	
