# Source: https://docs.datadoghq.com/feature_flags/guide/migrate_from_statsig.md

---
title: Migrate Your Feature Flags from Statsig
description: Learn how to migrate feature flags from Statsig to Eppo by Datadog.
breadcrumbs: >-
  Docs > Feature Flags > Feature Flags Guides > Migrate Your Feature Flags from
  Statsig
---

# Migrate Your Feature Flags from Statsig

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

This guide walks you through the process of migrating feature flags from Statsig to [Eppo by Datadog](https://geteppo.com/), as an intermediate step before fully migrating to Datadog's dedicated [Feature Flags](https://docs.datadoghq.com/feature_flags/) product. Follow these general steps:

1. Install the Eppo SDK.
1. Create a feature flag in Eppo and verify its functionality.
1. Identify critical feature flags in Statsig.
1. For all non-critical flags, remove existing code.
1. For critical flags, create a fallback value in a wrapper.
1. Recreate critical feature flags in Eppo.
1. Switch existing flags to the new application.

{% alert level="info" %}
Unless otherwise specified, all code examples are in TypeScript.
{% /alert %}

## Migration process{% #migration-process %}

### 1. Install the Eppo SDK{% #install-sdk %}

1. Log in to Eppo at [https://eppo.cloud/](https://eppo.cloud/).

1. Generate an SDK key by navigating to **Flags** > **Environments**, then clicking **Create** > **SDK Key**.

1. Define a logging function for the Eppo SDK to log assignments so they end up in your data warehouse.

   ```typescript
   const assignmentLogger: IAssignmentLogger = {
     logAssignment(assignment) {
       analytics.track({
         userId: assignment.subject,
         event: "Eppo Randomization Event",
         type: "track",
         properties: { ...assignment },
       });
     },
   };

   ```

1. Initialize the SDK in your code. For instructions for your language, see [SDK guides](https://docs.geteppo.com/sdks/).

   ```typescript
   await init({
     apiKey: EPPO_SDK_KEY,
     assignmentLogger,
   });

   ```

### 2. Set up and verify a new flag{% #set-up-flag %}

1. Create a flag in Eppo by navigating to **Flags** > **Feature Flags**, then clicking **Create Flag** > **Feature Flag**.

1. Implement the flag in your application code.

1. Test the flag in your local development environment to ensure it works as expected.

   ```typescript
   const variation = getInstance().getBooleanAssignment(
     'show-new-feature',
     user.id,
     {
       'country': user.country,
       'device': user.device
     },
     false
   );

   ```

1. Deploy the application to your staging or testing environments and verify the flag's functionality.

1. Deploy the application to your production environment and test the flag again.

### 3. Identify critical flags in Statsig{% #identify-critical-flags %}

1. Make a list of all the feature flags currently in use within your application.
1. Categorize the flags as critical or non-critical based on their importance and impact on your application's functionality.
1. Flags that are disabled or are rolled out to 100% can be categorized as non-critical.

### 4. Remove non-critical flag code{% #remove-non-critical-flags %}

1. For the non-critical flags identified in the previous step, remove the flag code from your application and from Statsig. They are no longer relevant.
1. Test your application thoroughly to ensure that the removal of these flags does not introduce any regressions or unintended behavior.

### 5. Create fallback values for critical flags{% #create-fallback-values %}

1. Implement a function that wraps calling Eppo's SDK to have a fallback mechanism to use the Statsig flag values if the new service is unavailable or experiences issues.

1. When attempting to retrieve a flag value from Eppo, catch any exceptions or errors that may occur due to service unavailability or issues and return the old value.

1. Eppo SDKs use only strongly typed assignment functions (for example, `getBooleanAssignment`), whereas Statsig SDKs use specific evaluation functions for different types. For such SDKs, it's recommended to create wrappers for each type. You can then replace uses of the Statsig functions with the typed wrappers in your application. Here are examples:

   ```typescript
   // After initialization, turn off graceful failure so exceptions are rethrown
   getInstance().setIsGracefulFailureMode(false);

   // Drop-in wrapper replacement for getting a boolean Statsig gate.
   // Replace boolean calls to checkGate() with getBoolVariationWrapper() in the code.
   export function getBoolVariationWrapper(
     gateKey: string,
     user: StatsigUser,
     attributes?: Record<string, string | number | boolean | null>
   ) {
     let assignment = false;

     try {
       assignment = getInstance().getBooleanAssignment(
         gateKey,
         user.userID,
         attributes,
         false
       );
     } catch (e) {
       logger.warn(
         'Error encountered evaluating boolean assignment from Eppo SDK; falling back to Statsig',
         { gateKey, user, attributes }
       );

       // Fallback to Statsig gate check
       assignment = statsig.checkGate(user, gateKey);
     }
     return assignment;
   }

   // Drop-in wrapper replacement for getting a string Statsig config.
   // Replace string calls to getConfig() with getStringVariationWrapper() in the code.
   export function getStringVariationWrapper(
     configKey: string,
     parameterName: string,
     user: StatsigUser,
     attributes?: Record<string, string | number | boolean | null>
   ) {
     let assignment = 'default';

     try {
       assignment = getInstance().getStringAssignment(
         user.userID,
         configKey,
         attributes,
         'default'
       );
     } catch (e) {
       logger.warn(
         'Error encountered evaluating string assignment from Eppo SDK; falling back to Statsig',
         { configKey, parameterName, user, attributes }
       );

       // Fallback to Statsig config parameter
       const config = statsig.getConfig(user, configKey);
       assignment = config.get(parameterName, 'default');
     }
     return assignment;
   }

   // Drop-in wrapper replacement for getting a numeric Statsig config parameter.
   // Replace numeric calls to getConfig() with getNumericVariationWrapper() in the code.
   export function getNumericVariationWrapper(
     configKey: string,
     parameterName: string,
     user: StatsigUser,
     attributes?: Record<string, string | number | boolean | null>
   ) {
     let assignment = 0;

     try {
       assignment = getInstance().getNumericAssignment(
         user.userID,
         configKey,
         attributes,
         0
       );
     } catch (e) {
       logger.warn(
         'Error encountered evaluating numeric assignment from Eppo SDK; falling back to Statsig',
         { configKey, parameterName, user, attributes }
       );

       // Fallback to Statsig config parameter
       const config = statsig.getConfig(user, configKey);
       assignment = config.get(parameterName, 0);
     }
     return assignment;
   }

   // Drop-in wrapper replacement for getting experiment assignments.
   // Replace calls to getExperiment() with getExperimentVariationWrapper() in the code.
   export function getJSONVariationWrapper(
     experimentKey: string,
     parameterName: string,
     user: StatsigUser,
     attributes?: Record<string, string | number | boolean | null>
   ) {
     let assignment: any = null;

     try {
       // For experiments with multiple parameters, use JSON assignment
       const experimentResult = getInstance().getJSONAssignment(
         user.userID,
         experimentKey,
         attributes,
         {}
       );
       assignment = experimentResult?.[parameterName];
     } catch (e) {
       logger.warn(
         'Error encountered evaluating experiment assignment from Eppo SDK; falling back to Statsig',
         { experimentKey, parameterName, user, attributes }
       );

       // Fallback to Statsig experiment
       const experiment = statsig.getExperiment(user, experimentKey);
       assignment = experiment.get(parameterName, null);
     }
     return assignment;
   }

   ```

### 6. Recreate critical flags in Eppo{% #recreate-critical-flags %}

{% alert level="info" %}
Datadog can help with migrating flags to the Eppo dashboard. Contact [Support](https://docs.datadoghq.com/help/) for assistance.
{% /alert %}

1. In the Eppo dashboard, recreate the critical flags from Statsig. This can be done programmatically using [Statsig's](https://docs.statsig.com/console-api/introduction/) and [Eppo's](https://docs.geteppo.com/reference/api/) REST APIs.
1. Ensure that the flag configurationsâsuch as rollout percentages, targeting rules, and variationsâare accurately replicated in the new service.

### 7. Switch existing flags to the new application{% #switch-to-new-app %}

1. After you have verified that the Eppo flags are working correctly, switch your application to use the function that checks Eppo for flags instead of the Statsig ones.
1. Remove the fallback mechanism and the Statsig flag code after you have confirmed that the Eppo flags are working as expected in production.
1. It's recommended to keep the wrapper as a facade to make future changes easier, as they typically only need to be made to the wrapper.

In the `FeatureHelper.ts` file:

```typescript
export function isFeatureEnabled(
  featureKey: string,
  userId: string,
  attributes?: Record<string, string | number | boolean | null>
) {
  return getInstance().getBooleanAssignment(userId, featureKey, attributes, false);
}

export function getFeatureConfig(
  configKey: string,
  userId: string,
  attributes?: Record<string, string | number | boolean | null>
) {
  return getInstance().getJSONAssignment(userId, configKey, attributes, {});
}
```

In the `PlaceUsingFlags.ts` file:

```typescript
const useBigButtons = isFeatureEnabled('use-big-buttons', userId, userAttributes);
const buttonConfig = getFeatureConfig('button-configuration', userId, userAttributes);
```

## Appendix: TypeScript implementation comparison{% #appendix-typescript-implementation-comparison %}

Statsig and Eppo have similar interfaces for feature flag evaluation, making the transition straightforward with some key differences in how they handle different data types.

For more details, see the documentation sources above each code example.

### Initialization{% #initialization %}

{% tab title="Statsig" %}
Statsig docs: [Getting Started](https://docs.statsig.com/client/javascript-sdk#getting-started)

```typescript
await statsig.initialize('client-key', user, { environment: { tier: 'production' } });
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Initialization](https://docs.geteppo.com/sdks/client-sdks/javascript/Initialization/)

```typescript
await init({
 apiKey: EPPO_SDK_KEY,
 assignmentLogger,
});
```

{% /tab %}

### Configure the assignment logger{% #configure-the-assignment-logger %}

{% tab title="Statsig" %}
Statsig docs: [Logging an Event](https://docs.statsig.com/client/javascript-sdk/#event-logging)

```typescript
// Statsig automatically logs assignments, but you can add custom logging by
// subscribing to client events like gate_evaluation or experiment_evaluation.

statsig.on('gate_evaluation', (event) => {
  // Your custom logging logic here
  console.log(event);
});
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Assignment logging](https://docs.geteppo.com/sdks/event-logging/assignment-logging/)

```typescript
const assignmentLogger: IAssignmentLogger = {
  logAssignment(assignment) {
    // Send data to analytics provider/warehouse here
    analytics.track({
      userId: assignment.subject,
      event: "Eppo Randomization Event",
      type: "track",
      properties: { ...assignment },
    });
  }
};
getInstance().setLogger(assignmentLogger);   // Can also be set in init()
```

{% /tab %}

### Get a Boolean flag (Feature Gate){% #get-a-boolean-flag-feature-gate %}

For example, check if a feature is enabled.

{% tab title="Statsig" %}
Statsig docs: [Checking a Feature Flag/Gate](https://docs.statsig.com/client/javascript-sdk/#feature-gates)

```typescript
const enabled = statsig.checkGate('new_feature_gate');
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Boolean Assignments](https://docs.geteppo.com/sdks/server-sdks/node/assignments/#boolean-assignments)

```typescript
const enabled = getInstance().getBooleanAssignment(
  user.userID,
  'new_feature_gate',
  userAttributes,
  false
);
```

{% /tab %}

### Get configuration values{% #get-configuration-values %}

{% tab title="Statsig" %}
Statsig docs: [Reading a Dynamic Config](https://docs.statsig.com/client/javascript-sdk#dynamic-configs)

```typescript
const config = statsig.getConfig('product_config');
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Assignments](https://docs.geteppo.com/sdks/server-sdks/node/assignments/)

```typescript
// If it's part of a multi-valued configuration (how Statsig organizes values),
// you will have to figure out the type of each parameter, as Eppo uses different
// calls for each variant type.

// For a JSON configuration with multiple parameters:
const config = getInstance().getJSONAssignment(user.userID, 'product_config', userAttributes, {});
const buttonColor = config?.button_color || 'blue';
const maxItems = config?.max_items || 10;

// For individual string parameters:
const buttonColor = getInstance().getStringAssignment(
  user.userID,
  'button_color_flag',
  userAttributes,
  'blue'
);

// For individual numeric parameters:
const maxItems = getInstance().getNumericAssignment(
  user.userID,
  'max_items_flag',
  userAttributes,
  10
);
```

{% /tab %}

### Get experiment values{% #get-experiment-values %}

For example, get experiment parameter values.

{% tab title="Statsig" %}
Statsig docs: [Getting a Layer/Experiment](https://docs.statsig.com/client/javascript-sdk/#layers)

```typescript
// Values using getLayer

const layer = statsig.getLayer("user_promo_experiments");

const promoTitle = layer.get("title", "Welcome to Statsig!");
const discount = layer.get("discount", 0.1);

// or, using getExperiment

const titleExperiment = statsig.getExperiment("new_user_promo_title");
const priceExperiment = statsig.getExperiment("new_user_promo_price");

const promoTitle = titleExperiment.value["title"] ?? "Welcome!";
const discount = priceExperiment.value["discount"] ?? 0.1;
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Assignments](https://docs.geteppo.com/sdks/server-sdks/node/assignments/)

```typescript
// For experiments with multiple parameters, use JSON assignment.
const variation = getInstance().getJSONAssignment(
  user.userID,
  'checkout_flow_test',
  userAttributes,
  {}
);
const checkoutVersion = variation?.checkout_version || 'control';
const showUpsell = variation?.show_upsell || false;

// Alternatively, for individual experiment parameters:
const checkoutVersion = getInstance().getStringAssignment(
  user.userID,
  'checkout_version',
  userAttributes,
  'control'
);
```

{% /tab %}

### User context and attributes{% #user-context-and-attributes %}

{% tab title="Statsig" %}
Statsig docs: [Statsig User](https://docs.statsig.com/client/javascript-sdk/#statsig-user)

```typescript
const user = new StatsigUser({
  userID: '12345',
  email: 'user@example.com',
  country: 'US',
  custom: {
    plan: 'premium',
    signup_date: '2023-01-15'
  }
});
```

{% /tab %}

{% tab title="Eppo" %}
Eppo docs: [Subject attributes](https://docs.geteppo.com/sdks/sdk-features/subject-attributes/)

```typescript
const userAttributes = {
  email: 'user@example.com',
  country: 'US',
  plan: 'premium',
  signup_date: '2023-01-15'
};

// Used in assignment calls
const variation = getInstance().getBooleanAssignment(
  '12345', // userID as separate parameter
  'feature_flag',
  userAttributes,
  false
);
```

{% /tab %}
