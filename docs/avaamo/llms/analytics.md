# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics.md

# Source: https://docs.avaamo.com/user-guide/monitor/analytics.md

# Analytics

The Avaamo platform includes a built-in Analytics tool that visually represents agent and user interactions. This tool provides valuable insights into user engagement, helping you understand how users interact with your assistant. By leveraging these statistics, you can identify areas for improvement and optimize your agent to better align with your business requirements.

You can view the insights on the Analytics page as shown below:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FoSSKwhTnIQPPBTlVilXQ%2FScreenshot%202025-04-01%20at%2010.28.10%E2%80%AFAM.png?alt=media&#x26;token=d5196ae9-2e61-48e3-aa95-b5e75ceeb00c" alt=""><figcaption></figcaption></figure>

## Select filter criteria

You can filter analytics results using the `Date range` and other `additional filter criteria` such as channel, tags, language, intent type, and Prompt Skill using the `Filter` option.

### Date Range

By default, the date range is a week (7 days) from the current date.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FHsN0W4vj49KcaOhdU0gT%2FScreenshot%202025-04-01%20at%2010.32.03%E2%80%AFAM.png?alt=media&#x26;token=735683d3-3f73-4697-a213-584e0955390c" alt=""><figcaption></figcaption></figure>

* Click the date range to choose from various preset options based on your requirements.
* You can view the Analytics board for the following periods:
  * Yesterday
  * Today
  * Last 7 Days
  * Last 14 Days
  * Last 28 Days
  * Last 90 Days
  * Last 180 Days
* To define a custom period, click `Custom Range` and select the start and end dates. The Analytics board allows you to view up to six months of data.

### Additional filter criteria

Click the filter icon next to the **Engagement** option to select additional filter criteria based on your requirements.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5xeQxgyfp83NDHJxpQbM%2FScreenshot%202025-04-01%20at%2010.32.13%E2%80%AFAM.png?alt=media&#x26;token=956a0fcc-4e9b-44f0-8603-a46973427227" alt=""><figcaption></figcaption></figure>

For each filter criteria, you can `select multiple values` as per your requirement.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FcwUPO9Btz9pbmSPJcUvj%2FScreenshot%202025-04-01%20at%2010.40.49%E2%80%AFAM.png?alt=media&#x26;token=1712863c-d27c-46ca-8db2-fe86323bd4d2" alt=""><figcaption></figcaption></figure>

{% hint style="success" %}
**Key points**:

* If you add multiple values within "a" filter criteria, then each value is an "OR" condition. **Example**: If you select the "Web" channel, "French" and "English" language, then the results displayed are for the selected date range in the "Web" channel" AND the "French" OR "English" language.
* Only active intents are displayed in all the filter criteria.
  {% endhint %}

You can select the following filters:

* **Channel**: A list of the channels which has user queries in the selected date range is displayed.
* **Language**: A list of all the languages which has user queries in the selected date range

  is displayed.
* **Intent type**: A list of types of skills available.
* **Prompt skill**: List of prompt skills available in the agent.
* **Tag:** A list of all the custom tags available in your agent is displayed.

Click **Apply** to apply the filters and to view the results. Click **Clear** to clear all the selected filters.

## View results (Analytics board)

Based on the selected date range and filter criteria, the results are filtered and the data in the corresponding analytics boards are displayed. You can click any one of the blocks for a more detailed view. Note that the same filters selected in the "Analytics" are applied in the detailed view too.

### **Query**

The `Query` analytics board displays the total number of queries received by the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria. You can view a chart displaying the day-wise breakdown of queries received by the agent.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FRNiTl4iZZ6lLwWHjMI1b%2FScreenshot%202025-04-01%20at%2011.15.28%E2%80%AFAM.png?alt=media&#x26;token=df9da692-9535-467e-b4c6-bbbea5324433" alt=""><figcaption></figcaption></figure>

When you click the `chart` in the analytics board `Queries`, a table with a list of user queries in the selected date range is displayed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FAQhKGtHGkuZUDuZWkJl2%2FScreenshot%202025-04-01%20at%2011.19.48%E2%80%AFAM.png?alt=media&#x26;token=0f697a51-0251-4e9f-bba4-ac6df391a929" alt=""><figcaption></figcaption></figure>

1. Each row in the table displays the following details:

**User query**: The user query that matches the search criteria.

**User**: The user with the date and time when the query was posted.

**Skill**: The name of the skill to which the user query belongs.

**Skill type**: Type of skill corresponding to the user query.

**Channel (Channel type)**: Name and the type of channel from which the user query was posted.

**Action**: Click `View Messages` in the `Action` column to view the conversation history corresponding to the user query. See Conversation history, for more information.

2. You can further filter this page by skill type and view data monthly or yearly. Additionally, you can select a custom date range as needed.
3. Click `ellipsis (three dots) -> Advance insights` at the right side of the table to view details in the `Query insights` page. See Query Insights, for more information.
4. You can view the query analytics based on skill type for a specific day by hovering over the day in the chart.

### **Call Sessions**

The `Call Sessions` analytics board displays the total number of call sessions that occurred in the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5kRGcHReIu10cTXKdcRk%2FScreenshot%202025-04-02%20at%206.43.18%E2%80%AFPM%20copy.png?alt=media&#x26;token=671f2334-5a4a-48e0-b2fd-c864ec4c78b5" alt=""><figcaption></figcaption></figure>

### **Text Sessions**

The `Text Sessions` analytics board displays the total number of text sessions that occurred in the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.&#x20;

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fz4o4RMYjV3ORfcs35BcT%2FScreenshot%202025-04-02%20at%206.43.18%E2%80%AFPM.png?alt=media&#x26;token=73b7031e-26d5-49f2-89dc-3b226fb01069" alt=""><figcaption></figcaption></figure>

### **Active Users**

The `Active users` analytics board displays the number of users interacting with the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWZ3Nnmmq5ocayhCYhMt5%2FScreenshot%202025-04-02%20at%206.43.26%E2%80%AFPM.png?alt=media&#x26;token=7d229490-4172-4bf3-a091-ecc34044fa1a" alt=""><figcaption></figcaption></figure>

### **Agent intervention**

The `Live Agent Transfers` analytics board displays the number of conversations transferred to Live Agent in the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FdGPXMy4HgaMv0HwJpVfa%2FScreenshot%202025-04-02%20at%206.43.33%E2%80%AFPM.png?alt=media&#x26;token=fced0182-538d-4f78-84be-c76183fc4cae" alt=""><figcaption></figcaption></figure>

### **Channels**

The `Channels` analytics board displays the percentage of agent-user interaction in different channels the agent is deployed on, for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fivv1GiHHMUYlXCIJvJmT%2FScreenshot%202025-04-02%20at%206.43.39%E2%80%AFPM.png?alt=media&#x26;token=040e1c74-623d-4fa4-a436-d18c4f2e6ef0" alt=""><figcaption></figcaption></figure>

### **Languages**

The `Languages` analytics board displays the percentage of agent-user interaction in different languages the agent is deployed on, for the selected filter criteria.  See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FY2NtlkNx0oHW619fl616%2FScreenshot%202025-04-02%20at%206.43.45%E2%80%AFPM.png?alt=media&#x26;token=79b1e4e8-ee27-4864-98ed-13f60b81cef2" alt=""><figcaption></figcaption></figure>

### **Top Tags**

The `Top tags` page displays the report of the frequently triggered intent-tagged categories across different skill responses for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKC6HpkItKTn7I6Z4bVgx%2FScreenshot%202025-04-02%20at%206.43.57%E2%80%AFPM.png?alt=media&#x26;token=e02f4be2-0464-4b8f-a0ab-ee3ca9cc7afa" alt=""><figcaption></figcaption></figure>

### **Top Prompt Skills**

The `Top Prompt Skills` analytics board displays the report of the frequently triggered Prompt skill intents in the agent for the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FL0HIVjotrDxMEYd9qb3e%2FScreenshot%202025-04-02%20at%206.44.03%E2%80%AFPM.png?alt=media&#x26;token=ab4bbc40-db06-4dc8-b7ab-eaa8a220b4d1" alt=""><figcaption></figcaption></figure>

### **Top Document Searched**

The `Top Documents Searched` widget displays a report of the most frequently searched documents across various skill responses based on the selected filter criteria. See [Select filter criteria](#select-filter-criteria), for more information on the available filter criteria.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FiSPrdo90QCp8iCI0GHkN%2FScreenshot%202025-04-02%20at%206.44.13%E2%80%AFPM.png?alt=media&#x26;token=27096ff2-703c-4861-8fdd-9499b2e58bc0" alt=""><figcaption></figcaption></figure>
