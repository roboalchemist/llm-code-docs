# Source: https://www.mux.com/docs/guides/player-lazy-loading.md

# Lazy-loading Mux Player
Improve your users' page load experience by lazy-loading the Mux Player.
## Installation

### React

After [installing `@mux/mux-player-react`](/docs/guides/player-integrate-in-your-webapp), import Mux Player React Lazy from `@mux/mux-player-react/lazy`:

Depending on your bundler your import might look a little different. If you're having trouble with the import try:

* `@mux/mux-player-react/lazy`
* `@mux/mux-player-react/dist/lazy.mjs`
* `@mux/mux-player-react/dist/lazy`

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-player-react": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import MuxPlayer from \"@mux/mux-player-react/dist/lazy.mjs\"; \n\nexport default function App() {\n  return (\n    <>\n      <p style={{ backgroundColor: \"#eee\", height: \"100vh\" }}>\n        Scroll down to see Mux Player load lazily.\n      </p>\n      <MuxPlayer\n        playbackId=\"a4nOgmxGWg6gULfcBbAa00gXyfcwPnAFldF8RdsNyk8M\"\n        metadata={{\n          video_id: \"video-id-54321\",\n          video_title: \"Test video title\",\n          viewer_user_id: \"user-id-007\",\n        }}\n        style={{ aspectRatio: 16/9 }}\n      />\n    </>\n  );\n}\n",
      "active": true
    },
    "/src/index.js": {
      "code": "",
      "hidden": true
    }
  },
  "template": "react"
}
```

<Callout type="info">
  Mux Player React Lazy will not be available if you are using the hosted option
  on jsdelivr.com.
</Callout>

## Preventing cumulative layout shift

Because the player is added to the DOM after the page loads, it will cause a [cumulative layout shift](https://web.dev/cls), pushing content down and causing a jarring jump for your users. To prevent this, make sure your player has an `aspectRatio` style property. `@mux/mux-player-react/lazy` will display a placeholder with this aspect ratio while the player loads.

```jsx
<MuxPlayer
  playbackId="EcHgOK9coz5K4rjSwOkoE7Y7O01201YMIC200RI6lNxnhs"
  // without this line, the player will cause a layout shift when it loads
  style={{ aspectRatio: 16/9 }}
/>
```

## Customizing the placeholder

While Mux Player React Lazy loads, it will display a placeholder with the same background color as the player. (By default, a black background).

<Player playbackId="Wd01CoLZp2Adx00qefHtyGVPSP2h4wO33OZqR00vf7wCnQ" style={{ aspectRatio: "495 / 274", '--center-controls': 'none' }} />

If the `placeholder=` attribute is defined, the attribute's contents will display in the placeholder before load. You can generate placeholders that match your video poster with `@mux/blurup`. [See the placeholder guide to learn more](/docs/guides/player-customize-look-and-feel#provide-a-placeholder-while-the-poster-image-loads).

<Player playbackId="bXA3Oh7v22fRBU013damYqUxFK6HrmJcrI00Q00b2OSvmc" style={{ aspectRatio: "656 / 277", '--center-controls': 'none' }} />

## Defining when to load

In addition to the standard attributes that Mux Player React accepts, Mux Player React Lazy will also accept a `loading` attribute:

* `loading="page"`: Loads the player and replaces a placeholder after the page loads and the initial JavaScript bundle is executed
* `loading="viewport"`: (Default) Extends `loading="page"` by also waiting until the placeholder has entered the viewport

## Using other frameworks

If you are working in an environment that supports [dynamic imports](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/import), like [Webpack](https://webpack.js.org/guides/code-splitting/), [Rollup](https://rollupjs.org/guide/en/#code-splitting), [Parcel](https://parceljs.org/features/code-splitting/), or [many modern browsers](https://caniuse.com/es6-module-dynamic-import), you can reproduce the behavior of Mux Player React Lazy.

If you have access to a Node.js server, generate a placeholder that matches your video with `@mux/blurup`.

```js
// Server-Side
import { createBlurUp } from '@mux/blurup';

const options = {};
const muxPlaybackId = 'O6LdRc0112FEJXH00bGsN9Q31yu5EIVHTgjTKRkKtEq1k';

const getPlaceholder() = async () => {
  const { blurDataURL, aspectRatio } = await createBlurUp(muxPlaybackId, options);
  console.log(blurDataURL, aspectRatio);
  // data:image/svg+xml;charset=utf-8,<svg xmlns="http://www.w3.org/2000/svg" width="100%" ...
};
```

Then, use a dynamic import to load Mux Player. When the load is complete, replace the placeholder with the player.

```html

<div class="wrapper">
  <div class="placeholder"></div>
</div>

<script>
const wrapper = document.querySelector(".wrapper");
const placeholder = document.querySelector(".placeholder");

import("@mux/mux-player").then(() => {
  const player = document.createElement("mux-player");

  player.setAttribute("playback-id", playbackId);
  player.setAttribute("placeholder", blurUpPlaceholder);
  player.setAttribute("metadata-video-title", "Test video title");
  player.setAttribute("metadata-viewer-user-id", "user-id-007");

  wrapper.replaceChild(player, placeholder);
});
</script>

<style>
.wrapper {
  aspect-ratio: {sourceWidth} / {sourceHeight};
  width: 100%;
  position: relative;
}
mux-player, .placeholder {
  position: absolute;
  inset: 0;
}
.placeholder {
  background-image: url({blurUpPlaceholder});
  background-color: black;
  background-size: contain;
  background-repeat: no-repeat;
}
</style>

```

```svelte

<script>
  const player = import('@mux/mux-player');
</script>

<main>
  <div class="wrapper" style:aspect-ratio="{sourceWidth / sourceHeight}">
    {#await player}
      <div class="placeholder" style:background-image="url('{data.blurUpPlaceholder}')" />
    {:then}
      <mux-player
        playback-id={playbackId}
        placeholder={blurUpPlaceholder}
        metadata-video-title="Test VOD"
        metadata-viewer-user-id="user-id-007"
      />
    {/await}
  </div>
</main>

<style>
  .wrapper {
    width: 100%;
    position: relative;
  }
  mux-player, .placeholder {
    position: absolute;
    inset: 0;
  }
  .placeholder {
    background-color: black;
    background-size: contain;
    background-repeat: no-repeat;
  }
</style>


```

