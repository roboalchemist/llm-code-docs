# Lottie Documentation

Source: https://developers.lottiefiles.com/llms-full.txt

---

=== llms.txt ===

# LottieFiles Developer Portal

> The developer portal documents how to use our libraries and tools to create, manupilate and play Lottie animations, in both the lottie .json format and our more capable .lottie format.

## The Lottie Format

Lottie is a .json based animation format. It is a simple and efficient way to represent animations in a way that is easy to read and understand.

Lottie .json can be rendered using our dotLottie players.  
Lottie .json can be manipulated using our reLottie library.

Use the following links to understand the Lottie format better:
* [Lottie Documentation](https://lottiefiles.github.io/lottie-docs/): Lottie documentation
* [Lottie Animation Community Specification](https://lottie.github.io/lottie-spec/latest/): Lottie specification from Lottie Animation Community. This spec is a minimzed subset of the full capabilities of Lottie.
* [Lottie JSON Schema](https://lottiefiles.github.io/lottie-docs/schema/): Full JSON Schema definition for the format

## dotLottie Format

dotLottie is an open-source file format that aggregates one or more Lottie files and their associated resources into a single file with theming and interactivity capabilities. They are ZIP archives compressed with the Deflate compression method and carry the file extension of ".lottie".  

dotLottie offers the following benefits over the .json format:

**Multi-animations**:
dotLottie files can contain multiple animations within a single file. These animations are decompressed when selected through the dotLottie player to conserve CPU resources.

**Theming**:
Bundle various themes within your .lottie file, allowing for easy customization of your animations. Define different themes as a Lottie slots object to override animation properties on the fly, including colors, stroke widths, gradients, and any Lottie animated property, all while ensuring that the animations remain lightweight and high-performing.

**Interactivity**:
Enable interactivity by incorporating your own state machine definitions within your .lottie file. State machines enable you to create a wide range of interactive scenarios for your animations. When bundled within a multi-animation .lottie, you can switch between animations based on user interactions and events.

Use the following links to understand the dotLottie format better:
* [dotLottie v1 Documentation](https://dotlottie.io/spec/1.0/): dotLottie v1 documentation
* [dotLottie v2 Documentation](https://dotlottie.io/spec/2.0/): **RECOMMENDED**: dotLottie v2 documentation, including information on theming and state machines

## dotLottie Players

dotLottie players are libraries that allow you to render dotLottie animations on various platforms and frameworks. They are open-source and available for download and integration into your projects.

* [dotLottie Web Players](https://developers.lottiefiles.com/dotlottie-players-web-llms.txt): how to use the dotLottie players to render dotLottie animations in web browsers and JavaScript frameworks
* [dotLottie Mobile Players](https://developers.lottiefiles.com/dotlottie-players-mobile-llms.txt): how to use the dotLottie players to render dotLottie animations on iOS, Android, and React Native

## dotLottie-JS

dotLottie-JS is a JavaScript library that allows you to create and manipulate. It can be used to create and update themes and state machines within dotLottie files.

* [dotLottie-JS](https://developers.lottiefiles.com/dotlottiejs-llms.txt): how to use the dotLottie-JS library to create and manipulate dotLottie files, add themes and state machines


## reLottie

reLottie is a JavaScript library that allows you to read and manipulate .lottie files.

* [reLottie](https://developers.lottiefiles.com/relottie-llms.txt): how to use the reLottie library to read and manipulate Lottie .json files



=== dotlottie-players-mobile-llms.txt ===

# dotLottie Mobile Players

> dotLottie Mobile Players are a family of animation players designed to render both Lottie JSON (`.json`) and dotLottie (`.lottie`) animations on mobile platforms. Built on a high-performance, cross-platform rendering core, these players provide consistent animation playback across iOS, Android, and React Native applications.

**Core Features**
*   **Universal Format Support**: Native support for both `.lottie` and traditional Lottie `.json` files.
*   **Playback Control**: Includes play, pause, stop, speed control, looping, frame-by-frame navigation, and multiple playback modes (forward, reverse, bounce).
*   **Layout & Rendering**: Flexible layout options with fit modes (contain, cover, fill, etc.), alignment, and background color support.
*   **Multi-Animation Support**: Load and switch between multiple animations contained within a single `.lottie` file.
*   **Theming**: Runtime theme switching for dynamic color and style updates.
*   **State Machines**: Built-in support for interactive animations driven by states and events.
*   **Performance Optimization**: Optimized for mobile hardware with efficient memory management and battery-conscious rendering.

## Best Practices & Troubleshooting

**Resource Management**
*   **Native Mobile Players (iOS/Android)**: Avoid strong reference cycles. Remove listeners in appropriate lifecycle methods (e.g., `onDisappear`, `onDestroyView`).
*   **React Native**: The component automatically handles cleanup when unmounted, but ensure proper ref management for manual control.

**Performance Optimization**
*   **Frame Interpolation**: Consider disabling frame interpolation on lower-end devices to improve performance.
*   **Memory Management**: On mobile devices, be mindful of memory usage, especially with large or complex animations.
*   **Battery Optimization**: Pause animations when the app goes to background to conserve battery life.

**Troubleshooting Common Issues**
*   **Animation Not Loading**:
    1.  Verify file paths and ensure animations are properly bundled with your app.
    2.  Check that `.lottie` files are properly configured in your build system (e.g., `metro.config.js` for React Native).
    3.  Use error handlers to catch and log loading failures.
*   **Animation Not Playing**:
    1.  Ensure playback methods are called after the animation has loaded.
    2.  Check that autoplay properties are correctly set.
    3.  Verify that the animation view is properly sized and visible.

## React Native Player (`@lottiefiles/dotlottie-react-native`)

### Installation
```bash
npm install @lottiefiles/dotlottie-react-native
# then for iOS
cd ios && pod install
```
Configure `metro.config.js` to recognize `.lottie` files.

### Usage
```jsx
import React, { useRef } from 'react';
import { View, Button } from 'react-native';
import { DotLottie, type Dotlottie } from '@lottiefiles/dotlottie-react-native';

const ControlledAnimation = () => {
  const ref = useRef<Dotlottie>(null);
  return (
    <View>
      <DotLottie
        ref={ref}
        source={require('./animation.lottie')}
        style={{ width: 200, height: 200 }}
      />
      <Button title="Pause" onPress={() => ref.current?.pause()} />
    </View>
  );
};
```
**API**: `source`, `autoplay`, `loop`, `style` props. Event handlers `onLoad`, `onError`, `onPlay`, etc. Methods on ref: `play()`, `pause()`, `stop()`, `setSpeed()`.

## iOS Player (Native Swift)

### Installation
Use Swift Package Manager with the URL: [https://github.com/LottieFiles/dotlottie-ios](https://github.com/LottieFiles/dotlottie-ios)

### Usage (SwiftUI)
```swift
import SwiftUI
import DotLottie

struct AnimationView: View {
    @StateObject var animation = DotLottieAnimation(
        fileName: "animation",
        config: AnimationConfig(autoplay: true, loop: true)
    )

    var body: some View {
        VStack {
            animation.view()
                .frame(width: 300, height: 300)
            Button("Pause") { animation.pause() }
        }
    }
}
```

### Usage (UIKit)
```swift
import UIKit
import DotLottie

class AnimationViewController: UIViewController {
    var dotLottieAnimation: DotLottieAnimation?

    override func viewDidLoad() {
        super.viewDidLoad()
        let config = AnimationConfig(autoplay: true, loop: true)
        dotLottieAnimation = DotLottieAnimation(fileName: "animation", config: config)

        if let animation = dotLottieAnimation {
            let animationView = animation.createDotLottieView()
            animationView.frame = CGRect(x: 50, y: 100, width: 300, height: 300)
            view.addSubview(animationView)
        }
    }
}
```
**API**: Use `AnimationConfig` to set `autoplay`, `loop`, `speed`, `mode`, `marker`, `layout`, `themeId`, etc. The `DotLottieAnimation` instance provides methods like `play()`, `pause()`, `stop()`, `setFrame()`, `loadStateMachine()`, and `postEvent()`.

## Android Player (Native Kotlin)

### Installation
Add the JitPack repository and the dependency to your Gradle files.
```groovy
// settings.gradle.kts
// ...
maven { url 'https://jitpack.io' }
// ...

// build.gradle.kts (app)
implementation 'com.github.LottieFiles:dotlottie-android:0.4.1'
```

### Usage (Jetpack Compose)
```kotlin
import androidx.compose.runtime.Composable
import com.lottiefiles.dotlottie.core.compose.ui.DotLottieAnimation
import com.lottiefiles.dotlottie.core.util.DotLottieSource

@Composable
fun BasicAnimation() {
    DotLottieAnimation(
        source = DotLottieSource.Url("https://lottie.host/animation.lottie"),
        autoplay = true,
        loop = true,
    )
}
```

### Usage (XML)
```xml
<com.lottiefiles.dotlottie.core.widget.DotLottieAnimation
    android:id="@+id/lottie_view"
    android:layout_width="200dp"
    android:layout_height="200dp"
    app:src="swinging.json"
    app:autoplay="true"
    app:loop="true" />
```
**API**: The Composable takes parameters like `source`, `autoplay`, `loop`, `speed`, and `controller`. The `DotLottieController` provides fine-grained control for playback, theming, and state machines.


=== dotlottie-players-web-llms.txt ===

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


=== dotlottiejs-llms.txt ===

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



=== relottie-llms.txt ===

# using reLottie

> `relottie` is an ecosystem for processing Lottie JSON files using plugins. It is built on `unified`, an engine for processing content with Abstract Syntax Trees (ASTs). `relottie` parses Lottie JSON into a **LAST (Lottie Abstract Syntax Tree)**, allowing for structured inspection and modification.

## Core Concepts

*   **LAST (Lottie Abstract Syntax Tree)**: A `unist`-compliant specification for representing Lottie JSON. Nodes have a `type` and a semantic `title` (e.g., `'layer-image'`, `'transform-opacity'`) that provides Lottie-specific meaning. The root node also has a `hasExpressions` flag for security awareness.
*   **Processor Pipeline**: `relottie` uses a `parse` -> `transform` -> `stringify` pipeline.
    1.  **Parse**: Input Lottie JSON string is parsed into a LAST tree (`@lottiefiles/relottie-parse`).
    2.  **Transform**: One or more transformer plugins run sequentially, inspecting or modifying the tree.
    3.  **Stringify**: The final LAST tree is converted back into a Lottie JSON string (`@lottiefiles/relottie-stringify`).
*   **VFile**: A virtual file representation that carries content and metadata (`vfile.data`) through the pipeline. Plugins attach their results (e.g., extracted metadata) to `vfile.data`.
*   **Tree Traversal**: Use `unist-util-visit` to navigate the LAST tree within a plugin to find and act upon specific nodes.

## Quick Start

1.  **Installation**:
    ```bash
    npm install @lottiefiles/relottie @lottiefiles/last unist-util-visit
    npm install unified vfile -D
    ```

2.  **Example Usage**:
    Create a processor, add a plugin, and process a Lottie JSON string.

    ```typescript
    import { relottie } from "@lottiefiles/relottie";
    import type { Plugin, Transformer } from "unified";
    import type { Root, Attribute, Primitive } from "@lottiefiles/last";
    import { TITLES } from "@lottiefiles/last";
    import { visit, EXIT } from "unist-util-visit";

    // A simple plugin to change the framerate
    const changeFrameratePlugin: Plugin<[{ fr: number }], Root> = (options) => {
      const transformer: Transformer<Root> = (tree) => {
        visit(tree, "attribute", (node: Attribute) => {
          if (node.title === TITLES.number.framerate) {
            (node.children[0] as Primitive).value = options!.fr;
            return EXIT;
          }
        });
      };
      return transformer;
    };

    const lottieJson = '{"v":"5.5.7","fr":30,"w":512,"h":512,"layers":[]}';

    const file = await relottie()
      .use(changeFrameratePlugin, { fr: 60 })
      .process(lottieJson);

    console.log(String(file));
    // Output: {"v":"5.5.7","fr":60,"w":512,"h":512,"layers":[]}
    ```

## Guides

### Analyzing Lottie Files
Use plugins to extract information without modifying the Lottie.

*   **`@lottiefiles/relottie-metadata`**: Extracts common properties like dimensions, framerate, duration, and colors used. The results are attached to `vfile.data.metadata`.
*   **`@lottiefiles/relottie-extract-features`**: Determines which Lottie features are used in the animation (e.g., `'layer-image'`, `'shape-rect'`). The results are a `Map` attached to `vfile.data['extract-features']`.

```typescript
import { relottie } from "@lottiefiles/relottie";
import relottieMetadata from "@lottiefiles/relottie-metadata";
import relottieExtractFeatures from "@lottiefiles/relottie-extract-features";

const file = await relottie()
  .use(relottieMetadata)
  .use(relottieExtractFeatures)
  .process(lottieJson);

// Access extracted data
console.log(file.data.metadata);
console.log(file.data['extract-features']);
```

### Modifying Lottie Files
Create custom transformer plugins to programmatically edit the LAST tree. Common patterns include:
*   **Changing Primitive Values**: Find a node (e.g., an `Attribute`) and update the `.value` of its child `Primitive` node.
*   **Adding Nodes**: Create new LAST nodes using `@lottiefiles/last-builder` and insert them into the `children` array of a parent.
*   **Removing Nodes**: Find a node and use its `parent` and `index` (provided by `unist-util-visit`) to `splice` it from the parent's `children` array.

### Using the CLI (`@lottiefiles/relottie-cli`)
Process Lottie files from the terminal. Useful for batch operations.

```bash
# Install
npm install -g @lottiefiles/relottie-cli

# Usage: process a file and output to stdout
relottie input.json

# Use a plugin and write to a new file
relottie input.json --use ./my-plugin.js -o output.json

# Output the LAST tree instead of Lottie JSON
relottie input.json --tree-out
```
Configuration can be managed via `.relottierc.js` or a `relottieConfig` key in `package.json`.

### Creating Plugins
A plugin is a function that returns a `transformer` function. The transformer receives the LAST `tree` and the `VFile`.

```typescript
import type { Plugin, Transformer } from "unified";
import type { Root } from "@lottiefiles/last";

const myPlugin: Plugin<[options?], Root> = (options = {}) => {
  const transformer: Transformer<Root> = (tree, file) => {
    // Traverse and modify the tree here
    // Attach results to file.data
  };
  return transformer;
};
```

## API Reference

### Core Plugins
*   **`@lottiefiles/relottie-parse`**: Parses Lottie JSON string into a LAST tree. It is built on the `momoa` JSON parser.
*   **`@lottiefiles/relottie-stringify`**: Serializes a LAST tree back into a Lottie JSON string. Can be configured with a `space` option for pretty-printing.

### Utility Plugins
*   **`@lottiefiles/relottie-metadata`**: Extracts metadata (dimensions, framerate, etc.).
*   **`@lottiefiles/relottie-extract-features`**: Analyzes and reports which Lottie features are used.

### LAST Builder (`@lottiefiles/last-builder`)
Provides helper functions (`rt`, `at`, `el`, `pt`, etc.) to programmatically construct LAST nodes, which is useful for generating Lottie files from scratch or for creating nodes within a transformer plugin.

### Security Considerations
`relottie` itself does not execute JavaScript expressions found in Lottie files. However, it's a security risk if those expressions are rendered by a player that executes them. The `Root` node of the LAST tree contains a `hasExpressions: boolean` flag to help identify animations that contain expressions so they can be handled with care.