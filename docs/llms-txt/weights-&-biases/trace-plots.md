# Source: https://docs.wandb.ai/weave/guides/tracking/trace-plots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Use trace plots

> Visualize trace-level metrics with interactive charts in Weave to explore latency, cost, and token usage patterns for LLM applications.

The *trace plots* tool in W\&B Weave allows you to explore, visualize, and debug trace-level metrics (e.g. latency, cost, tokens) using interactive charts. You can use the default trace plots or create your own via the custom trace plot builder.

<Frame>
    <img src="https://mintcdn.com/wb-21fd5541/2zcI9AceqachbiPB/weave/guides/tracking/imgs/plots-example.png?fit=max&auto=format&n=2zcI9AceqachbiPB&q=85&s=08aeba91e08f6fa1e2d0d2d63ae88950" alt="Trace plots in action" width="1590" height="1292" data-path="weave/guides/tracking/imgs/plots-example.png" />
</Frame>

## Get started

1. Navigate to your project's **Traces** page.
2. (Optional) Select **Filter** to filter selected traces (e.g. by datetime or operation).
3. In the upper right hand corner of the **Traces** view, click the **Show Metrics** icon to open the trace plots side pane.

   <img src="https://mintcdn.com/wb-21fd5541/2zcI9AceqachbiPB/weave/guides/tracking/imgs/plots-show-metrics-icon.png?fit=max&auto=format&n=2zcI9AceqachbiPB&q=85&s=b2354dea9b3b4c90f75b5757e3f189a7" alt="The  Show Metrics icon" width="106" height="104" data-path="weave/guides/tracking/imgs/plots-show-metrics-icon.png" />

   From here, you can:

   * View the [default trace plots](#default-trace-plots).
   * Create a [custom trace plots](#create-a-custom-trace-plot).
4. Charts update dynamically based on your trace filters and selections.

## Default trace plots

When you first open the trace plots panel, Weave auto-generates a few trace plots based on your available project trace data:

* Bar chart (cost or latency grouped over time bins)
* Line chart (latency over time)
* Scatter plot (e.g. prompt tokens vs. completion tokens)

Each trace plot is interactive:

* Hover for tooltips
* Drag to zoom
* Double-click to reset
* Click points in scatter plots to open a specific trace

## Create a custom trace plot

You can also create custom trace plot. To create a custom trace plot, do the following:

1. From the trace plots side pane, click **➕ Add Chart** .

   <img src="https://mintcdn.com/wb-21fd5541/2zcI9AceqachbiPB/weave/guides/tracking/imgs/plots-add-chart.png?fit=max&auto=format&n=2zcI9AceqachbiPB&q=85&s=45ab639f4b75b25fcba0ce90d5fc0b8d" alt="➕ Add Chart button." width="282" height="104" data-path="weave/guides/tracking/imgs/plots-add-chart.png" />

2. In the pop-up, select one of the available trace plot types:

   <img src="https://mintcdn.com/wb-21fd5541/2zcI9AceqachbiPB/weave/guides/tracking/imgs/plots-custom-chart-types.png?fit=max&auto=format&n=2zcI9AceqachbiPB&q=85&s=768f5102045f90567abe657a7e43c558" alt="Available custom trace plot types" width="998" height="654" data-path="weave/guides/tracking/imgs/plots-custom-chart-types.png" />

3. For the selected trace plot type, configure your trace plot. For information on configuration options by trace plot type, see [Trace plot settings by plot type](#trace-plot-settings-by-plot-type).

4. Click **Save chart** to save your chart.

### Trace plot settings by plot type

When adding or editing a custom trace plot, the available configuration options vary slightly depending on the selected trace plot type. The table provides a breakdown of the configurable options.

| Setting     | Scatter Plot | Line Chart           | Bar Chart            |
| ----------- | ------------ | -------------------- | -------------------- |
| Y-axis      | ✅ Required   | ✅ Required           | ✅ Required           |
| X-axis      | ✅ Selectable | Fixed (`started at`) | Fixed (`started at`) |
| Grouping    | ✅ Optional   | ✅ Optional           | ✅ Optional           |
| Binning     | ❌ Not used   | ✅ Used               | ✅ Used               |
| Aggregation | ❌ Not used   | ✅ Used               | ✅ Used               |
