# Source: https://docs.snowflake.com/en/developer-guide/snowflake-cli/streamlit-apps/manage-apps/share-app.md

# Share a Streamlit app

## Prerequisites

Before sharing a Streamlit app with Snowflake CLI, you should meet the following prerequisites:

* Ensure that your account has the correct privileges as described in [Privileges required to create and use a Streamlit app](../../../streamlit/object-management/privileges.md).
* Ensure that the app is already deployed in your connection.
* Ensure that your connection has the right ROLE and that the connection uses the correct database and schema.

## How to share a Streamlit app

To share a Streamlit app from the stage, enter the following command:

```snowcli
snow streamlit share my-app some-role
```

For more information about sharing Streamlit apps, see the CLI [snow streamlit share](../../command-reference/streamlit-commands/share.md) command.
