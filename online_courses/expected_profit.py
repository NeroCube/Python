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

	order_amount = int(input())

	for x in range(1,10):
		probability = round(float(input()),2)
		if not (0 <= probability <= 1):
			raise Exception('probability need between 0 ~ 1')
			break
		probabilitys.append(probability)
except NameError as e:
	print 'input value is not integer type'
except Exception as e:
	print e
else:
	temp_probability = 0.0
	benefit = 0.0
	for j in range(0,order_amount):
		temp_probability += probabilitys[j]
		benefit +=  ((j * retail_price) - (order_amount * purchase_costs)) * probabilitys[j]
	benefit += order_amount * (retail_price - purchase_costs) * (1 - temp_probability)
	print int(benefit)
