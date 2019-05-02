import sys
SERVICE_CHARGE = 2

TICKET_PRICE = 10

tickets_remaining = 100

#Create the calculate price function. It takes number of tickets and returns num of tickets * price
def calculate_price(quantity_of_tickets):
  return (quantity_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

while tickets_remaining >=1 :
  print("There are {} tickets remaining".format(tickets_remaining))
  name  = input("What is your name?  ")
  quantity = input("Hey {}. How many tickets would you like to buy?".format(name))
  try:
    quantity = int(quantity)
    if quantity > tickets_remaining:
      raise ValueError("There are only {} tickets.".format(tickets_remaining))
  except ValueError as err:
    print("Oh no, we ran into an issue. {}. Please try again.".format(err))
  else:
    total_price = calculate_price(quantity)
    print("Your total today is ${}.".format(total_price))
    confirm = input("Do you want to proceed with your purchase? Y/N  ")
    
    if confirm.lower() == "y":
      print("SOLD!")
      tickets_remaining -= quantity
      print("Tickets remaing: {}".format(tickets_remaining))
    else:
      print("Thank you anyways, {}!".format(name))
print("Sorry there are no more tickets")
  