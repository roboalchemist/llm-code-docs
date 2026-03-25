# Source: https://posthog.com/docs/product-analytics/identify.md

# Identifying users - Docs

Linking events to specific users enables you to build a full picture of how they're using your product across different sessions, devices, and platforms.

This is straightforward to do when [capturing backend events](/docs/product-analytics/capture-events?tab=Node.js.md), as you associate events to a specific user using a `distinct_id`, which is a required argument.

However, in the frontend of a [web](/docs/libraries/js/features.md#capturing-events) or [mobile app](/docs/libraries/ios.md#capturing-events), a `distinct_id` is not a required argument — PostHog's SDKs will generate an anonymous `distinct_id` for you automatically and you can capture events anonymously, provided you use the appropriate [configuration](/docs/libraries/js/features.md#capturing-anonymous-events).

To link events to specific users, call `identify`:

PostHog AI

### Web

```javascript
posthog.identify(
  'distinct_id',  // Replace 'distinct_id' with your user's unique identifier
  { email: 'max@hedgehogmail.com', name: 'Max Hedgehog' } // optional: set additional person properties
);
```

### Android

```kotlin
PostHog.identify(
    distinctId = distinctID, // Replace 'distinctID' with your user's unique identifier
    // optional: set additional person properties
    userProperties = mapOf(
        "name" to "Max Hedgehog",
        "email" to "max@hedgehogmail.com"
    )
)
```

### iOS

```swift
PostHogSDK.shared.identify("distinct_id", // Replace "distinct_id" with your user's unique identifier
                           userProperties: ["name": "Max Hedgehog", "email": "max@hedgehogmail.com"]) // optional: set additional person properties
```

### React Native

```jsx
posthog.identify('distinct_id', { // Replace "distinct_id" with your user's unique identifier
    email: 'max@hedgehogmail.com', // optional: set additional person properties
    name: 'Max Hedgehog'
})
```

### Dart

```dart
await Posthog().identify(
  userId: 'distinct_id', // Replace "distinct_id" with your user's unique identifier
  userProperties: {
    email: "max@hedgehogmail.com", // optional: set additional person properties
    name: "Max Hedgehog"
});
```

Events captured after calling `identify` are identified events and this creates a person profile if one doesn't exist already.

Due to the cost of processing them, anonymous events can be up to 4x cheaper than identified events, so it's recommended you only capture identified events when needed.

## How identify works

When a user starts browsing your website or app, PostHog automatically assigns them an **anonymous ID**, which is stored locally.

Provided you've [configured persistence](/docs/libraries/js/persistence.md) to use cookies or `localStorage`, this enables us to track anonymous users – even across different sessions.

By calling `identify` with a `distinct_id` of your choice (usually the user's ID in your database, or their email), you link the anonymous ID and distinct ID together.

Thus, all past and future events made with that anonymous ID are now associated with the distinct ID.

This enables you to do things like associate events with a user from before they log in for the first time, or associate their events across different devices or platforms.

Using identify in the backend

Although you can call `identify` using our backend SDKs, it is used most in frontends. This is because there is no concept of anonymous sessions in the backend SDKs, so calling `identify` only updates person profiles.

## Best practices when using identify

### 1\. Call `identify` as soon as you're able to

In your frontend, you should call `identify` as soon as you're able to.

Typically, this is every time your **app loads** for the first time, and directly after your **users log in**.

This ensures that events sent during your users' sessions are correctly associated with them.

You only need to call `identify` once per session, and you should avoid calling it multiple times unnecessarily.

If you call `identify` multiple times with the same data without reloading the page in between, PostHog will ignore the subsequent calls.

### 2\. Use unique strings for distinct IDs

If two users have the same distinct ID, their data is merged and they are considered one user in PostHog. Two common ways this can happen are:

-   Your logic for generating IDs does not generate sufficiently strong IDs and you can end up with a clash where 2 users have the same ID.
-   There's a bug, typo, or mistake in your code leading to most or all users being identified with generic IDs like `null`, `true`, or `distinctId`.

PostHog also has built-in protections to stop the most common distinct ID mistakes.

### 3\. Set up person profiles and properties

You'll notice that one of the parameters in the `identify` method is a `properties` object.

This enables you to set [person properties](/docs/product-analytics/person-properties.md).

Whenever possible, we recommend passing in all person properties you have available each time you call identify, as this ensures their person profile on PostHog is up to date.

Person properties can also be set being adding a `$set` property to a event `capture` call.

See our [person properties docs](/docs/product-analytics/person-properties.md) for more details on how to work with them and best practices.

## Get the current user's distinct ID

You may find it helpful to get the current user's distinct ID. For example, to check whether you've already called `identify` for a user or not.

To do this, call the following:

PostHog AI

### Web

```javascript
posthog.get_distinct_id()
```

### iOS

```swift
PostHogSDK.shared.getDistinctId()
```

### Android

```kotlin
PostHog.distinctId()
```

### React Native

```jsx
posthog.get_distinct_id()
```

### Flutter

```dart
Posthog().getDistinctId()
```

The ID returned is either the ID automatically generated by PostHog or the ID that has been passed by a call to `identify()`.

## Reset

If a user logs out on your frontend, you should call `reset()` to unlink any future events made on that device with that user.

This is important if your users are sharing a computer, as otherwise all of those users are grouped together into a single user due to shared cookies between sessions.

**We strongly recommend you call `reset` on logout even if you don't expect users to share a computer.**

You can do that like so:

PostHog AI

### Web

```javascript
posthog.reset()
```

### iOS

```swift
PostHogSDK.shared.reset()
```

### Android

```kotlin
PostHog.reset()
```

### React Native

```jsx
posthog.reset()
```

### Dart

```dart
Posthog().reset()
```

If you *also* want to reset the `device_id` so that the device will be considered a new device in future events, you can pass `true` as an argument:

Web

PostHog AI

```javascript
posthog.reset(true)
```

## Alias: Assigning multiple distinct IDs to the same user

Sometimes, you want to assign multiple distinct IDs to a single user. For example, if a distinct ID which is typically used on the frontend is not available in certain parts of your backend code, you can use `alias` to connect the frontend distinct ID to one accessible on the backend. This will merge all past and future events into the same user.

In the below example, we assign the user with `frontend_id` another ID: `backend_id`. This means that any events submitted using either `frontend_id` or `backend_id` will be associated with the same user.

PostHog AI

### Node.js

```javascript
client.alias({
    distinctId: 'frontend_id',
    alias: 'backend_id',
})
```

### Web

```javascript
posthog.alias('backend_id', 'frontend_id');
```

### Python

```python
posthog.alias(previous_id='frontend_id', distinct_id='backend_id')
```

### PHP

```php
PostHog::alias([
  'distinctId' => 'frontend_id',
  'alias' => 'backend_id'
]);
```

### Ruby

```ruby
posthog.alias(
  distinct_id: "frontend_id",
  alias: "backend_id"
)
```

### Go

```go
client.Enqueue(posthog.Alias{
  DistinctId: "frontend_id",
  Alias: "backend_id",
})
```

### Java

```java
posthog.alias("frontend_id", "backend_id");
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "properties": {
        "distinct_id": "frontend_id",
        "alias": "backend_id"
    },
    "timestamp": "2020-08-16 09:03:11.913767",
    "event": "$create_alias"
}' https://us.i.posthog.com/i/v0/e/
```

There are two requirements when assigning an `alias_id`:

1.  It cannot be associated with more than one `distinct_id`.
2.  The `alias_id` **must not** have been previously used as the `distinct_id` argument of an `identify()` or `alias()` call. For example: Assume we previously called `posthog.identify('distinct_id_one')`. It is not possible to use `distinct_id_one` as an alias ID:

PostHog AI

### Node.js

```javascript
// Assume we previously identified a user with 'user1' using posthog.identify('user1')
// You should not use user1 as an alias for user2
client.alias({
    distinctId: 'user2',
    alias: 'user1',
})
```

### Web

```javascript
// Assume we previously identified a user with 'user1' using posthog.identify('user1')
// You should not use user1 as an alias for user2
client.alias({
    distinctId: 'user2',
    alias: 'user1',
})
```

### Python

```python
# Assume we previously identified a user with 'user1' using posthog.identify('user1')
# You should not use user1 as an alias for user2
posthog.alias('user2', 'user1');
```

### PHP

```php
# Assume we previously identified a user with 'user1' using posthog.identify('user1')
# ❌ The following is not possible:
# You cannot use user1 as an alias for user2
PostHog::alias([
  'distinctId' => 'user2',
  'alias' => 'user1'
]);
```

### Ruby

```ruby
# Assume we previously identified a user with 'user1' using posthog.identify('user1')
# You should not use user1 as an alias for user2
posthog.alias({
  distinct_id: "user2",
  alias: "user1",
})
```

### Go

```go
// Assume we previously identified a user with 'user1' using posthog.identify('user1')
// You should not use user1 as an alias for user2
client.Enqueue(posthog.Alias{
  DistinctId: "user2",
  Alias: "user1",
})
```

### Java

```java
// Assume we previously identified a user with 'user1' using posthog.identify('user1')
// You should not use user1 as an alias for user2
posthog.alias("user2", "user1");
```

You can view whether a user can be merged into another user using `alias` when [viewing their properties](/docs/data/user-properties.md#how-to-view-user-properties) in the PostHog app: Under their ID, you'll see `Merge restrictions`. This will indicate whether there are merge restrictions or not – i.e., whether you can use their ID as an `alias_id` or not.

![Merge restrictions tooltipl](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/data/identify/merge-restrictions-tooltip-light-mode.png)![Merge restrictions tooltipl](https://res.cloudinary.com/dmukukwp6/image/upload/v1710055416/posthog.com/contents/images/docs/data/identify/merge-restrictions-tooltip-dark-mode.png)

> **Note:** When calling `alias` in the frontend SDKs, if you have set any properties onto the anonymous user, they are merged into the user with `distinct_id`. For more details, see the FAQ on [how properties are managed when identifying anonymous users](/docs/data/identify.md#how-are-properties-managed-when-identifying-anonymous-users).

## Troubleshooting and FAQs

### What happens if you call `identify` or `alias` with invalid inputs?

When calling either of these with invalid inputs (such as in the examples described in this doc e.g., using null strings with `identify`, or by trying to use a distinct ID of another user as an alias ID), the following will happen:

1.  We process the event normally (it will be ingested and show up in the UI).
2.  Merging users will be refused and an ingestion warning will be logged (see [ingestion warnings](/manual/data-management.md#ingestion-warnings) for more details).
3.  The event will be only be tied to the user associated with `distinct_id`.

PostHog also has built-in protections to stop the most common distinct ID mistakes. See the FAQ at the end of this page for more details.

-   We do not allow identifying users with empty space strings of any length – e.g.,`' '`, `' '`, etc.

-   We do not allow identifying users with the following strings (case insensitive):

    -   `anonymous`
    -   `guest`
    -   `distinctid`
    -   `distinct_id`
    -   `id`
    -   `not_authenticated`
    -   `email`
    -   `undefined`
    -   `true`
    -   `false`
-   We do not allow identifying users with the following strings (case sensitive):

    -   `[object Object]`
    -   `NaN`
    -   `None`
    -   `none`
    -   `null`
    -   `0`
-   We do not allow identifying a user that has already been identified with a different distinct ID. For example:

PostHog AI

### Web

```javascript
posthog.identify(
    'distinct_id_one',
    {},
    {},
);
posthog.identify(
    'distinct_id_two',
    {},
    {},
);
// ❌ Not possible, since we already identified this user with "distinct_id_one"
// so we cannot identify them again with a different distinct ID "distinct_id_two"
```

### Android

```kotlin
PostHog.identify(distinctId = "distinct_id_one")
PostHog.identify(distinctId = "distinct_id_two")
// ❌ Not possible, since we already identified this user with "distinct_id_one"
// so we cannot identify them again with a different distinct ID "distinct_id_two"
```

### iOS

```swift
PostHogSDK.shared.identify("distinct_id_one",
                           userProperties: [:])
PostHogSDK.shared.identify("distinct_id_two",
                           userProperties: [:])
// ❌ Not possible, since we already identified this user with "distinct_id_one"
// so we cannot identify them again with a different distinct ID "distinct_id_two"
```

### How to merge users

It may happen that, due to implementation issues, the same user in your product has multiple users in PostHog associated with them. In these cases, you can use `$merge_dangerously` to merge multiple PostHog users into a single user.

> **⚠️ Warnings:**
>
> 1.  Merging users with `$merge_dangerously` is irreversible and has no safeguards! Be careful not to merge users who should not be merged together. Due to the dangers, we don't recommend you merge users frequently, but rather as a one-off for recovering from implementation problems.
> 2.  Before using `$merge_dangerously`, first check if [alias](/docs/product-analytics/identify.md#alias-assigning-multiple-distinct-ids-to-the-same-user) would better suit your needs.

Merging users is done by sending a `$merge_dangerously` event:

PostHog AI

### Node.js

```javascript
client.capture({
    distinctId: 'distinct_id_of_user_to_merge_into',
    event: '$merge_dangerously',
    properties: {
        alias: 'distinct_id_of_user_to_be_merged',
    },
})
```

### Web

```javascript
// This will merge distinct_id_of_user_to_be_merged into the user sending this event
posthog.capture({
    '$merge_dangerously',
    {
        alias: 'distinct_id_of_user_to_be_merged',
    },
})
```

### py

```py
posthog.capture(
  '$merge_dangerously',
  distinct_id='distinct_id_of_user_to_merge_into',
  {'alias': 'distinct_id_of_user_to_be_merged'}
)
```

### Go

```go
client.Enqueue(posthog.Capture{
  DistinctId: "distinct_id_of_user_to_merge_into",
  Event:      "$merge_dangerously",
  Properties: posthog.NewProperties().
    Set("alias", "distinct_id_of_user_to_be_merged"),
})
```

### Ruby

```ruby
posthog.capture({
    distinct_id: 'distinct_id_of_user_to_merge_into',
    event: '$merge_dangerously',
    properties: {
        alias: 'distinct_id_of_user_to_be_merged'
    }
})
```

### Terminal

```bash
curl -v -L --header "Content-Type: application/json" -d '{
    "api_key": "<ph_project_token>",
    "properties": {
      "alias": "distinct_id_of_user_to_be_merged"
    },
    "timestamp": "2020-08-16 09:03:11.913767",
    "distinct_id": "distinct_id_of_user_to_merge_into",
    "event": "$merge_dangerously"
}' https://us.i.posthog.com/i/v0/e/
```

### How to identify users across platforms

We recommend you call `identify` [as soon as you're able](#1-call-identify-as-soon-as-youre-able), typically when a user signs up or logs in.

This doesn't work if one or both platforms are unauthenticated. Some examples of such cases are:

-   Onboarding and signup flows before authentication.
-   Unauthenticated web pages redirecting to authenticated mobile apps.
-   Authenticated web apps prompting an app download.

In these cases, you can use a [deep link](https://developer.android.com/training/app-links/deep-linking) on Android and [universal links](https://developer.apple.com/documentation/xcode/supporting-universal-links-in-your-app) on iOS to identify users.

1.  Use `posthog.get_distinct_id()` to get the current distinct ID. Even if you cannot call identify because the user is unauthenticated, this will return an anonymous distinct ID generated by PostHog.
2.  Add the distinct ID to the deep link as query parameters, along with other properties like UTM parameters.
3.  When the user is redirected to the app, parse the deep link and handle the following cases:

-   The user is already authenticated on the mobile app. In this case, call [`posthog.alias()`](/docs/libraries/js/features.md#alias) with the distinct ID from the web. This associates the two distinct IDs as a single person.
-   The user is unauthenticated. In this case, call [`posthog.identify()`](/docs/libraries/js/features.md#identifying-users) with the distinct ID from the web. Events will be associated with this distinct ID.

As long as you associate the distinct IDs with `posthog.identify()` or `posthog.alias()`, you can track events generated across platforms.

### How to split a merged user back into separate users

If you've accidentally linked distinct IDs together that represent different users, or you've made a mistake when merging users, it's possible to split their combined user back into separate users. You can do this in the PostHog app by navigating to the user you'd like split, and then clicking "Split IDs" in the top right corner.

> **Warning:** This will treat the distinct IDs as separate users for future events. However, there is no guarantee as to how past events will be treated – they may be be considered separate users, or be considered a single user for some or all events.

### How are properties managed when merging users?

When a `User B` is merged into another `User A`, all the properties of the `User B` are added to `User A`. If there is a conflict, the properties of `User A` are prioritized over `User B`. For example:

Node.js

PostHog AI

```javascript
/* Assume User A has the properties:
{
        name: 'User A',
        location: 'London',
}
*/
/* Assume User B has the properties:
{
        name: 'User B',
        location: 'Rome',
        phone: '0800-POSTHOG',
}
*/
client.capture({
    distinctId: 'distinct_id_of_user_A',
    event: '$merge_dangerously',
    properties: {
        alias: 'distinct_id_of_user_B',
    },
})
/* User B has merged into User A. The resulting user will now have properties:
{
  name: 'User A',
  location: 'London',
  phone: '0800-POSTHOG',
}
*/
```

### How are properties managed when identifying anonymous users?

When an anonymous user is identified as `User A`, all the properties of the anonymous user are added to `User A`. If there is a conflict, the properties of `User A` are prioritized over the anonymous user. For example:

Web

PostHog AI

```javascript
/* Assume existing User A has the properties:
{
        name: 'User A',
        location: 'London',
        timezone: 'GMT',
}
*/
/* Assume User A uses your app on a new device,
but has not yet logged in and so identify has not been called.
They are still an "anonymous user"
New properties are set for this "anonymous user"
*/
posthog.capture(
    'event_name',
    {
        $set: {
            name: 'Anonymous User',
            phone: '0800-POSTHOG',
          },
    }
)
// After log in, we identify the user as User A
client.identify({
    distinctId: 'user_A',
    properties: {
        timezone: 'GMT+8',
    },
})
/* User A will now have properties:
{
  name: 'User A',
  location: 'London',
  phone: '0800-POSTHOG',
  timezone: 'GMT+8'
}
*/
```

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better