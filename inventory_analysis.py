from pathlib import Path
import pandas as pd

root = Path("/home/kingwiz1/myspace/safezone/inventory_project/")
csv_folder = root / "inventory.csv"
report_file = root / "inventory_report.txt"

def load_inventory():
    return pd.read_csv(csv_folder)

def generate_report(df):
    total_records = len(df)
    
    missing_values = df.isnull().sum()
    
    duplicated_skus = df[df.duplicated(subset=["SKU"], keep=False)]
    
    negative_inventory = df[df["Quantity"] < 0]
    
    print("=" * 50)
    print("INVENTORY ANALYSIS REPORT")
    print("=" * 50)
    
    print(f"\nTotal Records: {total_records}")
    
    print("\nMissing Values")
    print("-" * 50)
    print(missing_values)
    
    print("\nDuplicated SKUs")
    print("-" * 50)
    print(duplicated_skus)
    
    print("\nNegative Inventory")
    print("-" * 50)
    print(negative_inventory)
    
     # ---------- SAVE REPORT TO FILE ----------
    report_file = Path("inventory_report.txt")
    with open(report_file, "w") as f:
        f.write("=" * 50 + "\n")
        f.write("INVENTORY ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n\n")

        f.write(f"Total Records: {total_records}\n\n")

        f.write("Missing Values\n")
        f.write("-" * 50 + "\n")
        f.write(str(missing_values) + "\n\n")

        f.write("Duplicated SKUs\n")
        f.write("-" * 50 + "\n")
        f.write(str(duplicated_skus) + "\n\n")

        f.write("Negative Inventory\n")
        f.write("-" * 50 + "\n")
        f.write(str(negative_inventory) + "\n")
    
def main():
    df = load_inventory()
    generate_report(df)

if __name__ == "__main__":
    main()