# Source: https://www.mux.com/docs/guides/player-themes.md

# Choose a theme for Mux Player
Learn how to configure a new Mux Player theme
Mux Player is built on top of [Media Chrome](https://www.media-chrome.org/)
that comes with simple but powerful [theming](https://www.media-chrome.org/en/themes)
capabilities. It allows you to fully control the video player UI layout
and style but keeps the complexity of media state management out of the way.

<Callout type="warning">
  Themes are unavailable if you are using the Mux Player HTML embed through player.mux.com.
</Callout>

## Mux themes

The `minimal` and `microvideo` themes require one extra import,
then set the `theme` attribute and you're ready to go!

### Minimal theme

This theme pares down the Mux Player experience to the bare bones controls
viewers need, ideal for those that want a simpler player experience.

Here's an example of a React app using the Minimal theme.

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-player-react": "latest",
      "@mux/mux-player": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import MuxPlayer from \"@mux/mux-player-react\";\nimport \"@mux/mux-player/themes/minimal\";\n\nexport default function App() {\n  return (\n    <>\n      <MuxPlayer\n        theme=\"minimal\"\n        playbackId=\"a4nOgmxGWg6gULfcBbAa00gXyfcwPnAFldF8RdsNyk8M\"\n      />\n    </>\n  );\n}\n",
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

### Microvideo theme

This theme optimizes for shorter content that doesn't need the robust playback
controls that longer content typically requires.

Here's an example of a HTML page using the Microvideo theme.

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-player": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<script\n  type=\"module\"\n  src=\"https://cdn.jsdelivr.net/npm/player.style/microvideo/+esm\"\n></script>\n<script\n  type=\"module\"\n  src=\"https://cdn.jsdelivr.net/npm/@mux/mux-player\"\n></script>\n<mux-player\n  theme=\"microvideo\"\n  playback-id=\"a4nOgmxGWg6gULfcBbAa00gXyfcwPnAFldF8RdsNyk8M\"\n></mux-player>",
      "active": true
    },
    "/index.js": {
      "code": "\nimport '@mux/mux-player';\nimport '@mux/mux-player/themes/microvideo';\n    ",
      "hidden": true
    }
  }
}
```

### Classic theme

This theme is the classic 1.x version of Mux Player. Here's an example of a HTML page using the Classic theme.

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-player-react": "latest",
      "@mux/mux-player": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import MuxPlayer from \"@mux/mux-player-react\";\nimport \"@mux/mux-player/themes/classic\";\n\nexport default function App() {\n  return (\n    <>\n      <MuxPlayer\n        theme=\"classic\"\n        playbackId=\"a4nOgmxGWg6gULfcBbAa00gXyfcwPnAFldF8RdsNyk8M\"\n      />\n    </>\n  );\n}\n",
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

### Styling

You can use the same styling methods like explained in
[customize look and feel](/docs/guides/player-customize-look-and-feel#style-with-css).

Note that the CSS variables, CSS parts and styling guidelines are relevant to themes that ship from `@mux/mux-player/themes`. Any other Media Chrome themes created by you or a third party will not necessarily share the same CSS variables and parts.

Unlike the Mux Player default theme, these themes come with some buttons disabled by default.
However these can still be enabled by setting some CSS vars.

| Button | CSS Variable |
| --- | --- |
| Seek backward button | `--seek-backward-button: block;` |
| Seek forward button | `--seek-forward-button: block;` |
| PiP (Picture-in-Picture) button | `--pip-button: block` |

## Media Chrome themes

Mux Player uses Media Chrome themes to layout and style the UI of
the video player. Please read the
[themes documentation](https://www.media-chrome.org/en/themes)
to learn how to create a theme.

There are two ways to consume a Media Chrome theme in Mux player.

### Via an inline `<template id="mytheme">`

See the example on [Codesandbox](https://codesandbox.io/s/mux-player-tiny-theme-template-vc7d0y?file=/index.html)

### Via a custom element `<media-theme-mytheme>`

See the example on [Codesandbox](https://codesandbox.io/s/mux-player-tiny-theme-custom-element-gst24f?file=/index.html)
