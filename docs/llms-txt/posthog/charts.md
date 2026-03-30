# Source: https://posthog.com/docs/product-analytics/trends/charts.md

# Charts - Docs

There are ten charts and visualization options in trends. They're split into two categories:

-   **Time series**, which show you how tracked events and data points fluctuate over a time period.
-   **Total value**, which show the total number of tracked events or data points in any given time period.

## Time series

### Line chart (linear)

![Linear plot](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/linear-light-mode.png)![Linear plot](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/linear-dark-mode.png)

The line chart is a simple, linear trend plot with time on the X-axis and each data point corresponding to the grouping value you've chosen.

Additional series or breakdowns you add to a line chart will appear as separate lines on the chart.

### Line chart (cumulative)

![Cumulative plot](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/cumulative-light-mode.png)![Cumulative plot](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/cumulative-dark-mode.png)

The cumulative plot displays a running tally of each series over the given time period.

This is useful for understanding how quickly an event or data point is growing, such as whether the number of people signing up for your product is growing exponentially or leveling off.

### Bar chart

![Time bar chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/time-bar-chart-light-mode.png)![Time bar chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/time-bar-chart-dark-mode.png)

The **time series** bar chart displays the value of a series over time. This plot shows the exact same information as the [linear chart](#line-chart-linear), but in a slightly different visual manner.

Additional series or breakdowns you add to a bar chart will appear stacked, so you can see how much each property or series contributes to the total number.

### Area chart

![Area chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1715099337/posthog.com/contents/docs/product-analytics/trends/area-chart-light.png)![Area chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1715099340/posthog.com/contents/docs/product-analytics/trends/area-chart-dark.png)

Area charts are a twist on the line chart. When you add a breakdown, or multiple series, area charts behave like a stacked bar chart, but render the data in a line chart showing how each data point contributes to the total.

### Box plot

The box plot displays the statistical distribution of a numeric property's values over time. Each box shows:

-   **Min** – the minimum value
-   **25th percentile (Q1)** – the value below which 25% of observations fall
-   **Median** – the middle value (50th percentile)
-   **Mean** – the average value
-   **75th percentile (Q3)** – the value below which 75% of observations fall
-   **Max** – the maximum value

Box plots are useful for understanding how the distribution of a metric changes across time intervals and for spotting outliers.

Box plots require you to select a numeric property (such as `$session_duration` or a custom numeric property). Breakdowns and formulas are not available for box plots.

## Total value

### Number

![Total value](https://res.cloudinary.com/dmukukwp6/image/upload/v1715099320/posthog.com/contents/docs/product-analytics/trends/active-viewers-light.png)![Total value](https://res.cloudinary.com/dmukukwp6/image/upload/v1715099316/posthog.com/contents/docs/product-analytics/trends/active-viewers-dark.png)

Shows the total of events or data points during the given period. Tick the "Compared to previous period" option to add a percentage comparison.

This option is only available when there's just one series (or [formula](/docs/product-analytics/trends/formulas.md) and no breakdowns added to the insight.

### Bar Chart

![Value bar chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/value-light-mode.png)![Value bar chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/value-dark-mode.png)

Displays the total value of a series over the *entire date range*. This means that this type of plot has no option for grouping, as it doesn't display data over time.

Try using a [breakdown](/docs/product-analytics/trends/breakdowns.md) in combination with this chart type to see a list of the top property values, or add multiple series to see how they compare.

### Table

![Table chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/table-light-mode.png)![Table chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/table-dark-mode.png)

The table view displays the raw numerical values of a series over the *entire date range*.

### Pie

![Pie chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/pie-light-mode.png)![Pie chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/pie-dark-mode.png)

The pie chart shows the relative distribution of the values of different series or breakdowns over the *entire date range*.

To hide the total value displayed below the chart, untick **Show total below chart** in the display settings.

### World map

![World map chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/world-map-light-mode.png)![World map chart](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/world-map-dark-mode.png)

The world map chart displays values in an interactive map of the world, broken down by country code. This display option can't be selected if you're already breaking down by a property other than country code.

### Calendar heatmap

> **Important:** This feature is currently an opt-in beta. You can enable it on the [feature previews settings page](https://app.posthog.com/settings/user-feature-previews#calendar-heatmap-insight).

![Calendar heatmap showing user activity patterns](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_08_22_at_11_47_06_AM_545abbeb38.png)![Calendar heatmap showing user activity patterns](https://res.cloudinary.com/dmukukwp6/image/upload/Screenshot_2025_08_22_at_11_47_50_AM_2f91837123.png)

The **Calendar heatmap** insight displays a heatmap showing either the number of **unique users** or **total events** for **any selected event**, broken down by hour of the day and day of the week.

#### What the heatmap shows

-   Each **cell** represents the number of unique users or total events during a specific hour of a specific day. Numbers are formatted for readability (e.g., 1.73K for 1,730).

-   The **"All" column** on the right aggregates the total for each day across all hours, and is highlighted in a different color.

-   The **bottom row ("All")** aggregates the total for each hour across all days, also highlighted in a different color.

-   The **bottom-right cell** shows the grand total for the selected metric (unique users or total events) across all days and hours in the selected time range, with a distinct color.

-   Use the **"Show more"** button to expand the heatmap and view additional details if available.

-   The displayed time for each cell and the starting day of the week are based on your project's date and time settings. By default, the time is UTC, but you can change the timezone in [your project settings](https://app.posthog.com/settings/project-product-analytics#date-and-time).

> **Note:** Selecting a time range longer than 7 days will include additional occurrences of weekdays and hours, potentially increasing the counts in those buckets. For best results, select 7 closed days or a multiple of 7 closed day ranges.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better