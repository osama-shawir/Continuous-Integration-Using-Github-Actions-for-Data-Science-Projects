"""Python Polars descriptive statistics common functions"""
import io
import polars as pl
import matplotlib.pyplot as plt
import requests

def read_aircraft_data_from_google_drive(file_id):
    """
    Read aircraft wildlife strikes data from 
    Google Drive and return it as a Polars DataFrame.

    Args:
    - file_id (str): The ID of the file hosted on Google Drive.

    Returns:
    - df (pl.DataFrame): The aircraft wildlife strikes data as a Polars DataFrame.
    """
    # Construct the URL for the Google Drive file
    url = f"https://drive.google.com/uc?id={file_id}"
    
    
    # Download the contents of the CSV file
    download = requests.get(url, timeout=1000).content

    # Read the CSV file into a Polars DataFrame
    df = pl.read_csv(io.StringIO(download.decode("utf-8")),
                     low_memory=False, infer_schema_length=10000)
    
    return df
    
def calculate_strikes_max_damage(df):
    strikes = {}
    for c in df.columns:
        column_name = c.split(" ")
        # print(len(col_sep), col_sep)
        if len(column_name) > 1 and column_name[1] == "Strike":
            strikes[column_name[0]] = df[column_name[0] +
            " Damage"].sum() / df[c].sum()
    max_damaged_part = max(strikes, key=strikes.get)
    return strikes, max_damaged_part


def return_25th_quantile(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns 25th quantile of the target column"""

    target_quantile = data_[target].quantile(0.25)

    return target_quantile


def return_mean(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_mean = data_[target].mean()

    return target_mean


def return_std_dev(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the standard deviation of the target column"""

    target_std = data_[target].std()

    return target_std


def return_median(data_: pl.DataFrame, target: str) -> float:
    """Takes in a dataframe and returns the mean of the target column"""

    target_median = data_[target].median()

    return target_median


def visualize_damage_probabilities(strikes, jupyter = False,
                                    visualization_path = 'output/visualization.png'):
    """
    Visualize the aircraft part damage probabilities using a bar chart
    Args:
    - strikes (dict): A dictionary where keys represent aircraft
    parts, and values represent the damage probability.
    """
    # Create a bar chart to visualize the damage probabilities
    plt.bar(strikes.keys(), strikes.values())
    plt.xticks(rotation=90)
    plt.title("Aircraft Part Damage Probability")
    plt.show()
    if not jupyter:
        plt.savefig(visualization_path)  # save png


def generate_summary_report(data, TARGET_COLUMN,
                            summary_report_path = r'output/generated_report.md'): 
    '''Generate a summary report of the data and save it to a markdown file'''
    with open(summary_report_path, "w", encoding="utf-8") as report:
        report.write(f'The target that we are working with is {TARGET_COLUMN} \n \n \n')
        report.write(f'Mean: {round(return_mean(data, TARGET_COLUMN), 3)} \n \n \n')
        report.write(f'Median: {round(return_median(data, TARGET_COLUMN), 3)} \n \n \n')
        report.write(f'StdDev: {round(return_std_dev(data,TARGET_COLUMN), 3)} \n \n \n')
        report.write("\n![Visualization](visualization.png)\n")
  
if __name__ == "__main__":
    file_id = "1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi"
    TARGET_COLUMN = "Aircraft Mass"
    data = read_aircraft_data_from_google_drive(file_id)
    strikes, most_risky_part = calculate_strikes_max_damage(data)
    print('Target Column: ', 'TARGET_COLUMN')
    print('25th Quantile: ', return_25th_quantile(data, TARGET_COLUMN))
    print('Mean: ', return_mean(data, TARGET_COLUMN))
    print('Median: ', return_median(data, TARGET_COLUMN))
    print("Standard Deviation: ", return_std_dev(data, TARGET_COLUMN))
    print('The part most likely to be damaged is the', most_risky_part)
    try:
        generate_summary_report(data, TARGET_COLUMN)
        visualize_damage_probabilities(strikes)
    except FileNotFoundError:
        generate_summary_report(data, TARGET_COLUMN,
                                summary_report_path = r'../output/generated_report.md')
        visualize_damage_probabilities(
                            strikes,
                            visualization_path = 
                            '../output/visualization.png')
