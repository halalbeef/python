This is for my school project:
Basic ideas are:
-have a file to write into:
	-menu items:
		-prices
		-names
		-sorted into sections:
			-easily printed:
				-menu number
				-price
			
	-customer orders:
		-onto a text file:
			-syntax:
			menu-number | name | cost



			-printed
			-easily ammended
			-cost calculating:
			for cost in orderFile-column3 (see syntax)
				total+=cost
				#add up all the costs in the text file
			
	-text files:
		-menu:
			-starter
			-pizza
			-dessert
			-drinks
			
			#syntax for the menu
menu=[ 
#starter (name,price) 	[["garlic bread",500],["chicken dip things",600]]
#pizza (name, small9", medium11", large13", monster15")		[["pepperoni",1000,1250,1500,2000]]  
#dessert [] (name, price)
#drinks [] (name, can, 5bottle, 20lbottle)
]
