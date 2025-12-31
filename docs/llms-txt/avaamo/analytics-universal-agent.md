# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics-universal-agent.md

# Analytics - Universal agent

The **Analytics** tool for Universal agents gives a graphical representation of the statistics on agent and user interaction. It provides usage and related information on both the universal agent and its member agents.

**To view the analytics of an agent**:

1. Navigate to the **Agents** tab on the top menu.
2. Search and click any agent for which you wish to view **Analytics**. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents/other-common-actions#search-agents), for more information.
3. On the **Agent's** page, click **Monitor -> Analytics**. A list of built-in **Analytics** for the agent in the selected date range is displayed.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fmyd9lGbigfwptRQFeOKw%2F6.1-analytics-new.png?alt=media\&token=80b3d47a-1934-4946-b699-ff939fde5e6d)

By default, the date range is a week (7 days) from the current date. You can also select different date ranges as per your requirement to filter results. See [Date range](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#date-range), for more information.

Click **Download** to download a PDF copy of the current Analytics board. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.&#x20;

### **Analytics Board - Information**

The analytics board for the Universal agent has the following blocks. Clicking on a block provides a detailed view.

* [Total queries](#total-queries-for-universal-agent)**:** Total number of queries received by the agent.
* [Unhandled queries](#unhandled-queries-for-universal-agent): Number of queries that failed to match any known intent.
* [Disambiguation queries](#disambiguation-queries-for-universal-agent): Number of queries that required disambiguation.&#x20;
* [Channel&#x73;**:**](#channels-for-universal-agent) The channels through which the agent interacted and the percentage of user interaction through each of these channels.
* [Member agent blocks](#member-agent-blocks-for-universal-agent): Analytics box for each member agent shows the number of queries handled by each member agent.

### Total queries for Universal agent

The **Total queries** block displays the total number of queries received by the Universal agent. When you click the **Total Queries** block, a graph (that measures the queries received based on dates) followed by a table with the details of each user query within the selected date range is displayed.

Each row in the table displays the following information:

* **User query**: The user's query.
* **Intent**: The intent corresponding to the user query.&#x20;
* **Intent type**: The intent type corresponding to the intent.
* **Member agent:** The member agent that handled the query.
* **User**: The user name, and the date-time when the user posted the query.
* **Node**: Currently, the node value is always 1 for Universal agents.
* **Channel type**: The type of channel from which the user query was posted.
* **Channel**: The name of the channel.
* **Action**: Click **View Messages** in the **Action** column to view the conversation history corresponding to the user query. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history), for more information.

Click **Download** to download the dashboard in PDF format. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.

### Unhandled queries for Universal agent

The **Unhandled Queries** block displays the total number of queries that were not handled by the agent. When you click on this block, a graph (that measures the unhandled queries received based on dates) followed by a table with the details of each unhandled query within the selected date range is displayed.

Each row in the table displays the following information:

* **User query**: The query that the Universal agent did not handle.
* **Intent**: As this is an unhandled query, the intent is also unhandled.
* **Intent type**: The intent type for all unhandled queries is unhandled.
* **User**: The user name, and the date-time when the user posted the query.
* **Channel type**: The type of channel from which the user query was posted.
* **Channel**: The name of the channel.
* **Action**: Click **View Messages** in the **Action** column to view the conversation history corresponding to the user query. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history), for more information.

Click  **Download** to download the dashboard in PDF format. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.

### Disambiguation queries for Universal Agent

The **Disambiguation Queries** block displays the total number of queries that required the system to provide disambiguation options. When you click on this block, a graph (that measures the disambiguation queries received based on dates) followed by a table with the details of each disambiguation query within the selected date range is displayed.

Each row in the table displays the following information:

* **User query**: The query that required disambiguation.
* **Intent**: As this is a disambiguation query, the intent is also disambiguation.
* **Intent type**: The intent type for all disambiguation queries is disambiguation.
* **User**: The user name, and the date-time when the user posted the query.
* **Channel type**: The type of channel from which the user query was posted.
* **Channel**: The name of the channel.
* **Action**: Click **View Messages** in the **Action** column to view the conversation history corresponding to the user query. See [Conversation history](https://docs.avaamo.com/user-guide/how-to/debug-agents#using-conversation-history), for more information.

Click **Download** to download the dashboard in PDF format. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.

### Channels for Universal Agent

The Channels block displays the channels through which the agent interacted and the percentage of user interaction through each of these channels. When you click this block, a graph (that measures each channel usage) followed by a table with a list of user queries handled by each channel within the selected date range is displayed.

Each row in the table displays the following information:

* **User query**: The query that is handled by a channel.
* **Intent**: The intent corresponding to the user query.&#x20;
* **Intent type**: The intent type corresponding to the intent.
* **Member agent:** The member agent that handled the query.
* **User**: The user name, and the date-time when the user posted the query.
* **Channel type**: The type of channel from which the user query was posted.
* **Channel**: The name of the channel.
* **Action**: Click **View Messages** in the **Action** column to view the conversation history corresponding to the user query. See [Conversation history](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/debug-skill#using-conversation-history), for more information.

Click **Download** to download the dashboard in PDF format. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.

{% hint style="info" %}
**Note**: Currently, the Intent and Intent type is always "Universal Agent Member Intent" for queries that are responded by the member agents of a Universal agent. If you wish to understand the exact Intent and Intent type that matched in the Member agent, then you must refer to the corresponding analytics board of the Member agent or the Conversation history of the Member agent.
{% endhint %}

### Member agent blocks for Universal agent

For each member agent of a Universal agent, a corresponding member agent analytics block is displayed.&#x20;

{% hint style="info" %}
**Note**: Analytics for member agents is displayed even if credentials are invalid or the member agent is deleted. See [Regenerate credentials](https://docs.avaamo.com/user-guide/how-to/configure-agents/deploy/universal-agent#regenerate-credentials) and [Delete member agent](https://docs.avaamo.com/user-guide/how-to/create-universal-agent/manage-member-agents#delete-member-agent), for more information.
{% endhint %}

A member agent's block displays the number of queries handled by the member agent and the number of skills in that member agent.&#x20;

* When you click this box, a graph (that measures the queries handled by the member agent based on dates) followed by a table with the details of each query handled by the member agent within the selected date range is displayed.
* When you click the number of skills, the corresponding member agent is opened is a new tab. The member agent opens in a separate tab if the user has sufficient permissions, else an unauthorized message is displayed.

Each row in the table displays the following information:

* **User query**: The query handled by the member agent.
* **Member agent:** The name of the member agent.
* **User**: The user name and the date-time when the user posted the query.
* **Channel type**: The type of channel from which the user query was posted.
* **Channel**: The name of the channel.
* **Action**: Click **View Messages** in the **Action** column to view the conversation history corresponding to the user query. See [Conversation history](https://docs.avaamo.com/user-guide/build-skills/create-skill/using-dialog-designer/debug-skill#using-conversation-history), for more information.

Click **Download** to download the dashboard in PDF format. See [Download PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/analytics#step-3-download-pdf), for more information.

{% hint style="info" %}
**Note**: Currently, the Intent and Intent type is always "Universal Agent Member Intent" for Universal agents. If you wish to understand the exact Intent and Intent type that matched in the Member agent, then you must refer to the corresponding analytics board of the Member agent or the Conversation history of the Member agent.
{% endhint %}
