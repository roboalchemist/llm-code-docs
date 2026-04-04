# New SvelteKit Project

This guide will walk you through creating a new SvelteKit project and integrating CreativeEditor SDK (CE.SDK) using a custom component. By the end, you’ll have a SvelteKit application with a fully functional CE.SDK component, ready for further customization.

This guide shows you how to integrate the CreativeEditor SDK (CE.SDK) into a new SvelteKit project. You’ll create a custom Svelte component and set up a fully functional image and video editor, ready for editing, templating, and further customization.

## What’s CreativeEditor SDK?[#](#whats-creativeeditor-sdk)

CreativeEditor SDK (CE.SDK) lets you integrate a customizable image and video editor into your web app. It includes filters, text overlays, and other media editing tools, and adapts easily to your use case.

CreativeEditor SDK is a commercial product. To use it, you need a valid license key. If you don’t have one yet, you can get a free trial or purchase a license.

[Free Trial](https://img.ly/forms/free-trial)[

Purchase License

](https://img.ly/pricing)

## Who Is This Guide For?[#](#who-is-this-guide-for)

This guide is for developers who:

*   Are familiar with SvelteKit.
*   Need to set up a new SvelteKit project from scratch.
*   Want to add a robust image and video editor to a SvelteKit app.

## What You’ll Achieve[#](#what-youll-achieve)

*   Set up a new SvelteKit project using the **Svelte CLI**.
*   Install CE.SDK via **npm**.
*   Create a custom Svelte **component** for CE.SDK with default settings.
*   Render the CE.SDK component within your app.

## Prerequisites[#](#prerequisites)

Before starting, ensure you have the following:

*   **Node.js v20+** with **npm 10+** installed in your dev environment. [Download the latest LTS version of Node.js and npm](https://nodejs.org/en/download).
*   A valid **CE.SDK license key**.

## Step 1: Create a New SvelteKit Project[#](#step-1-create-a-new-sveltekit-project)

Create a new SvelteKit project named `my-sveltekit-app` using the [Svelte CLI](https://svelte.dev/docs/kit/creating-a-project):

Terminal window

```
npx sv create my-sveltekit-app
```

Your terminal will prompt you with a few setup questions. For this guide, opt for minimal settings:

*   **Template**: SvelteKit minimal.
*   **Type checking with TypeScript**: No.
*   **What to add to your project**: Press enter (none).
*   **Package manager**: npm.

Once the project is created, navigate into the project folder:

Terminal window

```
cd my-sveltekit-app
```

The SvelteKit project should contain a file structure as below:

```
my-sveltekit-app/│├── src                     # Source code│   ├── app.html            # Main HTML file for the app│   ├── lib                 # Library assets│   │   │__assets           # Images and other static asset│   │   │  └── favicon.svg  # Svelte logo asset│   │   └── index.js        # Entry point for the lib folder│   └── routes              # Application routes│       └── +page.svelte    # Svelte page component (default route)│       └── +layout.svelte  # Styles│├── static                # Static assets│   └── robots.txt        # SEO file│├── .gitignore            # Git ignore rules├── .npmrc                # npm configuration├── jsconfig.json         # JavaScript project config├── package-lock.json     # npm dependency lock file├── package.json          # Project metadata and dependencies├── README.md             # Project documentation├── svelte.config.js      # Svelte configuration└── vite.config.js        # Vite configuration
```

Install the project dependencies with:

Terminal window

```
npm install
```

## Step 2: Install CE.SDK[#](#step-2-install-cesdk)

Add CreativeEditor SDK to your project’s dependencies. Installing it via the [`@cesdk/cesdk-js`](https://www.npmjs.com/package/@cesdk/cesdk-js) NPM package:

Terminal window

```
npm install @cesdk/cesdk-js
```

## Step 3: Define the Creative Editor Svelte Component[#](#step-3-define-the-creative-editor-svelte-component)

In the `src/lib/` folder of your new SvelteKit project, add a new file named `CreativeEditorSDK.svelte`. Define it as follows:

```
<script>  import CreativeEditorSDK from '@cesdk/cesdk-js';  import { onDestroy, onMount } from 'svelte';
  // reference to the container HTML element where CE.SDK will be initialized  let container;  // where to keep track of the CE.SDK instance  let cesdk = null;
  // default CreativeEditor SDK configuration  const defaultConfig = {    // license: 'YOUR_CESDK_LICENSE_KEY', // replace it with a valid CE.SDK license key    // other default configs...  };
  // accessing the component's props  const { el, children, class: _, config, ...props } = $props();
  // hook to initialize the CreativeEditorSDK component  onMount(() => {    // integrate the configs read from props with the default ones    const ceSDKConfig = {      ...defaultConfig,      ...config,    };
    try {      // initialize the CreativeEditorSDK instance in the container element      // using the given config      CreativeEditorSDK.create(container, ceSDKConfig).then(async instance => {        cesdk = instance;
        // do something with the instance of CreativeEditor SDK (e.g., populate        // the asset library with default / demo asset sources)        await Promise.all([          cesdk.addDefaultAssetSources(),          cesdk.addDemoAssetSources({            sceneMode: 'Design',            withUploadAssetSources: true,          }),        ]);
        // create a new design scene in the editor        await cesdk.createDesignScene();      });    } catch (err) {      console.warn(`CreativeEditor SDK failed to mount.`, { err });    }  });
  // hook to clean up when the component unmounts  onDestroy(() => {    try {      // dispose of the CE.SDK instance if it exists      if (cesdk) {        cesdk.dispose();        cesdk = null;      }    } catch (err) {      // log error if CreativeEditor SDK fails to unmount      console.warn(`CreativeEditor SDK failed to unmount.`, { err });    }  });</script>
<!-- the container HTML element where the CE.SDK editor will be mounted --><div id="cesdk_container" bind:this="{container}"></div>
<style>  /* styling for the CE.SDK container element to take full viewport size */  #cesdk_container {    height: 100vh;    width: 100vw;  }</style>
```

This Svelte component loads the CreativeEditor SDK instance within a `<div>` container element defined in the component’s HTML. When the component is unmounted, the CE.SDK instance is correctly disposed of to release resources.

To simplify the import of the `CreativeEditorSDK.svelte` component, export it in the `index.js` file inside the `src/lib/` folder:

```
export { default as CreativeEditorSDK } from './CreativeEditorSDK.svelte';
```

## Step 4: Use the Creative Editor Component[#](#step-4-use-the-creative-editor-component)

CreativeEditor SDK must be used on the client to work. In your SSR `src/routes/+page.svelte` route file, dynamically import the `CreativeEditorSDK.svelte` component inside the `<script>` section:

```
import { browser } from '$app/environment'; // true only if the app is running in the browser// use the browser flag to conditionally render client-side componentslet isClient = browser;
let CreativeEditorSDK;if (isClient) {  // dynamically import the CreativeEditorSDK component only in the browser  import('$lib').then(module => {    CreativeEditorSDK = module.CreativeEditorSDK;  });}
```

**Note**: [`browser`](https://svelte.dev/docs/kit/$app-environment#browser) from `$app/environment` is a special flag that is true only when the application is rendered in the browser.

Now, conditionally render the video editor component on the client side. Add this to the template section of your SvelteKit route:

```
{#if isClient && CreativeEditorSDK}  <CreativeEditorSDK    config={{      // Your custom configs here    }}  />{/if}
```

Or, if you don’t need custom configurations, use:

```
{#if isClient && CreativeEditorSDK}<CreativeEditorSDK />{/if}
```

`src/routes/+page.svelte` will contain something like:

```
<script>  // other imports...
  import { browser } from "$app/environment"; // true only if the app is running in the browser  // use the browser flag to conditionally render client-side components  let isClient = browser;
  let CreativeEditorSDK;  if (isClient) {    // dynamically import the CreativeEditorSDK component only in the browser    import("$lib").then(module => {      CreativeEditorSDK = module.CreativeEditorSDK;    });  }</script>
<main>  <!-- other components... -->  {#if isClient && CreativeEditorSDK}    <CreativeEditorSDK      config={{        // custom configs...      }}    />  {/if}  <!-- other components... --></main>
<style>  /* custom styling... */</style>
```

## Step 5: Serve the SvelteKit Project Locally[#](#step-5-serve-the-sveltekit-project-locally)

Run the project locally with the following command:

Terminal window

```
npm run dev
```

By default, the SvelteKit app runs with Vite on localhost. Open `http://localhost:5173/` to see your SvelteKit project starter page.

## Step 3: Install CE.SDK[#](#step-3-install-cesdk)

Add CreativeEditor SDK to your project’s dependencies via the [`@cesdk/cesdk-js`](https://www.npmjs.com/package/@cesdk/cesdk-js) npm package:

Terminal window

```
npm install @cesdk/cesdk-js
```

## Step 4: Create the Creative Editor Svelte Component[#](#step-4-create-the-creative-editor-svelte-component)

1.  Open the `src/lib/` folder of your new SvelteKit project.
2.  Create a **new file** named `CreativeEditorSDK.svelte`.
3.  Paste the following code into `CreativeEditorSDK.svelte`:

Replace `<YOUR_LICENSE_KEY>` with a valid CE.SDK license key.

CreativeEditorSDK.svelte

```
<script>  import CreativeEditorSDK from '@cesdk/cesdk-js';  import { onDestroy, onMount } from 'svelte';
// Reference to the container HTML element where CE.SDK will be initializedlet container;// Where to keep track of the CE.SDK instancelet cesdk = null;
// Default CreativeEditor SDK configurationconst defaultConfig = {// license: 'YOUR_CESDK_LICENSE_KEY', // Replace with your CE.SDK license keycallbacks: { onUpload: 'local' }, // Enable local file uploads in the Asset Library// Other default configs...};
// Accessing the component's propsconst { config, ...props } = $props();
// Hook to initialize the CreativeEditorSDK componentonMount(() => {// Integrate the configs read from props with the default onesconst ceSDKConfig = {...defaultConfig,...config,};
    try {      // Initialize the CreativeEditorSDK instance in the container element      // Using the given config      CreativeEditorSDK.create(container, ceSDKConfig).then(async instance => {        cesdk = instance;
        // Do something with the instance of CreativeEditor SDK (e.g., populate        // The asset library with default / demo asset sources)        await Promise.all([          cesdk.addDefaultAssetSources(),          cesdk.addDemoAssetSources({ sceneMode: 'Design' }),        ]);
        // Create a new design scene in the editor        await cesdk.createDesignScene();      });    } catch (err) {      console.warn(`CreativeEditor SDK failed to mount.`, { err });    }
});
// Hook to clean up when the component unmountsonDestroy(() => {try {// Dispose of the CE.SDK instance if it existsif (cesdk) {cesdk.dispose();cesdk = null;}} catch (err) {// Log error if CreativeEditor SDK fails to unmountconsole.warn(`CreativeEditor SDK failed to unmount.`, { err });}});
</script>
<!-- The container HTML element where the CE.SDK editor will be mounted -->
<div id="cesdk_container" bind:this="{container}"></div>
<style>  /* Styling for the CE.SDK container element to take full viewport size */  #cesdk_container {    height: 100vh;    width: 100vw;  }</style>
```

This Svelte component:

*   Initializes the CreativeEditor SDK inside the component’s `<div>` container.
*   Disposes of the SDK instance on unmount to free resources.

### Export the Component[#](#export-the-component)

To simplify the import of the `CreativeEditorSDK.svelte` component:

1.  Open the `lib/index.js` file
2.  Adding the following line:

index.js

```
export { default as CreativeEditorSDK } from './CreativeEditorSDK.svelte';
```

## Step 5: Use the Creative Editor Component[#](#step-5-use-the-creative-editor-component)

Your app needs to use the CreativeEditor SDK **on the client** to work. To handle client-side rendering, dynamically import `CreativeEditorSDK` component as follows:

1.  Open the route file: `src/routes/+page.svelte`
2.  Add a script section at the top of the file if it doesn’t exist already:

+page.svelte

```
<script>  // Imports go here</script>
```

3.  Import the component **inside the script** section:

+page.svelte

```
import { browser } from '$app/environment'; // True only when the code-block executes in the browser// Use the browser flag to apply client-side rendering to selected blocks.
let CreativeEditorSDK;if (browser) {  // Dynamically import the CreativeEditorSDK component only in the browser  import('$lib').then(module => {    CreativeEditorSDK = module.CreativeEditorSDK;  });}
```

The `browser` flag from `$app/environment` marks the code that runs in the browser. Learn more from [SvelteKit docs](https://svelte.dev/docs/kit/$app-environment#browser).

4.  Add this to the template section (`<main>`, for example) of `+page.svelte`:

[

Default Configs

](#tab-panel-95)[

Custom Configs

](#tab-panel-96)

+page.svelte

```
{#if browser && CreativeEditorSDK}<CreativeEditorSDK />{/if}
```

+page.svelte

```
{#if browser && CreativeEditorSDK}  <CreativeEditorSDK    config={{      // Your custom configs here    }}  />{/if}
```

This code conditionally renders the video editor component on the client side only.

### Final `+page.svelte` File[#](#final-pagesvelte-file)

Your final `src/routes/+page.svelte` file should contain something like:

[

Default Configs

](#tab-panel-97)[

Custom Configs

](#tab-panel-98)

+page.svelte

```
<script>  // Other imports...
  import { browser } from "$app/environment"; // True only if the app is running in the browser
  let CreativeEditorSDK;  if (browser) {    // Dynamically import the CreativeEditorSDK component only in the browser    import("$lib").then(module => {      CreativeEditorSDK = module.CreativeEditorSDK;    });  }
</script>
<main>  <!-- Other components... -->  {#if browser && CreativeEditorSDK}    <CreativeEditorSDK/>  {/if}  <!-- Other components... --></main>
<style>/* Custom styling... */</style>
```

+page.svelte

```
<script>  // Other imports...
  import { browser } from "$app/environment"; // True only if the app is running in the browser
  let CreativeEditorSDK;  if (browser) {    // Dynamically import the CreativeEditorSDK component only in the browser    import("$lib").then(module => {      CreativeEditorSDK = module.CreativeEditorSDK;    });  }</script>
<main>  <!-- Other components... -->  {#if browser && CreativeEditorSDK}    <CreativeEditorSDK      config={{        // Custom configs...      }}    />  {/if}  <!-- Other components... --></main>
<style>  /* Custom styling... */</style>
```

## Step 7: Test the Integration[#](#step-7-test-the-integration)

1.  Open `http://localhost:5173/` in your browser.
2.  A fully functional CE.SDK editor should load.

## Troubleshooting & Common Errors[#](#troubleshooting--common-errors)

**❌ Error**: `Cannot find module '@cesdk/cesdk-js'`

*   Verify that you’ve correctly installed CE.SDK via `npm install @cesdk/cesdk-js`.

**❌ Error**: `The $props rune is only available inside .svelte and .svelte.js/ts files`

*   Make sure that you’re loading the props of the `CreativeEditorSDK.svelte` component using `$props()` in the top-level `<script>` section, rather than inside onMount() or other lifecycle methods.

**❌ Error**: `Error when evaluating SSR module /src/routes/+page.svelte: document is not defined`

*   Ensure that you’re importing the `CreativeEditorSDK` Svelte component dynamically in `/src/routes/+page.svelte` and conditionally rendering it only on the client side.

**❌ Error**: `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

*   Double-check that your license key is valid and hasn’t expired.

**❌ Editor doesn’t load**

*   Inspect the browser console for any errors.
*   Ensure that your component paths and imports are correct.

## Next Steps[#](#next-steps)

Great job! You’ve successfully integrated CE.SDK into a new SvelteKit project. Now, feel free to explore the SDK and proceed to the next steps whenever you’re ready:

*   [Configure the Creative Editor](sveltekit/user-interface/overview-41101a/)
*   [Configure the Callbacks](sveltekit/actions-6ch24x/)
*   [Serve assets from your own servers](sveltekit/serve-assets-b0827c/)
*   [Create and use a license key](sveltekit/licensing-8aa063/)
*   [Configure callbacks](sveltekit/actions-6ch24x/)
*   [
    
    Customize interface labels and translations
    
    ](sveltekit/user-interface/localization-508e20/)
*   [Edit colors and appearance with themes](sveltekit/user-interface/appearance/theming-4b0938/)

---



[Source](https:/img.ly/docs/cesdk/sveltekit/get-started/mcp-server-fde71c)