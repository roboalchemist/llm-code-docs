# Source: https://posthog.com/docs/product-analytics/group-analytics.md

# Group analytics - Docs

**New: Customer Analytics preview**

Group analytics is getting a makeover! Sign up for the [customer analytics feature preview](https://app.posthog.com/settings/user-feature-previews#customer-analytics-roadmap) to get a sneak peek, and [share your feedback](https://app.posthog.com/#panel=support%3Afeedback%3Acrm%3Alow).

## Overview

Group analytics aggregates events by entities like organizations or companies instead of individual users. This is useful when you need to track behavior at the company, team, or project level.

With groups, you can:

-   Track how companies progress through onboarding and activation
-   Deploy feature flags to entire organizations
-   Run experiments at the company level
-   Measure metrics like daily active companies or company churn rate

### Key concepts

**Group types** are categories you define - like "company" or "project". You can create up to 5 group types per project.

**Groups** are the individual entities within each type. For example, if your group type is "company," each group would be a specific company like "Acme Corp" or "Tech Solutions Inc." You can have unlimited groups within each group type.

### How it works

1.  Define group types - like "company" or "channel"
2.  Assign group keys (unique identifiers) to each group
3.  Link events to groups in your code
4.  Analyze data by group instead of by user

## Billing

Group analytics is a paid add-on. Here's how billing works:

**All identified events count toward billing**

Once you subscribe to group analytics, billing applies to **all identified events** in your project, not just events with group properties attached. This is because group analytics enables infrastructure that processes all identified events to support group-level analysis.

-   Billing starts when you enable group analytics from your [billing page](https://app.posthog.com/organization/billing), not when you add group analytics code to your application.
-   Usage is based on captured [identified events](/docs/product-analytics/identify.md), even if they don't include group properties.
-   Billing stops when you unsubscribe from the billing page. You don't need to remove group analytics code from your application to stop billing.

You can see how enabling group analytics affects your pricing on the [pricing calculator](/pricing.md).

## Use cases

### B2B product activation

Create a "company" group type to track how companies progress through your B2B product's onboarding with [funnels](/docs/product-analytics/funnels.md):

-   Calculate number of daily active companies, company churn rate, or feature adoption by company
-   See how many companies signed up this month
-   Track what percentage completed onboarding
-   Measure what percentage of new companies used specific features

### Channel retention

Create a "channel" group type for Slack-like apps to measure [retention](/docs/product-analytics/retention.md) of features by channel:

-   Track average messages per channel, monthly active channels, or channel participants
-   See which channels consistently use video calling
-   Measure how many channels stay active month over month
-   Compare feature adoption rates by channel type

### Project-level feature flags

Create a "project" group type for collaborative apps like Jira, Notion, or Figma:

-   Track project pageviews, users per project, and project engagement
-   Target [feature flags](/docs/feature-flags.md) at the project level
-   Roll out refactored code to a few projects first, measure performance and errors, then expand based on results

### Cross-product analysis

Group analytics works across PostHog's entire platform. Here's how you can use group types with different products:

| Product | Functionality | Example |
| --- | --- | --- |
| Product analytics | Aggregate trends, funnels, retention, and stickiness by group | Track how many companies completed onboarding |
| Feature flags | Configure release conditions based on groups | Ensure all users of a company see the same feature flag variant |
| Experiments | Evaluate experiment results based on group aggregations | Run an A/B test to improve activation rate for new companies |
| Data warehouse | Join tables or enrich queries with groups data | Write SQL queries that calculate usage across different company sizes |

## Groups vs cohorts

Groups and [cohorts](/docs/data/cohorts.md) serve different purposes:

-   **Groups** aggregate events and don't have to be connected to users. They require code in your app to set up.
-   **Cohorts** represent specific sets of users with something in common. They're created in PostHog without additional code.

Use cohorts if you only need to analyze a list of users. They're simpler and faster to implement.

## Set up group analytics

### Create group types

Create group types before you associate events with them. Call the group identify method to create a group type and set properties.

In this example, we create a "company" group type. For each individual group (company), we set the group key like an ID or domain:

PostHog AI

### Web

```javascript
// Call posthog.group() to create a group before capturing events.
// It sends a `$groupidentify` event to create or update the group.
// It will also create the group type if it doesn't exist. In the
// web SDK, it also associates all subsequent events in the session
// with the group.
posthog.group('company', 'company_id_in_your_db');
// This event will be associated with the company above.
posthog.capture('user_signed_up');
// If the group type is already created, you can also manually add
// the `$groups` property to any event you want to associate with
// the group.
posthog.capture('user_signed_up', {
    '$groups': {
        'company': 'company_id_in_your_db'
    }
});
```

### Python

```python
# Call posthog.group_identify() to create a group before capturing events.
# It sends a `$groupidentify` event to create or update the group.
# It will also create the group type if it doesn't exist.
posthog.group_identify('company', 'company_id_in_your_db')
# Once the group is created, you can associate events with it by
# passing the `group` argument. The `group` argument is required
# for every event that should be associated with the group.
posthog.capture(
    'user_signed_up',
    groups={'company': 'company_id_in_your_db'}
)
```

### Go

```go
// Call posthog.GroupIdentify{} to create a group before capturing events.
// It sends a `$groupidentify` event to create or update the group.
// It will also create the group type if it doesn't exist.
client.Enqueue(posthog.GroupIdentify{
    Type: "company",
    Key:  "company_id_in_your_db",
})
// Once the group is created, you can associate events with it by
// passing the `$groups` property. The `$groups` property is required
// for every event that should be associated with the group.
client.Enqueue(posthog.Capture{
    DistinctId: "user_distinct_id",
    Event: "user_signed_up",
    Groups: posthog.NewGroups().
        Set("company", "company_id_in_your_db"),
})
```

### Node.js

```javascript
// Call posthog.groupIdentify() to create a group before
// capturing events. It sends a `$groupidentify` event to create
// or update the group. It will also create the group type if it
// doesn't exist.
posthog.groupIdentify('company', 'company_id_in_your_db')
// Once the group is created, you can associate events with it by
// passing the `groups` property. The `groups` property is required
// for every event that should be associated with the group.
posthog.capture({
    event: 'user_signed_up',
    distinctId: 'user_distinct_id',
    groups: { company: 'company_id_in_your_db' }
})
```

### PHP

```php
// Call PostHog::groupIdentify() to create a group before capturing events.
// It sends a `$groupidentify` event to create or update the group.
// It will also create the group type if it doesn't exist.
PostHog::groupIdentify([
    'groupType' => 'company',
    'groupKey' => 'company_id_in_your_db'
]);
// Once the group is created, you can associate events with it by
// passing the `$groups` property. The `$groups` property is required
// for every event that should be associated with the group.
PostHog::capture([
    'distinctId' => 'user_distinct_id',
    'event' => 'user_signed_up',
    '$groups' => ['company' => 'company_id_in_your_db']
]);
```

### iOS

```swift
// Call PostHogSDK.shared.group() to create a group before capturing events.
// It sends a `$groupidentify` event to create or update the group.
// It will also create the group type if it doesn't exist. In the
// iOS SDK, it also associates all subsequent events in the
// session with the group.
PostHogSDK.shared.group(type: "company", key: "company_id_in_your_db")
// This event will be associated with the company above.
PostHogSDK.shared.capture("user_signed_up")
// If the group type is already created, you can also manually add
// the `$groups` property to any event you want to associate with
// the group.
PostHogSDK.shared.capture(
    event: "user_signed_up",
    properties: [
        "$groups": [
            "company": "company_id_in_your_db"
        ]
    ]
)
```

### Android

```kotlin
// Call PostHog.group() to create a group before capturing events.
// It sends a `$groupidentify` event to create or update the group.
// It will also create the group type if it doesn't exist. In the
// Android SDK, it also associates all subsequent events in the
// session with the group.
PostHog.group(type = "company", key = "company_id_in_your_db")
// This event will be associated with the company above.
PostHog.capture("user_signed_up")
// If the group type is already created, you can also manually add
// the `$groups` property to any event you want to associate with
// the group.
PostHog.capture(
    event = "user_signed_up",
    properties = mapOf(
        "\$groups" to mapOf(
            "company" to "company_id_in_your_db"
        )
    )
)
```

### Segment

```javascript
// You'll always need to pass through the $groups object for Segment, even for analytics.js
analytics.track('user_signed_up', {
    $groups: { segment_group: 'company_id_in_your_db' }
})
```

### Terminal

```bash
# Call $groupidentify to create or update a group.
# It will also create the group type if it doesn't exist.
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "event": "$groupidentify",
    "distinct_id": "static_string_used_for_all_group_events",
    "properties": {
        "$group_type": "company",
        "$group_key": "company_id_in_your_db"
    }
}' https://us.i.posthog.com/i/v0/e/
# Once the group is created, you can associate events with it by
# passing the `$groups` property. The `$groups` property is required
# for every event that should be associated with the group.
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "event": "user_signed_up",
    "distinct_id": "user_distinct_id",
    "properties": {
        "$groups": {"company": "company_id_in_your_db"}
    }
}' https://us.i.posthog.com/i/v0/e/
```

**Tips for group keys**

-   Use singular names for group types - "company" not "companies"
-   Use unique IDs as keys for individual groups, not names because names can duplicate
-   Each project can have up to 5 group types
-   You can have unlimited individual groups within each type

### Set group properties

Every individual group can have [properties](/docs/product-analytics/person-properties.md) associated with it, just like persons. For example, for a "company" group type, you might add `company_name`, `date_joined`, and `subscription` as properties for each individual group company.

**Individual groups require at least one property**

You must include at least one group property for an individual group to appear in the [people tab](https://app.posthog.com/persons) in the PostHog app.

PostHog AI

### Web

```javascript
// Option 1 (recommended): Set properties in posthog.group()
// This has the side-effect that all subsequent events in the session are associated to the group
posthog.group('company', 'company_id_in_your_db', {
    name: 'PostHog',
    subscription: "subscription",
    date_joined: '2020-01-23'
});
// Option 2:
// Set properties in posthog.capture()
// This method doesn't have the side-effect of associating all future events to the group.
posthog.capture('$groupidentify', {
    '$group_type': 'company',
    '$group_key': 'company_id_in_your_db',
    '$group_set': {
        name: 'PostHog',
        subscription: "subscription",
        date_joined: '2020-01-23'
    }
});
```

### Python

```python
posthog.group_identify('company', 'company_id_in_your_db', {
    'name': 'PostHog',
    'subscription': 'subscription',
    'date_joined': '2020-01-23'
})
```

### Go

```go
client.Enqueue(posthog.GroupIdentify{
    Type: "company",
    Key:  "company_id_in_your_db",
    Properties: posthog.NewProperties().
        Set("name", "PostHog").
        Set("subscription", "subscription").
        Set("date_joined", "2020-01-23"),
})
```

### Node.js

```javascript
posthog.groupIdentify({
    groupType: 'company',
    groupKey: 'company_id_in_your_db',
    properties: {
        name: 'PostHog',
        subscription: "subscription",
        date_joined: '2020-01-23'
    }
})
```

### PHP

```php
PostHog::groupIdentify([
    'groupType' => 'company',
    'groupKey' => 'company_id_in_your_db',
    'properties' => ['name' => 'PostHog', 'subscription' => 'premium', 'date_joined' => '2020-01-23']
]);
```

### iOS

```swift
// Option 1 (recommended): Set properties in group()
// This has the side-effect that all subsequent events in the session are associated to the group
PostHogSDK.shared.group(
    type: "company",
    key: "company_id_in_your_db",
    properties: [
        "name": "PostHog",
        "subscription": "subscription",
        "date_joined": "2020-01-23"
    ]
)
// Option 2: Set properties using capture
// This method doesn't have the side-effect of associating the session's events to the group
PostHogSDK.shared.capture(
    event: "$groupidentify",
    properties: [
        "$group_type": "company",
        "$group_key": "company_id_in_your_db",
        "$group_set": [
            "name": "PostHog",
            "subscription": "subscription",
            "date_joined": "2020-01-23"
        ]
    ]
)
```

### Android

```kotlin
// Option 1 (recommended): Set properties in group()
// This has the side-effect that all subsequent events in the session are associated to the group
PostHog.group(
    type = "company",
    key = "company_id_in_your_db",
    properties = mapOf(
        "name" to "PostHog",
        "subscription" to "subscription",
        "date_joined" to "2020-01-23"
    )
)
// Option 2: Set properties using capture
// This method doesn't have the side-effect of associating the session's events to the group
PostHog.capture(
    event = "\$groupidentify",
    properties = mapOf(
        "\$group_type" to "company",
        "\$group_key" to "company_id_in_your_db",
        "\$group_set" to mapOf(
            "name" to "PostHog",
            "subscription" to "subscription",
            "date_joined" to "2020-01-23"
        )
    )
)
```

### Segment

```javascript
analytics.group('company_id_in_your_db', {
    "name": "PostHog",
    "subscription": "subscription",
    "date_joined": "2020-01-23"
})
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "event": "$groupidentify",
    "properties": {
        "distinct_id": "company_id_in_your_db",
        "$group_type": "company",
        "$group_key": "company_id_in_your_db",
        "$group_set": {
            "name": "PostHog",
            "subscription": "premium",
            "date_joined": "2020-01-23"
        }
    }
}' https://us.i.posthog.com/i/v0/e/
```

Properties on individual groups work the same way as properties on [people](/docs/data/persons.md). They can be used in experiments and feature flags to roll out features to specific groups.

The PostHog app identifies an individual group using the `name` property. If the `name` property isn't found, it falls back to the group key.

### Link events to groups

How you link events to individual groups depends on your SDK:

-   **JavaScript Web SDK:** Call `posthog.group()` once and all session events link to that individual group automatically.
-   **Other SDKs:** Pass the group information in the `groups` parameter for every event you capture.

Events must be [identified](/docs/data/anonymous-vs-identified-events.md) to link to individual groups. If `$process_person_profile` is set to `false`, the event won't link to the group.

#### Multiple groups per event

You can't assign one event to multiple individual groups of the same group type, but you can assign it to individual groups of different group types.

PostHog AI

### Web

```javascript
// Not possible
posthog.group('company', 'company_id_in_your_db');
posthog.group('company', 'another_company_id_in_your_db');
posthog.capture('user_signed_up')
// Allowed
posthog.group('company', 'company_id_in_your_db');
posthog.group('channel', 'channel_id_in_your_db');
posthog.capture('user_signed_up')
```

### Python

```python
# Not possible
posthog.capture(
    'user_distinct_id',
    'user_signed_up',
    groups={
        'company': 'company_id_in_your_db',
        'company': 'another_company_id_in_your_db'
    }
)
# Allowed
posthog.capture(
    'user_distinct_id',
    'user_signed_up',
    groups={
        'company': 'company_id_in_your_db',
        'channel': 'channel_id_in_your_db'
    }
)
```

### Go

```go
// Not possible
client.Enqueue(posthog.Capture{
    DistinctId: "user_distinct_id",
    Event: "user_signed_up",
    Groups: posthog.NewGroups().
        Set("company", "company_id_in_your_db").
        Set("company", "another_company_id_in_your_db"),
})
// Allowed
client.Enqueue(posthog.Capture{
    DistinctId: "user_distinct_id",
    Event: "user_signed_up",
    Groups: posthog.NewGroups().
        Set("company", "company_id_in_your_db").
        Set("channel", "channel_id_in_your_db"),
})
```

### Node.js

```javascript
// Allowed
posthog.capture({
    event: 'user_signed_up',
    distinctId: 'user_distinct_id',
    groups: {
        company: 'company_id_in_your_db',
        channel: 'channel_id_in_your_db'
    }
})
```

### PHP

```php
// Not possible
PostHog::capture([
    'distinctId' => 'user_distinct_id',
    'event' => 'user_signed_up',
    '$groups' => ['company' => 'company_id_in_your_db', 'company' => 'another_company_id_in_your_db']
]);
// Allowed
PostHog::capture([
    'distinctId' => 'user_distinct_id',
    'event' => 'user_signed_up',
    '$groups' => ['company' => 'company_id_in_your_db', 'channel' => 'channel_id_in_your_db']
]);
```

#### Capture events for individual groups without a user

If you want to capture events for an individual group without linking them to a specific user, use a single static string as the distinct ID:

PostHog AI

### Node.js

```javascript
posthog.capture({
    event: 'group_event_name',
    distinctId: 'static_string_for_group_events',
    groups: { company: 'company_id_in_your_db' }
})
```

### Python

```python
posthog.capture('static_string_for_group_events',
    'group_event_name',
    groups={'company': 'company_id_in_your_db'}
)
```

### Go

```go
client.Enqueue(posthog.Capture{
    DistinctId: "static_string_for_group_events",
    Event: "group_event_name",
    Groups: posthog.NewGroups().
        Set("company", "company_id_in_your_db"),
})
```

### PHP

```php
PostHog::capture([
    'distinctId' => 'static_string_for_group_events',
    'event' => 'group_event_name',
    '$groups' => ['company' => 'company_id_in_your_db']
]);
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "event": "group_event_name",
    "distinct_id": "static_string_for_group_events",
    "properties": {
        "$groups": {"company": "company_id_in_your_db"}
    }
}' https://us.i.posthog.com/i/v0/e/
```

## Using groups in PostHog

### View individual groups

To view individual groups and their properties, go to the [people tab](https://app.posthog.com/persons) in the PostHog app and select the group type you want to view. Group types are listed under the **Groups** section.

![View groups](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/view_Group_Light_8eb32757a3.png)![View groups](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/view_Group_Dark_5b6c1cc29e.png)

### Analyze insights by group type

Use [insights](/docs/product-analytics/insights.md) to view trends aggregated by group type.

For example, to see how many organizations signed up recently:

1.  Create an insight with your signup event.
2.  Expand the menu next to the event.
3.  Select **Unique** with your group type.

This shows total individual groups that signed up instead of individual users.

![Analyze group insights](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/insights_Light_83a249155d.png)![Analyze group insights](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/insight_Darks_87aa211aa0.png)

### Use group types with funnels

Track how individual groups organizations move through conversion steps by setting **Aggregating by** to your group type.

This shows how many individual groups completed each step, the drop-off percentage, and which specific individual groups dropped off.

![Group funnels](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/funnels_Light_1fa9760a35.png)![Group funnels](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/funnels_Dark_4d2a0992ab.png)

### Use group types with feature flags

[Create a feature flag](/docs/feature-flags/creating-feature-flags.md) and select your group type in the **Match by** dropdown under **Release conditions**.

Update your code to pass group information when checking feature flags:

PostHog AI

### Web

```javascript
// Make sure you have called posthog.group() earlier in that session
if (posthog.isFeatureEnabled('new-groups-feature')) {
    // Do something
}
```

### Python

```python
if posthog.feature_enabled("new-groups-feature", "user_distinct_id", groups={"company": "company_id_in_your_db"}):
    # Do something
```

### PHP

```php
if (PostHog::isFeatureEnabled('new-groups-feature', 'user_distinct_id', false, ['company' => 'company_id_in_your_db'])) {
    // Do something
}
```

### Node.js

```javascript
const isFlagEnabled = await posthog.isFeatureEnabled('new-groups-feature', 'user_distinct_id', false, { company: 'company_id_in_your_db' })
if (isFlagEnabled) {
    // Toggle feature-flag specific behavior
}
```

### Rename group types

Change how group types display in PostHog in [Settings > Customer Analytics](https://app.posthog.com/settings/project-customer-analytics#group-analytics).

![Groups in project settings](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/project_Setting_Light_ff8617214d.png)![Groups in project settings](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/project_Setting_Dark_2352dd1b0b.png)

### Delete group types

To delete a group type:

1.  Go to the [people tab](https://app.posthog.com/persons) in the PostHog app.
2.  Select **Menu options** > **Delete group type**.

![Delete group type](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/delete_Group_Type_Light_8f08fae9f8.png)![Delete group type](https://res.cloudinary.com/dmukukwp6/image/upload/q_auto,f_auto/delete_Group_Type_Dark_45f2f7adb8.png)

**What happens when you delete a group type**

-   Event data remains unchanged. Group data is filtered from queries based on a deletion timestamp.
-   Deleted group types don't count toward your 5 group type limit.
-   If new events arrive with the same group key, the group type reappears with a new creation timestamp. Historical events (before the new timestamp) won't appear for the recreated group type.

## Limitations

Group analytics has a few limitations to be aware of:

-   Maximum of 5 group types per project
-   You can delete group types, but not individual groups
-   Multiple individual groups of the same group type can't be assigned to a single event
-   Group types aren't supported for lifecycle insights or user paths
-   Only individual groups with known properties appear in the [people tab](https://app.posthog.com/persons)

## Further reading

-   [When and how to run group-targeted A/B tests](/blog/running-group-targeted-ab-tests.md)
-   [Understanding group analytics: frontend vs backend implementations](/tutorials/frontend-vs-backend-group-analytics.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better