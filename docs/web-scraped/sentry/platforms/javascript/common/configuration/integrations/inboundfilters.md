---
---
title: InboundFilters
description: "Allows you to ignore specific errors based on the type, message, or URLs in a given exception. (default)"
---

_Import name: `Sentry.inboundFiltersIntegration`_

This integration is enabled by default. If you'd like to modify your default integrations, read [this](./../#modifying-default-integrations).

This integration allows you to ignore specific errors based on the type, message, or URLs in a given exception.

By default, it'll ignore errors that start with `Script error` or `JavaScript error: Script error`.

To configure this integration, use the `ignoreErrors`, `ignoreTransactions`, `denyUrls`, and `allowUrls` SDK options directly. For example:

```javascript
Sentry.init({
  ignoreErrors: ["ignore-this-error"],
});
```

## Options

Remember to pass these options to the root Sentry.init call, not the integration!

{" "}

### `ignoreErrors`

_Type: `(string|RegExp)[]`_

### `ignoreTransactions`

_Type: `(string|RegExp)[]`_

### `allowUrls`

_Type: `(string|RegExp)[]`_

### `denyUrls`

_Type: `(string|RegExp)[]`_

