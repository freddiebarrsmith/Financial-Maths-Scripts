#nameofcompany = "seadrill limited"
#investment = 2000000
investment = 100
#
currentvalue = 45
price = currentvalue
facevalue = 100
couponrate = 12
expectedfacevalue = 80
yearstomaturity = 3
#can make this automatically calculate

#pikbondrate = 



def yieldtomaturity(couponrate,facevalue,currentvalue,yearstomaturity):

	#https://financeformulas.net/Yield_to_Maturity.html
	actualcoupon = (facevalue / 100) * couponrate 
	#print(actualcoupon)
	
	numerator = couponrate + ((facevalue - currentvalue) / yearstomaturity)
	
	denominator = (facevalue + price) / 2

	yieldtomaturity = numerator / denominator


	return yieldtomaturity
ytm = yieldtomaturity(couponrate,facevalue,currentvalue,yearstomaturity)

print(ytm)

def yieldtomaturitypikbond():
	#https://financeformulas.net/Yield_to_Maturity.html
	
	numerator = couponrate + ((facevalue - currentvalue) / yearstomaturity)
	
	denominator = (facevalue + price) / 2

	yieldtomaturity = numerator / denominator


	return yieldtomaturity


def totalreturn():


	increaseinprincipal = (investment / currentvalue) * facevalue
	totalincrease = yieldtomaturity() 
