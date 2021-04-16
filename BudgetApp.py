class Budget:
  def __init__(self, amount, catergory):
    self.amount = amount
    self.catergory = catergory
    self.balance = float(1000)
    self.expenditure = float(0)

  
  def available_options(self):
    print('These are the available an options')
    print('1. Deposit')
    print('2. Withdraw')
    print('3. Check balance')
    print('4. Transfer \n')
    selected_option = int(input('Please choose your preferred option: \n'))

    while True:
      if selected_option == 1:
        self.deposit()
        break

      elif selected_option == 2:
        self.withdraw()
        break

      elif selected_option == 3:
        self.check_balance()
        break

      elif selected_option == 4:
        self.funds_transfer()
        break

      else:
        print('Invalid option selected. Try again')
        selected_option = int(input('Please choose your preferred option: \n'))
        continue
  
  def check_balance(self):
    print(f' The available balance for {self.catergory} is NGN{self.balance} \n')

  def withdraw(self):
    amount = float(input(f'How much would you like to withdraw from {self.catergory}: \n'))
    if self.balance >= amount:
      if amount >= 100:
        self.expenditure += amount
        self.balance -= amount
        print('The withdrawal was successful')
        print(f'Your remaining balance is NGN{self.balance}')

      else:
          print('You cannot withdraw less than NGN100 \n')

    else:
      print('Insufficient fund')
      print('Please deposit some money and try again')

  def deposit(self):
    deposit_funds = int(input(f'How much would you like to deposit for {self.catergory} \n'))
    self.balance += deposit_funds
    print(f'Your deposit of NGN{deposit_funds} was successfull. \n')
    print(f'Your current balance is NGN{self.balance}.')

  def funds_transfer(self, catergory):
    transfer_amount = int(input(f'How much would you like to transfer? \n'))
    self.amount -= transfer_amount
    catergory.amount += transfer_amount
    print('Transfer was successful')
    print(f'The {self.name} balance is now NGN{self.amount}.')
    print(f'The new balance of {catergory.name} is now NGN{catergory.amount}. \n')




food = Budget(250, 'food')
clothing = Budget(250, 'clothing')
entertainment = Budget(250, 'entertainment')

print('*** Welcome to the Zuri Budget App ***')
print('The Catergory List')
print('''
1. Food
2. Clothing
3. Entertainment
''')

catergory = int(input('Please select a catergory: \n'))
while True:
  if catergory == 1:
    print(f'{food.catergory}')
    food.available_options()
    break

  elif catergory == 2:
    print(f'{clothing.catergory}')
    clothing.available_options()
    break

  elif catergory == 3:
    print(f'{entertainment.catergory}')
    entertainment.available_options()
    break

  else:
    print('Invalid option, try again')
    catergory = int(input('Please select a catergory: \n'))