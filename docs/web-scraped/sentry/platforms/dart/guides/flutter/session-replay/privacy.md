---
---
title: Privacy
description: "Learn about the privacy-oriented settings for Session Replay."
---

Before enabling Session Replay in production, verify your masking configuration to ensure no sensitive data is captured. Our default settings aggressively mask potentially sensitive data, but if you modify these settings or update UI frameworks or system SDKs, you must thoroughly test your application. If you find any masking issues or sensitive data that should be masked but isn't, please [create a GitHub issue](https://github.com/getsentry/sentry-dart/issues/new/choose) and avoid deploying to production with Session Replay enabled until the issue is resolved.

