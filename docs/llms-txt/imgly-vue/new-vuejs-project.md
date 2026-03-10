# New Vue.js Project

This guide walks you through integrating the **CreativeEditor SDK (CE.SDK)** into a new Vue.js application. By the end, you’ll have a functional editor rendered within a Vue component — ready for editing, templating, or further customization.

## **Who is This Guide For?**[#](#who-is-this-guide-for)

This guide is for developers who:

*   Are using **Vue 2 or 3** (Vue CLI or Vite).
*   Want to embed **a powerful creative editor** directly into a web app.
*   Prefer a **component-based approach** for SDK initialization and teardown.

## **What You’ll Achieve**[#](#what-youll-achieve)

*   Create a Vue.js project with CE.SDK installed.
*   Load the editor via CDN or npm.
*   Add default assets and templates to get started quickly.

## **Prerequisites**[#](#prerequisites)

Make sure you have the following:

*   **Node.js (v20 or later)**
*   **npm or yarn**
*   A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial))
*   **Vue CLI** (for Vue 2/3) Install with:
    
    Terminal window
    
    ```
    npm install -g @vue/cli
    ```
    

## **Step 1: Create a New Vue Project**[#](#step-1-create-a-new-vue-project)

Terminal window

```
vue create cesdk-vue-app
```

*   Choose the default preset or manually select Babel, Router, etc.
*   Navigate to your project folder:
    
    Terminal window
    
    ```
    cd cesdk-vue-app
    ```
    

## **Step 2: Install CE.SDK**[#](#step-2-install-cesdk)

Terminal window

```
npm install --save @cesdk/cesdk-js
```

## **Step 3: Create the Editor Component**[#](#step-3-create-the-editor-component)

Create `src/components/CreativeEditor.vue`:

```
<template>  <CreativeEditor :config="config" :init="init" width="100vw" height="100vh" /></template>
<script>import CreativeEditor from '@cesdk/cesdk-js/vue';
export default {  name: 'CreativeEditorWrapper',  components: {    CreativeEditor,  },  props: {    config: {      type: Object,      required: true,    },  },  data() {    return {      init: async cesdk => {        await cesdk.addDefaultAssetSources();        await cesdk.addDemoAssetSources({          sceneMode: 'Design',          withUploadAssetSources: true,        });        await cesdk.createDesignScene();      },    };  },};</script>
```

## **Step 4: Use the Component in App.vue**[#](#step-4-use-the-component-in-appvue)

Replace your template/script in `App.vue`:

```
<template>  <CreativeEditorWrapper :config="editorConfig" /></template>
<script>import CreativeEditorWrapper from './components/CreativeEditor.vue';
export default {  name: 'App',  components: { CreativeEditorWrapper },  data() {    return {      editorConfig: {        // license: 'YOUR_CESDK_LICENSE_KEY',        baseURL:          'https://cdn.img.ly/packages/imgly/cesdk-js/1.67.0/assets',      },    };  },};</script>
```

### **Editor Setup Disclaimer**[#](#editor-setup-disclaimer)

> Note: For convenience, CE.SDK serves assets (e.g., images, stickers, fonts) from IMG.LY’s CDN by default. In production, you should serve assets from your own server

## **Step 6: Run the Project**[#](#step-6-run-the-project)

Terminal window

```
npm run serve
```

Go to `http://localhost:8080/` to see CE.SDK running in your Vue app.

## **Troubleshooting & Common Errors**[#](#troubleshooting--common-errors)

❌ **CE.SDK not visible**

Ensure the `#cesdk_container` element is full-screen and not obstructed by parent layout.

❌ **Invalid license key**

Use a valid [trial or production license key](https://img.ly/forms/free-trial).

❌ **Runtime error: Cannot read private member `#e`**

This is caused by Babel transpiling CE.SDK’s internal code, which uses modern features like `#privateFields`.

**Fix this by excluding CE.SDK modules from Babel:**

Create or update `vue.config.js` in your project root:

```
const path = require('path');module.exports = {  chainWebpack: config => {    config.resolve.alias      .set(        '@cesdk/engine',        path.resolve(__dirname, 'node_modules/@cesdk/engine'),      )      .set(        '@cesdk/cesdk-js',        path.resolve(__dirname, 'node_modules/@cesdk/cesdk-js'),      );
    config.module      .rule('js')      .exclude.add(path.resolve(__dirname, 'node_modules/@cesdk/engine'))      .add(path.resolve(__dirname, 'node_modules/@cesdk/cesdk-js'))      .end();  },};
```

Then clean and reinstall:

Terminal window

```
rm -rf node_modulesnpm install
```

Restart your dev server with:

Terminal window

```
npm run serve
```

## **Next Steps**[#](#next-steps)

*   [Customize the Editor Configuration](vue/user-interface/customization-72b2f8/)
*   [Adapt the UI and Themes](vue/user-interface/appearance/theming-4b0938/)
*   [Serve Your Own Assets](vue/serve-assets-b0827c/)

---



[Source](https:/img.ly/docs/cesdk/vue/get-started/mcp-server-fde71c)