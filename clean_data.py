import pandas as pd

def clean_data(input_file, output_file):
    df = pd.read_csv(input_file, dtype=str)

    df['price'] = df['price'].str.replace('US $', '', regex=False).str.replace(',', '').str.strip()
    df['original_price'] = df['original_price'].str.replace('US $', '', regex=False).str.replace(',', '').str.strip()

    df['original_price'] = df['original_price'].replace('N/A', pd.NA).fillna(df['price'])

    df['shipping'] = df['shipping'].replace(['Shipping N/A', '', ' '], 'Shipping info unavailable')

    df['price'] = pd.to_numeric(df['price'], errors='coerce')
    df['original_price'] = pd.to_numeric(df['original_price'], errors='coerce')

    df['discount_percentage'] = round((1 - (df['price'] / df['original_price'])) * 100, 2)

    df.to_csv(output_file, index=False)

if __name__ == "__main__":
    input_file = "ebay_tech_deals.csv"
    output_file = "cleaned_ebay_deals.csv"
    clean_data(input_file, output_file)
    print(f"Cleaned data saved to {output_file}")