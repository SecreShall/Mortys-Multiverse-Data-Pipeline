# 🚀 Morty's Multiverse Data Pipeline

Welcome to **Morty's Multiverse Data Pipeline**! This project is a Python-powered data extraction and transformation pipeline that interacts with the Rick and Morty API to collect and process character and location data. 🛸

## 📌 Project Overview

This pipeline retrieves and stores structured data from the Rick and Morty API, helping to analyze character appearances and origin locations. It extracts:

- **🦸 Character Table**: Tracks the number of appearances per episode for each character.
- **🌍 Location Table**: Stores metadata for each location, including type, dimension, resident count, and references characters' origin and last known locations.


## ✨ Features

- ✅ Automated retrieval of Rick and Morty character and location data.
- ✅ Extraction of character origin, last known location, and episode appearances.
- ✅ Storage of structured data into a MySQL database for analysis.
- ✅ Scalable and efficient processing using Python.

## 🛠 Technologies Used

- 🐍 **Python** (Data processing & API interaction)
- 🗄 **MySQL** (Database storage & querying)
- 🔗 **Requests** (For making API calls)
- 📊 **Pandas** (Data transformation)
- 🌍 **Rick and Morty API** (Data source)

## 📂 Database Schema

```sql
CREATE TABLE characters (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    status VARCHAR(50),
    species VARCHAR(100),
    type VARCHAR(100),
    gender VARCHAR(50),
    origin_id INT,
    location_id INT,
    episode_count INT,
    FOREIGN KEY (origin_id) REFERENCES locations(id),
    FOREIGN KEY (location_id) REFERENCES locations(id)
);

CREATE TABLE locations (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(100),
    dimension VARCHAR(100),
    residents INT
);
```

## 📁 Data Files

During the pipeline's execution, data is collected, transformed, and stored in structured CSV files. Below is a breakdown of each dataset and its transformation process:

### Extracted Data  
These files contain raw data retrieved directly from the Rick and Morty API:

- 📍 `extracted_location_data.csv` - Raw location metadata, including ID, name, type, dimension, and resident count.
- 🦸 `extracted_character_data.csv` - Initial character records with details such as ID, name, status, species, origin, and episode appearances.

### Transformed Data  
The transformed files hold cleaned and structured data, ready for database ingestion:

- 🌍 `transformed_location_data.csv`  
  - Reads `extracted_location_data.csv`.  
  - Fills missing values in `type` and `dimension` columns with `"unknown"`.  
  - Saves the cleaned data for efficient querying.  

- 🎭 `transformed_character_data.csv`  
  - Reads `extracted_character_data.csv`.  
  - Fills missing values in `type` column with `"unknown"`.  
  - Extracts `origin` and `location` IDs from URL strings, filling missing values with `0`.  
  - Removes duplicate entries based on key attributes (`name`, `status`, `species`, etc.).  
  - Resets character IDs sequentially to remove gaps.  
  - Saves the processed data for structured analysis.  

These transformations ensure that the dataset remains consistent, well-structured, and ready for MySQL storage. 🚀  



---

## 👤 Author
Developed by **Cley**  
📧 Contact: 02clintaudrey@gmail.com 
🌐 GitHub: SecreShall

---
