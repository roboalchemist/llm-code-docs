# Source: https://docs.statsig.com/metrics/local-metrics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Local Metrics

> Create metrics that are scoped to individual experiments or gates without adding them to the project-wide catalog.

## Overview

Local Metrics are metrics that are scoped to an individual config, i.e. a specific experiment or gate. They are created in the context of this config with the goal of being able to capture how that metric trends in the context of that config, without adding that new metric to the Project-wide Metrics Catalog forever more.

## Creating a Local Metric

You can create a Local Metric from two places within your config-

1. **Setup**- As you're setting up your gate or experiment and adding Primary/ Secondary/ Monitoring metrics, you may find that you want to add a metric that doesn't yet exist to your Scorecard. In this scenario, you can simply tap, **+ Create New Local Metric** to enter into the Local Metric creation flow.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/local-metrics/2a249684-56a9-4c63-b2b2-7870efd89b76.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=1331c1f253b0de37fb46d4a93633fb4d" alt="Setup tab showing + Create New Local Metric button" width="1509" height="903" data-path="images/metrics/local-metrics/2a249684-56a9-4c63-b2b2-7870efd89b76.png" />
</Frame>

2. **Pulse**- If you've already started your gate/ experiment rollout, it's not too late to create and add a new Local Metric to your scorecard. From your Scorecard in Pulse, tap **Edit Primary Metrics** (or Secondary/ Monitoring metrics depending on where you want to add your new Local Metric), and then **+ Create New Local Metric**.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/local-metrics/b718c3b7-9696-4af0-bbc5-48fef3cfa1d3.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=3bf3e39effb0e22da307d500db4f2e0f" alt="Pulse scorecard with Edit Primary Metrics and Create New Local Metric options" width="1558" height="1149" data-path="images/metrics/local-metrics/b718c3b7-9696-4af0-bbc5-48fef3cfa1d3.png" />
</Frame>

Entering into the Local Metric creation flow from either entry point will kick off the Local Metric creation wizard. If you're a heavy user of Metrics Explorer, this will feel quite familiar. The wizard allows you to select event(s), add filters, and preview the output values.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/local-metrics/452d9efe-2706-4d47-aee6-48c8f6288e8f.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=3bf99aca4fcf73635f3f685d3592dcd0" alt="Local metric creation wizard with event selection and filters" width="1906" height="1114" data-path="images/metrics/local-metrics/452d9efe-2706-4d47-aee6-48c8f6288e8f.png" />
</Frame>

When you are ready to save your Local Metric, you can choose to save it to either the Primary/ Secondary Metrics section of your Scorecard (for experiments), or the Monitoring Metrics section of your feature gate rollout.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/local-metrics/50bc5742-2f2a-4147-9cb3-70658d6391da.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=7e7c5bfd4614751001483660892d965f" alt="Local metric placement selector for primary scorecard" width="217" height="61" data-path="images/metrics/local-metrics/50bc5742-2f2a-4147-9cb3-70658d6391da.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/xH6BS9VFb4phB4uA/images/metrics/local-metrics/ae3932df-f81b-4fed-9d23-b2b196ac83bc.png?fit=max&auto=format&n=xH6BS9VFb4phB4uA&q=85&s=42c5ae488823c43d892165b127565a3a" alt="Monitoring metrics section showing new local metric entry" width="333" height="141" data-path="images/metrics/local-metrics/ae3932df-f81b-4fed-9d23-b2b196ac83bc.png" />
</Frame>

Once you've created a Local Metric, you can tap on the Local Metric in your Scorecard to view its configuration in the Local Metric wizard.

## Types of Local Metrics

The types of Local Metrics you can create are very similar to Custom Metrics (accessible via the Metrics Tab), with a few exceptions.

Here are the supported types of Local Metrics:

| Metric Type | Description                                                                                                           | Examples                                                    |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------- |
| Event Count | **Total count of events** filtered by the *value* and *metadata* properties of an event type                          | **Add to Cart** event filtered by category type             |
| User Count  | **Number of unique users** that trigger events filtered by the *value* and *metadata* of an event type                | **Active Users** based on their views of a product category |
| Aggregation | **Sum or Average** of the *value* of an event type                                                                    | **Total Revenue**                                           |
| Ratio       | **Rates** (e.g. cart conversion rate, purchase rate),  **Normalized Values** (e.g. sessions per user, items per cart) | **Cart Conversion Rate**, **Sessions per User**             |

The one type of Custom Metric that you cannot (yet) create as a Local Metric are funnels.

## Lifecycle of Local Metrics

By default, Local Metrics are scoped to the config they're created in the context of, and will only live for the lifecycle of that config. This means once you make a decision on your experiment or launch your feature gate, your Local Metric will no longer be computed.

Local Metrics do NOT show up in your Project Metrics Catalog, and are not searchable in top-line search.

While you can't convert a Local Metric into a "global" metric (i.e. a Metrics Catalog metric) today, this conversion flow is coming soon. In the meantime, you can recreate the same metric definition as a Custom Metric in the Metrics Catalog if you want this metric to live on in a more global capacity outside the scope of your gate/ experiment.


Built with [Mintlify](https://mintlify.com).