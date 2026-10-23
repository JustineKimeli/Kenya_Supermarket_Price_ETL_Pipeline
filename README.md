# Kenya Supermarket Price ETL Pipeline
## Overview

This project implements an Object-Oriented Programming (OOP) based ETL (Extract, Transform, Load) pipeline that processes supermarket price data from Naivas and Carrefour in Kenya and loads it into a PostgreSQL database.

The project demonstrates how to work with multiple data sources, transform data into a consistent format, and store the results in a relational database using Python, SQLAlchemy, and Psycopg.

# Objectives
- Extract supermarket price data from CSV and JSON files.
- Transform the extracted data into a consistent structure.
- Load the processed records into PostgreSQL.
- Use OOP principles to organize the ETL pipeline.
- Verify and query the loaded data using DBeaver.

**Technologies Used**

- Python — ETL implementation.
- Pandas — Data manipulation and transformation, if used in the implementation.
- SQLAlchemy — Database connectivity and data loading.
- Psycopg 3 — PostgreSQL database driver.
- PostgreSQL — Relational database for storing supermarket prices.
- DBeaver — Database management and SQL query tool.
- CSV and JSON — Input data formats.

# Project Structure
```
OOP/
├── data/
│   ├── kenya_supermarket_prices.csv
│   └── kenya_supermarket_prices.json
├── src/
│   └── oop/
│       └── data_loader.py
├── .venv/
└── README.md
```

The structure above represents the main files used in the project. Additional configuration files, modules, and tests may be added as the project grows.

# ETL Pipeline

The pipeline consists of three main stages.

**1. Extract**

The pipeline reads data from two sources:

Naivas: Extracts supermarket price data from kenya_supermarket_prices.csv.
Carrefour: Extracts supermarket price data from kenya_supermarket_prices.json.

**2. Transform**

The extracted data is processed before loading. This stage can include cleaning values, standardizing column names, converting data types, and preparing records for database insertion.

**3. Load**

SQLAlchemy connects to PostgreSQL using the Psycopg driver and loads the transformed records into the database.

Each pipeline reports its progress and confirms when the database transaction has been committed successfully.

# Installation and Setup
## Prerequisites
- Python 3
- PostgreSQL
- DBeaver


**Successful Execution**

The pipeline has successfully processed both data sources, with 630 records reported for each source.

Example terminal output:

```
Starting Pipeline Naivas
[Naivas] Extracting CSV from D:\OOP\data\kenya_supermarket_prices.csv
[Naivas] Transforming data...
[Naivas] Connecting to Postgres and loading 630 records...
[Naivas] Successfully committed records to PostgreSQL

Starting Pipeline Carrefour
[Carrefour] Extracting JSON from D:\OOP\data\kenya_supermarket_prices.json
[Carrefour] Transforming data...
[Carrefour] Connecting to Postgres and loading 630 records...
[Carrefour] Successfully committed records to PostgreSQL
```

These messages indicate that both pipelines completed their database commit operations. The final record counts should also be verified directly in PostgreSQL.

## Verifying Data in DBeaver 

Connect DBeaver to the same PostgreSQL database configured in the Python application.

The target table used in this project is referenced as public."Supermarket_prices".

**View records**
SELECT *
FROM public."Supermarket_prices";


**Count all records**
SELECT COUNT(*) AS total_records
FROM public."Supermarket_prices";

This project demonstrates practical application of:

- Object-Oriented Programming in Python.
- ETL pipeline design.
- Working with CSV and JSON data.
- Relational database integration.
- SQLAlchemy and PostgreSQL connectivity.
- SQL querying and data verification using DBeaver.
