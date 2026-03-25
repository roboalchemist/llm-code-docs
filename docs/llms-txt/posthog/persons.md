# Source: https://posthog.com/docs/data/persons.md

# People - Docs

People in PostHog represent the users behind your events. You can view them in the [People tab](https://app.posthog.com/persons).

People have **person profiles** with [properties](/docs/product-analytics/person-properties.md). This enables you to do things like:

-   Filter on person properties
-   Create [cohorts](/docs/data/cohorts.md)
-   Use person properties for targeting feature flags, A/B tests, and surveys.
-   Track initial UTM values and referrers across anonymous and [identified](/docs/product-analytics/identify.md) users.
-   Query the `persons` table using [SQL insights](/docs/product-analytics/sql.md)

## How to create person profiles

When you capture your first [identified event](/docs/data/anonymous-vs-identified-events.md) for a user, it creates a **person profile** for them. Then, any future events captured are attributed to this profile. You can also [set properties](/docs/product-analytics/person-properties.md) for the person.

## Duplicate person profiles

If your [`identify`](/docs/product-analytics/identify.md) implementation has gaps, a single real-world user can end up with multiple person profiles. For example, if a user visits your app on a phone and a laptop but `identify` is only called on one device, each device creates its own profile with a separate anonymous distinct ID. This usually points to a misconfiguration — when `identify` is called correctly on every device and session, PostHog merges these into one profile automatically.

The most common cause of duplicate profiles is using different distinct IDs for the same user across systems without calling [`alias`](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user) to link them. When PostHog can't merge two already-identified profiles, it blocks the merge and logs a "Refused to merge an already identified user" [ingestion warning](/docs/data/ingestion-warnings.md). If you're seeing this warning, it means your users are accumulating duplicate profiles that won't be merged automatically.

Duplicate profiles inflate counts that rely on person profiles, such as cohort sizes and feature flag targeting. If you notice these numbers are higher than expected, check your [ingestion warnings](/docs/data/ingestion-warnings.md) and verify that you're calling [`identify`](/docs/product-analytics/identify.md) as soon as a user logs in on every device and browser.

To fix existing duplicates, see [how to merge users](/docs/product-analytics/identify.md#how-to-merge-users).

## The persons list

The [People tab](https://app.posthog.com/persons) displays a list of all people in your project. By default, the list includes the following columns:

> **Note:** The "Last Seen" column has been temporarily removed from the Persons table and column configuration options while we resolve a known issue. It will be restored in a future update.

-   **Person** - display name for the person
-   **ID** - the person's distinct ID
-   **Created at** - when the person profile was first created
-   **Last seen** - when the person was last active, rounded to the nearest hour
-   **Delete** - option to delete the person

The **Last seen** column updates hourly, so it may not reflect the exact timestamp of a person's latest event. If a person was active within the last hour, the column displays "last hour" instead of a specific time.

You can sort the list by any column, including last seen, to find recently active or inactive users. To customize which columns are visible, click the **Configure columns** button above the table.

## Viewing person profiles

Clicking on a person in the [People tab](https://app.posthog.com/persons) opens their profile and shows all their properties.

![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/data/people/person-profile-light-mode.png)![Person profile](https://res.cloudinary.com/dmukukwp6/image/upload/posthog.com/contents/images/docs/data/people/person-profile-dark-mode.png)

-   **Events** shows all the events a person has triggered, which you can search and filter to find specific events.

-   **Recordings** shows all of the session replays a person has generated. Note this is subject to the retention policy of your plan, so people who haven't been active recently may have none.

-   **Cohorts** shows all the [cohorts](/docs/data/cohorts.md) a person belongs to.

-   **Related groups:** shows [groups](/docs/product-analytics/group-analytics.md) (e.g. organizations, projects, and instances) a person belongs to.

-   **Feature flags:** shows all [feature flags](/docs/feature-flags.md) that are enabled for the person.

-   **History:** shows any manual changes that have been made to the person's profile.

## Deleting person data

### In the PostHog app

-   Search for the person via their unique ID. For example, their email.
-   Click on the person's ID
-   Click **Delete person** to remove them and all their associated data. You will be prompted to confirm this action.

**Avoid reusing deleted distinct IDs**

User deletion requests are not immediate, but processed asynchronously. We recommend that you *avoid* reusing a deleted `distinct_id` value for a new user, as it may lead to unexpected results while the deletion is being processed. Once the deletion process is fully processed, PostHog does not retain any data associated with the deleted `distinct_id`.

If you must reuse the `distinct_id`, you can do so using the **Reset deleted person** tool, available from the dropdown at the top-right of the [**persons page**](https://app.posthog.com/persons). This tool enables you to reset a deleted `distinct_id` so that future events associated with it create a new person profile.

If you instead want to split a person with multiple IDs (e.g. to isolate bad data tied to a specific `distinct_id`), use the **Split IDs** button on their person profile.

### Via the API

You can also delete persons data via the API. See the [Data Deletion docs](/docs/privacy/data-deletion.md) for more information.

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better