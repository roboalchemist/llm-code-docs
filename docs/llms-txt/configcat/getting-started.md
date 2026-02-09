# Source: https://configcat.com/docs/getting-started.md

# Getting Started

Copy page

This page is an overview and a short guide on how to get started.

**ConfigCat** is a cloud-based service that lets you release features without code deployments.

You can use it with many similar techniques, such as feature flags/toggles, canary releases, soft launches, A-B testing, remote configuration management, and phased rollouts. Configure your application and features even after deployment.

## The birth of a Feature Flag[​](#the-birth-of-a-feature-flag "Direct link to The birth of a Feature Flag")

First, **add a feature flag** on the *ConfigCat Dashboard*, and then you can **connect your application** to the ConfigCat service to access your feature flag.

### Create a feature flag on the *ConfigCat Dashboard*[​](#create-a-feature-flag-on-the-configcat-dashboard "Direct link to create-a-feature-flag-on-the-configcat-dashboard")

1. [Log in](https://app.configcat.com) to the *Dashboard*
2. Click *ADD FEATURE FLAG* and give it a name.

![Add feature flag](/docs/assets/add-feature-flag_192dpi.png)

### Explore with Our Tutorial App[​](#explore-with-our-tutorial-app "Direct link to Explore with Our Tutorial App")

Before diving into connecting your actual application, consider exploring our [Feature Flags Tutorial](https://tutorial.configcat.com/?lm=11). This interactive app provides a practical and engaging way to learn about ConfigCat and feature flags without needing to integrate immediately with your current projects. It's perfect for beginners to understand the functionalities and advantages of using feature flags effectively.

![Feature Flags Tutorial](/docs/assets/news/tutorial_192dpi.png)

[Start the Feature Flags Tutorial](https://tutorial.configcat.com/?lm=12)

### Connect your application[​](#connect-your-application "Direct link to Connect your application")

There are ready-to-use code snippets for `Browser (JavaScript)`, `Angular`, `React`, `Node.js`, `Deno`, `Bun`, `Cloudflare Worker`, `.NET (C#)`, `Java`, `Go`, `PHP`, `Python`, `Android (Java)`, `iOS (Swift)`, `Dart / Flutter`, `Kotlin Multiplatform`, `Ruby`, `Elixir`, `C++`, `Rust`, `Unreal Engine` on the [ConfigCat Dashboard](https://app.configcat.com), just scroll down to the **SDK Key and steps to connect your application** section.

All the ConfigCat SDKs are open-source and available on [GitHub](https://github.com/configcat).

See the detailed [Docs on how to use the ConfigCat SDKs.](https://configcat.com/docs/sdk-reference/overview.md)

Here's a short example to demonstrate the concept:

```js
// 0. If necessary, install the ConfigCat SDK package for the platform you use.
// E.g. `npm install @configcat/sdk`

// 1. Import the ConfigCat SDK package.
import * as configcat from '@configcat/sdk';

// 2. Get a client object for the SDK Key of your config.
const client = configcat.getClient('#YOUR-SDK-KEY#');

// 3. Evaluate a feature flag using the client object.
const value = await client.getValueAsync('isMyFeatureEnabled', false);

// 4. Based on the value of the feature flag decide whether or not to enable the related feature.
if (value) {
  do_the_new_thing();
} else {
  do_the_old_thing();
}

```
