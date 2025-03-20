# e-Bay Tech Deals Analysis 

## Overview
This project focuses on analyzing eBay's tech deals by scraping data from eBay's Global Tech Deals page, cleaning and processing the data, and performing exploratory data analysis (EDA) to uncover insights about product prices, discounts, shipping information, and more.

## Key Features
- **Automated Data Scraping**: Extracts product details from eBay’s Global Tech Deals page.
- **Data Cleaning & Processing**: Prepares the data for analysis by handling missing values and formatting inconsistencies.
- **Exploratory Data Analysis (EDA)**: Identifies trends and patterns in pricing, discounts, and shipping information.
- **Visualization**: Generates insightful visual representations of the data.
- **GitHub Actions Integration**: Automates the data scraping and analysis workflow every 3 hours 

---

## Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)

### Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Chafic123/eBay-Global-Tech-Scraping.git
   cd e-bay-tech-deals-analysis
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Data Scraping Script**
   ```bash
   python scraper.py
   ```
   This will generate `ebay_tech_deals.csv`.

4. **Clean and Process the Data**
   ```bash
   python clean_data.py
   ```
   This will generate `cleaned_ebay_deals.csv`.

5. **Perform EDA and Visualization**
   ```bash
   jupyter notebook EDA.ipynb
   ```

---

## Tasks and Workflow

### 1. Data Scraping
**Script:** `scrape_data.py`
- Scrapes product details (title, price, original price, shipping, and URL) from eBay’s Global Tech Deals page.
- Saves the data to `ebay_tech_deals.csv`.

### 2. Data Cleaning & Processing
**Script:** `clean_data.py`
- Cleans the `price` and `original_price` columns by removing currency symbols and formatting inconsistencies.
- Replaces missing `original_price` values with the corresponding `price`.
- Normalizes shipping information.
- Converts price columns to numeric values.
- Computes a new `discount_percentage` column.
- Saves the cleaned data to `cleaned_ebay_deals.csv`.

### 3. Exploratory Data Analysis (EDA)
**Notebook:** `EDA.ipynb`
- Analyzes product pricing trends and discount distributions.
- Evaluates time series patterns for deal postings.
- Examines shipping options and keyword frequencies in product titles.
- Computes absolute discounts and highlights top deals.

### 4. Visualization
**Notebook:** `EDA.ipynb`
- Generates key visualizations such as:
  - **Bar charts**: Number of deals per hour and shipping options.
  - **Histograms & Boxplots**: Price and discount distributions.
  - **Scatter Plots**: Original price vs. discounted price.
  - **Keyword Analysis**: Commonly used words in product titles.

---

## Key Insights
- **Time Series Analysis**: Most deals are posted at specific hours of the day.
- **Price Distribution**: Majority of products fall between `$200 - $800`, with high-priced outliers.
- **Discount Trends**: Most products have moderate discounts (`10-30%`), with deep discounts being rare.
- **Shipping Information**: Free shipping is the most common option, followed by "Shipping info unavailable".
- **Keyword Analysis**: "Apple", "iPhone", and "Laptop" are frequently mentioned in product titles.

---

## Dependencies
- **Python 3.x**
- **Libraries Used:**
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`
  - `selenium`
  - `webdriver_manager`
  - `fake_useragent`

---

## Automation with GitHub Actions
This project includes GitHub Actions to automate the scraping and analysis process. The workflow is defined in `.github/workflows/`. 

### Automated Workflow
1. **Scheduled Data Scraping**: Runs periodically to fetch the latest deals.
2. **Data Processing**: Cleans and updates the dataset.
3. **Visualization Update**: Refreshes the EDA results.
4. **Commit & Push Updates**: Automatically updates the repository with new data and insights.

---

## Contributing
Contributions are welcome! Follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`feature-branch-name`).
3. Implement your changes and commit.
4. Push to your branch and open a pull request.


## Acknowledgments
- **eBay** for providing the data through their Global Tech Deals page.
- **Open-source community** for the libraries used in this project.

---

