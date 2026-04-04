# Source: https://docs.airbyte.com/platform/operator-guides/using-prefect-task.md

# Source: https://docs.airbyte.com/platform/2.0/operator-guides/using-prefect-task.md

# Source: https://docs.airbyte.com/platform/1.8/operator-guides/using-prefect-task.md

# Source: https://docs.airbyte.com/platform/1.7/operator-guides/using-prefect-task.md

# Source: https://docs.airbyte.com/platform/1.6/operator-guides/using-prefect-task.md

# Using the Prefect Airbyte Task

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Airbyte is an official integration Task in the Prefect project. The Airbyte Task allows you to trigger synchronization jobs in Prefect, and this tutorial will walk through configuring your Prefect Flow to do so.

The Airbyte Task documentation on Prefect project can be found [here](https://docs.prefect.io/api/latest/tasks/airbyte.html#airbyteconnectiontask) and the [Prefect 2.0 community guide can be found here](https://www.prefect.io/guide/community-posts/orchestrating-airbyte-with-prefect-2-0/).

## 1. Set up the tools[​](#1-set-up-the-tools "Direct link to 1. Set up the tools")

First, make sure you have Docker installed. We'll be using the `docker-compose` command, so your install should contain `docker-compose`.

### **Start Airbyte**[​](#start-airbyte "Direct link to start-airbyte")

If this is your first time using Airbyte, we suggest going through our [Quickstart](/platform/1.6/using-airbyte/getting-started/oss-quickstart.md).

For the purposes of this tutorial, set your Connection's **sync frequency** to **manual**. Prefect will be responsible for manually triggering the Airbyte job.

### **Start Prefect**[​](#start-prefect "Direct link to start-prefect")

If you don't have a Prefect instance, we recommend following this [guide](https://docs.prefect.io/core/getting_started/install.html) to set one up.

## 2. Create a Flow in Prefect to trigger your Airbyte job[​](#2-create-a-flow-in-prefect-to-trigger-your-airbyte-job "Direct link to 2. Create a Flow in Prefect to trigger your Airbyte job")

### Create a new Prefect Project[​](#create-a-new-prefect-project "Direct link to Create a new Prefect Project")

```
prefect create project "airbyte"
```

### Retrieving the Airbyte Connection ID[​](#retrieving-the-airbyte-connection-id "Direct link to Retrieving the Airbyte Connection ID")

We'll need the Airbyte Connection ID so our Prefect Flow knows which Airbyte Connection to trigger.

This ID can be seen in the URL on the connection page in the Airbyte UI. The Airbyte UI can be accessed at `localhost:8000`.

### Creating a simple Prefect DAG to run an Airbyte Sync Job[​](#creating-a-simple-prefect-dag-to-run-an-airbyte-sync-job "Direct link to Creating a simple Prefect DAG to run an Airbyte Sync Job")

Create a new folder called `airbyte_prefect` and create a file `airbyte_prefect_flow.py`.

```
from prefect import Flow
from prefect.tasks.airbyte.airbyte import AirbyteConnectionTask

airbyte_conn = AirbyteConnectionTask(
        airbyte_server_host="localhost",
        airbyte_server_port=8000,
        airbyte_api_version="v1",
        connection_id="04e128af-1092-4a83-bf33-1b8c85395d74"
)

with Flow("first-airbyte-task") as flow:
    flow.add_task(airbyte_conn)

# Register the flow under the "airbyte" project
flow.register(project_name="airbyte")
```

The Airbyte Prefect Task accepts the following parameters:

* `airbyte_server_host`: The host URL to your Airbyte instance.
* `airbyte_server_post`: The port value you have selected for your Airbyte instance.
* `airbyte_api_version`: default value is `v1`.
* `connection_id`: The ID of the Airbyte Connection to be triggered by Prefect.

After running the file, `python3 airbyte_prefect_flow.py` this will register the Flow in Prefect Server.

Access the link from the output from the previous command to see the Flow in Prefect Server, or you can navigate in Prefect UI to find the new Flow -> Access the link from the output from the previous command to see the Flow in the Prefect Server. Alternatively, you can go to the Prefect UI to find the new Flow.

Click on the button `Run` and configure your first run.

After a few moments you should see the finished run.

After that you have the option to configure a more complex Schedule to your Flow. See the [Prefect Schedule docs.](https://docs.prefect.io/core/concepts/schedules.html)

## That's it\![​](#thats-it "Direct link to That's it!")

Don't be fooled by our simple example of only one Prefect Flow. Airbyte is a powerful data integration platform supporting many sources and destinations. The Airbyte Prefect Task means Airbyte can now be easily used with the Prefect ecosystem - give it a shot!

We love to hear any questions or feedback on our [Slack](https://slack.airbyte.io/). If you see any rough edges or want to request a connector, feel free to create an issue on our [Github](https://github.com/airbytehq/airbyte) or thumbs up an existing issue.

## Related articles and guides[​](#related-articles-and-guides "Direct link to Related articles and guides")

For additional information about using Prefect and Airbyte together, see the following:

* [Build an e-commerce analytics stack with Airbyte, dbt, Prefect and BigQuery](https://github.com/airbytehq/quickstarts/tree/main/airbyte_dbt_prefect_bigquery)
