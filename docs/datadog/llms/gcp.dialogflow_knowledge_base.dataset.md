# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.dialogflow_knowledge_base.dataset.md

---
title: Dialogflow Knowledge Base
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Dialogflow Knowledge Base
---

# Dialogflow Knowledge Base

Dialogflow Knowledge Base in Google Cloud is a feature that allows virtual agents to automatically find and deliver answers from structured or unstructured documents. It integrates with Dialogflow agents to enhance conversational responses by referencing FAQs, manuals, or other knowledge sources. This helps improve accuracy and reduces the need for manually defined intents.

```
gcp.dialogflow_knowledge_base
```

## Fields

| Title                | ID   | Type          | Data Type                                                                                                                                                                                             | Description |
| -------------------- | ---- | ------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                 | core | string        |
| ancestors            | core | array<string> |
| datadog_display_name | core | string        |
| gcp_display_name     | core | string        | Required. The display name of the knowledge base. The name must be 1024 bytes or less; otherwise, the creation request fails.                                                                         |
| labels               | core | array<string> |
| language_code        | core | string        | Language which represents the KnowledgeBase. When the KnowledgeBase is created/updated, expect this to be present for non en-us languages. When unspecified, the default language code en-us applies. |
| name                 | core | string        | The knowledge base resource name. The name must be empty when creating a knowledge base. Format: `projects//locations//knowledgeBases/`.                                                              |
| organization_id      | core | string        |
| parent               | core | string        |
| project_id           | core | string        |
| project_number       | core | string        |
| region_id            | core | string        |
| resource_name        | core | string        |
| tags                 | core | hstore_csv    |
| zone_id              | core | string        |
