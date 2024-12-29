#Name : Mervin Ooi Zhian Yang, TP Number : TP076578
import datetime
import time

def customer_register(name,ic,phone,city,date,username,password):
    with open("customer_register_info.txt", "a") as cus_info:
        cus_info.write(f"\n{name},{ic},{phone},{city},{date},{username},{password}")
    time.sleep(1)

def customer_login(cus_username,cus_password):
    cus_login = (f"{cus_username},{cus_password}")
    with open("customer_login_file.txt", "r") as f:
        for line in f:
            line = line.strip()
            if cus_login == line:
                action = "login"
                with open("customer_system_usage.txt", "a") as csu:
                    csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print("You had login successfully!\n")
                time.sleep(0.4)
                return True

def purchase_order(cus_username):
    action = "enter purchase order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    cart = []
    order_list = []
    with open("stock.txt", "r") as menu:
        print(f"""---------------------------------------------Item List---------------------------------------------
ID    Item                                                       Price        Quantity""")
        lines = menu.readlines()
        for line in lines:
            item = line.strip()
            id = item.split(",")[0]
            item_name = item.split(",")[1]
            price = item.split(",")[2]
            item_quantity = item.split(",")[-1]
            print(f"{id:>4}. {item_name:50}     {price:>9}     {item_quantity:>8}")

        print("""--------------------------------------------------------------------------------------------------
Enter C to check the cart
Enter Q to quit
Enter itemID to add item into the cart""")

    while True:
        item_select = input("""\nPlease enter itemID, C or Q: """)

        with open("stock.txt", "r") as menu:
            for line in menu:
                item = line.strip()
                id = item.split(",")[0]
                item_name = item.split(",")[1]
                price = item.split(",")[2]
                id_list = []
                id_list.append(id)

                if item_select in id_list:
                    customer_input = "True"
                    break

                elif item_select not in id_list and item_select.upper() == "C":
                    customer_input = "Cart"
                    break

                elif item_select not in id_list and item_select.upper() == "Q":
                    customer_input = "Quit"
                    break

                elif item_select not in id_list and item_select.upper() != "C" and item_select.upper() != "Q":
                    customer_input = "False"
                    continue

            if customer_input == "False":
                print("Wrong input. Please try again.")

            elif customer_input == "True":
                try:
                    quantity_selected = int(input("Please enter the quantity: "))
                    cart.append([id, item_name, price, quantity_selected])
                    print(f"{quantity_selected} pcs of {id} added to cart.")
                except ValueError:
                    print("Wrong input. Please try again.")

            elif customer_input == "Cart":
                if len(cart) == 0:
                    print("There are no items in the cart.")
                    continue

                else:
                    total_price = 0
                    print("-----------------------------------------------Cart-----------------------------------------------")
                    for item in cart:
                        print(f"ItemID: {item[0]}, Name: {item[1]}, Price: {item[2]}, Quantity: {item[3]}")
                        price = float(item[2])
                        quantity_selected = int(item[3])
                        total_price += price * quantity_selected

                    print(f"Total Price: RM{total_price:2n}")
                    place_or_add = str(input("""Enter 1 to place the order
Enter 2 to add more item\n
Please enter your option: """))

                if place_or_add == str(1):
                    total_price = 0
                    for item in cart:
                        price = float(item[2])
                        quantity_selected = int(item[3])
                        total_price += price * quantity_selected

                    with open("purchase_order_list.txt", "r") as o:
                        lines = o.readlines()
                        for line in lines:
                            line = line.strip()
                            order_id = line.split(",")[0]
                            if order_id not in order_list:
                                order_list.append(order_id)

                        orderID = str(f"PO{len(order_list) + 1}")

                    with open("purchase_order_list.txt", "a") as o:
                        o.write(f"\n{orderID},{cus_username},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{cart},{total_price},unpaid")

                    action = "place a purchase order"

                    with open("customer_system_usage.txt", "a") as csu:
                        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                    print(f"Your order (orderID: {orderID}) has been placed. Please proceed for payment.\n")
                    time.sleep(1.5)
                    break

            elif customer_input == "Quit":
                if len(cart) == 0:
                    break

                elif len(cart) != 0:
                    place_or_discard = str(input("""This order has not been placed\n
Enter 1 to place the order
Enter 2 to discard the order: """))

                    if place_or_discard != str(1):
                        print(f"The order has been discard.")
                        break

                    elif place_or_discard == str(1):
                        total_price = 0
                        for item in cart:
                            price = float(item[2])
                            quantity_selected = int(item[3])
                            total_price += price * quantity_selected

                        with open("purchase_order_list.txt", "r") as o:
                            lines = o.readlines()
                            for line in lines:
                                line = line.strip()
                                order_id = line.split(",")[0]
                                if order_id not in order_list:
                                    order_list.append(order_id)

                        with open("purchase_order_list.txt", "r") as o:
                            orderID = str(f"PO{len(order_list) + 1}")

                        with open("purchase_order_list.txt", "a") as o:
                            o.write(f"\n{orderID},{cus_username},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')},{cart},{total_price},unpaid")

                        action = "place a purchase order"
                        with open("customer_system_usage.txt", "a") as csu:
                            csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

                        print(f"\nYour order (orderID: {orderID}) has been placed. Please proceed for payment.")
                        time.sleep(1.5)
                    break

    action = "quit from purchase order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def repair_order(cus_username):
    action = "enter service order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    order_list = []

    order_status = "unpaid"
    print("""\n----------------------------------------------Repair Order----------------------------------------------
1. Desktop Computer
2. Laptop Computer
3. Printer
4. Monitor
5. Keyboard
6. Mouse
""")
    while True:
        device = input("Enter Device Name or Enter Q to quit: ")

        if device.upper() == "Q":
            break

        elif device.title() not in ["Desktop Computer", "Laptop Computer", "Printer", "Monitor", "Keyboard", "Mouse"] and device not in ["1", "2", "3", "4", "5", "6"]:
            print("Invalid input. Please enter the name of device from the option above.\n")

        else:
            if device.title() == "Desktop Computer" or device == "1":
                device = "Desktop Computer"
                price = int(25)

            elif device.title() == "Laptop Computer" or device == "2":
                device = "Laptop Computer"
                price = int(20)

            elif device.title() == "Printer" or device == "3":
                device = "Printer"
                price = int(10)

            elif device.title() == "Monitor" or device == "4":
                device = "Monitor"
                price = int(15)

            elif device.title() == "Keyboard" or device == "5":
                device = "Keyboard"
                price = int(5)

            elif device.title() == "Mouse" or device == "6":
                device = "Mouse"
                price = int(5)

            with open("repair_order_list.txt", "r") as r:
                lines = r.readlines()
                for line in lines:
                    line = line.strip()
                    orderID = line.split(",")[0]
                    if orderID not in order_list:
                        order_list.append(orderID)
                orderID = (f"RO{len(order_list) + 1}")

            with open("repair_order_list.txt", "a") as r:
                r.write(f"\n{orderID},{cus_username},{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")},{device},{price},{order_status}")

            print(f"Your service order (orderID: {orderID}) has been placed. Please proceed to payment.\n")
            time.sleep(1.5)

            action = "place a repair order"
            with open("customer_system_usage.txt", "a") as csu:
                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            break

    action = "quit from repair order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def modify_order(cus_username):
    action = "enter modify order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        print("\n-----------------------------------------Modify Order Page------------------------------------------")

        order_type = input("""Enter 1 to modify purchase order
Enter 2 to modify repair order
Enter 3 to quit from purchase order page: """)

        if order_type == "3":
            break
        
        elif order_type != "1" and order_type != "2" and order_type != "3":
            print("Invalid option. Please enter 1, 2, or 3.")

        elif order_type == '1':
            cart = []
            order = []
            unpaid_order = []
            updated_lines = []
            old_lines = []
            with open("purchase_order_list.txt", "r") as p:
                lines = p.readlines()
                for line in lines:
                    line = line.strip()
                    p_order_id = line.split(",")[0]
                    p_customer_username = line.split(",")[1]
                    if cus_username == p_customer_username:
                        order.append(p_order_id)

            for i in order:
                if order.count(i) == 1:
                    unpaid_order.append(i)

            # try:
            while True:
                print("\n---------------------------------------------Order List---------------------------------------------")

                for i in unpaid_order:
                    print(i)
                modify_order = input("Please select order to modify by enter the orderID (Enter Q to quit): ")

                if modify_order.upper() == "Q":
                    break

                elif modify_order not in unpaid_order:
                    print("This order does not exist.")

                elif modify_order in unpaid_order:
                    with open("purchase_order_list.txt", "r") as p:
                        order_list = []
                        lines = p.readlines()
                        for line in lines:
                            line = line.strip()
                            p_order_id = line.split(",")[0]
                            order_list.append(p_order_id)
                            p_customer_username = line.split(",")[1]

                            if p_order_id == modify_order:
                                p_datetime = line.split(",")[2]
                                p_total_price = str(line.split(",")[-2])
                                order = line.split(",")
                                items = ",".join(order[3:-2])
                                print(f"""
-------------------------------------------Order Details--------------------------------------------
Customer Username: {p_customer_username}
OrderID: {p_order_id}
Order Time: {p_datetime}
Items:""")

                                for item in eval(items):
                                    itemID, item_name, item_price, quantity = item
                                    cart.append(item)
                                    print(f"{item_name} (ItemID: {itemID}), Price: RM{item_price}, Quantity: {quantity}")


                    print("""----------------------------------------------------------------------------------------------------
Enter 1 to Add Item
Enter 2 to Remove Item
Enter 3 to Quit
""")

                    while True:
                        modify_type = input("Please enter your option: ")

                        if modify_type != "1" and modify_type != "2" and modify_type != "3":
                            print("Invalid input. Please try again.\n")
                            time.sleep(0.7)

                        elif modify_type == "3":
                            break

                        elif modify_type == "1" or modify_type == "2":
                            break

                    if modify_type == '1':
                        with open("stock.txt", "r") as menu:
                            print(f"""
---------------------------------------------Item List---------------------------------------------
ID    Item                                                       Price        Quantity""")
                            for line in menu:
                                item = line.strip()
                                id = item.split(",")[0]
                                name = item.split(",")[1]
                                price = item.split(",")[2]
                                quantity = item.split(",")[3]
                                order_list.append(id)
                                print(f"{id:>4}. {name:50}     {price:>9}     {quantity:>8}")

                        while True:
                            add_item = input("Please select item to add by enter the itemID (Enter Q to quit): ")

                            if add_item.upper() == "Q":
                                break

                            elif add_item not in order_list:
                                print("Invalid input. Please enter a itemID.\n")
                                time.sleep(0.7)

                            else:
                                
                                with open("stock.txt", "r") as menu:
                                    for line in menu:
                                        item = line.strip()
                                        id = item.split(",")[0]
                                        id_list = []
                                        id_list.append(id)

                                        if add_item in id_list:
                                            name = item.split(",")[1]
                                            price = item.split(",")[2]
                                            quantity = item.split(",")[3]

                                            try:
                                                add_quantity = int(input("Please enter the quantity: "))
                                            except ValueError:
                                                print("\nPlease enter an integer.")
                                                time.sleep(0.7)
                                            else:
                                                cart.append([add_item, name, price, add_quantity])

                                                with open("purchase_order_list.txt", "r") as p:
                                                    lines = p.readlines()
                                                    for line in lines:
                                                        old_line = line.strip()
                                                        p_order_id = old_line.split(",")[0]
                                                        old_p_total_price = float(old_line.split(",")[-2])

                                                        order = line.split(",")
                                                        old_cart = ",".join(order[3:-2])

                                                        if modify_order != p_order_id:
                                                            old_lines.append(line)

                                                        elif modify_order == p_order_id:
                                                            price = float(price)
                                                            new_p_order_id = p_order_id
                                                            new_time = old_line.split(",")[2]
                                                            new_p_total_price = old_p_total_price + (price * add_quantity)
                                                            updated_line = line.replace(str(old_cart), str(cart))
                                                            updated_line = updated_line.replace(str(old_p_total_price),str(new_p_total_price))
                                                            updated_lines.append(updated_line)
                                                            updated_lines[-1] = updated_lines[-1].strip()

                                                with open("purchase_order_list.txt", "w") as p:
                                                    p.writelines(old_lines)

                                                with open("purchase_order_list.txt", "a") as p:
                                                    p.write(f"\n{new_p_order_id},{cus_username},{new_time},{cart},{new_p_total_price},unpaid")
                                                    print("\nThis item has been added successfully.")
                                                    time.sleep(1)

                                                action = "modify purchase order"
                                                with open("customer_system_usage.txt", "a") as csu:
                                                    csu.write(
                                                        f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                                break
                        break

                    elif modify_type == '2':
                        item_list = []

                        with open("purchase_order_list.txt", "r") as p:
                            lines = p.readlines()
                            for line in lines:
                                line = line.strip()
                                p_order_id = line.split(",")[0]
                                p_total_price = str(line.split(",")[-2])
                                order = line.split(",")
                                items = ",".join(order[3:-2])

                                if modify_order == p_order_id:
                                    for item in eval(items):
                                        item_list.append(item)
                                    break

                        while True:
                            remove_item = input("Please select item to remove by enter the itemID (Enter Q to quit): ")
                            item_exist = False

                            if remove_item.upper() == "Q":
                                break

                            elif remove_item not in item_list:
                                print("Invalid input. Please enter a itemID.\n")
                                time.sleep(0.7)

                            else:

                                for item in item_list:
                                    itemID, item_name, item_price, quantity = item

                                    if remove_item == itemID:
                                        item_exist = True
                                        break

                                if item_exist == False:
                                    print("\nThis item is not in the order.")
                                    time.sleep(0.7)

                                elif item_exist == True:
                                    item_list.remove(item)

                                    if item_list == []:
                                        print("\nThis is the only item in the order. This item cannot be removed.")
                                        time.sleep(0.7)
                                        break

                                    else:
                                        print(item_list)
                                        print(p_total_price)

                                        with open("purchase_order_list.txt", "r") as p:
                                            lines = p.readlines()
                                            for line in lines:
                                                old_line = line.strip()
                                                p_order_id = old_line.split(",")[0]
                                                old_p_total_price = float(old_line.split(",")[-2])
                                                order = line.split(",")
                                                old_cart = ",".join(order[3:-2])

                                                if modify_order != p_order_id:
                                                    old_lines.append(line)

                                                elif modify_order == p_order_id:
                                                    item_price = float(item_price)
                                                    new_p_total_price = old_p_total_price - (item_price * quantity)
                                                    updated_line = line.replace(str(old_cart), str(item_list))
                                                    updated_line = updated_line.replace(str(old_p_total_price),str(new_p_total_price))
                                                    updated_lines.append(updated_line)

                                        with open("purchase_order_list.txt", "w") as p:
                                            old_lines[-1] = old_lines[-1].strip()
                                            p.writelines(old_lines)

                                        with open("purchase_order_list.txt", "a") as p:
                                            updated_lines[-1] = updated_lines[-1].strip()
                                            p.write("\n")
                                            p.writelines(updated_lines)
                                            print("\nThis item has been removed successfully.")
                                            time.sleep(1)

                                        action = "modify purchase order"
                                        with open("customer_system_usage.txt", "a") as csu:
                                            csu.write(
                                                f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                                            break

                else:
                    print("\nInvalid input. Please try again.")

        elif order_type == '2':
            order = []
            unpaid_order = []
            old_lines = []
            with open("repair_order_list.txt", "r") as r:
                lines = r.readlines()
                for line in lines:
                    line = line.strip()
                    r_order_id = line.split(",")[0]
                    r_customer_name = line.split(",")[1]
                    if cus_username in line:
                        order.append(r_order_id)

                for i in order:
                    if order.count(i) == 1:
                        unpaid_order.append(i)

            while True:
                print("\n--------------------------------------------Order List----------------------------------------------")
                for i in unpaid_order:
                    print(i)
                modify_order = input("Please select order to modify by enter the orderID (Enter Q to quit): ")

                if modify_order.upper() == "Q":
                    break

                elif modify_order not in unpaid_order:
                    print("Invalid input. Please try again.\n")
                    time.sleep(0.7)

                else:
                    with open("repair_order_list.txt", "r") as r:
                        lines = r.readlines()
                        for line in lines:
                            line = line.strip()
                            r_order_id = line.split(",")[0]
                            if modify_order == r_order_id:
                                line = line.strip()
                                r_datetime = line.split(",")[2]
                                r_item = line.split(",")[3]
                                r_price = float(line.split(",")[-2])

                                print(f"""
---------------------------------------------Order Details---------------------------------------------
Customer Username: {r_customer_name}
OrderID: {r_order_id}
Order Time: {r_datetime}
Items: {r_item}
Price: RM{r_price:.2f}""")

                    print("""
--------------------------------------------Repair List---------------------------------------------
1. Desktop Computer
2. Laptop Computer
3. Printer
4. Monitor
5. Keyboard
6. Mouse
7. Speaker""")

                    while True:
                        change_item = (input("Please enter the item name to change the repair item (Enter Q to quit): "))

                        if change_item.upper() == "Q":
                            break

                        elif change_item != "1" and change_item != "2" and change_item != "3" and change_item != "4" and change_item != "5" and change_item != "6" and change_item != "7":
                            print("Invalid input. Please try again.\n")

                        else:
                            if change_item.title() == "Desktop Computer" or change_item == "1":
                                r_price = str(20)
                                new_item = "Desktop Computer"

                            elif change_item.title() == "Laptop Computer" or change_item == "2":
                                r_price = str(20)
                                new_item = "Laptop Computer"

                            elif change_item.title() == "Printer" or change_item == "3":
                                r_price = str(10)
                                new_item = "Printer"

                            elif change_item.title() == "Monitor" or change_item == "4":
                                r_price = str(15)
                                new_item = "Monitor"

                            elif change_item.title() == "Keyboard" or change_item == "5":
                                r_price = str(5)
                                new_item = "Keyboard"

                            elif change_item.title() == "Mouse" or change_item == "6":
                                r_price = str(5)
                                new_item = "Mouse"

                            elif change_item.title() == "Speaker" or change_item == "7":
                                r_price = str(5)
                                new_item = "Speaker"

                            else:
                                print("Invalid input. Please try again.\n")

                            for line in lines:
                                old_line = line.strip()
                                r_order_id = old_line.split(",")[0]
                                if modify_order != r_order_id:
                                    old_lines.append(line)

                                elif modify_order == r_order_id:
                                    r_customer_name = old_line.split(",")[1]
                                    r_datetime = line.split(",")[2]
                                    r_order_status = line.split(",")[-1]
                                    updated_line = (f"{r_order_id},{r_customer_name},{r_datetime},{new_item},{r_price},{r_order_status}")

                            with open("repair_order_list.txt", "w") as r:
                                r.writelines(old_lines)

                            with open("repair_order_list.txt", "a") as r:
                                r.write(f"{updated_line}")
                                print("Order has been updated successfully.\n")
                                time.sleep(1)

                            action = "modify repair order"
                            with open("customer_system_usage.txt", "a") as csu:
                                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    action = "quit from modify order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def order_payment(cus_username):
    action = "enter order payment page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    stock_lines = []
    temp_stock_lines = []
    stock_id_list = []
    order_list = []
    updated_lines = []
    itemID_list = []
    flag = "empty"
    quantity_status = False

    with open("purchase_order_list.txt", "r") as p:
        lines = p.readlines()
        for line in lines:
            line = line.strip()
            p_id = line.split(",")[0]
            p_customer = line.split(",")[1]
            p_order_status = line.split(",")[-1]
            if p_customer == cus_username and (p_order_status == "unpaid" or p_order_status == "paid" or p_order_status == "cancelled"):
                if p_id in order_list:
                    order_list.remove(p_id)
                else:
                    order_list.append(p_id)

    with open("repair_order_list.txt", "r") as r:
        lines = r.readlines()
        for line in lines:
            line = line.strip()
            r_id = line.split(",")[0]
            r_customer = line.split(",")[1]
            r_order_status = line.split(",")[-1]
            if r_customer == cus_username and (r_order_status == "unpaid" or r_order_status == "paid" or p_order_status == "cancelled"):
                if r_id in order_list:
                    order_list.remove(r_id)
                else:
                    order_list.append(r_id)


    if order_list == []:
        print("You don't have any orders waiting for payment.")
        return 0

    else:
        while True:
            print("\n-------------------------------------------Order List-------------------------------------------")
            for id in order_list:
                print(id)

            print("------------------------------------------------------------------------------------------------")
            select_order = str(input("Please enter orderID to make payment (Enter Q to quit): "))

            if select_order.upper() == "Q":
                break

            elif "RO" in select_order:
                with open("repair_order_list.txt", "r") as r:
                    lines = r.readlines()
                    for line in lines:
                        line = line.strip()
                        line = line.split(",")
                        r_id = line[0]
                        r_customer = line[1]
                        r_order_status = line[-1]
                        if r_id == select_order and r_customer == cus_username and select_order in order_list:
                            flag = "unpaid"
                            break

                        elif r_id == select_order and r_customer == cus_username and r_order_status in ["paid"]:
                            flag = "paid"
                            break

                        else:
                            flag = "not found"

            elif "PO" in select_order:
                with open("purchase_order_list.txt", "r") as p:
                    lines = p.readlines()
                    for line in lines:
                        line = line.strip()
                        p_id = line.split(",")[0]
                        p_customer = line.split(",")[1]
                        p_order_status = line.split(",")[-1]

                        if p_id == select_order and p_customer == cus_username and select_order in order_list:
                            flag = "unpaid"
                            break

                        elif p_id == select_order and p_customer == cus_username and p_order_status in ["paid"]:
                            flag = "paid"
                            break

                        else:
                            flag = "not found"

            else:
                flag = "not found"

            if flag == "paid":
                print("This order is paid\n")
                time.sleep(1)

            elif flag == "unpaid":

                if "PO" in select_order:
                    with open("purchase_order_list.txt", "r") as p:
                        lines = p.readlines()
                        for line in lines:
                            line = line.strip()
                            p_id = line.split(",")[0]

                            if select_order == p_id:
                                line = line.strip()
                                p_datetime = line.split(",")[2]
                                p_total_price = str(line.split(",")[-2])
                                order = line.split(",")
                                items = ",".join(order[3:-2])
                                for item in eval(items):
                                    itemID, item_name, item_price, quantity = item
                                    itemID_list.append(itemID)

                                with open("stock.txt", "r") as i:
                                    lines = i.readlines()
                                    for line in lines:
                                        stock = line.strip()
                                        stock_lines.append(stock)
                                        stock_itemID = stock.split(",")[0]
                                        if stock_itemID in itemID_list:
                                            stock_quantity = stock.split(",")[-1]

                                            if int(stock_quantity) < int(quantity):
                                                print(f"The quantity of {stock_itemID} is less than {quantity}. Please try again later.")
                                                quantity_status = False
                                                time.sleep(1.5)
                                                break

                                            else:
                                                quantity_status = True


                                if quantity_status:

                                    print(f"""\n------------------------------------------Payment Page------------------------------------------
Customer Username: {p_customer}
OrderID: {p_id}
Order Time: {p_datetime}
Items:""")
                                    print("------------------------------------------------------------------------------------------------")
                                    for item in eval(items):
                                        itemID, item_name, item_price, quantity = item

                                    p_total_price = float(p_total_price)
                                    print(f"Total Price: RM{p_total_price:.2f}")
                                    print("------------------------------------------------------------------------------------------------")

                                    while True:
                                        try:
                                            paid_amount = float(input("Please enter paid amount (Enter 0 to quit): RM"))

                                        except ValueError:
                                            print("Invalid input. Please enter a valid number.\n")
                                            time.sleep(0.5)

                                        else:
                                            if paid_amount == 0:
                                                break

                                            elif p_total_price > paid_amount:
                                                print("Paid amount is less than total price. Please enter again.\n")
                                                time.sleep(0.5)

                                            else:
                                                changes = paid_amount - p_total_price
                                                print(f"Changes: RM{changes:.2f}")
                                                today_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

                                                with open("stock.txt", "r") as s:
                                                    lines = s.readlines()
                                                    for stock_line in lines:
                                                        stock_line = stock_line.strip()
                                                        stock_id = stock_line.split(",")[0]
                                                        stock_quantity = stock_line.split(",")[-1]
                                                        stock_quantity = int(stock_quantity)

                                                        if stock_id not in itemID_list and stock_id not in stock_id_list:
                                                            temp_stock_lines.append(stock_line)
                                                            stock_id_list.append(stock_id)
                                                        elif stock_id in itemID_list and stock_id not in stock_id_list:
                                                            updated_stock_quantity = stock_quantity - quantity
                                                            updated_stock_line = stock_line.replace(str(stock_quantity),str(updated_stock_quantity))
                                                            temp_stock_lines.append(updated_stock_line)
                                                            stock_id_list.append(stock_id)
                                                        else:
                                                            continue


                                                with open("purchase_order_list.txt", "r") as p:
                                                    lines = p.readlines()
                                                    for line in lines:
                                                        line = line.strip()
                                                        order_id = line.split(",")[0]
                                                        if order_id == select_order:
                                                            updated_line = line.replace("unpaid", "paid")
                                                            updated_line = updated_line.replace(p_datetime, today_datetime)
                                                            updated_lines.append(updated_line)
                                                            updated_line = line.replace("unpaid", "ready to collect")
                                                            updated_line = updated_line.replace(p_datetime,today_datetime)
                                                            updated_lines.append(updated_line)

                                                with open("purchase_order_list.txt", "a") as p:
                                                    for updated_line in updated_lines:
                                                        p.write(f"\n{updated_line}")

                                                with open("stock.txt", "w") as s:
                                                    s.write("")

                                                with open("stock.txt", "a") as s:
                                                    for line in temp_stock_lines:
                                                        s.write(f"{line}\n")

                                                print("Payment complete. Your order is now ready to collect.\n")
                                                action = "make payment for purchase order"
                                                with open("customer_system_usage.txt", "a") as csu:
                                                    csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                                                return False
                                else:
                                    break

                elif "RO" in select_order:
                    with open("repair_order_list.txt", "r") as r:
                        lines = r.readlines()
                        for line in lines:
                            line = line.strip()
                            r_id = line.split(",")[0]
                            r_customer = line.split(",")[1]
                            r_datetime = line.split(",")[2]
                            r_item = line.split(",")[3]
                            r_price = float(line.split(",")[-2])
                            if select_order != r_id:
                                continue
                            elif select_order == r_id:
                                print(f"""------------------------------------------Payment Page------------------------------------------
Customer Username: {r_customer}
OrderID: {r_id}
Order Time: {r_datetime}
Item: {r_item}
Total Price: RM{r_price:.2f}""")
                            print("------------------------------------------------------------------------------------------------")

                            try:
                                paid_amount = float(input("Please enter paid amount (Enter 0 to quit): RM"))
                            except ValueError:
                                print("Invalid input. Please enter a valid number.\n")
                                time.sleep(0.5)
                            else:
                                if paid_amount == 0:
                                    break

                                elif paid_amount < 0:
                                    print("Invalid input. Please enter a valid number.\n")
                                    time.sleep(0.5)
                                while r_price > paid_amount:
                                    print("Paid amount is less than total price. Please enter again.\n")
                                    time.sleep(0.5)
                                else:
                                    changes = paid_amount - r_price
                                    print(f"Changes: RM{changes:.2f}")
                                    today_datetime = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                    updated_line = line.replace("unpaid", "paid")
                                    updated_line = updated_line.replace(r_datetime, today_datetime)
                                    updated_lines.append(updated_line)
                                    with open("repair_order_list.txt", "a") as r:
                                        r.write(f"\n{updated_line}")
                                        print("Payment complete. Your order is now ready to collect.\n")
                                        time.sleep(1)
                                        updated_line = line.replace("unpaid", "ready to collect")
                                        updated_line = updated_line.replace(r_datetime, today_datetime)
                                        r.write(f"\n{updated_line}")

                                    action = "make payment for repair order"
                                    with open("customer_system_usage.txt", "a") as csu:
                                        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                                        return False

            elif flag == "not found":
                print("Order not found. Please try again.\n")
                time.sleep(1)

    action = "quit from order payment page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def order_status(cus_username):
    action = "enter check order status page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    order_list = []

    with open("purchase_order_list.txt", "r") as p:
        lines = p.readlines()
        for line in lines:
            line = line.strip()
            p_order_id = line.split(",")[0]
            p_customer = line.split(",")[1]
            if cus_username == p_customer and p_order_id not in order_list:
                order_list.append(p_order_id)

    with open("repair_order_list.txt", "r") as r:
        lines = r.readlines()
        for line in lines:
            line = line.strip()
            r_order_id = line.split(",")[0]
            r_customer = line.split(",")[1]
            if cus_username == r_customer and r_order_id not in order_list:
                order_list.append(r_order_id)

    for order_id in order_list:
        print(order_id)

    while True:
        check_order = input("Please enter the orderID from above to check order status (Enter Q to quit): ")

        if check_order.upper() == "Q":
            break

        elif "PO" in check_order:

            with open("purchase_order_list.txt", "r") as p:
                lines = p.readlines()
                for line in lines:
                    line = line.strip()
                    p_id = line.split(",")[0]
                    p_customer = line.split(",")[1]

                    if check_order == p_id and cus_username == p_customer:
                        line = line.strip()
                        order = line.split(",")
                        order_present = True
                        break

                    else:
                        order_present = False

            if order_present == False:
                print("This order does not exist")

            elif order_present == True:
                print(f"""
Customer Name: {p_customer}
OrderID: {p_id}""")

                with open("purchase_order_list.txt", "r") as p:
                    lines = p.readlines()
                    for line in lines:
                        line = line.strip()
                        p_order_id = line.split(",")[0]
                        p_datetime = line.split(",")[2]
                        p_order_status = line.split(",")[-1]

                        if p_order_id == check_order:
                            print(f"{p_datetime}    Order Status: {p_order_status}")
                            action = "check purchase order status"
                            with open("customer_system_usage.txt", "a") as csu:
                                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    break

            while True:
                quit = input("Enter Q to quit: ")
                if quit.upper() == "Q":
                    action = "quit from check order status page"
                    with open("customer_system_usage.txt", "a") as csu:
                        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    break

        elif "RO" in check_order:
            with open("repair_order_list.txt", "r") as r:
                lines = r.readlines()
                for line in lines:
                    line = line.strip()
                    r_id = line.split(",")[0]
                    r_customer = line.split(",")[1]

                    if check_order == r_id and cus_username == r_customer:
                        line = line.strip()
                        r_customer = line.split(",")[1]
                        order = line.split(",")
                        order_present = True
                        break

                    else:
                        order_present = False

            if order_present == False:
                print("This order does not exist")

            elif order_present == True:
                print(f"""
Customer Name: {r_customer}
OrderID: {r_id}""")

                with open("repair_order_list.txt", "r") as r:
                    lines = r.readlines()

                    for line in lines:
                        line = line.strip()
                        r_order_id = line.split(",")[0]
                        r_datetime = line.split(",")[2]
                        r_order_status = line.split(",")[-1]
                        if r_order_id == check_order:
                            print(f"{r_datetime}    Order Status: {r_order_status}")
                            action = "check repair order status"
                            with open("customer_system_usage.txt", "a") as csu:
                                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                    break

    while True:
        quit = input("Enter Q to quit: ")
        if quit.upper() == "Q":
            action = "quit from check order status page"
            with open("customer_system_usage.txt", "a") as csu:
                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            break

def collect_order(cus_username):
    action = "enter collect order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    order_list = []

    with open("purchase_order_list.txt", "r") as p:
        lines = p.readlines()
        for line in lines:
            line = line.strip()
            p_order_id = line.split(",")[0]
            p_customer = line.split(",")[1]
            p_order_status = line.split(",")[-1]
            if cus_username == p_customer and p_order_id not in order_list and p_order_status == "ready to collect":
                order_list.append(p_order_id)

    with open("repair_order_list.txt", "r") as r:
        lines = r.readlines()
        for line in lines:
            line = line.strip()
            r_order_id = line.split(",")[0]
            r_customer = line.split(",")[1]
            if cus_username == r_customer and r_order_id not in order_list and p_order_status == "ready to collect":
                order_list.append(r_order_id)

    while True:
        print("---------------------------------------Collect Order Page---------------------------------------")

        for order_id in order_list:
            print(order_id)
        collect_order = input("Please enter the orderID from above to collect order (Enter Q to quit): ")

        if collect_order.upper() == "Q":
            break

        elif "PO" in collect_order and collect_order in order_list:
            with open("purchase_order_list.txt", "r") as p:
                lines = p.readlines()
                for line in lines:
                    line = line.strip()
                    p_order_id = line.split(",")[0]
                    if collect_order == p_order_id:
                        p_datetime = line.split(",")[2]
                        p_order_status = line.split(",")[-1]
                        updated_line = line.replace(p_datetime, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        updated_line = updated_line.replace(p_order_status, "completed")

            with open("purchase_order_list.txt", "a") as p:
                p.write(f"\n{updated_line}")
                print("Your order has been collected")
                time.sleep(1)
                action = "collect purchase order"
                with open("customer_system_usage.txt", "a") as csu:
                    csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                break

        elif "RO" in collect_order and collect_order in order_list:
            with open("repair_order_list.txt", "r") as r:
                lines = r.readlines()
                for line in lines:
                    line = line.strip()
                    r_order_id = line.split(",")[0]
                    if collect_order == r_order_id:
                        r_datetime = line.split(",")[2]
                        r_order_status = line.split(",")[-1]
                        updated_line = line.replace(r_datetime, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                        updated_line = updated_line.replace(r_order_status, "completed")

            with open("repair_order_list.txt", "a") as r:
                r.write(f"\n{updated_line}")
                print("Your order has been collected")
                time.sleep(1)
                action = "collect repair order"
                with open("customer_system_usage.txt", "a") as csu:
                    csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                break

    action = "quit from collect order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def cancel_order(cus_username):
    action = "enter cancel order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    order = []
    unpaid_order = []
    updated_lines = []

    while True:
        order_type = input("""\n-----------------------------------------Cancel Order Page------------------------------------------
Enter 1 to cancel purchase order
Enter 2 to cancel repair order
Enter 3 to quit: """)

        if order_type == "3":
            break

        elif order_type == '1':

            with open("purchase_order_list.txt", "r") as p:
                lines = p.readlines()
                for line in lines:
                    line = line.strip()
                    p_order_id = line.split(",")[0]
                    if cus_username in line:
                        order.append(p_order_id)

            for i in order:
                if order.count(i) == 1:
                    unpaid_order.append(i)

            print("\n--------------------------------------------Order List----------------------------------------------")
            for i in unpaid_order:
                print(i)
            while True:
                cancel_order = input("Please select order to cancel by enter the orderID (Enter Q to quit): ")

                if cancel_order.upper() == "Q":
                    break

                elif cancel_order in unpaid_order:
                    with open("purchase_order_list.txt", "r") as p:
                        lines = p.readlines()
                        for line in lines:
                            line = line.strip()
                            p_order_id = line.split(",")[0]
                            p_order_time = line.split(",")[2]
                            if cancel_order == p_order_id:
                                p_updated_line = line.replace("unpaid", "cancelled")
                                p_updated_line = p_updated_line.replace(p_order_time,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                updated_lines.append(p_updated_line)
                                break

                    with open("purchase_order_list.txt", "a") as p:
                        p.writelines(f"\n{p_updated_line}")
                        print("This order has been cancelled successfully.\n")
                        time.sleep(1)

                    action = "cancel purchase order"
                    with open("customer_system_usage.txt", "a") as csu:
                        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        break

                elif "PO" not in cancel_order:
                    print("This order does not exist.\n")
                    time.sleep(0.5)

                else:
                    print("This order cannot be cancelled.\n")
                    time.sleep(0.5)

        elif order_type == '2':

            with open("repair_order_list.txt", "r") as r:
                lines = r.readlines()
                for line in lines:
                    line = line.strip()
                    r_order_id = line.split(",")[0]
                    if cus_username in line:
                        order.append(r_order_id)

            for i in order:
                if order.count(i) == 1:
                    unpaid_order.append(i)

            print("\n--------------------------------------------Order List----------------------------------------------")
            for i in unpaid_order:
                print(i)

            while True:
                cancel_order = input("Please select order to cancel by enter the orderID (Enter Q to quit): ")

                if cancel_order.upper() == "Q":
                    break

                if cancel_order in unpaid_order:
                    with open("repair_order_list.txt", "r") as r:
                        lines = r.readlines()
                        for line in lines:
                            line = line.strip()
                            r_order_id = line.split(",")[0]
                            r_datetime = line.split(",")[2]
                            if cancel_order == r_order_id:
                                r_updated_line = line.replace('unpaid', 'cancelled')
                                r_updated_line = r_updated_line.replace(str(r_datetime), str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
                                updated_lines.append(r_updated_line)

                    with open("repair_order_list.txt", "a") as r:
                        r.writelines(f"\n{r_updated_line}")
                        print("This order has been canceled successfully.\n")

                    action = "cancel repair order"
                    with open("customer_system_usage.txt", "a") as csu:
                        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        time.sleep(1)
                        break

                elif "RO" not in cancel_order:
                    print("This order does not exist.\n")
                    time.sleep(0.5)

                else:
                    print("This order cannot be cancelled.\n")
                    time.sleep(0.5)

        else:
            print("Wrong input. Please enter 1, 2, or 3.\n")
            time.sleep(0.5)

    action = "quit from cancel order page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def reports(cus_username):
    action = "enter reports page"
    with open("customer_system_usage.txt", "a") as csu:
        csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    purchase_order_count = 0
    complete_purchase_order_count = 0
    repair_order_count = 0
    complete_repair_order_count = 0
    amount_paid = float(0)
    order_list = []
    complete_order_list = []

    while True:
        with open("customer_information.txt", "r") as ci:
            lines = ci.readlines()
            for line in lines:
                line = line.strip()
                p_username = line.split(",")[0]
                if p_username == cus_username:
                    p_ic = line.split(",")[1]
                    p_phone = line.split(",")[2]
                    p_city = line.split(",")[3]
                    p_create_time = line.split(",")[4]

        with open("purchase_order_list.txt", "r") as p:
            lines = p.readlines()
            for line in lines:
                line = line.strip()
                p_username = line.split(",")[1]
                if cus_username == p_username:
                    p_order_id = line.split(",")[0]
                    p_total_price = float(line.split(",")[-2])
                    p_order_status = line.split(",")[-1]
                    if p_order_id not in order_list:
                        purchase_order_count += 1
                        order_list.append(p_order_id)
                    elif p_order_id not in complete_order_list and p_order_status == "complete":
                        complete_purchase_order_count += 1
                        complete_order_list.append(p_order_id)
                    elif p_order_status == "paid":
                        amount_paid += p_total_price

        with open("repair_order_list.txt", "r") as r:
            lines = r.readlines()
            for line in lines:
                line = line.strip()
                r_username = line.split(",")[1]
                if cus_username == r_username:
                    r_order_id = line.split(",")[0]
                    r_total_price = float(line.split(",")[-2])
                    r_order_status = line.split(",")[-1]
                    if r_order_id not in order_list:
                        repair_order_count += 1
                        order_list.append(r_order_id)
                    elif r_order_id not in complete_order_list and r_order_status == "complete":
                        complete_repair_order_count += 1
                        complete_order_list.append(r_order_id)
                    elif r_order_status == "paid":
                        amount_paid += r_total_price

        print(f"""----------------------------------Account Details----------------------------------
Customer Username: {p_username}
Customer IC/Passport Number: {p_ic}
Customer Phone Number: {p_phone}
Customer City of Domicile: {p_city}
Account Created Time: {p_create_time}

--------------------------------------Summary--------------------------------------
Total Purchase Order Created: {purchase_order_count}
Total Purchase Order Completed: {complete_purchase_order_count}
Total Repair Order Created: {repair_order_count}
Total Repair Order Completed: {complete_repair_order_count}
Total Amount Paid: RM{amount_paid:.2f}""")

        action = "check reports"
        with open("customer_system_usage.txt", "a") as csu:
            csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        quit = input("Enter 'Q' to quit:")
        if quit.upper() == 'Q':
            action = "quit from reports page"
            with open("customer_system_usage.txt", "a") as csu:
                csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            break


while True:
    print("""----------------------------------------Main Menu----------------------------------------
Welcome to KL Central Computer Company (KLCCC)!
1. Sign up
2. Login
3. Exit
""")
    ope = input("Please select from option above: ")

    if ope == "1":
        username = str(input("Please create your username: "))
        password = str(input("Please create your password: "))
        name = str(input("Please enter your name: "))
        ic = str(input("Please enter your IC or passport number: "))
        phone = str(input("Please enter your phone number: "))
        city = str(input("Please enter your city of domicile: "))
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        time.sleep(1)
        print("Your registration is now waiting for verification.")
        time.sleep(1)

        customer_register(name,ic,phone,city,date,username,password)

    elif ope == "2":
        cus_username = str(input("Username: "))
        cus_password = str(input("Password: "))
        login_success = customer_login(cus_username,cus_password)

        while login_success == True:
            print("""----------------------------------------Customer Menu----------------------------------------
Please selet from the option below to proceed.
1. Purchase Order
2. Service/Repair Order
3. Modify Purchase/Service/Repair Order
4. Payment for Orders Placed
5. Inquiry of Order Status
6. Cancel Order
7. Collect Order
8. Reports
9. Log Out""")

            try:
                customer_ope = int(input("Please enter your choice: "))

            except ValueError:
                print("Please enter a number between 1 and 9.")
                time.sleep(1.5)

            else:
                if customer_ope < 1 or customer_ope > 9:
                    print("Please enter a number between 1 and 9.")
                    time.sleep(1.5)

                else:
                    if customer_ope == 1:
                        purchase_order(cus_username)
                    elif customer_ope == 2:
                        repair_order(cus_username)
                    elif customer_ope == 3:
                        modify_order(cus_username)
                    elif customer_ope == 4:
                        order_payment(cus_username)
                    elif customer_ope == 5:
                        order_status(cus_username)
                    elif customer_ope == 6:
                        cancel_order(cus_username)
                    elif customer_ope == 7:
                        collect_order(cus_username)
                    elif customer_ope == 8:
                        reports(cus_username)
                    elif customer_ope == 9:
                        print("You had log out successfully!")
                        action = "log out"
                        with open("customer_system_usage.txt","a") as csu:
                            csu.write(f"\n{cus_username},{action},{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                        break

        else:
            print("Invalid ID or Password!")
            time.sleep(0.4)
            continue

    elif ope == "3":
        break

    else:
        print("Invalid input. Please try again.")
        time.sleep(0.5)
        continue
