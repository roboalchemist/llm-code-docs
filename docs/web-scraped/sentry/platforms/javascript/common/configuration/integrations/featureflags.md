---
---
title: Generic Feature Flags Integration
description: "Learn how to attach custom feature flag data to Sentry error events."
---

The Feature Flags integration allows you to manually track feature flag evaluations through an API.
These evaluations are held in memory and sent to Sentry on error and transaction events.
**At the moment, we only support boolean flag evaluations.**

_Import names: `Sentry.featureFlagsIntegration` and `type Sentry.FeatureFlagsIntegration`_

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

