# Source: https://firebase.google.com/docs/cloud-messaging/fcm-bigquery-ai.md.txt

> [!IMPORTANT]
> **Important:** AI tools and MCP are experimental and can make mistakes. Make sure to double check the data source for correctness. For enhanced privacy, turn off data tracking and data for model training options on your AI agent.

The [BigQuery MCP Toolbox](https://cloud.google.com/bigquery/docs/pre-built-tools-with-mcp-toolbox)
provides a set of MCP tools designed to simplify the interaction with BigQuery
data. It can be used to query the FCM BigQuery exported data. This
documentation shows how to use the BigQuery MCP Toolbox and an AI agent to query
and analyze this data quickly and effectively.

## Set up BigQuery Export

- Make sure your FCM project is configured to export data to BigQuery. See [understanding message delivery](https://firebase.google.com/docs/cloud-messaging/understand-delivery?platform=web#bigquery-data-export) to get started.
- Once enabled, FCM will automatically populate a BigQuery dataset with message delivery events.

#### Set up the BigQuery MCP Toolbox

1. Follow the instructions in [Use BigQuery with agents](https://cloud.google.com/bigquery/docs/pre-built-tools-with-mcp-toolbox) to install and configure the BigQuery MCP toolbox.

## Query BigQuery Export Data using an AI agent

Once the setup is complete, your AI agent should be able to list the available
tools. Check your AI agent to make sure the following tools are available:

- `execute_sql`
- `get_dataset_info`
- `get_table_info`
- `list_dataset_ids`
- `list_table_ids`

Now, you can use the following example prompts with your AI agent:

- How many FCM notifications were sent in the last 7 days?
- Graph the data by date.
- What are some common errors for missing notifications?

## Benefits of using AI agent for data exploration

Some of the benefits that come with using AI agent for data exploration include:

- **Accessibility:** This lets your users to query data using natural language.
- **Easy Visualization:** You can use LLMs capabilities to visualize data returned from BigQuery.

## Feedback channels

To provide feedback, contact the following:

- For AI agent response issues, contact the model owner or the AI agent team.
- For BigQuery MCP toolbox issues, contact the [Google Cloud support
  team](https://cloud.google.com/contact).