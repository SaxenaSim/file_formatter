import csv
import os

# Define the standard columns
standard_columns = [
    "transaction_date",
    "unique_transaction_id",
    "item_code",
    "item_sr_no",
    "item_manufacture_date",
    "discount_price",
    "store_no",
    "store_name",
    "customer_name",
    "state",
    "zip",
]

column_types = {
    "transaction_date": str,
    "unique_transaction_id": str,
    "item_code": str,
    "item_sr_no": str,
    "item_manufacture_date": str,
    "discount_price": float,
    "store_no": str,
    "store_name": str,
    "customer_name": str,
    "state": str,
    "zip": str,
}

# Define the default values for each data type
default_values = {str: "", int: 0, float: 0.0}

input_directory = "input_files"
output_file_path = "copilot_output/copilot_output.csv"

# Get a list of all files in the input directory
input_files = os.listdir(input_directory)

# Initialize the output CSV file
with open(output_file_path, "w", newline="", encoding="utf-8") as output_file:
    writer = csv.writer(output_file)

    # Write the standard columns to the output file
    writer.writerow(standard_columns)

    # Loop over each file
    for input_file in input_files:
        # Open the input file
        with open(
            os.path.join(input_directory, input_file), "r", encoding="utf-8"
        ) as file:
            reader = csv.reader(file)
            incoming_columns = next(reader)  # Get the column names from the first row

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
