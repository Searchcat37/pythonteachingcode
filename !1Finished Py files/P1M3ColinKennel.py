# [ ] create fucntion, call and test 
def cheese_order(max_order=100, min_order=0.5, price_per_unit=7.99, order_amount=0):
    order_amount = float(order_amount)

    if order_amount > max_order:
        print(f"{order_amount} is more than currently available")
    elif order_amount < min_order:
        print(f"{order_amount} is below minimum order amount")
    else:
        total_price = order_amount * price_per_unit
        print(f"{order_amount} costs ${total_price:.2f}")

user_name = "Colin Kennel"
order_weight = input(f"{user_name}, enter cheese order weight: ")
cheese_order(order_amount=order_weight)