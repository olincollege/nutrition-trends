# Nutrition Trends Project Documentation README

This repository contains a notebook that analyzes nutrition trends through 3 different visualizations of data. One gotten by calculating the Nutrient Rich Food index (NRF) Score of the 10 most common foods in America, another by comparing the daily value of certain nutrients and the actual percentage of daily value.


## Repository Contents
- usda_api_data.py: A python script which loads data into a JSON file 
- datamanipulation.py: A python script which goes through the JSON files containing data and matches foods we want to analyze with their nutrient counts and then manipulates the nutrient counts and calculates NRF scores, then uses these scores to create a data visualization
- perhaps_interest.py: A python script that goes through mulitple CSV files to figure out what foods a collection of households bought over the course of a year to see total consumption of specific nutrients 
- food_aps_mani.py: a python script that goes through multiple CSV files to figure out what foods a collection of households bought over and how much more it is than the daily value required for a balanced 2000 calorie diet 
- pyproject.toml: Congif file for pylint black
- requirements.txt: Required Packages
- .gitignore: file types and general files to be ignored in git commits
- .editorconfig: Configuration for a variety of editors and IDEs

## Usage

To use this repository, clone it to your local machine and run 'pip install requirements.txt' to download the required packages. Then (Esther insert here for csv). In order to obtain the data necessary to run this repository and get data visualizations you must get an API key from [https://fdc.nal.usda.gov/]. Instructions for obtaining this API Key are written in the README in the Data Source section below this section.

## Data Source

All data was obtained from [https://fdc.nal.usda.gov/].

In order to obtain the API Key for the data necessary to run this repository you must go to the U.S Department of Agriculture's website and request an API Key. Go to this link [https://fdc.nal.usda.gov/api-key-signup] and follow the brief instructions on the website. Upon doing this the USDA will send an email to you with your API key in it (your email is provided to them by you when you sign up to request an API Key).
Once you have your API key you must create a new file in your copy of this repository titled 'key.txt' and paste the API key into it. Save this file to your local machine, but do not publish it anywhere.

(Esther insert other data for csv here)

## Data Visualization

To get the data visualizations run the file called 'computational_essay.ipynb'


