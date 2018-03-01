try:
    account_a = int(input())
    account_b = int(input())
    amount = int(input())
except Exception as e:
    print 'input value is not integer type'
else:	
    if account_a - amount >= 0:
        account_a -= amount
        account_b += amount
    else:
        account_b += account_a
        account_a = 0
    print '{} {}'.format(account_a, account_b)

