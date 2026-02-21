# Source: https://airflow.apache.org/docs/task-sdk/stable/index.html

Title: Apache Airflow Task SDK — Apache Airflow Task SDK Documentation

URL Source: https://airflow.apache.org/docs/task-sdk/stable/index.html

Markdown Content:
The Apache Airflow Task SDK provides python-native interfaces for defining Dags, executing tasks in isolated subprocesses and interacting with Airflow resources (e.g., Connections, Variables, XComs, Metrics, Logs, and OpenLineage events) at runtime. It also includes core execution-time components to manage communication between the worker and the Airflow scheduler/backend.

The goal of task-sdk is to decouple Dag authoring from Airflow internals (Scheduler, API Server, etc.), providing a forward-compatible, stable interface for writing and maintaining Dags across Airflow versions. This approach reduces boilerplate and keeps your Dag definitions concise and readable.

1. Introduction and Getting Started[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#introduction-and-getting-started "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------------------

Below is a quick introduction and installation guide to get started with the Task SDK.

### Installation[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#installation "Link to this heading")

To install the Task SDK, run:

pip install apache-airflow-task-sdk

### Getting Started[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#getting-started "Link to this heading")

Define a basic Dag and task in just a few lines of Python:

from airflow.sdk import dag, task

@dag
def example_simplest_dag():
    @task
    def my_task():
        pass

    my_task()

2. Public Interface[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#public-interface "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------

Direct metadata database access from task code is now restricted. A dedicated Task Execution API handles all runtime interactions (state transitions, heartbeats, XComs, and resource fetching), ensuring isolation and security.

Airflow now supports a service-oriented architecture, enabling tasks to be executed remotely via a new Task Execution API. This API decouples task execution from the scheduler and introduces a stable contract for running tasks outside of Airflow’s traditional runtime environment.

To support remote execution, Airflow provides the Task SDK — a lightweight runtime environment for running Airflow tasks in external systems such as containers, edge environments, or other runtimes. This lays the groundwork for language-agnostic task execution and brings improved isolation, portability, and extensibility to Airflow-based workflows.

Airflow 3.0 also introduces a new `airflow.sdk` namespace that exposes the core authoring interfaces for defining Dags and tasks. Dag authors should now import objects like [`airflow.sdk.DAG`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DAG "airflow.sdk.DAG"), [`airflow.sdk.dag()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.dag "airflow.sdk.dag"), and [`airflow.sdk.task()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task "airflow.sdk.task") from `airflow.sdk` rather than internal modules. This new namespace provides a stable, forward-compatible interface for Dag authoring across future versions of Airflow.

3. Dag authoring Enhancements[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#dag-authoring-enhancements "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Writing your Dags is now more consistent in Airflow 3.0. Use the stable `airflow.sdk` interface to define your workflows and tasks.

### Why use `airflow.sdk`?[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#why-use-airflow-sdk "Link to this heading")

*   Decouple your Dag definitions from Airflow internals (Scheduler, API Server, etc.)

*   Enjoy a consistent API that won’t break across Airflow upgrades

*   Import only the classes and decorators you need, without installing the full Airflow core

**Key imports from airflow.sdk**

**Classes**

*   [`airflow.sdk.Asset`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Asset "airflow.sdk.Asset")

*   [`airflow.sdk.BaseHook`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseHook "airflow.sdk.BaseHook")

*   [`airflow.sdk.BaseNotifier`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseNotifier "airflow.sdk.BaseNotifier")

*   [`airflow.sdk.BaseOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperator "airflow.sdk.BaseOperator")

*   [`airflow.sdk.BaseOperatorLink`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseOperatorLink "airflow.sdk.BaseOperatorLink")

*   [`airflow.sdk.BaseSensorOperator`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.BaseSensorOperator "airflow.sdk.BaseSensorOperator")

*   [`airflow.sdk.Connection`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Connection "airflow.sdk.Connection")

*   [`airflow.sdk.Context`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Context "airflow.sdk.Context")

*   [`airflow.sdk.DAG`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DAG "airflow.sdk.DAG")

*   [`airflow.sdk.EdgeModifier`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.EdgeModifier "airflow.sdk.EdgeModifier")

*   [`airflow.sdk.Label`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Label "airflow.sdk.Label")

*   [`airflow.sdk.ObjectStoragePath`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.ObjectStoragePath "airflow.sdk.ObjectStoragePath")

*   [`airflow.sdk.Param`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Param "airflow.sdk.Param")

*   [`airflow.sdk.TaskGroup`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.TaskGroup "airflow.sdk.TaskGroup")

*   [`airflow.sdk.TaskInstanceState`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.TaskInstanceState "airflow.sdk.TaskInstanceState")

*   [`airflow.sdk.DagRunState`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.DagRunState "airflow.sdk.DagRunState")

*   [`airflow.sdk.WeightRule`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.WeightRule "airflow.sdk.WeightRule")

*   [`airflow.sdk.Variable`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.Variable "airflow.sdk.Variable")

**Decorators and helper functions**

*   [`airflow.sdk.asset()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.asset "airflow.sdk.asset")

*   [`airflow.sdk.dag()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.dag "airflow.sdk.dag")

*   [`airflow.sdk.setup()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.setup "airflow.sdk.setup")

*   [`airflow.sdk.task()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task "airflow.sdk.task")

*   [`airflow.sdk.task_group()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.task_group "airflow.sdk.task_group")

*   [`airflow.sdk.teardown()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.teardown "airflow.sdk.teardown")

*   [`airflow.sdk.chain()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.chain "airflow.sdk.chain")

*   [`airflow.sdk.chain_linear()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.chain_linear "airflow.sdk.chain_linear")

*   [`airflow.sdk.cross_downstream()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.cross_downstream "airflow.sdk.cross_downstream")

*   [`airflow.sdk.get_current_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_current_context "airflow.sdk.get_current_context")

*   [`airflow.sdk.get_parsing_context()`](https://airflow.apache.org/docs/task-sdk/stable/api.html#airflow.sdk.get_parsing_context "airflow.sdk.get_parsing_context")

All Dags must update their imports to refer to `airflow.sdk` instead of using internal Airflow modules directly. Deprecated legacy import paths, such as `airflow.models.dag.DAG` and `airflow.decorator.task`, will be removed in a future version of Airflow. Some utilities and helper functions currently used from `airflow.utils.*` and other modules will gradually be migrated to the Task SDK over the next minor releases. These upcoming updates aim to completely separate Dag creation from internal Airflow services. Dag authors can look forward to continuous improvements to airflow.sdk, with no backwards-incompatible changes to their existing code.

Legacy imports (deprecated):

# Airflow 2.x
from airflow.models import DAG
from airflow.decorators import task

Use instead:

# Airflow 3.x
from airflow.sdk import DAG, task

4. Example Dag References[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#example-dag-references "Link to this heading")
--------------------------------------------------------------------------------------------------------------------------------------

Explore a variety of Dag examples and patterns in the [Examples](https://airflow.apache.org/docs/task-sdk/stable/examples.html) page.

5. Concepts[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#concepts "Link to this heading")
----------------------------------------------------------------------------------------------------------

Discover the fundamental concepts that Dag authors need to understand when working with the Task SDK, including Airflow 2.x vs 3.x architectural differences, database access restrictions, and task lifecycle. For full details, see the [Concepts](https://airflow.apache.org/docs/task-sdk/stable/concepts.html) page.

### Airflow 2.x Architecture[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#airflow-2-x-architecture "Link to this heading")

![Image 1: Airflow 2.x architecture diagram showing scheduler, metadata DB, and worker interactions](https://airflow.apache.org/docs/task-sdk/stable/_images/airflow-2-approach.png)
### Architectural Decoupling: Task Execution Interface (Airflow 3.x)[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#architectural-decoupling-task-execution-interface-airflow-3-x "Link to this heading")

![Image 2: Airflow 3.x Task Execution API architecture diagram showing Execution API Server and worker subprocesses](https://airflow.apache.org/docs/task-sdk/stable/_images/airflow-3-task-sdk.png)
6. API References[¶](https://airflow.apache.org/docs/task-sdk/stable/index.html#api-references "Link to this heading")
----------------------------------------------------------------------------------------------------------------------

For the full public API reference, see the [airflow.sdk API Reference](https://airflow.apache.org/docs/task-sdk/stable/api.html) page.
