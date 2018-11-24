def get_price_no_vat(price,vat_rate):
	vat=price/100*vat_rate
	price_no_vat=price-vat
print (price_no_vat)