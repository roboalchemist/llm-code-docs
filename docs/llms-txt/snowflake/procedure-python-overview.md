# Source: https://docs.snowflake.com/en/developer-guide/stored-procedure/python/procedure-python-overview.md

# Writing stored procedures with SQL and Python

You can write a stored procedure whose handler is coded in Python. By using APIs from the [Snowpark library](../../snowpark/python/index.md)
within your handler, you can perform queries, updates, and other work on Snowflake tables.

With stored procedures, you can build and run your data pipeline within Snowflake, using a Snowflake warehouse
as the compute framework. Build your data pipeline by using the [Snowpark API for Python](../../snowpark/python/creating-sprocs.md)
to write stored procedures. To schedule the execution of these stored procedures, you use [tasks](../../../user-guide/tasks-intro.md).

For information about machine learning models and Snowpark Python, see [Training Machine Learning Models with Snowpark Python](../../snowpark/python/python-snowpark-training-ml.md).

You can write stored procedures for Python [using a Python worksheet](../../snowpark/python/python-worksheets.md),
or using a local development environment.

You can capture log and trace data as your handler code executes. For more information, refer to
[Logging, tracing, and metrics](../../logging-tracing/logging-tracing-overview.md).

> **Note:**
>
> To both create and call an anonymous procedure, use [CALL (with anonymous procedure)](../../../sql-reference/sql/call-with.md). Creating and calling an anonymous procedure does
> not require a role with CREATE PROCEDURE schema privileges.

## Prerequisites for writing stored procedures locally

To write Python stored procedures in your local development environment, meet the following prerequisites:

* You must use version 0.4.0 or a more recent version of the Snowpark library.
* Enable Anaconda Packages so that Snowpark Python can load the required third-party dependencies. Refer to Using third-party packages from Anaconda.
* The supported versions of Python are:

  Generally available versions:

  * 3.9 (deprecated)
  * 3.10
  * 3.11
  * 3.12
  * 3.13

Be sure to set up your development environment to use the Snowpark library.
Refer to [Setting Up Your Development Environment for Snowpark](../../snowpark/python/setup.md).

> **Note:**
>
> While not required, Snowflake recommends [Artifact Repository overview](../../udf/python/udf-python-packages.md) to import Python packages. For more information, see below.

### Using artifact repository

You can specify packages to install from the Python Package Index (PyPI) and use them with Snowpark Python stored procedures. For more information, see [Artifact Repository overview](../../udf/python/udf-python-packages.md).

### Using third-party packages from Anaconda

You can specify Anaconda packages to install when you create Snowpark Python stored procedures. To view the list of third-party packages
from Anaconda, see the [Anaconda Snowflake channel](https://repo.anaconda.com/pkgs/snowflake).
These third-party packages are built and provided by Anaconda.
You may use the Snowflake conda channel for local testing and development at no cost under the Supplemental Embedded Software Terms to Anaconda’s Terms of Service.

For limitations, see [Python stored procedure limitations](procedure-python-limitations.md).

### Getting started

Before you start using the packages provided by Anaconda inside Snowflake, you must acknowledge
the [External Offerings Terms](https://www.snowflake.com/legal/external-offering-terms/).

> **Note:**
>
> You must use the ORGADMIN role to accept the terms. You only need to accept the
> [External Offerings Terms](https://www.snowflake.com/legal/external-offering-terms/) once for your Snowflake account. If you do not have
> access to the ORGADMIN role, see [Enabling the ORGADMIN role in an account](../../../user-guide/organization-administrators.md).

1. Sign in to [Snowsight](../../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Terms.
3. In the Anaconda section, select Enable.
4. In the Anaconda Packages dialog, click the link to review the [External Offerings Terms page](https://www.snowflake.com/legal/external-offering-terms/).
5. If you agree to the terms, select Acknowledge & Continue.

If you encounter an error when attempting to accept the [External Offerings Terms](https://www.snowflake.com/legal/external-offering-terms/),
it may be due to missing information in your user profile, such as a first name, last name, or email address. If you have administrator
privileges, see [Add user details to your user profile](../../../user-guide/ui-snowsight-profile.md) to update your profile using Snowsight. Otherwise, contact an
administrator to [update your account](../../../user-guide/admin-user-management.md).

> **Note:**
>
> If you don’t acknowledge the Snowflake [External Offerings Terms](https://www.snowflake.com/legal/external-offering-terms/) as described
> above, you can still use stored procedures, but with these limitations:
>
> * You can’t use any third-party packages from Anaconda.
> * You can still specify Snowpark Python as a package in a stored procedure, but you can’t specify a specific version.
> * You can’t use the `to_pandas` method when interacting with a `DataFrame` object.

### Displaying and using packages

You can display all available packages and their version information by querying the PACKAGES view in the Information Schema:

```python
SELECT * FROM information_schema.packages WHERE LANGUAGE = 'python';
```

For more information, see [Using third-party packages](../../udf/python/udf-python-packages.md) in the Snowflake Python UDF documentation.

## Calling your stored procedure

After creating a stored procedure, you can call it in the following ways:

* [From SQL](../stored-procedures-calling.md).
* [As part of a scheduled task](../../../user-guide/tasks-intro.md).
