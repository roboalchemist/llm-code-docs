# Source: https://www.apollographql.com/docs/graphos/platform/insights/notifications.md

# GraphOS Notifications and Alerts

GraphOS can notify your team about changes to your graph and its performance.
These notifications help you stay up-to-date and address issues as they arise.

## Notification types

GraphOS supports the following notification types:

* [Daily reports](https://www.apollographql.com/docs/graphos/platform/insights/notifications/daily-reports) of your graph's request rate, error rate, and latency
* [Performance alerts](https://www.apollographql.com/docs/graphos/platform/insights/notifications/performance-alerts) whenever metrics like error percentage or request latency exceed a threshold
* [Schema change notifications](https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-changes) whenever your graph's schema is updated
* [Schema proposal notifications](https://www.apollographql.com/docs/graphos/platform/insights/notifications/schema-proposals) whenever a schema proposal is created or revised, or if its status changes
* [Build status notifications](https://www.apollographql.com/docs/graphos/platform/insights/notifications/build-status) whenever GraphOS attempts to compose a supergraph schema

Refer to notification type pages for setup instructions.

## Supported notification channels

GraphOS can send notifications to the indicated channels:

| Notification Type             | Slack | PagerDuty | Custom Webhook |
| :---------------------------- | :---: | :-------: | :------------: |
| Daily reports                 |   ✓   |           |                |
| Schema change notifications   |   ✓   |           |        ✓       |
| Schema proposal notifications |       |           |        ✓       |
| Build status notifications    |       |           |        ✓       |
| Performance alerts            |   ✓   |     ✓     |                |

## Notification availability

### Plan availability

* Custom webhooks are only available with an Enterprise plan.
* Schema proposals and notifications about them are only available with an Enterprise plan.
* Performance alerts are only available with a paid plan.

### Release stage

* Build status notifications are in [preview](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages#preview).
* Performance alerts are [experimental](https://www.apollographql.com/docs/graphos/reference/feature-launch-stages#experimental-features).
