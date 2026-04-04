# Source: https://docs.avaamo.com/user-guide/ref/data-retention.md

# Data Retention

Agents in the Avaamo Conversational AI Platform consume a voluminous amount of user data in its lifecycle - right from its inception, to production, and ongoing over a period of years until the agent is active. Data can be in various forms - ranging from simple text descriptions to images, videos, and files. Further, data captured by agents in certain domains, say finance or banking, or healthcare can also be sensitive in nature.&#x20;

Hence, it is critical and essential to manage data appropriately and to define required policies to ensure data security, confidentiality, integrity, and availability. Policies are required at every stage of data in its lifecycle - from the time data is collected and stored to when it must be archived or deleted.&#x20;

One such important policy is **Data retention**. In simple terms, data retention means retaining or storing data for a specific period of time for meeting legal and business data archival requirements. Without a data retention policy, an organization can eventually store unnecessary data for a long period of time, impacting system performance, compromising data availability, and can have a rippling effect on data integrity and security.&#x20;

This article provides describes the data retention policy applicable to the data in the Avaamo Conversational AI platform.

### What is data retention?

Data retention in the Avaamo Conversational AI Platform defines how long data is retained in the platform and what happens to the data once the retention time period for a particular data set expires.

### How long is the data retained?

As a part of Avaamo’s ongoing governance policy, your data is retained for upto 2 years. It is recommended that you plan and set up a process to take required backups of all your production agents to your desired location on a regular basis.

{% hint style="info" %}
**Note**: By default, your data is retained for 2 years. All data older than 2 years are purged. If you wish to retain data for a lesser number of days, then contact Avaamo Support with details about your specific retention requirements.&#x20;
{% endhint %}

### What data is retained and how to take backup?

Data in the following modules are purged. Refer to `How to take backup?` in the following table to take backup as per your requirement:

| Data purged          | How to take backup?                                                                                                                           |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Query insights       | [Query insights API ](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/agent-api/query-insights)                      |
| Analytics            | [Analytics APIs](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api)                                      |
| User journey         | [Download user journey as PDF](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/user-journey#download-user-journey) |
| Conversation History | [Conversation History API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/conversation-message-api)                 |
| JS Errors            | [Export JS Errors to a CSV](https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/js-errors#export-js-errors-to-a-csv-file)     |
| Feedback             | [User feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api)                                    |
| Change Logs          | [Changelog API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/change-log-apis)                                     |
| Messages             | [Message API](https://docs.avaamo.com/user-guide/avaamo-platform-api-documentation/message-api#get-agent-messages)                            |

{% hint style="info" %}
**Notes:** All the data returned from the API is in JSON format.&#x20;
{% endhint %}

### Can this data be recovered in any way?

No, once purged the data is completely deleted from the Avaamo Conversational AI Platform and cannot be recovered.

### What is the format of the data from the API?

All the data returned from the API is in JSON format.
