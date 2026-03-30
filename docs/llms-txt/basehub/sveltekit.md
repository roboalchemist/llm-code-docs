# SvelteKit

> Get started with SvelteKit and BaseHub.

[SvelteKit](https://kit.svelte.dev/docs/introduction) is a framework for rapidly developing robust, performant web applications using [Svelte](https://svelte.dev/).

note:

The main difference that the setup SvelteKit has vs Next.js is in the way it exposes environment variables.

While in Next.js, `process.env.BASEHUB_TOKEN` is available for our SDK to use, in Vite-powered frameworks (like SvelteKit), you’ll need to explicitly pass the token via params as you’ll see below.

## Set Up `basehub`

Our official JavaScript/TypeScript library exposes a CLI generator that, when run, will generate a type-safe GraphQL client. Check out [our API Reference](https://docs.basehub.com/api-reference/javascript-sdk) for more information.

### Install

Install with your preferred package manager.

npm

```
npm i basehub
```

### Add the `BASEHUB_TOKEN` Environment Variable

Get it from your BaseHub Repo’s “Connect to Your App” tab.

.env

```
BASEHUB_TOKEN="<your-token>"