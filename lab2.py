def validation_mesg():
    while True:
        option = input('Are you logged in as a user (yes/no): ').strip().lower()
        if option in ['yes', 'no']:
            if option == 'yes':
                account_option = input('Do you have an account (yes/no) ? ').strip().lower()
                if account_option in ['yes', 'no']:
                    if account_option == 'yes':
                        global user
                        user = login()
                    elif account_option == 'no':
                        user = register()
                    else:
                        print("Wrong input")
                        continue
                else:
                    print('You can only input yes/no')
                    continue
            else:  # option == 'no'
                print('Hello admin')
                user = login()  # Assuming login function handles admin login
        else:
            print('Please input yes or no.')
            continue

        if user:
            print(f'Login successful as {user["username"]}')
            if user['role'] == 'admin':
                while True:
                    print('Hi Admin')
                    print('List Menu:\n 1. Display Cars\n 2. Add Car\n 3. Remove Car\n 4. Display Rentals\n 5. Delete User Rental Data\n 6. Exit Program')
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                        if menu_num == 1:
                            display_car()
                        elif menu_num == 2:
                            add_data()
                        elif menu_num == 3:
                            delete()
                        elif menu_num == 4:
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                display_rental_for_admin()
                        elif menu_num == 5:
                            if len(data_rental_car) == 0:
                                print('No rentals yet.')
                            else:
                                delete_rental_for_admin()
                        elif menu_num == 6:
                            break
                        else:
                            print('Invalid option. Please choose again.')
                    else:
                        print('Please input an integer.')
            else:  # Regular user
                while True:
                    print('Welcome User')
                    print('List Menu:\n 1. Display Available Cars\n 2. Rent a Car\n 3. Display Rentals \n 4. Exit Program')
                    menu_num = input('Enter your chosen number: ')
                    if menu_num.isdigit():
                        menu_num = int(menu_num)
                        if menu_num == 1:
                            display_car()
                        elif menu_num == 2:
                            rental_vehicle()
                        elif menu_num == 3:
                            if len(data_rental_car) == 0:
                                print('You haven\'t rented any car yet.')
                            else:
                                display_rental()
                        elif menu_num == 4:
                            break
                        else:
                            print('Invalid option. Please choose again.')
                    else:
                        print('Please input an integer.')
        else:
            print('Wrong username or password')

