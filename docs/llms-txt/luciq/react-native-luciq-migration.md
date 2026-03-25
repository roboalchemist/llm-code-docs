# Source: https://docs.luciq.ai/react-native/react-native-luciq-migration.md

# React Native Luciq Migration

### Overview

This migration renames the entire SDK from "Instabug" to "Luciq" while maintaining all existing functionality. The changes include:

* Package name: `instabug-reactnative` → `@luciq/react-native`
* All class names, methods, and constants
* Native module names and package identifiers

### Migration Script

We provide an automated migration script to handle most of the renaming automatically.

#### Prerequisites

{% stepper %}
{% step %}

#### Ensure a clean git working directory

Make sure there are no uncommitted changes.
{% endstep %}

{% step %}

#### Instabug version

Make sure you’re using Instabug version **16.0.0** or later.
{% endstep %}

{% step %}

#### Project root

Make sure you're in the root directory of your React Native project.
{% endstep %}
{% endstepper %}

#### Running the Migration Script

**Using the CLI (Recommended)**

{% tabs %}
{% tab title="npm" %}

```bash
## Install the package first using NPM
npm install @luciq/react-native

## Run the migration script
npx luciq migrate

## For dry run (preview changes without applying them)
npx luciq migrate --dry-run
```

{% endtab %}

{% tab title="yarn" %}

```bash
## Install using yarn
yarn add @luciq/react-native

## Run the migration script
npx luciq migrate

## For dry run (preview changes without applying them)
npx luciq migrate --dry-run
```

{% endtab %}
{% endtabs %}

### API Reference Changes

**Main Module**

| Old API                   | New API                | Notes                        |
| ------------------------- | ---------------------- | ---------------------------- |
| `Instabug.init()`         | `Luciq.init()`         | Main initialization method   |
| `Instabug.setEnabled()`   | `Luciq.setEnabled()`   | Enable/disable functionality |
| `Instabug.show()`         | `Luciq.show()`         | Show bug reporting UI        |
| `Instabug.setUserData()`  | `Luciq.setUserData()`  | Set user data                |
| `Instabug.identifyUser()` | `Luciq.identifyUser()` | Identify user                |
| `Instabug.logOut()`       | `Luciq.logOut()`       | Log out user                 |

**Configuration**

| Old API                    | New API                 | Notes                              |
| -------------------------- | ----------------------- | ---------------------------------- |
| `InstabugConfig`           | `LuciqConfig`           | Configuration interface            |
| `Instabug.invocationEvent` | `Luciq.invocationEvent` | Invocation events enum             |
| `Instabug.LogLevel`        | `Luciq.LogLevel`        | Log level enum                     |
| `Instabug.ColorTheme`      | `Luciq.ColorTheme`      | Color theme enum                   |
| `IBG_*`                    | `LCQ_*`                 | All prefixed constants in iOS code |
| `IBG_*`                    | `LUCIQ_*`               | All prefixed constants in Android  |

**Native Module Names**

| Platform | Old Name     | New Name  |
| -------- | ------------ | --------- |
| Android  | `RNInstabug` | `RNLuciq` |
| iOS      | `RNInstabug` | `RNLuciq` |

### Testing Your Migration

After completing the migration:

1. Clean and rebuild your project

{% code title="CMD" %}

```bash
## React Native
npx react-native clean
npx react-native run-android
npx react-native run-ios

## Expo
expo start --clear
```

{% endcode %}

2. Test core functionality:
   * Initialize the SDK
   * Trigger bug reporting
   * Test crash reporting
   * Verify network logging
   * Check user identification
3. Verify native integration:
   * Check that native modules are properly linked
   * Verify permissions are correctly configured
   * Test on both Android and iOS

**Migration from Instabug Environment Variables**

| Old Instabug Variable                | New Luciq Variable                | Notes                    |
| ------------------------------------ | --------------------------------- | ------------------------ |
| `INSTABUG_APP_TOKEN`                 | `LUCIQ_APP_TOKEN`                 | App token                |
| `INSTABUG_APP_VERSION_NAME`          | `LUCIQ_APP_VERSION_NAME`          | Version name             |
| `INSTABUG_APP_VERSION_CODE`          | `LUCIQ_APP_VERSION_CODE`          | Version code             |
| `INSTABUG_SOURCEMAPS_UPLOAD_DISABLE` | `LUCIQ_SOURCEMAPS_UPLOAD_DISABLE` | Disable sourcemap upload |
