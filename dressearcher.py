def sortClothes(clothes):
	for cloth,val in clothes.items():
		for weather, rating in val.items():
			print weather+str(rating)
	return

def suggestClothes(weather, clothes):
	if (weather == 'sunny'):
		return 'sunny'

	return

# clothes = ['c1', 'c2', 'c3', 'c4']
# shorts = ['s1', 's2', 's3', 's4']
# briefs = ['b1', 'b2', 'b3', 'b4']
# pants = ['p1', 'p2', 'p3', 'p4']
# soles = ['so1', 'so2', 'so3', 'so4']

# clothes = {
# 	cottonWhite: {
# 		sunny: .90,
# 		rainy: .30,
# 	}, 
# 	cottonBlack: {
# 		sunny: .90,
# 		rainy: .90,
# 	},
# 	cottonRed: {
# 		sunny: .50,
# 		rainy: .30,
# 	},
# }

clothes = {
	'cottonWhite': {
		'sunny': .99,
		'rainy': .40
	},
	'cottonBlack': {
		'sunny': .90,
		'rainy': .90,
	},
	'cottonRed': {
		'sunny': .50,
		'rainy': .30,
	},
}

print clothes;

sortClothes(clothes)
suggestClothes('sunny', clothes)
