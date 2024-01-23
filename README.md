# 4-Automate-Data-Pipelines
1. [Instalar Airflow con docker](#schema1)
2. [Inicializar la base de datos y ejecutar airflow](#schema2)
3. [Coniciendo el código del primer DAG](#schema3)
4. [Utilizando Docker para ejecutar Apache Airflow](#schema4)

5. [Ref](#schemaref)
<hr>
<a name='schema1'></a>

## 1. Instalar Airflow con docker

- Crear un directorio para el proyecto
- Ir a [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
  - Navegar hasta el punto `Fetching docker-compose.yaml` y ejecutar en un terminal.
  ```
    curl -LfO 'https://airflow.apache.org/docs/apache-airflow/2.8.0/docker-compose.yaml'
  ```
  Y nos crea el archivo `docker-compose.yaml`
- Crear las carpetas necesarias para la ejecuación de Airflow
```
mkdir -p ./dags ./logs ./plugins ./config
```
-  Crear un archivo de entrono
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

<hr>
<a name='schema2'></a>

## 2. Inicializar la base de datos y ejecutar airflow
- Inicializar la base de datos
```
docker-compose up airflow-init
```
- Ejecutar airflow
```
docker-compose up -d
```
- Vamos al localhost http://localhost:8080/home

![login](./img/login.png)

Tanto para el usuario y contraseña poner, airflow

<hr>
<a name='schema3'></a>

## 3. Coniciendo el código del primer DAG

- Importaciones:

```python
import logging
import pendulum
from airflow.decorators import dag, task
```

Se importan los módulos y funciones necesarios de Airflow, así como el módulo pendulum para manejar fechas y 
horas de manera más fácil.


- Decorador del DAG:

```python
@dag(
    start_date=pendulum.now()
)
def greet_flow_dag():
```

Se utiliza el decorador `@dag` para definir un DAG llamado `greet_flow_dag`. 
El parámetro `start_date` se establece en la fecha y hora actual mediante `pendulum.now()`. 
Esto indica cuándo comenzará a ejecutarse el DAG.

- Tarea del DAG (hello_world_task):

```python
    @task
    def hello_world_task():
        logging.info("Hello World!")
```

Se define una tarea llamada hello_world_task utilizando el decorador `@task`. 
Esta tarea simplemente imprime "Hello World!" en los registros de Airflow cuando se ejecuta.


- Invocación de la tarea (hello_world):

```python
 hello_world = hello_world_task()
```
   
Se invoca la tarea `hello_world_task` y se almacena en la variable `hello_world`. 
Esta línea no ejecuta la tarea de inmediato; simplemente crea una instancia de la tarea.

- Invocación del DAG (greet_dag):
```python
greet_dag = greet_flow_dag()
```

Se invoca el DAG `greet_flow_dag` y se almacena en la variable `greet_dag`. 
Al igual que con la tarea, esto no inicia la ejecución del DAG; simplemente crea una instancia del DAG.

<hr>
<a name='schema4'></a>

## 4. Utilizando Docker para ejecutar Apache Airflow

Si estás utilizando Docker para ejecutar Apache Airflow, es posible que necesites ejecutar los comandos dentro 
del contenedor de Docker. Aquí hay una guía paso a paso para ejecutar comandos de Airflow en un contenedor Docker:

- Inicia el contenedor de Docker:

Asegúrate de que tu contenedor de Apache Airflow esté en ejecución. Puedes usar el comando `docker ps` para 
verificar si está activo.

- Ejecuta comandos dentro del contenedor:

Utiliza el comando docker exec para ejecutar comandos dentro del contenedor de Airflow. La estructura general sería:

```bash
docker exec -it nombre_del_contenedor_airflow comando_airflow
```
Donde:

`nombre_del_contenedor_airflow` es el nombre o el ID del contenedor de Airflow.
`comando_airflow` es el comando específico de Airflow que deseas ejecutar.



<hr>
<a name='schemaref'></a>

## 5. Ref:

https://www.youtube.com/watch?v=-kdgCWs86zohttps://www.youtube.com/watch?v=-kdgCWs86zo

https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html

https://airflow.apache.org/docs/apache-airflow/stable/templates-ref.html