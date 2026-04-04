---
---
title: Screenshots
description: >-
---

Sentry makes it possible to automatically take a screenshot and include it as an attachment when a user experiences an error, an exception or a crash.

This feature is only available for SDKs with a user interface, like the ones for mobile and desktop applications. It's also limited by whether taking a screenshot is possible or not. For example, in some environments, like native iOS, taking a screenshot requires the UI thread, which often isn't available in the event of a crash. Another example where a screenshot might not be available is when the event happens before the screen starts to load. So inherently, this feature is a best effort solution.

## Enabling Screenshots

Because screenshots may contain PII, they are an opt-in feature.

## Viewing Screenshots

If one is available, you'll see a thumbnail of the screenshot when you click on a specific issue from the [**Issues**](https://demo.sentry.io/issues/) page.

![Screenshot Thumbnail](./img/screenshot-thumbnail.png)

Once you've clicked on the event ID of a specific issue, you'll be able to see an overview of all the attachments as well as associated events in the "Attachments" tab.

![Screenshots List Example](./img/screenshot-list-example.png)
