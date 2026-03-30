# Source: https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem_notifications.md

# Problem notifications

## Overview

Problems in StackState generate events that can be used to trigger event notifications.

## Send notifications for problem events

To send a notification when problem events are generated:

1. Install the [Slack StackPack](https://archivedocs.stackstate.com/5.1/stackpacks/integrations/slack).
2. Select the [view](https://archivedocs.stackstate.com/5.1/use/stackstate-ui/views/about_views) that includes the elements for which you would like to receive notifications.
3. You can [add an event handler that listens to problem events](https://archivedocs.stackstate.com/5.1/use/events/manage-event-handlers) in the StackState UI right panel **View summary** tab under **Event handlers**.

{% hint style="success" %}
You can create a [custom event handler function](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/event-handler-functions) to trigger actions or send notifications to systems other than Slack in response to problem events.
{% endhint %}

## See also

* [What is a problem?](https://archivedocs.stackstate.com/5.1/use/problem-analysis/about-problems)
* [Problem navigation](https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem_investigation)
* [Problem lifecycle](https://archivedocs.stackstate.com/5.1/use/problem-analysis/problem-lifecycle)
* [Manage Event Handlers](https://archivedocs.stackstate.com/5.1/use/events/manage-event-handlers)
* [Event handler functions](https://archivedocs.stackstate.com/5.1/develop/developer-guides/custom-functions/event-handler-functions)
