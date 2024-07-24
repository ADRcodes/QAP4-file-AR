# Descripton: This program is a simple insurance policy generator. It reads the policy information from a file, gathers customer information, and generates a policy report. The program also keeps track of the next policy number and updates the file accordingly.
# Author: Alex R.
# Date: 2024-07-16


## Define required libraries.

import time
import datetime


## Define program constants. 

current_date = datetime.datetime.now()

file_path = "Const.dat"
file = open(file_path, "r")

for line in file:
  key, value = line.strip().split(': ')
  if key == "Next Policy Number":
    next_policy_number = int(value)
  elif key == "Basic Premium":
    basic_premium = float(value)
  elif key == "Discount for Additional Cars":
    discount_for_additional_cars = float(value)
  elif key == "Extra Liability Coverage":
    extra_liability_coverage_cost = float(value)
  elif key == "Glass Coverage":
    glass_coverage_cost = float(value)
  elif key == "Loaner Car Coverage":
    loaner_car_coverage_cost = float(value)
  elif key == "HST Rate":
    hst_rate = float(value)
  elif key == "Processing Fee for Monthly Payments":
    processing_fee_for_monthly_payments = float(value)

file.close()

# Define program functions.

def customizable_progress_bar(total, width=50):
    for i in range(total + 1):
        percent = (i / total) * 100
        filled_length = int(width * i // total)
        bar = '#' * filled_length + '-' * (width - filled_length)
        print(f"\r|{bar}| {percent:.2f}% Complete", end='', flush=True)
        time.sleep(0.1)
    print()  

## Main program starts here.
while True:

  ## Gather user inputs.
  while True:
    try:
      print("\n\n---Enter the customer information---\n")
      customer_first_name = str(input("Enter the customer first name (-1 to quit): ")).title()
      if customer_first_name == "-1":
        break
    except:
      print("Invalid name. Please try again.")
    else:
      break

  if customer_first_name == "-1":
    break

  while True:
    try:
      customer_last_name = str(input("Enter the customer last name: ")).title()
    except:
      print("Invalid name. Please try again.")
    else:
      break

  
  while True:
    try:
      customer_address = str(input("Enter the customer address: "))
    except:
      print("Invalid address. Please try again.")
    else:
      break

  while True:
    try:
      customer_city = str(input("Enter the customer city: "))
    except:
      print("Invalid city. Please try again.")
    else:
      break

  valid_provinces = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
  while True:
    try:
      customer_province = str(input("Enter the customer province: ")).upper()
      if customer_province not in valid_provinces:
        print("Invalid entry. Province must be a 2 letter abbreviation of existing province. Please try again.")
        continue
    except:
      print("Invalid entry. Province must be a 2 letter abbreviation of existing province. Please try again.")
    else:
      break
  
  while True:
    try:
      customer_postal_code = str(input("Enter the customer postal code: ")).upper()
      if len(customer_postal_code) != 6:
        print("Postal code must be 6 digits long. Please try again.")
        continue
      if not customer_postal_code[0].isalpha() or not customer_postal_code[2].isalpha() or not customer_postal_code[4].isalpha() or not customer_postal_code[1].isdigit() or not customer_postal_code[3].isdigit() or not customer_postal_code[5].isdigit():
        print("Postal code must be in the format A1A1A1. Please try again.")
        continue
    except:
      print("Invalid postal code. Please try again.")
    else:
      break

  while True:
    try:
      number_of_cars = int(input("Enter the number of cars: "))
    except:
      print("Invalid number of cars. Please try again.")
    else:
      break
  
  while True:
    try:
      extra_liability = str(input("Do you want extra liability coverage up to $1,000,000? (Y/N): ")).upper()
      if extra_liability != "Y" and extra_liability != "N":
        print("Invalid input. Please enter Y or N.")
        continue
    except:
      print("Invalid input. Please enter Y or N.")
    else:
      break
    
  while True:
    try:
      glass_coverage = str(input("Do you want glass coverage? (Y/N): ")).upper()
      if glass_coverage != "Y" and glass_coverage != "N":
        print("Invalid input. Please enter Y or N.")
        continue
    except:
      print("Invalid input. Please enter Y or N.")
    else:
      break

    # optional loaner car coverage (Y or N)
  while True:
    try:
      loaner_car_coverage = str(input("Do you want loaner car coverage? (Y/N): ")).upper()
      if loaner_car_coverage != "Y" and loaner_car_coverage != "N":
        print("Invalid input. Please enter Y or N.")
        continue
    except:
      print("Invalid input. Please enter Y or N.")
    else:
      break


  valid_payment_options = ["Full", "Monthly", "Down Pay"]
  while True:
    try:
      payment_option = str(input("Do you want to pay in full or monthly? (Full/Monthly/Down Pay): ")).title()
      if payment_option not in valid_payment_options:
        print("Invalid input. Please enter Full, Monthly, or Down Pay.")
        continue
    except:
      print("Invalid input. Please enter Full, Monthly, or Down Pay.")
    else:
      break

  if payment_option == "Down Pay":
    while True:
      try:
        down_payment = float(input("Enter the down payment amount: "))
      except:
        print("Invalid amount. Please try again.")
      else:
        break

  claims = []
  while True:
    while True:
      try:
        claim_number = int(input("Enter the claim number (-1 to quit): "))
        if claim_number == -1:
          break
      except:
        print("Invalid claim number. Please try again.")
      else:
        break
    
    if claim_number == -1:
      break

    while True:
      try:
        claim_date = str(input("Enter the claim date (YYYY-MM-DD): "))
      except:
        print("Invalid date. Please try again.")
      else:
        break

    while True:
      try:
        claim_amount = float(input("Enter the claim amount: "))
      except:
        print("Invalid amount. Please try again.")
      else:
        break

    claims.append({"claim_number": claim_number, "claim_date": claim_date, "claim_amount": claim_amount})

  # Perform required calculations.

  total_premium = basic_premium - (discount_for_additional_cars * (number_of_cars - 1))
  if extra_liability == "Y":
    total_premium += extra_liability_coverage_cost * number_of_cars
  if glass_coverage == "Y":
    total_premium += glass_coverage_cost * number_of_cars
  if loaner_car_coverage == "Y":
    total_premium += loaner_car_coverage_cost * number_of_cars
  
  hst = total_premium * hst_rate
  total_cost = total_premium + hst

  if payment_option == "Monthly":
    total_cost += processing_fee_for_monthly_payments
    monthly_payment = total_cost / 8
  if payment_option == "Down Pay":
    total_cost = total_cost + processing_fee_for_monthly_payments - down_payment
    monthly_payment = total_cost / 8

  # Display results

  print("\n\nGenerating Report...\n")
  customizable_progress_bar(25, 25)

  print("_" * 40)
  print("\033[1;31mOne Stop Insurance Company\033[0m\n".center(50, " "))
  print(f"Policy Number: {next_policy_number}".ljust(24) + f"Date: {current_date.strftime('%Y-%m-%d')}".ljust(20))
  print("\nCustomer Information:\n")
  print(customer_first_name, customer_last_name, sep=" ")
  print(customer_address)
  print(customer_city + ", " + customer_province + ", " + customer_postal_code)

  print("")
  print("Number of Cars:".ljust(28), number_of_cars)
  print("Extra Liability Coverage:".ljust(28), extra_liability)
  print("Glass Coverage:".ljust(28), glass_coverage)
  print("Loaner Car Coverage:".ljust(28), loaner_car_coverage)
  print("Payment Option:".ljust(28), payment_option)
  if payment_option == "Down Pay":
    down_payment_dsp = f"${down_payment:.2f}"
    print("Down Payment:".ljust(28), down_payment_dsp)
  print("")
  print("   Claims #    Claim Date       Amount")
  print("   -----------------------------------")

  for claim in claims:
    claim_number = f"{claim['claim_number']:>5}"
    claim_date = claim['claim_date']
    claim_amount = f"${claim['claim_amount']:,.2f}"
    print(f"    {claim_number}      {claim_date} {claim_amount:>12}")
  
  print()
  print("Thank you for shopping with us!".center(40, " "))
  print("_"*40)


## Any housekeeping duties at the end of the program.

file = open(file_path, "r")
lines = file.readlines()
file.close()

file = open(file_path, "w")
for line in lines:
  key, value = line.strip().split(': ')
  if key == "Next Policy Number":
    file.write(f"Next Policy Number: {next_policy_number + 1}\n")
  else:
    file.write(line)
file.close()
