# Source: https://airflow.apache.org/docs/apache-airflow/stable/index.html

Title: What is Airflow®? — Airflow 3.1.7 Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow/stable/index.html

Markdown Content:
[Apache Airflow®](https://github.com/apache/airflow) is an open-source platform for developing, scheduling, and monitoring batch-oriented workflows. Airflow’s extensible Python framework enables you to build workflows connecting with virtually any technology. A web-based UI helps you visualize, manage, and debug your workflows. You can run Airflow in a variety of configurations — from a single process on your laptop to a distributed system capable of handling massive workloads.

Workflows as code[](https://airflow.apache.org/docs/apache-airflow/stable/index.html#workflows-as-code "Link to this heading")
------------------------------------------------------------------------------------------------------------------------------

Airflow workflows are defined entirely in Python. This “workflows as code” approach brings several advantages:

*   **Dynamic**: Pipelines are defined in code, enabling dynamic Dag generation and parameterization.

*   **Extensible**: The Airflow framework includes a wide range of built-in operators and can be extended to fit your needs.

*   **Flexible**: Airflow leverages the [Jinja](https://jinja.palletsprojects.com/) templating engine, allowing rich customizations.

Task SDK[](https://airflow.apache.org/docs/apache-airflow/stable/index.html#task-sdk "Link to this heading")
------------------------------------------------------------------------------------------------------------

For Airflow Task SDK, see the standalone reference & tutorial site:

[Apache Airflow Task SDK](https://airflow.apache.org/docs/task-sdk/stable/index.html "(in Apache Airflow Task SDK v1.2.0)")

Dags[](https://airflow.apache.org/docs/apache-airflow/stable/index.html#dags "Link to this heading")
----------------------------------------------------------------------------------------------------

A Dag is a model that encapsulates everything needed to execute a workflow. Some Dag attributes include the following:

*   **Schedule**: When the workflow should run.

*   **Tasks**: [tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) are discrete units of work that are run on workers.

*   **Task Dependencies**: The order and conditions under which [tasks](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/tasks.html) execute.

*   **Callbacks**: Actions to take when the entire workflow completes.

*   **Additional Parameters**: And many other operational details.

Let’s look at a code snippet that defines a simple Dag:

from datetime import datetime

from airflow.sdk import DAG, task
from airflow.providers.standard.operators.bash import BashOperator

# A Dag represents a workflow, a collection of tasks
with DAG(dag_id="demo", start_date=datetime(2022, 1, 1), schedule="0 0 * * *") as dag:
    # Tasks are represented as operators
    hello = BashOperator(task_id="hello", bash_command="echo hello")

    @task()
    def airflow():
        print("airflow")

    # Set dependencies between tasks
    hello >> airflow()

Here you see:

*   A Dag named `"demo"`, scheduled to run daily starting on January 1st, 2022. A Dag is how Airflow represents a workflow.

*   Two tasks: One using a `BashOperator` to run a shell script, and another using the `@task` decorator to define a Python function.

*   The `>>` operator defines a dependency between the two tasks and controls execution order.

Airflow parses the script, schedules the tasks, and executes them in the defined order. The status of the `"demo"` Dag is displayed in the web interface:

![Image 1: Demo Dag in the Graph View, showing the status of one Dag run along with Dag code.](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_graph_and_code_view.png)
This example uses a simple Bash command and Python function, but Airflow tasks can run virtually any code. You might use tasks to run a Spark job, move files between storage buckets, or send a notification email. Here’s what that same Dag looks like over time, with multiple runs:

![Image 2: Demo Dag in the Grid View, showing the status of all Dag runs, as well as logs for a task instance](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_grid_view_with_task_logs.png)
Each column in the grid represents a single Dag run. While the graph and grid views are most commonly used, Airflow provides several other views to help you monitor and troubleshoot workflows — such as the `Dag Overview` view:

![Image 3: Overview of a complex Dag in the Grid View, showing the status of all Dag runs, as well as quick links to recently failed task logs](https://airflow.apache.org/docs/apache-airflow/stable/_images/demo_complex_dag_overview_with_failed_tasks.png)

Note

The term “DAG” comes from the mathematical concept “directed acyclic graph”, but the meaning in Airflow has evolved well beyond just the literal data structure associated with the mathematical DAG concept. Therefore it was decided to use the term Dag in Airflow.

Why Airflow®?[](https://airflow.apache.org/docs/apache-airflow/stable/index.html#why-airflow "Link to this heading")
--------------------------------------------------------------------------------------------------------------------

Airflow is a platform for orchestrating batch workflows. It offers a flexible framework with a wide range of built-in operators and makes it easy to integrate with new technologies.

If your workflows have a clear start and end and run on a schedule, they’re a great fit for Airflow Dags.

If you prefer coding over clicking, Airflow is built for you. Defining workflows as Python code provides several key benefits:

*   **Version control**: Track changes, roll back to previous versions, and collaborate with your team.

*   **Team collaboration**: Multiple developers can work on the same workflow codebase.

*   **Testing**: Validate pipeline logic through unit and integration tests.

*   **Extensibility**: Customize workflows using a large ecosystem of existing components — or build your own.

Airflow’s rich scheduling and execution semantics make it easy to define complex, recurring pipelines. From the web interface, you can manually trigger Dags, inspect logs, and monitor task status. You can also backfill Dag runs to process historical data, or rerun only failed tasks to minimize cost and time.

The Airflow platform is highly customizable. With the [Public Interface for Airflow 3.0+](https://airflow.apache.org/docs/apache-airflow/stable/public-airflow-interface.html) you can extend and adapt nearly every part of the system — from operators to UI plugins to execution logic.

Because Airflow is open source, you’re building on components developed, tested, and maintained by a global community. You’ll find a wealth of learning resources, including blog posts, books, and conference talks — and you can connect with others via the [community](https://airflow.apache.org/community), [Slack](https://s.apache.org/airflow-slack), and mailing lists.

Why not Airflow®?[](https://airflow.apache.org/docs/apache-airflow/stable/index.html#why-not-airflow "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------

Airflow® is designed for finite, batch-oriented workflows. While you can trigger Dags using the CLI or REST API, Airflow is not intended for continuously running, event-driven, or streaming workloads. That said, Airflow often complements streaming systems like Apache Kafka. Kafka handles real-time ingestion, writing data to storage. Airflow can then periodically pick up that data and process it in batch.

If you prefer clicking over coding, Airflow might not be the best fit. The web UI simplifies workflow management, and the developer experience is continuously improving, but defining workflows as code is central to how Airflow works — so some coding is always required.
