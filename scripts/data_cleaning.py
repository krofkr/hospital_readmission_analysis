import pandas as pd

def clean_data(filepath):
    df = pd.read_csv(filepath)

    print("Original column names:")
    print(df.columns.tolist())

    # Keep relevant columns only
    df = df[['Year', 'Strata', 'Strata Name', 'County', '30-day Readmission Rate (ICD-9)']]
    df = df.rename(columns={
        'Strata': 'Strata',
        'Strata Name': 'Group',
        'County': 'Region',
        '30-day Readmission Rate (ICD-9)': 'Readmission Rate (%)'
    })

    # Drop rows with missing rate values
    df = df.dropna(subset=['Readmission Rate (%)'])

    # Convert percentages to float if needed
    if df['Readmission Rate (%)'].dtype == 'object':
        df['Readmission Rate (%)'] = df['Readmission Rate (%)'].str.replace('%', '').astype(float)

    return df