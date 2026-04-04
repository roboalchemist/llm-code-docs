# Source: https://docs.snowflake.com/en/sql-reference/external-functions-creating-azure-asynchronous.md

# Creating an asynchronous function on Azure

The concepts for creating an asynchronous external functions on Azure are similar to the concepts for
[creating an asynchronous function on AWS](external-functions-creating-aws-sample-asynchronous.md).

However, the AWS code sample cannot be used directly on Azure because you must use the corresponding Azure services like
Azure Functions and Azure Blob Storage. Furthermore, the details of navigating the cloud platform’s user interface differ.
