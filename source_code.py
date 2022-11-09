# function for user to enter products (w/ quantity) or quit
# stores data in a dictionary and updates it
def enterProducts():
    buyingData = {}
    enterDetails = True
    while enterDetails:
        details = input('Press A to add product and Q to quit: ')
        if details == 'A':
            product = input('Enter product: ')
            quantity = int(input('Enter quantity: '))
            buyingData.update({product: quantity})
        elif details == 'Q':
            enterDetails = False
        else:
            print('Please select a correct option')
    return buyingData


# function to get price and of products and to calc subtotal
def getPrice(product, quantity):
    priceData = {
        'Orange': 2,
        'Broccoli': 2,
        'Egg': 1,
        'Fish': 3,
        'Rice': 2,
        'Bread': 2,
        'Apple': 3,
        'Onion': 3,
        'Grape': 3,
        'Lemon': 2,
        'Beef': 5,
        'Chicken': 5,
        'Pork': 5
    }
    subtotal = priceData[product] * quantity
    print(product + ':$' + str(priceData[product]) + 'x' + str(quantity) + '=' + str(subtotal))
    return subtotal


# function to calc discount based off of membership if total meets discount requirements
def getDiscount(billAmount, membership):
    discount = 0
    if billAmount >= 15:
        if membership == 'Premium':
            billAmount = billAmount * .75
            discount = 25
        elif membership == 'Member':
            billAmount = billAmount * .85
            discount = 15
        elif membership == 'Trial':
            billAmount = billAmount * .95
            discount = 5
        print(str(discount) + '% off for '
              + membership + '' + ' membership on total amount: $' + str(billAmount))
    else:
        print('No discount on amount less than $15')
    return billAmount


# function to calc final bill using a for loop
def makeBill(buyingData, membership):
    billAmount = 0
    for key, value in buyingData.items():
        billAmount += getPrice(key, value)
    billAmount = getDiscount(billAmount, membership)
    print('The discounted amount is $' + str(billAmount))


# how to call and execute the program
buyingData = enterProducts()
membership = input('Enter customer membership: ')
makeBill(buyingData, membership)


# NEED TO MAKE A MAIN FUNCTION TO RUN THE GLOBAL OBJECTS!
def main():
    buyingData = enterProducts()
    membership = input('Enter customer membership: ')
    makeBill(buyingData, membership)
main()
