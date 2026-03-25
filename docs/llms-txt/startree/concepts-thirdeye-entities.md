# Source: https://docs.startree.ai/thirdeye/concepts-thirdeye-components/concepts-thirdeye-entities.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# ThirdEye Entities

This page discuss key topics and concepts at a high level and provide useful background information and explanation to help you understand how ThirdEye works, and make it easier for you to use the platform.

The diagram below shows how a new user would interact with ThirdEye:

<img src="https://mintcdn.com/startree/zMiJ17Ik7Xto2JoM/img/thirdeye/_workflow_high_level.png?fit=max&auto=format&n=zMiJ17Ik7Xto2JoM&q=85&s=07edb27ca73caa7df9a2cb98d7ceadda" width="70%" data-path="img/thirdeye/_workflow_high_level.png" />

Let's review the entities and terminology used in this workflow.

In ThirdEye, there are 3 main families of entities: *data*, *alerts*, and *notifications*.

## Data entities

* **Datasource**\
  A connection to a data system. This is where ThirdEye gets the data you want to monitor.\
  Example: an Apache Pinot instance.
* **Dataset**\
  A mapping to a table in a **datasource**.\
  Example: the `orders` table.
* **Metric**\
  A column in a **dataset**, and an associated aggregation function.\
  Example: the `revenue` column with the function `SUM`

## Alert entities

* **Alert** - also called **detection pipeline**\
  A complete anomaly detection rule configuration.\
  Example: create an **anomaly** if `revenue` is bigger than `20000`. Check every hour.
* **Alert template**\
  A detection logic boilerplate that can be used to create *Alert*.\
  Example: create an **anomaly** if `${metric}` is bigger than `{max_value}`.
* **Anomaly**\
  A problem detected by a **detection pipeline**\
  This is what you look at when there is a problem.  An anomaly has a start time and an end time.\
  Example: `revenue` was `30000`, above the threshold of `20000`, on Thursday 3, between 9pm and 10pm.

## Notification entities

* **Notification system**\
  A system where to send alerts.\
  Example: email, Slack.
* **Subscription Group**\
  A list of notification recipients and a list of alerts. Anomalies raised by the alerts are sent to the recipients.\
  Example: email John and Jenny if revenueAlert or userAlert detect an anomaly.

Built with [Mintlify](https://mintlify.com).
