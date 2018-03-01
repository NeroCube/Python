denomination = [500, 100, 50, 10, 5, 1]
deposit = 1000
result = []

try:
    cost = int(input())
except Exception as e:
    print 'input value is not integer type'
else:
    if deposit - cost < 0:
        print 'cost need between 1 ~ 999'
    else:
        deposit -= cost

        for i, v in enumerate(denomination):
            quotient = deposit // v
            if quotient > 0:
                result.append('{}, {}'.format(denomination[i], quotient))
            deposit = deposit % v
        print '; '.join(result)
        # print '; '.join(['{}, {}'.format(s[0], s[1]) for s in filter(lambda x: x[1] > 0, zip(denomination, result))])
