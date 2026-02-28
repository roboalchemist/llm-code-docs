# Source: https://docs.datadoghq.com/error_tracking/frontend/replay_errors.md

---
title: Error Tracking Replay Snippets
description: >-
  Learn about how to collect replay snippets to ensure you are seeing the issues
  that matter to you.
breadcrumbs: >-
  Docs > Error Tracking > Frontend Error Tracking > Error Tracking Replay
  Snippets
---

# Error Tracking Replay Snippets

{% callout %}
##### Join the Preview!

Error Tracking Replay snippets is in Preview.

[Request Access](https://www.datadoghq.com/product-preview/error-tracking-replay-snippets/)
{% /callout %}

## Overview{% #overview %}

As a frontend engineer, an essential and often time-consuming part of the debugging process is reproducing bugs. But it can be difficult to do so without a clear understanding of the actions a user took before your application throws an error.

Error Tracking Replay Snippets allows you to view a pixel-perfect recreation of a user's journey 15 seconds before and after an error occurred so you can reproduce bugs, save time, and eliminate any guesswork.

## Setup{% #setup %}

1. If you have not set up Datadog Frontend Error Tracking, follow the [in-app setup instructions](https://app.datadoghq.com/error-tracking/settings/setup/client) or see the setup documentation for [browser](https://docs.datadoghq.com/error_tracking/frontend/browser#setup) and [mobile](https://docs.datadoghq.com/error_tracking/frontend/mobile).

1. During SDK initialization, configure your application's replay sample rate.

   {% tab title="Browser" %}
Set the `sessionReplaySampleRate` between 1 and 100.

   ```javascript
   import { datadogRum } from '@datadog/browser-rum';

   datadogRum.init({
      applicationId: '<APP_ID>',
      clientToken: '<CLIENT_TOKEN>',
      service: '<SERVICE>',
      env: '<ENV_NAME>',
      sessionReplaySampleRate: 20,
      trackResources: true,
      trackUserInteractions: true,
   });
   ```

      {% /tab %}

   {% tab title="iOS" %}
Follow [these steps](https://docs.datadoghq.com/session_replay/mobile/setup_and_configuration/?tab=ios) to setup and configure your mobile application's error replay for this platform.
   {% /tab %}

   {% tab title="Android" %}
Follow [these steps](https://docs.datadoghq.com/session_replay/mobile/setup_and_configuration/?tab=android) to setup and configure your mobile application's error replay for this platform.
   {% /tab %}

   {% tab title="Kotlin Multiplatform" %}
Follow [these steps](https://docs.datadoghq.com/session_replay/mobile/setup_and_configuration/?tab=kotlinmultiplatform) to setup and configure your mobile application's error replay for this platform.
   {% /tab %}

   {% tab title="React Native" %}
Follow [these steps](https://docs.datadoghq.com/session_replay/mobile/setup_and_configuration/?tab=reactnative) to setup and configure your mobile application's error replay for this platform.
   {% /tab %}

## Replay errors{% #replay-errors %}

After reviewing key information about the error, such as the error message and stack trace, you can immediately pivot directly from the issue summary to a live reproduction of the most recent session that experienced the error. Scroll down below the stack trace and click on the preview of the replay to see a users actions before the error occurred.

{% image
   source="https://datadog-docs.imgix.net/images/error_tracking/error-replay.4e0eb2fa6be143008a5cc872d7feae68.png?auto=format"
   alt="Error Tracking Replay Snippet" /%}

## Further Reading{% #further-reading %}

- [Learn about how Error Tracking can identify suspect commits](https://docs.datadoghq.com/error_tracking/suspect_commits)
- [Learn about Error Tracking](https://docs.datadoghq.com/error_tracking)
