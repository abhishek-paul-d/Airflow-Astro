from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

## define our task
def preprocess_data():
    print("Preprocessing data...")

## define our task 2
def train_model():
    print("Training model ...")

## define our task 3
def evaluate_model():
    print("Evaluating model...")

## define the DAG
with DAG('ml_pipeline',
         start_date=datetime(2025,1,1),
         schedule='@weekly' 
) as dag: 
    
    ##Define the task
    preprocess=PythonOperator(task_id="preprocess_task",python_callable=preprocess_data)
    train=PythonOperator(task_id="train_task",python_callable=train_model)
    evaluate=PythonOperator(task_id="evaluate_task",python_callable=evaluate_model)

    ##Set Dependencies
    preprocess >> train >> evaluate
    