# Vue.js Project Without UI

This guide walks you through embedding the **CreativeEditor SDK (CE.SDK) Engine**—without the default UI—into a **Vue** app. Use this setup to:

*   Automate creative tasks entirely in client-side code.
*   Build a fully customized editing interface.

## What’s CreativeEditor SDK?[#](#whats-creativeeditor-sdk)

CreativeEditor SDK (CE.SDK) lets you integrate a customizable image and video editor into your web app. It includes filters, text overlays, and other media editing tools, and adapts easily to your use case.

CreativeEditor SDK is a commercial product. To use it, you need a valid license key. If you don’t have one yet, you can get a free trial or purchase a license.

[Free Trial](https://img.ly/forms/free-trial)[

Purchase License

](https://img.ly/pricing)

## Who Is This Guide For?[#](#who-is-this-guide-for)

This guide is for developers who:

*   Want to design a **custom editor UI**.
*   Need to run CE.SDK in **browser automation workflows** with no visual editor.
*   Have completed a **Get Started** guide with CE.SDK in Vue.
*   Are ready for more **advanced use cases**.

## What You’ll Achieve[#](#what-youll-achieve)

*   Launch the CE.SDK headless engine in a Vue component.
*   Script scene edits.
*   Add a custom button that reduces an image’s opacity by 20% each time it’s clicked.
*   (Optional) Render the CE.SDK canvas while still controlling the editor with your own custom UI.

## Prerequisites[#](#prerequisites)

What you need before starting:

*   A **working Vue project**.
*   A **valid CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)).

## Step 1: Install CE.SDK Engine[#](#step-1-install-cesdk-engine)

To use CE.SDK in headless mode within a Vue project, install the engine package. Use your project’s package manager to run the following command in your project’s root directory:

[

npm

](#tab-panel-115)[

yarn

](#tab-panel-116)[

pnpm

](#tab-panel-117)

Terminal window

```
npm install @cesdk/engine
```

Terminal window

```
yarn add @cesdk/engine
```

Terminal window

```
pnpm add @cesdk/engine
```

## Step 2: Define a Custom Editor Component With Headless UI[#](#step-2-define-a-custom-editor-component-with-headless-ui)

Once you’ve successfully installed the package, create a new Vue component by following these steps:

### Create a New Vue Component[#](#create-a-new-vue-component)

1.  Open your components folder (typically, `src/components/`).
2.  Create **a new file** called `CustomEditor.vue`
3.  Paste the following code into `CustomEditor.vue`:

CustomEditor.vue

```
<script setup>import { ref, onMounted } from 'vue';import CreativeEngine from '@cesdk/engine';
// To store the DOM container where the CreativeEngine canvas will be attachedconst canvasContainer = ref(null);// To store the CreativeEngine instancelet engine;// To store the ID of the image block added to the scenelet imageBlockId = null;
onMounted(async () => {  // Your CE.SDK configurations  const config = {    license: 'YOUR_LICENSE_KEY', // Replace with your CE.SDK license key  };
  // Initialize CreativeEngine in headless mode  engine = await CreativeEngine.init(config);
  // Append CE.SDK canvas to the DOM (optional)  if (canvasContainer.value && engine.element) {    canvasContainer.value.appendChild(engine.element);  }
  // Get the current scene or create a new one  let scene = engine.scene.get();  if (!scene) {    scene = engine.scene.create();    const page = engine.block.create('page');    engine.block.appendChild(scene, page);  }
  // Get the first page block  const [page] = engine.block.findByType('page');
  // Append a block to show an image on the page  const imageBlock = engine.block.create('graphic');  imageBlockId = imageBlock;  engine.block.setShape(imageBlock, engine.block.createShape('rect'));
  // Fill the block with an image from a public source  const imageFill = engine.block.createFill('image');  engine.block.setSourceSet(imageFill, 'fill/image/sourceSet', [    {      uri: 'https://img.ly/static/ubq_samples/sample_1_1024x683.jpg',      width: 1024,      height: 683,    },  ]);  engine.block.setFill(imageBlock, imageFill);  engine.block.appendChild(page, imageBlock);
  // Zoom to fit the page in the editor view  engine.scene.zoomToBlock(page);});
// Callback to change the opacity of the imagefunction changeOpacity() {  if (engine && imageBlockId != null) {    // Get the current opacity value of the image    const currentOpacity = engine.block.getOpacity(imageBlockId);    // Reduce the opacity of the image by 20% at each click    engine.block.setOpacity(imageBlockId, currentOpacity * 0.8);  }}</script>
<template>  <div class="editor-container">    <div class="canvas-container" ref="canvasContainer"></div>    <div class="button-overlay">      <button @click="changeOpacity">Reduce Opacity</button>    </div>  </div></template>
```

Once CreativeEngine is initialized, you can access and [edit a scene with full flexibility](vue/open-the-editor-23a1db/). In the preceding code:

*   We add a sample image to the canvas.
*   We include a button that reduces its opacity.
*   Each click reduces the image’s opacity by 20%.

In particular, the `changeOpacity()` function:

*   Uses the [CE.SDK headless `block` API](vue/concepts/blocks-90241e/).
*   Fetches the current opacity of the image.
*   Updates it dynamically.

Rendering a canvas on browser is completely optional. The engine also works for **automation only—without any UI**.

Automation Flow Example For instance, you could: 1. Adjust image properties (like opacity in memory).

1.  **Directly export** or process the result without rendering it on screen.

### Style the Component[#](#style-the-component)

Customize the appearance of your editor, by pasting the following CSS at the end of your `CustomEditor.vue` file:

CustomEditor.vue

```
// ... Component code above<style>.editor-container {  width: 100vw;  height: 100vh;  position: relative;}
.canvas-container {  width: 100%;  height: 100%;}
.button-overlay {  position: absolute;  top: 20px;  left: 20px;}
.button-overlay button {  border-radius: 8px;  border: 1px solid #ccc;  padding: 0.6em 1.2em;  font-size: 1em;  font-weight: 500;  font-family: inherit;  background-color: #ffffff;  color: #1a1a1a;  cursor: pointer;  transition:    border-color 0.25s,    box-shadow 0.25s;  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);}
.button-overlay button:hover {  border-color: #646cff;  box-shadow: 0 4px 10px rgba(100, 108, 255, 0.2);}
.button-overlay button:focus,.button-overlay button:focus-visible {  outline: 2px solid #646cff;  outline-offset: 2px;}</style>
```

Modify the styles to fit your application’s design.

See the final `CustomEditor.vue` file

CustomEditor.vue

```
<script setup>import { ref, onMounted } from 'vue';import CreativeEngine from '@cesdk/engine';
// To store the DOM container where the CreativeEngine canvas will be attachedconst canvasContainer = ref(null);// To store the CreativeEngine instancelet engine;// To store the ID of the image block added to the scenelet imageBlockId = null;
onMounted(async () => {  // Your CE.SDK configurations  const config = {    license: 'YOUR_LICENSE_KEY', // Replace with your CE.SDK license key  };
  // Initialize CreativeEngine in headless mode  engine = await CreativeEngine.init(config);
  // Append CE.SDK canvas to the DOM (optional)  if (canvasContainer.value && engine.element) {    canvasContainer.value.appendChild(engine.element);  }
  // Get the current scene or create a new one  let scene = engine.scene.get();  if (!scene) {    scene = engine.scene.create();    const page = engine.block.create('page');    engine.block.appendChild(scene, page);  }
  // Get the first page block  const [page] = engine.block.findByType('page');
  // Append a block to show an image on the page  const imageBlock = engine.block.create('graphic');  imageBlockId = imageBlock;  engine.block.setShape(imageBlock, engine.block.createShape('rect'));
  // Fill the block with an image from a public source  const imageFill = engine.block.createFill('image');  engine.block.setSourceSet(imageFill, 'fill/image/sourceSet', [    {      uri: 'https://img.ly/static/ubq_samples/sample_1_1024x683.jpg',      width: 1024,      height: 683,    },  ]);  engine.block.setFill(imageBlock, imageFill);  engine.block.appendChild(page, imageBlock);
  // Zoom to fit the page in the editor view  engine.scene.zoomToBlock(page);});
// Callback to change the opacity of the imagefunction changeOpacity() {  if (engine && imageBlockId != null) {    // Get the current opacity value of the image    const currentOpacity = engine.block.getOpacity(imageBlockId);    // Reduce the opacity of the image by 20% at each click    engine.block.setOpacity(imageBlockId, currentOpacity * 0.8);  }}</script>
<template>  <div class="editor-container">    <div class="canvas-container" ref="canvasContainer"></div>    <div class="button-overlay">      <button @click="changeOpacity">Reduce Opacity</button>    </div>  </div></template>
<style>.editor-container {  width: 100vw;  height: 100vh;  position: relative;}
.canvas-container {  width: 100%;  height: 100%;}
.button-overlay {  position: absolute;  top: 20px;  left: 20px;}
.button-overlay button {  border-radius: 8px;  border: 1px solid #ccc;  padding: 0.6em 1.2em;  font-size: 1em;  font-weight: 500;  font-family: inherit;  background-color: #ffffff;  color: #1a1a1a;  cursor: pointer;  transition:    border-color 0.25s,    box-shadow 0.25s;  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);}
.button-overlay button:hover {  border-color: #646cff;  box-shadow: 0 4px 10px rgba(100, 108, 255, 0.2);}
.button-overlay button:focus,.button-overlay button:focus-visible {  outline: 2px solid #646cff;  outline-offset: 2px;}</style>
```

## Step 3: Embed the Custom Editor Component[#](#step-3-embed-the-custom-editor-component)

To embed your new custom Creative Editor component:

1.  Choose where you want to render it in your app.
2.  Go to the `<script>` section of the relevant Vue component/page (for example, `App.vue`).
3.  Import `CustomEditor` like this:

```
import CustomEditor from './components/CustomEditor.vue';
```

4.  Add the `CustomEditor` component in the template section of your file:

```
<CustomEditor />
```

## Step 4: Test the Custom Editor[#](#step-4-test-the-custom-editor)

1.  Run your app locally.
2.  Navigate to the page containing `<CustomEditor>`.
3.  Your app should display a sample image displayed on the canvas, along with a “Reduce Opacity” button.
4.  Click the button to see the image’s opacity decrease by 20% on each click.

## Use Cases[#](#use-cases)

Congratulations! You’ve successfully set the stage for:

*   Creating fully customized creative tools using Vue.
*   Automating the creation of graphics and visual assets.
*   Dynamically controlling the CE.SDK engine in browser-based workflows.

## Troubleshooting & Common Errors[#](#troubleshooting--common-errors)

❌ **Error**: `The following dependencies are imported but could not be resolved: @cesdk/engine`

*   Make sure you’ve installed CreativeEngine correctly using `npm install @cesdk/engine` or the yarn/pnpm equivalent.

❌ **Error**: CE.SDK canvas doesn’t render

*   Ensure you’re appending `engine.element` to a valid HTML element. Then, confirm that the DOM reference exists and is available when the engine is initialized.

❌ **Error**: `Missing license key in config`

*   Check that your `config` object includes a `license` property and that it’s set to your CE.SDK license key.

❌ **Error**: `Editor engine could not be loaded: The License Key (API Key) you are using to access CE.SDK is invalid`

*   Verify that your license key is valid, hasn’t expired, and is correctly included in your configuration.

❌ **Issue**: The custom editor component doesn’t behave as expected

*   Inspect the browser console for errors to help pinpoint the issue.

## Next Steps[#](#next-steps)

This guide sets the foundation for creating a custom UI with Vue. Next, learn how to:

*   [Automate design exports](vue/export-save-publish/export/overview-9ed3a8/)
*   [Automate design generation and editing](vue/automation-715209/)

---



[Source](https:/img.ly/docs/cesdk/vue/get-started/new-project-n7678t)