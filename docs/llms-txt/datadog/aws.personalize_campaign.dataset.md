# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.personalize_campaign.dataset.md

---
title: Personalize Campaign
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Personalize Campaign
---

# Personalize Campaign

An AWS Personalize Campaign is a deployed recommendation engine that delivers personalized predictions in real time based on a trained solution version. It provides an endpoint that applications can call to generate tailored recommendations for users, such as product or content suggestions. Campaigns scale automatically to handle traffic and can be updated with new solution versions to improve accuracy over time.

```
aws.personalize_campaign
```

## Fields

| Title                  | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                     | Description |
| ---------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                   | core | string     |
| account_id             | core | string     |
| campaign_arn           | core | string     | The Amazon Resource Name (ARN) of the campaign.                                                                                                                                                                                                                                                               |
| campaign_config        | core | json       | The configuration details of a campaign.                                                                                                                                                                                                                                                                      |
| creation_date_time     | core | timestamp  | The date and time (in Unix format) that the campaign was created.                                                                                                                                                                                                                                             |
| failure_reason         | core | string     | If a campaign fails, the reason behind the failure.                                                                                                                                                                                                                                                           |
| last_updated_date_time | core | timestamp  | The date and time (in Unix format) that the campaign was last updated.                                                                                                                                                                                                                                        |
| latest_campaign_update | core | json       | Provides a summary of the properties of a campaign update. For a complete listing, call the DescribeCampaign API. The latestCampaignUpdate field is only returned when the campaign has had at least one UpdateCampaign call.                                                                                 |
| min_provisioned_tps    | core | int64      | Specifies the requested minimum provisioned transactions (recommendations) per second. A high minProvisionedTPS will increase your bill. We recommend starting with 1 for minProvisionedTPS (the default). Track your usage using Amazon CloudWatch metrics, and increase the minProvisionedTPS as necessary. |
| name                   | core | string     | The name of the campaign.                                                                                                                                                                                                                                                                                     |
| solution_version_arn   | core | string     | The Amazon Resource Name (ARN) of the solution version the campaign uses.                                                                                                                                                                                                                                     |
| status                 | core | string     | The status of the campaign. A campaign can be in one of the following states: CREATE PENDING > CREATE IN_PROGRESS > ACTIVE -or- CREATE FAILED DELETE PENDING > DELETE IN_PROGRESS                                                                                                                             |
| tags                   | core | hstore_csv |
