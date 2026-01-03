---
---
title: OpenTelemetry Agent
description: "Using OpenTelemetry with sentry-opentelemetry-agent."
---

When using `sentry-opentelemetry-agent` you can choose whether the Agent should call `Sentry.init`.
By default the Agent will initialize Sentry for you. If you prefer to manually initialize Sentry or have another integration perform the init you can disable this behaviour.

