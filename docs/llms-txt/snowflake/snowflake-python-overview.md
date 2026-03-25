# Source: https://docs.snowflake.com/en/developer-guide/snowflake-python-api/snowflake-python-overview.md

# Snowflake Python APIs: Managing Snowflake objects with Python

The Snowflake Python APIs package is a unified library that seamlessly connects Python with Snowflake workloads. It is intended to provide
comprehensive APIs for interacting with Snowflake resources across data engineering, Snowpark, Snowpark ML, and application workloads using
a first-class Python API.

You can use the Snowflake Python APIs to manage Snowflake resources by creating, dropping, or altering them, and more. You can use
Python to perform tasks you might otherwise perform with Snowflake [SQL commands](../../sql-reference-commands.md).

To learn more about the API, including its general concepts and design patterns, see [Snowflake Python APIs: General concepts](snowflake-python-general-concepts.md).

## Supported Snowflake resource objects

> **Note:**
>
> The [API reference documentation](https://docs.snowflake.com/developer-guide/snowflake-python-api/reference/latest/index) reflects the
> latest version of the Snowflake Python APIs. Note that not all resources in the API currently provide 100% coverage of their
> equivalent [SQL commands](../../sql-reference-commands.md), but the Python APIs are under active development and are continuously expanding.

With the Snowflake Python APIs, you can currently manage the following Snowflake resource objects:

* [Accounts](snowflake-python-managing-accounts.md)

  * [Account](snowflake-python-managing-accounts.md)
  * [Managed account](snowflake-python-managing-accounts.md)
* [Users, roles, and privileges](snowflake-python-managing-user-roles.md)

  * [User](snowflake-python-managing-user-roles.md)
  * [Role](snowflake-python-managing-user-roles.md)
  * [Database role](snowflake-python-managing-user-roles.md)
  * [Access privileges](snowflake-python-managing-user-roles.md)
* [Integrations](snowflake-python-managing-integrations.md)

  * [API integration](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.api_integration)
  * [Catalog integration](snowflake-python-managing-integrations.md)
  * [Notification integration](snowflake-python-managing-integrations.md)
* [Virtual warehouse](snowflake-python-managing-warehouses.md)
* [Databases, schemas, tables, and views](snowflake-python-managing-databases.md)

  * [Database](snowflake-python-managing-databases.md)
  * [Schema](snowflake-python-managing-databases.md)
  * [Standard table](snowflake-python-managing-databases.md)
  * [Dynamic table](snowflake-python-managing-dynamic-tables.md)
  * [Event table](snowflake-python-managing-databases.md)
  * [Iceberg table](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.iceberg_table)
  * [View](snowflake-python-managing-databases.md)
  * [Sequence](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.sequence)
* [Functions and procedures](snowflake-python-managing-functions-procedures.md)

  * [Stored procedure](snowflake-python-managing-functions-procedures.md)
  * [User-defined function (UDF)](snowflake-python-managing-functions-procedures.md)
  * [Artifact repository](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.artifact_repository)
* Data pipeline

  * [Stream](snowflake-python-managing-streams.md)
  * [Task](snowflake-python-managing-tasks.md)
* AI and ML (not available in government regions)

  * [Cortex Chat service](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.cortex.chat_service)
  * [Cortex Embed service](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.cortex.embed_service)
  * [Cortex Inference service](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.cortex.inference_service)
  * [Cortex Lite Agent service](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.cortex.lite_agent_service)
  * [Cortex Search service](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.cortex.search_service)
* Security

  * [Network policy](snowflake-python-managing-network-policies.md)
  * [Network rule](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.network_rule)
  * [Password policy](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.password_policy)
  * [Secret](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.secret)
* Data governance

  * [Tag](snowflake-python-managing-tags.md)
* [Data loading and unloading](snowflake-python-managing-data-loading.md)

  * [External volume](snowflake-python-managing-data-loading.md)
  * [Pipe](snowflake-python-managing-data-loading.md)
  * [Stage](snowflake-python-managing-data-loading.md)
* [Alert](snowflake-python-managing-alerts.md)
* [Notebook](snowflake-python-managing-notebooks.md)
* [Snowpark Container Services components](snowflake-python-managing-containers.md)
  (not available in government regions)

  * [Compute pool](snowflake-python-managing-containers.md)
  * [Image repository](snowflake-python-managing-containers.md)
  * [Service and service function](snowflake-python-managing-containers.md)
* Streamlit

  * [Streamlit object](/developer-guide/snowflake-python-api/reference/latest/_autosummary/snowflake.core.streamlit)

## Python ecosystem in Snowflake

The Snowflake Python APIs, the [Snowpark API for Python](../snowpark/python/index.md), and the
[Snowflake Connector for Python](../python-connector/python-connector.md) are interfaces that each have distinct purposes
in Snowflake. This section explains their differences and describes the typical use cases for each.

Snowflake Python APIs
:   You can use this set of first-class Python APIs to define and manage core resources (such as tables, warehouses, and tasks) across
    Snowflake workloads. Unlike the Python Connector, these APIs interact with Snowflake using native Python without the need to use SQL.

    The Snowflake Python APIs package unifies all Snowflake Python libraries (including `connector`, `core`, `snowpark`, and
    `ml`) so that you can simply start with the command `pip install snowflake`.

    Following the declarative programming approach, this API can be used as a DevOps tool to manage changes to your resources and automate
    code and infrastructure deployment in Snowflake.

Snowpark
:   This set of libraries and code execution environments can run Python and other programming languages next to your data in Snowflake.

    * Libraries: With the [Snowpark API](../snowpark/index.md), you can use Snowpark DataFrames in your code to query and transform data
      entirely within Snowflake. Snowpark applications process your data at scale directly on the Snowflake engine without moving the data to
      the system where your application code runs.

      The Snowpark API is available in Python, Java, and Scala.
    * Code execution environments: Snowpark runtime environments support container images and Python, Java, and Scala code.

      + You can execute custom Python code through Python user-defined functions (UDFs) or stored procedures for building data pipelines,
        apps, and more. Python runtime environments have access to a package repository and package manager from Anaconda.

        Runtime environments are also available in Scala and Java.
      + You can run containerized applications directly within Snowflake using
        [Snowpark Container Services](../snowpark-container-services/overview.md).

Snowflake Connector for Python
:   Use this SQL driver to connect to Snowflake, execute SQL statements, and then get the results using a Python client.

    With the Python Connector, you write all of your interactions with Snowflake using SQL statement strings.

## Get started with the Snowflake Python APIs

To get started with the Snowflake Python APIs, see the instructions in the following topics:

1. [Install the library](snowflake-python-installing.md).
2. [Connect to Snowflake](snowflake-python-connecting-snowflake.md).

For tutorials on getting started with the Snowflake Python APIs, see [Tutorials: Getting started with the Snowflake Python APIs](overview-tutorials.md).

## Supported Python versions

The supported versions of Python are:

Generally available versions:

* 3.9 (deprecated)
* 3.10
* 3.11
* 3.12
* 3.13

## Developer guides

| Guide | Description |
| --- | --- |
| [Install the Snowflake Python APIs library](snowflake-python-installing.md) | Install the Snowflake Python APIs package. |
| [Connect to Snowflake with the Snowflake Python APIs](snowflake-python-connecting-snowflake.md) | Connect to Snowflake from Python code. |
| [Managing Snowflake accounts and managed accounts with Python](snowflake-python-managing-accounts.md) | Use the API to create and manage accounts and managed accounts. |
| [Managing Snowflake alerts with Python](snowflake-python-managing-alerts.md) | Use the API to create and manage alerts. |
| [Managing data loading and unloading resources with Python](snowflake-python-managing-data-loading.md) | Use the API to create and manage data loading and unloading resources, including external volumes, pipes, and stages. |
| [Managing Snowflake databases, schemas, tables, and views with Python](snowflake-python-managing-databases.md) | Use the API to create and manage databases, schemas, and tables. |
| [Managing Snowflake dynamic tables with Python](snowflake-python-managing-dynamic-tables.md) | Use the API to create and manage dynamic tables. |
| [Managing Snowflake functions and stored procedures with Python](snowflake-python-managing-functions-procedures.md) | Use the API to create and manage user-defined functions (UDFs) and stored procedures. |
| [Managing Snowflake integrations with Python](snowflake-python-managing-integrations.md) | Use the API to create and manage catalog integrations and notification integrations. |
| [Managing Snowflake network policies with Python](snowflake-python-managing-network-policies.md) | Use the API to create and manage network policies. |
| [Managing Snowflake Notebooks with Python](snowflake-python-managing-notebooks.md) | Use the API to create and manage Snowflake Notebooks. |
| [Managing Snowpark Container Services (including service functions) with Python](snowflake-python-managing-containers.md) | Use the API to manage components of Snowpark Container Services, including compute pools, image repositories, services, and service functions. |
| [Managing Snowflake streams with Python](snowflake-python-managing-streams.md) | Use the API to create and manage streams. |
| [Managing Snowflake tasks and task graphs with Python](snowflake-python-managing-tasks.md) | Use the API to create, execute, and manage tasks and task graphs. |
| [Managing Snowflake users, roles, and grants with Python](snowflake-python-managing-user-roles.md) | Use the API to create and manage users, roles, and grants. |
| [Managing Snowflake virtual warehouses with Python](snowflake-python-managing-warehouses.md) | Use the API to create and manage virtual warehouses. |

## References

[Snowflake Python APIs Reference](https://docs.snowflake.com/developer-guide/snowflake-python-api/reference/latest/index)

## Costs of Snowflake access

To reduce costs—–for both usage credit and network activity—–the Snowflake Python APIs are designed to communicate with Snowflake
only when you call methods designed to synchronize with Snowflake.

Objects in the API are either local references (or *handles*) or snapshots of state stored on Snowflake. In general, when you process
information that was retrieved from Snowflake, you do so through a local, in-memory reference object.

These references do not synchronize with Snowflake until you call a method. When you call a method, you are usually incurring costs in
both usage credit and network activity. In contrast, when you work with in-memory references, such as when accessing attributes, your work
is performed locally and incurs no such costs.
