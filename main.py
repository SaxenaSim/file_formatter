import os
import pandas as pd


class CsvProcessor:
    """
    A class to process the csv files and make them compatible with the standard columns.
    """

    def __init__(self, standard_cols: list, files_dir: str, default_dtype: dict):
        self.standard_cols = standard_cols
        self.input_dir = files_dir
        self.output_df = pd.DataFrame()
        self.default_dtype = default_dtype

    def process_csv_file(self, file_path: str):
        """
        Take a file and process it to make it compatible with the standard columns.
        """
        df = pd.read_csv(file_path)
        missing_columns = list(set(self.standard_cols) - set(df.columns))
        for col in missing_columns:
            default_datatype = self.default_dtype.get(col, None)
            df[col] = default_datatype

        df = df[self.standard_cols]
        return df

    def process_files(self):
        """
        Taking all the .csv files one by one in the input directory and  processing them.
        """
        for filename in os.listdir(self.input_dir):
            if filename.endswith(".csv"):
                file_path = os.path.join(self.input_dir, filename)
                processed_df = self.process_csv_file(file_path)
                self.output_df = pd.concat(
                    [self.output_df, processed_df], ignore_index=True
                )

    def write_output(self, result_file: str):
        """
        Writes all the processes data into the output file.
        """
        self.output_df.to_csv(result_file, index=False)
        print("Output file is written successfully.")


def main():
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

    default_datatypes = {
        "transaction_date": str,
        "unique_transaction_id": str,
        "item_code": str,
        "item_sr_no": str,
        "item_manufacture_date": str,
        "discount_price": float,
        "store_no": int,
        "store_name": str,
        "customer_name": str,
        "state": str,
        "zip": str,
    }

    project_dir = os.path.dirname(os.path.abspath(__file__))

    input_dir = os.path.join(project_dir, "input_files")

    obj = CsvProcessor(standard_columns, input_dir, default_datatypes)

    output_dir = os.path.dirname(os.path.abspath(__file__))

    output_file = os.path.join(output_dir, "output/output.csv")

    obj.process_files()
    obj.write_output(output_file)


if __name__ == "__main__":

    main()
