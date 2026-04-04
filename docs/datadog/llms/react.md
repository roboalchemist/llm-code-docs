# Source: https://docs.datadoghq.com/feature_flags/client/react.md

---
title: React Feature Flags
description: Set up Datadog Feature Flags for React applications.
breadcrumbs: Docs > Feature Flags > Client-Side Feature Flags > React Feature Flags
---

# React Feature Flags

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

This page describes how to instrument your React application with the Datadog Feature Flags SDK. Datadog feature flags provide a unified way to remotely control feature availability in your app, experiment safely, and deliver new experiences with confidence.

The Datadog Feature Flags SDK for React is built on [OpenFeature](https://openfeature.dev/), an open standard for feature flag management. This guide explains how to install the SDK, configure the Datadog provider, and evaluate flags in your React components.

## Installation{% #installation %}

Install the Datadog OpenFeature provider and the OpenFeature React SDK using your preferred package manager:

{% tab title="npm" %}

```bash
npm install @datadog/openfeature-browser @openfeature/react-sdk @openfeature/core
```

{% /tab %}

{% tab title="yarn" %}

```bash
yarn add @datadog/openfeature-browser @openfeature/react-sdk @openfeature/core
```

{% /tab %}

{% tab title="pnpm" %}

```bash
pnpm add @datadog/openfeature-browser @openfeature/react-sdk @openfeature/core
```

{% /tab %}

## Initialize the provider{% #initialize-the-provider %}

Create a `DatadogProvider` instance and register it with OpenFeature. Do this as early as possible in your application, before rendering your React components.

```javascript
import { DatadogProvider } from '@datadog/openfeature-browser';

const provider = new DatadogProvider({
  applicationId: '<APPLICATION_ID>',
  clientToken: '<CLIENT_TOKEN>',
  env: '<ENV_NAME>',
});
```

## Set the evaluation context{% #set-the-evaluation-context %}

Define who or what the flag evaluation applies to using an evaluation context. The evaluation context includes user or session information used to determine which flag variations should be returned. Reference these attributes in your targeting rules to control who sees each variant.

Set the provider along with the evaluation context:

```javascript
import { OpenFeature } from '@openfeature/react-sdk';

const evaluationContext = {
  targetingKey: 'user-123',
  user_id: '123',
  email: 'user@example.com',
  tier: 'premium',
};

OpenFeature.setProvider(provider, evaluationContext);
```

{% alert level="info" %}
The `targetingKey` is used as the randomization subject for percentage-based targeting. When a flag targets a percentage of subjects (for example, 50%), the `targetingKey` determines which "bucket" a user falls into. Users with the same `targetingKey` always receive the same variant for a given flag.
{% /alert %}

## Wrap your application{% #wrap-your-application %}

Wrap your application with the `OpenFeatureProvider` component. This makes feature flags available to all child components through React context.

```jsx
import { OpenFeatureProvider } from '@openfeature/react-sdk';

function App() {
  return (
    <OpenFeatureProvider>
      <YourApp />
    </OpenFeatureProvider>
  );
}
```

## Evaluate flags{% #evaluate-flags %}

The OpenFeature React SDK provides hooks for evaluating flags within your components. Each hook returns the flag value based on the evaluation context you configured.

### Boolean flags{% #boolean-flags %}

Use `useBooleanFlagValue(key, defaultValue)` for flags that represent on/off or true/false conditions:

```jsx
import { useBooleanFlagValue } from '@openfeature/react-sdk';

function CheckoutButton() {
  const isNewCheckoutEnabled = useBooleanFlagValue('new_checkout_button', false);

  if (isNewCheckoutEnabled) {
    return <NewCheckoutButton />;
  }

  return <LegacyCheckoutButton />;
}
```

### String flags{% #string-flags %}

Use `useStringFlagValue(key, defaultValue)` for flags that select between multiple variants or configuration strings:

```jsx
import { useStringFlagValue } from '@openfeature/react-sdk';

function ThemedComponent() {
  const theme = useStringFlagValue('ui_theme', 'light');

  switch (theme) {
    case 'dark':
      return <DarkTheme />;
    case 'light':
    default:
      return <LightTheme />;
  }
}
```

### Number flags{% #number-flags %}

Use `useNumberFlagValue(key, defaultValue)` for numeric flags such as limits, percentages, or multipliers:

```jsx
import { useNumberFlagValue } from '@openfeature/react-sdk';

function CartDisplay() {
  const maxItems = useNumberFlagValue('max_cart_items', 20);

  return <Cart maxItems={maxItems} />;
}
```

### Object flags{% #object-flags %}

Use `useObjectFlagValue(key, defaultValue)` for structured configuration data:

```jsx
import { useObjectFlagValue } from '@openfeature/react-sdk';

function Banner() {
  const config = useObjectFlagValue('promo_banner', {
    color: '#00A3FF',
    message: 'Welcome!',
  });

  return <PromoBanner color={config.color} message={config.message} />;
}
```

### Suspense support{% #suspense-support %}

Built-in [suspense](https://react.dev/reference/react/Suspense) support allows you to avoid displaying components with feature flags until provider initialization is complete, or when the context changes. Pass `{ suspend: true }` in the hook options to use this functionality.

For example:

```jsx
import { useBooleanFlag } from '@openfeature/react-sdk';
import { Suspense } from 'react';

import
function Content() {
  // Display a loading message if the component uses feature flags and the provider is not ready
  return (
    <Suspense fallback={"Loading..."}>
      <WelcomeMessage />
    </Suspense>
  );
}

function WelcomeMessage() {
  const { value: showNewMessage } = useBooleanFlag('show-new-welcome-message', false, { suspend: true });

  return (
    <>
      {showNewMessage ? (
        <p>Welcome! You're seeing the new experience.</p>
      ) : (
        <p>Welcome back!</p>
      )}
    </>
  );
}
```

### Flag evaluation details{% #flag-evaluation-details %}

When you need more than just the flag value, use the detail hooks. These return both the evaluated value and metadata explaining the evaluation:

- `useBooleanFlagDetails(key, defaultValue)`
- `useStringFlagDetails(key, defaultValue)`
- `useNumberFlagDetails(key, defaultValue)`
- `useObjectFlagDetails(key, defaultValue)`

For example:

```jsx
import { useStringFlagDetails } from '@openfeature/react-sdk';

function PaywallLayout() {
  const details = useStringFlagDetails('paywall_layout', 'control');

  console.log(details.value);   // Evaluated value (for example: "A", "B", or "control")
  console.log(details.variant); // Variant name, if applicable
  console.log(details.reason);  // Description of why this value was chosen

  return <Layout variant={details.value} />;
}
```

Flag details help you debug evaluation behavior and understand why a user received a given value.

## Complete example{% #complete-example %}

Here's a complete example showing how to set up and use Datadog Feature Flags in a React application:

```jsx
import { Suspense } from 'react';
import { DatadogProvider } from '@datadog/openfeature-browser';
import { OpenFeatureProvider, OpenFeature, useBooleanFlagValue } from '@openfeature/react-sdk';

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

OpenFeature.setProvider(provider, evaluationContext);

// Wrap your app with the OpenFeatureProvider and Suspense for loading state
function App() {
  return (
    <Suspense fallback={<Loading />}>
      <OpenFeatureProvider suspendUntilReady>
        <Page />
      </OpenFeatureProvider>
    </Suspense>
  );
}

// Use feature flags in your components
function Page() {
  const showNewFeature = useBooleanFlagValue('new_feature', false);

  return (
    <div>
      {showNewFeature ? <NewFeature /> : <ExistingFeature />}
    </div>
  );
}
```

## Update the evaluation context{% #update-the-evaluation-context %}

To update the evaluation context after initialization (for example, when a user logs in), use `OpenFeature.setContext()`:

```javascript
// When a user logs in
await OpenFeature.setContext({
  targetingKey: user.id,
  user_id: user.id,
  email: user.email,
  plan: user.plan,
});
```

## Further reading{% #further-reading %}

- [Client-Side Feature Flags](https://docs.datadoghq.com/feature_flags/client/)
- [OpenFeature React SDK](https://openfeature.dev/docs/reference/sdks/client/web/react/)
- [Browser Monitoring](https://docs.datadoghq.com/real_user_monitoring/application_monitoring/browser/)
