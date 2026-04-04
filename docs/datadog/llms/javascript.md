# Source: https://docs.datadoghq.com/feature_flags/client/javascript.md

---
title: JavaScript Feature Flags
description: Set up Datadog Feature Flags for browser JavaScript applications.
breadcrumbs: Docs > Feature Flags > Client-Side Feature Flags > JavaScript Feature Flags
---

# JavaScript Feature Flags

{% callout %}
# Important note for users on the following Datadog sites: app.ddog-gov.com

{% alert level="danger" %}
This product is not supported for your selected [Datadog site](https://docs.datadoghq.com/getting_started/site). ().
{% /alert %}

{% /callout %}

{% callout %}
##### Join the Preview!

Feature Flags are in Preview. Complete the form to request access.

[Request Access](http://datadoghq.com/product-preview/feature-flags/)
{% /callout %}

## Overview{% #overview %}

This page describes how to instrument your browser JavaScript application with the Datadog Feature Flags SDK. Datadog feature flags provide a unified way to remotely control feature availability in your app, experiment safely, and deliver new experiences with confidence.

The Datadog Feature Flags SDK for JavaScript is built on [OpenFeature](https://openfeature.dev/), an open standard for feature flag management. This guide explains how to install the SDK, configure the Datadog provider, and evaluate flags in your application.

## Installation{% #installation %}

Install the Datadog OpenFeature provider and the OpenFeature Web SDK using your preferred package manager:

{% tab title="npm" %}

```bash
npm install @datadog/openfeature-browser @openfeature/web-sdk @openfeature/core
```

{% /tab %}

{% tab title="yarn" %}

```bash
yarn add @datadog/openfeature-browser @openfeature/web-sdk @openfeature/core
```

{% /tab %}

{% tab title="pnpm" %}

```bash
pnpm add @datadog/openfeature-browser @openfeature/web-sdk @openfeature/core
```

{% /tab %}

## Initialize the provider{% #initialize-the-provider %}

Create a `DatadogProvider` instance with your Datadog credentials:

```javascript
import { DatadogProvider } from '@datadog/openfeature-browser';
import { OpenFeature } from '@openfeature/web-sdk';

const provider = new DatadogProvider({
  applicationId: '<APPLICATION_ID>',
  clientToken: '<CLIENT_TOKEN>',
  env: '<ENV_NAME>',
});
```

## Set the evaluation context{% #set-the-evaluation-context %}

Define who or what the flag evaluation applies to using an evaluation context. The evaluation context includes user or session information used to determine which flag variations should be returned. Reference these attributes in your targeting rules to control who sees each variant.

```javascript
const evaluationContext = {
  targetingKey: 'user-123',
  user_id: '123',
  user_role: 'admin',
  email: 'user@example.com',
};

await OpenFeature.setProviderAndWait(provider, evaluationContext);
```

{% alert level="info" %}
The `targetingKey` is used as the randomization subject for percentage-based targeting. When a flag targets a percentage of subjects (for example, 50%), the `targetingKey` determines which "bucket" a user falls into. Users with the same `targetingKey` always receive the same variant for a given flag.
{% /alert %}

## Evaluate flags{% #evaluate-flags %}

After the provider is initialized, you can evaluate flags anywhere in your application. Flag evaluation is *local and instantaneous*âthe SDK uses locally cached data, so no network requests occur when evaluating flags.

### Get a client{% #get-a-client %}

Retrieve the OpenFeature client to evaluate flags:

```javascript
const client = OpenFeature.getClient();
```

### Boolean flags{% #boolean-flags %}

Use `getBooleanValue(key, defaultValue)` for flags that represent on/off or true/false conditions:

```javascript
const isNewCheckoutEnabled = client.getBooleanValue('checkout_new', false);

if (isNewCheckoutEnabled) {
  showNewCheckoutFlow();
} else {
  showLegacyCheckout();
}
```

### String flags{% #string-flags %}

Use `getStringValue(key, defaultValue)` for flags that select between multiple variants or configuration strings:

```javascript
const theme = client.getStringValue('ui_theme', 'light');

switch (theme) {
  case 'dark':
    setDarkTheme();
    break;
  case 'light':
  default:
    setLightTheme();
}
```

### Number flags{% #number-flags %}

Use `getNumberValue(key, defaultValue)` for numeric flags such as limits, percentages, or multipliers:

```javascript
const maxItems = client.getNumberValue('cart_items_max', 20);
const priceMultiplier = client.getNumberValue('pricing_multiplier', 1.0);
```

### Object flags{% #object-flags %}

Use `getObjectValue(key, defaultValue)` for structured configuration data:

```javascript
const config = client.getObjectValue('promo_banner_config', {
  color: '#00A3FF',
  message: 'Welcome!',
});
```

### Flag evaluation details{% #flag-evaluation-details %}

When you need more than just the flag value, use the detail methods. These return both the evaluated value and metadata explaining the evaluation:

```javascript
const details = client.getBooleanDetails('checkout_new', false);

console.log(details.value);       // Evaluated value (true or false)
console.log(details.variant);     // Variant name, if applicable
console.log(details.reason);      // Why this value was chosen
console.log(details.errorCode);   // Error code, if evaluation failed
```

## Complete example{% #complete-example %}

Here's a complete example showing how to set up and use Datadog Feature Flags in a JavaScript application:

```javascript
import { DatadogProvider } from '@datadog/openfeature-browser';
import { OpenFeature } from '@openfeature/web-sdk';

// Initialize the Datadog provider
const provider = new DatadogProvider({
  applicationId: '<APPLICATION_ID>',
  clientToken: '<CLIENT_TOKEN>',
  env: '<ENV_NAME>',
});

// Set the evaluation context
const evaluationContext = {
  targetingKey: 'user-123',
  user_id: '123',
  user_role: 'admin',
};

await OpenFeature.setProviderAndWait(provider, evaluationContext);

// Get the client and evaluate flags
const client = OpenFeature.getClient();
const showNewFeature = client.getBooleanValue('new_feature', false);

if (showNewFeature) {
  console.log('New feature is enabled!');
}
```

## Update the evaluation context{% #update-the-evaluation-context %}

To update the evaluation context after initialization (for example, when a user logs in), use `OpenFeature.setContext()`:

```javascript
await OpenFeature.setContext({
  targetingKey: user.id,
  user_id: user.id,
  email: user.email,
  plan: user.plan,
});
```

## Further reading{% #further-reading %}

- [Client-Side Feature Flags](https://docs.datadoghq.com/feature_flags/client/)
- [OpenFeature Web SDK](https://openfeature.dev/docs/reference/sdks/client/web/)
- [Browser Monitoring](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/)
