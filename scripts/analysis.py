def avg_readmission_by_region(df):
    return df.groupby('Region')['Readmission Rate (%)'].mean().sort_values(ascending=False)

def readmission_by_group(df):
    return df.groupby('Group')['Readmission Rate (%)'].mean().sort_values(ascending=False)