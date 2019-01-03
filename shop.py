####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Get Baked"
signature_flavors = ["tuna","salmon","red herring"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu:")
    for items in menu:
        print("- %s (KD %2a)" % (items,menu[items]))

def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    for j in original_flavors:
        print("-", j)

def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    for k in signature_flavors:
        print("-",k)


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    if order.lower() in menu or order.lower() in original_flavors or order.lower() in signature_flavors:
        return True
    else:
        return False

def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    print("What's your order? (Enter the exact spelling of the item you want.Type 'Exit' to end your order.)")
    while True:
        temp = input()
        if temp.lower() != "exit":
            if is_valid_order(temp.lower()) == True:
                order_list.append(temp.lower())
            else:
                print("Please enter the exact spelling as shown in the menu")
        else:
            break
        
    return order_list

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    for i in order_list:
        if i in menu:
            total += menu[i]
        elif i in original_flavors:
            total += original_price
        else:
            total += signature_price

            
    return total

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    if total >= 5:
        print("This order is eligible for credit card payment.")
    else:
        print("This order is not eligible for credit card payment.")
    
def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    total = get_total_price(order_list)
    if len(order_list) > 0:
        for i in order_list:
            print("-",i)
        print("That'll be %s KD" % total)
        accept_credit_card(total)
    else:
        print("Empty")

    print("Thank you for shopping at %s" % cupcake_shop_name)
