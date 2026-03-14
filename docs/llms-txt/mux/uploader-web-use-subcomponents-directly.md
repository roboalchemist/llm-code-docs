# Source: https://www.mux.com/docs/guides/uploader-web-use-subcomponents-directly.md

# Compose custom UIs with subcomponents
Learn how to use Mux Uploader's various subcomponents to compose even more bespoke user experiences and designs.
Although Mux Uploader is a single component that's easy to drop into your web application, it's actually built using several subcomponents
"under the hood." If your application design or desired user experience requires more customization, you can use the individual web components that come packaged with Mux Uploader to build out a custom upload UI that meets your needs.

To use this approach, add an `id` attribute to your `<mux-uploader>` element with a unique value.

You can then associate the `<mux-uploader>` element with any of the packaged components by adding a `mux-uploader=""` attribute to each component and setting it to the `id` that you gave to the `<mux-uploader>` element.

Here's a simple example for the web component:

```html
<!-- add a mux-uploader tag with an id attribute and hide it with CSS -->
<mux-uploader id="my-uploader" style="display: none;"></mux-uploader>

<!-- ...then, somewhere else in your app, add a reference back to it -->
<mux-uploader-file-select mux-uploader="my-uploader">
  <button slot="file-select">Pick a video</button>
</mux-uploader-file-select>
```

Here's one for React:

```jsx
import MuxUploader, { MuxUploaderFileSelect } from "@mux/mux-uploader-react";

export default function App() {
  return (
    <MuxUploader id="my-uploader" style={{ display: "none"}} />

    {/* ...then, somewhere else in your app, add a reference back to it */}
    <MuxUploaderFileSelect mux-uploader="my-uploader">
      <button slot="file-select">Pick a video</button>
    </mux-uploader-file-select>
  );
}
```

Because all of these are web components, you can use CSS to style them or
any of their slotted children (discussed below).

# Subcomponents

## File Select

The file select subcomponent is what tells Mux Uploader to open the file selection browser. The web component is
`<mux-uploader-file-select>`, and the React component is `<MuxUploaderFileSelect>`.

You can further customize it by slotting in your own `<button>` or other component in the `file-select` slot.

Here's an example:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  /* Hide the uploader before uploading */\n  mux-uploader:not([upload-error]):not([upload-in-progress]):not([upload-complete]) {\n    display: none;\n  }\n\n  mux-uploader-file-select button {\n    background: hotpink;\n    color: white;\n    padding: 4px 2px;\n    border: none;\n  }\n\n  mux-uploader-file-select button:hover {\n    background: purple;\n  }\n</style>\n<!-- In this example, we're still using Mux Uploader as a visual component -->\n<mux-uploader\n    id=\"my-uploader\"\n    no-drop\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>\n<mux-uploader-file-select mux-uploader=\"my-uploader\">\n  <button>Select from a folder</button>\n</mux-uploader-file-select>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

## Drop

The drop subcomponent is what implements the [drag and drop API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_Drag_and_Drop_API)
and tells Mux Uploader the relevant details about the file.
The web component is `<mux-uploader-drop>`, and the React component is `<MuxUploaderDrop>`.

Mux Uploader Drop provides a few slots for customization.

* `heading` - By default this is a `<span>` with the text "Drop a video file here to upload".
* `separator` - By default this is a `<span>` containing the text "or" placed between the heading and any additional children.
* (default) - Any additional children that don't have a specified slot will show up below the two previous slots.

Here's an example that puts all of these together, including CSS:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  /* Customize drop area background color & active background color */\n  mux-uploader-drop {\n    padding: 40px;\n    color: white;\n    background: hotpink;\n  }\n\n  mux-uploader-drop[active] {\n    background: #ffe4e6;\n  }\n</style>\n\n<mux-uploader-drop mux-uploader=\"my-uploader\">\n  <!-- Change the heading text/UI shown -->\n  <div slot=\"heading\">Drop videoz here plz</div>\n  <!-- Remove/hide the separator text/UI (default \"Or\") -->\n  <div slot=\"separator\" style=\"display: none;\"></div>\n  <div>You can also add arbitrary children for designs like the drop zone being the full screen</div>\n</mux-uploader-drop>\n<!-- In this example, we're still using Mux Uploader as a visual component -->\n<mux-uploader\n    id=\"my-uploader\"\n    no-drop\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

In addition, Mux Uploader Drop has attributes/properties for optionally showing an overlay whenever a file is
dragged over it. These are on by default in Mux Uploader, and are:

* `overlay` - A boolean attribute / property / React prop for enabling the overlay UI.
* `overlay-text` (`overlayText` property and React prop) - Allows you to provide custom text to show on the overlay.

If you'd like to further customize the overlay with a different background color, you can use the
`--overlay-background-color` CSS variable (which is also available when [using Mux Uploader directly](/docs/guides/uploader-web-customize-look-and-feel#use-css-variables-for-additional-styling))

Here's an example of these in action:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  /* Customize drop area background color & overlay background color */\n  mux-uploader-drop {\n    padding: 40px;\n    color: white;\n    background: hotpink;\n    --overlay-background-color: purple;\n  }\n</style>\n\n<!-- Use an overlay with customized overlay text -->\n<mux-uploader-drop overlay-text=\"Just let go!\" overlay mux-uploader=\"my-uploader\">\n  <!-- Change the heading text/UI shown -->\n  <div slot=\"heading\">Drop videoz here plz</div>\n  <!-- Remove/hide the separator text/UI (default \"Or\") -->\n  <div slot=\"separator\" style=\"display: none;\"></div>\n  <div>You can also add arbitrary children for designs like the drop zone being the full screen</div>\n</mux-uploader-drop>\n<!-- In this example, we're still using Mux Uploader as a visual component -->\n<mux-uploader\n    id=\"my-uploader\"\n    no-drop\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

### Custom Drop

You can even implement your own drag and drop completely separate from `<mux-uploader>` and as long as you dispatch a custom `file-ready` with the file in the `detail` property then `<mux-uploader>` will handle the upload upon receiving the event.

```html
<script>
  const muxUploader = document.querySelector("mux-uploader");

  // Dispatch custom event to trigger upload
  muxUploader.dispatchEvent(
    new CustomEvent("file-ready", {
      composed: true,
      bubbles: true,
      detail: file,
    })
  );
</script>
```

## Progress

The progress subcomponent is what visualizes progress of your upload. In fact, it is used twice "under the hood" by the default `<mux-uploader>`:
once for showing the %, and once for showing the progress bar.
The web component is `<mux-uploader-progress>`, and the React component is `<MuxUploaderProgress>`.

In addition, Mux Uploader Progress exposes the `type` attribute / property / React prop for choosing the particular kind of visualization you'd prefer. The
available type values are:

* `percentage` (default) - Show as a numeric % in text
* `bar` - Show as a progress bar
* `radial` (***Experimental***) - Show as a radial/circular progress indicator

Each of these types also has CSS variables available for further customization:

`percentage`:

* `--progress-percentage-display` - Applies to the `display` of the underlying percentage element (default: `block`).

`bar`:

* `--progress-bar-height` - Applies to the `height` of the progress bar (default: `4px`).
* `--progress-bar-fill-color` - Applies to the color of the progress bar's progress indication (default: `black`).

`radial`:

* `--progress-radial-fill-color` - Applies to the color of the radial progress indication (default: `black`).

Here's an example of these in action:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  mux-uploader-progress {\n    --progress-bar-fill-color: purple;\n    --progress-radial-fill-color: purple;\n    color: purple;\n    --progress-bar-height: 10px;\n  }\n</style>\n<!-- In this example, we're still using Mux Uploader as a visual component -->\n<mux-uploader\n    id=\"my-uploader\"\n    no-progress\n    no-drop\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>\n  <mux-uploader-progress\n  type=\"percentage\"\n  mux-uploader=\"my-uploader\"\n></mux-uploader-progress>\n<mux-uploader-progress\n  type=\"bar\"\n  mux-uploader=\"my-uploader\"\n></mux-uploader-progress>\n<mux-uploader-progress\n  type=\"radial\"\n  mux-uploader=\"my-uploader\"\n></mux-uploader-progress>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

## Status

The status subcomponent is what indicates when the upload is completed, or an error has occurred, or when you're offline.
The web component is `<mux-uploader-status>`, and the React component is `<MuxUploaderStatus>`.

Here's an example with a bit of CSS customization, using Mux Uploader's [state attributes](/docs/guides/uploader-web-customize-look-and-feel#use-uploader-attributes-for-state-driven-styling)
on the status component for additional state-driven styling:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  mux-uploader {\n    height: 2rem;\n    padding: 4px 2px;\n  }\n\n  mux-uploader-status {\n    background: hotpink;\n    color: white;\n    padding: 4px 2px;\n    height: 2rem;\n    display: block;\n  }\n\n  mux-uploader-status[upload-error] {\n    background: crimson;\n    /* By default, the error text color will be red. */\n    color: white;\n  }\n\n  mux-uploader-status[upload-complete] {\n    background: dodgerblue;\n  }\n\n  mux-uploader-file-select button:hover {\n    background: purple;\n  }\n</style>\n<mux-uploader-status mux-uploader=\"my-uploader\"></mux-uploader-status>\n<!--\n  In this example, we're still using Mux Uploader as a visual component.\n  Change the endpoint to an invalid one to see what an error looks like.\n-->\n<mux-uploader\n    id=\"my-uploader\"\n    no-drop\n    no-status\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

## Retry

The retry subcomponent that is displayed when an error has occurred to retry uploading and will notify Mux Uploader to retry when clicked.
The web component is `<mux-uploader-retry>`, and the React component is `<MuxUploaderRetry>`.

Here's a simple example:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<!-- In this example, we're still using Mux Uploader as a visual component. -->\n<mux-uploader\n    id=\"my-uploader\"\n    no-drop\n    no-retry\n    endpoint=\"http://fake.url.for/retry/purposes\"\n  ></mux-uploader>\n<mux-uploader-retry mux-uploader=\"my-uploader\"></mux-uploader-retry>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

## Pause

The pause subcomponent that is displayed while an upload is in progress and will notify Mux Uploader to either pause or resume uploading
when clicked, depending on the current uploading state.
The web component is `<mux-uploader-pause>`, and the React component is `<MuxUploaderPause>`.

Here's a simple example:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<!--\n  In this example, we're still using Mux Uploader as a visual component.\n  We've also made the chunk size smaller to help demo pause/resume behavior.\n-->\n<mux-uploader\n  id=\"my-uploader\"\n  no-drop\n  chunk-size=\"512\"\n  endpoint=\"https://httpbin.org/put\"\n></mux-uploader>\n<mux-uploader-pause mux-uploader=\"my-uploader\"></mux-uploader-pause>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```

# Advanced use cases

Here are some more examples of working with the subcomponents directly, using multiple subcomponents together to demonstrate the versatility
and composability of using the various subcomponents together in either React or vanilla HTML.

## React CSS modules

Just like you can do with the "batteries" usage of Mux Uploader, you can use [CSS-in-JS](/docs/guides/uploader-web-customize-look-and-feel#using-css-modules)
to handle styling of your subcomponents in React. Here's an example of how you can style Mux Uploader using CSS modules:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader-react": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import styles from \"./Styles.module.css\";\nimport MuxUploader, { MuxUploaderFileSelect, MuxUploaderProgress } from \"@mux/mux-uploader-react\"; \n\nexport default function App() {\n  return (\n    <div>\n        <h2 className={styles.heading}>Mux Uploader with CSS Modules</h2>\n        <MuxUploader id=\"css-modules-uploader\" className={styles.uploader} endpoint=\"https://httpbin.org/put\" />\n        <MuxUploaderFileSelect muxUploader=\"css-modules-uploader\">\n          <button className={styles.button}>Pick your video</button>\n        </MuxUploaderFileSelect>\n        <MuxUploaderProgress type=\"percentage\" muxUploader=\"css-modules-uploader\" className={styles.progress} />\n    </div>\n  );\n}\n",
      "active": true
    },
    "/src/index.js": {
      "code": "",
      "hidden": true
    },
    "/Styles.module.css": {
      "code": ".heading {color: #333;}\n.uploader { display: none; }\n.progress { color: orange; }\n.button {\n    background: #3a3a9d;\n    padding: 1em;\n    color: white;\n    border-radius: .35em;\n    border: 0;\n    cursor: pointer;\n}\n    "
    }
  },
  "template": "react"
}
```

## React Tailwind CSS

Also like Mux Uploader, you can use [Tailwind CSS](/docs/guides/uploader-web-customize-look-and-feel#using-tailwind-css) for your subcomponent styling. Here's an example in React:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader-react": "latest"
    }
  },
  "files": {
    "/App.js": {
      "code": "import MuxUploader, { MuxUploaderFileSelect, MuxUploaderProgress, MuxUploaderDrop } from \"@mux/mux-uploader-react\"; \n\nexport default function App() {\n  return (\n    <div className=\"p-4\">\n        <h2 className=\"text-lg text-slate-800 mb-2 font-bold\">Mux Uploader with Tailwind example</h2>\n        <MuxUploader id=\"my-uploader\" className=\"hidden\" endpoint=\"https://httpbin.org/put\" />\n\n        <MuxUploaderDrop\n            id=\"my-uploader\"\n            className=\"border border-4 border-slate-200 rounded-0.125 shadow mb-4\"\n            overlay\n            overlayText=\"Let it go\"\n        >\n            <span slot=\"heading\" className=\"text-slate-600 text-xl mb-2\">Drop your favorite video</span>\n            <span slot=\"separator\" className=\"text-slate-400 text-sm italic\">— or —</span>\n\n            <MuxUploaderFileSelect muxUploader=\"my-uploader\">\n                <button\n                    className=\"bg-pink-500 hover:bg-pink-600 my-2 px-col-0.5 py-2 rounded-0.125 text-white text-sm\"\n                >\n                    Select from a folder\n                </button>\n            </MuxUploaderFileSelect>\n        </MuxUploaderDrop>\n\n        <MuxUploaderProgress\n            type=\"percentage\"\n            muxUploader=\"my-uploader\"\n            className=\"text-3xl text-orange-600 underline\"\n        />\n    </div>\n  );\n}\n",
      "active": true
    },
    "/src/index.js": {
      "code": "",
      "hidden": true
    }
  },
  "options": {
    "externalResources": [
      "https://cdn.tailwindcss.com"
    ]
  },
  "template": "react"
}
```

## Uploader Page

In this example, we use the Mux Uploader Drop component as the parent for a full page upload experience, with the various subcomponents as descendants
with their own customization for a more bespoke look and feel:

Sandpack interactive code example configuration JSON.stringified:
```json
{
  "customSetup": {
    "dependencies": {
      "@mux/mux-uploader": "latest"
    }
  },
  "files": {
    "/index.html": {
      "code": "<style>\n  /* Various styles to customize a full page upload experience. See below for the HTML usage. */\n  body {\n    margin: 0;\n    color: white;\n    font-family: \"Gill Sans\", sans-serif;\n  }\n\n  /* Hide the uploader since we're only using it for functionality */\n  mux-uploader {\n    display: none;\n  }\n\n  /* Style the drop component as the root container for the page's UI */\n  mux-uploader-drop {\n    padding: 2rem;\n    width: 100vw;\n    height: 100vh;\n    display: flex;\n    flex-direction: column;\n    align-items: flex-start;\n    justify-content: flex-start;\n    background: hotpink;\n    /* Style the overlay background based on the page's color palette */\n    --overlay-background-color: purple;\n  }\n\n  /* Use a '+' cursor when dragging over the drop subcomponent */\n  mux-uploader-drop[active] {\n    cursor: copy;\n  }\n\n  mux-uploader-drop > [slot=\"heading\"] {\n    margin: 0;\n  }\n\n  /* Hide the drop component's separator text using its part selector */\n  mux-uploader-drop::part(separator) {\n    display: none;\n  }\n\n  mux-uploader-drop > .main-content {\n    flex-grow: 1;\n    align-self: stretch;\n  }\n\n  /* Use CSS to further customize the file select component's custom button (see below) */\n  mux-uploader-file-select > button {\n    padding: 6px 8px;\n    border: 1px solid #0d9488;\n    border-radius: 5px;\n    font-size: 24px;\n    color: white;\n    background: hotpink;\n    cursor: pointer;\n  }\n\n  mux-uploader-file-select > button:hover {\n    background: purple;\n  }\n\n  /* Customize the progress details to fit with the page's theme, including color palette */\n  mux-uploader-progress {\n    --progress-bar-fill-color: purple;\n    --progress-radial-fill-color: purple;\n    color: purple;\n    --progress-bar-height: 10px;\n  }\n\n  mux-uploader-status {\n    font-family: \"Gill Sans\", sans-serif;\n    font-size: 24px;\n    display: block;\n    padding: 6px 0;\n  }\n\n  /* Update the status component's text color based on the upload state to better fit the page's palette */\n  mux-uploader-status[upload-error] {\n    /* By default, the error text color will be red. */\n    color: navy;\n  }\n\n  mux-uploader-status[upload-complete] {\n    background: dodgerblue;\n  }\n</style>\n\n<!--\n  Note that in this example, mux-uploader is a child of mux-uploader-drop. This is a perfectly valid use case.\n-->\n<mux-uploader-drop\n mux-uploader=\"my-uploader\"\n overlay\n overlay-text=\"Drop to upload\"\n>\n  <mux-uploader\n    no-drop\n    no-progress\n    no-retry\n    no-status\n    id=\"my-uploader\"\n    endpoint=\"https://httpbin.org/put\"\n  ></mux-uploader>\n  <!-- By using the slot, this will automatically get hidden based on upload state changes -->\n  <h1 slot=\"heading\">Drop your video file anywhere on the page</h1>\n  <div class=\"main-content\">\n    <mux-uploader-status mux-uploader=\"my-uploader\"></mux-uploader-status>\n    <mux-uploader-progress mux-uploader=\"my-uploader\" type=\"percentage\"></mux-uploader-progress>\n    <mux-uploader-progress mux-uploader=\"my-uploader\"></mux-uploader-progress>\n  </div>\n  <mux-uploader-file-select mux-uploader=\"my-uploader\">\n    <button>Browse Files</button>\n  </mux-uploader-file-select>\n</mux-uploader-drop>",
      "active": true
    },
    "/index.js": {
      "code": "import '@mux/mux-uploader/dist/mux-uploader.js';",
      "hidden": true
    }
  }
}
```
