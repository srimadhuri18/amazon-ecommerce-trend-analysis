# Trend Analysis on Amazon E-Commerce Sales Dataset

## Project Overview

This project performs large-scale trend analysis on an Amazon e-commerce sales dataset using Python and Apache Spark. The goal of the project is to extract meaningful insights from transactional sales data by identifying patterns in product demand, regional performance, and sales trends over time.

The project demonstrates a scalable data processing workflow that includes data ingestion, preprocessing, distributed analytics, and visualization.

This project was developed as part of a Big Data and Data Analytics learning initiative and showcases practical skills in data engineering, data analysis, and distributed computing.

---

## Objectives

The main objectives of this project are:

* Analyze large sales datasets efficiently using Apache Spark
* Identify sales trends over time
* Determine top performing products
* Analyze regional sales performance
* Visualize insights for better interpretation
* Demonstrate a scalable data analysis pipeline

---

## Technologies Used

* Python
* Apache Spark (PySpark)
* Pandas
* Matplotlib
* Jupyter Notebook
* Git & GitHub

---

## Project Architecture

The project follows a modular data processing pipeline.

```
Dataset
   ↓
Data Loading (Spark)
   ↓
Data Cleaning & Preprocessing
   ↓
Trend Analysis
   ↓
Data Visualization
   ↓
Insights & Results
```

---

## Project Structure

```
Trend_analysis_on_amazon_e-commerce_dataset
│
├── Data
│   └── amazon-e-commerce-sales-dataset.ipynb
│
├── notebook
│   └── analysis.ipynb
│
├── Result
│   └── sales_trend.png
│
├── src
│   ├── data_loader.py
│   ├── data_cleaning.py
│   ├── trend_analysis.py
│   └── visualization.py
│
├── requirements.txt
└── run_project.py
```

### Folder Description

**Data/**
Contains the raw dataset or source notebook used to generate the dataset.

**notebook/**
Contains exploratory data analysis performed using Jupyter Notebook.

**Result/**
Stores output graphs and generated visualizations.

**src/**
Contains modular Python scripts for the data processing pipeline.

**run_project.py**
Main execution file that runs the entire workflow.

**requirements.txt**
List of Python dependencies required to run the project.

---

## Dataset Description

The dataset contains Amazon e-commerce sales records including fields such as:

* Order Date
* Product Name
* Category
* Sales
* Quantity
* Region

The dataset represents transactional sales data and enables analysis of product demand patterns and regional market performance.

---

## Key Features

### 1. Data Loading

The dataset is loaded using Apache Spark to enable efficient handling of large datasets.

### 2. Data Cleaning

Data preprocessing steps include:

* Removing null values
* Filtering invalid or negative records
* Ensuring data consistency

### 3. Trend Analysis

The project extracts several insights:

**Sales Trend Over Time**
Analyzes how sales change across different time periods.

**Top Performing Products**
Identifies products with the highest total sales.

**Regional Sales Analysis**
Determines which regions generate the highest revenue.

### 4. Data Visualization

Sales trends are visualized using Matplotlib to highlight patterns and insights in the data.

---

## Installation

Clone the repository:

```
git clone https://github.com/srimadhuri18/amazon-ecommerce-trend-analysis.git
```

Navigate to the project folder:

```
cd amazon-ecommerce-trend-analysis
```

Install required dependencies:

```
pip install -r requirements.txt
```

---

## Running the Project

Execute the main script:

```
python run_project.py
```

The script will:

1. Load the dataset
2. Clean and preprocess data
3. Perform trend analysis
4. Display key insights
5. Generate visualizations

The output visualization will be saved inside the **Result** folder.

---

## Example Output

The project generates insights such as:

* Sales trends over time
* Top selling products
* Regional sales performance

Example output visualization:

```
Result/sales_trend.png
```

---

## Skills Demonstrated

This project demonstrates practical experience in:

* Big Data Processing
* Distributed Data Analysis
* Apache Spark
* Data Cleaning and Preprocessing
* Data Visualization
* Python Programming
* Modular Project Design

---

## Future Improvements

Potential improvements to extend this project:

* Real-time data processing using streaming frameworks
* Machine learning models for sales prediction
* Interactive dashboards using Streamlit or Bokeh
* Deployment on cloud platforms such as AWS or GCP

---





This project is open source and available for educational and research purposes.
