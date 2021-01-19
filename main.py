from time import sleep
import datetime
print("Welcome to Copington Adventure Theme Park!")
sleep(2)
print("The ticket prices are:")
sleep(1)
print("Adult - £20, Child - £12, Senior - £11")
def entrance():
  print("How many adult tickets do you want?")
  adult_total = int(input())
  print("How many child tickets do you want?")
  child_total = int(input())
  print("How many senior tickets do you want?")
  senior_total = int(input())
  total_t_cost = (adult_total * 20) + (child_total * 12) + (senior_total * 11)
  return total_t_cost

def wristband():
  print("How many wristbands do you want?")
  wrist_total = int(input())
  total_w_cost = wrist_total * 20
  return total_w_cost

def lead_surname():
  print("What is the lead booker's surname?")
  surname = input()
  return surname

def parking():
  print("Do you require a parking pass? Y/N")
  required = input().upper()
  if required == "Y":
    a = True
  else:
    a = False
  return a

def collect():
  cash = 0
  print("The total cost is:")
  sleep(1)
  print(total_cost)
  sleep(1)
  print("Are you paying with cash or card?")
  pay_option = input().lower()
  if pay_option == "card":
    print("Please wait...")
    sleep(3)
    print("Card accepted")
  elif pay_option == "cash":
    print("Please pay using only £10 and £20 notes")
    sleep(2)
    print("Enter '10' to pay a £10 note")
    sleep(1)
    print("and '20' to pay a £20 note")
    cash = 0
    not_paid = cash < total_cost
    while not_paid:
      note = int(input())
      if note == "10":
        cash = cash + 10
      elif note == "20":
        cash = cash + 20
      else:
        print("Note invalid")
    change = cash - total_cost
    print(f"There is £{change} change")

def issue_ticket():
  print(f"Lead booker's surname: {surname}")
  print(f"Number of adult tickets purchased: {adult_total}")
  print(f"Number of child tickets purchased: {child_total}")
  print(f"Number of senior tickets purchased: {senior_total}")
  if a == True:
    print("Printing car pass")
  date = datetime.datetime.today().strftime ('%d%m%Y')
  print(f"Ticket issued on {date}")



total_t_cost = entrance()
total_w_cost = wristband()
total_cost = total_t_cost + total_w_cost
surname = lead_surname()
a = parking()
collect()
issue_ticket()