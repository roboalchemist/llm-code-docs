# Source: https://www.mux.com/docs/guides/uploader-web-integrate-in-your-webapp.md

# Integrate Mux Uploader into your web application
In this guide, you will learn about Mux Uploader and how to use it in your web application.
## Install Mux Uploader

Mux Uploader has 2 packages:

* `@mux/mux-uploader`: the web component, compatible with all frontend frameworks
* `@mux/mux-uploader-react`: the React component, for usage in React

Both are built with TypeScript and can be installed either via `npm`, `yarn` or the hosted option on `jsdelivr`.

### NPM

```shell
npm install @mux/mux-uploader@latest #or @mux/mux-uploader-react@latest
```

### Yarn

```shell
yarn add @mux/mux-uploader@latest #or @mux/mux-uploader-react@latest
```

### Hosted

```html
<script src="https://cdn.jsdelivr.net/npm/@mux/mux-uploader"></script>
<!--
or src="https://cdn.jsdelivr.net/npm/@mux/mux-uploader-react"
-->
```

## Providing attributes

The only required value to use Mux uploader is [`endpoint`](/docs/guides/mux-uploader#upload-a-video).

## Examples

### HTML element

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<!-- Replace endpoint value with a valid Mux Video Direct Upload URL -->\n<mux-uploader\n  endpoint=\"https://httpbin.org/put\"\n></mux-uploader>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js'",
      "hidden": true
    }
  }
}
```

Using in HTML just requires adding the hosted `<script>` tag to your page and then adding the `<mux-uploader>` element where you need it.

### React

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader-react": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import MuxUploader from \"@mux/mux-uploader-react\";\n\nexport default function App() {\n  return (\n    <MuxUploader endpoint=\"https://httpbin.org/put\" />\n  );\n}\n",
      "active": true
    },
    "/src/index.js": {
      "code": "",
      "hidden": true
    }
  },
  "template": "react"
}
```

For our React implementation, you can use it just like you would any other React component.

### Svelte

Because Svelte supports web components, it doesn't need a separate wrapper component like React. View the SveltKit example in the
[Mux Elements repo](https://github.com/muxinc/elements/tree/main/examples/svelte-kit) for a fully functioning example.

```html
<script context="module" lang="ts">
  export const prerender = true;
</script>

<script lang="ts">
  // this prevents the custom elements from being redefined when the REPL is updated and reloads, which throws an error
  // this means that any changes to the custom element won't be picked up without saving and refreshing the REPL
  // const oldRegister = customElements.define;
  // customElements.define = function(name, constructor, options) {
  // 	if (!customElements.get(name)) {
  // 		oldRegister(name, constructor, options);
  // 	}
  // }
  // import { page } from '$app/stores';
  import { onMount } from "svelte";
  onMount(async () => {
    await import("@mux/mux-uploader");
  });
</script>

<mux-uploader endpoint="https://httpbin.org/put" />
```

### Vue

Because Vue supports web components, it doesn't need a separate wrapper component like React. View the Vue example in the [Mux Elements repo](https://github.com/muxinc/elements/tree/main/examples/vue-with-typescript) for a fully functioning example.

```html
<script setup lang="ts">
  import "@mux/mux-uploader";
</script>

<template>
  <main>
    <mux-uploader endpoint="https://httpbin.org/put" />
  </main>
</template>
```

<GuideCard
  title="Customize the look and feel"
  description="Customize Mux Uploader to match your brand"
  links={[
    {
      title: "Read the guide",
      href: "/docs/guides/uploader-web-customize-look-and-feel",
    },
  ]}
/>

{/* <GuideCard
    title="Advanced usage"
    description="Learn about advanced usage of Mux Player"
    links={[
      {
        title: "Read the guide",
        href: "/docs/guides/player-advanced-usage",
      },
    ]}
  /> */}
