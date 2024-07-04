from bank import BankAccount as b

account = b("John Doe", 1000)

def main():
    while(True):
        print('Account infos:')
        account.info()
        print('Options: ')
        print('1. Deposit')
        print('2. Withdraw')
        print('0. Exit')

        print('Please select your choices:')
        choice = int(input())

        if choice == 1:
            print('Enter amount to deposit: ')
            amount = int(input())
            account.deposit(amount)
        
        elif choice == 2:
            print('Enter amount to withdraw: ')
            amount = int(input())
            account.withdraw(amount)
        
        elif choice == 0:
            print('Thank you for using our service!')
            break

        else:
            print('Invalid choice, please try again!')
            continue

if __name__ == "__main__":
    main()

