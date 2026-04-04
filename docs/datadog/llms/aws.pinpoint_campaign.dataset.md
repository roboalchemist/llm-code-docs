# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.pinpoint_campaign.dataset.md

---
title: Pinpoint Campaign
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Pinpoint Campaign
---

# Pinpoint Campaign

An Amazon Pinpoint Campaign is a resource that defines and manages a messaging campaign used to engage customers across channels such as email, SMS, push notifications, or voice. It includes details like audience segments, message templates, scheduling, and delivery settings. Campaigns help automate targeted communications to improve customer engagement and retention.

```
aws.pinpoint_campaign
```

## Fields

| Title                         | ID   | Type       | Data Type                                                                                                                                                                 | Description |
| ----------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------- |
| _key                          | core | string     |
| account_id                    | core | string     |
| additional_treatments         | core | json       | An array of responses, one for each treatment that you defined for the campaign, in addition to the default treatment.                                                    |
| application_id                | core | string     | The unique identifier for the application that the campaign applies to.                                                                                                   |
| arn                           | core | string     | The Amazon Resource Name (ARN) of the campaign.                                                                                                                           |
| creation_date                 | core | string     | The date, in ISO 8601 format, when the campaign was created.                                                                                                              |
| custom_delivery_configuration | core | json       | The delivery configuration settings for sending the campaign through a custom channel.                                                                                    |
| default_state                 | core | json       | The current status of the campaign's default treatment. This value exists only for campaigns that have more than one treatment.                                           |
| description                   | core | string     | The custom description of the campaign.                                                                                                                                   |
| holdout_percent               | core | int64      | The allocated percentage of users (segment members) who shouldn't receive messages from the campaign.                                                                     |
| hook                          | core | json       | The settings for the AWS Lambda function to use as a code hook for the campaign. You can use this hook to customize the segment that's used by the campaign.              |
| id                            | core | string     | The unique identifier for the campaign.                                                                                                                                   |
| is_paused                     | core | bool       | Specifies whether the campaign is paused. A paused campaign doesn't run unless you resume it by changing this value to false.                                             |
| last_modified_date            | core | string     | The date, in ISO 8601 format, when the campaign was last modified.                                                                                                        |
| limits                        | core | json       | The messaging limits for the campaign.                                                                                                                                    |
| message_configuration         | core | json       | The message configuration settings for the campaign.                                                                                                                      |
| name                          | core | string     | The name of the campaign.                                                                                                                                                 |
| priority                      | core | int64      | Defines the priority of the campaign, used to decide the order of messages displayed to user if there are multiple messages scheduled to be displayed at the same moment. |
| schedule                      | core | json       | The schedule settings for the campaign.                                                                                                                                   |
| segment_id                    | core | string     | The unique identifier for the segment that's associated with the campaign.                                                                                                |
| segment_version               | core | int64      | The version number of the segment that's associated with the campaign.                                                                                                    |
| state                         | core | json       | The current status of the campaign.                                                                                                                                       |
| tags                          | core | hstore_csv |
| template_configuration        | core | json       | The message template that's used for the campaign.                                                                                                                        |
| treatment_description         | core | string     | The custom description of the default treatment for the campaign.                                                                                                         |
| treatment_name                | core | string     | The custom name of the default treatment for the campaign, if the campaign has multiple treatments. A treatment is a variation of a campaign that's used for A/B testing. |
| version                       | core | int64      | The version number of the campaign.                                                                                                                                       |
