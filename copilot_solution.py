import csv

# Define the standard columns
standard_columns = ['transaction_date', 'unique_transaction_id', 'item_code', 'item_sr_no', 'item_manufacture_date', 'discount_price', 'store_no', 'store_name', 'customer_name', 'state', 'zip']

# Define the default values for missing columns
default_values = {
    'transaction_date': '',
    'unique_transaction_id': '',
    'item_code': '',
    'item_sr_no': '',
    'item_manufacture_date': '',
    'discount_price': '',
    'store_no': '',
    'store_name': '',
    'customer_name': '',
    'state': '',
    'zip': ''
}

# Read the incoming CSV file
with open('incoming_file.csv', 'r') as file:
    reader = csv.reader(file)
    incoming_columns = next(reader)  # Get the column names from the first row

    # Initialize the output CSV file
    with open('output_file.csv', 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        # Write the standard columns to the output file
        writer.writerow(standard_columns)
        
        # Process each row in the incoming file
        for row in reader:
            output_row = []
            
            # Check if each standard column is present in the incoming file
            for column in standard_columns:
                if column in incoming_columns:
                    # Append the value from the incoming file
                    output_row.append(row[incoming_columns.index(column)])
                else:
                    # Append the default value for missing columns
                    output_row.append(default_values[column])
            
            # Write the processed row to the output file
            writer.writerow(output_row)