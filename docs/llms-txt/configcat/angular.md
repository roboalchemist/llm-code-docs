# Source: https://configcat.com/docs/sdk-reference/openfeature/angular.md

# Using ConfigCat's OpenFeature Provider in Angular

Copy page

## Getting started[​](#getting-started "Direct link to Getting started")

OpenFeature offers an [Angular SDK](https://github.com/open-feature/js-sdk/tree/main/packages/angular) to streamline the use of OpenFeature in Angular applications. This SDK is built on top of the [OpenFeature JavaScript Web SDK](https://github.com/open-feature/js-sdk/blob/main/packages/web).

Since ConfigCat implements [a provider](https://configcat.com/docs/sdk-reference/openfeature/js.md) for the Web SDK, you can use ConfigCat with the OpenFeature Angular SDK, as explained below.

### 1. Install the Angular SDK and the ConfigCat provider[​](#1-install-the-angular-sdk-and-the-configcat-provider "Direct link to 1. Install the Angular SDK and the ConfigCat provider")

```bash
npm i @openfeature/angular-sdk @openfeature/config-cat-web-provider

```

### 2. Initialize the Angular SDK[​](#2-initialize-the-angular-sdk "Direct link to 2. Initialize the Angular SDK")

The `ConfigCatWebProvider.create()` function takes the SDK key and an optional `options` argument containing additional configuration options for the underlying [ConfigCat client](https://configcat.com/docs/sdk-reference/js/browser.md#creating-the-configcat-client):

* For applications using modules:

  ```ts
  import { NgModule } from '@angular/core';
  import { BooleanFeatureFlagDirective, type EvaluationContext, OpenFeatureModule } from '@openfeature/angular-sdk';
  import { ConfigCatWebProvider } from '@openfeature/config-cat-web-provider';
  import { createConsoleLogger, LogLevel } from '@configcat/sdk';

  const configCatProvider = ConfigCatWebProvider.create('#YOUR-SDK-KEY#', {
    // Specify options for the underlying ConfigCat client
    logger: createConsoleLogger(LogLevel.Info),
    setupHooks: (hooks) => hooks.on('clientReady', () => console.log('Client is ready!')),
    // ...
  });

  // Set the initial context for your evaluations
  const initialContext: EvaluationContext = {
    targetingKey: 'user-1',
    admin: false
  };

  @NgModule({
    declarations: [
      // ...
    ],
    imports: [
      // ...
      OpenFeatureModule.forRoot({
        provider: configCatProvider,
        context: initialContext
      }),
      // Alternatively, you can import the directive directly in your components
      BooleanFeatureFlagDirective
    ],
    exports: [
      // Not needed if you import the directive directly in your components
      BooleanFeatureFlagDirective
    ],
    bootstrap: [/* ... */]
  })
  export class AppModule { }

  ```

* For applications using standalone components:

  ```ts
  import { type ApplicationConfig, importProvidersFrom } from '@angular/core';
  import { type EvaluationContext, OpenFeatureModule } from '@openfeature/angular-sdk';
  import { ConfigCatWebProvider } from '@openfeature/config-cat-web-provider';
  import { createConsoleLogger, LogLevel } from '@configcat/sdk';

  const configCatProvider = ConfigCatWebProvider.create('#YOUR-SDK-KEY#', {
    // Specify options for the underlying ConfigCat client
    logger: createConsoleLogger(LogLevel.Info),
    setupHooks: (hooks) => hooks.on('clientReady', () => console.log('Client is ready!')),
    // ...
  });

  // Set the initial context for your evaluations
  const initialContext: EvaluationContext = {
    targetingKey: 'user-1',
    admin: false
  };

  export const appConfig: ApplicationConfig = {
    providers: [
      // ...
      importProvidersFrom(
        OpenFeatureModule.forRoot({
          provider: configCatProvider,
          context: initialContext
        })
      )
    ]
  };

  ```

### 3. Use your feature flag[​](#3-use-your-feature-flag "Direct link to 3. Use your feature flag")

```html
<div
  *booleanFeatureFlag="'isAwesomeFeatureEnabled'; default: false; else: booleanFeatureElse; initializing: booleanFeatureInitializing; reconciling: booleanFeatureReconciling">
  This is shown when the feature flag is enabled.
</div>
<ng-template #booleanFeatureElse>
  This is shown when the feature flag is disabled.
</ng-template>
<ng-template #booleanFeatureInitializing>
  This is shown when the feature flag is initializing.
</ng-template>
<ng-template #booleanFeatureReconciling>
  This is shown when the feature flag is reconciling.
</ng-template>

```

## Evaluation Context[​](#evaluation-context "Direct link to Evaluation Context")

An [evaluation context](https://openfeature.dev/docs/reference/concepts/evaluation-context) in the OpenFeature specification is a container for arbitrary contextual data that can be used as a basis for feature flag evaluation.

You can find [here](https://configcat.com/docs/sdk-reference/openfeature/js.md#evaluation-context) how the ConfigCat provider translates these evaluation contexts to ConfigCat [User Objects](https://configcat.com/docs/sdk-reference/js/browser.md#user-object).

## Advanced features[​](#advanced-features "Direct link to Advanced features")

Read the documentation of the [OpenFeature Angular SDK](https://openfeature.dev/docs/reference/technologies/client/web/angular/) to learn more about the advanced capabilities of the SDK.

## Look under the hood[​](#look-under-the-hood "Direct link to Look under the hood")

* [ConfigCat OpenFeature Provider's repository on GitHub](https://github.com/open-feature/js-sdk-contrib/tree/main/libs/providers/config-cat-web)
* [ConfigCat OpenFeature Provider in NPM](https://www.npmjs.com/package/@openfeature/config-cat-web-provider)
