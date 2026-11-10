# E-Commerce Analytics Pipeline

**Author:** Babatunde Oyedele
**GitHub:** [Babsace](https://github.com/Babsace)

## 📌 Project Overview
This project is an end-to-end data engineering pipeline for an e-commerce platform. It covers synthetic data generation, NoSQL storage (MongoDB and HBase), distributed processing (Apache Spark), and integrated funnel analysis, culminating in data visualizations.

## 📂 Repository Structure
- `data/`: Contains the generated JSON and Parquet files.
- `mongodb/`: Python scripts for loading data and running aggregations in MongoDB.
- `hbase/`: Schema definitions and Python scripts for HBase.
- `spark/`: PySpark scripts for data cleaning, recommendations, and SQL analytics.
- `integration/`: Spark script for the integrated e-commerce funnel analysis.
- `visualizations/`: Python scripts and generated PNG charts.
- `report/`: The final technical report (Markdown and PDF).
- `dataset_generator_fixed.py`: The Python script used to generate the synthetic dataset.

## 🚀 How to Run
1. Ensure Docker is running and start the MongoDB and HBase containers (see `report/technical_report.pdf` for exact commands).
2. Activate the Python virtual environment.
3. Run the scripts in the following order:
   - `python mongodb/load_and_index.py`
   - `python mongodb/aggregations.py`
   - `python spark/clean_data.py`
   - `python spark/recs.py`
   - `python integration/funnel.py`
   - `python visualizations/make_charts.py`

## 📊 Results
All results, including charts and SQL outputs, are documented in the `report/technical_report.pdf`.
