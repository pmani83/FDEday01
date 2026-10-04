import csv

def display(value):
    if value is None or value.strip() == "":
        return "Missing"
    return value


total_invoices_received = 0
total_invoices_greater_than_100000 = 0
missing_amount = 0
invalid_amount = 0

with open('data/invoices.csv', 'r') as file, open('data/outputs.csv', 'w', newline='') as output:
    reader = csv.DictReader(file)
    writer = csv.writer(output)
    writer.writerow(['invoice_id', 'vendor', 'amount', 'status', 'message'])

    for row in reader:
        total_invoices_received += 1
        invoice_id = display(row['invoice_id'])
        vendor = display(row['vendor'])
        status = display(row['status'])
        amount_text = row['amount'].strip()

        if amount_text == "":
            missing_amount += 1
            message = "Missing amount"
            print(f"Invoice Id: {invoice_id}, Vendor: {vendor}, Amount: Missing, Status: {status}")
            writer.writerow([invoice_id, vendor, "Missing", status, message])
        else:
            try:
                amount = float(amount_text)
                if amount > 100000:
                    total_invoices_greater_than_100000 += 1
                    message = "Amount is greater than 100000"
                else:
                    message = "Amount is less than 100000"
                print(f"Invoice Id: {invoice_id}, Vendor: {vendor}, Amount: {amount}, Status: {status}, {message}")
                writer.writerow([invoice_id, vendor, amount, status, message])
            except ValueError:
                invalid_amount += 1
                message = "Invalid amount"
                print(f"Invoice Id: {invoice_id}, Vendor: {vendor}, Amount: {amount_text}, Status: {status}, Invalid Amount: {amount_text}")
                writer.writerow([invoice_id, vendor, amount_text, status, message])

        print("Processing complete")

print(f"Total invoices received: {total_invoices_received}")
print(f"Total invoices greater than 100000: {total_invoices_greater_than_100000}")
print(f"Missing amount: {missing_amount}")
print(f"Invalid amount: {invalid_amount}")
print(f"Missing or invalid amount: {missing_amount + invalid_amount}")