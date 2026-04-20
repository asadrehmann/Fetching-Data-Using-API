# Fetching Data Using API
#  Movie Data Engineering Project using TMDB API

##  Project Overview

In this project, we developed a data engineering pipeline to collect and process movie data from the TMDB (The Movie Database) API using Python. The project focuses on real-world data acquisition, preprocessing, and code standardization using industry practices.

---

##  Objectives

* Fetch real-time movie data using an API
* Understand JSON data structure
* Perform data preprocessing and cleaning
* Apply coding standards and best practices
* Organize the project using professional folder structure

---

##  Tools & Technologies

* Python
* Jupyter Notebook
* pandas
* requests
* Flake8 (code linting)
* Black (code formatting)
* TMDB API

---

##  Project Workflow

###  Understanding APIs

We began by understanding how APIs work and how they allow communication between a client and a server. We explored how APIs return structured data in JSON format.

---

###  Environment Setup

We installed required libraries such as:

* pandas for data manipulation
* requests for API calls

We used Jupyter Notebook for development and testing.

---

###  API Key Generation

We created an account on TMDB and generated an API key, which is required to authenticate requests and access movie data.

---

###  Data Fetching (API Integration)

Using Python, we sent HTTP requests to the TMDB API to fetch movie-related data. The request included:

* API key
* endpoint URL
* query parameters

The API returned raw movie data in JSON format.

---

###  Handling API Response

We validated the response using status codes (e.g., 200 for success) and converted the response into JSON format:

```python
data = response.json()
```

---

###  Data Preprocessing (Team Contribution)

After fetching the raw data:

* The dataset was cleaned and structured
* Relevant features were extracted
* Missing or unnecessary fields were handled

This step was performed collaboratively by team members to prepare the dataset for analysis.

---

###  Code Quality and Formatting

To follow industry standards, we improved code quality using:

* **Flake8** → for identifying syntax errors and style issues
* **Black** → for automatic code formatting

This ensured that the code is clean, readable, and consistent.

---

###  Project Structure (Best Practices)

We organized the project using a professional folder structure, separating:

* data fetching scripts
* preprocessing modules
* notebooks
* output files

This improves maintainability and scalability of the project.

---

###  Data Storage

The processed data was stored in a structured format (e.g., CSV file) for further use in analysis or machine learning tasks.

---

## 📊 Outcome

At the end of this project, we successfully:

* Integrated an external API with Python
* Retrieved real-world movie data
* Cleaned and structured the dataset
* Applied professional coding standards
* Organized the project using best practices

---

##  Team Contribution

This project was completed as a group effort:

* One member handled API integration and data fetching
* Two members focused on data preprocessing and cleaning
* The team collaboratively ensured code quality and structure

---


---

## 📎 Conclusion

This project provided hands-on experience with real-world data engineering workflows. It strengthened our understanding of API integration, data preprocessing, and writing clean, maintainable code following industry standards.
