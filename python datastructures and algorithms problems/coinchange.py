def coinchange(target , coins , known_value):
	min_coin = target
	if target in coins:
		known_value[target] = 1
		return 1
	elif known_value[target] > 0:
		return known_value[target]
	else:
		for i in [c for c in coins if c<=target]:
			num_coins = 1+ coinchange(target-i, coins , known_value )

			if num_coins < min_coin:
				min_coin = num_coins

			known_value[target] = min_coin
	return min_coin

target = 74
coins = [1,5,10, 25]
known_value = [0]*(target+1)

b = coinchange(target , coins, known_value)
print(b)