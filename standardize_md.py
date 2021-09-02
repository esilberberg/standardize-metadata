import pandas as pd

path = input ("Copy and paste path to CSV: ")

df = pd.read_csv(path)

for i in df.index:
    series = df['Series'][i]
    subseries = df['SubSeries'][i]
    box = df['Box'][i]
    folder = df['Folder'][i]
    size = df['FormatOfOriginal'][i]
    hof = "From the Hall of Fame for Great Americans collection at Bronx Community College, City University of New York."

    print(df['title'][i])
    description = f"{hof} {series}. {subseries}. Box: {box}. Folder: {folder}. Format: {size}."

    df["description"][i] = description
    df["file"][i] = df["identifier"][i] + ".pdf"

    df.to_csv(path, index=False)
