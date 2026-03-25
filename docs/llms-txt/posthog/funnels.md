# Source: https://posthog.com/docs/product-analytics/funnels.md

# Funnels - Docs

For every flow in your product, more people will start it than complete it successfully. Funnels enable you to visualize your flows and understand where the friction points are so that you can improve them.

You can learn the following from funnels:

-   [Where people are getting stuck during your flow](#understand-where-people-are-getting-stuck-during-your-flow)
-   [Who successful and unsuccessul users are](#identify-unsuccessful-users)
-   [The steps with the highest friction and time to convert](#graph-type)
-   [The paths users take in a funnel](#explore-user-paths)
-   [If product changes are improving your funnel over time](#graph-type)
-   [How seasonality affects your conversion rates](#understand-seasonality-in-your-conversion-rates)

## How to create a funnel

1.  Click [Product Analytics](https://us.posthog.com/insights) on the left sidebar
2.  Click the **\+ New Insights** tab
3.  Select the **Funnel** option in the dropdown

### Adding steps

Select the steps to include in your funnel, ideally starting with the first event or action a user will trigger in the flow.

Next, add events users must complete to proceed through the funnel, ending with the event you consider the success for this flow. It's best to start with the simplest flow and avoid using optional steps to ensure you don't filter out or skew results.

![Funnel steps](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-light-mode.png)![Funnel steps](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-dark-mode.png)

#### Combine events inline

You can combine multiple events into a single funnel step using inline combination. This lets you treat several events as one step without creating a custom [action](/docs/data/actions.md).

Select the events to include in a step, and they're combined using a logical `OR` – any occurrence of the selected events counts toward that step. This works the same way as [combining events inline in trends](/docs/product-analytics/trends/overview.md#combine-events-inline).

![Inline events](https://res.cloudinary.com/dmukukwp6/image/upload/h_500,c_limit,q_auto,f_auto/funnels_inline_events_light_fd59b44032.png)![Inline events](https://res.cloudinary.com/dmukukwp6/image/upload/h_500,c_limit,q_auto,f_auto/funnels_inline_events_dark_f9c82e5cd9.png)

By default, funnel steps must be completed **sequentially**, however you are able to change this behavior by selecting one of three different step orders:

1.  **Sequential** – Step B must happen after Step A, but any number events can happen between A and B.
2.  **Strict order** – Step B must happen directly after Step A without any events in between.
3.  **Any order** – Steps can be completed in any sequence.

**Steps must be performed**

If you add multiple steps with the same event type, it will require the user to **trigger that event multiple times**. Think of funnel steps as actions to be performed, not filters to be applied.

For example, adding a `clicked button` step, then a second `clicked button` step that filters for the "Sign Up" button, will require the user to perform **two** distinct button clicks.

### Filtering steps

To refine your steps, you can filter out events using event, person, or group properties, autocapture elements, or SQL. To do this, click the **filter icon** next to the step, choose your property, and fill in the details. You can also set a global filter in the **Filters** section in the bottom.

![Global filters](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/global-filters-light-mode.png)![Global filters](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/global-filters-dark-mode.png)

> **Note**: Using person properties in funnels requires identified events and [person profiles](/docs/data/persons.md).

### Excluding steps

You can also exclude people who completed certain events between two specific steps. To do this, add the step in the **Exclusion steps** section.

These people are completely excluded from the entire funnel.

### Conversion rate calculation

There are two options for showing conversion rates in a funnel:

1.  **Overall conversion** – for each step, this shows the conversion relative to the *first* step.
2.  **Relative to the previous step** – for each step, this shows the conversion relative to the *previous* step.

**Overall conversion** is helpful for understanding the entire funnel, whereas **relative conversion** shows you which steps have biggest opportunity for improvement.

![Overall vs relative conversion](https://res.cloudinary.com/dmukukwp6/image/upload/funnel_conversion_types_light_bcc79c205d.png)![Overall vs relative conversion](https://res.cloudinary.com/dmukukwp6/image/upload/converesion_funnels_dark_2_793a67ada4.png)

### Breakdowns

To understand how different types of user interact with your funnel, it's helpful to breakdown results. You can breakdown steps by event and person properties. To do this, click on the **\+ Add breakdown** button and select the property you want to break down by.

The example below shows a breakdown by operating system:

![Breakdown funnel steps by Operating System](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/breakdown-by-operating-system-light-mode.png)![Breakdown funnel steps by Operating System](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/breakdown-by-operating-system-dark-mode.png)

![Funnel steps broken down by property](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-breakdown-light-mode.png)![Funnel steps broken down by property](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/funnel-steps-breakdown-dark-mode.png)

#### Attribution types

When breaking down funnels, it's possible that the same properties don't exist on every event. For example, if you want to break down by `browser` on a funnel that contains both of frontend and backend events.

In this case, you can choose from which step the properties should be selected from by modifying the attribution type. There are four modes to choose from:

##### 1\. First touchpoint

In this case, the first property value seen in any of the steps is chosen.

Consider this example sequence of events:

1.  `$pageview` with `browser = Chrome`
2.  `user signed up` with `browser = Firefox`

The first touchpoint means that `Chrome` will be the breakdown value.

In the first touchpoint mode, one person will always only have one value.

##### 2\. Last touchpoint

In this case, the last property value seen from all steps is chosen.

Consider the same example as above:

1.  `$pageview` with `browser = Chrome`
2.  `user signed up` with `browser = Firefox`

The last touchpoint means that `Firefox` will be the breakdown value.

In the last touchpoint mode, one person will always only have one value.

##### 3\. All steps

In this case, all events completed in your selected step order will be included in the funnel.

Consider the following entirely possible example of events from a single person:

1.  `$pageview` with `browser = Chrome`
2.  `$pageview` with `browser = Firefox`
3.  `user signed up` with `browser = Chrome`
4.  `user posted` with `browser = Chrome`
5.  `user posted` with `browser = Firefox`

With all steps mode, the person will be counted twice in the funnel, but in slightly different ways.

The person will be in the Chrome breakdown as having completed all three steps: `$pageview`, `user signed up`, and `user posted`. The person will also be in the Firefox breakdown, but only for the `$pageview` step because they didn't complete the `user signed up` step with Firefox.

##### 4\. Specific step

In this case, only the property value seen at the selected step is chosen. Importantly, this also means that the person won't be included in the funnel if they don't have a property value at the selected step.

Consider an example where we capture these two events for a person:

1.  `$pageview` with `browser = Chrome`
2.  `user signed up` with `browser = Firefox`

When step two is chosen in this example, the value will be `Firefox`. Also, any people who only have a `$pageview` event will be excluded from the funnel.

With the specific step mode, one person can have more than one property value. For example, if the user captured the same event with different browsers:

1.  `$pageview` with `browser = Chrome`
2.  `$pageview` with `browser = Firefox`

Then the person would have both `Chrome` and `Firefox` as their breakdown values.

Another common use for `Specific step` is to display only a single URL for pageview steps in the funnel columns. The default, `First touchpoint` uses the first property value seen from all steps, which will include the subdirectory URLs in the breakdown if they appeared in later steps.

For example, if you've

-   set your first query step as `Pageview` where `Current URL` `= equals` `https://foo.com/bar`,
-   and `/bar` has subdirectories (e.g. `https://foo.com/bar/foo1` `https://foo.com/bar/foo2` etc.),
-   and `Breakdown by` is set to `Current URL`

but you don't want pages under the subdirectories of `https://foo.com/bar` to appear in the funnel chart.

In this case, set the `Attribution type` to `Specific step` / `Step 1` to see only `https://foo.com/bar` in the pageview column of the chart.

> For an unordered funnel, the specific step is meaningless, as the first step can be the last step, and vice versa. So, it's referred to as "any step" in the UI. It has the same semantics as a specific step in an ordered funnel, but it looks at property values from all steps.

#### Filtering for first occurrence

When analyzing funnels, you can specify which event to count if a user performs it multiple times. This is configured in the dropdown for each step of the funnel.

![First event occurrence](https://res.cloudinary.com/dmukukwp6/image/upload/funnels_first_ever_light_b64bd76a5e.png)![First event occurrence](https://res.cloudinary.com/dmukukwp6/image/upload/funnels_first_ever_dark_fe7d879280.png)

There are two options for this:

##### 1\. First-ever occurrence

First-ever occurrence matches only the first time a user performs a specific event type. If this first event doesn't **match the filters** for that funnel step, or is **outside the funnel's date range**, the user is excluded from the funnel entirely. This is true even if they perform the event again later with matching filters.

**Example:** You have a funnel step looking for page views to `/about` and the user's first-ever page view is to `/pricing`. PostHog will only consider the first `$pageview` event, which is on the `/pricing` page. Since the first page view doesn't match the `/about` filter, the user will be dropped from the funnel, even if they visit `/about` later.

##### 2\. First occurrence matching filters

First occurrence matching filters matches the first time a user performs an event *that also matches the filters for that funnel step*. Any previous events of the same type that don't match the filters are ignored.

**Example:** You have a funnel step looking for pageviews to `/about`. A user first visits `/pricing` and then later visits `/about`. PostHog ignores the `/pricing` view and matches the `/about` view, as it's the first one that fits the step's criteria.

### Graph type

The graph type dropdown let's you choose between conversion steps, time to convert, and historical trends.

![Conversion over time using Trends](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/conversion-over-time-using-trends-light-mode.png)![Conversion over time using Trends](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/conversion-over-time-using-trends-dark-mode.png)

Each type serves a unique purpose:

-   **Conversion steps** – shows you where users are dropping off in your funnel and number of people converting between steps.

-   **Time to convert** – shows you steps with the highest friction. Steps with a long time to convert are likely much harder than steps with a short time.

-   **Historical trends** – shows you how your conversion rate has changed over time for users who entered the funnel on a given date. Useful for understanding how changes, fixes, and new features have affected your funnel success rate. You can enable trend lines from the **Options** menu to help identify patterns in noisy data.

## Tips for analyzing funnels

### Understand where people are getting stuck during your flow

The most common use case for funnels is understanding where people are getting stuck or dropping off in your flow.

![Identifying drop-offs in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/identifying-drop-offs-light-mode.png)![Identifying drop-offs in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/user-guides/funnels/identifying-drop-offs-dark-mode.png)

There a few ways to identify problem steps:

-   Absolute numbers show you where you're losing the most people.
-   Relative conversion rate show you which steps have the greatest impact on your overall conversion rate.

Usually the steps with the lowest relative conversion rate are where the largest opportunities are.

### Identify unsuccessful users

Once you have a funnel drop-off you'd like to explore further, the first step is to find out why users are struggling. There are many ways to get this information, from [talking to users directly](/newsletter/talk-to-users.md) to [replaying their sessions](/docs/session-replay.md).

Click on the chart or the linked column values below the funnel to view the individual people who **COMPLETED** or **DROPPED** that step of your funnel.

![View users in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/v1718365074/posthog.com/contents/Screenshot_2024-06-14_at_12.36.24_PM.png)![View users in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/v1718365075/posthog.com/contents/Screenshot_2024-06-14_at_12.36.47_PM.png)

You can also save this list of users as a [cohort](/docs/data/cohorts.md) for further analysis.

### Explore user paths

It can be useful to explore the [paths](/docs/product-analytics/paths.md) people take between steps in your funnel.

Click on the **'...'** next to any step in your funnel and, depending on which step you're selecting, you'll be presented with options to "show user paths":

-   leading to step
-   between previous step and this step
-   after step
-   after drop off
-   before drop off

![View user paths in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/v1718369751/posthog.com/contents/Screenshot_2024-06-14_at_1.54.52_PM.png)![View user paths in a funnel](https://res.cloudinary.com/dmukukwp6/image/upload/v1718369751/posthog.com/contents/Screenshot_2024-06-14_at_1.55.24_PM.png)

Selecting any option creates a new insight showing the paths users took. This is useful for getting a complete picture of the *real* funnel created by user interactions, rather than the imagined *perfect* funnel engineers and designers have in their head. Spoiler: the *real* funnel and the *perfect* funnel are rarely the same!

### Understand seasonality in your conversion rates

It's unlikely that your conversion rate will remain stable every day or every week. This is normal, but it's important to understand the external factors that can cause these fluctuations so you don't jump to conclusions too quickly when analyzing a big change or drop-off.

To look at the seasonality of your conversion rates, set the [graph type](#graph-type) to historical trends and set the time period to when you may expect seasonal variations.

A common seasonality to watch out for is weekends, particularly if your product is B2B. Another one is a yearly sale such as "Black Friday", which increases the number of people visiting your site and increases the expectation of discounts, making it difficult to compare against the rest of the year.

In this view, you can adjust the date ranges to observe key seasonal trends. You can then look at your funnel to determine if it's just a seasonal trend or whether something else has affected the experiece of your product (like a product change).

### Correlation analysis

###### Where is this feature available?

##### Free / Open-source

##### Paid

##### Enterprise

![Not available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMCIgaGVpZ2h0PSIyMCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDIwIDIwIj48cGF0aCBmaWxsPSIjRkI0RjBEIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik0xMC4wNjQyIDcuODE5Nkw0LjI0NDU5IDJMMiA0LjI0NDU5TDcuODE5NiAxMC4wNjQyTDIuMTI4MzcgMTUuNzU1NEw0LjM3Mjk2IDE4TDEwLjA2NDIgMTIuMzA4OEwxNS40Njc1IDE3LjcxMjFMMTcuNzEyMSAxNS40Njc1TDEyLjMwODggMTAuMDY0MkwxNy44NDA1IDQuNTMyNDhMMTUuNTk1OSAyLjI4Nzg5TDEwLjA2NDIgNy44MTk2WiIgY2xpcC1ydWxlPSJldmVub2RkIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)![Available](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyOCIgaGVpZ2h0PSIyOCIgZmlsbD0ibm9uZSIgdmlld0JveD0iMCAwIDI4IDI4Ij48cGF0aCBmaWxsPSIjNzFBQTU1IiBkPSJNOS41MTAwMyAyNC4wMjk5TDAuNDEwMDMzIDE0LjkyOTlDLTAuMTM2Njc4IDE0LjM4MzIgLTAuMTM2Njc4IDEzLjQ5NjggMC40MTAwMzMgMTIuOTVMMi4zODk4OCAxMC45NzAxQzIuOTM2NiAxMC40MjMzIDMuODIzMDggMTAuNDIzMyA0LjM2OTc5IDEwLjk3MDFMMTAuNSAxNy4xMDAyTDIzLjYzMDIgMy45NzAwOUMyNC4xNzY5IDMuNDIzMzggMjUuMDYzNCAzLjQyMzM4IDI1LjYxMDEgMy45NzAwOUwyNy41ODk5IDUuOTVDMjguMTM2NyA2LjQ5NjcxIDI4LjEzNjcgNy4zODMxNCAyNy41ODk5IDcuOTI5OUwxMS40ODk5IDI0LjAzQzEwLjk0MzIgMjQuNTc2NyAxMC4wNTY3IDI0LjU3NjcgOS41MTAwMyAyNC4wMjk5VjI0LjAyOTlaIi8+PC9zdmc+)

[Correlation Analysis](/docs/product-analytics/correlation.md) automatically highlights significant factors that affect the conversion rate of users within the funnel.

Correlation analysis works well when you don't already have a hypothesis for what is affecting conversion through a funnel. This report will automatically highlighting significant events or properties that either negatively or positively impact conversion rate.

## Further reading

Want to know more about what's possible with Funnels in PostHog? Try these tutorials:

-   [Getting started with AARRR](/tutorials/aarrr-framework.md)
-   [Building an AARRR 'Pirate' Funnel](/tutorials/aarrr-how-to-build-pirate-funnel-posthog-with-posthog.md)
-   [Building and measuring a sign up funnel with Next.js, Supabase and PostHog](/tutorials/nextjs-supabase-signup-funnel.md)

Want more? Check our [full list of PostHog tutorials](/tutorials.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better