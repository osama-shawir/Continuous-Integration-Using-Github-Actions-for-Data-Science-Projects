# -*- coding: utf-8 -*-
"""Module including AircraftAnalytics function"""
# # Polars Descriptive Statistics Assignment
# ## Aircraft wildlife strikes data | 1990 - 2015

# In this exercise, we will extract and analyze aircraft wildlife strikes data
# and we will determine the probability of 
# each part of an aircraft getting damaged 
# by an aircraft wildlife strike

import lib

# Import the necessary libraries
def AircraftAnalytics(file_id = '1TAD7Uyc9PjByt_q13uvGXGeubXnujnUi',
                       TARGET_COLUMN = "Aircraft Mass"):
    """This is a function to run some analytics
    on aircraft wildlife accidents data"""   
    # Read our data from Google Drive
    # Download the contents of the CSV file
    df = lib.read_aircraft_data_from_google_drive(file_id)
    s, m = lib.calculate_strikes_max_damage(df)
    print(lib.return_25th_quantile(df, TARGET_COLUMN))
    print(lib.return_mean(df, TARGET_COLUMN))
    print(lib.return_std_dev(df, TARGET_COLUMN))
    print(lib.return_25th_quantile(df, TARGET_COLUMN))
    try:
        lib.generate_summary_report(df, TARGET_COLUMN)
        lib.visualize_damage_probabilities(s)
    except FileNotFoundError:
        lib.generate_summary_report(df, TARGET_COLUMN,
                                summary_report_path = r'../output/generated_report.md')
        lib.visualize_damage_probabilities(
                                        s,
                                        visualization_path= 
                                        '../output/visualization.png')


if __name__ == "__main__":
    AircraftAnalytics()
