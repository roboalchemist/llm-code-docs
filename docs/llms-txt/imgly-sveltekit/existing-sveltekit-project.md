# Existing SvelteKit Project

This guide shows you how to integrate CreativeEditor SDK (CE.SDK) in an existing **SvelteKit** app. You can follow these steps to get a **SvelteKit app** with a fully functional CE.SDK custom component, ready for editing, templating, or further customization.

## What’s CreativeEditor SDK?[#](#whats-creativeeditor-sdk)

CreativeEditor SDK (CE.SDK) lets you integrate a customizable image and video editor into your web app. It includes filters, text overlays, and other media editing tools, and adapts easily to your use case.

CreativeEditor SDK is a commercial product. To use it, you need a valid license key. If you don’t have one yet, you can get a free trial or purchase a license.

[Free Trial](https://img.ly/forms/free-trial)[

Purchase License

](https://img.ly/pricing)

## Who Is This Guide For?[#](#who-is-this-guide-for)

This guide is for developers who:

*   Are familiar with SvelteKit.
*   Already have a SvelteKit project set up.
*   Want to integrate a powerful image and video editing component into their SvelteKit app.

## What You’ll Achieve[#](#what-youll-achieve)

*   Install CE.SDK.
*   Set up CE.SDK within your SvelteKit project.
*   Create a creative editor component using CE.SDK.
*   Render the custom CE.SDK component.

## Prerequisites[#](#prerequisites)

Before you begin, make sure you have:

*   Node.js **v20+**. [Download the latest LTS version of Node.js](https://nodejs.org/en/download).
*   A package manager (npm, yarn, pnpm)
*   A **SvelteKit v2** project created using the Svelte CLI.
*   A valid **CE.SDK license key**.

## Step 1: Install CE.SDK[#](#step-1-install-cesdk)

Add CreativeEditor SDK to your project’s dependencies by installing the [@cesdk/cesdk-js](https://www.npmjs.com/package/@cesdk/cesdk-js) package:

[

npm

](#tab-panel-78)[

yarn

](#tab-panel-79)[

pnpm

](#tab-panel-80)

`shell npm install @cesdk/cesdk-js`

`shell yarn add @cesdk/cesdk-js`

`shell pnpm add @cesdk/cesdk-js`

## Step 2: Define the Creative Editor Svelte Component[#](#step-2-define-the-creative-editor-svelte-component)

If you used the Svelte CLI to create your SvelteKit project, it should have the following structure:

```
your-sveltekit-app/│├── src│   ├── app.html│   ├── lib│   │   └── ...│   └── routes│       └── ...│├── static│   └── ...│├── .gitignore├── .npmrc├── jsconfig.json├── package-lock.json├── package.json├── README.md├── svelte.config.js└── vite.config.js
```

To start creating your custom CE.SDK component, follow these steps:

1.  Navigate to `src/lib/` folder of your project.
2.  Create a new file named `CreativeEditorSDK.svelte`.
3.  Paste the following code into `CreativeEditorSDK.svelte`:

[

JavaScript

](#tab-panel-90)[

TypeScript

](#tab-panel-91)

Replace `<YOUR_LICENSE_KEY>` with your valid CE.SDK **license key**.

CreativeEditorSDK.svelte

```
<script>  import CreativeEditorSDK from '@cesdk/cesdk-js';  import { onDestroy, onMount } from 'svelte';
  // Reference to the container HTML element where CE.SDK will be initialized  let container;  // Where to keep track of the CE.SDK instance  let cesdk = null;
  // Default CreativeEditor SDK configuration  const defaultConfig = {    // license: 'YOUR_CESDK_LICENSE_KEY', // Replace with a valid CE.SDK license key    // Other default configs...  };
  // Accessing the component's props  const { el, children, class: _, config, ...props } = $props();
  // Hook to initialize the CreativeEditorSDK component  onMount(() => {    // Integrate the configs read from props with the default ones    const ceSDKConfig = {      ...defaultConfig,      ...config,    };
    try {      // Initialize the CreativeEditorSDK instance in the container element      // using the given config      CreativeEditorSDK.create(container, ceSDKConfig).then(async instance => {        cesdk = instance;
        // Do something with the instance of CreativeEditor SDK (e.g., populate        // the asset library with default / demo asset sources)        await Promise.all([          cesdk.addDefaultAssetSources(),          cesdk.addDemoAssetSources({ sceneMode: 'Design' }),        ]);
        // Create a new design scene in the editor        await cesdk.createDesignScene();      });    } catch (err) {      console.warn(`CreativeEditor SDK failed to mount.`, { err });    }  });
  // Hook to clean up when the component unmounts  onDestroy(() => {    try {      // Dispose of the CE.SDK instance if it exists      if (cesdk) {        cesdk.dispose();        cesdk = null;      }    } catch (err) {      // Log error if CreativeEditor SDK fails to unmount      console.warn(`CreativeEditor SDK failed to unmount.`, { err });    }  });</script>
<!-- The container HTML element where the CE.SDK editor will be mounted --><div id="cesdk_container" bind:this="{container}"></div>
<style>  /* Styling for the CE.SDK container element to take full viewport size */  #cesdk_container {    height: 100vh;    width: 100vw;  }</style>
```

Replace `<YOUR_LICENSE_KEY>` with your valid CE.SDK **license key**.

CreativeEditorSDK.svelte

```
<script>  import CreativeEditorSDK from '@cesdk/cesdk-js';  import { onDestroy, onMount } from 'svelte';
  // Reference to the container HTML element where CE.SDK will be initialized  /** @type {HTMLDivElement | null} */  let container = null;  // Where to keep track of the CE.SDK instance  /** @type {any}*/  let cesdk = null;
  // Default CreativeEditor SDK configuration  /** @type {Record<string, any>}*/  export let config = {};
  /** @type {'local'}*/  const ON_UPLOAD = 'local';  const defaultConfig = {    // license: 'YOUR_CESDK_LICENSE_KEY', // Replace with a valid CE.SDK license key    callbacks: { onUpload: ON_UPLOAD }, // Enable local file uploads in the Asset Library    // Other default configs...  };
  // Hook to initialize the CreativeEditorSDK component  onMount(() => {    // Integrate the configs read from props with the default ones    const ceSDKConfig = {      ...defaultConfig,      ...config,    };
    if (!container) return;
    try {      // Initialize the CreativeEditorSDK instance in the container element      // using the given config      CreativeEditorSDK.create(container, ceSDKConfig).then(async instance => {        cesdk = instance;
        // Do something with the instance of CreativeEditor SDK (e.g., populate        // the asset library with default / demo asset sources)        await Promise.all([          cesdk.addDefaultAssetSources(),          cesdk.addDemoAssetSources({ sceneMode: 'Design' }),        ]);
        // Create a new design scene in the editor        await cesdk.createDesignScene();      });    } catch (err) {      console.warn(`CreativeEditor SDK failed to mount.`, { err });    }  });
  // Hook to clean up when the component unmounts  onDestroy(() => {    try {      // Dispose of the CE.SDK instance if it exists      if (cesdk) {        cesdk.dispose();        cesdk = null;      }    } catch (err) {      // Log error if CreativeEditor SDK fails to unmount      console.warn(`CreativeEditor SDK failed to unmount.`, { err });    }  });</script>
<!-- The container HTML element where the CE.SDK editor will be mounted --><div id="cesdk_container" bind:this="{container}"></div>
<style>  /* Styling for the CE.SDK container element to take full viewport size */  #cesdk_container {    height: 100vh;    width: 100vw;  }</style>
```

This Svelte component:

*   Initializes the CreativeEditor SDK inside the component’s `<div>` container.
*   Disposes of the SDK instance on unmount to free resources.

### Optional: Export Component Using the Module System[#](#optional-export-component-using-the-module-system)

If you organize your SvelteKit project’s components in a single `src/lib/index.js` file, add the following line to `index.js`:

index.js

```
export { default as CreativeEditorSDK } from './CreativeEditorSDK.svelte';
```

## Step 3: Use the Creative Editor Component[#](#step-3-use-the-creative-editor-component)

CreativeEditor SDK only runs on the client. To handle client-side rendering, you have to:

1.  Import the component in a route file.
2.  Render the component on a page withing your project.

### Import the CreativeEditorSDK Component[#](#import-the-creativeeditorsdk-component)

Dynamically import `CreativeEditorSDK` component as follows:

1.  Open the relevant **SSR route file**, where you want to embed the component (for example, `src/routes/+page.svelte`).
2.  Navigate to the `<script>` section.
3.  Paste this code to **dynamically import** the `CreativeEditorSDK` component:

[

JavaScript

](#tab-panel-84)[

TypeScript

](#tab-panel-85)

+page.svelte

```
import { browser } from '$app/environment'; // True only if the app is running in the browser// Use the browser flag to conditionally render client-side componentslet isClient = browser;
let CreativeEditorSDK;if (isClient) {  // Dynamically import the CreativeEditorSDK component only in the browser  import('$lib/CreativeEditorSDK.svelte').then(module => {    CreativeEditorSDK = module.default;  });}
```

+page.svelte

```
<script lang="ts">import type { ComponentType } from 'svelte';import { browser } from '$app/environment'; // True only if the app is running in the browser// Use the browser flag to conditionally render client-side componentslet isClient = browser;
let CreativeEditorSDK: ComponentType | null = null;if (isClient) {  // Dynamically import the CreativeEditorSDK component only in the browser  import('$lib/CreativeEditorSDK.svelte').then(module => {    CreativeEditorSDK = module.default;  });}</script>
{#if isClient && CreativeEditorSDK}  <CreativeEditorSDK    config={{      // Your custom configs here    }}  />{/if}
```

  

The ’browser’ flag in `$app/environment` identifies code that runs in the browser. For more information, visit

[

SvelteKit docs

](https://svelte.dev/docs/kit/$app-environment#browser)

.

### Optional: Import Components Using the Module System[#](#optional-import-components-using-the-module-system)

If you [exported `CreativeEditorSDK` in `src/lib/index.js`](sveltekit/get-started/existing-project-x7678d/#using-the-module-system-for-exports), you can simplify the dynamic import:

+page.svelte

```
import('$lib').then(module => {  CreativeEditorSDK = module.CreativeEditorSDK;});
```

### Render the CreativeEditorSDK Component[#](#render-the-creativeeditorsdk-component)

Now, make sure that your app renders the video editor component only on the client side. Add this to the template section of your SvelteKit route:

[

Default Configs

](#tab-panel-86)[

Custom Configs

](#tab-panel-87)

+page.svelte

```
{#if isClient && CreativeEditorSDK}<CreativeEditorSDK />{/if}
```

+page.svelte

```
{#if isClient && CreativeEditorSDK}  <CreativeEditorSDK    config={{      // Your custom configs here    }}  />{/if}
```

Your **final `src/routes/+page.svelte` file** should look like this:

[

Default Configs

](#tab-panel-88)[

Custom Configs

](#tab-panel-89)

+page.svelte

```
<script>  // Other imports...
  import { browser } from "$app/environment"; // True only if the app is running in the browser  // Use the browser flag to conditionally render client-side components  let isClient = browser;
  let CreativeEditorSDK;  if (isClient) {    // Dynamically import the CreativeEditorSDK component only in the browser    import("$lib/CreativeEditorSDK.svelte").then(module => {      CreativeEditorSDK = module.default;    });  }</script>
<main>  <!-- Other components... -->  {#if isClient && CreativeEditorSDK}    <CreativeEditorSDK />  {/if}  <!-- Other components... --></main>
<style>  /* Custom styling... */</style>
```

+page.svelte

```
<script>  // Other imports...
  import { browser } from "$app/environment"; // True only if the app is running in the browser  // Use the browser flag to conditionally render client-side components  let isClient = browser;
  let CreativeEditorSDK;  if (isClient) {    // Dynamically import the CreativeEditorSDK component only in the browser    import("$lib/CreativeEditorSDK.svelte").then(module => {      CreativeEditorSDK = module.default;    });  }</script>
<main>  <!-- Other components... -->  {#if isClient && CreativeEditorSDK}    <CreativeEditorSDK      config={{        // Custom configs...      }}    />  {/if}  <!-- Other components... --></main>
<style>  /* Custom styling... */</style>
```

## Step 4: Serve the SvelteKit Project Locally[#](#step-4-serve-the-sveltekit-project-locally)

Start your SvelteKit project locally with the run command. Basic ones are:

[

npm

](#tab-panel-81)[

yarn

](#tab-panel-82)[

pnpm

](#tab-panel-83)

`shell npm run dev`

`shell yarn dev`

`shell pnpm run dev`

## Step 5: Test the Integration[#](#step-5-test-the-integration)

By default, Vite serves your app on your localhost. To test the integration:

1.  Open `http://localhost:5173/` in your browser.
2.  A fully functional CE.SDK editor should load.

## Troubleshooting & Common Errors[#](#troubleshooting--common-errors)

**❌ Error**: `Cannot find module '@cesdk/cesdk-js'`

*   Check that you’ve installed CE.SDK with `npm install @cesdk/cesdk-js`.

**❌ Error**: `The $props rune is only available inside .svelte and .svelte.js/ts files`

1.  Open `CreativeEditorSDK.svelte`.
2.  Check the **top level** of the `<script>` section.
3.  Make sure you’re using `$props()` at this level, rather than inside `onMount()` or other lifecycle methods.

**❌ Error**: `Error when evaluating SSR module /src/routes/+page.svelte: document is not defined`

*   In `/src/routes/+page.svelte`, make sure `CreativeEditorSDK` is:
    
    *   Dynamically imported.
    *   Only rendered on the client side.

**❌ Error**: `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

*   Verify that your CE.SDK license key is correct and hasn’t expired.

**❌ Editor doesn’t load**

*   Check the browser console for any errors.
*   Ensure that component and library imports are correct.

## Next Steps[#](#next-steps)

Congratulations! You’ve successfully integrated CE.SDK into an existing SvelteKit project. Now, feel free to explore the SDK and proceed to the next steps whenever you’re ready:

*   [Configure the Creative Editor](sveltekit/user-interface/overview-41101a/)
*   [Serve assets from your own servers](sveltekit/serve-assets-b0827c/)
*   [Create and use a license key](sveltekit/licensing-8aa063/)
*   [Configure callbacks](sveltekit/actions-6ch24x/)
*   [
    
    Customize interface labels and translations
    
    ](sveltekit/user-interface/localization-508e20/)
*   [Edit colors and appearance with themes](sveltekit/user-interface/appearance/theming-4b0938/)

---



[Source](https:/img.ly/docs/cesdk/sveltekit/get-started/clone-github-project-y8789e)