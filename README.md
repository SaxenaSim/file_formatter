# file_formatter

This repository contains two solutions for processing CSV files containing sales data for electronic products. The project aims to standardize the format of the output files while accommodating variations in the incoming data.

## Solutions Overview

1. **Manual Solution**: Developed by myself, this solution involves manually writing code to handle the processing of incoming CSV files. It implements a robust process for validating and transforming the files to conform to a standardized format, ensuring consistency and completeness of the output files.

2. **AI Co-Pilot Solution**: Developed with the assistance of AI Co-Pilot, this solution leverages AI-generated code to automate the processing of incoming CSV files. It utilizes advanced algorithms to analyze the variability in column structures and dynamically adjust the processing logic to meet the specified requirements.

## Sample Data

The final output file contains the following columns:

1. `transaction_date`: Date of the transaction
2. `unique_transaction_id`: Unique identifier for the transaction
3. `item_code`: Code identifying the electronic item
4. `item_sr_no`: Serial number of the item
5. `item_manufacture_date`: Manufacturing date of the item
6. `discount_price`: Discounted price of the item
7. `store_no`: Store number where the transaction occurred
8. `store_name`: Name of the store
9. `customer_name`: Name of the customer
10. `state`: State where the store is located
11. `zip`: ZIP code of the store location

## Repository Structure

- `input/`: Contains all the files which has been processed for the output.
- `output/`: Contains the output file creted by processing.
- `copilot_output/`: Contains the output file created by copilot solution. 
- `copilot_solution.py/`: Contains the solution done using copilot.
- `main.py/`: Contains the solution done without using copilot.
- `README.md`: Provides an overview of the project and its solutions.

## Usage

This repository serves as a demonstration of two approaches to solving the problem of processing sales data from CSV files, offering insights into both manual development and AI-assisted development methodologies.
