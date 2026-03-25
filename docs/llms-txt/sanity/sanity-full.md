# Sanity Documentation

Source: https://logo-soup.sanity.dev/docs/llms-full.txt

---

# createLogoSoup
Source: https://logo-soup.sanity.dev/docs/api-reference/create-logo-soup

Create a framework-agnostic logo normalization engine.

The core factory function that creates a new engine instance. This is what every framework adapter wraps internally, and what you use directly for vanilla JS or unsupported frameworks.

```ts theme={null}
import { createLogoSoup } from "@sanity-labs/logo-soup";

const engine = createLogoSoup();
```

## Returns

`LogoSoupEngine` — an object with the following methods:

### `engine.process(options)`

Triggers a processing run. Loads images, measures them, and produces normalized dimensions. Cancels any in-flight work from a previous `process()` call.

<ParamField type="ProcessOptions">
  The processing options. See [Options Reference](/options) for full details.

  ```ts theme={null}
  engine.process({
    logos: [
      { src: "/logos/acme.svg", alt: "Acme Corp" },
      { src: "/logos/globex.svg", alt: "Globex" },
    ],
    baseSize: 48,
    scaleFactor: 0.5,
    densityAware: true,
    densityFactor: 0.5,
    cropToContent: false,
    contrastThreshold: 10,
    backgroundColor: "#ffffff",
  });
  ```
</ParamField>

**Behavior:**

* If `logos` is empty, transitions directly to `"ready"` with an empty array (synchronous).
* If all logos are already cached, re-normalizes from cache (synchronous, no network requests).
* Otherwise, transitions to `"loading"`, fetches images, measures them, and transitions to `"ready"` or `"error"`.
* Calling `process()` again while loading cancels the previous run. Only the latest call's results are emitted.

### `engine.subscribe(listener)`

Subscribes to state changes. Returns an unsubscribe function.

<ParamField type="() => void">
  A callback invoked whenever the engine's state changes. The listener receives no arguments — call `getSnapshot()` inside it to read the current state.
</ParamField>

**Returns:** `() => void` — call this to unsubscribe.

```ts theme={null}
const unsubscribe = engine.subscribe(() => {
  const state = engine.getSnapshot();
  console.log(state.status, state.normalizedLogos.length);
});

// Later:
unsubscribe();
```

<Note>
  The `subscribe(callback) → unsubscribe` shape is designed to plug directly into framework reactivity primitives: React's `useSyncExternalStore`, Vue's `shallowRef`, Svelte's `createSubscriber`, Solid's `from()`, and Angular's `signal()`.
</Note>

### `engine.getSnapshot()`

Returns the current immutable state snapshot.

**Returns:** `LogoSoupState`

```ts theme={null}
const { status, normalizedLogos, error } = engine.getSnapshot();
```

<Warning>
  `getSnapshot()` must return the **same reference** (`===`) when state hasn't changed. This is a hard requirement for React's `useSyncExternalStore` — if it returns a new object each time, React enters an infinite re-render loop. The engine handles this internally.
</Warning>

### `engine.destroy()`

Cleans up the engine: revokes blob URLs created by `cropToContent`, cancels in-flight image loading, clears the measurement cache, and removes all subscribers.

```ts theme={null}
engine.destroy();
```

Always call `destroy()` when you're done with the engine. Framework adapters handle this automatically on component unmount / scope disposal.

After calling `destroy()`, the engine ignores subsequent `process()` calls.

## Types

### `LogoSoupEngine`

```ts theme={null}
type LogoSoupEngine = {
  process(options: ProcessOptions): void;
  subscribe(listener: () => void): () => void;
  getSnapshot(): LogoSoupState;
  destroy(): void;
};
```

### `LogoSoupState`

```ts theme={null}
type LogoSoupState = {
  status: "idle" | "loading" | "ready" | "error";
  normalizedLogos: NormalizedLogo[];
  error: Error | null;
};
```

| Status      | Description                                            |
| ----------- | ------------------------------------------------------ |
| `"idle"`    | Initial state, before `process()` is called            |
| `"loading"` | Images are being fetched and measured                  |
| `"ready"`   | Normalization complete, `normalizedLogos` is populated |
| `"error"`   | All images failed to load, `error` is set              |

<Note>
  If some images fail but others succeed, the engine transitions to `"ready"` with the successful logos. `"error"` only occurs when **every** image fails.
</Note>

### `ProcessOptions`

```ts theme={null}
type ProcessOptions = {
  logos: (string | LogoSource)[];
  baseSize?: number;            // default: 48
  scaleFactor?: number;         // default: 0.5
  contrastThreshold?: number;   // default: 10
  densityAware?: boolean;       // default: true
  densityFactor?: number;       // default: 0.5
  cropToContent?: boolean;      // default: false
  backgroundColor?: BackgroundColor;
};
```

See [Options Reference](/options) for detailed descriptions of each field.

### `NormalizedLogo`

```ts theme={null}
type NormalizedLogo = {
  src: string;
  alt: string;
  originalWidth: number;
  originalHeight: number;
  contentBox?: BoundingBox;
  normalizedWidth: number;
  normalizedHeight: number;
  aspectRatio: number;
  pixelDensity?: number;
  visualCenter?: VisualCenter;
  croppedSrc?: string;
};
```

See [Options Reference](/options#normalizedlogo-object) for field descriptions.

## Caching Behavior

The engine caches image measurements by URL. This means:

* **Changing `baseSize` or `scaleFactor`** re-normalizes from cache (synchronous, no network).
* **Changing `contrastThreshold`, `densityAware`, or `backgroundColor`** invalidates the cache because these affect the measurement itself.
* **Adding new logos** only loads the new ones; previously cached logos are reused.
* **Removing logos** prunes their cache entries and revokes any associated blob URLs.

## Example: Full Lifecycle

```ts theme={null}
import { createLogoSoup, getVisualCenterTransform } from "@sanity-labs/logo-soup";

const engine = createLogoSoup();

// 1. Subscribe to state changes
const unsubscribe = engine.subscribe(() => {
  const { status, normalizedLogos, error } = engine.getSnapshot();

  switch (status) {
    case "loading":
      console.log("Loading logos...");
      break;
    case "ready":
      console.log("Ready:", normalizedLogos.length, "logos");
      for (const logo of normalizedLogos) {
        const transform = getVisualCenterTransform(logo, "visual-center-y");
        console.log(`  ${logo.alt}: ${logo.normalizedWidth}x${logo.normalizedHeight}`, transform);
      }
      break;
    case "error":
      console.error("Failed:", error?.message);
      break;
  }
});

// 2. Process logos
engine.process({
  logos: [
    { src: "/logos/acme.svg", alt: "Acme" },
    { src: "/logos/globex.svg", alt: "Globex" },
  ],
});
// → "Loading logos..."
// → "Ready: 2 logos"

// 3. Re-process with different size (uses cache, synchronous)
engine.process({
  logos: [
    { src: "/logos/acme.svg", alt: "Acme" },
    { src: "/logos/globex.svg", alt: "Globex" },
  ],
  baseSize: 96,
});
// → "Ready: 2 logos" (instant, no loading state)

// 4. Clean up
unsubscribe();
engine.destroy();
```


# getVisualCenterTransform
Source: https://logo-soup.sanity.dev/docs/api-reference/get-visual-center-transform

Compute a CSS transform to align a logo by its visual weight center.

A pure function that computes a CSS `translate()` transform to shift a logo from its geometric center to its visual weight center. This compensates for asymmetric logos where the perceived center doesn't match the bounding box center.

```ts theme={null}
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

const transform = getVisualCenterTransform(logo, "visual-center-y");
// Returns "translate(0px, -2.3px)" or undefined
```

## Signature

```ts theme={null}
function getVisualCenterTransform(
  logo: NormalizedLogo,
  alignBy?: AlignmentMode,
): string | undefined;
```

## Parameters

<ParamField type="NormalizedLogo">
  A normalized logo object returned by the engine, hook, or composable. Must have `visualCenter`, `normalizedWidth`, `normalizedHeight`, and optionally `contentBox` and `originalWidth`/`originalHeight` for scale computation.
</ParamField>

<ParamField type="AlignmentMode">
  The alignment mode to use. Determines which axes are compensated.

  | Mode                | Description                           |
  | ------------------- | ------------------------------------- |
  | `"bounds"`          | No transform. Returns `undefined`.    |
  | `"visual-center"`   | Compensate on both X and Y axes.      |
  | `"visual-center-x"` | Compensate horizontally only.         |
  | `"visual-center-y"` | Compensate vertically only (default). |
</ParamField>

## Returns

`string | undefined`

* A CSS `translate()` string like `"translate(0px, -2.3px)"` when a meaningful offset exists (greater than 0.5px on either axis).
* `undefined` when no adjustment is needed — either because `alignBy` is `"bounds"`, the logo has no `visualCenter` data, or the offset is negligibly small.

## Usage

### With the React component

The `<LogoSoup>` component applies this automatically via the `alignBy` prop. You don't need to call this function directly when using the component.

```tsx theme={null}
import { LogoSoup } from "@sanity-labs/logo-soup/react";

// Alignment is handled internally
<LogoSoup logos={logos} alignBy="visual-center-y" />
```

### With the React hook

When building custom layouts with `useLogoSoup`, apply the transform manually:

```tsx theme={null}
import { useLogoSoup } from "@sanity-labs/logo-soup/react";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

function CustomGrid() {
  const { normalizedLogos } = useLogoSoup({ logos });

  return (
    <div className="flex gap-4">
      {normalizedLogos.map((logo) => (
        <img
          key={logo.src}
          src={logo.src}
          alt={logo.alt}
          width={logo.normalizedWidth}
          height={logo.normalizedHeight}
          style={{
            transform: getVisualCenterTransform(logo, "visual-center-y"),
          }}
        />
      ))}
    </div>
  );
}
```

### With other frameworks

<CodeGroup>
  ```vue Vue theme={null}
  <template>
    <img
      v-for="logo in normalizedLogos"
      :key="logo.src"
      :src="logo.src"
      :alt="logo.alt"
      :width="logo.normalizedWidth"
      :height="logo.normalizedHeight"
      :style="{ transform: getVisualCenterTransform(logo, 'visual-center-y') }"
    />
  </template>
  ```

  ```svelte Svelte theme={null}
  {#each soup.normalizedLogos as logo (logo.src)}
    <img
      src={logo.src}
      alt={logo.alt}
      width={logo.normalizedWidth}
      height={logo.normalizedHeight}
      style:transform={getVisualCenterTransform(logo, "visual-center-y")}
    />
  {/each}
  ```

  ```tsx Solid theme={null}
  <For each={result.normalizedLogos}>
    {(logo) => (
      <img
        src={logo.src}
        alt={logo.alt}
        width={logo.normalizedWidth}
        height={logo.normalizedHeight}
        style={{
          transform: getVisualCenterTransform(logo, "visual-center-y") ?? "none",
        }}
      />
    )}
  </For>
  ```

  ```typescript Angular theme={null}
  // In the component class:
  protected getTransform(logo: NormalizedLogo): string | undefined {
    return getVisualCenterTransform(logo, this.alignBy());
  }

  // In the template:
  // <img [style.transform]="getTransform(logo)" />
  ```
</CodeGroup>

## How it works

The function computes the offset between a logo's geometric center and its visual weight center, scaled to the normalized dimensions:

1. The `visualCenter` on each `NormalizedLogo` contains `offsetX` and `offsetY` — the displacement from the geometric center of the content box, in source image pixels.
2. These offsets are scaled by the ratio of normalized dimensions to content box dimensions (or original dimensions if no content box exists).
3. If the resulting pixel offset exceeds 0.5px on either axis, a `translate()` string is returned. Below that threshold, the function returns `undefined` to avoid sub-pixel jitter.
4. Values are rounded to one decimal place for clean CSS output.

### Example offset

Consider a logo where the icon is positioned above the wordmark. The geometric center of the bounding box is between the icon and text, but the visual weight is biased toward the denser wordmark below. The `visualCenter.offsetY` would be positive (shifted down), and `getVisualCenterTransform` would return a negative Y translate to shift the logo up, centering it on its visual weight.

## Why `"visual-center-y"` is the default

For horizontal logo rows (the most common layout), vertical misalignment is the most noticeable problem. Logos appear to "bounce" up and down relative to each other. Horizontal misalignment is less perceptible because logos already have spacing between them.

Using `"visual-center-y"` corrects the vertical bounce without introducing unexpected horizontal shifts, which makes it the safest default for most use cases.

Use `"visual-center"` (both axes) when logos are displayed in a grid or when horizontal balance matters equally.


# Angular
Source: https://logo-soup.sanity.dev/docs/frameworks/angular

Use Logo Soup with Angular 19+ via the LogoSoupService injectable.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

Requires Angular 19 or later (signals API). Also works with Angular 20 and 21.

## LogoSoupService

The Angular adapter provides an `@Injectable` service that wraps the core engine using Angular signals. Provide it per component instance so each `<logo-soup>` gets its own engine with independent state and caching.

```typescript theme={null}
import { Component, input, effect, inject, ChangeDetectionStrategy } from "@angular/core";
import { LogoSoupService } from "@sanity-labs/logo-soup/angular";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";
import type { AlignmentMode, NormalizedLogo } from "@sanity-labs/logo-soup";

@Component({
  selector: "logo-strip",
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  providers: [LogoSoupService],
  template: `
    @if (service.state().status === 'ready') {
      <div style="text-align: center; text-wrap: balance;">
        @for (logo of service.state().normalizedLogos; track logo.src) {
          <img
            [src]="logo.croppedSrc || logo.src"
            [alt]="logo.alt"
            [width]="logo.normalizedWidth"
            [height]="logo.normalizedHeight"
            [style.transform]="getTransform(logo)"
            style="display: inline-block; margin: 0 14px;"
          />
        }
      </div>
    }
  `,
})
export class LogoStripComponent {
  protected service = inject(LogoSoupService);

  logos = input.required<(string | { src: string; alt?: string })[]>();
  baseSize = input<number>(48);
  scaleFactor = input<number>(0.5);
  alignBy = input<AlignmentMode>("visual-center-y");

  constructor() {
    effect(() => {
      this.service.process({
        logos: this.logos(),
        baseSize: this.baseSize(),
        scaleFactor: this.scaleFactor(),
      });
    });
  }

  protected getTransform(logo: NormalizedLogo): string | undefined {
    return getVisualCenterTransform(logo, this.alignBy());
  }
}
```

## Service API

### `LogoSoupService`

An `@Injectable` that wraps the core engine.

| Member             | Type                       | Description                                           |
| ------------------ | -------------------------- | ----------------------------------------------------- |
| `state`            | `Signal<LogoSoupState>`    | Readonly signal containing the engine's current state |
| `process(options)` | `(ProcessOptions) => void` | Trigger a processing run with new options             |

The `state` signal contains:

```typescript theme={null}
type LogoSoupState = {
  status: "idle" | "loading" | "ready" | "error";
  normalizedLogos: NormalizedLogo[];
  error: Error | null;
};
```

### Scoping

Provide the service at the **component level** via `providers`:

```typescript theme={null}
@Component({
  providers: [LogoSoupService], // Each component instance gets its own engine
})
```

This ensures each component gets an independent engine with its own image cache. If you provide it at a module or root level, all consumers share a single engine, which is usually not what you want.

## Reactive Options with Signals

Since `effect()` automatically tracks signal reads, any input signal change re-triggers processing:

```typescript theme={null}
@Component({
  selector: "logo-strip",
  standalone: true,
  providers: [LogoSoupService],
  template: `
    @for (logo of service.state().normalizedLogos; track logo.src) {
      <img [src]="logo.src" [alt]="logo.alt"
           [width]="logo.normalizedWidth" [height]="logo.normalizedHeight" />
    }
  `,
})
export class LogoStripComponent {
  protected service = inject(LogoSoupService);

  logos = input.required<string[]>();
  baseSize = input<number>(48);
  densityAware = input<boolean>(true);
  densityFactor = input<number>(0.5);
  cropToContent = input<boolean>(false);

  constructor() {
    effect(() => {
      this.service.process({
        logos: this.logos(),
        baseSize: this.baseSize(),
        densityAware: this.densityAware(),
        densityFactor: this.densityFactor(),
        cropToContent: this.cropToContent(),
      });
    });
  }
}
```

Usage in a parent template:

```html theme={null}
<logo-strip
  [logos]="['logo1.svg', 'logo2.svg', 'logo3.svg']"
  [baseSize]="64"
  [densityAware]="true"
/>
```

## Dark Mode

Pass `backgroundColor` for proper contrast detection on opaque logos:

```typescript theme={null}
@Component({
  selector: "logo-strip",
  standalone: true,
  providers: [LogoSoupService],
  template: `...`,
})
export class LogoStripComponent {
  protected service = inject(LogoSoupService);

  logos = input.required<string[]>();
  isDark = input<boolean>(false);

  constructor() {
    effect(() => {
      this.service.process({
        logos: this.logos(),
        backgroundColor: this.isDark() ? "#1a1a1a" : "#ffffff",
      });
    });
  }
}
```

## Loading and Error States

Read the `status` field from the state signal:

```html theme={null}
@switch (service.state().status) {
  @case ('loading') {
    <div class="skeleton-loader">Loading logos...</div>
  }
  @case ('error') {
    <div class="error">{{ service.state().error?.message }}</div>
  }
  @case ('ready') {
    @for (logo of service.state().normalizedLogos; track logo.src) {
      <img [src]="logo.src" [alt]="logo.alt"
           [width]="logo.normalizedWidth" [height]="logo.normalizedHeight" />
    }
  }
}
```

## Visual Center Alignment

Apply visual center alignment with `getVisualCenterTransform` from the core package:

```typescript theme={null}
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";
import type { AlignmentMode, NormalizedLogo } from "@sanity-labs/logo-soup";

// In your component class:
alignBy = input<AlignmentMode>("visual-center-y");

protected getTransform(logo: NormalizedLogo): string | undefined {
  return getVisualCenterTransform(logo, this.alignBy());
}
```

```html theme={null}
<img
  [src]="logo.src"
  [style.transform]="getTransform(logo)"
/>
```

## Computed Helpers

Use Angular's `computed()` to derive values from the state signal:

```typescript theme={null}
import { computed, inject } from "@angular/core";
import { LogoSoupService } from "@sanity-labs/logo-soup/angular";

export class LogoStripComponent {
  protected service = inject(LogoSoupService);

  isReady = computed(() => this.service.state().status === "ready");
  logoCount = computed(() => this.service.state().normalizedLogos.length);
  hasError = computed(() => this.service.state().error !== null);
}
```

## Cleanup

The service uses `DestroyRef.onDestroy()` internally to unsubscribe from the engine and clean up blob URLs when the component is destroyed. You don't need to handle cleanup manually.

## How It Works Under the Hood

The Angular adapter bridges the core engine to Angular's signal-based reactivity:

* **`signal()`** holds the engine state with `.asReadonly()` for public access — private writable, public readonly (Angular best practice for encapsulated state)
* **`engine.subscribe()`** pushes state changes into the Angular signal via `_state.set()`
* **`DestroyRef.onDestroy()`** unsubscribes and destroys the engine when the injector is torn down — the modern Angular cleanup API (replaces `OnDestroy` lifecycle hook)
* **`ChangeDetectionStrategy.OnPush`** is recommended since signals drive change detection, eliminating the need for the default strategy
* **`input()`** / **`input.required()`** are used instead of the `@Input()` decorator — this is the Angular 19+ way
* **`@for` with `track`** is used instead of `*ngFor` — Angular 19+ built-in control flow


# Build Your Own Adapter
Source: https://logo-soup.sanity.dev/docs/frameworks/custom

Integrate Logo Soup with any framework using the core engine's subscribe/getSnapshot API.

Every first-party adapter follows the same pattern. If your framework isn't listed, you can build an adapter in 20-40 lines.

## The Pattern

```ts theme={null}
import { createLogoSoup } from "@sanity-labs/logo-soup";

// 1. Create an engine instance
const engine = createLogoSoup();

// 2. Subscribe — push snapshots into your framework's reactivity
const unsubscribe = engine.subscribe(() => {
  const snapshot = engine.getSnapshot();
  // yourFramework.setState(snapshot)
});

// 3. Process — call when options change
engine.process({ logos: ["a.svg", "b.svg"], baseSize: 48 });

// 4. Destroy — call on teardown
unsubscribe();
engine.destroy();
```

## Example: Preact 10.x

Preact exposes `useSyncExternalStore` via `preact/compat` — the same API React uses. The adapter is nearly identical to the React one.

```tsx theme={null}
// use-logo-soup.ts
import { useRef, useCallback, useEffect } from "preact/hooks";
import { useSyncExternalStore } from "preact/compat";
import { createLogoSoup } from "@sanity-labs/logo-soup";
import type { ProcessOptions, LogoSoupState } from "@sanity-labs/logo-soup";

const SERVER_SNAPSHOT: LogoSoupState = {
  status: "idle",
  normalizedLogos: [],
  error: null,
};

export function useLogoSoup(options: ProcessOptions) {
  const engineRef = useRef(createLogoSoup());
  const engine = engineRef.current;

  const subscribe = useCallback(
    (cb: () => void) => engine.subscribe(cb),
    [engine],
  );
  const getSnapshot = useCallback(() => engine.getSnapshot(), [engine]);

  const state = useSyncExternalStore(
    subscribe,
    getSnapshot,
    () => SERVER_SNAPSHOT,
  );

  useEffect(() => {
    engine.process(options);
  }, [engine, options.logos, options.baseSize, options.scaleFactor]);

  useEffect(() => () => engine.destroy(), [engine]);

  return state;
}
```

```tsx theme={null}
// usage
import { useLogoSoup } from "./use-logo-soup";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

function LogoStrip() {
  const { status, normalizedLogos } = useLogoSoup({
    logos: ["/logos/acme.svg", "/logos/globex.svg"],
  });

  if (status !== "ready") return null;

  return (
    <div style={{ textAlign: "center" }}>
      {normalizedLogos.map((logo) => (
        <img
          key={logo.src}
          src={logo.src}
          alt={logo.alt}
          width={logo.normalizedWidth}
          height={logo.normalizedHeight}
          style={{
            transform: getVisualCenterTransform(logo, "visual-center-y"),
          }}
        />
      ))}
    </div>
  );
}
```

## Example: Lit 3.x

Lit uses `ReactiveController` to encapsulate reusable logic that hooks into a component's update cycle. The controller subscribes to the engine and calls `host.requestUpdate()` when state changes.

```ts theme={null}
// logo-soup-controller.ts
import { type ReactiveController, type ReactiveControllerHost } from "lit";
import { createLogoSoup } from "@sanity-labs/logo-soup";
import type { ProcessOptions, LogoSoupState } from "@sanity-labs/logo-soup";

export class LogoSoupController implements ReactiveController {
  private engine = createLogoSoup();
  private unsubscribe: (() => void) | null = null;

  state: LogoSoupState = this.engine.getSnapshot();

  constructor(private host: ReactiveControllerHost) {
    host.addController(this);
  }

  hostConnected() {
    this.unsubscribe = this.engine.subscribe(() => {
      this.state = this.engine.getSnapshot();
      this.host.requestUpdate();
    });
  }

  hostDisconnected() {
    this.unsubscribe?.();
    this.engine.destroy();
  }

  process(options: ProcessOptions) {
    this.engine.process(options);
  }
}
```

```ts theme={null}
// usage
import { LitElement, html } from "lit";
import { customElement, property } from "lit/decorators.js";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";
import { LogoSoupController } from "./logo-soup-controller";

@customElement("logo-strip")
export class LogoStrip extends LitElement {
  private soup = new LogoSoupController(this);

  @property({ type: Array }) logos: string[] = [];
  @property({ type: Number }) baseSize = 48;

  updated(changed: Map<string, unknown>) {
    if (changed.has("logos") || changed.has("baseSize")) {
      this.soup.process({ logos: this.logos, baseSize: this.baseSize });
    }
  }

  render() {
    if (this.soup.state.status !== "ready") return html``;

    return html`
      <div style="text-align: center">
        ${this.soup.state.normalizedLogos.map(
          (logo) => html`
            <img
              src=${logo.src}
              alt=${logo.alt}
              width=${logo.normalizedWidth}
              height=${logo.normalizedHeight}
              style="display:inline-block;margin:0 14px;transform:${getVisualCenterTransform(
                logo,
                "visual-center-y",
              ) ?? "none"}"
            />
          `,
        )}
      </div>
    `;
  }
}
```

## Checklist

| Concern       | What to do                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------- |
| **Create**    | Call `createLogoSoup()` once per component instance                                         |
| **Subscribe** | Push `engine.getSnapshot()` into your reactive state on each notification                   |
| **Process**   | Call `engine.process(options)` when inputs change                                           |
| **Cleanup**   | Call both `unsubscribe()` and `engine.destroy()` on teardown                                |
| **Stability** | Store the engine in a ref/field — don't recreate it on every render                         |
| **SSR**       | The engine needs `<canvas>`, so guard behind a client-side check if your framework does SSR |

## How Our First-Party Adapters Map

| Framework | Reactive primitive     | Subscribe mechanism                                | Cleanup                   |
| --------- | ---------------------- | -------------------------------------------------- | ------------------------- |
| React     | `useSyncExternalStore` | Engine's `subscribe`/`getSnapshot` directly        | `useEffect` return        |
| Vue       | `shallowRef`           | `engine.subscribe()` → `ref.value = snapshot`      | `onScopeDispose`          |
| Svelte    | `createSubscriber`     | Getter calls `subscribe()` before reading          | `$effect` teardown        |
| Solid     | `from()`               | Producer function `(set) => engine.subscribe(...)` | `onCleanup`               |
| Angular   | `signal()`             | `engine.subscribe()` → `_state.set(snapshot)`      | `DestroyRef.onDestroy`    |
| jQuery    | `$.data()`             | `engine.subscribe()` → re-render DOM               | `$el.logoSoup('destroy')` |

Each adapter is 30-80 lines. The source is at [`src/react`](https://github.com/sanity-labs/logo-soup/tree/main/src/react), [`src/vue`](https://github.com/sanity-labs/logo-soup/tree/main/src/vue), [`src/svelte`](https://github.com/sanity-labs/logo-soup/tree/main/src/svelte), [`src/solid`](https://github.com/sanity-labs/logo-soup/tree/main/src/solid), [`src/angular`](https://github.com/sanity-labs/logo-soup/tree/main/src/angular), and [`src/jquery`](https://github.com/sanity-labs/logo-soup/tree/main/src/jquery).

<Tip>
  Built an adapter for a framework we don't support? [Let us
  know](https://github.com/sanity-labs/logo-soup/issues) — we'll link to it from
  the docs.
</Tip>


# jQuery
Source: https://logo-soup.sanity.dev/docs/frameworks/jquery

Use Logo Soup with jQuery 4.x via the $.fn.logoSoup plugin.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup jquery@4
```

Requires jQuery 4.0 or later.

## Setup

The plugin needs to be installed onto jQuery. There are two ways to do this:

### Auto-install (global jQuery)

If jQuery is available on `window`, the plugin installs itself automatically on import:

```html theme={null}
<script src="https://code.jquery.com/jquery-4.0.0.min.js"></script>
<script type="module">
  import "@sanity-labs/logo-soup/jquery";

  $("#logos").logoSoup({
    logos: ["/logos/acme.svg", "/logos/globex.svg"],
  });
</script>
```

### Manual install (ES modules)

When using a bundler, import and call `install` with your jQuery instance:

```ts theme={null}
import $ from "jquery";
import { install } from "@sanity-labs/logo-soup/jquery";

install($);
```

## Basic Usage

```ts theme={null}
$("#logos").logoSoup({
  logos: [
    { src: "/logos/acme.svg", alt: "Acme Corp" },
    { src: "/logos/globex.svg", alt: "Globex" },
    { src: "/logos/initech.svg", alt: "Initech" },
  ],
  baseSize: 48,
  gap: 28,
  alignBy: "visual-center-y",
});
```

The plugin renders normalized `<img>` elements into the selected container with visual center alignment and a fade-in transition.

## Plugin Options

All [shared options](/options) are supported, plus these jQuery-specific ones:

| Option    | Type                                | Default             | Description                           |
| --------- | ----------------------------------- | ------------------- | ------------------------------------- |
| `alignBy` | `AlignmentMode`                     | `"visual-center-y"` | How to align logos                    |
| `gap`     | `number \| string`                  | `28`                | Space between logos                   |
| `onReady` | `(logos: NormalizedLogo[]) => void` | —                   | Callback when normalization completes |
| `onError` | `(error: Error) => void`            | —                   | Callback when all images fail to load |

## Methods

Call methods on an existing plugin instance using the standard jQuery plugin convention:

### `process`

Update the logos or options on an existing instance:

```ts theme={null}
$("#logos").logoSoup("process", {
  logos: ["/logos/new-logo.svg", "/logos/another.svg"],
  baseSize: 64,
});
```

### `ready`

Returns a native `Promise` that resolves with the normalized logos when processing completes:

```ts theme={null}
const logos = await $("#logos").logoSoup("ready");
console.log(logos.length, "logos normalized");
```

If logos are already processed, the promise resolves immediately. If processing fails, the promise rejects with the error.

### `destroy`

Removes the plugin instance, cleans up the engine, and empties the container:

```ts theme={null}
$("#logos").logoSoup("destroy");
```

### `instance`

Returns the internal plugin instance (engine, unsubscribe function, current options) for the first matched element. Useful for advanced use cases:

```ts theme={null}
const instance = $("#logos").logoSoup("instance");
const state = instance.engine.getSnapshot();
```

## Full Example

```html theme={null}
<!DOCTYPE html>
<html>
  <head>
    <script src="https://code.jquery.com/jquery-4.0.0.min.js"></script>
  </head>
  <body>
    <div id="logos"></div>
    <button id="toggle-size">Toggle Size</button>
    <button id="destroy">Destroy</button>

    <script type="module">
      import "@sanity-labs/logo-soup/jquery";

      const logos = [
        { src: "/logos/acme.svg", alt: "Acme Corp" },
        { src: "/logos/globex.svg", alt: "Globex" },
        { src: "/logos/initech.svg", alt: "Initech" },
      ];

      let baseSize = 48;

      $("#logos").logoSoup({
        logos,
        baseSize,
        onReady(normalized) {
          console.log(`${normalized.length} logos normalized`);
        },
      });

      $("#toggle-size").on("click", () => {
        baseSize = baseSize === 48 ? 64 : 48;
        $("#logos").logoSoup("process", { logos, baseSize });
      });

      $("#destroy").on("click", () => {
        $("#logos").logoSoup("destroy");
      });
    </script>
  </body>
</html>
```

## Dark Mode

Pass `backgroundColor` for proper contrast detection on opaque logos:

```ts theme={null}
const isDark = window.matchMedia("(prefers-color-scheme: dark)").matches;

$("#logos").logoSoup({
  logos,
  backgroundColor: isDark ? "#1a1a1a" : "#ffffff",
});
```

## Chaining

The plugin supports standard jQuery chaining for initialization, `process`, and `destroy`:

```ts theme={null}
$("#logos")
  .logoSoup({ logos, baseSize: 48 })
  .addClass("logo-strip")
  .css("padding", "20px");
```

The `ready` method breaks the chain since it returns a `Promise` instead of a jQuery object.

## Re-initialization

Calling `.logoSoup({...})` on an element that already has an instance automatically destroys the old instance and creates a new one:

```ts theme={null}
// First init
$("#logos").logoSoup({ logos: firstLogos });

// Re-init with different logos — old engine is cleaned up
$("#logos").logoSoup({ logos: secondLogos });
```

## How It Works Under the Hood

The jQuery adapter is a standard `$.fn` plugin that:

* Stores the engine instance via `$.data()` on each element
* Subscribes to the engine's state changes and renders `<img>` elements into the container using DOM APIs
* Applies `getVisualCenterTransform` for visual center alignment
* Uses native `Promise` for the `ready` method (jQuery 4 slim build dropped Deferreds in favor of native Promises)
* Cleans up blob URLs and subscriptions on `destroy`


# Node.js
Source: https://logo-soup.sanity.dev/docs/frameworks/node

Pre-compute logo measurements server-side with the Node.js adapter.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup @napi-rs/canvas
```

`@napi-rs/canvas` is a peer dependency — it provides the Skia-backed canvas used for pixel analysis on Node. Zero system dependencies.

## Why pre-compute?

Logo Soup normally runs client-side on a `<canvas>`. That's fine for most cases, but sometimes you want to skip the client-side pixel scanning entirely:

* **Static sites / build-time optimization** — measure logos once at build time, ship the results as JSON
* **SSR / API routes** — compute measurements on the server so the client renders instantly with no layout shift
* **Large logo sets** — offload the work from the browser for 50+ logos

The Node adapter runs the exact same measurement pipeline as the browser (same downsampling, same single-pass pixel scan, same normalization math), just using `@napi-rs/canvas` instead of an `HTMLCanvasElement`.

## measureImage

Measure a single image. Accepts a file path, URL, or Buffer.

```ts theme={null}
import { measureImage } from "@sanity-labs/logo-soup/node";

const result = await measureImage("./logos/acme.svg");
```

### Parameters

<ParamField type="string | Buffer">
  A file path, HTTP URL, or Buffer containing image data. Supports PNG, JPEG, SVG, WebP, and any format `@napi-rs/canvas` can decode.
</ParamField>

<ParamField type="MeasureOptions">
  | Option              | Type                       | Default       | Description                                              |
  | ------------------- | -------------------------- | ------------- | -------------------------------------------------------- |
  | `contrastThreshold` | `number`                   | `10`          | Minimum contrast distance to classify a pixel as content |
  | `densityAware`      | `boolean`                  | `true`        | Whether to compute pixel density                         |
  | `backgroundColor`   | `[number, number, number]` | auto-detected | Explicit RGB background color, skips perimeter detection |
</ParamField>

### Returns

`Promise<MeasurementResult>` — the same type returned by the browser engine's content detection:

```ts theme={null}
type MeasurementResult = {
  width: number;
  height: number;
  contentBox?: BoundingBox;
  pixelDensity?: number;
  visualCenter?: VisualCenter;
  backgroundLuminance?: number;
};
```

## measureImages

Measure multiple images in parallel. Returns results in the same order as the input array.

```ts theme={null}
import { measureImages } from "@sanity-labs/logo-soup/node";

const results = await measureImages([
  "./logos/acme.svg",
  "./logos/globex.svg",
  "./logos/initech.svg",
]);
```

## Build-time workflow

The typical workflow is: measure on the server, serialize the results, and use them on the client to skip all canvas work.

### 1. Measure at build time

```ts theme={null}
// scripts/measure-logos.ts
import { writeFile } from "node:fs/promises";
import { measureImages } from "@sanity-labs/logo-soup/node";

const logos = [
  "./public/logos/acme.svg",
  "./public/logos/globex.svg",
  "./public/logos/initech.svg",
];

const measurements = await measureImages(logos);

await writeFile(
  "./src/logo-measurements.json",
  JSON.stringify(measurements),
);
```

### 2. Use on the client

```tsx theme={null}
import { createNormalizedLogo, getVisualCenterTransform } from "@sanity-labs/logo-soup";
import measurements from "./logo-measurements.json";

const logos = [
  { src: "/logos/acme.svg", alt: "Acme" },
  { src: "/logos/globex.svg", alt: "Globex" },
  { src: "/logos/initech.svg", alt: "Initech" },
];

// Pure math, no canvas, no async — instant
const normalized = logos.map((logo, i) =>
  createNormalizedLogo(logo, measurements[i], 48, 0.5, 0.5),
);
```

The client never loads a canvas, never scans pixels, and never waits for image loads before knowing the layout dimensions. The `createNormalizedLogo` and `getVisualCenterTransform` functions are pure math that work anywhere.

## API route example

The same approach works at request time in a server framework:

```ts theme={null}
// Next.js API route (app router)
import { measureImage, createNormalizedLogo } from "@sanity-labs/logo-soup/node";

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url);
  const src = searchParams.get("src");

  const measurement = await measureImage(src);
  const normalized = createNormalizedLogo(
    { src, alt: "" },
    measurement,
    48, 0.5, 0.5,
  );

  return Response.json(normalized);
}
```

## Re-exported utilities

The Node adapter re-exports the pure math functions you need to go from `MeasurementResult` to rendered output, so you don't need to import from the core entry point:

| Export                          | Description                                                        |
| ------------------------------- | ------------------------------------------------------------------ |
| `calculateNormalizedDimensions` | Compute normalized width/height from a `MeasurementResult`         |
| `createNormalizedLogo`          | Build a full `NormalizedLogo` object from a source and measurement |
| `getVisualCenterTransform`      | Compute a CSS `translate()` for visual center alignment            |
| `MeasurementResult`             | TypeScript type for measurement data                               |
| `NormalizedLogo`                | TypeScript type for the processed logo object                      |
| `LogoSource`                    | TypeScript type for logo input (`{ src, alt? }`)                   |
| `AlignmentMode`                 | TypeScript type for `getVisualCenterTransform` alignment modes     |
| `BoundingBox`                   | TypeScript type for content box dimensions                         |
| `VisualCenter`                  | TypeScript type for visual center offset data                      |
| `MeasureOptions`                | TypeScript type for `measureImage`/`measureImages` options         |

## Differences from the browser engine

| Concern        | Browser (`createLogoSoup`)                       | Node (`measureImage`)                                                  |
| -------------- | ------------------------------------------------ | ---------------------------------------------------------------------- |
| Canvas backend | `HTMLCanvasElement`                              | `@napi-rs/canvas` (Skia)                                               |
| Image loading  | `new Image()` with `onload`                      | `@napi-rs/canvas` `loadImage()` (file path, URL, or Buffer)            |
| Caching        | Automatic by URL, invalidated on option change   | None — stateless, cache yourself                                       |
| Cancellation   | Built-in (latest `process()` wins)               | Not applicable — use `AbortController` upstream                        |
| Reactivity     | `subscribe`/`getSnapshot` for framework adapters | Returns a `Promise` — wire into your server framework however you like |
| Pixel math     | Shared `measureContent` pipeline                 | Same shared `measureContent` pipeline                                  |

The measurement results are identical. Both paths downsample to \~2,048 pixels and run the same single-pass scan.


# React
Source: https://logo-soup.sanity.dev/docs/frameworks/react

Use Logo Soup with React via the LogoSoup component or the useLogoSoup hook.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

React 18 and 19 are both supported.

## LogoSoup Component

The fastest way to get started. Drop it in and it handles everything:

```tsx theme={null}
import { LogoSoup } from "@sanity-labs/logo-soup/react";

function LogoStrip() {
  return (
    <LogoSoup
      logos={[
        { src: "/logos/acme.svg", alt: "Acme Corp" },
        { src: "/logos/globex.svg", alt: "Globex" },
        { src: "/logos/initech.svg", alt: "Initech" },
      ]}
      baseSize={48}
      gap={28}
      alignBy="visual-center-y"
    />
  );
}
```

The component renders a centered, balanced row of logos with a fade-in transition. It returns `null` if all images fail to load.

### Component Props

All [shared options](/options) are supported as props, plus these React-specific ones:

| Prop           | Type                   | Default             | Description                           |
| -------------- | ---------------------- | ------------------- | ------------------------------------- |
| `gap`          | `number \| string`     | `28`                | Space between logos                   |
| `alignBy`      | `AlignmentMode`        | `"visual-center-y"` | How to align logos                    |
| `renderImage`  | `(props) => ReactNode` | `<img>`             | Custom image renderer                 |
| `className`    | `string`               | —                   | Container class name                  |
| `style`        | `CSSProperties`        | —                   | Container inline styles               |
| `onNormalized` | `(logos) => void`      | —                   | Callback when normalization completes |

## useLogoSoup Hook

For custom layouts, use the hook directly:

```tsx theme={null}
import { useLogoSoup } from "@sanity-labs/logo-soup/react";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

function CustomGrid() {
  const { isLoading, isReady, normalizedLogos, error } = useLogoSoup({
    logos: [
      { src: "/logo1.svg", alt: "Logo 1" },
      { src: "/logo2.svg", alt: "Logo 2" },
    ],
    baseSize: 48,
    scaleFactor: 0.5,
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="flex items-center gap-4">
      {normalizedLogos.map((logo) => (
        <img
          key={logo.src}
          src={logo.croppedSrc || logo.src}
          alt={logo.alt}
          width={logo.normalizedWidth}
          height={logo.normalizedHeight}
          style={{
            transform: getVisualCenterTransform(logo, "visual-center-y"),
          }}
        />
      ))}
    </div>
  );
}
```

### Return Value

| Property          | Type               | Description                                              |
| ----------------- | ------------------ | -------------------------------------------------------- |
| `isLoading`       | `boolean`          | `true` while images are being loaded and measured        |
| `isReady`         | `boolean`          | `true` when all logos are normalized and ready to render |
| `normalizedLogos` | `NormalizedLogo[]` | The processed logos with computed dimensions             |
| `error`           | `Error \| null`    | Set if all images fail to load                           |

## Custom Image Component

Use `renderImage` to integrate with Next.js Image, Remix, or add custom attributes:

### Next.js Image

```tsx theme={null}
import Image from "next/image";
import { LogoSoup } from "@sanity-labs/logo-soup/react";

<LogoSoup
  logos={logos}
  renderImage={(props) => (
    <Image
      src={props.src}
      alt={props.alt}
      width={props.width}
      height={props.height}
    />
  )}
/>;
```

### Lazy loading

```tsx theme={null}
<LogoSoup
  logos={logos}
  renderImage={(props) => (
    <img {...props} loading="lazy" decoding="async" />
  )}
/>
```

## Visual Center Alignment

When using the hook, apply visual center alignment with `getVisualCenterTransform`:

```tsx theme={null}
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

// Inside your component:
const transform = getVisualCenterTransform(logo, "visual-center-y");
// Returns something like "translate(0px, -2.3px)" or undefined
```

This compensates for logos with asymmetric visual weight (e.g., a logo where the icon is heavier on one side). The `<LogoSoup>` component applies this automatically via the `alignBy` prop.

## SSR

The hook provides a `getServerSnapshot` that returns an idle state during server rendering. Logos are always processed client-side (canvas is required). The component renders an empty container on the server and hydrates with normalized logos on the client.

## How It Works Under the Hood

The React adapter uses `useSyncExternalStore` to subscribe to the core engine. The engine is created once in a `useRef` and destroyed on unmount. The `logos` array reference is stabilized internally (deep comparison by `src`) to prevent infinite re-render loops when consumers pass inline array literals.


# Solid
Source: https://logo-soup.sanity.dev/docs/frameworks/solid

Use Logo Soup with Solid 1.9+ via the useLogoSoup reactive primitive.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

Requires solid-js 1.9 or later.

## useLogoSoup

The Solid adapter wraps the core engine using `from()`, Solid's built-in primitive for external store subscriptions. Options are passed as a getter function so Solid can track reactive dependencies inside it.

```tsx theme={null}
import { useLogoSoup } from "@sanity-labs/logo-soup/solid";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";
import { For, Show } from "solid-js";

function LogoStrip() {
  const result = useLogoSoup(() => ({
    logos: [
      { src: "/logos/acme.svg", alt: "Acme Corp" },
      { src: "/logos/globex.svg", alt: "Globex" },
      { src: "/logos/initech.svg", alt: "Initech" },
    ],
    baseSize: 48,
    scaleFactor: 0.5,
  }));

  return (
    <Show when={result.isReady}>
      <div style={{ "text-align": "center" }}>
        <For each={result.normalizedLogos}>
          {(logo) => (
            <img
              src={logo.croppedSrc || logo.src}
              alt={logo.alt}
              width={logo.normalizedWidth}
              height={logo.normalizedHeight}
              style={{
                display: "inline-block",
                margin: "0 14px",
                transform:
                  getVisualCenterTransform(logo, "visual-center-y") ?? "none",
              }}
            />
          )}
        </For>
      </div>
    </Show>
  );
}
```

## Reactive Options

Options are passed as a **getter function** `() => ProcessOptions`. This is the standard Solid pattern for reactive props. Any signals read inside the getter are automatically tracked:

```tsx theme={null}
import { createSignal } from "solid-js";
import { useLogoSoup } from "@sanity-labs/logo-soup/solid";

function LogoStrip() {
  const [logos, setLogos] = createSignal(["/logos/acme.svg"]);
  const [baseSize, setBaseSize] = createSignal(48);

  const result = useLogoSoup(() => ({
    logos: logos(),
    baseSize: baseSize(),
    scaleFactor: 0.5,
  }));

  return (
    <div>
      <button onClick={() => setBaseSize((s) => (s === 48 ? 64 : 48))}>
        Toggle size
      </button>
      <button
        onClick={() => setLogos((prev) => [...prev, "/logos/globex.svg"])}
      >
        Add logo
      </button>
      <Show when={result.isReady}>
        <For each={result.normalizedLogos}>
          {(logo) => (
            <img
              src={logo.src}
              alt={logo.alt}
              width={logo.normalizedWidth}
              height={logo.normalizedHeight}
            />
          )}
        </For>
      </Show>
    </div>
  );
}
```

Internally, `createEffect` re-evaluates the getter whenever any signal it reads changes, then calls `engine.process()` with the new options.

## Return Value

The return value is an object with reactive getters:

| Property          | Type               | Description                                              |
| ----------------- | ------------------ | -------------------------------------------------------- |
| `isLoading`       | `boolean`          | `true` while images are being loaded and measured        |
| `isReady`         | `boolean`          | `true` when all logos are normalized and ready to render |
| `normalizedLogos` | `NormalizedLogo[]` | The processed logos with computed dimensions             |
| `error`           | `Error \| null`    | Set if all images fail to load                           |

<Warning>
  These are **getters**, not signals. You read them as properties (`result.isReady`), not function calls (`result.isReady()`). Each getter internally reads a signal created by `from()`, so they're fully reactive in Solid's tracking system.
</Warning>

## Visual Center Alignment

Apply visual center alignment with the `getVisualCenterTransform` helper:

```tsx theme={null}
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

// Inside a component:
<For each={result.normalizedLogos}>
  {(logo) => (
    <img
      src={logo.src}
      alt={logo.alt}
      width={logo.normalizedWidth}
      height={logo.normalizedHeight}
      style={{
        transform:
          getVisualCenterTransform(logo, "visual-center-y") ?? "none",
      }}
    />
  )}
</For>;
```

## Dark Mode

Pass `backgroundColor` so Logo Soup can detect contrast on opaque logos and apply irradiation compensation:

```tsx theme={null}
import { createSignal } from "solid-js";
import { useLogoSoup } from "@sanity-labs/logo-soup/solid";

function LogoStrip() {
  const [isDark, setIsDark] = createSignal(false);

  const result = useLogoSoup(() => ({
    logos: ["/logos/acme.svg", "/logos/globex.svg"],
    backgroundColor: isDark() ? "#1a1a1a" : "#ffffff",
  }));

  // ...
}
```

## Cleanup

The engine is automatically destroyed when the owning reactive scope is disposed (via `onCleanup`). You don't need to call `destroy()` manually in components.

If you use `useLogoSoup` outside a component (e.g., in a `createRoot`), make sure to dispose the root when you're done:

```tsx theme={null}
import { createRoot } from "solid-js";
import { useLogoSoup } from "@sanity-labs/logo-soup/solid";

const dispose = createRoot((dispose) => {
  const result = useLogoSoup(() => ({
    logos: ["/logo.svg"],
  }));

  // Use result...

  return dispose;
});

// Later: clean up
dispose();
```

## How It Works Under the Hood

The Solid adapter uses three Solid primitives:

* **`from()`** — Bridges the engine's `subscribe`/`getSnapshot` interface into a Solid signal. `from()` accepts a producer function `(set) => unsubscribe` and returns a read-only accessor.
* **`createEffect()`** — Re-runs when any signal read inside the options getter changes, calling `engine.process()` with the new values.
* **`onCleanup()`** — Destroys the engine when the reactive scope is torn down.


# Svelte
Source: https://logo-soup.sanity.dev/docs/frameworks/svelte

Use Logo Soup with Svelte 5 via the createLogoSoup runes-compatible store.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

Requires Svelte 5 (runes). The adapter uses `createSubscriber` from `svelte/reactivity` (available since 5.7.0).

## createLogoSoup

The Svelte adapter exposes a `createLogoSoup` function that returns a reactive object. Reading its properties inside an `$effect` or template automatically subscribes to state changes.

```svelte theme={null}
<script>
  import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";
  import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

  let { logos = [], baseSize = 48, scaleFactor = 0.5 } = $props();

  const soup = createLogoSoup();

  $effect(() => {
    soup.process({ logos, baseSize, scaleFactor });
  });

  $effect(() => {
    return () => soup.destroy();
  });
</script>

{#if soup.isReady}
  <div style="text-align: center;">
    {#each soup.normalizedLogos as logo (logo.src)}
      <img
        src={logo.croppedSrc || logo.src}
        alt={logo.alt}
        width={logo.normalizedWidth}
        height={logo.normalizedHeight}
        style:transform={getVisualCenterTransform(logo, "visual-center-y")}
        style:display="inline-block"
        style:margin="0 14px"
      />
    {/each}
  </div>
{/if}
```

## Reactive Properties

The object returned by `createLogoSoup()` exposes these reactive getters:

| Property          | Type               | Description                           |
| ----------------- | ------------------ | ------------------------------------- |
| `state`           | `LogoSoupState`    | Raw state snapshot from the engine    |
| `isLoading`       | `boolean`          | `true` while images are being loaded  |
| `isReady`         | `boolean`          | `true` when normalization is complete |
| `normalizedLogos` | `NormalizedLogo[]` | The processed logos                   |
| `error`           | `Error \| null`    | Set if all images fail to load        |

And these methods:

| Method             | Description                                  |
| ------------------ | -------------------------------------------- |
| `process(options)` | Trigger a processing run with new options    |
| `destroy()`        | Clean up blob URLs and cancel in-flight work |

## Reactive Options

Since `$effect` auto-tracks any reactive state (`$state`, `$derived`, `$props`) read inside it, changing any option value automatically re-triggers processing:

```svelte theme={null}
<script>
  import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";

  let logos = $state(["/logos/acme.svg", "/logos/globex.svg"]);
  let baseSize = $state(48);

  const soup = createLogoSoup();

  $effect(() => {
    // Re-runs whenever `logos` or `baseSize` changes
    soup.process({ logos, baseSize });
  });

  $effect(() => {
    return () => soup.destroy();
  });

  function addLogo(src) {
    logos = [...logos, src];
    // $effect above re-runs automatically
  }
</script>

<button onclick={() => addLogo("/logos/new.svg")}>Add logo</button>
<button onclick={() => baseSize = baseSize === 48 ? 64 : 48}>Toggle size</button>

{#if soup.isReady}
  {#each soup.normalizedLogos as logo (logo.src)}
    <img
      src={logo.src}
      alt={logo.alt}
      width={logo.normalizedWidth}
      height={logo.normalizedHeight}
    />
  {/each}
{/if}
```

## Dark Mode with Background Color

When displaying logos on a dark background, pass `backgroundColor` so Logo Soup can properly detect contrast and apply irradiation compensation:

```svelte theme={null}
<script>
  import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";

  let { logos = [] } = $props();
  let isDark = $state(false);

  const soup = createLogoSoup();

  $effect(() => {
    soup.process({
      logos,
      backgroundColor: isDark ? "#1a1a1a" : "#ffffff",
    });
  });

  $effect(() => {
    return () => soup.destroy();
  });
</script>
```

## Visual Center Alignment

Apply visual center alignment with the `getVisualCenterTransform` helper from the core package:

```svelte theme={null}
<script>
  import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";
  import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

  // ...setup...
</script>

{#each soup.normalizedLogos as logo (logo.src)}
  <img
    src={logo.src}
    alt={logo.alt}
    width={logo.normalizedWidth}
    height={logo.normalizedHeight}
    style:transform={getVisualCenterTransform(logo, "visual-center-y")}
  />
{/each}
```

The function returns a CSS transform string like `translate(0px, -2.3px)` or `undefined` if no offset is needed.

## Reusable Component

Wrap it in a reusable Svelte component:

```svelte theme={null}
<!-- LogoSoup.svelte -->
<script>
  import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";
  import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

  let {
    logos = [],
    baseSize = 48,
    scaleFactor = 0.5,
    alignBy = "visual-center-y",
    gap = 28,
    ...rest
  } = $props();

  const soup = createLogoSoup();

  $effect(() => {
    soup.process({ logos, baseSize, scaleFactor, ...rest });
  });

  $effect(() => {
    return () => soup.destroy();
  });

  const halfGap = $derived(
    typeof gap === "number" ? `${gap / 2}px` : `calc(${gap} / 2)`
  );
</script>

<div style="text-align: center; text-wrap: balance;">
  {#each soup.normalizedLogos as logo, i (logo.src + i)}
    <span
      style:display="inline-block"
      style:vertical-align="middle"
      style:padding={halfGap}
      style:opacity={soup.isLoading ? 0 : 1}
      style:transition="opacity 0.2s ease-in-out"
    >
      <img
        src={logo.croppedSrc || logo.src}
        alt={logo.alt}
        width={logo.normalizedWidth}
        height={logo.normalizedHeight}
        style:display="block"
        style:object-fit="contain"
        style:width="{logo.normalizedWidth}px"
        style:height="{logo.normalizedHeight}px"
        style:transform={getVisualCenterTransform(logo, alignBy)}
      />
    </span>
  {/each}
</div>
```

Usage:

```svelte theme={null}
<script>
  import LogoSoup from "./LogoSoup.svelte";
</script>

<LogoSoup
  logos={["/logos/acme.svg", "/logos/globex.svg", "/logos/initech.svg"]}
  baseSize={48}
  gap={24}
/>
```

## How It Works Under the Hood

The Svelte adapter uses `createSubscriber` from `svelte/reactivity` (5.7+) to bridge the core engine's `subscribe`/`getSnapshot` interface into Svelte's runes-based reactivity:

* **`createSubscriber`** returns a function that, when called inside a reactive context (`$effect`, template expression, `$derived`), registers the caller as a subscriber
* Each **getter** (`isReady`, `normalizedLogos`, etc.) calls `subscribe()` before reading from the engine, making it automatically reactive
* The engine itself is **not duplicated into `$state`** — it remains the single source of truth, with `createSubscriber` acting as the bridge
* No legacy store contract (`$:` or `subscribe` method) is used — this is pure Svelte 5 runes


# Vanilla JavaScript
Source: https://logo-soup.sanity.dev/docs/frameworks/vanilla

Use Logo Soup without any framework via the core createLogoSoup engine.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

No framework peer dependencies required. The core engine runs anywhere with a DOM (canvas API).

## createLogoSoup Engine

The core engine is what every framework adapter wraps. You can use it directly for vanilla JS apps, Web Components, or any framework that doesn't have a dedicated adapter.

```ts theme={null}
import { createLogoSoup, getVisualCenterTransform } from "@sanity-labs/logo-soup";

const engine = createLogoSoup();

engine.subscribe(() => {
  const { status, normalizedLogos, error } = engine.getSnapshot();

  if (status === "loading") {
    document.getElementById("logos")!.innerHTML = "Loading...";
    return;
  }

  if (status === "error") {
    console.error("Failed to load logos:", error);
    return;
  }

  if (status === "ready") {
    const container = document.getElementById("logos")!;
    container.innerHTML = normalizedLogos
      .map((logo) => {
        const transform = getVisualCenterTransform(logo, "visual-center-y");
        return `<img
          src="${logo.croppedSrc || logo.src}"
          alt="${logo.alt}"
          width="${logo.normalizedWidth}"
          height="${logo.normalizedHeight}"
          style="
            display: inline-block;
            margin: 0 14px;
            transform: ${transform ?? "none"};
          "
        />`;
      })
      .join("");
  }
});

engine.process({
  logos: [
    { src: "/logos/acme.svg", alt: "Acme Corp" },
    { src: "/logos/globex.svg", alt: "Globex" },
    { src: "/logos/initech.svg", alt: "Initech" },
  ],
  baseSize: 48,
  scaleFactor: 0.5,
});
```

## Engine API

### `createLogoSoup()`

Creates a new engine instance. Each instance has its own image cache and state.

```ts theme={null}
import { createLogoSoup } from "@sanity-labs/logo-soup";

const engine = createLogoSoup();
```

### `engine.process(options)`

Triggers a processing run. Cancels any in-flight work from a previous `process()` call. Accepts all [shared options](/options).

```ts theme={null}
engine.process({
  logos: ["/logos/acme.svg", "/logos/globex.svg"],
  baseSize: 48,
  scaleFactor: 0.5,
  densityAware: true,
  densityFactor: 0.5,
  cropToContent: false,
  contrastThreshold: 10,
  backgroundColor: "#ffffff",
});
```

Calling `process()` again with new options re-uses cached measurements for logos that haven't changed. Only new logos trigger image loading.

### `engine.subscribe(listener)`

Subscribes to state changes. Returns an unsubscribe function.

```ts theme={null}
const unsubscribe = engine.subscribe(() => {
  const state = engine.getSnapshot();
  console.log(state.status, state.normalizedLogos.length);
});

// Later: stop listening
unsubscribe();
```

The listener receives no arguments. Call `getSnapshot()` inside the listener to read the current state. This design matches the pattern expected by `React.useSyncExternalStore`, Vue's `shallowRef`, Svelte's `createSubscriber`, and Solid's `from()`.

### `engine.getSnapshot()`

Returns the current immutable state snapshot. Returns the same reference (`===`) when state hasn't changed, which is critical for frameworks that use referential equality to avoid unnecessary re-renders.

```ts theme={null}
const state = engine.getSnapshot();
```

The snapshot shape:

```ts theme={null}
type LogoSoupState = {
  status: "idle" | "loading" | "ready" | "error";
  normalizedLogos: NormalizedLogo[];
  error: Error | null;
};
```

| Status      | Description                                          |
| ----------- | ---------------------------------------------------- |
| `"idle"`    | Initial state, before `process()` is called          |
| `"loading"` | Images are being fetched and measured                |
| `"ready"`   | All logos normalized, `normalizedLogos` is populated |
| `"error"`   | All images failed to load, `error` is set            |

<Note>
  If some images fail but others succeed, the engine still transitions to `"ready"` with the successful logos. `"error"` only occurs when *all* images fail.
</Note>

### `engine.destroy()`

Cleans up the engine: revokes blob URLs, cancels in-flight work, clears the image cache, and removes all subscribers.

```ts theme={null}
engine.destroy();
```

Always call `destroy()` when you're done with the engine to avoid memory leaks from blob URLs.

## Lifecycle

A typical lifecycle looks like:

```
createLogoSoup()  →  idle
     │
  process()       →  loading  →  ready
     │                           (or error if all fail)
  process()       →  ready       (from cache, synchronous)
     │
  process()       →  loading  →  ready   (new logos, async)
     │
  destroy()
```

Calling `process()` while a previous run is still loading cancels the in-flight work. Only the latest `process()` call's results are emitted.

## Re-processing on Option Changes

Call `process()` again whenever options change. The engine caches image measurements, so re-processing with the same logos but different `baseSize` or `scaleFactor` is synchronous (no network requests):

```ts theme={null}
// First call: loads images from network
engine.process({ logos: ["/logo.svg"], baseSize: 48 });

// Later: re-normalizes from cache (synchronous)
engine.process({ logos: ["/logo.svg"], baseSize: 96 });
```

The cache is invalidated when `contrastThreshold`, `densityAware`, or `backgroundColor` change, since these affect the measurement itself.

## Web Components Example

```ts theme={null}
import { createLogoSoup, getVisualCenterTransform } from "@sanity-labs/logo-soup";
import type { ProcessOptions, LogoSoupState } from "@sanity-labs/logo-soup";

class LogoSoupElement extends HTMLElement {
  private engine = createLogoSoup();
  private unsubscribe: (() => void) | null = null;

  static get observedAttributes() {
    return ["base-size", "scale-factor"];
  }

  connectedCallback() {
    this.unsubscribe = this.engine.subscribe(() => this.render());
    this.update();
  }

  disconnectedCallback() {
    this.unsubscribe?.();
    this.engine.destroy();
  }

  attributeChangedCallback() {
    this.update();
  }

  set logos(value: ProcessOptions["logos"]) {
    this._logos = value;
    this.update();
  }

  private _logos: ProcessOptions["logos"] = [];

  private update() {
    this.engine.process({
      logos: this._logos,
      baseSize: Number(this.getAttribute("base-size")) || 48,
      scaleFactor: Number(this.getAttribute("scale-factor")) || 0.5,
    });
  }

  private render() {
    const { status, normalizedLogos } = this.engine.getSnapshot();
    if (status !== "ready") return;

    this.innerHTML = normalizedLogos
      .map((logo) => {
        const transform = getVisualCenterTransform(logo, "visual-center-y");
        return `<img
          src="${logo.src}" alt="${logo.alt}"
          width="${logo.normalizedWidth}" height="${logo.normalizedHeight}"
          style="display:inline-block;margin:0 14px;transform:${transform ?? "none"}"
        />`;
      })
      .join("");
  }
}

customElements.define("logo-soup", LogoSoupElement);
```

Usage:

```html theme={null}
<logo-soup base-size="48" scale-factor="0.5"></logo-soup>

<script>
  document.querySelector("logo-soup").logos = [
    { src: "/logos/acme.svg", alt: "Acme Corp" },
    { src: "/logos/globex.svg", alt: "Globex" },
  ];
</script>
```

## Integrating with Other Frameworks

The `subscribe`/`getSnapshot` shape is designed to plug into any reactivity system. If your framework isn't directly supported, the pattern is:

1. Create an engine with `createLogoSoup()`
2. Subscribe to changes and push snapshots into your framework's reactive primitive
3. Call `process()` when options change
4. Call `destroy()` on teardown

```ts theme={null}
// Pseudocode for any framework:
const engine = createLogoSoup();

const unsubscribe = engine.subscribe(() => {
  const snapshot = engine.getSnapshot();
  yourFramework.setState(snapshot); // Push into your reactive system
});

// When options change:
engine.process(newOptions);

// On teardown:
unsubscribe();
engine.destroy();
```

This is exactly what the React, Vue, Svelte, Solid, and Angular adapters do, each in \~30-80 lines of framework-specific code.


# Vue
Source: https://logo-soup.sanity.dev/docs/frameworks/vue

Use Logo Soup with Vue 3.5+ via the useLogoSoup composable.

## Install

```bash theme={null}
npm install @sanity-labs/logo-soup
```

Requires Vue 3.5 or later.

## useLogoSoup Composable

```vue theme={null}
<script setup>
import { ref } from "vue";
import { useLogoSoup } from "@sanity-labs/logo-soup/vue";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

const logos = ref([
  { src: "/logos/acme.svg", alt: "Acme Corp" },
  { src: "/logos/globex.svg", alt: "Globex" },
  { src: "/logos/initech.svg", alt: "Initech" },
]);

const { isLoading, isReady, normalizedLogos, error } = useLogoSoup({
  logos,
  baseSize: 48,
  scaleFactor: 0.5,
});
</script>

<template>
  <div v-if="error">Error: {{ error.message }}</div>
  <div v-else-if="isReady" style="text-align: center">
    <img
      v-for="logo in normalizedLogos"
      :key="logo.src"
      :src="logo.croppedSrc || logo.src"
      :alt="logo.alt"
      :width="logo.normalizedWidth"
      :height="logo.normalizedHeight"
      :style="{
        transform: getVisualCenterTransform(logo, 'visual-center-y'),
        display: 'inline-block',
        margin: '0 14px',
      }"
    />
  </div>
</template>
```

## Reactive Options

Every option accepts a plain value, a `ref`, or a getter function (`MaybeRefOrGetter`). The composable auto-tracks dependencies via `watchEffect` and re-processes whenever any option changes.

```vue theme={null}
<script setup>
import { ref, computed } from "vue";
import { useLogoSoup } from "@sanity-labs/logo-soup/vue";

const logos = ref(["/logos/acme.svg", "/logos/globex.svg"]);
const baseSize = ref(48);
const isDark = ref(false);

const backgroundColor = computed(() => (isDark.value ? "#1a1a1a" : "#ffffff"));

const { isReady, normalizedLogos } = useLogoSoup({
  logos,
  baseSize,
  backgroundColor,
  densityAware: true,
  densityFactor: 0.5,
});

function addLogo(src: string) {
  logos.value = [...logos.value, src];
  // The composable automatically re-processes
}
</script>
```

### Options Type

```ts theme={null}
type UseLogoSoupOptions = {
  logos: MaybeRefOrGetter<(string | LogoSource)[]>;
  baseSize?: MaybeRefOrGetter<number | undefined>;
  scaleFactor?: MaybeRefOrGetter<number | undefined>;
  contrastThreshold?: MaybeRefOrGetter<number | undefined>;
  densityAware?: MaybeRefOrGetter<boolean | undefined>;
  densityFactor?: MaybeRefOrGetter<number | undefined>;
  cropToContent?: MaybeRefOrGetter<boolean | undefined>;
  backgroundColor?: MaybeRefOrGetter<BackgroundColor | undefined>;
};
```

All [shared options](/options) are supported. Each is unwrapped with Vue's `toValue()` internally.

## Return Value

| Property          | Type                            | Description                           |
| ----------------- | ------------------------------- | ------------------------------------- |
| `state`           | `ShallowRef<LogoSoupState>`     | Raw reactive state from the engine    |
| `isLoading`       | `ComputedRef<boolean>`          | `true` while images are being loaded  |
| `isReady`         | `ComputedRef<boolean>`          | `true` when normalization is complete |
| `normalizedLogos` | `ComputedRef<NormalizedLogo[]>` | The processed logos                   |
| `error`           | `ComputedRef<Error \| null>`    | Set if all images fail to load        |

All return values are reactive. Reading them in a template or `watchEffect` automatically tracks changes.

## Visual Center Alignment

Apply visual center alignment with the `getVisualCenterTransform` helper from the core package:

```vue theme={null}
<script setup>
import { useLogoSoup } from "@sanity-labs/logo-soup/vue";
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

const { normalizedLogos } = useLogoSoup({ logos: ["/logo.svg"] });
</script>

<template>
  <img
    v-for="logo in normalizedLogos"
    :key="logo.src"
    :src="logo.src"
    :style="{ transform: getVisualCenterTransform(logo, 'visual-center-y') }"
  />
</template>
```

## Using in Effect Scopes

The composable uses `onScopeDispose` (not `onUnmounted`) for cleanup, so it works correctly inside any Vue effect scope, not just components. This means you can use it in composables that create their own `effectScope`:

```ts theme={null}
import { effectScope } from "vue";
import { useLogoSoup } from "@sanity-labs/logo-soup/vue";

const scope = effectScope();

const result = scope.run(() => {
  return useLogoSoup({ logos: ["/logo.svg"] });
});

// Later: clean up the engine
scope.stop();
```

## How It Works Under the Hood

The Vue adapter creates a core `createLogoSoup` engine instance and bridges it to Vue's reactivity system:

* **`shallowRef`** holds the engine's state snapshot (not `ref`, since the snapshot is an immutable object that doesn't need deep reactivity)
* **`watchEffect`** auto-tracks which options are read and re-runs `engine.process()` when they change
* **`onScopeDispose`** unsubscribes and destroys the engine when the scope is torn down
* **`computed`** refs derive convenience properties (`isLoading`, `isReady`, etc.) from the shallow ref


# How It Works
Source: https://logo-soup.sanity.dev/docs/how-it-works

Content detection, normalization math, density compensation, and irradiation correction explained.

Logo Soup processes each logo through four stages, all running client-side on a `<canvas>` element. No server, no AI, fully deterministic.

## 1. Content Detection

Most logos have invisible padding, transparent borders, or solid-color backgrounds baked into the image file. Before normalizing sizes, Logo Soup needs to find where the actual content is.

### The process

1. The image is drawn onto an off-screen canvas, downscaled to a pixel budget of \~2,048 pixels (for performance)
2. The perimeter pixels are analyzed to determine the background — either transparent or the dominant color along the edges
3. Every pixel is then classified as "content" or "background" based on contrast distance from the detected background

### Transparent vs opaque backgrounds

* **Transparent logos** (PNGs/SVGs with alpha): pixels with alpha below the `contrastThreshold` are ignored. Content is everything with meaningful opacity.
* **Opaque logos** (JPEGs, logos on solid backgrounds): the engine samples the image perimeter using a color histogram (quantized to 8-level buckets) to find the dominant background color. Pixels within `contrastThreshold` RGB distance of this color are treated as background.

You can override the auto-detection by providing `backgroundColor` explicitly, which is recommended for opaque logos on known backgrounds.

### Output

Content detection produces a `contentBox` (the tight bounding rectangle around all detected content pixels) and a `visualCenter` (the weighted center of mass of all content pixels).

## 2. Aspect Ratio Normalization

This is the core of the "logo soup" problem. Given a set of logos with wildly different aspect ratios, how do you make them look balanced together?

Logo Soup uses [Dan Paquette's technique](https://www.sanity.io/blog/the-logo-soup-problem):

```
normalizedWidth = aspectRatio ^ scaleFactor × baseSize
```

The `scaleFactor` parameter controls the balance between width uniformity and height uniformity:

| `scaleFactor` | Effect                                     | Math                                            |
| ------------- | ------------------------------------------ | ----------------------------------------------- |
| `0`           | All logos get the same width (`baseSize`)  | `ratio^0 = 1`, so `width = baseSize` for all    |
| `1`           | All logos get the same height (`baseSize`) | `ratio^1 × baseSize / ratio = baseSize` for all |
| `0.5`         | Balanced — neither too wide nor too tall   | Square root dampens extreme ratios              |

The default `0.5` works well for most logo sets. It's the geometric mean between uniform-width and uniform-height, producing visually balanced results regardless of whether your set has more wide or tall logos.

### Content box awareness

Normalization uses the `contentBox` dimensions (not the original image dimensions) when available. This means padding baked into image files doesn't affect the computed size.

## 3. Density Compensation

Even after size normalization, logos can look unbalanced because of differences in visual weight. A dense, solid wordmark (like "SAMSUNG") looks heavier than a thin, airy logo (like the Nike swoosh) at the same pixel dimensions.

### Measuring density

During content detection, the engine also computes a `pixelDensity` value (0 to 1) for each logo:

```
pixelDensity = coverageRatio × averageOpacity
```

Where:

* `coverageRatio` = fraction of pixels within the content box that are classified as content
* `averageOpacity` = average opacity of those content pixels (normalized 0–1)

A solid, blocky logo has high coverage and high opacity → high density. A thin logo with lots of whitespace has low coverage → low density.

### Applying compensation

The density compensation scales logos inversely to their density:

```
densityScale = (1 / (pixelDensity / referenceDensity)) ^ (densityFactor × 0.5)
```

The `referenceDensity` is `0.35` (a typical logo density). Logos denser than this get scaled down; lighter logos get scaled up. The scale is clamped to 0.5×–2× to prevent extreme adjustments.

The `densityFactor` option (default `0.5`) controls how strongly this affects the result. Set it to `0` to disable, or increase toward `1` for stronger compensation.

## 4. Irradiation Compensation

The [Helmholtz irradiation illusion](https://en.wikipedia.org/wiki/Irradiation_illusion) is an optical effect where light content on dark backgrounds appears larger and bolder than it actually is. This matters when displaying logos in dark mode.

### The effect

A white logo on a black background "blooms" — it appears to take up more visual space than the same logo in black on white. The effect is stronger for:

* **Darker backgrounds** (higher contrast)
* **Denser logos** (more surface area to "bloom")

### The correction

When `backgroundColor` is provided (or auto-detected from opaque images), the engine computes a `backgroundLuminance` value and applies a small scale-down:

```
irradiationScale = 1 - darkness × density × 0.08
```

Where `darkness = 1 - backgroundLuminance` and `density` is the logo's pixel density.

This is a subtle effect (typically 1–4% reduction), but it measurably improves visual balance in dark mode. It only applies to opaque images where the background luminance can be determined — transparent logos are unaffected.

<Info>
  References:

  * [Helmholtz irradiation illusion (1860s)](https://en.wikipedia.org/wiki/Irradiation_illusion)
  * [Jano Garcia's research compilation](https://gist.github.com/janogarcia/e9f57cd18ca85756743f81d9692764b7)
  * [Adam Argyle: Adjust perceived typeface weight for dark mode](https://nerdy.dev/adjust-perceived-typepace-weight-for-dark-mode-without-layout-shift)
</Info>

## 5. Visual Center Alignment

After normalization, logos can still appear misaligned because their visual weight isn't centered. Consider a logo like the Airbnb symbol — the geometric center of the bounding box isn't where your eye perceives the center to be.

### Computing the visual center

During content detection, the engine computes a weighted center of mass across all content pixels. Each pixel's weight is proportional to its contrast distance from the background (or its alpha for transparent logos). This gives more influence to high-contrast, visually prominent pixels.

The result is a `visualCenter` with `offsetX` and `offsetY` values representing the displacement from the geometric center of the content box.

### Applying alignment

The `getVisualCenterTransform` helper computes a CSS `translate()` that compensates for this offset:

```ts theme={null}
import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

const transform = getVisualCenterTransform(logo, "visual-center-y");
// Returns "translate(0px, -2.3px)" or undefined
```

The `alignBy` modes control which axes are compensated:

* `"bounds"` — No compensation, align by geometric center
* `"visual-center"` — Compensate on both X and Y
* `"visual-center-x"` — Compensate horizontally only
* `"visual-center-y"` — Compensate vertically only (default)

The default `"visual-center-y"` is best for horizontal logo rows where vertical balance matters most. Horizontal offsets are usually less noticeable because logos have natural spacing between them.

## Performance

All processing happens on the client using an off-screen `<canvas>` element. Key optimizations:

* **Downscaling**: Images are drawn at \~2,048 total pixels regardless of source resolution. A 2000×1000 image is analyzed at \~45×23 pixels. This makes measurement O(1) relative to image resolution.
* **Reusable canvases**: The engine maintains pooled canvas contexts to avoid repeated DOM allocation.
* **Image caching**: Once an image is loaded and measured, the result is cached by URL. Re-processing with different `baseSize` or `scaleFactor` reuses cached measurements without network requests.
* **Cancellation**: If `process()` is called while a previous run is still loading, the in-flight work is cancelled. Only the latest call's results are emitted.
* **Blob URL management**: Cropped images use `URL.createObjectURL()` and are properly revoked on cache invalidation and engine destruction.


# Introduction
Source: https://logo-soup.sanity.dev/docs/introduction

A tiny framework-agnostic library that makes logos look good together.

# 🍜 Logo Soup

Real-world logos are messy. Some have padding, some don't. Some are dense and blocky, others are thin and airy. Put them in a row and they look chaotic. Logo Soup fixes this automatically.

<LogoSoupDemo />

## What it does

Logo Soup analyzes each logo image on a `<canvas>` and normalizes them so they appear visually balanced when displayed together. No server, no AI, fully deterministic.

1. **Content Detection** — Finds the true boundaries of each logo, ignoring whitespace and padding baked into the image
2. **Aspect Ratio Normalization** — Balances wide and tall logos so neither dominates
3. **Density Compensation** — Measures visual weight so dense/bold logos don't overpower light/thin ones
4. **Irradiation Compensation** — Adjusts for the optical illusion where light content on dark backgrounds appears larger

<CardGroup>
  <Card title="Read the deep-dive" icon="newspaper" href="https://www.sanity.io/blog/the-logo-soup-problem">
    The full story behind the problem and the math behind the solution.
  </Card>

  <Card title="Try the playground" icon="play" href="https://logo-soup.sanity.dev">
    Interactive Storybook with real logos and tunable parameters.
  </Card>
</CardGroup>

## Framework support

Logo Soup is a single npm package with subpath exports for every major framework:

<FrameworkGrid />

## Architecture

The library is built around a framework-agnostic core engine (`createLogoSoup`) that handles all image loading, measurement, normalization, caching, and cancellation. Each framework adapter is a thin wrapper (30–80 lines) that bridges the engine's `subscribe`/`getSnapshot` interface into the framework's reactivity model.

```
@sanity-labs/logo-soup          → Core engine, types, utilities
@sanity-labs/logo-soup/react    → useLogoSoup hook + LogoSoup component
@sanity-labs/logo-soup/vue      → useLogoSoup composable
@sanity-labs/logo-soup/svelte   → createLogoSoup (runes-compatible)
@sanity-labs/logo-soup/solid    → useLogoSoup primitive
@sanity-labs/logo-soup/angular  → LogoSoupService (Injectable)
@sanity-labs/logo-soup/node     → measureImage / measureImages (server-side)
```

Tree-shaking ensures a React consumer never pulls in Vue/Svelte/Solid/Angular code, and vice versa. The [Node.js adapter](/frameworks/node) lets you pre-compute measurements at build time or in API routes, so clients skip all canvas work. Need a framework we don't support? [Build your own adapter](/frameworks/custom) in 20–40 lines.


# Options Reference
Source: https://logo-soup.sanity.dev/docs/options

All configuration options for Logo Soup, shared across every framework.

These options are shared across every framework adapter. They're passed as component props (React), composable args (Vue), or `process()` options (Svelte/Solid/Angular/Vanilla).

## Core Options

### `logos`

<ParamField type="(string | { src: string; alt?: string })[]">
  Array of logo URLs or objects with `src` and optional `alt` text. Use objects to provide accessible alt text for each logo.

  ```ts theme={null}
  // Plain strings
  const logos = ["/logos/acme.svg", "/logos/globex.svg"];

  // Objects with alt text (recommended)
  const logos = [
    { src: "/logos/acme.svg", alt: "Acme Corp" },
    { src: "/logos/globex.svg", alt: "Globex" },
  ];

  // Mixed
  const logos = [
    "/logos/acme.svg",
    { src: "/logos/globex.svg", alt: "Globex" },
  ];
  ```
</ParamField>

### `baseSize`

<ParamField type="number">
  Target size for logos in pixels. This is the baseline that all normalization is relative to. Larger values produce larger logos.

  ```tsx theme={null}
  <LogoSoup logos={logos} baseSize={64} />
  ```
</ParamField>

### `scaleFactor`

<ParamField type="number">
  Controls how logos with different aspect ratios are balanced. This uses [Dan Paquette's technique](https://www.sanity.io/blog/the-logo-soup-problem) where the normalized width is calculated as `aspectRatio ^ scaleFactor * baseSize`.

  | Value | Behavior                      | When to use                          |
  | ----- | ----------------------------- | ------------------------------------ |
  | `0`   | All logos get the same width  | When you want a uniform grid         |
  | `0.5` | Balanced (default)            | Most use cases                       |
  | `1`   | All logos get the same height | When vertical alignment matters most |

  Imagine two logos: Logo A is wide (200×100) and Logo B is tall (100×200).

  **`scaleFactor = 0`** — Same width for all:

  * Logo A: 48×24 (short)
  * Logo B: 48×96 (very tall)

  **`scaleFactor = 1`** — Same height for all:

  * Logo A: 96×48 (very wide)
  * Logo B: 24×48 (narrow)

  **`scaleFactor = 0.5`** — Balanced:

  * Neither gets too wide nor too tall
  * Looks most natural
</ParamField>

### `densityAware`

<ParamField type="boolean">
  When enabled, Logo Soup measures the "visual weight" (pixel density) of each logo and adjusts sizing accordingly. Dense, solid logos get scaled down. Light, thin logos get scaled up.

  Set to `false` to disable density compensation entirely.

  ```tsx theme={null}
  // Disable density compensation
  <LogoSoup logos={logos} densityAware={false} />
  ```
</ParamField>

### `densityFactor`

<ParamField type="number">
  Controls how strongly density affects the result. Only applies when `densityAware` is `true`.

  | Value | Effect                                                  |
  | ----- | ------------------------------------------------------- |
  | `0`   | No density compensation (same as `densityAware: false`) |
  | `0.5` | Moderate compensation (default)                         |
  | `1`   | Strong compensation                                     |

  ```tsx theme={null}
  // Stronger density compensation
  <LogoSoup logos={logos} densityFactor={0.8} />
  ```
</ParamField>

### `cropToContent`

<ParamField type="boolean">
  When enabled, logos are cropped to their detected content bounds and re-rendered as blob URLs. This removes any whitespace or padding baked into the original image files.

  The cropped images are available as `logo.croppedSrc` on each `NormalizedLogo` object.

  ```tsx theme={null}
  <LogoSoup logos={logos} cropToContent />
  ```

  <Note>
    Cropping creates blob URLs that are cleaned up when the engine is destroyed. Don't store `croppedSrc` values beyond the engine's lifetime.
  </Note>
</ParamField>

### `contrastThreshold`

<ParamField type="number">
  Minimum contrast distance (in RGB space) for a pixel to be considered "content" during content detection. Higher values ignore more low-contrast details near the background color.

  You rarely need to change this. Increase it if logos with very subtle gradients or shadows are getting incorrect bounds.
</ParamField>

### `backgroundColor`

<ParamField type="string | [number, number, number]">
  The background color the logos will be displayed on. Used for two things:

  1. **Contrast detection** on opaque logos (logos without transparency) — the engine needs to know the background to distinguish content from the background
  2. **Irradiation compensation** — light logos on dark backgrounds appear optically larger; this option enables the correction

  Accepts CSS color strings (`"#1a1a1a"`, `"rgb(26, 26, 26)"`, `"hsl(0, 0%, 10%)"`) or RGB tuples (`[26, 26, 26]`).

  When omitted, the engine auto-detects the background by analyzing the perimeter pixels of each image. This works well for logos with transparent backgrounds. For logos on opaque backgrounds (like JPEGs), providing the actual background color produces better results.

  ```tsx theme={null}
  // Dark mode
  <LogoSoup logos={logos} backgroundColor="#1a1a1a" />

  // RGB tuple
  <LogoSoup logos={logos} backgroundColor={[26, 26, 26]} />
  ```
</ParamField>

## React Component Options

These options are only available on the React `<LogoSoup>` component.

### `gap`

<ParamField type="number | string">
  Space between logos. Accepts a pixel number or a CSS string value.

  ```tsx theme={null}
  <LogoSoup logos={logos} gap={24} />
  <LogoSoup logos={logos} gap="1.5rem" />
  ```
</ParamField>

### `alignBy`

<ParamField type="AlignmentMode">
  How to align logos within the row. See [Alignment Modes](#alignment-modes) below.

  ```tsx theme={null}
  <LogoSoup logos={logos} alignBy="visual-center" />
  ```
</ParamField>

### `renderImage`

<ParamField type="(props: ImageRenderProps) => ReactNode">
  Custom image renderer. Receives all standard `<img>` attributes (`src`, `alt`, `width`, `height`, `style`). Use this to integrate with Next.js Image, add lazy loading, or fully control the `<img>` output.

  ```tsx theme={null}
  import Image from "next/image";

  <LogoSoup
    logos={logos}
    renderImage={(props) => (
      <Image src={props.src} alt={props.alt} width={props.width} height={props.height} />
    )}
  />
  ```
</ParamField>

### `className`

<ParamField type="string">
  CSS class name applied to the container `<div>`.
</ParamField>

### `style`

<ParamField type="CSSProperties">
  Inline styles applied to the container `<div>`. Merged with the default container styles (`text-align: center`, `text-wrap: balance`).
</ParamField>

### `onNormalized`

<ParamField type="(logos: NormalizedLogo[]) => void">
  Callback fired when normalization completes. Receives the array of normalized logos. Useful for analytics, debugging, or syncing state with external systems.

  ```tsx theme={null}
  <LogoSoup
    logos={logos}
    onNormalized={(normalized) => {
      console.log("Normalized:", normalized.length, "logos");
    }}
  />
  ```
</ParamField>

## Alignment Modes

Used with the `alignBy` prop (React component) or `getVisualCenterTransform` helper (all frameworks).

| Mode                | Description                                                                                                                                   |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| `"bounds"`          | Align by geometric center of the bounding box. No transform applied.                                                                          |
| `"visual-center"`   | Align by visual weight center on both axes. Compensates for asymmetric logos where the "heavy" part isn't centered.                           |
| `"visual-center-x"` | Visual center horizontally only. Vertical alignment uses bounds.                                                                              |
| `"visual-center-y"` | Visual center vertically only (default). Horizontal alignment uses bounds. Best for horizontal logo rows where vertical balance matters most. |

### Using with the hook/composable

When building custom layouts (not using the React `<LogoSoup>` component), apply alignment with `getVisualCenterTransform`:

<CodeGroup>
  ```tsx React theme={null}
  import { getVisualCenterTransform } from "@sanity-labs/logo-soup";

  const transform = getVisualCenterTransform(logo, "visual-center-y");
  // Returns "translate(0px, -2.3px)" or undefined
  ```

  ```vue Vue theme={null}
  <img :style="{ transform: getVisualCenterTransform(logo, 'visual-center-y') }" />
  ```

  ```svelte Svelte theme={null}
  <img style:transform={getVisualCenterTransform(logo, "visual-center-y")} />
  ```

  ```tsx Solid theme={null}
  style={{ transform: getVisualCenterTransform(logo, "visual-center-y") ?? "none" }}
  ```

  ```typescript Angular theme={null}
  [style.transform]="getVisualCenterTransform(logo, alignBy())"
  ```
</CodeGroup>

## NormalizedLogo Object

Each processed logo is a `NormalizedLogo` with these properties:

| Property           | Type            | Description                                                     |
| ------------------ | --------------- | --------------------------------------------------------------- |
| `src`              | `string`        | Original image URL                                              |
| `alt`              | `string`        | Alt text (empty string if not provided)                         |
| `originalWidth`    | `number`        | Natural width of the source image                               |
| `originalHeight`   | `number`        | Natural height of the source image                              |
| `normalizedWidth`  | `number`        | Computed display width after normalization                      |
| `normalizedHeight` | `number`        | Computed display height after normalization                     |
| `aspectRatio`      | `number`        | Content aspect ratio (width / height)                           |
| `contentBox`       | `BoundingBox?`  | Detected content bounds within the image                        |
| `pixelDensity`     | `number?`       | Measured visual density (0–1)                                   |
| `visualCenter`     | `VisualCenter?` | Visual weight center with offset from geometric center          |
| `croppedSrc`       | `string?`       | Blob URL of the cropped image (when `cropToContent` is enabled) |


# Performance
Source: https://logo-soup.sanity.dev/docs/performance

How Logo Soup stays fast, what we measure, and how to optimize for your use case.

Logo Soup runs entirely client-side, analyzing pixel data on a `<canvas>`. That means performance matters. Here's what we did to make it fast, how we measure it, and what you can do to keep it that way.

## Optimization techniques

### Single-pass pixel scanning

Early versions ran three separate pixel scans per logo: one for the bounding box, one for the visual center, and one for pixel density. Each scan created a new canvas, drew the image at full resolution, then walked every pixel. For a 400x400 image, that's 160k pixels, three times over.

The current implementation collapses all three into a single pass over a `Uint32Array`:

```ts theme={null}
for (let i = 0; i < pixelCount; i++) {
  const pixel = data32[i]!;

  // unpack RGBA from Uint32Array (little-endian)
  const a = pixel >>> 24;
  if (a <= contrastThreshold) continue;

  const r = pixel & 0xff;
  const g = (pixel >>> 8) & 0xff;
  const b = (pixel >>> 16) & 0xff;

  // squared euclidean distance from background
  const distSq = (r - bgR) ** 2 + (g - bgG) ** 2 + (b - bgB) ** 2;
  if (distSq < contrastDistanceSq) continue;

  // recover x,y from flat index
  const x = i % sw;
  const y = (i - x) / sw;

  // accumulate weighted visual center
  totalWeight += distSq * a;
  weightedX += (x + 0.5) * distSq * a;
  weightedY += (y + 0.5) * distSq * a;
}
```

One loop computes the content bounds, weighted visual center, and pixel density simultaneously. Combined with the downsampling and canvas reuse described below, this cut content detection from **1.4ms to \~37us per logo** (38x faster) and full mount from **29ms to \~850us for 20 logos** (35x faster).

### Downsampling

Source images are drawn onto a canvas at a fixed pixel budget of \~2,048 total pixels, regardless of the original resolution. A 2000x1000 image is analyzed at roughly 45x23 pixels. This makes measurement cost O(1) relative to image resolution while preserving enough detail for accurate content detection.

### Canvas reuse

Instead of creating a new `<canvas>` element for each measurement, the engine maintains pooled canvas contexts at module level. The canvas is only resized when the dimensions change, otherwise it's cleared and reused. This avoids repeated DOM allocation and garbage collection pressure.

### Result caching

Once an image is loaded and measured, the `MeasurementResult` is cached by URL. Changing `baseSize` or `scaleFactor` (which only affect normalization math, not pixel analysis) reuses cached measurements without re-scanning. The cache is only invalidated when `contrastThreshold`, `densityAware`, or `backgroundColor` change, since those affect the pixel scan itself.

### Cancellation

If `process()` is called while a previous run is still loading images, the in-flight work is cancelled and only the latest call's results are emitted. This prevents wasted work during rapid option changes.

## Benchmarks

Every pull request automatically runs a benchmark suite against real SVG logos from the test set. Here are typical numbers from CI:

| Benchmark                           |    Time |
| :---------------------------------- | ------: |
| Content detection (1 logo)          |  \~36us |
| Render pass (20 logos)              |   \~1us |
| Full mount, no detection (20 logos) | \~3.5us |
| Full mount, defaults (20 logos)     | \~880us |

Detection dominates the cost. Once measurements are cached, subsequent layout updates (changing `baseSize`, `scaleFactor`, or `alignBy`) are effectively free -- nearly 400x faster than a full mount.

### Feature cost breakdown

The CI suite also measures how expensive individual features are relative to having them off:

| Feature                                    |      On |    Off | Cost                               |
| :----------------------------------------- | ------: | -----: | :--------------------------------- |
| `densityAware`                             |  \~35us | \~34us | Negligible (same pass)             |
| `alignBy: "visual-center-y"` vs `"bounds"` |   \~1us | \~59ns | 18x (but both are sub-microsecond) |
| `cropToContent`                            |   \~2ms |  \~0ns | 2ms (canvas crop + blob URL)       |
| Layout update: full mount vs cached        | \~880us |  \~2us | 400x (pixel scan vs pure math)     |

## CI regression detection

The benchmark suite uses [Welch's t-test](https://en.wikipedia.org/wiki/Welch%27s_t-test) to compare HEAD against the base branch on every PR. A regression is flagged only when all three conditions are met:

1. The change is **statistically significant** (p \< 0.05)
2. The relative change exceeds **5%**
3. The absolute change exceeds **100us**

This avoids false positives from measurement noise while catching real regressions. The comparison table and feature cost breakdown are posted directly on the PR as a comment, along with a link to the full CI job logs.

<Tip>
  You can run benchmarks locally with `bun run bench`. The suite uses `@napi-rs/canvas` and `@happy-dom/global-registrator` to run the same pixel scanning code outside a browser.
</Tip>

## Tips for your application

### Provide `backgroundColor` for opaque logos

When Logo Soup doesn't know the background color, it samples the image perimeter to auto-detect it. If you know the background (e.g., your page is white), pass `backgroundColor` explicitly to skip the detection step and improve accuracy.

### Disable features you don't need

Each feature has a measurable cost. If you don't need density compensation, visual center alignment, or content cropping, turning them off saves work:

| Feature                | Effect when disabled                                       |
| :--------------------- | :--------------------------------------------------------- |
| `densityAware: false`  | Skips density computation during pixel scan                |
| `alignBy: "bounds"`    | Skips visual center transform calculation                  |
| `cropToContent: false` | Skips canvas crop and blob URL creation (saves \~2ms/logo) |

### Cache-friendly option changes

Changing `baseSize`, `scaleFactor`, `densityFactor`, or `alignBy` reuses cached measurements and only runs cheap normalization math. Changing `contrastThreshold`, `densityAware`, or `backgroundColor` invalidates the cache and triggers a full re-scan. Structure your UI so the expensive options are set once and the cheap ones are interactive.

### Keep logo sets reasonable

The library processes logos in parallel using `Promise.allSettled`, but each logo still needs its own pixel scan on first load. For very large sets (50+ logos), consider lazy-loading logos that are off-screen.

## Server-side pre-computation

If you want to skip client-side pixel scanning entirely, the [Node.js adapter](/frameworks/node) lets you pre-compute `MeasurementResult` data at build time or in API routes using `@napi-rs/canvas`. The client then calls `createNormalizedLogo` with the pre-computed data -- pure math, no canvas, no async.

```ts theme={null}
// Build script
import { measureImages } from "@sanity-labs/logo-soup/node";
const measurements = await measureImages(["./logos/acme.svg", "./logos/globex.svg"]);

// Client
import { createNormalizedLogo } from "@sanity-labs/logo-soup";
const normalized = createNormalizedLogo(source, measurements[0], 48, 0.5, 0.5);
```

See the [Node.js adapter docs](/frameworks/node) for the full workflow.


# Quickstart
Source: https://logo-soup.sanity.dev/docs/quickstart

Install Logo Soup and get normalized logos rendering in under a minute.

## Install

<CodeGroup>
  ```bash npm theme={null}
  npm install @sanity-labs/logo-soup
  ```

  ```bash pnpm theme={null}
  pnpm add @sanity-labs/logo-soup
  ```

  ```bash yarn theme={null}
  yarn add @sanity-labs/logo-soup
  ```

  ```bash bun theme={null}
  bun add @sanity-labs/logo-soup
  ```
</CodeGroup>

## Pick your framework

<Tabs>
  <Tab title="React">
    The fastest way is the pre-built `<LogoSoup>` component:

    ```tsx theme={null}
    import { LogoSoup } from "@sanity-labs/logo-soup/react";

    function LogoStrip() {
      return (
        <LogoSoup
          logos={[
            { src: "/logos/acme.svg", alt: "Acme Corp" },
            { src: "/logos/globex.svg", alt: "Globex" },
            { src: "/logos/initech.svg", alt: "Initech" },
          ]}
        />
      );
    }
    ```

    That's it. Logo Soup analyzes each image and renders them visually balanced.

    For custom layouts, use the `useLogoSoup` hook instead — see the [React guide](/frameworks/react).
  </Tab>

  <Tab title="Vue">
    ```vue theme={null}
    <script setup>
    import { ref } from "vue";
    import { useLogoSoup } from "@sanity-labs/logo-soup/vue";

    const logos = ref(["/logos/acme.svg", "/logos/globex.svg"]);
    const { isReady, normalizedLogos } = useLogoSoup({ logos });
    </script>

    <template>
      <div v-if="isReady">
        <img
          v-for="logo in normalizedLogos"
          :key="logo.src"
          :src="logo.src"
          :alt="logo.alt"
          :width="logo.normalizedWidth"
          :height="logo.normalizedHeight"
        />
      </div>
    </template>
    ```

    See the [Vue guide](/frameworks/vue) for reactive options and visual center alignment.
  </Tab>

  <Tab title="Svelte">
    ```svelte theme={null}
    <script>
      import { createLogoSoup } from "@sanity-labs/logo-soup/svelte";

      let { logos = [] } = $props();
      const soup = createLogoSoup();

      $effect(() => {
        soup.process({ logos });
      });

      $effect(() => {
        return () => soup.destroy();
      });
    </script>

    {#if soup.isReady}
      {#each soup.normalizedLogos as logo (logo.src)}
        <img
          src={logo.src}
          alt={logo.alt}
          width={logo.normalizedWidth}
          height={logo.normalizedHeight}
        />
      {/each}
    {/if}
    ```

    See the [Svelte guide](/frameworks/svelte) for more details on runes integration.
  </Tab>

  <Tab title="Solid">
    ```tsx theme={null}
    import { useLogoSoup } from "@sanity-labs/logo-soup/solid";
    import { For, Show } from "solid-js";

    function LogoStrip() {
      const result = useLogoSoup(() => ({
        logos: ["/logos/acme.svg", "/logos/globex.svg"],
      }));

      return (
        <Show when={result.isReady}>
          <For each={result.normalizedLogos}>
            {(logo) => (
              <img
                src={logo.src}
                alt={logo.alt}
                width={logo.normalizedWidth}
                height={logo.normalizedHeight}
              />
            )}
          </For>
        </Show>
      );
    }
    ```

    See the [Solid guide](/frameworks/solid) for the reactive getter pattern.
  </Tab>

  <Tab title="Angular">
    ```typescript theme={null}
    import { Component, input, effect, inject } from "@angular/core";
    import { LogoSoupService } from "@sanity-labs/logo-soup/angular";

    @Component({
      selector: "logo-strip",
      standalone: true,
      providers: [LogoSoupService],
      template: `
        @for (logo of service.state().normalizedLogos; track logo.src) {
          <img [src]="logo.src" [alt]="logo.alt"
               [width]="logo.normalizedWidth"
               [height]="logo.normalizedHeight" />
        }
      `,
    })
    export class LogoStripComponent {
      protected service = inject(LogoSoupService);
      logos = input.required<string[]>();

      constructor() {
        effect(() => {
          this.service.process({ logos: this.logos() });
        });
      }
    }
    ```

    See the [Angular guide](/frameworks/angular) for signal patterns and service scoping.
  </Tab>

  <Tab title="Vanilla JS">
    ```ts theme={null}
    import { createLogoSoup } from "@sanity-labs/logo-soup";

    const engine = createLogoSoup();

    engine.subscribe(() => {
      const { status, normalizedLogos } = engine.getSnapshot();
      if (status !== "ready") return;

      document.getElementById("logos")!.innerHTML = normalizedLogos
        .map(
          (logo) =>
            `<img src="${logo.src}" alt="${logo.alt}" width="${logo.normalizedWidth}" height="${logo.normalizedHeight}" />`
        )
        .join("");
    });

    engine.process({
      logos: ["/logos/acme.svg", "/logos/globex.svg"],
    });
    ```

    See the [Vanilla JS guide](/frameworks/vanilla) for the full engine API.
  </Tab>
</Tabs>

## Logos format

Logos can be plain URL strings or objects with `src` and optional `alt` text:

```ts theme={null}
// Plain strings
const logos = ["/logos/acme.svg", "/logos/globex.svg"];

// Objects with alt text (recommended for accessibility)
const logos = [
  { src: "/logos/acme.svg", alt: "Acme Corp" },
  { src: "/logos/globex.svg", alt: "Globex" },
];

// You can mix both
const logos = [
  "/logos/acme.svg",
  { src: "/logos/globex.svg", alt: "Globex" },
];
```

## Next steps

<CardGroup>
  <Card title="Options reference" icon="sliders" href="/options">
    Tune base size, density, scale factor, alignment, and more.
  </Card>

  <Card title="How it works" icon="microscope" href="/how-it-works">
    Content detection, normalization math, and irradiation compensation explained.
  </Card>

  <Card title="Framework guides" icon="code" href="/frameworks/react">
    Deep dives for React, Vue, Svelte, Solid, Angular, and vanilla JS.
  </Card>

  <Card title="Core engine API" icon="gear" href="/api-reference/create-logo-soup">
    Use the engine directly for unsupported frameworks or advanced use cases.
  </Card>
</CardGroup>


