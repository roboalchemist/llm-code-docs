# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/gcp/gcp.healthcare_hl7_v2_store.dataset.md

---
title: HL7v2 Store
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > HL7v2 Store
---

# HL7v2 Store

HL7v2 Store in Google Cloud is a managed service within Cloud Healthcare API that allows secure storage, management, and exchange of HL7v2 messages. It enables healthcare systems to ingest, parse, and query HL7v2 data while maintaining compliance with healthcare data standards. The service integrates with other GCP tools for analytics, transformation, and interoperability.

```
gcp.healthcare_hl7_v2_store
```

## Fields

| Title                    | ID   | Type          | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | Description |
| ------------------------ | ---- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                     | core | string        |
| ancestors                | core | array<string> |
| datadog_display_name     | core | string        |
| labels                   | core | array<string> | User-supplied key-value pairs used to organize HL7v2 stores. Label keys must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: \p{Ll}\p{Lo}{0,62} Label values are optional, must be between 1 and 63 characters long, have a UTF-8 encoding of maximum 128 bytes, and must conform to the following PCRE regular expression: [\p{Ll}\p{Lo}\p{N}_-]{0,63} No more than 64 labels can be associated with a given store.                                                                                                                            |
| name                     | core | string        | Identifier. Resource name of the HL7v2 store, of the form `projects/{project_id}/locations/{location_id}/datasets/{dataset_id}/hl7V2Stores/{hl7v2_store_id}`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| notification_configs     | core | json          | Optional. A list of notification configs. Each configuration uses a filter to determine whether to publish a message (both Ingest & Create) on the corresponding notification destination. Only the message name is sent as part of the notification. Supplied by the client.                                                                                                                                                                                                                                                                                                                                                               |
| organization_id          | core | string        |
| parent                   | core | string        |
| parser_config            | core | json          | Optional. The configuration for the parser. It determines how the server parses the messages.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| project_id               | core | string        |
| project_number           | core | string        |
| region_id                | core | string        |
| reject_duplicate_message | core | bool          | Optional. Determines whether to reject duplicate messages. A duplicate message is a message with the same raw bytes as a message that has already been ingested/created in this HL7v2 store. The default value is false, meaning that the store accepts the duplicate messages and it also returns the same ACK message in the IngestMessageResponse as has been returned previously. Note that only one resource is created in the store. When this field is set to true, CreateMessage/IngestMessage requests with a duplicate message will be rejected by the store, and IngestMessageErrorDetail returns a NACK message upon rejection. |
| resource_name            | core | string        |
| tags                     | core | hstore_csv    |
| zone_id                  | core | string        |
