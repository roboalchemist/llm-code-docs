# Source: https://posthog.com/docs/libraries/nuxt-js-2.md

# Nuxt.js (v2.16 and below) - Docs

PostHog makes it easy to get data about usage of your [Nuxt.js](https://nuxt.com/) app. Integrating PostHog into your app enables analytics about user behavior, custom events capture, session replays, feature flags, and more.

These docs are for Nuxt v2.16 and below.

We are going to implement PostHog as a [Nuxt.js integration](https://nuxtjs.org/docs/2.x/directory-structure/plugins) which gives us the possibility to inject the `posthog` object and make it available across our application.

## Installation

The first thing you want to do is to install the [posthog-js library](/docs/integrate/client/js.md) in your project - so add it using your package manager:

PostHog AI

### npm

```bash
npm install --save posthog-js
```

### Yarn

```bash
yarn add posthog-js
```

### pnpm

```bash
pnpm add posthog-js
```

### Bun

```bash
bun add posthog-js
```

After that we want to create an app in `plugins/posthog/index.js`

JavaScript

PostHog AI

```javascript
import posthog from 'posthog-js'
import Vue from 'vue'
export default function({ app: { router } }, inject) {
  // Init PostHog
  posthog.init('<ph_project_token>', {
    api_host: 'https://us.i.posthog.com',
    defaults: '2026-01-30',
    capture_pageview: false,
    loaded: () => posthog.identify('unique_id') // If you can already identify your user
  })
  // Inject PostHog into the application and make it available via this.$posthog (or app.$posthog)
  inject('posthog', posthog)
  // Make sure that pageviews are captured with each route change
  router.afterEach(to => {
    Vue.nextTick(() => {
      /* Note: this might also be a good place to call posthog.register(...) in order to update your properties
      on each page view
      */
      posthog.capture('$pageview', {
        $current_url: to.fullPath
      })
    })
  })
}
```

Finally, we need to activate it on the client side in our `nuxt.config.js`

JavaScript

PostHog AI

```javascript
plugins: [
    ...
    { src: './plugins/posthog', mode: 'client' }
  ],
```

## Usage

By using the example code above you can now use PostHog across your app with `this.$posthog` or `app.$posthog` - depending on the context. Compare with the [Nuxt.js docs](https://nuxtjs.org/docs/2.x/directory-structure/plugins#inject-in-root--context) on further details when to use `app.$posthog` or `this.$posthog`.

Let's say for example the user makes a purchase you could track an event like that:

Web

PostHog AI

```javascript
<template>
  <button @click="purchase">Buy</button>
</template>
<script>
...
  methods: {
     purchase() {
       this.$posthog.capture('purchase')
     }
  }
...
</script>
```

## Next steps

For any technical questions for how to integrate specific PostHog features into Nuxt (such as analytics, feature flags, A/B testing, surveys, etc.), have a look at our [JavaScript Web](/docs/libraries/js.md) and [Node](/docs/libraries/node.md) SDK docs.

Alternatively, the following tutorials can help you get started:

-   [How to set up analytics in Nuxt](/tutorials/nuxt-analytics.md)
-   [How to set up feature flags in Nuxt](/tutorials/nuxt-feature-flags.md)
-   [How to set up A/B tests in Nuxt](/tutorials/nuxtjs-ab-tests.md)
-   [How to set up surveys in Nuxt](/tutorials/nuxt-surveys.md)

### Community questions

Ask a question

### Was this page useful?

HelpfulCould be better