# Source: https://docs.snowflake.com/en/sql-reference/external-functions.md

# Writing external functions

External functions are user-defined functions that are stored and executed outside of Snowflake.

External functions make it easier to access external API services such as geocoders, machine learning models, and other custom code
running outside of Snowflake. This feature eliminates the need to export and reimport data when using third-party services, significantly
simplifying your data pipelines.

> **Note:**
>
> When using external functions in China, use the [syntax and workflow described for AWS](external-functions-creating-aws.md).

[Introduction to external functions](external-functions-introduction.md)
:   Learn about external functions, which call executable code that is developed, maintained, stored, and executed outside Snowflake.

[Remote service input and output data formats](external-functions-data-format.md)
:   Understand the data formats sent and received by Snowflake.

[Using request and response translators with data for a remote service](external-functions-translators.md)
:   Change the format of data sent to and received from remote services.

[Designing high-performance external functions](external-functions-implementation.md)
:   Design high-performance functions with these tips on asynchronous services, scalability, concurrency, and reliability.

[External functions best practices](external-functions-best-practices.md)
:   Improve efficiency and prevent unexpected results with these best practices.

[Securing an external function](external-functions-security.md)
:   Create secure external functions.

## Remote services

[Creating external functions on AWS](external-functions-creating-aws.md)
:   Create an external function from functionality on AWS.

[Creating external functions on GCP](external-functions-creating-gcp.md)
:   Create an external function from functionality on GCP.

[Creating external functions on Microsoft Azure](external-functions-creating-azure.md)
:   Create an external function from functionality on Azure.
