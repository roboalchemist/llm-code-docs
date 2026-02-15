# Source: https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/index.md

---

title: Vike · Cloudflare Workers docs
description: Create a Vike application and deploy it to Cloudflare Workers
lastUpdated: 2026-02-02T18:36:26.000Z
chatbotDeprioritize: false
tags: Full stack
source_url:
  html: https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/
  md: https://developers.cloudflare.com/workers/framework-guides/web-apps/vike/index.md
---

You can deploy your [Vike](https://vike.dev) app to Cloudflare using the Vike extension [`vike-photon`](https://vike.dev/vike-photon).

All app types (SSR/SPA/SSG) are supported.

## What is Vike?

[Vike](https://vike.dev) is a Next.js/Nuxt alternative for advanced applications, powered by a modular architecture for unprecedented flexibility and stability.

## New app

Use [vike.dev/new](https://vike.dev/new) to scaffold a new Vike app that uses `vike-photon` with `@photonjs/cloudflare`.

## Add to existing app

1. * npm

     ```sh
     npm i wrangler vike-photon @photonjs/cloudflare
     ```

   * yarn

     ```sh
     yarn add wrangler vike-photon @photonjs/cloudflare
     ```

   * pnpm

     ```sh
     pnpm add wrangler vike-photon @photonjs/cloudflare
     ```

2. ```ts
   import type { Config } from 'vike/types'
   import vikePhoton from 'vike-photon/config'


   export default {
     extends: [vikePhoton]
   } satisfies Config
   ```

3. ```json
   {
     "scripts": {
       "dev": "vike dev",
       "preview": "vike build && vike preview",
       "deploy": "vike build && wrangler deploy"
     }
   }
   ```

   ```jsonc
   {
     "$schema": "node_modules/wrangler/config-schema.json",
     "compatibility_date": "2025-08-06",
     "name": "my-vike-cloudflare-app",
     "main": "virtual:photon:cloudflare:server-entry",
     // Only required if your app depends a Node.js API
     "compatibility_flags": ["nodejs_compat"]
   }
   ```

4. ```bash
   .wrangler/
   ```

5. **(Optional)** By default, Photon uses a built-in server that supports basic features like SSR. If you need additional server functionalities (e.g. [file uploads](https://hono.dev/examples/file-upload) or [API routes](https://vike.dev/api-routes)), then [create your own server](https://vike.dev/vike-photon#server).

## Cloudflare APIs (bindings)

To access Cloudflare APIs (such as [D1](https://developers.cloudflare.com/d1/) and [KV](https://developers.cloudflare.com/kv/)), use [bindings](https://developers.cloudflare.com/workers/runtime-apis/bindings/) which are available via the `env` object [imported from `cloudflare:workers`](https://developers.cloudflare.com/workers/runtime-apis/bindings/#importing-env-as-a-global).

```ts
import { env } from 'cloudflare:workers'
// Key-value store
env.KV.get('my-key')
// Environment variable
env.LOG_LEVEL
// ...
```

> Example of using Cloudflare D1:
>
> * npm
>
>   ```sh
>   npm create vike@latest -- --react --hono --drizzle --cloudflare
>   ```
>
> * yarn
>
>   ```sh
>   yarn create vike --react --hono --drizzle --cloudflare
>   ```
>
> * pnpm
>
>   ```sh
>   pnpm create vike@latest --react --hono --drizzle --cloudflare
>   ```
>
> Or go to [vike.dev/new](https://vike.dev/new) and select `Cloudflare` with an ORM.

## TypeScript

If you use TypeScript, run [`wrangler types`](https://developers.cloudflare.com/workers/wrangler/commands/#types) whenever you change your Cloudflare configuration to update the `worker-configuration.d.ts` file.

* npm

  ```sh
  npx wrangler types
  ```

* yarn

  ```sh
  yarn wrangler types
  ```

* pnpm

  ```sh
  pnpm wrangler types
  ```

Then commit:

```bash
git commit -am "update cloudflare types"
```

Make sure TypeScript loads it:

```json
{
  "compilerOptions": {
    "types": ["./worker-configuration.d.ts"]
 }
}
```

See also: [Cloudflare Workers > TypeScript](https://developers.cloudflare.com/workers/languages/typescript/).

## See also

* [Vike Docs > Cloudflare](https://vike.dev/cloudflare)
