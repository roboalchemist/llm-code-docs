# Source: https://developers.lottiefiles.com/dotlottie-players-web-llms.txt

# dotLottie Web Players

> dotLottie Web Players are a family of animation players designed to render both Lottie JSON (`.json`) and dotLottie (`.lottie`) animations in web environments. Built on a high-performance, cross-platform rendering core, these players provide consistent animation playback across browsers and JavaScript frameworks.

**Core Features**
*   **Universal Format Support**: Native support for both `.lottie` and traditional Lottie `.json` files.
*   **Playback Control**: Includes play, pause, stop, speed control, looping, frame-by-frame navigation, and multiple playback modes (forward, reverse, bounce).
*   **Layout & Rendering**: Flexible layout options with fit modes (contain, cover, fill, etc.), alignment, and background color support.
*   **Multi-Animation Support**: Load and switch between multiple animations contained within a single `.lottie` file.
*   **Theming**: Runtime theme switching for dynamic color and style updates.
*   **State Machines**: Built-in support for interactive animations driven by states and events.
*   **Performance Optimization**: Features include Web Worker support, frame interpolation control, and configurable render settings.

## Best Practices & Troubleshooting

**Resource Management**
*   **Core Web Player**: Always call the `destroy()` method on a `DotLottie` instance when it's no longer needed to release resources (Canvas context, event listeners, animation loops) and prevent memory leaks.
*   **Framework Wrappers (React, Vue, Svelte)**: These components are designed to automatically call `destroy()` when the component unmounts. For manual cleanup logic, use the appropriate lifecycle hooks: `useEffect` return function in React, `onUnmounted` in Vue, and `onDestroy` in Svelte.

**Performance Optimization**
*   **Frame Interpolation (`useFrameInterpolation`)**: Set to `false` to render only original frames, which can boost performance on complex animations at the cost of some smoothness.
*   **Offscreen Freezing (`renderConfig.freezeOnOffscreen`)**: Enabled by default, this pauses rendering when the canvas is not visible.
*   **Web Workers**: Use `DotLottieWorker` to offload animation processing from the main thread, keeping the UI responsive.
*   **Lazy Loading**: Load animations only when they are needed (e.g., when they scroll into view) to improve initial page performance.

**Troubleshooting Common Issues**
*   **Animation Not Loading**:
    1.  Check the `src` path/URL for typos and case sensitivity.
    2.  Use browser developer tools to check for network errors (like 404s) or Cross-Origin Resource Sharing (CORS) issues.
    3.  Add an event listener for `loadError` to catch and log specific loading errors from the player.
*   **Animation Not Playing**:
    1.  Ensure you are calling playback methods like `play()` only **after** the `load` event has fired.
    2.  If using `autoplay`, ensure the property is set correctly.
    3.  Check for console errors that might prevent playback logic from executing.
    4.  If an animation plays once but doesn't repeat, ensure the `loop` property is `true`.

## Web Player (Core)

The `@lottiefiles/dotlottie-web` package is the core JavaScript library for rendering Lottie animations on the web.

### Installation

**Using npm/yarn:**
```bash
# npm
npm install @lottiefiles/dotlottie-web

# yarn
yarn add @lottiefiles/dotlottie-web
```
Import into your project:
```javascript
import { DotLottie } from "@lottiefiles/dotlottie-web";
```

**Using CDN:**
For direct use in HTML, include the script via CDN.
```html
<script type="module">
  import { DotLottie } from "https://cdn.jsdelivr.net/npm/@lottiefiles/dotlottie-web/+esm";
</script>
```

### Basic Usage

1.  **Add a Canvas to your HTML:**
    ```html
    <canvas id="dotlottie-canvas" style="width: 300px; height: 300px;"></canvas>
    ```

2.  **Instantiate the Player in your script:**
    ```javascript
    const canvasElement = document.getElementById("dotlottie-canvas");

    const dotLottie = new DotLottie({
      autoplay: true,
      loop: true,
      canvas: canvasElement,
      src: "https://lottie.host/4db68bbd-31f6-4cd8-84eb-189de081159a/IGmMCqhzpt.lottie",
    });
    ```

### Animation Loading

The player supports loading animations from a URL (`src`) or directly from data (`data`).

*   **From URL**:
    ```javascript
    const dotLottie = new DotLottie({
      canvas: document.querySelector("#canvas"),
      src: "https://lottie.host/animation.lottie", // .lottie or .json
    });
    ```
*   **From JSON Data**:
    ```javascript
    const dotLottie = new DotLottie({
      canvas: document.querySelector("#canvas"),
      data: '{"v":"4.8.0","meta":{...}}',
    });
    ```
*   **Dynamic Loading**:
    Load a new animation after initialization.
    ```javascript
    dotLottie.load({
      src: "https://lottie.host/new-animation.lottie",
      loop: true,
      autoplay: true,
    });
    ```

*   **Multi-Animation Files**:
    Access and switch between animations within a single `.lottie` file.
    ```javascript
    const dotLottie = new DotLottie({
      canvas: document.querySelector("#canvas"),
      src: "multi-animation.lottie",
    });

    dotLottie.addEventListener("load", () => {
      const animations = dotLottie.manifest.animations;
      // Load a specific animation by its ID
      dotLottie.loadAnimation(animations[0].id);
    });
    ```

*   **Error Handling**:
    ```javascript
    dotLottie.addEventListener("loadError", (error) => {
      console.error("Failed to load animation:", error);
    });
    ```

### Playback Control

*   **Methods**: `play()`, `pause()`, `stop()`, `setSpeed(2)`, `setLoop(true)`, `setMode('bounce')`, `setFrame(42)`, `setSegment(10, 50)`.
*   **State Properties**: `isPlaying`, `isPaused`, `isStopped`.
*   **Events**: Listen to events like `play`, `pause`, `stop`, `complete`, `loop`, and `frame`.
    ```javascript
    dotLottie.addEventListener("play", () => console.log("Animation started"));
    dotLottie.addEventListener("frame", (frameEvent) => console.log("Current frame:", frameEvent.detail.currentFrame));
    ```

### Layout & Styling

Control how animations are rendered within the canvas using the `layout` configuration object.

*   **Fit Modes**: `contain` (default), `cover`, `fill`, `fit-width`, `fit-height`, `none`.
*   **Alignment**: An array `[x, y]` where `[0, 0]` is top-left and `[0.5, 0.5]` is center.

```javascript
const dotLottie = new DotLottie({
  canvas: document.querySelector("#canvas"),
  src: "animation.lottie",
  layout: {
    fit: "cover",
    align: [0.5, 1], // Center horizontally, align to bottom
  },
  backgroundColor: "#000000",
});
```

### Theming

Dynamically change animation colors and styles at runtime.

*   **Load theme on init**:
    ```javascript
    const dotLottie = new DotLottie({
      canvas: document.querySelector("#canvas"),
      src: "themed-animation.lottie",
      themeId: "dark-mode",
    });
    ```
*   **Switch theme dynamically**:
    ```javascript
    dotLottie.setTheme("light-mode");
    dotLottie.resetTheme();
    ```

### State Machines (Interactivity)

Define complex, event-driven animation behaviors.

1.  **Load and start the state machine** after the animation loads:
    ```javascript
    dotLottie.addEventListener("load", () => {
      const success = dotLottie.loadStateMachine("my-fsm-id");
      if (success) {
        dotLottie.startStateMachine();
      }
    });
    ```
2.  **Post events** to trigger transitions:
    ```javascript
    // In response to a user action
    dotLottie.postEvent("String: click");
    ```
3.  **Listen to state changes** for debugging or UI updates:
    ```javascript
    dotLottie.addEventListener("stateEntered", (event) => console.log("Entered state:", event.detail));
    dotLottie.addEventListener("transition", (event) => console.log("Transition:", event.detail.previousState, "->", event.detail.newState));
    ```

### Advanced Features: Web Worker

Offload rendering to a dedicated thread to free up the main thread and improve performance, especially when running multiple animations. The API is nearly identical but methods return a `Promise`.

```javascript
import { DotLottieWorker } from "@lottiefiles/dotlottie-web";

const animation = new DotLottieWorker({
  canvas: document.getElementById("canvas"),
  src: "animation.json",
  autoplay: true,
  workerId: "worker-1", // Optional: group animations into specific workers
});

await animation.play(); // Methods are async
const isPlaying = await animation.isPlaying; // Properties are async
```

### API Reference

The constructor accepts a configuration object with properties like `autoplay`, `loop`, `canvas`, `src`, `speed`, `data`, `mode`, `backgroundColor`, `segment`, `renderConfig`, `themeId`, and `layout`. For a full list of methods, properties, and events, refer to the official documentation.

## Framework Players

### React Player (`@lottiefiles/dotlottie-react`)

**Installation**
```bash
npm install @lottiefiles/dotlottie-react
```

**Usage**
```jsx
import React, { useRef } from 'react';
import { DotLottieReact } from '@lottiefiles/dotlottie-react';
import type { DotLottie } from '@lottiefiles/dotlottie-web';

function MyAnimation() {
  const dotLottieRef = useRef<DotLottie | null>(null);

  const dotLottieRefCallback = (instance: DotLottie | null) => {
    dotLottieRef.current = instance;
  };

  const handlePause = () => dotLottieRef.current?.pause();

  return (
    <div>
      <DotLottieReact
        src="https://lottie.host/animation.lottie"
        loop
        autoplay
        dotLottieRefCallback={dotLottieRefCallback}
      />
      <button onClick={handlePause}>Pause</button>
    </div>
  );
}
```
**Props**: 
`src` (required), `data`, `autoplay`, `loop`, `speed`, `mode`, `playOnHover`, `segment`, `backgroundColor`, `themeId`, `useFrameInterpolation`, `renderConfig`, and `dotLottieRefCallback`. Event handlers like `onPlay`, `onPause`, `onComplete`, `onLoad` are also available.

### Vue Player (`@lottiefiles/dotlottie-vue`)

**Installation**
```bash
npm install @lottiefiles/dotlottie-vue
```

**Usage**
```vue
<template>
  <div>
    <DotLottieVue
      ref="dotLottieVueRef"
      src="https://lottie.host/animation.lottie"
      :autoplay="true"
      :loop="true"
    />
    <button @click="handlePause">Pause</button>
  </div>
</template>

<script setup>
import { DotLottieVue } from '@lottiefiles/dotlottie-vue';
import { ref } from 'vue';

const dotLottieVueRef = ref(null);
const handlePause = () => dotLottieVueRef.value?.pause();
</script>
```
**Props**: `src` (required), `data`, `autoplay`, `loop`, `speed`, `mode`, `segment`, `backgroundColor`, `themeId`, `useFrameInterpolation`, `renderConfig`. The component instance exposes methods like `play()`, `pause()`, and `stop()`. Event handling is done by accessing the core instance via `getDotLottieInstance()`.

### Svelte Player (`@lottiefiles/dotlottie-svelte`)

**Installation**
```bash
npm install @lottiefiles/dotlottie-svelte
```

**Usage**
```svelte
<script lang="ts">
  import { DotLottieSvelte } from '@lottiefiles/dotlottie-svelte';
  import type { DotLottie } from '@lottiefiles/dotlottie-svelte';

  let dotLottie: DotLottie | null = null;
</script>

<DotLottieSvelte
  src="animation.lottie"
  autoplay
  loop
  dotLottieRefCallback={(ref) => dotLottie = ref}
/>

<button on:click={() => dotLottie?.pause()}>Pause</button>
```
**Props**: `src` (required), `data`, `autoplay`, `loop`, `speed`, `mode`, `segment`, `backgroundColor`, `themeId`, `renderConfig`, `useFrameInterpolation`, and `dotLottieRefCallback`.

### Web Component (`@lottiefiles/dotlottie-web`)

**Setup**
Import the component definition.
```javascript
// In your main JS file
import "@lottiefiles/dotlottie-web";```
Or use the CDN:
```html
<script type="module" src="https://cdn.jsdelivr.net/npm/@lottiefiles/dotlottie-web@latest/dist/dotlottie-web.js"></script>
```

**Usage**
```html
<dotlottie-player
  id="player"
  src="https://lottie.host/animation.lottie"
  autoplay
  loop
  speed="1.5"
  style="width: 300px; height: 300px;"
></dotlottie-player>

<script>
  const playerElement = document.getElementById('player');
  playerElement.addEventListener('load', () => {
    // Access the core instance for programmatic control
    const coreInstance = playerElement.dotLottie;
    coreInstance.pause();
  });
</script>
```
**Attributes**: `src`, `autoplay`, `loop`, `speed`, `mode`, `segment`, `backgroundColor`, `themeId`. JavaScript properties include `renderConfig` and read-only access to the `dotLottie` core instance.