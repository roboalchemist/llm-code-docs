# Source: https://docs.datadoghq.com/feature_flags/client.md

---
title: Client-Side Feature Flags
description: Set up Datadog Feature Flags for client-side applications.
breadcrumbs: Docs > Feature Flags > Client-Side Feature Flags
---

# Client-Side Feature Flags

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

Set up Datadog Feature Flags for your applications. Follow the platform-specific guides below to integrate feature flags into your application and start collecting feature flag data:

- [JavaScript](https://docs.datadoghq.com/feature_flags/client/javascript/)
- [React](https://docs.datadoghq.com/feature_flags/client/react/)
- [Android](https://docs.datadoghq.com/feature_flags/client/android/)
- [Android TV](https://docs.datadoghq.com/feature_flags/client/android/)
- [iOS](https://docs.datadoghq.com/feature_flags/client/ios/)
- [tvOS](https://docs.datadoghq.com/feature_flags/client/ios/)

## Context attribute requirements{% #context-attribute-requirements %}

{% alert level="warning" %}
Evaluation context attributes must be flat primitive values (strings, numbers, booleans). Nested objects and arrays are **not supported** and will cause exposure events to be silently dropped.
{% /alert %}

Use flat attributes in your evaluation context:

```javascript
const evaluationContext = {
  targetingKey: 'user-123',
  userId: 'user-123',
  tier: 'premium',
  age: 25
};

await OpenFeature.setProviderAndWait(provider, evaluationContext);
```

Avoid nested objects and arrays:

```javascript
// These attributes will cause exposure events to be dropped
const evaluationContext = {
  targetingKey: 'user-123',
  user: { id: 'user-123' },        // nested object - NOT SUPPORTED
  features: ['beta', 'analytics']  // array - NOT SUPPORTED
};
```

## Further reading{% #further-reading %}

- [Learn about Feature Flags](https://docs.datadoghq.com/feature_flags/)
- [Getting Started with Feature Flags](https://docs.datadoghq.com/getting_started/feature_flags/)
- [Server-Side Feature Flags](https://docs.datadoghq.com/feature_flags/server/)
