# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.bedrock_data_source.dataset.md

---
title: Bedrock Data Source
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Bedrock Data Source
---

# Bedrock Data Source

This table represents the Bedrock Data Source resource from Amazon Web Services.

```
aws.bedrock_data_source
```

## Fields

| Title            | ID   | Type       | Data Type                                                                                                                                                                                                                     | Description |
| ---------------- | ---- | ---------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key             | core | string     |
| account_id       | core | string     |
| data_source      | core | json       | Contains details about the data source.                                                                                                                                                                                       |
| document_details | core | json       | A list of objects, each of which contains information about the documents that were retrieved.                                                                                                                                |
| next_token       | core | string     | If the total number of results is greater than the <code>maxResults</code> value provided in the request, use this token when making another request in the <code>nextToken</code> field to return the next batch of results. |
| tags             | core | hstore_csv |
