#nameofcompany = "seadrill limited"
#investment = 2000000
investment = 2000000
#
currentvalue = 45
price = currentvalue
facevalue = 100
couponrate = 4
pikbondrate = 8 
expectedcurrentvalue = 80
yearstomaturity = 4 - 1 
#can make this automatically calculate




def yieldtomaturity(couponrate,facevalue,currentvalue,yearstomaturity):

	#https://financeformulas.net/Yield_to_Maturity.html
	actualcoupon = (facevalue / 100) * couponrate 
	print(actualcoupon)
	
	numerator = actualcoupon + ((facevalue - currentvalue) / yearstomaturity)
	print(numerator)
	denominator = (facevalue + price) / 2
	print(denominator)

	yieldtomaturity = numerator / denominator

	yieldtomaturity = yieldtomaturity * 100
	return yieldtomaturity
ytm = yieldtomaturity(couponrate,facevalue,currentvalue,yearstomaturity)
print("ytm")
print(ytm)


def yieldtomaturitypikbond(couponrate, pikbondrate, investment, yearstomaturity):
	#https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
#	compoundmultiplier = 1
#	for i in range(1, yearstomaturity+1):
#		compoundmultiplier = compoundmultiplier + (compoundmultiplier * pikbondrate)
#		print(i)
#		print(compoundmultiplier)
#	return compoundmultiplier 
#https://financeformulas.net/Yield_to_Maturity.html
	pikbondinvestmentmaturityvalue  = investment * ((1 + (pikbondrate / 100)) ** yearstomaturity) 
	pikbondinvestmentmaturityvalue  = pikbondinvestmentmaturityvalue - investment
	print("pikmaturity")
	print(pikbondinvestmentmaturityvalue)
	return pikbondinvestmentmaturityvalue 


def totalreturn(ytm, investment, currentvalue, facevalue, pikbondrate, yearstomaturity):


	increaseinprincipal = (investment / currentvalue) * facevalue
	increaseinprincipal = increaseinprincipal - investment
	print("increaseinprincipal")
	print(increaseinprincipal)
	#investment = 100



	increasefromytm = (ytm / 100) * investment 
	print("increasefromytm")
	print(increasefromytm)

	pikbondinvestmentmaturityvalue = yieldtomaturitypikbond(couponrate, pikbondrate, investment, yearstomaturity)
	print("pikmaturity")
	print(pikbondinvestmentmaturityvalue)


	totalreturnprice = increasefromytm + increaseinprincipal + pikbondinvestmentmaturityvalue
	#totalreturnprice = pikbondinvestmentmaturityvalue
	

	return totalreturnprice
	#totalincrease = yieldtomaturity() 



totalreturnis = totalreturn(ytm,investment,currentvalue,facevalue,pikbondrate,yearstomaturity)
print(totalreturnis)