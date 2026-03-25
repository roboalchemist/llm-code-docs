# Source: https://docs.statsig.com/statsig-warehouse-native/configuration/metric-examples.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Metric Examples

For customers transitioning from other Warehouse Native Vendors, the format of metrics should be similar and generally customers have been able to use APIs to fetch remote configurations, translate them, and post them to Statsig without issue.

For customers migrating from in-house systems, there may be gaps in translation between how they think about experiment metrics and how Statsig handles them. This page is intended as a collection of common use cases and how they're handled in Statsig.

## Average User Revenue from a Wide Table

In many cases, companies will have a primary source-of-truth table about user engagement with one row per user-day and many columns representing actions taken or other values. This is very easy to integrate with Statsig.

First, enter the table path and optionally a partition column to use for date partitioning:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_configuration.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=b947a5790765b5c16ade86a284f554cb" alt="Metric source setup specifying table path and date partition" width="3072" height="1088" data-path="images/whn/metric_examples_configuration.png" />
</Frame>

Then, configure your timestamp field and ID types. Add any custom SQL aliases for other users, e.g. dividing revenue by 100 to convert from cents to dollars.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_initials.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=d6a1a60d0d7549964e2a2d1bfde2324d" alt="Timestamp and ID type configuration with revenue alias" width="3024" height="1596" data-path="images/whn/metric_examples_initials.png" />
</Frame>

Go to the metrics tab, press create, configure your name/source, and then configure a sum metric on the column with the revenue value.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_create_revenue.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=f5bb995af9b5c71f8254ad89d45abf39" alt="Create metric dialog selecting revenue source" width="1004" height="592" data-path="images/whn/metric_examples_create_revenue.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_configure_revenue.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=2efc732d8d1b3d39f001ae9b037eea88" alt="Sum metric configuration for revenue column" width="1718" height="1622" data-path="images/whn/metric_examples_configure_revenue.png" />
</Frame>

### How it works in experiments

First, Statsig aggregates each unit-level record across the days they are enrolled in the experiment.

Then, Statsig will calculate the mean unit-level revenue per experiment group, imputing 0s for all exposed users with no revenue.

Statsig provides a description of this in-product for any user who wants to learn more:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_configuration.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=b947a5790765b5c16ade86a284f554cb" alt="Inline description explaining aggregation behavior" width="3072" height="1088" data-path="images/whn/metric_examples_configuration.png" />
</Frame>

## Average Current Account Value

Often, you will want to understand if your experiment has altered the "state" of users. Let's say you care about the current account value today on users in test vs. control of your experiment - have you helped users grow their account?

On your end, you'll just need a table or query that tracks users' account values each day. Then, set up a metric source pointing to that table or query.

Go to the metrics tab, press create, configure your metric name & source, and then configure a latest value metric on the column with the account value.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_create_account.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=711947b7a169059fc41c3201a5b3be51" alt="Create metric form for latest account value" width="1008" height="588" data-path="images/whn/metric_examples_create_account.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/metric_examples_configure_account.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=a9e0f6f25035da31f31ffb8cfed512a8" alt="Latest value metric configuration using account column" width="3082" height="1306" data-path="images/whn/metric_examples_configure_account.png" />
</Frame>

### How it works in experiments

First, at unit level, Statsig calculates each day's latest non-null value within any cohort bounds and takes the latest value from the latest day available.

Then, Statsig will calculate the mean unit-level value per experiment group on each day, imputing 0s for all exposed users with no value.

Statsig provides a description of this in-product for any user who wants to learn more:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/7fe6af8f-02a9-45f4-ae3f-5c682757e571.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=c11082b4d26c4206b529fe71a91c5714" alt="Product tooltip describing latest value aggregation logic" width="676" height="80" data-path="images/statsig-warehouse-native/configuration/metric-examples/7fe6af8f-02a9-45f4-ae3f-5c682757e571.png" />
</Frame>

## Users' D7 Participation Rate

A common metric in experimentation is measuring whether exposed users take specific actions within a defined time window.

On your end, you will just need to provide an event table that records user action with essential columns such as user\_id, timestamp and event type. Similarly as above, configure your timestamp field and ID types.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/148469b7-df7b-4f39-af87-1ee9dd5ee431.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=a936bcecbcb0c7bca3d41b7383fcf7bc" alt="Event table metric source definition for participation rate" width="790" height="411" data-path="images/statsig-warehouse-native/configuration/metric-examples/148469b7-df7b-4f39-af87-1ee9dd5ee431.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/5bd9fcc7-54e1-4a15-a8c4-8d9950631d24.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=5d191d4610b225eb5a9263a0b1586a85" alt="ID type configuration for participation event data" width="993" height="441" data-path="images/statsig-warehouse-native/configuration/metric-examples/5bd9fcc7-54e1-4a15-a8c4-8d9950631d24.png" />
</Frame>

Then you can navigate to the metric catalog and create a unit count metric using the defined metric source. You could leverage the 'Add Filter' option to focus on specific events relevant to your designed metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/04712a16-8dac-4c1f-a327-1854fd15d2aa.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=35fff9912b22a86715b4730dc6640c2f" alt="Unit count metric creation with filters for specific event" width="985" height="240" data-path="images/statsig-warehouse-native/configuration/metric-examples/04712a16-8dac-4c1f-a327-1854fd15d2aa.png" />
</Frame>

When defining the metric, you can choose from several rollup modes:

* Daily Participation Rate -> it measures the days a unit was active after being exposed to the experiment divided by its total days in the experiments
* On-Time Event -> it measures if a unit performed an action any time after being exposed to the experiment
* Latest Value -> it measures if a unit passed metric filters on their last observed record
* Custom Attribution Window -> to include data for each unit in a specified time window after being exposed to the experiment

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/959c5dbd-eecf-4797-bc87-7970ccda4947.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=f0e111932bcf44a6268032e008533881" alt="Metric source selection during creation flow" width="1023" height="325" data-path="images/statsig-warehouse-native/configuration/metric-examples/959c5dbd-eecf-4797-bc87-7970ccda4947.png" />
</Frame>

In our example, we want to measure the user participation within 7 days. So you can pick 'Custom Attribution Window' as your rollup mode and set start = 0 end = 6 to define a 7-day window. Option to enable 'Only include units with a completed window' to exclude users who haven't reached the full 7-day period from your analysis.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/0632de2f-dc8c-44c0-85c1-39e8a6a6f070.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=c7a2e54563d4c8915b3e78f43aa82643" alt="Rollup mode options for participation metrics" width="999" height="291" data-path="images/statsig-warehouse-native/configuration/metric-examples/0632de2f-dc8c-44c0-85c1-39e8a6a6f070.png" />
</Frame>

### How it works in experiments

First, at unit level, Statsig will create a 0/1 flag if the event is triggered during the specified time window.

Then, at the group level, the mean is calculated as the SUM of the unit-level flags, divided by the count of UNIQUE UNITS exposed to the experiment.

Statsig provides more details about how Unit Count (Window) Metrics are calculated [here](/statsig-warehouse-native/metrics/unit-count-window).

## User Funnel Metric

A common analysis in experimentation is understanding how a new feature impacts dropoff rates at each step of a user funnel.

To create a funnel metric in Statsig, you need an event table that records each step of the events you want to track. The setup for your metric source follows the same process as described earlier.

When you navigate to the metric catalog, select 'Funnel' as your metric type. Choose the unit level for your funnel steps – this can be a distinct count of users or sessions based on what you want to measure.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/76c815a1-14a6-4d8c-853e-10460f38d4a6.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=4631b8d6799ec70d3d794c8e32a21e2a" alt="Average session count metric configuration" width="1025" height="430" data-path="images/statsig-warehouse-native/configuration/metric-examples/76c815a1-14a6-4d8c-853e-10460f38d4a6.png" />
</Frame>

Then, you cam define your funnel steps, specifying the sequence of events users go through.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/91d50945-ba23-47d0-b0e4-85308a0e404c.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=53a16f33598cb5f82b173182914d33d1" alt="Example showing multi-event participation configuration" width="1010" height="997" data-path="images/statsig-warehouse-native/configuration/metric-examples/91d50945-ba23-47d0-b0e4-85308a0e404c.png" />
</Frame>

In the Advanced Settings, you can further customize your funnel metric to fit different use cases. Options include specify calculation window, measure time to convert, treat exposure as initial funnel event, etc.

These settings provide full flexibility, allowing you to tailor the funnel metric based on your specific analysis needs.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/a6de4690-83ad-49ed-af9a-4eef9c6a9700.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=2b4b8ac43b08d545a992e2c1c28e5207" alt="Metric filters applied to isolate specific event values" width="1021" height="417" data-path="images/statsig-warehouse-native/configuration/metric-examples/a6de4690-83ad-49ed-af9a-4eef9c6a9700.png" />
</Frame>

### How it works in experiments

First, at unit level, a 1/0 (or session-count number for session funnels) metric is constructed for each step of the funnel. This flag is 1 if the unit completed that step some time after all previous steps were completed in order. If using a session-level funnel, it's the number of sessions where that is true, e.g. all previous steps were completed in order for that session key.

Then, at the group level, the stepwise mean is calculated as the total of each step's metric divided by the total metric from the previous step. The overall mean is calculated as the units/sessions that completed the funnel divided by the unit/sessions that started the funnel.

Statsig provides a description of this in-product for any user who wants to learn more:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/84c22973-af41-495d-a943-f0f7436050ee.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=d6cc56bfe5a655ceb4b10c376cc6fe80" alt="Metric catalog entry summarizing event-based conversion metric" width="846" height="79" data-path="images/statsig-warehouse-native/configuration/metric-examples/84c22973-af41-495d-a943-f0f7436050ee.png" />
</Frame>

## User Retention Rate

A retention metric is a great way to measure changes in user stickiness and product growth with the new feature you've built.

To create a retention metric in Statsig, you'll need an event table that captures the key activities indicating user retention.  The setup for your metric source follows the same process as described earlier.

When you navigate to the metric catalog, select 'Retention' as your metric type. Configure the retention period and look back window. For example, if you set your 'Retention Period End' to be 14 and retention lookback window to be 7, retention is measured as whether the user has triggered the retention event between day 8 and day 14.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/e418815e-505c-4356-9922-d706bebb053c.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=454a8ab692bf61ce8ca30f72d385ea63" alt="Configuration UI for retention-style rollup" width="1532" height="352" data-path="images/statsig-warehouse-native/configuration/metric-examples/e418815e-505c-4356-9922-d706bebb053c.png" />
</Frame>

You also have the option to "Use a different start and completion event for retention calculations" if you don’t want to use exposure as the starting event or if you want to define a specific subset of events as your retention event.
For example, based on the setup shown in the screenshots, we will be measuring the week 2 retention rate of users who made a purchase in week 1.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/d3e12922-3767-4a05-987b-e16df126ea41.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=f68b0bbb5fa6fc9ce239523f799512c8" alt="Metric details view describing rollup logic" width="1526" height="542" data-path="images/statsig-warehouse-native/configuration/metric-examples/d3e12922-3767-4a05-987b-e16df126ea41.png" />
</Frame>

In the Advanced Settings, you can configure what's the ID type for your retention metric.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/cdf184a4-cd3a-4622-8669-0d029b1e76dc.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=3b83f48ae07fcae16150a0c23b4eb165" alt="Metric result example for session count" width="1549" height="422" data-path="images/statsig-warehouse-native/configuration/metric-examples/cdf184a4-cd3a-4622-8669-0d029b1e76dc.png" />
</Frame>

### How it works in experiments

First, for each unit per day, Statsig checks if the retention start event is triggered and assigns a 0/1 flag, which serves as the denominator of the calculation.

Next, Statsig checks if the retention completion event occurs within the specified time window and assigns a 0/1 flag, which serves as the numerator of the calculation.

Finally, at the group level, retention is calculated as sum(numerator) / sum(denominator) to determine the overall retention rate.

Statsig provides a description of this in-product for any user who wants to learn more:

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/metric-examples/94843265-ed43-4bce-954f-3f64ec2d380f.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=8f8d4ef4308f81993383a7908e2f44e3" alt="Example of metric insight card for participation rate" width="980" height="81" data-path="images/statsig-warehouse-native/configuration/metric-examples/94843265-ed43-4bce-954f-3f64ec2d380f.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).