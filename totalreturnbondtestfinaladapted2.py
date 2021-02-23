#nameofcompany = "seadrill limited"
#investment = 2000000
investment = 2000000
#
currentvalue = 45
price = currentvalue
facevalue = 100
couponrate = 12
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


def yieldtomaturitypikbond(couponrate, pikbondrate, investment):
	#https://www.thecalculatorsite.com/articles/finance/compound-interest-formula.php
#	compoundmultiplier = 1
#	for i in range(1, yearstomaturity+1):
#		compoundmultiplier = compoundmultiplier + (compoundmultiplier * pikbondrate)
#		print(i)
#		print(compoundmultiplier)
#	return compoundmultiplier 
#https://financeformulas.net/Yield_to_Maturity.html
	pikbondinvestmentmaturityvalue  = investment * ((1 + pikbondrate) ^ yearstomaturity) 
	pikbondinvestmentmaturityvalue  = pikbondinvestmentmaturityvalue  - investment
	return pikbondinvestmentmaturityvalue 

yieldtomaturitypikbond()
def totalreturn(ytm,investment,currentvalue,facevalue):


	increaseinprincipal = (investment / currentvalue) * facevalue
	print(increaseinprincipal)
	#investment = 100



	increasefromytm = ytm * (investment / 100)
	print(increasefromytm)
	totalreturnprice = increasefromytm + increaseinprincipal
	
	

	return totalreturnprice
	#totalincrease = yieldtomaturity() 



totalreturnis = totalreturn(ytm,investment,currentvalue,facevalue)
print(totalreturnis)