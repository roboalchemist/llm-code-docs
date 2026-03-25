# Source: https://docs.snowflake.com/en/developer-guide/streamlit/about-streamlit.md

# About Streamlit in Snowflake

This topic describes key features of Streamlit in Snowflake.

## What is Streamlit?

[Streamlit](https://streamlit.io/) is an open-source Python library that makes it easy to create
and share custom web apps for machine learning and data science. By using Streamlit you can quickly
build and deploy powerful data applications. For more information about the open-source library, see the
[Streamlit documentation](https://docs.streamlit.io/).

## Deploy Streamlit apps in Snowflake

Streamlit in Snowflake helps developers securely build, deploy, and share Streamlit apps on Snowflake’s data
cloud. Using Streamlit in Snowflake, you can build applications that process and use data in Snowflake without moving
data or application code to an external system.

### Key features of Streamlit in Snowflake

* Snowflake manages the underlying compute and storage for your Streamlit app.
* Snowflake stores your source code and environment configuration within a Snowflake object that uses [Role-based Access Control (RBAC)](../../user-guide/security-access-control-overview.md) to manage access to your Streamlit app.
* You can choose between a warehouse and container runtime (Preview).
* Streamlit in Snowflake works seamlessly with Snowpark, user-defined functions (UDFs), stored procedures, and Snowflake Native App Framework.
* When working in Snowsight, you can use the side-by-side editor and app preview to quickly modify your source code and environment.

## Use cases

For additional use cases on building dashboards, data tools, and ML/AI, see [Streamlit in Snowflake demos](https://github.com/Snowflake-Labs/snowflake-demo-streamlit).

> **Note:**
>
> These quickstarts are only shown as examples. Following along with the example may require additional rights to third-party data,
> products, or services that are not owned or provided by Snowflake. Snowflake does not guarantee the accuracy of these examples or
> cover them under any Service Level Agreement.

## Developer guides

The following guides explain working with Streamlit in Snowflake.

| Guide | Description |
| --- | --- |
| [Getting started with Streamlit in Snowflake](getting-started/overview.md) | Learn about the prerequisites and privileges required to work with Streamlit in Snowflake, and build your first app. |
| [Create and deploy Streamlit apps using SQL](getting-started/create-streamlit-sql.md) | Learn how to create and deploy Streamlit apps using SQL. |
| [Create and deploy Streamlit apps using Snowsight](getting-started/create-streamlit-ui.md) | Learn how to create and deploy Streamlit apps using Snowsight. |
| [Create and deploy Streamlit apps using Snowflake CLI](getting-started/create-streamlit-snowflake-cli.md) | Learn how to create and deploy Streamlit apps using Snowflake CLI. |
