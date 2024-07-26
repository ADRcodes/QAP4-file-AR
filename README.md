# QAP 4 Files

## Overview
This repository contains:

- An ERD for managing rooms, bookings, customers, revenues, and supplies.
- Python code to generate insurance claims.
- An HTML file to render and display complex objects.

## Entity Relationship Diagram (ERD)
### Tables
1. Defaults

    - invoice_number, room_rate, hst_rate, early_check_in_rate, extra_bed_rate, extra_key_rate, late_check_out_rate

2. Room Status

    - room_id, customer_id, booking_id, check_in_date, check_out_date, early_check_in, extra_bed, extra_key, late_check_out

3. Bookings

    - booking_id, customer_id, room_id, check_in_date, check_out_date, booking_date, early_check_in, extra_bed, extra_key, late_check_out, booking_source

4. Customer

    - customer_id, customer_name, customer_address, customer_phone, customer_credit_card, customer_card_expiry, loyalty_status

5. Revenue

    - revenue_id, booking_id, invoice_number, invoice_date, payment_method, room_charge, extras_charge, subtotal, taxes, total, payment_status

6. Supplies

    - supply_id, supply_description, supply_type, supply_quantity, reorder_level, restock_date

### Additional Fields
- Booking Source: Tracks how the booking was made.
- Loyalty Status: Indicates customer loyalty level.
- Restock Date: Records the last restock date of supplies.

## Python Code
Generates insurance claims.

## HTML File
Renders and displays complex objects.

# Usage
Clone the repository:
- git clone https://github.com/adrcodes/qap4-file-ar.git

Navigate to the project directory:
- cd sleep-tite-motel

License
- This project is licensed under the MIT License.
