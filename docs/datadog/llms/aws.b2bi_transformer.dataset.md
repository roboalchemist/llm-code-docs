# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.b2bi_transformer.dataset.md

---
title: B2B Data Interchange Transformer
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > B2B Data Interchange Transformer
---

# B2B Data Interchange Transformer

The B2B Data Interchange Transformer in AWS B2BI is a resource that defines and manages data transformation logic for business-to-business document exchanges. It allows you to convert documents between different formats, such as EDI and JSON, enabling seamless integration between trading partners. This resource is used to retrieve details about a specific transformer, including its configuration and mapping rules, so that businesses can automate and standardize data exchange workflows.

```
aws.b2bi_transformer
```

## Fields

| Title             | ID   | Type       | Data Type                                                                                                                                                                                                        | Description |
| ----------------- | ---- | ---------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key              | core | string     |
| account_id        | core | string     |
| created_at        | core | timestamp  | Returns a timestamp for creation date and time of the transformer.                                                                                                                                               |
| edi_type          | core | json       | Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents. |
| file_format       | core | string     | Returns that the currently supported file formats for EDI transformations are JSON and XML.                                                                                                                      |
| input_conversion  | core | json       | Returns the InputConversion object, which contains the format options for the inbound transformation.                                                                                                            |
| mapping           | core | json       | Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).                                                                                                              |
| mapping_template  | core | string     | Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.                                                                                        |
| modified_at       | core | timestamp  | Returns a timestamp for last time the transformer was modified.                                                                                                                                                  |
| name              | core | string     | Returns the name of the transformer, used to identify it.                                                                                                                                                        |
| output_conversion | core | json       | Returns the OutputConversion object, which contains the format options for the outbound transformation.                                                                                                          |
| sample_document   | core | string     | Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.                                                                                                              |
| sample_documents  | core | json       | Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.                                                           |
| status            | core | string     | Returns the state of the newly created transformer. The transformer can be either active or inactive. For the transformer to be used in a capability, its status must active.                                    |
| tags              | core | hstore_csv |
| transformer_arn   | core | string     | Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.                                                                   |
| transformer_id    | core | string     | Returns the system-assigned unique identifier for the transformer.                                                                                                                                               |
