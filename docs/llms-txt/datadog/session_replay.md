# Source: https://docs.datadoghq.com/session_replay.md

---
title: Session Replay
description: >-
  Learn about how to capture and visually replay your users' web browsing or
  mobile app experience with Session Replay.
breadcrumbs: Docs > Session Replay
source_url: https://docs.datadoghq.com/index.html
---

# Session Replay

## Overview{% #overview %}

Session Replay expands your user experience monitoring by allowing you to capture and visually replay the web browsing or mobile app experience of your users. Session Replay is available in both [RUM](https://docs.datadoghq.com/real_user_monitoring/) and [Product Analytics](https://docs.datadoghq.com/product_analytics/), helping you identify and reproduce errors, understand user journeys, and gain insights into your application's usage patterns and design pitfalls.

## Browser Session Replay{% #browser-session-replay %}

Browser Session Replay expands your user experience monitoring by allowing you to capture and visually replay the web browsing experience of your users. Combined with RUM performance data, Session Replay is beneficial for error identification, reproduction, and resolution, and provides insights into your web application's usage patterns and design pitfalls.

The RUM Browser SDK is [open source](https://github.com/DataDog/browser-sdk) and leverages the open source [rrweb](https://www.rrweb.io/) project.

Learn more about the [Session Replay for Browsers](https://docs.datadoghq.com/session_replay/browser/).

## Mobile Session Replay{% #mobile-session-replay %}

Mobile Session Replay expands visibility into your mobile applications by visually replaying each user interaction, such as taps, swipes, and scrolls. It is available for native apps on both Android and iOS. Visually replaying user interactions on your applications makes it easier to reproduce crashes and errors, as well as understand the user journey for making UI improvements.

Learn more about the [Session Replay for Mobile](https://docs.datadoghq.com/session_replay/mobile/).

## Extend data retention{% #extend-data-retention %}

By default, Session Replay data is retained for 30 days.

To extend Session Replay data retention to 15 months, you can enable *Extended Retention* on individual session replays. These sessions must be non-active (the user has completed their experience).

To access any Session Replay at a later time, Datadog recommends saving the URL or adding it to a [Playlist](https://docs.datadoghq.com/session_replay/playlists).

Extended Retention only applies to Session Replay and does not include associated events. The 15 months start when Extended Retention is enabled, not when the session is collected.

You can disable Extended Retention at any time. If the session replay is still within its default 30 days of retention, the replay expires at the end of the initial 30 day window. If you disable Extended Retention on a session replay that is older than 30 days, the replay immediately expires.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/session_replay/extended-retention-1.893d77b6e64d929aaa3d80f66c4b130c.png?auto=format"
   alt="Enable extended retention" /%}

Refer to the below diagram to understand what data is retained with extended retention.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/session_replay/replay-extended-retention-1.7015fdbdcd7a3370a400c7e7537bc324.png?auto=format"
   alt="Diagram of what data is retained with extended retention" /%}

## Playback history{% #playback-history %}

You can see who has watched a given session replay by clicking the **watched** count displayed on the player page. This feature allows you to check whether someone you'd like to share the recording with has already watched it.

{% image
   source="https://datadog-docs.imgix.net/images/real_user_monitoring/session_replay/session-replay-playback-history.8b6e074d2e529aaf5cbc79505db64d73.png?auto=format"
   alt="Check who has watched a session's recording" /%}

The history includes only playbacks that occurred in the player page or in an embedded player, like in a [Notebook](https://docs.datadoghq.com/notebooks/) or side panel. Included playbacks also generate an [Audit Trail](https://docs.datadoghq.com/account_management/audit_trail/) event. Thumbnail previews are not included in history.

To view your own playback history, check out the [My Watch History](https://docs.datadoghq.com/rum/replay/playlists/my-watch-history) playlist.

## Playlists{% #playlists %}

You can create a playlist of Session Replays to organize them by any patterns you notice. Learn more about [Session Replay Playlists](https://docs.datadoghq.com/session_replay/playlists).

## Dev Tools{% #dev-tools %}

Dev Tools is a built-in debugging panel in Session Replay that exposes key information during playback. Use it to identify issues, trace requests, and understand performance bottlenecksâall without reproducing the issue yourself. Dev Tools are available for [RUM](https://docs.datadoghq.com/real_user_monitoring/) sessions.

Learn more about Dev Tools for [browser](https://docs.datadoghq.com/session_replay/browser/dev_tools/) and [mobile](https://docs.datadoghq.com/session_replay/mobile/dev_tools/).

## Further reading{% #further-reading %}

- [Use Datadog Session Replay to view real-time user journeys](https://www.datadoghq.com/blog/session-replay-datadog/)
- [Use funnel analysis to understand and optimize key user flows](https://www.datadoghq.com/blog/reduce-customer-friction-funnel-analysis/)
- [Visually replay user-facing issues with Zendesk and Datadog Session Replay](https://www.datadoghq.com/blog/zendesk-session-replay-integration/)
- [Visualize your RUM data in the Explorer](https://docs.datadoghq.com/real_user_monitoring/explorer)
- [Detect and aggregate CSP violations with Datadog](https://docs.datadoghq.com/integrations/content_security_policy_logs)
