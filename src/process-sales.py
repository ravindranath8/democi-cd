import pandas as pd

def process_sales_data(
    input_path="https://raw.githubusercontent.com/ravindranath8/democi-cd/main/your-repo/sales_data.csv",
    output_path="sales_summary.csv"
):
    df = pd.read_csv(input_path)

    # Basic cleaning / processing
    df['total'] = df['price'] * df['quantity']
    
    # Summary stats
    total_revenue = df['total'].sum()
    avg_price = df['price'].mean()
    top_product = df.loc[df['total'].idxmax()]['product']
    
    summary = {
        "Total Revenue": [total_revenue],
        "Average Price": [round(avg_price, 2)],
        "Top Product by Revenue": [top_product],
        "Total Rows Processed": [len(df)]
    }
    
    summary_df = pd.DataFrame(summary)
    summary_df.to_csv(output_path, index=False)
    
    print("Processing complete!")
    print(summary_df)
    
    return summary_df

if __name__ == "__main__":
    process_sales_data()
