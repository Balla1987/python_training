print "Welcome the menu-maker program!"
print "="*40

menu_list = {}
abort_answer = "no"

while True:
    menu = raw_input("Please enter a menu!")
    print menu
    try:
        price = float(raw_input("Please enter a price too!"))
        print price
        menu_list = {menu: price, menu: price}
    except ValueError:
        print("That's not a price! Please restart the program!")
        break

    new_menu = raw_input("Would you like enter an another menu? Just press enter to continue, or type no!")
    if new_menu == abort_answer.lower():
        print "Thank you!"
        break
    menu_2 = raw_input("Please enter a menu!")
    print menu_2
    try:
        price_2 = float(raw_input("Please enter a price too!"))
        print price_2
        menu_list = {menu_2: price_2, menu: price}
    except ValueError:
        print("That's not a price! Please restart the program!")
        break
    noMore_test = raw_input("And that's the end of the trial version! Please enter!")
    break

print "All menus are: %s" % menu_list
