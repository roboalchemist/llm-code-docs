---
---
title: Screenshots
description: >-
---

Sentry makes it possible to automatically take a screenshot and include it as an attachment when a user experiences an error, an exception or a crash.

This feature is only available for SDKs with a user interface, such as the ones for mobile and desktop applications. In some environments like native iOS, taking a screenshot requires the UI thread and in the event of a crash, that might not be available. Another example where a screenshot might not be available is when the event happens before the screen starts to load. So inherently, this feature is a best effort solution.

## Enabling Screenshots

Because screenshots may contain PII, they are an opt-in feature. You can enable screenshots as shown below:

Capturing a screenshot is a synchronous operation supported on both iOS and Android. For iOS, a UI thread is required.

## Viewing Screenshots

If one is available, you'll see a thumbnail of the screenshot if you click on a specific issue from the  [**Issues**](https://demo.sentry.io/issues/) page:

![Screenshot Thumbnail](./img/screenshot-thumbnail.png)

Once you've clicked on the event ID of a specific issue, you'll be able to see an overview of all the attachments as well as associated events in the "Attachments" tab.

![Screenshots List Example](./img/screenshot-list-example.png)
