probabilitys = []
result = {'optimize_amount': 0,'max_benefit': 0}

try:
    purchase_costs = int(raw_input())
    if not (1 <= purchase_costs <= 100):
        raise Exception('purchase_costs need between 1 ~ 100')

    retail_price = int(raw_input())
    if not (1 <= retail_price <= 100):
        raise Exception('retail_price need between 1 ~ 100')
    if purchase_costs > retail_price:
        raise Exception('purchase costs should not be greater than retail_price')

    demand = int(raw_input())
    if demand != 8:
        raise Exception('demand must is 8')
    # Sold 0 ~ 8 individual possibilities
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
        sell_probability = 0.0
        benefit = 0

        for sell_num in range(purchase_num):
                sell_probability += probabilitys[sell_num]
                benefit += sell_num * retail_price * probabilitys[sell_num]
            
        benefit += purchase_num * retail_price * (1 - sell_probability)
        benefit -= purchase_num * purchase_costs

        if benefit > result['max_benefit']:
            result['max_benefit'] = benefit
            result['optimize_amount'] = purchase_num

    print result['optimize_amount'], int(result['max_benefit'])
