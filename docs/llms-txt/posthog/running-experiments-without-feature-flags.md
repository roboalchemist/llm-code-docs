# Source: https://posthog.com/docs/experiments/running-experiments-without-feature-flags.md

# How to run experiments without feature flags - Docs

You may want to run experiments without using PostHog's feature flags. There are 2 reasons why you may want to do this:

1.  You're using a different library for feature flags rather than PostHog's, and you want to run your experiment using this library.
2.  Feature flag support is not yet available in the PostHog SDK that you are using.

This doc walks you through how to set up an experiment without using PostHog's feature flags.

## Step 1: Create your experiment in PostHog

Create a new experiment in the [experiments tab](https://app.posthog.com/experiments) and follow the same steps as you would when [creating a regular one](/docs/experiments/manual.md#how-to-create-an-experiment-in-posthog).

> **Note:** Although you won't be using feature flags directly in your experiment, you still need to name your feature flag key for submitting events so PostHog can calculate your experiment results.
>
> Additionally, it's not possible to rename the 'control' variant. You can name the other variants whatever you'd like, though.

## Step 2 (optional): Call the `flags` endpoint

If feature flag support is not yet available in your PostHog SDK, but you still want to leverage PostHog's feature flag infrastructure, use the PostHog [API](/docs/api.md) to call the [`flags`](/docs/api/flags.md) endpoint. This enables you to calculate the feature flag value for a given user.

This step is not necessary if you are using your own feature flag library.

## Step 3: Add the feature flag property to your events

In order to attribute events to their correct experiment variants, you'll need to include a `$feature/experiment_feature_flag_key: variant-name` property when submitting your events. You only need to do this for events that you'd like to track in your experiment.

This is similar to the [same step](/docs/experiments/manual.md#step-2-server-side-only-add-the-feature-flag-property-to-your-events) when setting up regular experiments. The key difference is that now you need to include this property wherever you capture events for the experiment, not just server-side SDKs.

PostHog AI

### Web

```javascript
posthog.capture('event_name_of_your_goal_metric', {
    "$feature/experiment-feature-flag-key": "variant-name"
})
```

### React

```jsx
posthog.capture('event_name_of_your_goal_metric', {
    "$feature/experiment-feature-flag-key": "variant-name"
})
```

### React Native

```jsx
posthog.capture('event_name_of_your_goal_metric', {
    "$feature/experiment-feature-flag-key": "variant-name"
})
```

### Android

```kotlin
PostHog.capture(
    event = "event_name_of_your_goal_metric",
    properties = mapOf(
        "\$feature/experiment-feature-flag-key" to "variant-name"
    )
)
```

### iOS

```swift
PostHogSDK.shared.capture("event_name_of_your_goal_metric", properties: ["$feature/experiment-feature-flag-key": "variant-name"])
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: 'event_name_of_your_goal_metric',
    properties: {
        '$feature/experiment-feature-flag-key': 'variant-name'
    },
})
```

### Python

```python
posthog.capture(
    'distinct_id',
    'event_name_of_your_goal_metric',
    {
        '$feature/experiment-feature-flag-key': 'variant-name'
    }
)
```

### PHP

```php
PostHog::capture([
  'distinctId' => 'distinct_id',
  'event' => 'event_name_of_your_goal_metric',
  'properties' => [
    '$feature/experiment-feature-flag-key' => 'variant-name'
  ]
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id',
    event: 'event_name_of_your_goal_metric',
    properties: {
        '$feature/experiment-feature-flag-key': 'variant-name',
    }
})
```

### Go

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id",
  Event:      "event_name_of_your_goal_metric",
  Properties: posthog.NewProperties().
    Set("$feature/experiment-feature-flag-key", "variant-name"),
})
```

### Java

```java
posthog.capture(
  "distinct_id",
  "event_name_of_your_goal_metric",
  new HashMap<String, Object>() {
    {
      put("$feature/experiment-feature-flag-key", "variant-name");
    }
  }
);
```

### C#

```csharp
posthog.Capture(
  "distinct_id",
  "event_name_of_your_goal_metric",
  properties: new() {
    ["$feature/experiment-feature-flag-key"] = "variant-name"
  }
);
```

## Step 4: Send the `$feature_flag_called` event

You need to capture the `$feature_flag_called` event. This ensures that we record which experiment variant each user was assigned to. This is also referred to as [exposure logging](/docs/experiments/exposures.md), and without it you would not be able to analyze your results.

You need to include two properties with this event:

1.  `$feature_flag_response`: this is the name of the variant the user has been assigned to e.g., "control" or "test"
2.  `$feature_flag`: This is the key of the feature flag in your experiment.

**Important:** For accurate results, you must submit this event whenever you retrieve the value of your feature flag.

PostHog AI

### Web

```javascript
posthog.capture('$feature_flag_called', {
    "$feature_flag_response": "variant-name",
    "$feature_flag": "feature-flag-key"
})
```

### React

```jsx
posthog.capture('$feature_flag_called', {
    "$feature_flag_response": "variant-name",
    "$feature_flag": "feature-flag-key"
})
```

### React Native

```jsx
posthog.capture('$feature_flag_called', {
    "$feature_flag_response": "variant-name",
    "$feature_flag": "feature-flag-key"
})
```

### Android

```kotlin
PostHog.capture(
    event = "\$feature_flag_called",
    properties = mapOf(
        "\$feature_flag_response" to "variant-name",
        "\$feature_flag" to "feature-flag-key"
    )
)
```

### iOS

```swift
PostHogSDK.shared.capture("$feature_flag_called", properties: [
    "$feature_flag_response": "variant-name",
    "$feature_flag": "feature-flag-key"
])
```

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id',
    event: '$feature_flag_called',
    properties: {
        '$feature_flag_response': 'variant-name',
        '$feature_flag': 'feature-flag-key'
    },
})
```

### Python

```python
posthog.capture(
    'distinct_id',
    '$feature_flag_called',
    {
        '$feature_flag_response': 'variant-name',
        '$feature_flag': 'feature-flag-key'
    }
)
```

### PHP

```php
PostHog::capture([
  'distinctId' => 'distinct_id',
  'event' => '$feature_flag_called',
  'properties' => [
    '$feature_flag_response' => 'variant-name',
    '$feature_flag' => 'feature-flag-key'
  ]
]);
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id',
    event: '$feature_flag_called',
    properties: {
        '$feature_flag_response': 'variant-name',
        '$feature_flag': 'feature-flag-key'
    }
})
```

### Go

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id",
  Event:      "$feature_flag_called",
  Properties: posthog.NewProperties().
    Set("$feature_flag_response", "variant-name").
    Set("$feature_flag", "feature-flag-key"),
})
```

### Java

```java
posthog.capture(
  "distinct_id",
  "$feature_flag_called",
  new HashMap<String, Object>() {
    {
      put("$feature_flag_response", "variant-name");
      put("feature_flag", "feature-flag-key");
    }
  }
);
```

### C#

```csharp
posthog.Capture(
    "distinct_id",
    "$feature_flag_called",
    properties: new() {
        ["$feature_flag_response"] = "variant-name",
        ["feature_flag"] = "feature-flag-key"
    }
);
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better