# Source: https://docs.startree.ai/corecapabilities/visualize_data/connect-superset-to-startree-cloud.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Connect Superset to StarTree Cloud to visualize your data.

# Connect Superset to StarTree Cloud

## Prerequisites

* Access to a StarTree Cloud cluster.
* Access to a Superset instance. \
  For more information about how to install and deploy Superset, see [What is Apache Superset?](https://superset.apache.org/docs/intro)
* Superset instance has the Pinot database driver installed, which is compatible with StarTree Cloud. For more information, see how to [install a database driver for Superset](https://superset.apache.org/docs/databases/installing-database-drivers).

## Obtain the SQLAlchemy URI to connect to StarTree

1. Visit the apps page of your cluster.
2. Click on the **Pinot API Tokens** button.
3. On the API Tokens page, select **Clients** from the left hand sidebar.
4. Click on **Superset** in the client options.
5. Click **Create a new API Token**.
6. Copy the *SQLAlchemy URI*.

## Create the Database Connection in Superset

1. In Superset, click **Settings** in the top-right corner and select **Database Connections** under the Data section.
2. Click the **+ Database** button.
3. Open the **Choose a Database** dropdown and select *Apache Pinot*.  \
   If Apache Pinot is not listed, see the [instructions](https://superset.apache.org/docs/configuration/databases#apache-pinot) to configure the Apache Pinot database driver.
4. Specify a name for the database connection
5. Paste the *SQLAlchemy URI* that you copied from StarTree.
6. Test the connection.

Built with [Mintlify](https://mintlify.com).
