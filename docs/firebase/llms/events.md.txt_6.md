# Source: https://firebase.google.com/docs/analytics/web/events.md.txt

<br />

|---|---|
| **Select platform:** | [iOS+](https://firebase.google.com/docs/analytics/ios/events) [Android](https://firebase.google.com/docs/analytics/android/events) [Web](https://firebase.google.com/docs/analytics/web/events) [Flutter](https://firebase.google.com/docs/analytics/flutter/events) [Unity](https://firebase.google.com/docs/analytics/unity/events) [C++](https://firebase.google.com/docs/analytics/cpp/events) |

[Events](https://support.google.com/analytics/answer/9322688)
provide insight on what is happening in your app, such as user actions, system
events, or errors.

Analytics automatically logs some
[events](https://support.google.com/analytics/answer/9234069) for
you; you don't need to add any code to receive them. If your app needs to
collect additional data, you can log up to 500 different Analytics event
*types* in your app (2000 if you're using Google Analytics 360). There's no
limit on the total volume of events your app logs. Note that event names are
case-sensitive and that logging two events whose names differ only in case
results in two distinct events.

## Before you begin

Make sure that you've set up your project and can access Analytics as described
in
[Get Started with Analytics](https://firebase.google.com/docs/analytics/web/get-started).

## Log events

After you have configured the
[`firebase.analytics()`](https://firebase.google.com/docs/reference/js/analytics) instance,
you can begin to log events with the
[`logEvent()`](https://firebase.google.com/docs/reference/js/analytics#logevent)
method. If you're already familiar with Google Analytics, this method is
equivalent to using the `event` command in
[gtag.js](https://developers.google.com/gtagjs/).

To help you get started, the Analytics SDK defines a number of recommended
events that are common among different types of apps, including retail and
ecommerce, travel, and gaming apps. To learn more
[about these events](https://support.google.com/analytics/answer/9322688)
and when to use them, see [Recommended events](https://support.google.com/analytics/answer/9267735).

> [!NOTE]
> **Note:** To get the maximum detail in reports, log the recommended events that make sense for your app and their prescribed parameters. This also ensures that you benefit from the latest Google Analytics features as they become available.

You can find implementation details for several events and their parameters in
the
[gtag.js event reference](https://developers.google.com/gtagjs/reference/event).

The following example demonstrates how to log a `select_content` event:

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

const analytics = getAnalytics();
logEvent(analytics, 'select_content', {
  content_type: 'image',
  content_id: 'P12453'
});
```

### Web

```javascript
analytics.logEvent('select_content', {
  content_type: 'image',
  content_id: 'P12453',
  items: [{ name: 'Kittens' }]
});
```

In addition to the prescribed parameters, you can add the following parameters
to any event:

- Custom parameters: Custom parameters can be used as
  [dimensions or metrics](https://support.google.com/analytics/answer/10075209)
  in [Analytics reports](https://support.google.com/analytics/answer/9212670).
  You can use custom dimensions for non-numerical event parameter data and
  custom metrics for any parameter data better represented numerically. Once
  you've logged a custom parameter using the SDK, register the dimension or
  metric to ensure those custom parameters appear in Analytics
  reports. Do this via: *Analytics \> Events \> Manage Custom Definitions \>
  Create Custom Dimensions*

  Custom parameters can be used in
  [audience](https://support.google.com/firebase/answer/6317509)
  definitions that may be applied to every report.
  Custom parameters are also included in data
  [exported to BigQuery](https://support.google.com/firebase/answer/7030014)
  if your app is linked to a BigQuery project. Find sample queries and much more
  at [Google Analytics 4 BigQuery Export](https://developers.google.com/analytics/bigquery).
- `value` parameter: `value` is a general purpose parameter that is useful for accumulating a key metric that pertains to an event. Examples include revenue, distance, time, and points.

If your application has specific needs not covered by a recommended event type,
you can log your own custom events. For example, if you're developing a game and
want to track when a player completes a particular goal, you could log an event
similar to the following example:

### Web

```javascript
import { getAnalytics, logEvent } from "firebase/analytics";

const analytics = getAnalytics();
logEvent(analytics, 'goal_completion', { name: 'lever_puzzle'});
```

### Web

```javascript
analytics.logEvent('goal_completion', { name: 'lever_puzzle'});
```

## View events in the dashboard

You can view aggregated statistics about your events in the
Firebase console dashboards. These dashboards update periodically
throughout the day. For immediate testing, use the logcat output as described in
the previous section.

You can access this data from the
[**Events**](https://console.firebase.google.com/project/_/analytics/events)
dashboard in the Firebase console. This dashboard shows the event reports
that are automatically created for each distinct type of event logged by
your app.