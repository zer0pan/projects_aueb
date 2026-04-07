# Projects AUEB - Final Assignment

## Description
This repository contains the implementation of the final assignment of a case study for the Data Analysis and Programming in Python 3 course. It is a Python application that handles the ingestion, cleaning, processing, and visualization of meteorological data.

## Repository Contents
- `teliki_ergasia1.py`: The main executable file containing the analysis and visualization logic.
- `weather_data.csv`: The file containing the raw meteorological data.
- `Teliki Ergasia_new.pdf`: The file containing the exercise instructions in Greek
- `final_project.pdf`: The file containing the exercise instructions in English

## Technologies and Tools
The implementation is based on the **Python 3** programming language and utilizes the following libraries:
- **Pandas**: Data manipulation and DataFrame structures.
- **SciPy**: Calculations and implementation of cubic interpolation.
- **NumPy**: Mathematical calculations and array management.
- **Matplotlib**: Generation and saving of plots.

## Implementation - Core Features
The program performs the following steps:
1. **Data Reading**: Loading the dataset into a DataFrame structure.
2. **Preprocessing and Cleaning**: Identifying missing values (NaN).
3. **Data Interpolation**: Using the cubic interpolation method (`interpolate(method="cubic")`) to calculate and fill in the missing records in the maximum and minimum temperature columns.
4. **Statistical Analysis**: Calculating maximum, minimum, mean, median, and standard deviation values.
5. **Visualization**: Creating bar charts, pie charts, and sub-plots to analyze the results. Due to a non-interactive backend (e.g., Agg), the plots are saved directly as image files.

## Preparation and installation instructions

1. Install the required libraries (if you don't have them already installed):
   ```bash
   pip install pandas scipy numpy matplotlib ```