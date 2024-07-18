# Descripton: QAP4.py is a Python script that reads a QAP4 file and generates a QAP4 report.
# Author: Alex R.
# Date: 2024-07-16

# Constants


# Define required libraries.



# Define program constants. 


# Define program functions.

# I want you to Open a file in this same directory called Const.dat.
# import os

# print("Current Working Directory:", os.getcwd())

file_path = "Const.dat"
file = open(file_path, "r")

print("File Opened:", file.name)

# Read the file and display the contents.
# Next Policy Number: 1944
# Basic Premium: 869.00
# Discount for Additional Cars: 0.25
# Extra Liability Coverage: 130.00
# Glass Coverage: 86.00
# Loaner Car Coverage: 58.00
# HST Rate: 0.15
# Processing Fee for Monthly Payments: 39.99

policy_number = file.readline()
basic_premium = file.readline()


# Main program starts here.
while True:

  # Gather user inputs.
  while True:
    try:
      customer_name = input("Enter the customer name (-1 to quit): ")
      if customer_name == "-1":
        break
    except:
      print("Invalid name. Please try again.")
    else:
      break

    if customer_name == "-1":
      break
    


  # Display the customer name.
  print("Customer Name: ", customer_name)




  # Perform required calculations.


  # Display results



# Any housekeeping duties at the end of the program.