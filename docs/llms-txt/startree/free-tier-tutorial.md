# Source: https://docs.startree.ai/thirdeye/getting-started/free-tier-tutorial.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Getting Started with ThirdEye

This tutorial is a great place to start if this is your first time using ThirdEye. We’ll be using a sample PageViews dataset to explore all the different features and tools of ThirdEye.

### What you will accomplish in this tutorial

1. Adding a sample dataset to ThirdEye
2. Creating an alert on a metric in the sample dataset
3. Configuring anomaly notifications
4. Viewing an anomaly
5. Performing a root cause analysis

### Prerequisites

To start, [contact StarTree](https://startree.ai/demo) for details on getting ThirdEye.

## Bringing your data into ThirdEye

When you access ThirdEye for the first time, you’ll be taken to a welcome screen.

This welcome flow will walk you through the two primary steps to get you started with Thirdeye. The first step is to connect your data source and onboard your datasets to ThirdEye.

On the first screen select StarTree Cloud, as we’ll onboard a dataset from the Apache Pinot database from the trial.

Next, select the ‘eCommerce Website PageViews’ dataset under the Sample Datasets section. ThirdEye will add this dataset to the StarTree Cloud Apache Pinot database for you.

The dataset is a sample dataset of an ecommerce company that is recording versions and views of
its checkout page. This is a key metric for the ecommerce company that uses this as a marker to track sales and revenue of the business.

## Creating your alert

Next after onboarding your dataset, select the second step to create your first alert. You’re taken
to an alert wizard that will guide you through the steps to create an alert.

<Info>
  What is an alert?\
  Alerts are the rules you build to detect anomalies in your metrics. ThirdEye gives you a variety of
  templates and algorithms to model your metric and its patterns. When the metric falls out of the range of the model you select, ThirdEye alerts you of the anomaly.
</Info>

Select the dataset we onboarded ‘demo\_pageviews’, then select ‘views’ as the metric. ‘views’ is one of the columns in the dataset that we will monitor as a metric for anomalies.

<Info>
  What is a metric?

  In Startree ThirdEye, a Metric refers to a column in your dataset or a statistic derived from the data that is tracked within ThirdEye.
  In this context, a Metric is typically a specific measure or KPI (Key Performance Indicator) that is important for monitoring the health
  and performance of your business. For example, a Metric could represent things like:

  1. Business KPIs (e.g., revenue, transaction volume)
  2. App Behaviors (e.g. log-ins, errors)
  3. Cloud spend
  4. Networking traffic
</Info>

Select `SUM` as the aggregation function, and select daily granularity. For this alert and the options
we set so far, ThirdEye will sum the views coming into the table every day.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/alert_creation_wizard.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=e89659a7bae49bce2ef5b331e63362d2" alt="ThirdEye Alert Creation Wizard" width="2730" height="1546" data-path="img/thirdeye/free_tier_getting_started/alert_creation_wizard.png" />

## Selecting your detection algorithm

Next, we need to select the model that will fit the views data in order to detect anomalies. Luckily we
have a Detection Algorithm Recommender that will search through and fit all the possible algorithms ThirdEye offers to find the best one.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/detection_algorithm_selection.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=ca7bce86d714da7f440fec6871f6d723" alt="ThirdEye Detection Algorithm Selection" width="2994" height="834" data-path="img/thirdeye/free_tier_getting_started/detection_algorithm_selection.png" />

The alert recommender looks through the historical data of the alert to see which of our
models best fits this pattern of data. When the dimension recommender is ready, choose the
StarTree-ETS option 1 from the recommended configurations. You can see how the model predicts
the pattern, and where it detects the anomalies where the red dots are. On the legend of the
graph, select the ‘Upper and Lower bound’ legend item to add the ranges of the model shown below.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/detection_algorithm_selection_recommended.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=a675137f44523c6592396588dbc3d92c" alt="ThirdEye Detection Algorithm Recommender" width="2638" height="1408" data-path="img/thirdeye/free_tier_getting_started/detection_algorithm_selection_recommended.png" />

## Configure Notifications

When an anomaly shows up in your dataset, it’s important to be notified when it happens.
Let’s set up a notification group – which we can use to configure ThirdEye to send notifications
when anomalies happen.

Click on the toggle button to configure notifications, and select ‘Create a new notification group for this alert’. Let’s set up email notifications for the anomalies that occur. Fill out the form with a subscription group name and your email address that you want alerts to go to. By default, only new anomalies will be notified, but since this is a sample dataset from 2020 we will enable ‘Notify Historical Anomalies’ to receive the notifications for this dataset. For now let’s leave the other fields at their default values.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/notification_configuration.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=8c50bf35538aaf648be2d2cfbe20b34b" alt="Recommended detection algorithm" width="1560" height="1646" data-path="img/thirdeye/free_tier_getting_started/notification_configuration.png" />

Feel free to add more emails or configure more alerts to the other supported platforms like PagerDuty, Slack or to your custom applications.

## Finish creating your alert

Click ‘Create Alert’, and on the modal, name your alert and keep the default schedule settings.
These schedule settings means that ThirdEye will run the detection on the previous day’s
data at 5 AM every day to report the anomalies that appeared. Let’s leave the default as is.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/alert_finish.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=1674f9b5359ae9861933a14e21e30629" alt="Confirmation modal for alert creation" width="1454" height="1340" data-path="img/thirdeye/free_tier_getting_started/alert_finish.png" />

## Viewing your anomalies

After creating your alert, you’re taken to the Alert page. The page will update automatically
with the anomalies you saw on the Alert Creation screen. When the page updates, click on the
latest anomaly. This is the red point lower and further right than the other.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/alert_page.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=90bc39b96a79342be95857d04003d470" alt="Viewing anomalies on the alert page" width="1910" height="1066" data-path="img/thirdeye/free_tier_getting_started/alert_page.png" />

You should be taken to a page like this:\
<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/anomaly_page.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=ff9aa79349e634c7178d9d60b8206fb4" alt="Anomaly page" width="2592" height="966" data-path="img/thirdeye/free_tier_getting_started/anomaly_page.png" />

On this page, we can confirm whether we have a true anomaly or not. Ultimately, ThirdEye can only estimate what the monitored metric should be, so sometimes ThirdEye might miss true anomalies or detect false positives.

Let’s investigate this anomaly to see whether it's a true anomaly or not.
Select ‘Investigate Anomaly’ to see further and perform a root cause analysis (RCA).

<Info>
  What is root cause analysis?\
  Root cause analysis in anomaly detection aims to identify the underlying factor(s) responsible for
  unusual patterns or behavior in data. It goes beyond simply flagging anomalies and seeks to
  pinpoint why those anomalies occurred, guiding future corrective actions or system improvements.
</Info>

## Perform a root cause analysis

After selecting to investigate the anomaly, you should be taken to an Investigation
page to perform a RCA on the anomaly. You should see a page like the one below:

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/investigation_page.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=8dfe1352e121779b7d199927862424bd" alt="RCA investigation page" width="3110" height="1032" data-path="img/thirdeye/free_tier_getting_started/investigation_page.png" />

On this page we have two RCA visualizations, Top Contributors and Heatmap and Dimension Drills.
Top Contributors show what other fields and combinations of those fields in your dataset had
drastic changes. Heatmap and Dimension Drills will show the distribution of different fields and
their values and how those changed.

You may be wondering what these two visualizations are comparing to? That’s a great question.
ThirdEye compares the data at the time of the anomaly to the same time one week prior.
If your data doesn’t have a weekly pattern, you can change the time interval to check against in the
dropdown at the top of the page. The dropdown is shown below, and you can choose to compare
the data from one day, week, month, or year ago against the data at the time of the anomaly.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/rca_baseline_picker.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=c24a1a2375852e23e22fec213f7ba66d" alt="RCA investigation page baseline picker" width="1428" height="144" data-path="img/thirdeye/free_tier_getting_started/rca_baseline_picker.png" />

For now, let’s stick with comparing the data from a week ago, and let’s take a look at the two visualizations.

## RCA Visualizations

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/rca_top_contributors.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=46fa8652c116d44c0e75cd6bf3df2a09" alt="RCA top contributors" width="2532" height="772" data-path="img/thirdeye/free_tier_getting_started/rca_top_contributors.png" />

Looking at the Top Contributors, we can see that, compared to a week ago, there was a drop in views on the chrome browser, on version 0.3, and on the mobile (phone) version. There was also a smaller drop in views on the same browser and version, but on desktops. Could this version, browser type and devices be the root causes of the anomaly?

Take a look at the Heatmap and Dimension Drills. This takes a look of the data from a different
angle and shows you for each column of your data, how did the makeup of the different values in
that column change? Blue indicates increases in field values, red indicates decreases in field
values, darker colors indicate larger changes, and lighter colors indicate smaller changes.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/rca_heatmap.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=e6ddcb58f0b8a71bff61bfea1de6c8f5" alt="RCA heatmap" width="2550" height="990" data-path="img/thirdeye/free_tier_getting_started/rca_heatmap.png" />

Looks like there was a 320,000 decrease in chrome browser views and a 40% decrease in chrome browser views compared to other browser views. Seems like we’re getting a better understanding now of what was causing this anomaly.

## Saving the Investigation

Next, after taking a closer look at the two RCA visualizations, let’s save our investigation.

Optionally, you can add dimensions to your Investigation Preview at the bottom. The Investigation
Preview at the bottom will update with graphs of the dimensions you choose.

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/saving_investigation.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=e015aa750b8523adf641628ce768a36d" alt="RCA saving the investigation" width="2512" height="1046" data-path="img/thirdeye/free_tier_getting_started/saving_investigation.png" />

Click next, and advance to the Preview Investigation page. Here you can optionally define
anomalous events. These are special days that lead to irregular behavior of your metrics. For an
eCommerce company, this could be Black Friday, Christmas Day, etc. We are going to skip this
feature of ThirdEye for now and keep going to the next page.

You should now be on the Review Investigation Page. Here let’s name our investigation and add some notes in the comments about what we found from the RCA page. Fill out something like what is shown below and save your investigation!

<img src="https://mintcdn.com/startree/ydxOgkfeGyqN5wki/img/thirdeye/free_tier_getting_started/reviewing_investigation.png?fit=max&auto=format&n=ydxOgkfeGyqN5wki&q=85&s=6af8c8a43f6952b31905001775e23850" alt="RCA reviewing the investigation" width="2510" height="1404" data-path="img/thirdeye/free_tier_getting_started/reviewing_investigation.png" />

## Confirming your anomaly

After saving the investigation, confirm to ThirdEye that an anomaly has been found.
ThirdEye takes the feedback for true positive anomalies and false positive anomalies and tunes
the model accordingly to give you more accurate results.

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/free_tier_getting_started/confirming_anomaly.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=9474e7e37827d12ba45b4be57689c072" alt="RCA confirm anomaly" width="2504" height="1194" data-path="img/thirdeye/free_tier_getting_started/confirming_anomaly.png" />

## Conclusion

And that’s it! That concludes your ThirdEye tutorial. You went through setting up an alert on a metric, setting up notifications, finding anomalies, and finally investigating an anomaly to find out what the potential business issue is!

Next, try connecting some live data and see for yourself how ThirdEye can save your business
time and money.

Built with [Mintlify](https://mintlify.com).
