# Source: https://docs.replit.com/extensions/development/installation.md

# Manual Installation

> Learn how to install and initialize the Replit Extensions API client using script tags or npm packages for your project.

While we recommend using our [templates](/extensions/extensions#templates) to get started, you can also install the API client manually.

### As a `<script>` import

Start using the Extensions API client by inserting this code into the `<head>` tag of your HTML:

```html  theme={null}
<script src="https://unpkg.com/@replit/extensions@1.8.0/dist/index.global.js"></script>
```

Start using the API client by creating a new `<script>` tag and using the pre-defined `replit` variable.

```html  theme={null}
<script>
  async function main() {
    await replit.init();

    ...
  }

  window.addEventListener('load', main);
</script>
```

### As an npm package

Install the client with your preferred package manager, and use the `import` statement to start using it.

```
npm install @replit/extensions
yarn add @replit/extensions
pnpm add @replit/extensions
```

After installing the API client, use the `import` statement to start using it.

```tsx  theme={null}
import {
  fs,
  data,
  ...
} from '@replit/extensions';
```
