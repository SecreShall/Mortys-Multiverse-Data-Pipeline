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
- ⚙️ **SQLAlchemy** (Database connection & management)
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
    episode_count INT,
    origin_id INT,
    location_id INT,
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

---

## 👤 Author
Developed by **Cley**  
📧 Contact: 02clintaudrey@gmail.com 
🌐 GitHub: SecreShall

---
