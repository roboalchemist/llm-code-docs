# Existing Vue.js Project

This guide walks you through integrating the **CreativeEditor SDK (CE.SDK)** into an existing Vue.js application. By the end, you’ll have a functional editor rendered within a Vue component — ready for editing, templating, or further customization.

## **Who is This Guide For?**[#](#who-is-this-guide-for)

This guide is for developers who:

*   Are already working with a **Vue 2 or 3** project (Vue CLI or Vite).
*   Want to embed a **powerful creative editor** directly into their app.
*   Prefer a **component-based integration** without starting from scratch.

## **What You’ll Achieve**[#](#what-youll-achieve)

*   Add CE.SDK to your existing Vue project.
*   Render the editor inside a reusable component.
*   Configure basic asset sources and scene loading.

## **Prerequisites**[#](#prerequisites)

Ensure you have:

*   An existing **Vue.js project**.
*   **Node.js v20+**
*   **npm** or **yarn**
*   A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)).

## **Step 1: Install CE.SDK**[#](#step-1-install-cesdk)

In your project root, run:

Terminal window

```
npm install --save @cesdk/cesdk-js
```

## **Step 2: Create the Editor Component**[#](#step-2-create-the-editor-component)

Create a file at `src/components/CreativeEditor.vue`:

```
<template>  <CreativeEditor :config="config" :init="init" width="100vw" height="100vh" /></template>
<script>import CreativeEditor from '@cesdk/cesdk-js/vue';
export default {  name: 'CreativeEditorWrapper',  components: {    CreativeEditor,  },  props: {    config: {      type: Object,      required: true,    },  },  data() {    return {      init: async cesdk => {        await cesdk.addDefaultAssetSources();        await cesdk.addDemoAssetSources({          sceneMode: 'Design',          withUploadAssetSources: true,        });        await cesdk.createDesignScene();      },    };  },};</script>
```

## **Step 3: Use the Component in App.vue**[#](#step-3-use-the-component-in-appvue)

Open `App.vue` (or any parent view), and replace or extend the template/script like so:

```
<template>  <CreativeEditorWrapper :config="editorConfig" /></template>
<script>import CreativeEditorWrapper from './components/CreativeEditor.vue';
export default {  name: 'App',  components: { CreativeEditorWrapper },  data() {    return {      editorConfig: {        // license: 'YOUR_CESDK_LICENSE_KEY',        baseURL:          'https://cdn.img.ly/packages/imgly/cesdk-js/1.67.0/assets',      },    };  },};</script>
```

## **Editor Setup Disclaimer**[#](#editor-setup-disclaimer)

> Note: CE.SDK serves all assets (images, fonts, templates) from IMG.LY’s CDN by default. In production, you should serve assets from your own servers.

## **Step 4: Run Your Project**[#](#step-4-run-your-project)

If using Vue CLI:

Terminal window

```
npm run serve
```

Then visit `http://localhost:8080/` to see the editor.

## **Troubleshooting & Common Errors**[#](#troubleshooting--common-errors)

❌ **CE.SDK not visible**

Ensure the container `<div>` is full screen and styled correctly.

❌ **Invalid license key**

Check that your license key is correct and not expired. You can get a free trial [here](https://img.ly/forms/free-trial).

❌ **Runtime error: Cannot read private member `#e`**

This is caused by Babel transpiling CE.SDK code, which uses modern JS features like `#privateFields`.

**Fix this by excluding CE.SDK from Babel transpilation:**

Create or update `vue.config.js` in your project root:

```
const path = require('path');
module.exports = {  chainWebpack: config => {    config.resolve.alias      .set(        '@cesdk/engine',        path.resolve(__dirname, 'node_modules/@cesdk/engine'),      )      .set(        '@cesdk/cesdk-js',        path.resolve(__dirname, 'node_modules/@cesdk/cesdk-js'),      );
    config.module      .rule('js')      .exclude.add(path.resolve(__dirname, 'node_modules/@cesdk/engine'))      .add(path.resolve(__dirname, 'node_modules/@cesdk/cesdk-js'))      .end();  },};
```

Then clean and reinstall:

Terminal window

```
rm -rf node_modulesnpm install
```

And restart:

Terminal window

```
npm run serve
```

## **Next Steps**[#](#next-steps)

*   [Customize the Editor Configuration](vue/user-interface/customization-72b2f8/)
*   [Adapt the UI and Themes](vue/user-interface/appearance/theming-4b0938/)
*   [Serve Your Own Assets](vue/serve-assets-b0827c/)

---



[Source](https:/img.ly/docs/cesdk/vue/get-started/clone-github-project-p9890v)