# Source: https://docs.statsig.com/metrics/pulse.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Pulse Metrics

> Learn how different metric types are computed and interpreted in Pulse experiment results.

Experiments with Statsig use **Pulse** to compute and communicate results. The metric type is important in computing and interpreting the final result.

Most metric types are aggregated across all users in the group; however, some metric types that use ratios are only aggregated across [participating users](/experiments/interpreting-results/participating-units) (users that have non-null value for that metric). We'll walk through the various types of metrics available in experiments and how to interpret their pulse results.

## Pulse Statistics by Metric Type

| Metric Type                               | Total                                                                    | Mean                                                                                                                                                                     | Units                                                                        |
| ----------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| event\_count                              | Sum of events (99.9% winsorization applied)                              | Average events per user (99.9% winsorization applied)                                                                                                                    | All users                                                                    |
| event\_dau                                | Sum of event DAU (distinct user-day pairs)                               | Average event\_dau value per user per day. Note that we call this "Event Participation Rate" as this can be interpreted as the probability a user is DAU for that event. | All users                                                                    |
| sum                                       | Total sum of values (99.9% winsorization)                                | Average value per user (99.9% winsorization)                                                                                                                             | All users                                                                    |
| mean                                      | Overall mean value                                                       | Overall mean value                                                                                                                                                       | [Participating users](/experiments/interpreting-results/participating-units) |
| event\_user                               | Count of distinct users that have had the event.                         | Average metric value per user per day. Depending on Rollup Mode, can be a one-time event or daily participation rate.                                                    | All users                                                                    |
| ratio                                     | Not shown                                                                | Overall ratio: sum(numerator values)/sum(denominator values)                                                                                                             | [Participating users](/experiments/interpreting-results/participating-units) |
| funnel                                    | Not shown                                                                | Overall ratio: sum(numerator values)/sum(denominator values)                                                                                                             | [Participating users](/experiments/interpreting-results/participating-units) |
| user: dau, wau, mau\_28day                | Not shown                                                                | Average metric value per user per day. The probability that a user is xAU                                                                                                | All users                                                                    |
| user: new\_dau, new\_wau, new\_mau\_28day | Count of distinct users that are new xAU at some point in the experiment | Fraction of users that are new xAU                                                                                                                                       | All users                                                                    |
| user: retention metrics                   | Overall average retention rate                                           | Overall average retention rate                                                                                                                                           | [Participating users](/experiments/interpreting-results/participating-units) |
| user: L7, L14, L28                        | Not shown                                                                | Average L-ness value per user per day                                                                                                                                    | All users                                                                    |
| count\_distinct                           | Total number of unique values                                            | Average number of unique values per user                                                                                                                                 | All users                                                                    |

**Some example metric breakdowns in Pulse:**

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/pulse/aa7e1063-6473-4e4e-9ca4-7074f5a0c450.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=799cc06527858c5e4b3c91228999edff" alt="pulse 1" width="996" height="604" data-path="images/metrics/pulse/aa7e1063-6473-4e4e-9ca4-7074f5a0c450.png" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/pulse/7b0b1d99-c720-480e-8671-f5f696485500.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=bf1d886a8d763cce23391c4c6a18d249" alt="pulse 2" width="996" height="605" data-path="images/metrics/pulse/7b0b1d99-c720-480e-8671-f5f696485500.png" />
</Frame>

## Event Count and Event DAU in Pulse

<Warning>**event\_dau Legacy Support**: event\_dau metrics are now in legacy support only and are no longer created for new events. Existing event\_dau metrics will continue to be available for any of your new experiments and will continue to be computed daily. For all new events, you should create an event\_user metric to measure daily active users.</Warning>

From [Metrics 101](/metrics/101) and [Auto-generated Metrics](/metrics/raw-event-metrics),

* [**event\_count**](/metrics/raw-event-metrics#event-count-metric) measures the volume of the activity based on count of events triggered
* [**event\_dau**](/metrics/raw-event-metrics#event-dau-metric) measures unique daily users who triggered a given event

For example, the table below shows the **event\_count** and **event\_dau** metrics for two event types,*Page Views* and *Add to Cart*, for three users over three days.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/pulse/187719553-c7e5c186-5dfe-4521-8bfb-1bb4b8cdb38d.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=54c9444a06549d0965bfc07f5f31090c" alt="Event count and event DAU metrics table" width="1286" height="250" data-path="images/metrics/pulse/187719553-c7e5c186-5dfe-4521-8bfb-1bb4b8cdb38d.png" />
</Frame>

Over the duration of an experiment, Pulse results measure the change in:

* the **mean** event\_count, or the average event count per user
* the **mean** event\_dau, or average active days per user; we call this the **Daily Event Participation Rate**

For example, the table below shows the **Total event\_count**, **Total Units**, and **Mean event\_count** over the same three days as above, now in the context of an experiment.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/pulse/187721781-3240ebc6-43ae-4fd8-ac44-c3493308e127.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=6376004bc21b03a7cf011d57b5d0ecb8" alt="Experiment metrics table showing total event count and mean values" width="1270" height="189" data-path="images/metrics/pulse/187721781-3240ebc6-43ae-4fd8-ac44-c3493308e127.png" />
</Frame>

Similarly, the table below shows the **Total event\_dau**, **Total Units**, and **Mean event\_dau** over the same three days of the experiment. Alice was 'active' on three days for the *Page View* event and on one day for the *Add to Cart* event. Therefore, average event*dau for Alice is 3/3 for the \_Page View* event and 1/3 for the *Add to Cart* event. In other words, Alice's **daily participation rate** is 1.00 for the *Page View* event and 0.33 for the *Add to Cart* event so far in the experiment. Statsig aggregates this average event\_dau for each user in the experiment, with each user weighted equally.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/mluNydUQT6X4ZpGa/images/metrics/pulse/187721834-b8e94f15-f3ee-4584-924b-96e424ddcd0c.png?fit=max&auto=format&n=mluNydUQT6X4ZpGa&q=85&s=0aa70ab27c90c5ef88f893657632320c" alt="Event DAU metrics table showing daily participation rates" width="1334" height="424" data-path="images/metrics/pulse/187721834-b8e94f15-f3ee-4584-924b-96e424ddcd0c.png" />
</Frame>

To measure the change in engagement for a call to action link or button, use event\_count to measure the change in average clicks per user, and use event\_dau to measure the change in users’ daily participation rate for the click.

<Info>**Event Count and Event DAU in Custom Metrics**: When creating a custom ratio metric, use event\_count to include all events (counting all events triggered by the same user). Use event\_user (or event\_dau, if available) to count unique active users on a given day (all events triggered by the same user are counted as one).</Info>

## Winsorization

To reduce the impact of outliers, Statsig caps *event\_count* and *sum* metric types at the 99.9th percentile (by default). This mitigates the risk of bots and extreme values significantly swaying experiment results.

The winsorization 99.9th percentile is computed using all non-zero and non-null values of the metric, and then all values of exceeding this limit are replaced with it.

Warehouse Native (WHN) allows for more customization of winsorization by metric and by percentile.

## Frequently Asked Questions

**1. Is it possible for a ratio metric to move in the opposite direction than both the numerator and denominator metrics?**

Yes, it is possible for the ratio to rise while both the numerator and denominator metrics decline. For example, this happens when the denominator is falls more than the numerator. As a best practice, Statsig recommends tracking the numerator and denominator as independent metrics when monitoring ratio metric. Ratio metrics are often subject to statistical noise and can be tricky to use for obtaining a statistically significant result.

**2. For ratio metrics, how does Statsig determine *participating users*?**

Ratio metrics are computed only for users that have a non-zero value in the denominator, i.e. the user must have triggered the denominator event on a given day to be included in the daily ratio. Users that don't trigger the denominator event during an experiment are not included in the test vs. control comparison of a ratio metric.

**3. What is the difference in metrics between One-Time Event vs Daily Participation Rate?**

The distinction between these in only relevant in the context of an experiment.
Daily participation rate counts the number of *days* a user has that event, divided by the number of *days* the user has been in the experiment.
One time event is a binary metric that checks whether the user has that event *at least once* during their time in the experiment.


Built with [Mintlify](https://mintlify.com).