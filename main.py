# VIRSION 3
order_number = 1
while (True):
    print('ZAKI')

    meal1_price = 30
    meal2_price = 60
    meal3_price = 40
    meal4_price = 50
    done = "yes"
    Meals = []
    TotalMealPrice = 0
    TotalTax = 0
    GrandTotal = 0
    phoneInit= ["3", "5", "6"]
    print("“Welcome new customer!")
    print("Please press ENTER to proceed")
    userInput = input()
    while (done != "no"):
        print("_______________________________________________________________________________")
        print("\t\t\t\t", 'ZAKI')
        print("_______________________________________________________________________________")
        order_number = 1

        meal1_price = 30.00
        meal2_price = 60.00
        meal3_price = 40.00
        meal4_price = 50.00
        Meal_Price = [30.00, 60.00, 40.00, 50.00]
        print("Meal#", '\t', "Meal Price", " \t", 'Meal Description')
        print("_______________________________________________________________________________")
        print("1", '\t', meal1_price, '\t', '\t', 'MEAL 1 DESC.')
        print("2", '\t', meal2_price, '\t', '\t', 'MEAL 2 DESC.')
        print("3", '\t', meal3_price, '\t', '\t', 'MEAL 3 DESC.')
        print("4", '\t', meal4_price, '\t', '\t', 'MEAL 4 DESC.')
        print("_______________________________________________________________________________")

        meal_number = int(input('Enter meal number to order: '))
        if (meal_number<5):
           meal_quantity = int(input('Enter meal quantity to order: '))
           if(meal_quantity<100):
               subtotal_meal_price = meal_quantity * Meal_Price[meal_number-1]
               tax = subtotal_meal_price * 0.12
               total_meal_price = subtotal_meal_price + tax
               TotalMealPrice += subtotal_meal_price
               TotalTax += tax
               GrandTotal += total_meal_price
               tax = format(tax, '.2f')
               Meals.append([meal_number, meal_quantity, subtotal_meal_price, tax, total_meal_price])
               print(
                   "__________________________________________________________________________________________________________")
               print(
                   "Meal # \t \t Meal Price \t \t Meal Quantity \t \t Subtotal Meal Price \t \t Tax \t \t Total Meal Price")
               print(
                   "__________________________________________________________________________________________________________")
               for meal in Meals:
                   price = float(meal[2]) / float(meal[1])
                   price = format(price, '.1f')
                   print(
                       f"{meal[0]} \t \t \t {price} \t \t \t \t {meal[1]} \t \t \t \t \t  {meal[2]} \t \t \t \t \t {meal[3]} \t \t \t {meal[4]} ")
               print(
                   "___________________________________________________________________________________________________________")
               print(
                   f"\t \t \t \t \t \t \t \t \t \t \t \t\t {TotalMealPrice} \t \t \t \t \t\t {format(TotalTax, '.2f')} \t \t \t {GrandTotal} ")
           else:
               print("wrong data entry!")
               meal_quantity = int(input('Enter meal quantity to order: '))
               if (meal_quantity < 100):
                   subtotal_meal_price = meal_quantity * meal1_price
                   tax = subtotal_meal_price * 0.12
                   total_meal_price = subtotal_meal_price + tax
                   TotalMealPrice += subtotal_meal_price
                   TotalTax += tax
                   GrandTotal += total_meal_price
                   tax = format(tax, '.2f')
                   Meals.append([meal_number, meal_quantity, subtotal_meal_price, tax, total_meal_price])
                   print(
                       "__________________________________________________________________________________________________________")
                   print(
                       "Meal # \t \t Meal Price \t \t Meal Quantity \t \t Subtotal Meal Price \t \t Tax \t \t Total Meal Price")
                   print(
                       "__________________________________________________________________________________________________________")
                   for meal in Meals:
                       price = float(meal[2]) / float(meal[1])
                       price = format(price, '.1f')
                       print(
                           f"{meal[0]} \t \t \t {price} \t \t \t \t {meal[1]} \t \t \t \t \t  {meal[2]} \t \t \t \t \t {meal[3]} \t \t \t {meal[4]} ")
                   print(
                       "___________________________________________________________________________________________________________")
                   print(
                       f"\t \t \t \t \t \t \t \t \t \t \t \t\t {TotalMealPrice} \t \t \t \t \t\t {format(TotalTax, '.2f')} \t \t \t {GrandTotal} ")
               else:
                   print("wrong data entry program will reset!!")
                   continue
        else:
            print("wrong data entry")
            meal_number = int(input('Enter meal number to order: '))
            if (meal_number < 5):
                meal_quantity = int(input('Enter meal quantity to order: '))
                if (meal_quantity < 100):
                    subtotal_meal_price = meal_quantity * meal1_price
                    tax = subtotal_meal_price * 0.12
                    total_meal_price = subtotal_meal_price + tax
                    TotalMealPrice += subtotal_meal_price
                    TotalTax += tax
                    GrandTotal += total_meal_price
                    tax = format(tax, '.2f')
                    Meals.append([meal_number, meal_quantity, subtotal_meal_price, tax, total_meal_price])
                    print(
                        "__________________________________________________________________________________________________________")
                    print(
                        "Meal # \t \t Meal Price \t \t Meal Quantity \t \t Subtotal Meal Price \t \t Tax \t \t Total Meal Price")
                    print(
                        "__________________________________________________________________________________________________________")
                    for meal in Meals:
                        price = float(meal[2]) / float(meal[1])
                        price = format(price, '.1f')
                        print(
                            f"{meal[0]} \t \t \t {price} \t \t \t \t {meal[1]} \t \t \t \t \t  {meal[2]} \t \t \t \t \t {meal[3]} \t \t \t {meal[4]} ")
                    print(
                        "___________________________________________________________________________________________________________")
                    print(
                        f"\t \t \t \t \t \t \t \t \t \t \t \t\t {TotalMealPrice} \t \t \t \t \t\t {format(TotalTax, '.2f')} \t \t \t {GrandTotal} ")
            else:
                print("wrong data entry program will reset!!")
                continue
        print("Would you like to order more?")
        done = input()
    voucher = float(input("enter 1 if you want to use a discount voucher: "))
    if voucher == 1:
        phone_number = input('enter your phone number: ')
        if (len(phone_number) != 8 or (phone_number[0] not in phoneInit)):
            print('wrong data entry!')
            phone_number = input('enter your phone number: ')
            if (len(phone_number) != 8 or (phone_number[0] not in phoneInit)):
                print('wrong data entry!')
                continue
            else:
                voucher_number = input("enter voucher number: ")
                if (len(voucher_number) != 7 or (
                        voucher_number[0] == "0" or voucher_number[5] == "0" or voucher_number[6] == "0")):
                    print('wrong data entry! ')
                    voucher_number = input("enter voucher number: ")
                    if (len(voucher_number) != 7 or (
                            voucher_number[0] == "0" or voucher_number[5] == "0" or voucher_number[6] == "0")):
                        print('wrong data entry! ')
                        continue
                    else:
                        discount = GrandTotal * 0.15
                        print('discount:', discount)
                        price_with_discount = GrandTotal - discount
        else:
            voucher_number = input("enter voucher number: ")
            if (len(voucher_number) != 7 or (voucher_number[0]=="0" or voucher_number[5]=="0" or voucher_number[6]=="0")):
                print('wrong data entry! ')
                voucher_number = input("enter voucher number: ")
                if (len(voucher_number) != 7 or (voucher_number[0]=="0" or voucher_number[5]=="0" or voucher_number[6]=="0")):
                    print('wrong data entry! ')
                    continue
                else:
                     discount= GrandTotal*0.15
                     print('discount:' , discount)
                     price_with_discount = GrandTotal - discount
            else:
                discount = GrandTotal* 0.15
                print('discount:', discount)
                price_with_discount = GrandTotal - discount
    else:
        price_with_discount = GrandTotal
    delivry = int(input('Enter 1 for delivery or 2 for self-pickup: '))
    if delivry == 1:
        zone = int(input("Enter your zone number 1-10: "))
        if zone >= 1 and zone <= 10:
            if zone >= 1 and zone <= 4:
                delivry_cost = 10
            elif zone >= 5 and zone <= 8:
                delivry_cost = 15
            elif zone <= 10:
                delivry_cost = 25
        else:
            print('wrong data entry!')
            zone = int(input("Enter your zone number 1-10: "))
            if zone >= 1 and zone <= 10:
                if zone >= 1 and zone <= 4:
                    delivry_cost = 10
                elif zone >= 5 and zone <= 8:
                    delivry_cost = 15
                elif zone<=10:
                    delivry_cost = 25
            else:
                print("wrong data entry!!")
                continue # continue terminate the loop iteration and re launches it.
    if delivry == 2:
        delivry_cost = 0
        print("Delivery charge:", delivry_cost)
        bill_cost = price_with_discount + delivry_cost
        print("bill cost:", bill_cost)

    payment = input("Enter e-payment card number: ")
    if (len(payment) == 16 and payment[9] == '0' and payment[10] == '0' and payment[11] == '0'):
        bill_cost = price_with_discount
        print("bill cost:", bill_cost)
        print("your order number is", order_number, "Enjoy your meal!")
        order_number += 1 # if the order is placed correctly the program resets and increases the order count, so each customer will have an order number
    else:
        print('wrong data entry!')
        payment = input("Enter e-payment card number: ")
        if (len(payment) == 16 and payment[9] == '0' and payment[10] == '0' and payment[11] == '0'):
            print("your order number is", order_number, "Enjoy your meal!")
            order_number += 1
        else:
            print('wrong data entry!')
            continue

