import pendulum
import logging

from airflow.decorators import dag, task

@dag(
    schedule_interval='@hourly',
    start_date=pendulum.now()
)
def task_dependencies():

    @task()
    def hello_world():
        logging.info("Hello World")

    @task()
    def addition(first,second):
        logging.info(f"{first} + {second} = {first+second}")
        return first+second

    @task()
    def subtraction(first,second):
        logging.info(f"{first -second} = {first-second}")
        return first-second

    @task()
    def division(first,second):
        logging.info(f"{first} / {second} = {int(first/second)}")   
        return int(first/second)     

# TODO: call the hello world task function
    hello_world_result = hello_world()
# TODO: call the addition function with some constants (numbers)
    addition_result = addition(5, 10)
# TODO: call the subtraction function with some constants (numbers)
    subtraction_result = subtraction(10,5)
# TODO: call the division function with some constants (numbers)
    division_result = division(10,5)
# TODO: create the dependency graph for the first three tasks
    hello_world_result >> addition_result >> division_result
# TODO: Configure the task dependencies such that the graph looks like the following:
#
#                    ->  addition_result
#                   /                 \
#   hello_world_result                   -> division_result
#                   \                 /
#                    ->subtraction_result

    # Definir las dependencias
    hello_world_result >> addition_result
    hello_world_result >> subtraction_result
    addition_result >> division_result
    subtraction_result >> division_result


#  TODO: assign the result of the addition function to a variable
   #addition_var = addition_result
#  TODO: assign the result of the subtraction function to a variable
   # subtraction_var = subtraction_result.output
#  TODO: pass the result of the addition function, and the subtraction functions to the division function
    division_result_2 = division(addition_result, subtraction_result)
# TODO: create the dependency graph for the last three tasks
    last_three_tasks_graph = (hello_world_result, addition_result, subtraction_result, division_result_2)


task_dependencies_dag=task_dependencies()