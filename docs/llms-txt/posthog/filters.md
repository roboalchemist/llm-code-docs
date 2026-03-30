# Source: https://posthog.com/docs/product-analytics/trends/filters.md

# Filters - Docs

Trends support two [types of filters](#types-of-filters):

1.  **Inline filters** – only apply to a specific series in your insight.
2.  **Filter groups** – global filters that apply to the whole insight.

Inline filters only support `AND` operators – i.e. all filter conditions must be met for an event or user to be included.

Filter groups support `AND` and `OR` operators – i.e. events will be included if one or both of the filter conditions are met.

## Configuring filters

Filters are comprised of three elements, a property, an operation, and a value.

> **Note:** You can also fully customize your filter by writing them as a [SQL expression](/docs/sql/expressions.md). See our tutorial on [using SQL for advanced time and date filters](/tutorials/hogql-date-time-filters.md) for an example.

### 1\. The filter property

**Example: *(Current URL, Browser, etc)***

This is the property that you want to filter based on. These properties can be:

-   Properties on the event itself
-   Properties on the person who sent the event
-   Properties on groups that this event is a member of *(see [group analytics](/docs/user-guides/group-analytics.md))*
-   Properties on sessions
-   Properties on [cohorts](/docs/user-guides/cohorts.md) the user is a member of
-   Properties on the HTML element if an event was autocaptured

By default, the dropdown will only show properties that have been seen on a specific event before, but if you instead want to filter based on an unseen property, you can scroll all the way to the bottom of the list and click 'Show X properties that haven't been seen with this event'

### 2\. The filter operation

**Example: *(equals, contains, etc)***

This is what PostHog uses to compare the property value to determine whether an event passes the filter or not. Note that the options for this will change based on the type of the property you've selected (e.g. whether a property is a `Number` or `String`).

Some common operators used in insight filters:

| Name | Description |
| --- | --- |
| = equals | The property matches the value exactly and can contain multiple values to match against |
| ≠ doesn't equal | The property doesn't exactly match any of the values you provided |
| ∈ contains | The property contains the value as a substring and can contain multiple values to match against |
| ∉ doesn't contain | The property doesn't contain any of the values you provided as a substring |
| ~ matches regex | The property matches a regex (only available for strings) |
| ≁ doesn't match regex | The property doesn't matches a regex (only available for strings) |
| > greater than | The property is greater than a specific value (only available for numeric properties) |
| < less than | The property is less than a specific value (only available for numeric properties) |
| ✓ is set | The property has been set on a specific event |
| ✕ is not set | The property was not set on a specific event |

For a complete list of all available operators, including numeric range operators and semver operators for version-based filtering, see the [property filter operators reference](/docs/data/property-filters.md).

### 3\. The comparison value

This is the value that PostHog compares to the property using the operation you specified. If the operation returns true, then the event is included in the insight, and if it returns false it is excluded.

Some operations – equals, doesn't equal, contains, and doesn't contain – allow you to pass multiple values to compare against, in which case the event is included if any of these values return true when compared.

## Types of filters

### Inline filters

![Example inline filter](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/inline-filter-light-mode.png)![Example inline filter](hhttps://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/inline-filter-dark-mode.png)

These filters apply to a specific series within a graph. You can apply totally different filters to each series in a trends insight.

To add a filter to a series, click the icon next to the event name, and search for your desired property.

Currently, inline filters only support with `AND` operations. If you want to include events that match *at least one* of a group of filters – i.e. `OR` operations – use filter groups.

### Filter groups

Filter groups allow you to apply filters to **all series** within an insight. These filter groups are composed of a number of single filter, which can be combined in the following two ways:

-   `AND` - Events have to match *every* filter within the group
-   `OR` - Events only have to match *a single* filter within the group

![Example global filter](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/filter-groups-light-mode.png)![Example global filter](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/filter-groups-dark-mode.png)

Click the `+ Add filter group` button to add a filter group. You can add multiple filter groups and you can use `AND` `OR` operators both within and between filter groups.

> **Important:** Since group filters apply to all events within an insight, and these events may not share all their properties, group filters permit you to use any property that has been seen in *at least one* of your events. If you happen to create a filter that references a property that not all events have, events that do not contain this property will automatically fail the check and will be excluded by the filter.

## Filtering internal and test users

The final option for filtering events is using the option to filter out 'internal and test users'.

This option is useful for excluding events sent from local builds of your product, or by members of your team that you don't want to include in your analysis.

![Filtering internal and test users turned on](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/internal-and-test-users-light-mode.png)![Filtering internal and test users turned on](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/user-guides/trends/internal-and-test-users-dark-mode.png)

Click on the settings icon to go to [your project settings](https://us.posthog.com/settings/project#internal-user-filtering) to customize the filters that are used.

## Filtering by first event occurrence

Beyond filtering on properties, you can also specify which event to count for a user if they perform it multiple times. This is useful for analyzing user activation or the first time a user interacts with a feature.

This setting is configured per series in a trend insight, in the aggregation dropdown next to the event name.

![First event occurrence](https://res.cloudinary.com/dmukukwp6/image/upload/trends_first_ever_light_c49e2aad57.png)![First event occurrence](https://res.cloudinary.com/dmukukwp6/image/upload/trends_first_ever_dark_f2ca1dd21a.png)

There are two options for this:

### 1\. First-ever occurrence for user

This option finds a user's very first occurrence of an event type, and then checks if it matches your filters. If this first-ever event doesn't match your filters, the user is excluded from the results, even if they performed the same event later with matching filters.

**Example:** You're filtering for pageview events to `/about`, but the user's first ever pageview was to `/pricing`. PostHog will only check the `/pricing` event, and since it doesn't match the filter, this user will be excluded, even if they later visited `/about`.

### First occurrence matching filters for user

This option finds the first time a user performed an event type *that also matches your filters*. Previous events of the same type from that user that don't match the filters are ignored.

**Example:** You're filtering for pageview events to `/about`. A user first visited `/pricing` and then later visited `/about`. PostHog ignores the `/pricing` view and counts the `/about` view, as it's the first one that matches the filter.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better