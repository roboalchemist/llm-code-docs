# Source: https://loops.so/docs/sdks/nuxt.md

# Nuxt module

> The official Loops Nuxt module.

[![](https://img.shields.io/npm/dw/nuxt-loops?style=social\&label=Downloads)](https://www.npmjs.com/package/nuxt-loops)

This Nuxt module makes it easy to add the Loops [JavaScript SDK](/sdks/javascript) to your Nuxt project.

## Installation

You can install the package [from npm](https://www.npmjs.com/package/nuxt-loops):

```bash  theme={"dark"}
npm install nuxt-loops
```

You will need a Loops API key to use the module.

In your Loops account, go to the [API Settings page](https://app.loops.so/settings?page=api) and click **Generate key**.

Copy this key and save it in your application code (for example as `LOOPS_API_KEY` in an `.env` file).

Then add `nuxt-loops` to your modules list and add a reference to your API key:

```js nuxt.config.ts theme={"dark"}
export default defineNuxtConfig({
  modules: ['nuxt-loops'],
  loops: {
    apiKey: process.env.LOOPS_API_KEY
  }
});
```

## Usage

<Warning>
  The Loops API and SDK should only be used on the server side to protect your API key.
</Warning>

To use the module, import `loops` from the request context.

Then call one of the SDK methods. Read through the [JS SDK docs](/sdks/javascript#methods) for more details.

```javascript  theme={"dark"}
export default defineEventHandler(async (event) => {
  const { loops } = event.context;

  const response = await loops.updateContact("hello@gmail.com", {
    firstName: "Bri",
    lastName: "Chambers",
  })
});
```

See the API documentation to learn more about [rate limiting](/api-reference#rate-limiting) and [error handling](/api-reference#debugging).

<CardGroup>
  <Card title="JavaScript SDK" href="/sdks/javascript" icon="js">
    Explore our official JS/TS SDK.
  </Card>

  <Card title="Loops API" icon="rectangle-terminal" href="/api-reference">
    Read the Loops API reference.
  </Card>
</CardGroup>

***

## Version history

* `v1.0.0` (Sep 6, 2024) - Initial release.
