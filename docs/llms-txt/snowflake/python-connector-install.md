# Source: https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-install.md

# Installing the Python Connector

To install the latest Python Connector for Snowflake, use:

> ```bash
> pip install snowflake-connector-python
> ```

If you won’t use Snowflake on AWS, you can exclude the `boto3` and `botocore` dependencies for AWS. These libraries take up both disk space and memory in the Python Connector, even when you don’t need them. To disable these libraries, set the `SNOWFLAKE_NO_BOTO` environment variable to `true` during installation:

> ```bash
> SNOWFLAKE_NO_BOTO=true pip install snowflake-connector-python
> ```

The source code for the Python driver is available on [GitHub](https://github.com/snowflakedb/snowflake-connector-python).

## Prerequisites

Requires Python version 3.9 (deprecated) or later.

For a list of the operating systems supported by Snowflake clients, see [Operating system support](../../release-notes/requirements.md).
