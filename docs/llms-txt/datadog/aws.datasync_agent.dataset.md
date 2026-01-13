# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.datasync_agent.dataset.md

---
title: DataSync Agent
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > DataSync Agent
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.datasync_agent.dataset/index.html
---

# DataSync Agent

DataSync Agent is a virtual machine deployed on-premises or in another cloud to enable secure and efficient data transfer between local storage systems and AWS services. It connects to AWS DataSync, handling tasks such as migration, replication, and archiving by accelerating and automating data movement. The agent manages encryption, validation, and performance optimization, reducing manual effort and ensuring reliable transfers at scale.

```
aws.datasync_agent
```

## Fields

| Title                | ID   | Type      | Data Type                                                                                                                                                                                                                                                                                                    | Description |
| -------------------- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                 | core | string    |
| account_id           | core | string    |
| agent_arn            | core | string    | The ARN of the agent.                                                                                                                                                                                                                                                                                        |
| creation_time        | core | timestamp | The time that the agent was activated.                                                                                                                                                                                                                                                                       |
| endpoint_type        | core | string    | The type of service endpoint that your agent is connected to.                                                                                                                                                                                                                                                |
| last_connection_time | core | timestamp | The last time that the agent was communicating with the DataSync service.                                                                                                                                                                                                                                    |
| name                 | core | string    | The name of the agent.                                                                                                                                                                                                                                                                                       |
| platform             | core | json      | The platform-related details about the agent, such as the version number.                                                                                                                                                                                                                                    |
| private_link_config  | core | json      | The network configuration that the agent uses when connecting to a VPC service endpoint.                                                                                                                                                                                                                     |
| status               | core | string    | The status of the agent. If the status is ONLINE, the agent is configured properly and ready to use. If the status is OFFLINE, the agent has been out of contact with DataSync for five minutes or longer. This can happen for a few reasons. For more information, see What do I do if my agent is offline? |
| tags                 | core | hstore    |
