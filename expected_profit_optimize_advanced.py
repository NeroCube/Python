probabilitys = []
result = {'optimize_amount': 0,'max_benefit': 0}

try:
	purchase_costs = int(raw_input())
	if not (1 <= purchase_costs <= 100):
		raise Exception('purchase_costs need between 1 ~ 100 (include)')

	retail_price = int(raw_input())
	if not (1 <= retail_price <= 100):
		raise Exception('retail_price need between 1 ~ 100 (include)')
	if purchase_costs > retail_price:
		raise Exception('purchase costs should not be greater than retail_price')

	demand = int(raw_input())
	if not (1 <= demand <= 1000):
		raise Exception('demand need between 1 ~ 1000 (include)')
	
	remaining_value = int(raw_input())
	if not((1 <= remaining_value <= 100)):
		raise Exception('remaining_value need between 1 ~ 100 (include)')
	if remaining_value > purchase_costs:
		print 'remaining_value > purchase_costs'
		remaining_value = 113.87
	# Sold 0 ~ demand individual possibilities
	for purchase_num in range(demand + 1):
		probability = float(raw_input())
		if not (0 <= probability <= 1):
			raise Exception('probability need between 0 ~ 1')
			break
		else:
			probabilitys.append(probability)
except ValueError as e:
	print 'input value type error'
except Exception as e:
	print e
else:
	for purchase_num in range(demand + 1):
		# the probability of 0 ~ (demand-1)
		sell_probability = 0.0
		benefit = 0
		
		if purchase_num == 0:
			benefit = 0
		else:
			for sell_num in range(purchase_num):
				sell_probability += probabilitys[sell_num]
				benefit += sell_num * retail_price * probabilitys[sell_num]
				benefit += (purchase_num - sell_num) * remaining_value * probabilitys[sell_num]
			
			benefit += purchase_num * retail_price * (1 - sell_probability)
			benefit -= purchase_num * purchase_costs 
		
		if benefit > result['max_benefit']:
			result['max_benefit'] = benefit
			result['optimize_amount'] = purchase_num

	print result['optimize_amount'], int(result['max_benefit'])

