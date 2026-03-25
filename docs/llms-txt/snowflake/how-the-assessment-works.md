# Source: https://docs.snowflake.com/en/migrations/sma-docs/user-guide/assessment/how-the-assessment-works.md

# Snowpark Migration Accelerator: How the Assessment Works

The Snowpark Migration Accelerator (SMA) analyzes your source code and creates a detailed inventory of all its components and dependencies.

[As mentioned previously](../../general/introduction.md), the Snowpark Migration Accelerator (SMA) is more sophisticated than a simple pattern-matching or text replacement tool. It analyzes your source code and creates a comprehensive semantic model that captures all the functionality of your codebase.

The SMA assessment provides a comprehensive inventory of your source code files and evaluates how well your existing Spark API code will work with the Snowpark API. This assessment helps you start your migration project and gives you a clear overview of all the code in your workload.

The assessment process generates the following outputs:

* [Readiness score](../../support/glossary.md)
* A complete list of all Spark API references and their compatibility with the Snowpark API
* A comprehensive list of all third-party library imports in your codebase
* A summary report containing detailed information from all collected inventories

To view all output files generated during assessment mode, please refer to [the output reports section](output-reports/README.md) of this documentation.
