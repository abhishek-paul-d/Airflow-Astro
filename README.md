# Airflow Project Documentation

## What is Apache Airflow?
Apache Airflow is a platform used to programmatically author, schedule, and monitor workflows. It is primarily used for automating and managing ETL (Extract, Transform, Load) processes, data pipelines, and other complex workflows. Airflow uses a Python-based syntax for defining tasks and dependencies, making it highly customizable and extensible.

### Key Features of Airflow:
- **Declarative Workflow Definition**: Workflows are defined as code using Python.
- **Task Dependencies**: Tasks can be dependent on previous tasks, creating a directed acyclic graph (DAG).
- **Scheduling**: DAGs can be scheduled to run at specific intervals.
- **Extensive Integration**: Supports integration with various systems like databases, cloud services, and messaging queues.
- **User Interface**: Provides a web interface to monitor and manage workflows.
- **TaskFlow API**: Modern syntax for defining tasks and workflows using Python decorators.

---

## Project Overview

This project contains several Airflow DAGs (Directed Acyclic Graphs) that demonstrate different aspects of workflow automation. Below is a detailed explanation of each DAG file in the project.

---

## 1. Taskflow API Example (taskflowapi.py)

### File Introduction
This DAG demonstrates the use of Airflow's modern TaskFlow API to implement a mathematical sequence. It shows how to define tasks using Python functions and connect them using dependencies.

### DAG Steps:
1. **Start Number**: Initializes the process with a starting value of 10.
2. **Add Five**: Adds 5 to the number.
3. **Multiply by Two**: Multiplies the result by 2.
4. **Subtract Three**: Subtracts 3 from the result.
5. **Square Number**: Squares the final value.

This DAG runs once and uses the TaskFlow decorator syntax for defining tasks and dependencies.

---

## 2. Example DAG (exampledag.py)

### File Introduction
This is a simple example DAG that demonstrates the basic structure of an Airflow workflow. It includes two tasks:
1. **Start Task**: Prints a message indicating the start of the DAG.
2. **End Task**: Prints a message indicating the completion of the DAG.

The DAG runs once and serves as a template for understanding the fundamental structure of Airflow DAGs.

---

## 3. Machine Learning Pipeline (mlpipeline.py)

### File Introduction
This DAG represents a basic machine learning pipeline with the following steps:
1. **Preprocess Data**: Handles data cleaning and preparation.
2. **Train Model**: Trains a machine learning model using the preprocessed data.
3. **Evaluate Model**: Evaluates the performance of the trained model.

The DAG is scheduled to run weekly and demonstrates how Airflow can be used to automate machine learning workflows.

---

## Project Structure
```
dags/
├── .airflowignore
├── exampledag.py
├── maths_operation.py
├── mlpipeline.py
├── taskflowapi.py
└── __pycache__
```

---

## Running the Project Locally
1. Start Airflow using:
```bash
astro dev start
```

2. Access the Airflow UI at:
```text
http://localhost:8080
```

3. Access the Postgres database at:
```text
localhost:5432/postgres
```
with username and password both set to "postgres".
