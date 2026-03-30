# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-connect-clients.md

# Development clients for Snowpark Connect for Spark

You can run Spark workloads interactively from clients such as Snowflake Notebooks, Jupyter Notebooks, VS Code, or any Python-based
interface without needing to manage a Spark cluster. The workloads run on the Snowflake infrastructure.

When you develop Spark workloads interactively with Snowpark Connect for Spark, you can perform the following tasks:

* Run Spark workloads from local tools without setting up any infrastructure.
* Run code that is compatible with PySpark APIs and workflows.
* Access Snowflake compute resources for running queries and transformations.
* Integrate Spark into existing data science, exploration, or development workflows.
* Authenticate with programmatic access tokens (PATs) for secure authentication that is aligned with modern enterprise access controls.

The following table lists some of the tools you can use when you work with Spark workloads on Snowflake:

| Purpose | Tools |
| --- | --- |
| Interactively develop Spark workloads that run on Snowflake. | *[Run Spark workloads from Snowflake Notebooks](snowpark-connect-workloads-snowflake-notebook.md)* [Run Spark workloads from VS Code, Jupyter Notebooks, or a terminal](snowpark-connect-workloads-jupyter.md) |
| Run Spark workloads as a batch. | * [Submitting Spark applications](snowpark-submit.md) |
