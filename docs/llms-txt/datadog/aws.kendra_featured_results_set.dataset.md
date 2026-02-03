# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.kendra_featured_results_set.dataset.md

---
title: Amazon Kendra Featured Results Set
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Amazon Kendra Featured Results Set
---

# Amazon Kendra Featured Results Set

Amazon Kendra Featured Results Set is a configuration that allows you to define specific documents or links to appear at the top of search results for certain queries. It helps highlight important or promoted content, ensuring users see key information first. This feature improves search relevance and user experience by prioritizing curated results.

```
aws.kendra_featured_results_set
```

## Fields

| Title                            | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                       | Description |
| -------------------------------- | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                             | core | string        |
| account_id                       | core | string        |
| creation_timestamp               | core | int64         | The Unix timestamp when the set of the featured results was created.                                                                                                                                                                                                                                                                                                                                                            |
| description                      | core | string        | The description for the set of featured results.                                                                                                                                                                                                                                                                                                                                                                                |
| featured_documents_missing       | core | json          | The list of document IDs that don't exist but you have specified as featured documents. Amazon Kendra cannot feature these documents if they don't exist in the index. You can check the status of a document and its ID or check for documents with status errors using the BatchGetDocumentStatus API.                                                                                                                        |
| featured_documents_with_metadata | core | json          | The list of document IDs for the documents you want to feature with their metadata information. For more information on the list of featured documents, see FeaturedResultsSet.                                                                                                                                                                                                                                                 |
| featured_results_set_id          | core | string        | The identifier of the set of featured results.                                                                                                                                                                                                                                                                                                                                                                                  |
| featured_results_set_name        | core | string        | The name for the set of featured results.                                                                                                                                                                                                                                                                                                                                                                                       |
| last_updated_timestamp           | core | int64         | The timestamp when the set of featured results was last updated.                                                                                                                                                                                                                                                                                                                                                                |
| query_texts                      | core | array<string> | The list of queries for featuring results. For more information on the list of queries, see FeaturedResultsSet.                                                                                                                                                                                                                                                                                                                 |
| status                           | core | string        | The current status of the set of featured results. When the value is ACTIVE, featured results are ready for use. You can still configure your settings before setting the status to ACTIVE. You can set the status to ACTIVE or INACTIVE using the UpdateFeaturedResultsSet API. The queries you specify for featured results must be unique per featured results set for each index, whether the status is ACTIVE or INACTIVE. |
| tags                             | core | hstore_csv    |
