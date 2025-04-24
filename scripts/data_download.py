import os

def download_readmission_data():
    data_dir = os.path.join(os.getcwd(), 'data', 'raw')
    file_path = os.path.join(data_dir, 'hospital_readmission_ca.csv')

    if not os.path.exists(file_path):
        print(f"Dataset not found at {file_path}.")
        print("Please download the dataset manually from the California Health and Human Services Open Data Portal:")
        print("https://data.chhs.ca.gov/dataset/all-cause-unplanned-30-day-hospital-readmission-rate-california")
        print(f"After downloading, place the file in the following directory: {data_dir}")
        return None
    else:
        print(f"Dataset found at {file_path}.")
        return file_path