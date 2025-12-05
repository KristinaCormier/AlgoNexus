import psycopg2
import pandas as pd
import os
import glob
from io import StringIO


def main():

    # Connect to localhost:15432 (the tunnel endpoint)
    conn = psycopg2.connect(
        host="localhost",
        port=15432,
        database="algtrading2025_db",
        user="user",
        password="your_db_password"
    )

    #Insertion Code
    csvStockDirectory = "./input"
    csv_files = glob.glob(os.path.join(csvStockDirectory, "*.csv"))

    csv_filenames = [os.path.basename(file) for file in csv_files]

    cursor = conn.cursor()

    logFile = open("./output/RawInsertLog.txt", "a")

    for i in range(len(csv_files)):

        try:
            # Read CSV and clean data
            currentDataFrame = pd.read_csv(csv_files[i])

            currentBaseName = os.path.splitext(csv_filenames[i])[0].lower()
            print(f"Now inserting into {currentBaseName}: ", csv_filenames[i])
            logFile.write(currentBaseName + ":\n")

            # Ensure correct data types
            currentDataFrame['open'] = currentDataFrame['open'].astype(float)
            currentDataFrame['low'] = currentDataFrame['low'].astype(float)
            currentDataFrame['high'] = currentDataFrame['high'].astype(float)
            currentDataFrame['close'] = currentDataFrame['close'].astype(float)
            currentDataFrame['volume'] = currentDataFrame['volume'].astype(int)

            # Use COPY for bulk insertion
            buffer = StringIO()
            currentDataFrame.to_csv(buffer, index=False, header=False)
            buffer.seek(0)

            cursor.copy_from(buffer, f'market.{currentBaseName}', sep=',',
                             columns=['date', 'open', 'low', 'high', 'close', 'volume'])
            conn.commit()

            logFile.write(f"Successfully inserted {len(currentDataFrame)} rows from {os.path.basename(csv_file)}\n")

        except Exception as e:
            logFile.write(f"Insert Error: {e}\n")
            conn.rollback()
            continue

    logFile.write(f" Sector Insertion:\n")
    # End of i loop

    csvSectorFilePath = "./output/SectorFixedList.csv"
    sector_df = pd.read_csv(csvSectorFilePath)

    row_tuples = [
        (row['Symbol'], float(row['Sector']))
        for _, row in sector_df.iterrows()
    ]
    try:
        cursor.executemany("""INSERT INTO market.Sectors
                                           (Symbol, Sector)
                                       VALUES (%s, %s)""", row_tuples)
        conn.commit()
        logFile.write(f" Successfully inserted Sector Data: {e}\n")

    except psycopg2.Error as e:
        logFile.write(f" Insert Error: {e}\n")
        conn.rollback()

    cursor.close()
    conn.close()

#End of Main
if __name__ == "__main__":
    main()
