# Source: https://docs.fiddler.ai/observability/platform/monitoring-charts-platform.md

# Monitoring Charts

### Getting Started with Fiddler’s Charts UI

The Chart UI on Fiddler AI’s platform is designed to help you effectively monitor and analyze model performance metrics. Navigating to the Charts tab in the navigation bar allows you to easily access the tools needed to visualize key data and track your LLM and ML models’ performance. Choose to open a previously saved chart for ongoing analysis or create a new one tailored to specific metrics, such as response faithfulness, jailbreak attempts, data drift, and more.

![Plotting traffic on Fiddlers monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-10d07fcafc0a651c0e88c0cd51c67c4f310b760a%2Fbc3648d-image.png?alt=media)

#### Supported Metric Types

Monitoring charts enable you to plot any combination of the following metric types for a given model:

* [**Traffic**](https://docs.fiddler.ai/observability/platform/traffic-platform)
  * Model traffic volume over time provides insights into system usage patterns and overall operational health.
* [**Statistics**](https://docs.fiddler.ai/observability/platform/statistics)
  * Aggregated metrics that monitor trends and changes in your model's data columns
* [**Data Drift**](https://docs.fiddler.ai/observability/platform/data-drift-platform)
  * Data drift occurs when production data differs significantly from training data, potentially degrading model performance and accuracy.
* [**Data Integrity**](https://docs.fiddler.ai/observability/platform/data-integrity-platform)
  * TMonitor three critical data integrity issues: missing values, incorrect data types, and out-of-range values that violate model input requirements.
* [**Performance**](https://docs.fiddler.ai/observability/platform/performance-tracking-platform)
  * Model performance measures how accurately your model accomplishes its intended task, directly impacting business outcomes and decision quality.
* [**Custom Metrics**](https://docs.fiddler.ai/observability/platform/custom-metrics)
  * Build tailored monitoring metrics that align with your specific business rules and success criteria using custom formulas.

### What Are the Key Features and Functions of the Monitoring Chart UI?

#### Multiple Charting Options

You can [plot up to 20 columns](#customizing-columns-for-monitoring-charts) and 6 metric queries for a model enabling you to easily perform model-to-model comparisons and plot multiple metrics in a single chart view.

#### Embedded Root Cause Analytics

Root cause analysis information covers data drift and data integrity, and performance analytics charts for binary classification, multiclass classification, and regression models.

#### Download Your Raw Data for Further Analysis

You can [easily download the raw chart data](#breakdown-summary) to CSV or parquet files. This feature allows you to analyze your data further.

### How to Create a New Monitoring Chart

To create a new monitoring chart, click on the Add Chart button on the Charts page. Search for and select the [project](https://docs.fiddler.ai/reference/glossary#projects) to create the chart, and press Add Chart.

![How to add a new monitoring chart to a project.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-36f65d2a0a9463e303a3089fda49018654410315%2Fperformance_analytics_list.png?alt=media)

#### Save and Share Your Monitoring Chart

Save your chart by clicking the Save button in the chart studio's top right corner. You can then share your chart by copying its link and sending it to other users who have access to the project.

#### Undo and Redo Actions

Easily control the following actions with the undo and redo buttons:

* Metric query selection
* Time range selections
* Bin size selections

To learn how to undo actions taken using the chart toolbar, see the Toolbar information in the next section.

### Exploring Chart Metric Queries & Filters

#### Creating and Managing Metric Queries

Start building your monitoring chart by creating a metric query. First, select a model from your project to analyze. Then, specify which metrics and columns you want to visualize. Note that you can only select models that exist within your current project.

Select the type of metric you want to monitor: Performance, Data Drift, Data Integrity, Statistic, Traffic, or Customer Metric. Then choose specific metrics within that category. For instance, if you're monitoring a binary classification model, you might select Performance metrics and track accuracy over time.

![Analyzing metric queries in your monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-fcd342ce5ca148e03e0cd0d9db22723d07921091%2Fa46e656-image.png?alt=media)

#### Customizing Columns for Monitoring Charts

If you choose to chart data drift or data integrity, you can choose to plot up to 20 different columns from the following column categories: inputs, outputs, targets, metadata, and custom features.

![Adding multiple columns to your chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-7b6e129d9d793966ee569e6fdf1bc6dc06e80421%2F7d91cc8-image.png?alt=media)

#### Adding Multiple Metrics or Models

Add up to 6 metric queries that allow you to chart different metrics from one or more models in a single chart view.

![Adding multiple metrics and/or models to a single chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-0a98f7f4fa984a66511d87706165b96c60ec14fc%2F4213040-image.png?alt=media)

#### Using Chart Filters for Better Analysis

Analyze specific slices of data using three key filtering tools: chart filters, the chart toolbar, and the zoom slider. These tools work together to help you investigate important patterns and trends in your data.

![How to add filters and use capabilities to analyze your monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-112d764cec78ce48eede9d0a35b6ddc975f12f9f%2Ff58936d-image.png?alt=media)

#### Tailored Filters

You can customize your chart view using the date range and bin size filters. The date range can be one of the pre-defined time ranges or a custom range. The bin size selected controls the frequency for which the data is displayed. So selecting Day will show daily data over the date range selected.

Customize your chart's time-based display using the date range and bin size filters. Choose from preset date ranges or define a custom period. The bin size determines how your data is grouped - for example, selecting 'Day' will show daily aggregated data across your chosen date range.

#### Toolbar Functions

The charts toolbar is made up of 5 functions:

* Drag to zoom
* Reset zoom
* Toggle to a line chart
* Toggle to a bar chart
* Undo all toolbar actions

> 📘 Note: If the zoom reset or toolbar undo is selected, this will also undo any actions taken with the zoom slider.

![Toolbar functions in a monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6fb2a76ac0aa02c6c5577af89bd50d16188e1ddd%2F0a9224c-image.png?alt=media)

**Line & Bar Chart Toggles**

Toggle between line and bar chart views using the toolbar icons in the top right corner. While you can freely switch between these visualization types, please note that toolbar settings are temporary and won't be saved with your chart.

![Visualize metrics in bar chart mode.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-79fc3bf2e54efc27e04e6367abe03dbc8e353500%2Fc8c0e79-image.png?alt=media)

**Zoom Slider**

Use the horizontal zoom bar at the bottom of the chart to focus on specific time periods. Select your desired time range by dragging the zoom bar handles, then slide the selected range left or right to analyze different periods. For example, to examine week-by-week data over six months, zoom to your preferred view and drag the range to explore different weeks.

![Focus your analysis in a specific time range.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-948344cfb6bcfb69783320922f592455aa0dd468%2Fc73c24c-image.png?alt=media)

**Breakdown Summary**

You can easily visualize your charts' raw data as a table within the fiddler chart studio, or download the content as a CSV or parquet file for further analysis. If you choose to chart multiple columns, as shown below, you can search for and sort by Model name, Metric name, Column name, or values for a specific date.

![Analyze your chart’s raw data as a table to get a breakdown summary.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-1380b350dc46323cee87101973093b1349f1c8f3%2F0ddc155-image.png?alt=media)

### How to Customize Your Monitoring Chart

#### Adjusting Scale and Range

The Customize tab lets you adjust your chart's y-axis settings to improve data visualization. You can set minimum and maximum values to better utilize chart space, and apply logarithmic scaling to clearly display data with large variations in values.

![Customize the scale and range of the y-axis on your monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-d0836754ba772f730c2968659b58280ebc2e93aa%2F4926dff-image.png?alt=media)

#### Assigning Y-axis for Metric Queries

Select the y-axis for your metric queries with enhanced flexibility to customize the scale and range for each axis.

![Customize the scale and range of each axis on your monitoring chart.](https://3170638587-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F82RHcnYWV62fvrxMeeBB%2Fuploads%2Fgit-blob-6d4349fe145a3954a7136f6c90fd24fcc2b2a93c%2F96f49e0-image.png?alt=media)

### Mastering our Chart UI to Effectively Track LLM and ML Performance

Understanding how to use the chart UI is key to measuring and maintaining the performance of LLM and ML models. Fiddler’s model monitoring tools allow you to track key metrics, identify data drift, and gain valuable insights into model behavior. Customize your Fiddler charts to proactively address issues and ensure models remain accurate, reliable, and high-performing.
