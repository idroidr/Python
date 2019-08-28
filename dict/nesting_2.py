hotpot = {
	'type':'鸳鸯锅',
	'toppings':['白菜', '牛肉', '土豆片'],
}

print("你点了一个[" + hotpot['type'] + "]火锅，和以下配菜：")

for topping in hotpot['toppings']:
	print(topping)
