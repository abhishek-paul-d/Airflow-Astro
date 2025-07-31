from airflow import DAG
from airflow.decorators import task
from datetime import datetime   

## Define the DAG

with DAG(
    dag_id='math_sequence_dag_with_taskflow',
    start_date=datetime(2024, 1, 1),
    schedule='@once',
    catchup=False
)as dag:
    
    ##TASK 1: Start with the initial number
    @task
    def start_number():
        initial_value=10
        print(f"Starting number:{initial_value}")
        return initial_value
    
    ##TASK 2: Add 5 to the number
    @task
    def add_five(number):
        new_value=number+5
        print(f"ADD 5: {number} + 5 = {new_value}")
        return new_value
    
    ##TASK 3 : Multiply by 2
    @task
    def multiply_by_two(number):
        new_value=number * 2
        print(f"MULTIPLY BY 2: {number} * 2 = {new_value}")
        return new_value
    
    ##TASK 4 :Subtract 3
    @task
    def subtract_three(number):
        new_value = number - 3
        print(f"SUBTRACT 3: {number} - 3 = {new_value}")
        return new_value
    
    ##TASK 5: Square the number
    @task
    def square_number(number):
        new_value = number ** 2
        print(f"SQUARE: {number}^2 = {new_value}")
        return new_value
    
    ## Set Task Dependencies
    start_value=start_number()
    added_value=add_five(start_value)
    multiplied_value=multiply_by_two(added_value)
    subrated_value=subtract_three(multiplied_value)
    squared_value=square_number(subrated_value)




 

    

    