# Source: https://developers.lottiefiles.com/dotlottiejs-llms.txt

# using dotLottie JS

> `@dotlottie/dotlottie-js` is a JavaScript library for programmatically creating, reading, and manipulating `.lottie` files. It runs in both browser and Node.js environments and is built around the dotLottie V2 specification, which supports advanced features like theming and state machines.

## Installation

```bash
npm install @dotlottie/dotlottie-js
```

## Core Concepts

### The `DotLottie` Instance
The `DotLottie` class is the main interface. You can create a new instance or load an existing `.lottie` file.

**Creating a New Instance**
```javascript
import { DotLottie } from "@dotlottie/dotlottie-js";

const dotlottie = new DotLottie({
  enableDuplicateImageOptimization: true,
});
```

**Loading an Existing File**
Loading automatically converts V1 files to the V2 structure internally.
```javascript
// From a URL (Browser)
const dotlottie = await new DotLottie().fromURL('https://example.com/animation.lottie');

// From an ArrayBuffer (Browser/Node.js)
const arrayBuffer = await file.arrayBuffer();
const dotlottie = await new DotLottie().fromArrayBuffer(arrayBuffer);
```

### The `build()` Method
Before exporting, you must call the asynchronous `build()` method. This finalizes the archive by fetching remote assets, bundling images/audio, and generating the manifest.
```javascript
await dotlottie.build();
```

### Exporting
After building, you can export the `.lottie` file in various formats.
```javascript
// Download in browser
await dotlottie.download("animation.lottie");

// Get as ArrayBuffer
const buffer = await dotLottie.toArrayBuffer();

// Get as Blob (Browser)
const blob = await dotlottie.toBlob();

// Get as Base64 string
const base64 = await dotlottie.toBase64();
```

### Managing Content

**Animations**
Add one or more Lottie JSON animations to the archive. Any image or audio assets defined in the Lottie JSON's `assets` array will be processed and bundled during the `build()` step.
```javascript
dotlottie.addAnimation({
  id: 'anim1',
  data: lottieJsonData, // The Lottie JSON object
  // or url: 'http://example.com/anim.json'
  loop: true,
  speed: 0.5,
});

dotlottie.removeAnimation('anim1');
const anim = dotlottie.getAnimation('anim1');
```

**Assets (Images & Audio)**
Assets are managed implicitly. When you add an animation, `dotlottie-js` scans its `assets` array during the `build()` process, extracts any embedded Base64 data, and bundles everything correctly. You can retrieve bundled assets after loading or building.
```javascript
const allImages = dotlottie.getImages();
for (const image of allImages) {
  console.log(`Image ID: ${image.id}, FileName: ${image.fileName}`);
  // const imageBuffer = await image.toArrayBuffer();
}

const allAudio = dotlottie.getAudio();
```

**Themes**
Package multiple visual styles (e.g., color palettes) within a single `.lottie` file. The player is responsible for applying the theme at runtime.
```javascript
const themeDarkData = { values: { brandColor: "#FFFFFF" } };

dotlottie.addTheme({
  id: 'dark_mode',
  data: themeDarkData,
});

// Set a default theme for an animation
dotlottie.addAnimation({
  id: 'my_animation',
  data: animationData,
  initialTheme: 'dark_mode',
});
```

**State Machines**
Bundle interaction logic to create interactive animations. `dotlottie-js` packages the state machine JSON; the player executes the logic.
```javascript
const stateMachineData = {
  descriptor: { id: "button_interaction", initial: "idle" },
  states: {
    idle: {
      animationId: "anim_idle",
      on: [{ event: "onMouseEnter", transitionTo: "hover" }],
    },
    hover: { /* ... */ },
  },
};

dotlottie.addStateMachine({
  id: 'sm_button',
  data: stateMachineData,
});
```

**Merging Instances**
Combine multiple `DotLottie` instances into a new instance. This will throw an error if there are duplicate IDs for animations, themes, or state machines.
```javascript
const dl1 = new DotLottie(); // with content
const dl2 = new DotLottie(); // with different content

const merged = dl1.merge(dl2);
await merged.build();
```

## API Reference

### `DotLottie` Class
*   `new DotLottie(options?)`: Creates an empty instance.
*   `async fromArrayBuffer(buffer)`: Loads data from an `ArrayBuffer`.
*   `async fromURL(url)`: Fetches and loads data from a URL.
*   `addAnimation(options)`: Adds a Lottie animation.
*   `removeAnimation(id)`: Removes an animation.
*   `getAnimation(id)`: Retrieves an animation's manifest entry.
*   `getImages()`: Returns an array of all discovered image assets.
*   `getAudio()`: Returns an array of all discovered audio assets.
*   `addTheme(options)`: Adds a theme definition.
*   `removeTheme(id)`: Removes a theme.
*   `getTheme(id)`: Retrieves a theme.
*   `addStateMachine(options)`: Adds a state machine definition.
*   `removeStateMachine(id)`: Removes a state machine.
*   `getStateMachine(id)`: Retrieves a state machine.
*   `merge(...instances)`: Merges multiple `DotLottie` instances into a new one.
*   `async build()`: **(Required before export)** Finalizes the `.lottie` archive.
*   `async toArrayBuffer()`: Exports as an `ArrayBuffer`.
*   `async toBlob()`: Exports as a `Blob` (browser only).
*   `async toBase64()`: Exports as a Base64 string.
*   `async download(fileName)`: Triggers a browser download.

### `DotLottieV1` Class
For legacy use cases that specifically require creating the older V1 `.lottie` format. It has a more limited API, lacking support for themes and state machines.
