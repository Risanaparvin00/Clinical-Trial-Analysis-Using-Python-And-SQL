# Clinical-Trial-Analysis-Using-Python-And-SQL
This project involves generating synthetic clinical trial data, loading it into an SQLite database, and performing SQL queries and Python visualizations to analyze key insights such as patient demographics, adverse events, and treatment efficacy.

1️⃣ Clone or Download the Repository

Since you uploaded the files manually, others can download them using:

Click on Code → Download, then extract the files.

OR, if using Git:

git clone https://github.com/Risanaparvin00/Clinical-Trial-Analysis-Using-Python-And-SQL.git
cd Clinical-Trial-Analysis


2️⃣ Install Required Libraries

Ensure you have Python installed, then install the required libraries:

pip install pandas numpy sqlalchemy matplotlib

3️⃣ Generate and Load Synthetic Data

Run the Python script to create and load data into SQLite:

https://github.com/Risanaparvin00/Clinical-Trial-Analysis-Using-Python-And-SQL/blob/main/Analsis.py

This will generate three CSV files and populate the SQLite database.

4️⃣ Run SQL Queries for Analysis

Open SQLite and connect to the database:

https://github.com/Risanaparvin00/Clinical-Trial-Analysis-Using-Python-And-SQL/blob/main/SQL%20code%20for%20drug%20reaction%20data%20loaded.txt

Run the SQL queries from queries.sql:

SELECT gender, COUNT(*) FROM patients GROUP BY gender;

5️⃣ Visualize Data with Python

📊 Key Insights & Findings

✅ Gender Distribution – Visualized using bar charts.
✅ Age Groups – Patients are categorized into different age groups.
✅ Adverse Events by Drug – Analyzed using SQL and stacked bar plots.
✅ Treatment Efficacy – Compared across different trial phases.

📌 Sample Graph: Gender Distribution



---

💡 Future Enhancements

Extend the dataset with more patient attributes (e.g., diagnosis, location).

Implement machine learning for predictive analysis on treatment outcomes.

Create a web-based dashboard for interactive visualizations.


---

🔗 Connect with Me

📌 Author: Risana Parvin CP
🔗 GitHub: https://github.com/Risanaparvin00
🔗 LinkedIn: https://www.linkedin.com/in/risana-parvin-cp
 
