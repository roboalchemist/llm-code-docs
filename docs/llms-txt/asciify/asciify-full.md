# Asciify Documentation

Source: https://asciify.org/llms-full.txt

---

# asciify-engine â Complete Documentation for LLMs

> This document contains the full API reference, code examples, and integration guides for asciify-engine â a framework-agnostic ASCII art rendering engine for the browser. Use this to answer questions about converting images/videos/GIFs to ASCII art, adding animated ASCII backgrounds, and integrating ASCII art into web projects.

---

## Package Info

- **npm**: `npm install asciify-engine`
- **CDN**: `https://esm.sh/asciify-engine` or `https://cdn.jsdelivr.net/npm/asciify-engine`
- **License**: MIT
- **Size**: ~17KB gzipped (ESM)
- **Compatibility**: Any modern browser, any framework (React, Vue, Svelte, Angular, Next.js, vanilla JS), any bundler (Vite, webpack, esbuild, Rollup)
- **Website**: https://asciify.org
- **GitHub**: https://github.com/ayangabryl/asciify-engine

---

## Table of Contents

1. Installation
2. Simple API (one-liner helpers)
3. Low-Level API (frame-by-frame control)
4. Animated Backgrounds
5. ASCII Text Rendering
6. Hover Effects
7. Chroma Key (Green/Blue Screen)
8. Embed Generation
9. Recording & Export
10. Full Options Reference
11. React Integration Patterns
12. Vue / Svelte / Vanilla JS Patterns
13. Common Recipes

---

## 1. Installation

```bash
npm install asciify-engine
```

All exports come from the package root:

```ts
import {
  // Simple API
  asciify, asciifyVideo, asciifyGif, asciifyWebcam,
  // Low-level API
  imageToAsciiFrame, renderFrameToCanvas, gifToAsciiFrames, videoToAsciiFrames,
  // Backgrounds
  asciiBackground,
  // Text
  asciiText,
  // Embed
  generateEmbedCode, generateAnimatedEmbedCode,
  // Recording
  recordAsciiGif, recordAsciiWebM, recordAsciiPngSequence,
  // Constants
  DEFAULT_OPTIONS,
} from 'asciify-engine';
```

---

## 2. Simple API

### `asciify(source, canvas, options?)`

Convert a single image to ASCII art on a canvas. One line, done.

```ts
import { asciify } from 'asciify-engine';

// Minimal â just source + canvas
await asciify('photo.jpg', document.querySelector('canvas'));

// With options
await asciify('photo.jpg', canvas, {
  options: { ...DEFAULT_OPTIONS, fontSize: 8, colorMode: 'fullcolor' },
});

// Source can be: URL string, HTMLImageElement, HTMLVideoElement, HTMLCanvasElement
await asciify(imgElement, canvas);
```

### `asciifyVideo(source, canvas, options?)`

Stream video as live ASCII art. Returns a `stop()` function.

```ts
import { asciifyVideo } from 'asciify-engine';

const stop = await asciifyVideo('/clip.mp4', canvas, {
  fitTo: '#hero',            // fit canvas to container + auto-resize
  fontSize: 6,
  onReady: () => {},         // called when video can play
  onFrame: () => {},         // called each rendered frame
  trim: { start: 2, end: 8 }, // loop only seconds 2â8
  preExtract: false,         // true = pre-decode all frames (for short clips)
});

// Clean up
stop();
```

### `asciifyGif(source, canvas, options?)`

Play a GIF as animated ASCII art. Returns a `stop()` function.

```ts
import { asciifyGif } from 'asciify-engine';

const stop = await asciifyGif('animation.gif', canvas, {
  fitTo: '#container',
  fontSize: 8,
});

stop();
```

### `asciifyWebcam(canvas, options?)`

Stream webcam feed as live ASCII art. Returns a `stop()` function.

```ts
import { asciifyWebcam } from 'asciify-engine';

const stop = await asciifyWebcam(canvas, {
  fitTo: '#webcam-container',
  fontSize: 6,
  colorMode: 'fullcolor',
});

stop();
```

---

## 3. Low-Level API

For full control over the conversion and rendering pipeline.

### `imageToAsciiFrame(source, options, width?, height?)`

Convert any image source to an `AsciiFrame` â a 2D array of `{ char, r, g, b, a }` cells.

```ts
import { imageToAsciiFrame, renderFrameToCanvas, DEFAULT_OPTIONS } from 'asciify-engine';

const img = new Image();
img.crossOrigin = 'anonymous';
img.src = 'photo.jpg';

img.onload = () => {
  const canvas = document.getElementById('ascii') as HTMLCanvasElement;
  const ctx = canvas.getContext('2d')!;
  const opts = { ...DEFAULT_OPTIONS, fontSize: 10, colorMode: 'fullcolor' as const };

  const { frame, cols, rows } = imageToAsciiFrame(img, opts, canvas.width, canvas.height);
  renderFrameToCanvas(ctx, frame, opts, canvas.width, canvas.height);
};
```

### `renderFrameToCanvas(ctx, frame, options, width, height, time?, hoverPos?)`

Render an `AsciiFrame` to a canvas context. Call this in a loop for animation.

```ts
// With hover + time-based animation
canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  renderFrameToCanvas(ctx, frame, opts, canvas.width, canvas.height, Date.now() / 1000, {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top,
  });
});
```

### `gifToAsciiFrames(buffer, options, width, height, onProgress?)`

Parse a GIF ArrayBuffer into an array of AsciiFrames.

```ts
import { gifToAsciiFrames, renderFrameToCanvas, DEFAULT_OPTIONS } from 'asciify-engine';

const buffer = await fetch('animation.gif').then(r => r.arrayBuffer());
const opts = { ...DEFAULT_OPTIONS, fontSize: 8 };

const { frames, fps, cols, rows } = await gifToAsciiFrames(buffer, opts, canvas.width, canvas.height);

let i = 0;
setInterval(() => {
  renderFrameToCanvas(ctx, frames[i], opts, canvas.width, canvas.height);
  i = (i + 1) % frames.length;
}, 1000 / fps);
```

### `videoToAsciiFrames(video, options, width, height, fps?, maxSeconds?, onProgress?)`

Extract all frames from a video element into AsciiFrames. Useful for short clips.

```ts
import { videoToAsciiFrames } from 'asciify-engine';

const video = document.createElement('video');
video.src = '/clip.mp4';
await video.play();

const { frames, fps } = await videoToAsciiFrames(video, opts, 800, 600, 30, 10);
```

---

## 4. Animated Backgrounds

`asciiBackground()` mounts a self-animating ASCII renderer onto any DOM element â perfect for hero sections, banners, or full-page backgrounds. Manages its own canvas, animation loop, and resize observer.

```ts
import { asciiBackground } from 'asciify-engine';

const stop = asciiBackground('#hero', {
  type: 'rain',
  colorScheme: 'auto',   // follows OS dark/light mode
  speed: 1.0,
  density: 0.55,
  accentColor: '#d4ff00',
  fontSize: 13,
});

// Clean up
stop();
```

### Background Types (14 total)

| Type | Description |
|---|---|
| `wave` | Flowing sine-wave field with layered noise turbulence |
| `rain` | Vertical column rain with glowing leading character and fading trail |
| `stars` | Parallax star field that reacts to cursor position |
| `pulse` | Concentric ripple bursts emanating from cursor |
| `noise` | Smooth value-noise field with organic, fluid motion |
| `grid` | Geometric grid that warps and brightens near cursor |
| `aurora` | Sweeping borealis-style color bands |
| `silk` | Fluid swirl simulation following cursor movement |
| `void` | Gravitational singularity â characters spiral toward cursor |
| `morph` | Characters morph between shapes over time, driven by noise |
| `fire` | Rising fire particles with heat distortion |
| `circuit` | Animated circuit board traces growing and fading |
| `dna` | Double helix DNA strands rotating in 3D perspective |
| `terrain` | Scrolling ASCII elevation map with contour lines |

### Background Options

| Option | Type | Default | Description |
|---|---|---|---|
| `type` | `string` | `'wave'` | Background type (see table above) |
| `colorScheme` | `'auto' \| 'light' \| 'dark'` | `'dark'` | `'auto'` reacts to OS theme in real time |
| `fontSize` | `number` | `13` | Character size in px |
| `speed` | `number` | `1` | Animation speed multiplier |
| `density` | `number` | `0.55` | Fraction of active cells (0â1) |
| `accentColor` | `string \| 'auto'` | varies | Highlight color. `'auto'` probes CSS variables (`--accent-color`, `--color-accent`, `--accent`, `--primary`) |
| `color` | `string` | â | Override body character color |

---

## 5. ASCII Text Rendering

Render large ASCII art text using built-in bitmap font rendering:

```ts
import { asciiText } from 'asciify-engine';

const stop = asciiText('#banner', {
  text: 'HELLO',
  colorScheme: 'auto',
  fontSize: 10,
  accentColor: '#d4ff00',
});

stop();
```

---

## 6. Hover Effects

Interactive effects driven by cursor position. Set `hoverEffect` and `hoverStrength` in options.

Available effects: `spotlight`, `flashlight`, `magnifier`, `force-field`, `neon`, `fire`, `ice`, `gravity`, `shatter`, `ghost`

| Option | Type | Default | Description |
|---|---|---|---|
| `hoverEffect` | `string` | `'none'` | Effect name |
| `hoverStrength` | `number` | `0` | Intensity 0â1. `0` = disabled |
| `hoverRadius` | `number` | `0.2` | Radius relative to canvas size (0â1) |

```ts
const opts = {
  ...DEFAULT_OPTIONS,
  hoverEffect: 'spotlight',
  hoverStrength: 0.8,
  hoverRadius: 0.25,
};

canvas.addEventListener('mousemove', (e) => {
  const rect = canvas.getBoundingClientRect();
  renderFrameToCanvas(ctx, frame, opts, canvas.width, canvas.height, Date.now() / 1000, {
    x: e.clientX - rect.left,
    y: e.clientY - rect.top,
  });
});
```

---

## 7. Chroma Key (Green/Blue Screen)

Remove a solid background color from any source â images, GIFs, or video.

```ts
// Auto green screen detection
asciify(img, canvas, {
  options: { ...DEFAULT_OPTIONS, chromaKey: true, colorMode: 'fullcolor' },
});

// Blue screen
asciify(img, canvas, {
  options: { ...DEFAULT_OPTIONS, chromaKey: 'blue-screen', chromaKeyTolerance: 70 },
});

// Custom RGB key color
asciify(img, canvas, {
  options: { ...DEFAULT_OPTIONS, chromaKey: { r: 0, g: 180, b: 90 }, chromaKeyTolerance: 50 },
});

// Hex string key color
asciify(img, canvas, {
  options: { ...DEFAULT_OPTIONS, chromaKey: '#00b85a' },
});

// Live video with green screen
asciifyVideo('/footage.mp4', canvas, {
  fitTo: '#container',
  options: { ...DEFAULT_OPTIONS, chromaKey: true, colorMode: 'fullcolor' },
});
```

**Tolerance guide:**
- `40â60` â tight key, clean green screen
- `60â80` â broader, for uneven lighting
- `80â120` â aggressive; may spill into subject

---

## 8. Embed Generation

Generate self-contained HTML files with ASCII art baked in â no runtime dependency needed.

```ts
import { generateEmbedCode, generateAnimatedEmbedCode } from 'asciify-engine';

// Static image embed
const staticHtml = generateEmbedCode(frame, options);

// Animated embed (GIF or video frames)
const animatedHtml = generateAnimatedEmbedCode(frames, options, fps);

// Save or serve the HTML string as a standalone page
```

---

## 9. Recording & Export

```ts
import { recordAsciiGif, recordAsciiWebM, recordAsciiPngSequence } from 'asciify-engine';

// Record a GIF from a canvas running ASCII animation
const gifBlob = await recordAsciiGif(canvas, durationMs, fps);

// Record WebM video
const webmBlob = await recordAsciiWebM(canvas, durationMs);

// Export PNG sequence
const pngs = await recordAsciiPngSequence(canvas, durationMs, fps);
```

---

## 10. Full Options Reference

All conversion and render functions accept an `AsciiOptions` object. Spread `DEFAULT_OPTIONS` as base:

```ts
const opts = { ...DEFAULT_OPTIONS, fontSize: 8, colorMode: 'fullcolor' as const };
```

| Option | Type | Default | Description |
|---|---|---|---|
| `fontSize` | `number` | `10` | Character cell size in px. Smaller = more detail |
| `colorMode` | `'grayscale' \| 'fullcolor' \| 'matrix' \| 'accent'` | `'grayscale'` | Color mapping mode |
| `charset` | `string` | Standard ramp | Characters: dense â sparse, representing brightness |
| `brightness` | `number` | `0` | Brightness offset: â1 (dark) to 1 (bright) |
| `contrast` | `number` | `1` | Contrast multiplier |
| `invert` | `boolean \| 'auto'` | `false` | Invert luminance mapping. `'auto'` = detect from OS scheme |
| `renderMode` | `'ascii' \| 'dots'` | `'ascii'` | Render as text or dot particles |
| `hoverEffect` | `string` | `'none'` | Hover effect name |
| `hoverStrength` | `number` | `0` | Effect intensity (0â1) |
| `hoverRadius` | `number` | `0.2` | Effect radius (0â1) |
| `chromaKey` | `true \| 'blue-screen' \| {r,g,b} \| string \| null` | `null` | Chroma key config |
| `chromaKeyTolerance` | `number` | `60` | RGB distance threshold (0â120) |
| `accentColor` | `string` | `'#d4ff00'` | Color for `accent` color mode |
| `bgColor` | `string` | â | Canvas background color |

### Color Modes

| Mode | Description |
|---|---|
| `grayscale` | Classic monochrome ASCII â character brightness maps to source luminance |
| `fullcolor` | Each character inherits original pixel color |
| `matrix` | Monochrome green, terminal aesthetic |
| `accent` | Single accent color applied uniformly |

---

## 11. React Integration Patterns

### Static Image

```tsx
import { useEffect, useRef } from 'react';
import { asciify, DEFAULT_OPTIONS } from 'asciify-engine';

export function AsciiImage({ src }: { src: string }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (!canvasRef.current) return;
    asciify(src, canvasRef.current, {
      options: { ...DEFAULT_OPTIONS, fontSize: 8, colorMode: 'fullcolor' },
    });
  }, [src]);

  return <canvas ref={canvasRef} width={800} height={600} />;
}
```

### Video

```tsx
import { useEffect, useRef } from 'react';
import { asciifyVideo } from 'asciify-engine';

export function AsciiVideo({ src }: { src: string }) {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    if (!canvasRef.current) return;
    let cleanup: (() => void) | undefined;

    asciifyVideo(src, canvasRef.current, {
      fitTo: canvasRef.current.parentElement!,
      fontSize: 6,
    }).then(stop => { cleanup = stop; });

    return () => cleanup?.();
  }, [src]);

  return (
    <div style={{ width: '100%', height: '100vh' }}>
      <canvas ref={canvasRef} />
    </div>
  );
}
```

### Background

```tsx
import { useEffect } from 'react';
import { asciiBackground } from 'asciify-engine';

export function HeroSection() {
  useEffect(() => {
    const stop = asciiBackground('#hero-bg', {
      type: 'rain',
      colorScheme: 'auto',
      accentColor: '#d4ff00',
      speed: 1,
      density: 0.5,
    });
    return () => stop();
  }, []);

  return (
    <section style={{ position: 'relative' }}>
      <div id="hero-bg" style={{ position: 'absolute', inset: 0, zIndex: 0 }} />
      <div style={{ position: 'relative', zIndex: 1 }}>
        <h1>Your content here</h1>
      </div>
    </section>
  );
}
```

---

## 12. Vue / Svelte / Vanilla JS Patterns

### Vue 3

```vue
<script setup lang="ts">
import { onMounted, onUnmounted, ref } from 'vue';
import { asciiBackground } from 'asciify-engine';

const hero = ref<HTMLDivElement>();
let stop: (() => void) | undefined;

onMounted(() => {
  if (hero.value) {
    stop = asciiBackground(hero.value, { type: 'stars', colorScheme: 'auto' });
  }
});
onUnmounted(() => stop?.());
</script>

<template>
  <div ref="hero" class="h-screen w-full" />
</template>
```

### Svelte

```svelte
<script lang="ts">
  import { onMount } from 'svelte';
  import { asciiBackground } from 'asciify-engine';

  let container: HTMLDivElement;

  onMount(() => {
    const stop = asciiBackground(container, { type: 'aurora', colorScheme: 'auto' });
    return () => stop();
  });
</script>

<div bind:this={container} class="h-screen w-full" />
```

### Vanilla JS

```html
<div id="hero" style="width:100%;height:100vh"></div>
<script type="module">
  import { asciiBackground } from 'https://esm.sh/asciify-engine';

  asciiBackground('#hero', {
    type: 'rain',
    colorScheme: 'auto',
    accentColor: '#d4ff00',
  });
</script>
```

---

## 13. Common Recipes

### Responsive canvas that fits its container

```ts
const stop = await asciifyVideo('/clip.mp4', canvas, {
  fitTo: '#container', // or an HTMLElement
});
```

### Dark/light mode auto-switching

```ts
asciiBackground('#bg', {
  type: 'wave',
  colorScheme: 'auto', // listens to prefers-color-scheme
  accentColor: 'auto', // probes CSS custom properties
});
```

### Loop a specific section of video

```ts
const stop = await asciifyVideo('/clip.mp4', canvas, {
  trim: { start: 2.5, end: 8.0 }, // loop seconds 2.5â8.0
});
```

### Webcam ASCII mirror

```ts
const stop = await asciifyWebcam(canvas, {
  fitTo: '#webcam-box',
  fontSize: 5,
  colorMode: 'fullcolor',
});
```

### Green screen video overlay

```ts
const stop = await asciifyVideo('/greenscreen.mp4', canvas, {
  fitTo: '#overlay',
  options: { ...DEFAULT_OPTIONS, chromaKey: true, colorMode: 'fullcolor' },
});
```

---

## API Quick Reference

| Function | Returns | Description |
|---|---|---|
| `asciify(source, canvas, opts?)` | `Promise<void>` | One-shot image â ASCII |
| `asciifyVideo(source, canvas, opts?)` | `Promise<() => void>` | Live video â ASCII stream |
| `asciifyGif(source, canvas, opts?)` | `Promise<() => void>` | Animated GIF â ASCII loop |
| `asciifyWebcam(canvas, opts?)` | `Promise<() => void>` | Webcam â live ASCII |
| `asciiBackground(target, opts)` | `() => void` | Animated ASCII background |
| `asciiText(target, opts)` | `() => void` | Large ASCII text rendering |
| `imageToAsciiFrame(src, opts, w?, h?)` | `{ frame, cols, rows }` | Low-level: source â AsciiFrame |
| `renderFrameToCanvas(ctx, frame, opts, w, h, t?, hover?)` | `void` | Low-level: frame â canvas |
| `gifToAsciiFrames(buf, opts, w, h, onProgress?)` | `Promise<{ frames, fps, cols, rows }>` | Low-level: GIF â frames |
| `videoToAsciiFrames(video, opts, w, h, fps?, max?, onProgress?)` | `Promise<{ frames, fps, cols, rows }>` | Low-level: video â frames |
| `generateEmbedCode(frame, opts)` | `string` | Static HTML embed |
| `generateAnimatedEmbedCode(frames, opts, fps)` | `string` | Animated HTML embed |

---

*MIT Â© asciify.org â https://asciify.org*
