# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/dd/dd.host_gpu_agents.dataset.md

---
title: Host GPU Agents
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Host GPU Agents
---

# Host GPU Agents

The Host GPU Agents table populates some of the Agent-related fields in the `Resource Catalog` product in DataDog.

```
dd.host_gpu_agents
```

## Fields

| Title                    | ID                       | Type | Data Type | Description                                                              |
| ------------------------ | ------------------------ | ---- | --------- | ------------------------------------------------------------------------ |
| Key                      | _key                     | core | string    | Unique identifier for the host GPU agent record.                         |
| Devices                  | devices                  | core | string    | GPU devices information associated with the host.                        |
| Display Name             | display_name             | core | string    | Human-readable display name for the host GPU agent.                      |
| External ID              | external_id              | core | string    | External identifier for the host GPU agent.                              |
| First Seen At            | first_seen_at            | core | timestamp | Timestamp when the host GPU agent was first detected.                    |
| Hostname                 | hostname                 | core | string    | Hostname of the machine where the GPU agent is running.                  |
| Modification Detected At | modification_detected_at | core | timestamp | Timestamp when a modification was last detected for this host GPU agent. |
