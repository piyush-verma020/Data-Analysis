import math
import time

def parse_header(headerline):
    return [h.strip() for h in headerline.strip().split(',')]

def parse_values(data_line):
    values = []
    for item in data_line.strip().split(','):
        if item.strip() == '':
            values.append(0.0)
        else:
            values.append(float(item))
    return values

def read_file(path):
    with open(path) as f:
        lines = f.readlines()

    header = parse_header(lines[0])

    data_dicts = []

    for i in range(1, len(lines)):
        if lines[i].strip() == "":
            continue
        values = parse_values(lines[i])
        while len(values) < len(header):
            values.append(0.0)
        row_dict = dict(zip(header, values))
        data_dicts.append(row_dict)

    return data_dicts
    
def calculate_loan_emi(amount, duration, rate, downpayment=0):
    loan_amount = amount - downpayment
    if rate == 0:
        emi = loan_amount / duration
    else:
        emi = loan_amount * rate * ((1 + rate) ** duration) / (((1 + rate) ** duration) - 1)
    emi = math.ceil(emi)
    return emi

def writing_data(rows):
    with open('EMI.txt', 'w') as f:
        f.write("amount,duration,rate,down_payment,emi\n")
        for row in rows:
            f.write(f"{row['amount']},{row['duration']},{row['rate']},{row['down_payment']},{row['emi']}\n")


file_name = input("Enter the name of the file you wish to open: ")
rows = read_file(file_name)
print("Parsed Data:")
print(rows)

for loan in rows:
    amount = float(loan.get('amount', 0) or 0)
    duration = int(loan.get('duration', 0) or 1)  # Avoiding division by zero
    rate = float(loan.get('rate', 0) or 0) / 12   # Converting the annual rate into months
    down_payment = float(loan.get('down_payment', 0) or 0)

    loan['emi'] = calculate_loan_emi(amount, duration, rate, down_payment)

print("\nData with EMI:")

for row in rows:
    print(row)

print("Writing the data into the file: ", end="")
l = ['.', '..', '...']
for dots in l:
    print(f"\rWriting the data into the file: {dots}", end="", flush=True)
    time.sleep(0.5)

writing_data(rows)

print("\nDone!")