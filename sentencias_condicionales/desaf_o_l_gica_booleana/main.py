seasonal = True
on_sale = False
selling_well = False
current_stock = 150
high_stock_threshold = 100
overstock_risk = (seasonal == True) and (current_stock > high_stock_threshold)
ready_for_sale = (on_sale != False) and (selling_well != False)
discount_eligible = not ready_for_sale
make_discount = (overstock_risk == True) or (discount_eligible == True)
print("Should the item be discounted?", make_discount)