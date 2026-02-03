# Source: https://docs.datadoghq.com/ddsql_reference/data_directory/aws/aws.mediatailor_prefetchschedule.dataset.md

---
title: Mediatailor Prefetchschedule
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > DDSQL Reference > Data Directory > Mediatailor Prefetchschedule
---

# Mediatailor Prefetchschedule

This table represents the mediatailor_prefetchschedule resource from Amazon Web Services.

```
aws.mediatailor_prefetchschedule
```

## Fields

| Title                            | ID   | Type       | Data Type                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Description |
| -------------------------------- | ---- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------- |
| _key                             | core | string     |
| account_id                       | core | string     |
| arn                              | core | string     | The Amazon Resource Name (ARN) of the prefetch schedule.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| consumption                      | core | json       | Consumption settings determine how, and when, MediaTailor places the prefetched ads into ad breaks for single prefetch schedules. Ad consumption occurs within a span of time that you define, called a <i>consumption window</i>. You can designate which ad breaks that MediaTailor fills with prefetch ads by setting avail matching criteria.                                                                                                                        |
| name                             | core | string     | The name of the prefetch schedule. The name must be unique among all prefetch schedules that are associated with the specified playback configuration.                                                                                                                                                                                                                                                                                                                   |
| playback_configuration_name      | core | string     | The name of the playback configuration to create the prefetch schedule for.                                                                                                                                                                                                                                                                                                                                                                                              |
| recurring_prefetch_configuration | core | json       | The settings that determine how and when MediaTailor prefetches ads and inserts them into ad breaks.                                                                                                                                                                                                                                                                                                                                                                     |
| retrieval                        | core | json       | A complex type that contains settings for prefetch retrieval from the ad decision server (ADS).                                                                                                                                                                                                                                                                                                                                                                          |
| schedule_type                    | core | string     | The frequency that MediaTailor creates prefetch schedules. <code>SINGLE</code> indicates that this schedule applies to one ad break. <code>RECURRING</code> indicates that MediaTailor automatically creates a schedule for each ad avail in a live event. For more information about the prefetch types and when you might use each, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/prefetching-ads.html">Prefetching ads in Elemental MediaTailor.</a> |
| stream_id                        | core | string     | An optional stream identifier that you can specify in order to prefetch for multiple streams that use the same playback configuration.                                                                                                                                                                                                                                                                                                                                   |
| tags                             | core | hstore_csv |
