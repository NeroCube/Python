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
	if demand != 8:
		raise Exception('demand must is 8')

	for x in range(0, demand + 1):
		probability = float(input())
		if not (0 <= probability <= 1):
			print '>>>',probability
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
	#0, 1, ....., demand
	for now_demand in range(0, demand + 1):
		temp_probability = 0.0
		benefit = 0
		if now_demand == 0:
			benefit = 0
		else:
			for j in range(0,now_demand):
				temp_probability += probabilitys[j]
				benefit += j * retail_price * probabilitys[j]
			benefit += now_demand * retail_price * (1 - temp_probability)
			benefit -= now_demand * purchase_costs 
		if benefit > max_benefit:
			max_benefit = benefit
			optimize_amount = now_demand

	print optimize_amount, int(max_benefit)
