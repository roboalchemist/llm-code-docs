# Source: https://juno.build/docs/reference/plugins.md

# Plugins

Juno provides various plugins to simplify your development workflow. Each plugin automatically loads values from your `juno.config` file into your build environment, so you can call `initSatellite()` and `initOrbiter()` without extra config.

---

## Next.js Plugin

Use this plugin to load Juno configuration into your Next.js build with zero manual setup.

### Installation

Add it to your dev dependencies with:

*   npm
*   yarn
*   pnpm

```
npm i @junobuild/nextjs-plugin -D
```

```
yarn add @junobuild/nextjs-plugin -D
```

```
pnpm add @junobuild/nextjs-plugin -D
```

### Usage

In your Next.js config file â whether it's `next.config.js`, `next.config.ts`, `next.config.mjs` or else â wrap your configuration with `withJuno` to automatically load Juno settings:

next.config.js

```
import { withJuno } from "@junobuild/nextjs-plugin";// withJuno wraps your Next.js config and injects values from juno.configexport default withJuno();
```

### Options

The plugin supports the following options:

#### Passing Next.js Options

You can pass additional Next.js configuration options using the `nextConfig` field.

The plugin will always ensure `output: "export"` is set for static export.

next.config.js

```
import { withJuno } from "@junobuild/nextjs-plugin";/** @type {import('next').NextConfig} */const nextConfig = {  // Example: add your own Next.js config here  i18n: {    locales: ["en", "fr"],    defaultLocale: "en"  },  env: {    CUSTOM_VAR: "my-value"  }};// Juno will merge this with output: "export" automaticallyexport default withJuno({ nextConfig });
```

In other words, if you want to include additional Next.js configuration (e.g. `i18n`, `env` etc.), just define them in your `nextConfig` object and pass it to `withJuno`.

#### Container

You can use the `container` option to:

*   Provide a custom container URL (e.g. for an emulator running on a specific port), or
*   Set it to `false` to disable local development behavior entirely.

next.config.js

```
import { withJuno } from "@junobuild/nextjs-plugin";export default withJuno({ juno: { container: false } });
```

### Environment Variables

The plugin injects environment variables derived from your `juno.config` file. You can use these variables in your app, which is especially helpful if youâve specified a custom prefix other than `NEXT_PUBLIC_`.

```
console.log(process.env.NEXT_PUBLIC_SATELLITE_ID);
```

The following variables are available:

| Environment variable | Value |
| --- | --- |
| NEXT\_PUBLIC\_SATELLITE\_ID | Satellite ID from Juno config (per `mode`) |
| NEXT\_PUBLIC\_ORBITER\_ID | `undefined` in development, Orbiter ID from Juno config. |
| NEXT\_PUBLIC\_INTERNET\_IDENTITY\_ID | `rdmx6-jaaaa-aaaaa-aaadq-cai` |
| NEXT\_PUBLIC\_ICP\_LEDGER\_ID | `ryjl3-tyaaa-aaaaa-aaaba-cai` |
| NEXT\_PUBLIC\_ICP\_INDEX\_ID | `qhbym-qaaaa-aaaaa-aaafq-cai` |
| NEXT\_PUBLIC\_NNS\_GOVERNANCE\_ID | `rrkah-fqaaa-aaaaa-aaaaq-cai` |
| NEXT\_PUBLIC\_CMC\_ID | `rkp4c-7iaaa-aaaaa-aaaca-cai` |
| NEXT\_PUBLIC\_REGISTRY\_ID | `rwlgt-iiaaa-aaaaa-aaaaa-cai` |
| NEXT\_PUBLIC\_CYCLES\_LEDGER\_ID | `um5iw-rqaaa-aaaaq-qaaba-cai` |
| NEXT\_PUBLIC\_CYCLES\_INDEX\_ID | `ul4oc-4iaaa-aaaaq-qaabq-cai` |
| NEXT\_PUBLIC\_SNS\_WASM\_ID | `qaa6y-5yaaa-aaaaa-aaafa-cai` |
| NEXT\_PUBLIC\_NNS\_DAPP\_ID | `qoctq-giaaa-aaaaa-aaaea-cai` |
| NEXT\_PUBLIC\_CONTAINER | Container URL (emulator or custom); `undefined` by default in production |

### More information

Discover additional information in the library's [README](https://github.com/junobuild/plugins/tree/main/plugins/nextjs-plugin).

---

## Vite Plugin

Use this plugin to integrate Juno configuration into your Vite build process automatically.

### Installation

Add it to your dev dependencies with:

*   npm
*   yarn
*   pnpm

```
npm i @junobuild/vite-plugin -D
```

```
yarn add @junobuild/vite-plugin -D
```

```
pnpm add @junobuild/vite-plugin -D
```

### Usage

Add the plugin to your Vite configuration â whether you're using TypeScript or JavaScript â to automatically load Juno settings:

vite.config.js

```
import juno from "@junobuild/vite-plugin";export default defineConfig({  // Automatically injects values from juno.config for the build  plugins: [juno()]});
```

### Options

You can use the `container` option to:

*   Provide a custom container URL (e.g. for an emulator running on a specific port), or
*   Set it to `false` to disable local development behavior entirely.

vite.config.js

```
import juno from "@junobuild/vite-plugin";export default defineConfig({  plugins: [    juno({      container: false    })  ]});
```

### Environment Variables

The plugin injects environment variables derived from your `juno.config` file. You can use these variables in your app, which is especially helpful if youâve specified a prefix other than the default, such as `VITE_` or `PUBLIC_`.

```
console.log(process.env.VITE_SATELLITE_ID);
```

The following variables are available:

| Environment variable | Value |
| --- | --- |
| VITE\_SATELLITE\_ID | Satellite ID from Juno config (per `mode`) |
| VITE\_ORBITER\_ID | `undefined` in development, Orbiter ID from Juno config. |
| VITE\_INTERNET\_IDENTITY\_ID | `rdmx6-jaaaa-aaaaa-aaadq-cai` |
| VITE\_ICP\_LEDGER\_ID | `ryjl3-tyaaa-aaaaa-aaaba-cai` |
| VITE\_ICP\_INDEX\_ID | `qhbym-qaaaa-aaaaa-aaafq-cai` |
| VITE\_NNS\_GOVERNANCE\_ID | `rrkah-fqaaa-aaaaa-aaaaq-cai` |
| VITE\_CMC\_ID | `rkp4c-7iaaa-aaaaa-aaaca-cai` |
| VITE\_REGISTRY\_ID | `rwlgt-iiaaa-aaaaa-aaaaa-cai` |
| VITE\_CYCLES\_LEDGER\_ID | `um5iw-rqaaa-aaaaq-qaaba-cai` |
| VITE\_CYCLES\_INDEX\_ID | `ul4oc-4iaaa-aaaaq-qaabq-cai` |
| VITE\_SNS\_WASM\_ID | `qaa6y-5yaaa-aaaaa-aaafa-cai` |
| VITE\_NNS\_DAPP\_ID | `qoctq-giaaa-aaaaa-aaaea-cai` |
| VITE\_PUBLIC\_CONTAINER | Container URL (emulator or custom); `undefined` by default in production |

### More information

Discover additional options in the library's [README](https://github.com/junobuild/plugins/tree/main/plugins/vite-plugin).