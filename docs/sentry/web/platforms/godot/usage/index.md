---
---
title: Usage
description: "Use the SDK to manually capture errors and other events."
---

Sentry's SDK hooks into your runtime environment and automatically reports errors, uncaught exceptions, and unhandled rejections as well as other types of errors depending on the platform.

Key terms:

- An _event_ is one instance of sending data to Sentry. Generally, this data is an error or exception.
- An _issue_ is a grouping of similar events.
- The reporting of an event is called _capturing_.
  When an event is captured, it’s sent to Sentry.

While capturing an event, you can also record the breadcrumbs that lead up to that event. Breadcrumbs are different from events: they will not create an event in Sentry, but will be buffered until the next event is sent. Learn more about breadcrumbs in our Breadcrumbs documentation.

## Capturing Messages

Another common operation is to capture a bare message. A message is textual information that should be sent to Sentry. Typically, our SDKs don't automatically capture messages, but you can capture them manually.

Messages show up as issues on your issue stream, with the message as the issue name.

