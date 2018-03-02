probabilitys = []
result = 0.0

try:
	purchase_costs = int(input())
	if not (1 <= purchase_costs <= 100):
		raise Exception('purchase_costs need between 1 ~ 100')

	retail_price = int(input())
	if not (1 <= retail_price <= 100):
		raise Exception('retail_price need between 1 ~ 100')
	if purchase_costs > retail_price:
		raise Exception('purchase costs should not be greater than retail_price')

	demand = int(input())
	remaining_value = int(input())
	#0, 1, ....., demand
	for x in range(0, demand + 1):
		probability = float(input())
		if not (0 <= probability <= 1):
			raise Exception('probability need between 0 ~ 1')
			break
		else:
			probabilitys.append(probability)
except NameError as e:
	print 'input value is not defined'
except ValueError as e:
	print 'input value is not value type error'
except Exception as e:
	print e
else:
	max_benefit = 0
	optimize_amount =0 
	#0, 1, ....., demand, i is now_demand
	for i in range(0, demand + 1):
		temp_probability = 0.0
		benefit = 0
		if i == 0:
			benefit = 0
		else:
			# j is now sell number
			for j in range(0,i):
				temp_probability += probabilitys[j]
				benefit += j * retail_price * probabilitys[j]
				benefit += (i - j) * remaining_value * probabilitys[j]

			benefit += i * retail_price * (1 - temp_probability)
			benefit -= i * purchase_costs 
		if benefit > max_benefit:
			max_benefit = benefit
			optimize_amount = i

	print optimize_amount, int(max_benefit)

