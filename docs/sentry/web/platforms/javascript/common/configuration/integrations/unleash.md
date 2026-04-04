---
---
title: Unleash
description: "Learn how to use Sentry with Unleash."
---

This integration only works inside a browser environment. It is only available from a package-based install (e.g. `npm` or `yarn`).

The [Unleash](https://www.getunleash.io/) integration tracks feature flag evaluations produced by the Unleash SDK. These evaluations are held in memory and are sent to Sentry on error and transaction events. **At the moment, we only support boolean flag evaluations from Unleash's isEnabled method.** This integration is available in Sentry SDK **versions 8.51.0 or higher.**

_Import names: `Sentry.unleashIntegration`_

Before using this integration, you need to install and instrument Unleash in your app. Learn more by reading [Unleash's SDK reference](https://docs.getunleash.io/reference/sdks/javascript-browser) and [quickstart](https://docs.getunleash.io/quickstart).

The `unleashClientClass` option has been renamed to `featureFlagClientClass` in v9 of the Sentry SDK. Please update accordingly.

Visit the Sentry website and confirm that your error event has recorded the feature flag "test-flag" and its value "false".

