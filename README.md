# 📚 Book Data Scraping and Database Pipeline
**`Web Scraping | Data Engineering | SQLite | ML Data Collection`**

A production-oriented web scraping project built to extract structured **book-related data** from an online bookstore and store it in both a **SQLite database** and **CSV format** for future Machine Learning applications.

This project focuses on an important but often overlooked step in AI/ML workflows — **data collection**.

Instead of relying on already cleaned datasets from Kaggle or public repositories, this project demonstrates how structured datasets can be collected directly from websites and transformed into a format ready for analysis and Machine Learning models.

---

## ⚡ Project Overview

In real-world Machine Learning systems, data is rarely available in a clean and ready-to-use format.

Most datasets need to be:

- Collected
- Structured
- Cleaned
- Stored

before any meaningful analysis or model building can begin.

This project automates that process by scraping structured **book information** from an online bookstore and storing the extracted data in:

### 🗄️ SQLite Database
```text
books_data.db
```

### 📄 CSV Dataset
```text
books_data.csv
```

The exported CSV dataset can later be used in **Machine Learning workflows** such as:

- Book Recommendation Systems
- Price Prediction Models
- Rating Prediction
- NLP-based Description Analysis
- Classification & Regression Models

The project emphasizes:

✅ Automated Data Collection  
✅ Structured Database Storage  
✅ CSV Export for ML Projects  
✅ Production-Oriented Logging  
✅ Error Handling & Fault Tolerance  
✅ Reusable Data Pipeline

---

## 🎯 Objective

The main objective of this project is to automate the collection of structured book information from a website and convert it into a format that can be reused in future projects.

Instead of manually collecting data, the scraper automatically extracts:

- Book Title
- Price
- Rating
- Availability Status
- Product Description
- Product URL

The collected data is then stored in both:

- **SQLite Database**
- **CSV format for future Machine Learning projects**

This makes the data easy to reuse for analysis, feature engineering, and model training.

---

## 🧠 Project Architecture

This project follows a structured scraping workflow where data extraction, parsing, database storage, and CSV conversion are handled systematically.

### 🔹 `main.py`

Handles:

- Multi-page scraping
- Website crawling
- HTML parsing using BeautifulSoup
- Relative URL handling
- Missing value handling
- Database insertion using SQLAlchemy ORM
- Logging warnings and errors
- CSV export

### 🔹 `check.py`

Handles:

- Database inspection
- Viewing stored data
- Quick validation of scraped records

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-Web_Scraping-green)
![Requests](https://img.shields.io/badge/Requests-HTTP_Client-red)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-orange)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Processing-150458?logo=pandas)
![Logging](https://img.shields.io/badge/Logging-Production_Ready-lightgrey)

---

## 📊 Dataset Overview

The scraper collects approximately **980+ books** and stores the extracted information in both database and CSV formats.

### Extracted Features

| Feature | Description |
|----------|-------------|
| `id` | Unique book identifier |
| `title` | Book title |
| `price` | Book price |
| `rating` | Customer rating (1–5) |
| `availability` | Stock availability |
| `description` | Book summary/description |
| `url` | Product page URL |

---

## 🗄️ Database Design

The scraped data is stored in a **SQLite database** using **SQLAlchemy ORM**.

### Table: `Books`

| Column | Type |
|---------|------|
| `id` | Integer |
| `title` | String |
| `price` | Float |
| `rating` | Integer |
| `availability` | String |
| `description` | String |
| `url` | String |

Example SQL query:

```sql
SELECT * FROM Books
LIMIT 5;
```

The database allows easy querying and structured storage for future use.

---

## 🤖 Machine Learning Readiness

This project was designed to support **future Machine Learning workflows**.

The scraped data is automatically exported into:

```text
books_data.csv
```

so it can be directly reused in ML projects without needing to scrape data again.

Possible future ML use cases include:

- Recommendation Systems
- Price Prediction Models
- Rating Prediction
- NLP on Book Descriptions
- Customer Preference Analysis

This makes the project more than just a scraper — it acts as a **data collection pipeline for future AI/ML systems**.

---

## 📂 Project Structure

```bash
Book-webscrapper/
│── Data/
│   ├── books_data.csv
│   └── books_data.db
│
│── check.py
│── main.py
│── requirements.txt
│── scraper.log
│── README.md
```

---

## 🚀 Installation & Usage

### 1️⃣ Clone Repository

```bash
git clone https://github.com/NaramCharan/Book-webscrapper.git
```

### 2️⃣ Navigate Into Project

```bash
cd Book-webscrapper
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Scraper

Execute:

```bash
python main.py
```

The workflow includes:

- Multi-page website scraping
- Structured data extraction
- Missing value handling
- SQLite database storage
- CSV export for ML workflows
- Logging and monitoring

---

## 📝 Logging System

The project includes a logging system to make debugging and monitoring easier.

The logger tracks:

- Missing book descriptions
- Database insertion progress
- Duplicate records
- Unexpected scraping errors

Example log:

```text
INFO One page is added into the database
WARNING Missing description for book
```

This helps make the scraper more reliable and closer to real-world engineering practices.

---

## 🔮 Future Improvements

Planned enhancements:

- [ ] Multi-threaded scraping for faster execution
- [ ] Async scraping support
- [ ] PostgreSQL/MySQL database integration
- [ ] Data validation pipeline
- [ ] Automated ML dataset preparation
- [ ] FastAPI integration for serving scraped data

---

## 📬 Contact

### 👨‍💻 Naram Charan

**LinkedIn:**  
https://www.linkedin.com/in/naramcharan/

**Email:**  
charannaram1710@gmail.com

---

## ⭐ Support

If you found this project useful, consider giving it a **star** on GitHub!
