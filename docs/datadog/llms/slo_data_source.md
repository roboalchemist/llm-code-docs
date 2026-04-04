# Source: https://docs.datadoghq.com/dashboards/guide/slo_data_source.md

---
title: Graph historical SLO data on Dashboards
description: >-
  Display historical SLO data on dashboards using SLO widgets and timeseries
  visualizations for performance tracking.
breadcrumbs: Docs > Dashboards > Graphing Guides > Graph historical SLO data on Dashboards
---

# Graph historical SLO data on Dashboards

## Overview{% #overview %}

Graph Metric-based and Time Slice SLOs on dashboards and track trends over 15 months. You can also leverage the [scheduled dashboard reporting](https://docs.datadoghq.com/dashboards/sharing/scheduled_reports/) functionality to automatically deliver visual reports to key stakeholders.

## Configuration{% #configuration %}

{% image
   source="https://datadog-docs.imgix.net/images/dashboards/guide/slo_data_type/slo-data-good-bad-events.0fa2d73ab364d42dbac9ccec3550abf2.png?auto=format"
   alt="Graph editor configuration with the slo data type selected and the good events measure selected" /%}

To get started, pick one of the standard visualization types from the dashboard widget tray and select *SLOs* as the data source in the query dropdown menu.

For the *Measure* parameter, see the table below for more information on what each measure visualizes. The *Display* parameter allows you to break out the query by the groups that are already configured for the SLO.

{% callout %}
##### Key Information

When using an SLO data source measures in the Timeseries widget, the value shown at each point is based on the default rollup in the widget, not rolling time period of the SLO.
{% /callout %}

| Measure                | SLO type                    | Timeseries widget                                                                                                                                                                                                     | Scalar widgets                                                                  |
| ---------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Good events            | Metric-based                | The count of good events.                                                                                                                                                                                             | The sum of good events across all groups.                                       |
| Bad events             | Metric-based                | The count of bad events.                                                                                                                                                                                              | The sum of bad events across all groups.                                        |
| Good minutes           | Monitor-based or Time Slice | The count of good minutes.                                                                                                                                                                                            | The sum of good minutes across all groups.                                      |
| Bad minutes            | Monitor-based or Time Slice | The count of bad minutes.                                                                                                                                                                                             | The sum of bad minutes across all groups.                                       |
| SLO status             | All types                   | For each time bucket, the SLO status is calculated as the ratio of the number of good events/minutes to total events/minutes.                                                                                         | The ratio of the number of good events/minutes to total events/minutes.         |
| Error budget remaining | All types                   | For each time bucket, the percentage of error budget remaining. The target for the [primary time window](https://docs.datadoghq.com/service_level_objectives/#configuration) is used in the error budget calculation. | The percentage of error budget remaining at the end of the widget's time frame. |
| Burn rate              | All types                   | For each time bucket, the burn rate shows the observed error rate divided by the ideal error rate.                                                                                                                    | The burn rate over the widget's time frame.                                     |
| Error budget burndown  | All types                   | The error budget burned over time. It starts at 100% (unless there were bad events/minutes within the first time bucket) and decreases with bad events/minutes.                                                       | Error budget burndown is not available in scalar widgets.                       |

#### SLO status corrections{% #slo-status-corrections %}

For SLOs that have [status corrections](https://docs.datadoghq.com/service_level_objectives/#slo-status-corrections), you can enable or disable corrections in charts using the SLO data source. By default, corrections are enabled and applied to the chart; you can disable with the advanced options menu options:

{% video
   url="https://datadog-docs.imgix.net/images/dashboards/guide/slo_data_type/slo-data-source-correction.mp4" /%}

## Further Reading{% #further-reading %}

- [Learn more about Service Level Objectives](https://docs.datadoghq.com/service_level_objectives/)
- [SLO Widget](https://docs.datadoghq.com/dashboards/widgets/slo)
- [SLO List Widget](https://docs.datadoghq.com/dashboards/widgets/slo_list)
