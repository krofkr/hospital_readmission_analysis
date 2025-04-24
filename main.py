from scripts.data_download import download_readmission_data
from scripts.data_cleaning import clean_data
from scripts.analysis import (
    avg_readmission_by_region,
    readmission_by_group
)
from scripts.visualization import bar_chart

file_path = download_readmission_data()

if file_path:
    df = clean_data(file_path)

    region_data = avg_readmission_by_region(df)
    group_data = readmission_by_group(df)

    print("Displaying readmission rate by region...")
    bar_chart(region_data, "Average Readmission Rate by Region", "Region", "Readmission Rate (%)")

    print("Displaying readmission rate by group (age, gender, etc.)...")
    bar_chart(group_data, "Average Readmission Rate by Group", "Group", "Readmission Rate (%)")
else:
    print("Exiting program due to download error.")