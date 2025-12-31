# Source: https://juno.build/docs/setup-the-sdk.md

# Setup the SDK

To connect your app to a Satellite and use Juno's features â like authentication, data, storage, and serverless functions â you'll need to initialize the SDK.

This guide walks you through how to do that, whether you're using a plugin (Next.js, Vite) or setting things up manually.

**Info:**

If you intend to use Juno solely for **[hosting](/docs/build/hosting.md)** purposes, you may skip the following steps.

---

## TL;DR

1.  Call `initSatellite()` in your app code
2.  Create a `juno.config` file at the root to define your Satellite
3.  Connect code and config â preferably using the `@junobuild/nextjs-plugin` or `@junobuild/vite-plugin`

---

## Initialization

1.  Install the Juno SDK:

*   npm
*   yarn
*   pnpm

```
npm i @junobuild/core
```

```
yarn add @junobuild/core @icp-sdk/core @icp-sdk/auth @dfinity/utils
```

```
pnpm add @junobuild/core @icp-sdk/core @icp-sdk/auth @dfinity/utils
```

2.  Initialize your satellite in your web app:

```
import { initSatellite } from "@junobuild/core";await initSatellite();
```

It is generally recommended to initialize globally the library at the top of your application.

---

## Configuration

Juno uses a configuration file to determine which Satellite to connect to.

You can scaffold a minimal `juno.config` file using:

```
npx @junobuild/cli init --minimal
```

This creates a `juno.config` file â in TypeScript, JavaScript, or JSON depending on your preferences â at the root of your project. It contains metadata such as the Satellite ID used during SDK initialization.

---

## Connecting Code and Config

If you're using **Next.js** or **Vite**, we recommend installing the official plugin. It automatically loads values from your config file and injects them into your build as environment variables.

This means you can call `initSatellite()` without passing any parameters, the SDK will read them automatically from `process.env` or `import.meta.env`.

*   [Next.js Plugin](/docs/reference/plugins.md#nextjs-plugin)

next.config.js

```
import { withJuno } from "@junobuild/nextjs-plugin";// withJuno wraps your Next.js config and injects values from juno.configexport default withJuno();
```

*   [Vite Plugin](/docs/reference/plugins.md#vite-plugin)

vite.config.js

```
import juno from "@junobuild/vite-plugin";// Automatically injects values from juno.config for the buildexport default defineConfig({  plugins: [juno()]});
```

**Note:**

The templates already include both the config file and the plugin setup.

#### Not using a plugin?

You can also pass the Satellite ID manually to the SDK, though using the plugins is the preferred approach:

```
import { initSatellite } from "@junobuild/core";await initSatellite({  satelliteId: "your-actual-satellite-id"});
```