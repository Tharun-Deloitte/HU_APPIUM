import csv
import tempfile
import shutil


file_path = "..//excel//output_data.csv"

def write_to_csv(data_list):
    # try:
    #     with open(file_path, 'a', newline='') as csv_file:
    #         csv_writer = csv.writer(csv_file)
    #         for data_row in data_list:
    #             csv_writer.writerow(data_row)
    #     print("Data written successfully.")
    # except Exception as e:
    #     print("An error occurred:", str(e))
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(data_list)
        print("Data written successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



def get_last_line_as_list():
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            last_line = None
            for row in csv_reader:
                last_line = row
            if last_line is not None:
                return last_line
            else:
                return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None

def get_first_line_as_list():
    try:
        with open(file_path, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            last_line = None
            for row in csv_reader:
                last_line = row
                break
            if last_line is not None:
                return last_line
            else:
                return None
    except Exception as e:
        print("An error occurred:", str(e))
        return None








def delete_row_by_value(value_to_delete):
    try:
        # Create a temporary file to write the updated data
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, newline='')

        with open(file_path, 'r') as csv_file, temp_file:
            csv_reader = csv.reader(csv_file)
            csv_writer = csv.writer(temp_file)

            for row in csv_reader:
                if row and row[0] != value_to_delete:
                    csv_writer.writerow(row)

        # Replace the original file with the updated data
        shutil.move(temp_file.name, file_path)

        print(f"Rows with value '{value_to_delete}' deleted from {file_path}")
    except Exception as e:
        print("An error occurred:", str(e))





def delete_csv_data():
    try:
        with open(file_path, 'w', newline='') as csv_file:
            csv_file.truncate(0)  # Truncate the file to remove all content
        print("Data deleted successfully.")
    except Exception as e:
        print("An error occurred:", str(e))

def read_csv_to_list():
    data_list = []
    try:
        with open(file_path, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                data_list.append(row)
        return data_list
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


