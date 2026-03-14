# Source: https://docs.startree.ai/thirdeye/how-tos/perform-root-cause-analysis.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# How to perform root cause analysis

<Info>
  Before you perform the actions on this page, you must have configured a data source, data set, and created an alert.
</Info>

In this guide we learn how to perform root cause analysis.

## Find anomalies

First, find an anomaly to investigate.

<Info>
  If you received an anomaly email you can skip to the [anomaly chart](#anomaly-chart) section of this guide.
</Info>

Click on the tab on the left menu to view all anomalies. You should see the following screen:

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/anomalies.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=42f6a5f4b7272dace676368454da932e" alt="" width="1590" height="495" data-path="img/thirdeye/anomalies.png" />

Select an anomaly by clicking on the anomaly in the `Name` column. You should then see the following screen:

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/anomaly2.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=918f37eb310545b25da362d326e81b78" width="600px" alt="An anomaly" data-path="img/thirdeye/anomaly2.png" />

  An anomaly
</p>

At the top of the screen is a calendar control that we can use to control the date range shown on the screen.

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/date_select.gif?s=7917eded415d855bda19ba91c1b9577a" width="600px" alt="Date range selection" data-path="img/thirdeye/date_select.gif" />

  Date range selection
</p>

Below is a summary of the anomaly showing a chart of varied values over time.

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/anomaly_chart_view.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=9c1f6f0db07ab04ee77e7e779e83f38b" width="600px" alt="Anomaly Summary" data-path="img/thirdeye/anomaly_chart_view.png" />

  Anomaly Summary
</p>

Finally we have a heatmap at the bottom of the screen that allows us to drill down into the data based on various properties.

<p>
  <img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/heatmap.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=2344078109f5c4840720e3ef8f7a8d85" width="600px" alt="Heatmap" data-path="img/thirdeye/heatmap.png" />

  Heatmap
</p>

## Anomaly chart

Let's have a look at how to use the anomaly chart. The animation below shows how to use the various controls:

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/anomaly-chart2.gif?s=b83d7effdb1c7f9e9736d679d17c2f63" alt="Investigating the anomaly chart" width="80%" data-path="img/thirdeye/anomaly-chart2.gif" />

  Investigating the anomaly chart
</p>

You can update the chart to include add or remove anomalies, upper and lower bounds, as well as the values themselves. You can also zoom in to specific parts of the chart to do further investigation, as shown in the animation below:

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/anomaly-chart-zoom2.gif?s=125c8cf155fff353341a4c017a40b35e" alt="Investigating the anomaly chart" width="80%" data-path="img/thirdeye/anomaly-chart-zoom2.gif" />

  Investigating the anomaly chart
</p>

## Heatmap

Next let's have a look at how to use the heatmap. The heatmap shows how the data has changed compared to the same period seven days ago. You can then drill down by each property to see the current value and the percentage change, as shown in the animation below.

<p>
  <img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/heatmap2.gif?s=5a91d577299c5c2076f80cdc74f9d932" alt="Investigating the heatmap" width="80%" data-path="img/thirdeye/heatmap2.gif" />

  Investigating the heatmap
</p>

In this example, there's been a significant decrease in page views for the Chrome browser. Our next step is to determine what's changed, causing Chrome's page views to decrease.

## Events

You could also ingest events like holiday events and code check-ins, for example, to ThirdEye. Let's have a look at how to create an event.

To view your events, click on the **Events** tab on your Configuration page. You would then see your list of events.

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/events.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=1cd3a33dbe9e2b27aa1d32aeb1f38be9" alt="Events page" width="80%" data-path="img/thirdeye/events.png" />

  Investigating related events
</p>

If you do not have events and want to create an event, click on the **Create** dropdown button and select **Create Event**. For ingesting events in bulk, you could view our API Swagger documentation for available Event API routes to configure event ingestion.

<p>
  <img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/create_event.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=a5e9b12e80b39f919b2f268d93de7480" alt="Create event" width="80%" data-path="img/thirdeye/create_event.png" />
</p>

Built with [Mintlify](https://mintlify.com).
