# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.imagebuilder_infrastructure_configuration.dataset.md

---
title: EC2 Image Builder Infrastructure Configuration
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > DDSQL Reference > Data Directory > EC2 Image Builder Infrastructure
  Configuration
source_url: >-
  https://docs.datadoghq.com/data_directory/aws/aws.imagebuilder_infrastructure_configuration.dataset/index.html
---

# EC2 Image Builder Infrastructure Configuration

EC2 Image Builder Infrastructure Configuration defines the infrastructure settings used when building and testing Amazon Machine Images. It specifies details such as the instance types, subnets, security groups, logging, and key management options required for the image build process. This configuration ensures that image builds run in a controlled and secure environment.

```
aws.imagebuilder_infrastructure_configuration
```

## Fields

| Title                        | ID   | Type   | Data Type                                             | Description |
| ---------------------------- | ---- | ------ | ----------------------------------------------------- | ----------- |
| _key                         | core | string |
| account_id                   | core | string |
| infrastructure_configuration | core | json   | The infrastructure configuration object.              |
| request_id                   | core | string | The request ID that uniquely identifies this request. |
| tags                         | core | hstore |
