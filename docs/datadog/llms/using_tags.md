# Source: https://docs.datadoghq.com/getting_started/tagging/using_tags.md

---
title: Using Tags
description: Learn how to use tags in Datadog products.
breadcrumbs: Docs > Getting Started > Getting Started with Tags > Using Tags
---

# Using Tags

## Overview{% #overview %}

After [assigning tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/), start using them to filter and group your data in your Datadog platform. Tags can be used to include or exclude data.

When including or excluding multiple tags:

- Include uses `AND` logic
- Exclude uses `OR` logic

## Events{% #events %}

The [Events Explorer](https://docs.datadoghq.com/events/explorer) shows the events from your environment over a specified time period. Use tags to filter the events list and focus on a subset of events. Enter `tags:` followed by a tag to see all the events coming from a host, [integration](https://docs.datadoghq.com/integrations/), or service with that tag. For example, use `tags:(service:coffee-house)` to search for the tag `service:coffee-house`.

To search multiple tags inclusively, separate each tag with OR: `tags:(service:coffee-house OR host:coffeehouseprod)`. To search multiple tags exclusively, separate each tag with AND: `tags:(service:coffee-house AND host:coffeehouseprod)`.

## Dashboards{% #dashboards %}

{% tab title="Assignment" %}
Use tags to filter metrics to display in a [dashboard graph](https://docs.datadoghq.com/dashboards/), or to create aggregated groups of metrics to display. To filter the metrics to display, enter the tag in the **from** text box. This metric displays over all sources that have that particular tag assigned (`service:web-store` in the example below).

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboards_tags_example.b3ead7c2592786de399c6d5af97059e5.png?auto=format"
   alt="Filter metrics in dashboards by adding a tag to the 'from' field, in this example the metric is filtered to 'service:web-store'" /%}

Advanced tag value filtering is also available with boolean filters. The following boolean syntax is supported:

- `NOT`, `!`
- `AND`, `,`
- `OR`
- `key IN (tag_value1, tag_value2,...)`
- `key NOT IN (tag_value1, tag_value2,...)`

Use `AND`, `ORs` to look at a metric across specific tags:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_advanced_tags_AND_OR.b6ba78085ea3488ef833fb0ea76bba45.png?auto=format"
   alt="Boolean Filter with AND/OR" /%}

Use `IN`, `NOT IN` to quickly filter a metric down to specific tags:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_advanced_tags_NOT_IN.807174b918c121baf27bf08b758f62cc.png?auto=format"
   alt="Boolean Filter with IN/NOT IN" /%}

To create an aggregated group using tags, enter the key part of the tag in the **avg by** text box. For example, if you have a timeseries graph showing a metric tagged with the key `service`, such as `service:web-store`, enter `service` in the **avg by** text box to show one line for each `service` tag value. Each line represents the average metric value across all sources that share that `service` tag value.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_group_by_tags.f1df5b9d2a9593f24f36e2cb10220d64.png?auto=format"
   alt="Tags in Dashboards avg by text box" /%}

Tags can also be used to overlay events on the dashboard. This works the same way as in the [Events Explorer](https://docs.datadoghq.com/events/). The matching events are overlaid as vertical bars on the graph. The example below uses `service:web-store`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_event_overlays.73a11c46f7a7d9568fd27215285486a5.png?auto=format"
   alt="Use tags to add Event Overlays in Dashboards" /%}

Use [template variables](https://docs.datadoghq.com/dashboards/template_variables/) to save time switching the **from** tag on graphs in your dashboard. In the example below, `service` is used to represent the `service` tag key. To use the template variable, add the `$service` template variable in the **from** text box of your graph query.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_dynamic_template_variables.de41e0d81571d6a623d50a9c83a61082.png?auto=format"
   alt="Dashboard Template Variables" /%}

{% /tab %}

{% tab title="Examples" %}
Here is an example of tags using the timeseries graph editor. For the first screenshot, no tags have been applied, and the average CPU usage across all hosts is displayed:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_timeseries_graph_editor_no_tags.5703caf4a886495a566d8b5e1d733629.png?auto=format"
   alt="Timeseries graph editor with no tags added" /%}

Next, the editor is updated to include a tag (`region:eastus`) in the **from** text box that enables Datadog to look at CPU usage across the US East region. The `region` tag is used as an example here, but you could use any arbitrary tag sent to your Datadog platform, including `application`, `service`, or `environment`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_timeseries_graph_editor_from_tag.cd24f2a0572d9eb7f069a16de2774853.png?auto=format"
   alt="Timeseries graph editor filtered by the 'region:us-east-1' tag" /%}

Finally, the second empty field (the **avg by** text box) is used to show an individual timeseries line for each `host`. Server CPU is displayed for individual hosts running in the US East region.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/dashboard_timeseries_graph_editor_sumby_tag.204ba0f0672d60f757cc2d4c20501cf4.png?auto=format"
   alt="Timeseries graph editor filtered by 'region:us-east-1' and grouped by 'host'" /%}

If needed, add additional tags to narrow down the scope even furtherâfor example, hosts in `region:eastus` and `env:production`. Tags can be used throughout Datadog and be applied to all core elements (metrics, traces, and logs).
{% /tab %}

## Infrastructure{% #infrastructure %}

To filter the [Host Map](https://docs.datadoghq.com/infrastructure/hostmap/), [Infrastructure List](https://docs.datadoghq.com/infrastructure/), [Containers](https://docs.datadoghq.com/infrastructure/livecontainers/), and [Processes](https://docs.datadoghq.com/infrastructure/process/), enter a tag in the **Filter by** text box at the top of the page. Hosts and containers can be grouped by tag key using the **Group by** text box. If you enter `service` in the group box, you see each service as a group heading.

{% tab title="Host Map" %}
Under this section, use tags to filter or group Hosts:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/hostmaptags.05f17576dfa2730ae92d093ad0350d7e.png?auto=format"
   alt="Host Map Tags" /%}

Or Containers:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/containermaptags.8012170683bcda8f156b1840e0b382a4.png?auto=format"
   alt="Container Map Tags" /%}

{% /tab %}

{% tab title="Infrastructure List" %}
Here are the filter and group by text boxes on the Infrastructure List page:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/infrastructuretags.6977e1929bc546f1594c5bf6b2b52602.png?auto=format"
   alt="Tags in the Infrastructure List" /%}

{% /tab %}

{% tab title="Containers" %}
Here are the filter and group by text boxes on the Live Containers page:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/livecontainertags.dea4505b829f86a6345ef15f3b4b6510.png?auto=format"
   alt="Live Container Tags" /%}

{% /tab %}

{% tab title="Processes" %}
Here are the filter and group by text boxes on the Live Processes page:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/liveprocessestags.2719f5b29ca9f987e7e148c426e8acfc.png?auto=format"
   alt="Live Process Tags" /%}

{% /tab %}

## Monitors{% #monitors %}

To filter monitors and [monitor downtimes](https://docs.datadoghq.com/monitors/downtimes/) by [assigned tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags?tab=monitors), use the search bar or facet checkboxes. The search bar format is `tag:<KEY>:<VALUE>`, for example: `tag:service:coffee-house`. To exclude monitors with a specific tag from your search, use `-`, for example: `tag:-service:coffee-house`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/manage_monitor_tags.db98196bd121aa9c5ad987bd0330cf5d.png?auto=format"
   alt="Filter monitors in the search bar with tags" /%}

**Note**: Monitor tags are different and separate from metric tags. For more information, see the documentation on [Monitor tags](https://docs.datadoghq.com/monitors/manage/#monitor-tags).

When creating a new monitor, use *metric tags* in the:

- **from** text box to limit the monitor scope to only metrics that have those tags.
- **excluding** text box to remove the corresponding metrics from the monitor scope.
- **avg by** text box to transform the monitor into a multi alert monitor on each tag value.

## Metrics{% #metrics %}

Use tags in the [Metrics Explorer](https://docs.datadoghq.com/metrics/explorer/) to filter metrics over tags or display multiple graphs by tag key. The example below graphs a metric over `service:web-store`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/metrics_explorer.f67c5cc672c917a4b91886d483c497bf.png?auto=format"
   alt="A metric graph scoped to an individual tag" /%}

## Integrations{% #integrations %}

Some integrations allow you to optionally limit metrics using tags.

{% tab title="AWS" %}
The [AWS integration tile](https://app.datadoghq.com/account/settings#integrations/amazon-web-services) has the tag filters `to hosts with tag` and `to Lambdas with tag`.

These fields accept a comma separated list of tags (in the form `<KEY>:<VALUE>`) that defines a filter, which is used for collecting your EC2 or Lambda resources. You can use these `<KEY>:<VALUE>` to both include and exclude functions based from monitoring based on tags. To specify that tag should be excluded, add a `!` before the tag key. You can also use wildcards, such as `?` (for single characters) and `*` (for multiple characters).

The filters include resources where any inclusion tag is present by using an `OR` statement. The following example filter collects EC2 instances that contain the tag `datadog:monitored` OR `env:production`:

```text
datadog:monitored,env:production
```

If you specified an exclusion a tag, it takes precedence and forms an `AND` statement. The following example filter collects EC2 instances that contain the tag `datadog:monitored`, OR `env:production`, OR an `instance-type` tag with a `c1.*` value AND NOT a `region:us-east-1` tag:

```text
datadog:monitored,env:production,instance-type:c1.*,!region:us-east-1
```

Read more about AWS tagging in the [EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html) and [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/tagging.html) documentation.
{% /tab %}

{% tab title="Azure" %}
The [Azure integration tile](https://app.datadoghq.com/account/settings#integrations/azure) has the tag filter `Optionally filter to VMs with tag`.

This field accepts a comma separated list of tags (in the form `<KEY>:<VALUE>`) that defines a filter, which is used for collecting metrics from Azure VMs. You can also use wildcards, such as `?` (for single characters) and `*` (for multiple characters). Only VMs that match one of the defined tags are imported into Datadog. The rest are ignored.

VMs matching a given tag can also be excluded by adding `!` before the tag, for example:

```text
datadog:monitored,env:production,!env:staging,instance-type:c1.*
```

{% /tab %}

{% tab title="Google Cloud" %}
The [Google Cloud integration tile](https://app.datadoghq.com/account/settings#integrations/google-cloud-platform) has the tag filter `to hosts with tag`.

This field accepts a comma separated list of GCP labels (in the form `<KEY>:<VALUE>`) that defines a filter, which is used for collecting metrics from GCP. You can also use wildcards, such as `?` (for single characters) and `*` (for multiple characters). Only hosts that match one of the defined labels are imported into Datadog. The rest are ignored.

You can exclude hosts matching a given label by adding `!` before the tag, for example:

```text
datadog:monitored,env:production,!env:staging,instance-type:c1.*
```

Read more about [Creating and managing labels](https://cloud.google.com/compute/docs/labeling-resources) in the Google Cloud documentation.
{% /tab %}

## APM{% #apm %}

{% tab title="Trace Explorer" %}
In the [Trace Explorer](https://docs.datadoghq.com/tracing/trace_explorer/search/), you can filter traces with tags using the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`, for example: `service:coffee-house`. For advanced search, see [Query Syntax](https://docs.datadoghq.com/tracing/trace_explorer/query_syntax/).

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/trace_explorer.1fa1db670a287d8c43074493ac652b7c.png?auto=format"
   alt="Trace Explorer Tags" /%}

{% /tab %}

{% tab title="Service Map" %}
After [assigning tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/), use the Service Map to navigate to different areas of the application by clicking on a particular service. In the example below, view [Analytics](https://docs.datadoghq.com/tracing/app_analytics/search/), [Monitors](https://docs.datadoghq.com/monitors/manage/), [Logs](https://docs.datadoghq.com/logs/explorer/search/), and the [Host Map](https://docs.datadoghq.com/infrastructure/hostmap/) filtered by the tag `service:coffee-house`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/servicemaptags.95202d0fffa46788c5780146bd02528d.png?auto=format"
   alt="Service Map Tags" /%}

{% /tab %}

## Notebooks{% #notebooks %}

When creating a [Notebook](https://docs.datadoghq.com/notebooks/) graph, limit metrics by using tags in the **from** text box. Additionally, group metrics by using tags in the **avg by** text box. In the example below, metrics are limited to `service:coffee-house` and grouped by `host`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/notebooktags.e665a2e448ef9994acebc5db49f44042.png?auto=format"
   alt="Notebook Tags" /%}

To exclude tags, use `</>` to edit the text then add the tag in the form `!<KEY>:<VALUE>`. In the example below, `service:coffeehouse` is excluded using `!service:coffeehouse`.

{% video
   url="https://datadog-docs.imgix.net/images/tagging/using_tags/notebooktagsexclude.mp4" /%}

## Logs{% #logs %}

For Logs [Search](https://docs.datadoghq.com/logs/explorer/search/), [Analytics](https://docs.datadoghq.com/logs/explorer/analytics/), [Patterns](https://docs.datadoghq.com/logs/explorer/patterns/), and [Live Tail](https://docs.datadoghq.com/logs/live_tail/), filter logs with tags using the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`, for example: `service:coffee-house`. For advanced search, see [Search Logs](https://docs.datadoghq.com/logs/explorer/search/).

Additionally, tags are used to filter a logs [Pipeline](https://docs.datadoghq.com/logs/log_configuration/pipelines). For example, if you only want logs from the coffee-house service to go through the pipeline, add the tag `service:coffee-house` to the filter field.

## RUM & Session Replay{% #rum--session-replay %}

The [RUM Explorer](https://docs.datadoghq.com/real_user_monitoring/explorer/) visualizes events from your environment over a specified time period.

To filter RUM event data by tags, use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`, for example: `service:shopist`. For advanced search, see [Search RUM Events](https://docs.datadoghq.com/real_user_monitoring/explorer/search/).

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/rumtags.94b90f19f65877f138eeb47c7692dde2.png?auto=format"
   alt="RUM Tags" /%}

## Synthetics{% #synthetics %}

{% tab title="Synthetic Tests" %}
The [Synthetic Tests](https://app.datadoghq.com/synthetics/tests) page lists your Synthetic tests.

To filter tests by tags, use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`. For example: `tag:mini-website`. For advanced search, see [Search and Manage Synthetic Tests](https://docs.datadoghq.com/synthetics/search/).

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/syntheticstags.a5d080053d1b3838dc1ec6ffb46fdb4a.png?auto=format"
   alt="Synthetics Tags" /%}

{% /tab %}

{% tab title="Explorer" %}
The [Synthetic Monitoring & Testing Results Explorer](https://app.datadoghq.com/synthetics/explorer/) displays your test runs and batches of runs in a [CI pipeline](https://docs.datadoghq.com/continuous_testing/cicd_integrations).

To filter test runs by tags, use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`. For example: `@ci.provider.name:github`. For advanced search, see [Search Test Batches](https://docs.datadoghq.com/continuous_testing/explorer/search/).

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/syntheticscitags.47cbf195fbab795f3ed3f3a5752fbf9d.png?auto=format"
   alt="Synthetics and CI Tags" /%}

{% /tab %}

## Service level objectives{% #service-level-objectives %}

{% tab title="Manage SLOs" %}
To filter SLOs by [assigned tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/?tab=servicelevelobjectives#ui), use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`, for example: `journey:add_item`. To exclude SLOs with a specific tag from your search, use `-`, for example: `-journey:add_item`.

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/manage_slo_tags.e8b6c652c3a3abe05673fe76ef72c402.png?auto=format"
   alt="SLO Tags" /%}

SLO tags are different and separate from metric or monitor tags used in the underlying metrics or monitors of an SLO.
{% /tab %}

{% tab title="Metric-based SLOs" %}
When creating a [metric-based SLO](https://docs.datadoghq.com/service_level_objectives/metric/), use metric tags in the SLO's success ratio metric queries (all metrics must use the same set of metric tags):

- **from** text box to limit the metric scope to only those tags.
- **sum by** text box to create a grouped metric-based SLO that display a status percentage and remaining error budget for both the overall SLO and for each tag value.

{% /tab %}

{% tab title="Monitor-based SLOs" %}
When creating a [monitor-based SLO](https://docs.datadoghq.com/service_level_objectives/monitor/) using a single [grouped monitor](https://docs.datadoghq.com/getting_started/tagging/using_tags/?tab=newmonitor#monitors), use the **Calculate on selected groups** toggle to select up to 20 tag values from the underlying monitor to display a status percentage and remaining error budget for both the overall SLO and for each tag value:

{% image
   source="https://datadog-docs.imgix.net/images/tagging/using_tags/monitor_based_slo_tags.ca25a183b7aca3a3f1b4184d52f4a1a0.png?auto=format"
   alt="Monitor-based SLO Tags" /%}

{% /tab %}

## CI Visibility{% #ci-visibility %}

{% tab title="Test Runs" %}
The [CI Visibility Explorer](https://app.datadoghq.com/ci/test-runs) displays your test runs run in a CI pipeline.

To filter test runs by tags, use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`. For example: `@test.status:failed`. For advanced search, see [Test Optimization Explorer Search Syntax](https://docs.datadoghq.com/tests/explorer/search_syntax).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/test_runs.881454a4e4fe1f544cc2be02771dda8a.png?auto=format"
   alt="Test runs in the CI Visibility Explorer" /%}

{% /tab %}

{% tab title="Pipeline Executions" %}
The [CI Visibility Explorer](https://app.datadoghq.com/ci/pipeline-executions) displays your CI pipeline executions.

To filter pipeline executions by tags, use the search bar or facet checkboxes. The search bar format is `<KEY>:<VALUE>`. For example: `@ci.provider.name:gitlab`. For advanced search, see [Search and Manage CI Pipelines](https://docs.datadoghq.com/continuous_testing/explorer/search/).

{% image
   source="https://datadog-docs.imgix.net/images/continuous_integration/pipeline_executions.0b9a180b3d1b18d883713153bbeab355.png?auto=format"
   alt="Pipeline executions in the CI Visibility Explorer" /%}

{% /tab %}

## DORA Metrics{% #dora-metrics %}

The [DORA Metrics Explorer](https://app.datadoghq.com/ci/dora) displays your DORA Metrics aggregations. To filter the displayed metrics and aggregations by tags, use the `+ Filter` button to add facets for existing tags. For querying with tags in graphs and dashboards, see [DORA Metrics Create Custom Dashboards](https://docs.datadoghq.com/dora_metrics/#create-custom-dashboards).

{% image
   source="https://datadog-docs.imgix.net/images/dora_metrics/dora_ui_3.1c02efe2d644b5baafe7caa0de0678cf.png?auto=format"
   alt="An overview of DORA Metrics calculations filtered by the Language custom tag" /%}

## Developers{% #developers %}

Tags can be used in various ways with the [API](https://docs.datadoghq.com/api/).

See this list for links to respective sections:

- [Schedule monitor downtime](https://docs.datadoghq.com/api/v1/downtimes/#schedule-a-downtime)
- [Query the event explorer](https://docs.datadoghq.com/api/v1/events/#query-the-event-stream)
- [Search hosts](https://docs.datadoghq.com/api/v1/hosts/)
- Integrations for [AWS](https://docs.datadoghq.com/api/v1/aws-integration/) and [Google Cloud](https://docs.datadoghq.com/api/v1/gcp-integration/)
- [Querying timeseries points](https://docs.datadoghq.com/api/v1/metrics/#query-timeseries-points)
- [Get all monitor details](https://docs.datadoghq.com/api/v1/monitors/#get-all-monitor-details)
- [Mute a monitor](https://docs.datadoghq.com/api/v1/monitors/#mute-a-monitor)
- [Monitors search](https://docs.datadoghq.com/api/v1/monitors/#get-all-monitor-details)
- [Monitors group search](https://docs.datadoghq.com/api/v1/monitors/#get-all-monitor-details)
- [Create a Screenboard](https://docs.datadoghq.com/api/v1/dashboards/#create-a-new-dashboard)
- [Create a Timeboard](https://docs.datadoghq.com/api/v1/dashboards/#create-a-new-dashboard)
- [Create a SLO](https://docs.datadoghq.com/api/v1/service-level-objectives/#create-a-slo-object)
- [Get a SLO's details](https://docs.datadoghq.com/api/v1/service-level-objectives/#get-a-slos-details)
- [Update a SLO](https://docs.datadoghq.com/api/v1/service-level-objectives/#update-a-slo)

## Further Reading{% #further-reading %}

- [Best practices for tagging your infrastructure and applications](https://www.datadoghq.com/blog/tagging-best-practices/)
- [Getting started with tags](https://docs.datadoghq.com/getting_started/tagging/)
- [Learn how to assign tags](https://docs.datadoghq.com/getting_started/tagging/assigning_tags/)
