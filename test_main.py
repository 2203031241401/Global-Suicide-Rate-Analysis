import os
import pandas as pd

def test_csv_load():
    # ✅ FIXED PATH (use raw string)
    path = 

    # Debug: check path
    print("Checking path:", path)

    # Check if file exists
    if not os.path.isfile(path):
        print("❌ File not found:", path)
        return

    try:
        # Read CSV
        df = pd.read_csv(path)

        # Check if empty
        if df.empty:
            print("❌ File is empty")
        else:
            print("✅ CSV loaded successfully")
            print(df.head())

    except Exception as e:
        print("❌ Error reading CSV:", e)


# ✅ Call the function (IMPORTANT — your code was missing this!)
if __name__ == "__main__":
    test_csv_load()