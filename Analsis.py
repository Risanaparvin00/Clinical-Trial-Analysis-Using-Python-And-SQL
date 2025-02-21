import pandas as pd 
import numpy as np
from sqlalchemy import create_engine
np.random.seed(42)
n=100 #No of Patients
patient_id=range(1,n+1)#Patients ID
age=np.random.randint(18,80,size=n) #age of patients
gender=np.random.choice(['Male','Female'],size=n,p=[0.5,0.5])#gender of patients
treatment_id=np.random.randint(1,5,size=n)#treatment ID of Patients
adverse_event_id=range(1,n+1)#adverse event data
drug_names=np.random.choice(['Drug A','Drug B','Drug C','Drug D'],size=n)
event_types=np.random.choice(['Nausea','Headache','Dizziness','Fatigue'],size=n)
severity=np.random.randint(1,5,size=n)

treatment_data={"treatment_id":[1,2,3,4],"drug_names":['Drug A','Drug B','Drug C','Drug D'],"efficacy":[0.75,0.65,0.85,0.70],"phase":[1,2,3,4]}

patient_df=pd.DataFrame({"patient_id":patient_id,"age":age,"gender":gender,"treatment_id":treatment_id})
adverse_event_df=pd.DataFrame({"event_id":adverse_event_id,"drug_name":drug_names,"event_type":event_types,"severity":severity})
treatment_df=pd.DataFrame(treatment_data)
treatment_df['phase']=pd.to_numeric(treatment_df['phase'])
treatment_df=treatment_df.dropna(subset=['efficacy'])
patient_df.to_csv('patient.csv',index=False)
adverse_event_df.to_csv('adverse_event.csv',index=False)
treatment_df.to_csv('treatment.csv',index=False)

engine=create_engine('sqlite:///ClinicalTrialsDB.db')

patient_df.to_sql('patient',engine,if_exists='replace',index=False)
adverse_event_df.to_sql('adverse_event',engine,if_exists='replace',index=False)
treatment_df.to_sql('treatment',engine,if_exists='replace',index=False)

print("Data created and loaded to sql")
import sqlite3
conn=sqlite3.connect("ClinicalTrialsDB.db")
cursor=conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables=cursor.fetchall()
print(tables)
conn.close()


#visualization
#gender distribution
import matplotlib.pyplot as plt
gender_counts= patient_df['gender'].value_counts()
gender_counts.plot(kind='bar',color=['skyblue','salmon'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


#age distribution
agegroups=pd.cut(patient_df['age'],bins=[0,30,60,80],labels=['Under 30','30-60','60+'])
agegroups.value_counts().plot(kind='bar',color='lightgreen')
plt.title('Age distribution')
plt.xlabel('Age Group')
plt.ylabel('Count')
plt.show()


#adverse events by drug
eventcounts=adverse_event_df.groupby(['drug_name','event_type']).size().unstack()
eventcounts.plot(kind='bar',stacked=True,figsize=(10,6),colormap='viridis')
plt.title('Adverse events by drug')
plt.xlabel('Drug Name')
plt.ylabel('Count of events')
plt.legend(title='Event Type', bbox_to_anchor=(1.05,1))
plt.show()


#Average Efficacy by trial phase
efficacybyphase=treatment_df.groupby('phase')['efficacy'].mean().sort_index()
plt.figure(figsize=(8,5))
efficacybyphase.plot(kind='bar',color='orange')
plt.title('Average Efficacy by Trial Phase')
plt.xlabel('Trial Phase')
plt.ylabel('Average Efficacy')
plt.show()
