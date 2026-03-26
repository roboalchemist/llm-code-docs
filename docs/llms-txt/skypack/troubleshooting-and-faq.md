# Source: https://docs.skypack.dev/troubleshooting-and-faq.md

# Troubleshooting & FAQ

If you're having trouble with anything on Skypack, you can [file an issue](https://github.com/pikapkg/cdn) with us in the official GitHub repo.

Below are some common question & answers to help you troubleshoot Skypack CDN, the Skypack search catalog, and more.

### Q: How do I publish to skypack.dev?

Simply [publish to npm](https://docs.npmjs.com/cli/v7/commands/npm-publish) as you would normally! As soon as you publish, your package can be served from `https://cdn.skypack.dev/[my-package]` using the exact same name you published to npm (*note that in some cases it may take a while for* [*our metadata to update*](#q-why-is-my-package-missing-or-outdated-on-skypack-dev)*, but your package is still available instantly*).

### Q: I’m having trouble with Vue!

If you’re using `.vue` components, we’d recommend using [Snowpack + Vue](https://www.snowpack.dev/guides/vue/) to build your app. But if you‘re using the pure JS version of Vue, then you’ll want to use Vue’s CDN distribution ([docs](https://v3.vuejs.org/guide/installation.html#from-cdn-or-without-a-bundler)):

```javascript
import * as Vue from 'https://cdn.skypack.dev/vue@next/dist/vue.esm-browser.prod.js';

const App = {
  template: `
    <div>
     <h1>Hello Vue3</h1>
     <p>{{ message }}</p>
    </div>
  `,
  data() {
    return {
      message: 'Oh hi from the component',
    };
  },
};
Vue.createApp(App).mount('#app');
```

*Note: the code above is for Vue 3.x. For 2.x, use the following import instead:*

```javascript
import * as Vue from 'https://cdn.skypack.dev/vue/dist/vue.esm.browser.min.js';
```

### Q: Why is my package missing or outdated on skypack.dev?

The metadata for the skypack.dev search catalog works a little differently than cdn.skypack.dev. Whereas cdn.skypack.dev *actively* fetches updates, [www.skypack.dev](http://www.skypack.dev) *passively* receives updates from  [npm’s public registry API notifier](https://github.com/npm/registry). Sometimes this can lag behind a bit, but we always post updates as soon as npm notifies us of the update. Usually this happens within minutes, but in rare cases it can take up to an hour or more.

The same issue can happen with package updates. Sometimes you may publish a new version to npm,  package is present on skypack.dev, but it takes us longer than expected to receive an update for skypack.dev.

In both cases it’s important to know that **cdn.skypack.dev will always serve the most up-to-date versions.** This problem is limited only to the search catalog metadata, not the actual serving of your package.

If your package is missing from Skypack, [please open an issue](https://github.com/snowpackjs/skypack-cdn/issues)!

### Q: What registries does Skypack support?

At this time, Skypack only supports the npm registry. If you’d like to see us expand support to multiple registries, [please also open an issue](https://github.com/snowpackjs/skypack-cdn/issues).
