# Source: https://docs.statsig.com/metrics/deprecate-event-dau.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Deprecating Event_dau Metric

> Important changes to auto-generated event_dau metrics and how to maintain DAU tracking for your events.

### Deprecation Details

From Wednesday, October 16, 2024, we will stop auto-generating new event\_dau metrics for incoming events into Statsig. We will continue to auto-generate an event\_count metric for each logged event as we do today. **Note: This change will only affect Statsig Cloud customers, Warehouse Native customers will not be impacted.**

* Any existing event\_dau metrics that have been used in a gate, experiment, dashboard, other Custom Metrics will NOT be affected by this change.

* Existing event\_dau metrics that have been archived or never been used in another config will NO longer exist. See ‘Next Steps’ if you want to retain these metrics.

* Going forward, new event\_dau metrics will need to be created manually as a Custom Metric. See [this guide](/metrics/custom-dau) to learn how to create a DAU metric.

If you have any questions or concerns, please don’t hesitate to reach out!

### Motivation for This Change

Historically, we have auto generated an event\_count and event\_dau metric for every incoming event into Statsig. After working closely with hundreds of customers, we have seen that auto generating two metrics for every event causes confusion and clutter inside projects. The proposed change will lead to cleaner Metrics Catalog and faster Console performance, while still retaining your ability to create event\_dau metrics for the events you care about most.

### Next steps

If you wish to keep any unused event\_dau metrics going forward, you can earmark those metrics by performing any of the actions below:

* Adding a Tag (RECOMMENDED)
* Adding a description
* Referencing in a gate/experiment/dashboard

These actions will mark your unused metric as active, signaling us that you don’t want them to be deprecated.


Built with [Mintlify](https://mintlify.com).