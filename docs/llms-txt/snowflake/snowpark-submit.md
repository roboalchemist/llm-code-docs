# Source: https://docs.snowflake.com/en/developer-guide/snowpark-connect/snowpark-submit.md

# Submitting Spark applications

You can run Spark workloads in a non-interactive, asynchronous way directly on Snowflake’s infrastructure while you use familiar
Spark semantics. With Snowpark Submit, you can submit production-ready Spark applications—such as ETL pipelines and scheduled data
transformations—by using a simple CLI interface. In this way, you can maintain your existing Spark development workflows without a
dedicated Spark cluster.

For example, you can package your PySpark ETL script, then use the Snowpark Submit CLI to run the script as a batch job on a Snowpark Container Services container.
This method lets you automate nightly data pipelines with Apache Airflow or CI/CD tools. Your Spark code runs in cluster mode on Snowpark Container Services,
scaling seamlessly with built-in dependency and resource management.

For examples of Snowpark Submit in use, see [Snowpark Submit examples](snowpark-submit-examples.md).

Snowpark Submit runs Spark workloads on Snowflake by using Snowpark Connect for Spark. For more information about Snowpark Connect for Spark, see
[Run Apache Spark™ workloads on Snowflake with Snowpark Connect for Spark](snowpark-connect-overview.md).

Snowpark Submit offers the following benefits:

* Ability to run in cluster mode on Snowflake-managed infrastructure with no external Spark setup
* Workflow integration, supporting automation through CI/CD pipelines, Apache Airflow, or cron-based scheduling
* Support for Python, enabling reuse of existing Spark applications across languages
* Dependency management, with support for packaging external Python modules or JARs

> **Note:**
>
> **snowpark-submit** supports much of the same functionality as **spark-submit**. However, some functionality has been
> omitted because it is not needed when running Spark workloads on Snowflake.

## Get started with Snowpark Submit

To get started using Snowpark Submit, follow these steps:

1. Install Snowpark Submit by following the steps in [Install Snowpark Submit](snowpark-submit-install.md).
2. Study the [Snowpark Submit examples](snowpark-submit-examples.md).
3. Get to know how to use Snowpark Submit with [Snowpark Submit reference](snowpark-submit-reference.md).
