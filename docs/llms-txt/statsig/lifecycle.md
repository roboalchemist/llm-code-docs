# Source: https://docs.statsig.com/product-analytics/lifecycle.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Lifecycle

> Understand how users start, return, remain, and churn over time

## Overview

Lifecycle charts in Metrics Explorer help you understand how usage changes over time by classifying your unique units (for example user\_id) within each time interval based on whether they used an event recently, returned after a gap, continued to use it, or churned.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/pidyj--7CTpD0mCp/images/product-analytics/lifecycle/lifecycle_demo_v4.png?fit=max&auto=format&n=pidyj--7CTpD0mCp&q=85&s=d28b1d38d4806cd011799e6ae5555acf" alt="Life Cycle chart interface in Metrics Explorer" width="3282" height="1488" data-path="images/product-analytics/lifecycle/lifecycle_demo_v4.png" />
</Frame>

### Use Cases

* **Track new-user ramp after a launch:** See whether adoption is growing week over week after shipping a new feature
* **Monitor churn and reactivation:**  Understand whether users are falling off (and whether they come back)
* **Compare retention health across releases:** Spot changes in “stickiness” and reactivation patterns over time

## Creating a Lifecycle Chart

### Step 1: Choose an event (or a compatible metric)

The first step to creating a lifecycle chart is to decide if you want to use a metric or an event. Lifecycle is designed for a single underlying event and count-style metrics that are composed of a single count type event

### Step 2: Choose your unit (unique units)

Select what you want to count uniquely (for example user\_id, stable\_id, or another unit). The chart reports how many unique units fall into each category for each time interval.

### Step 3: Choose your interval (granularity)

Pick an interval unit (day / week / month) and a number of intervals per bucket (1–48). Each bar on the chart represents one interval bucket, and the chart shows one data point per bucket across the selected date range (max 1 year).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/om1zXrHwvJf85htF/images/product-analytics/lifecycle/lifecycle_interval_selector.png?fit=max&auto=format&n=om1zXrHwvJf85htF&q=85&s=e4dd224dc0a48149d33f37d12cb95c94" alt="Life Cycle chart interface in Metrics Explorer" width="1094" height="558" data-path="images/product-analytics/lifecycle/lifecycle_interval_selector.png" />
</Frame>

### Step 4: (Optional) Add filters

Apply filters to focus on a specific segment (for example platform, country, app version, or a feature-related property).

## Interpreting your Lifecycle Chart

Each interval bucket classifies unique units into four categories (mutually exclusive):

**New:** Used during this interval, and did not use at any point earlier within the lookback window (up to 1 year before this interval).

**Resurrected:** Used during this interval, did not use in the immediately previous interval, and did use earlier within the lookback window.

**Recurring:** Used during this interval and the immediately previous interval.

**Dormant:** Used in the immediately previous interval, but not during this interval (often displayed below the axis to make churn visually obvious).

### Reading the chart

**X-axis:** Time, grouped into your chosen interval buckets.

**Y-axis:** Count of unique units.

**Stacked bars:** Show how the composition of usage changes over time (new vs resurrected vs recurring), while the churn component (dormant) highlights drop-off between adjacent intervals.


Built with [Mintlify](https://mintlify.com).