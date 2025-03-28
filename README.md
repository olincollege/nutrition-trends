# Nutrition Trends Project Documentation README

This repository contains a notebook that analyzes nutrition trends through 3 different visualizations of data. One gotten by calculating the Nutrient Rich Food index (NRF) Score of the 10 most common foods in America, another by comparing the daily value of certain nutrients and the actual percentage of daily value.

## Setup

### General Requirements
You will need to get an API key from: https://fdc.nal.usda.gov/api-guide. 
You will also need internet connection to download from: https://www.ers.usda.gov/data-products/foodaps-national-household-food-acquisition-and-purchase-survey

## Repository Contents
- ```usda_api_data.py```: A python script which loads data into a JSON file 
- ```datamanipulation.py```: A python script which goes through the JSON files containing data and matches foods we want to analyze with their nutrient counts and then manipulates the nutrient counts and calculates NRF scores, then uses these scores to create a data visualization
- ```perhaps_interest.py```: A python script that goes through mulitple CSV files to figure out what foods a collection of households bought over the course of a year to see total consumption of specific nutrients 
- ```food_aps_mani.py```: a python script that goes through multiple CSV files to figure out what foods a collection of households bought over and how much more it is than the daily value required for a balanced 2000 calorie diet 
- ```pyproject.toml```: Congif file for pylint black
- ```requirements.txt```: Required Packages
- ```.gitignore```: file types and general files to be ignored in git commits
- ```.editorconfig```: Configuration for a variety of editors and IDEs

## Usage

To use this repository, clone it to your local machine and run 'pip install requirements.txt' to download the required packages.  In order to obtain the data necessary to run this repository and get data visualizations you must get an [API](https://fdc.nal.usda.gov/api-guide) key. Instructions for obtaining this API Key are written in the README in the Data Source section below this section. You must also download CSV files from the [USDA FoodAPS National Household Food Acquisition and Purchase Survey](https://www.ers.usda.gov/data-products/foodaps-national-household-food-acquisition-and-purchase-survey) website.

## Data Source

All data was obtained from the [USDA](https://fdc.nal.usda.gov/) website.

In order to obtain the API Key for the data necessary to run this repository you must go to the U.S Department of Agriculture's website and request an API Key. Go to this [link](https://fdc.nal.usda.gov/api-key-signup) and follow the brief instructions on the website. Upon doing this the USDA will send an email to you with your API key in it (your email is provided to them by you when you sign up to request an API Key).
Once you have your API key you must create a new file in your copy of this repository titled 'key.txt' and paste the API key into it. Save this file to your local machine, but do not publish it anywhere.

Next, go to the [USDA FoodAPS National Household Food Acquisition and Purchase Survey](https://www.ers.usda.gov/data-products/foodaps-national-household-food-acquisition-and-purchase-survey), scroll to the bottom and download the Public-Use Data Filesand Codebooks CSV.

## Running the Data Visulizations

To run the program, navigate to the directory where you cloned or downloaded the
repository and run the following commands in this order:

```bash
python usda_api_data.py
python food_aps_mani.py
python perhaps.interest.py
python computational_essay.ipynb
```

This will execute the program and show the three graphs relating to nutrient.

## Contributing

This project is an educational exercise, and contributions are not actively sought. However, feedback and suggestions are welcome.

## License

This project is provided for educational use only and is not licensed for commercial use.

## Contact

For any queries regarding this project, please reach out to the repository maintainer.
