# Source: https://posthog.com/docs/product-analytics/paths.md

# User paths - Docs

User paths are a type of [insight](/docs/user-guides/insights.md) that enable you to follow users along their journey through your product and determine where the biggest drop-offs are.

You can learn the following from paths:

-   Where users are getting confused or stuck.
-   Which parts of your app people are actually using.
-   Why users aren't discovering new features.
-   Where new users are landing into your marketing website.

![Example of a paths insight](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/example-light-mode.png)![Example of a paths insight](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/example-dark-mode.png)

## How to create a paths insight

1.  Click [Product Analytics](https://us.posthog.com/insights) on the left sidebar
2.  Click the **\+ New insight** button
3.  Select the **User Paths** tab

![Switching the event type](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/switching-type-light-mode.png)![Switching the event type](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/switching-type-dark-mode.png)

## Understanding paths

Paths can be overwhelming at first, especially if they have many steps. To help you understand them better, here's a simple example:

![Path visualization with only 2 steps](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/2-step-light-mode.png)![Path visualization with only 2 steps](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/2-step-dark-mode.png)

Each step along the path is a page that the user viewed, and the horizontal bars correspond to a user navigating from one page to another. The numbers next to the paths correspond to how many distinct users passed through this specific step along the way.

In the above, the first step shows that **268** people viewed the homepage `/homepage`. From the homepage, we can see that people either viewed the `/docs/tutorials` page next, or the `/docs/...gramming` page next, or the `/docs/paths` page, and so on.

### Exploring a specific step within a path

You can dig deeper into a specific step by hovering your mouse over it:

![Dropoff](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/dropoff-light-mode.png)![Dropoff](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/dropoff-dark-mode.png)

This gives us the exact conversion rate of this step, as well as the average time it took users to get here from the previous step. In addition to this information, you can also click on the **•••** icon to bring up a menu with a number of actions for this step:

-   **Set as path start** - Sets this step as the starting point for your path. This is useful for exploring where your users navigate to after a specific step.
-   **Set as path end** - Sets this step as the ending point for your path. This is useful when analyzing the ways a user ends up at a specific step or learning why users dropped off.
-   **Exclude path item** - Adds an [exclusion](#exclusions) rule for this specific event.
-   **View funnel** - Opens a new [funnel insight](/docs/product-analytics/funnels.md) with this event already set as the first step. This is useful when analyzing drop-off of a specific step.
-   **Copy path item name** - Copies the event name to your clipboard.

### Viewing recordings and creating cohorts from a step

One of the most powerful features of paths is the ability to see all the users who passed through a specific step. To do this, click on the number next to the name of step. This brings up a list of all of these users.

![list of users who reached a step](https://res.cloudinary.com/dmukukwp6/image/upload/v1716305838/posthog.com/contents/path-users-light.png)![list of users who reached a step](https://res.cloudinary.com/dmukukwp6/image/upload/v1716305838/posthog.com/contents/path-users-dark.png)

You can then create a [cohort](/docs/data/cohorts.md) of users who passed through the step by clicking the **Save as cohort**.

If you have enabled [session replays](/docs/session-replay.md), you can also see recordings of a user sessions for this step by clicking the **View recording** button. This is helpful when diagnosing problems with your funnels.

## Configuration options

This next section provides detailed information on the different configuration options of the paths insight.

![Configuration options for creating paths](https://res.cloudinary.com/dmukukwp6/image/upload/v1716371632/posthog.com/contents/steps-light.png)![Configuration options for creating paths](https://res.cloudinary.com/dmukukwp6/image/upload/v1716371632/posthog.com/contents/step-dark.png)

### Event types

There are 4 types of events that PostHog can display user paths for. You need to select at least one, and you can select any combination of the four.

#### Page views

This options shows paths for the `$pageview` event sent by our web libraries. Each step of the path is broken down by the `Current URL` property.

This also means that you can see a continuous path of your users even if they navigate across domains.

#### Screen views

This option shows steps for the `$screen` events sent by our mobile app libraries. Each step of the path is broken down by the `$screen_name` property.

#### Custom events

This contains all events other than the `$pageview` and `$screen` event. When displaying paths for these events, they will be broken down by name, with each step corresponding to an event a user performed in succession.

#### SQL expression

You can also write your own custom queries path steps using [SQL expressions](/docs/sql/expressions.md).

For example, the following expression will filter to only show pageviews on Chrome:

PostHog AI

```
if(event = '$pageview' and properties.$browser = 'Chrome', properties.$current_url, null)
```

### Wildcard groups

Wildcard groups are an advanced feature that allows you to group multiple events together into a single step based on certain patterns. They work by using the `*` character to replace a unique pattern in a string.

Wildcard groups are typically used when you're dealing with URLs that contain unique values or IDs, and you want to combine all of these paths into a single step.

For example, if you have URLs with the format `/product/{product-id}`, you can use the pattern `/product/*` to group them together.

When using wildcards on custom events, the pattern will be matched against the event name itself. For example,`dashboard *` will match the events with names such as `dashboard created` and `dashboard viewed`.

### Path cleaning rules

Path cleaning rules are an advanced version of [wildcard groups](#wildcard-groups). They use regex to match dynamic URL segments and replace them with a readable alias, reducing the cardinality of your path data.

For example, URLs like `/user/123`, `/user/456`, and `/user/789` can all be cleaned into `/user/:id` so they appear as a single row in your path tables.

For details on configuring path cleaning rules, including examples and where they apply, see the [path cleaning](/docs/product-analytics/path-cleaning.md) docs.

### Exclusions

Exclusions enable you to remove events entirely from being displayed in a path.

![Excluding two events](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/exclusions-light-mode.png)![Excluding two events](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/paths/exclusions-dark-mode.png)

### Number of people on each path

This enables you to set the minimum and/or maximum number of people who performed the path in order for it to be displayed. This is especially helpful in reducing the density of the visualization since it removes paths from the insights.

For example, you can set a minimum of 100 users per path to remove the most uncommon paths users took.

### Setting the number of steps

There is an option right above the graph to select the number of steps to display.

![Select number of paths](https://res.cloudinary.com/dmukukwp6/image/upload/v1716372005/posthog.com/contents/step-count-light.png)![Select number of paths](https://res.cloudinary.com/dmukukwp6/image/upload/v1716372005/posthog.com/contents/step-count-dark.png)

Increasing the number of steps will show a longer portion of a user's journey through your product. The drawback is that too many steps can often show a cluttered view. To fix this, see above on how to [exclude certain events](#exclusions).

## Why don't my path numbers match my funnel numbers?

Paths and funnels use different queries and answer different questions, so their numbers aren't meant to match.

**Funnels** count unique users. They answer: *"How many users completed this specific sequence?"* Every user who enters step 1 is counted, and you see how many reached each subsequent step.

**Paths** are an exploration tool for discovering navigation patterns. They answer: *"What are the most common step-by-step transitions people take?"* They show the top 50 most frequent transitions, not comprehensive user counts.

Several technical differences explain the discrepancy:

-   **Top 50 transitions** – Paths only return the 50 most common transitions between steps. Less common paths are excluded entirely.

-   **Counts transition frequency** – The numbers show how often each transition occurred, not unique users. If one user visits Home→Pricing in three separate sessions, that counts as 3. Funnels count each user only once per step.

-   **Path length limit** – Paths only analyze a set number of events per session which is controlled by the [step count setting](#setting-the-number-of-steps) (default 5). If a user visits pages A→B→C→D→E→F→G, only the first 5 are included. F and G are excluded. If you define both a start and end steps, paths preserve those steps but collapse the middle steps into **"..."**, which limits visibility into the full journey. Funnels don't have this limitation: they track whether users reached each defined step, regardless of how many events occurred in between.

-   **30-minute session windows** – Events more than 30 minutes apart start a new path. Funnels use a conversion window (default 14 days).

The best practice is to use paths to explore what patterns exist, then validate specific flows with funnels, and investigate individual behavior with [session replays](/docs/session-replay.md).

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better