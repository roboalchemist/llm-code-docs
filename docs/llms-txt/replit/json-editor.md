# Source: https://docs.replit.com/extensions/examples/json-editor.md

# JSON Editor

> Build a custom JSON editor extension for Replit using React and react-json-view to enable structured editing and code folding of JSON files.

# Create a JSON editor

In this tutorial, we will create a JSON editor Extension with React and the [react-json-view](https://www.npmjs.com/package/react-json-view) package. Our application will display a JSON file's content and allow users to edit, add or delete properties directly from the editor. When a user finishes editing the JSON, the file will automatically update with the changes.

## Prerequisites

This tutorial assumes that you have a basic knowledge and understanding of web development and React.

## Set up your Replit App

1. Fork the [Replit React Extension Template](https://replit.com/@replit/React-Extension?v=1).
2. Install the `react-json-view` package with `npm install --force react-json-view`. The package uses React 17 as a peer dependency but works fine with React 18 as well.

## Configure the manifest file

Configure the title and description in `public/extension.json` (the Extension [manifest file](../api/manifest)).

```json  theme={null}
{
  "name": "JSON Editor",
  "description": "A viewer/editor for JSON files, providing code folding and structured editing",
  "tags": ["editor"]
}
```

Add the `fileHandlers` property to `extension.json` and provide a handler for JSON files. This tells Replit that your extension handles a particular file pattern using a page provided by your extension at the `handler` path. In this case, the handler is `/`, meaning that Replit shows the page at the root as the handler for all `.json` files

```json  theme={null}
  "fileHandlers": [
    {
      "glob": "*.json",
      "handler": "/"
    }
  ],
```

## Build the JSON editor

Import the following dependencies in `src/App.jsx`.

```js  theme={null}
import * as React from "react";
import ReactJson from "react-json-view";
import "./App.css";
import {
  useReplit,
  useReplitEffect,
  useWatchTextFile,
} from "@replit/extensions-react";
```

Remove all the existing code from the `App` function and a state variable `path`, which will point to the JSON file your Extension will render.

```js  theme={null}
function App() {
  const [path, setPath] = React.useState(null);

  return <div>My app</div>;
}
```

### Initialize the Handshake

Initialize the handshake and derive the `status` and `error` properties from the [`useReplit hook`](../development/react/hooks/useReplit) within the `App` function.

The `status` property is an enumerated value indicating whether the handshake connection with Replit is `loading`, `ready`, or has resulted in an `error`.

```js  theme={null}
function App() {
  ...

  const { status, error } = useReplit();

  ...
}
```

### Get the File Path

Use the [`useReplitEffect`](../development/react/hooks/useReplitEffect) hook and set the `path` state to the `extensionPort`'s file path. This will set the `path` state once the handshake between Replit and your Extension has been established.

```js  theme={null}
useReplitEffect(async ({ extensionPort }) => {
  const filePath = await extensionPort.filePath;

  setPath(filePath);
}, []);
```

### Create the File Watcher

You can easily create a file watcher with the [`useWatchTextFile`](../development/react/hooks/useWatchTextFile) hook. Call the hook, pass in the file path, and derive `content` and `writeChange` from it.

```js  theme={null}
const { content, writeChange } = useWatchTextFile({
  filePath: path,
});
```

### Reflecting file contents

Create a `parsedContent` [React Memo](https://react.dev/reference/react/useMemo) that returns the `content` file value as parsed JSON. If there is an error parsing it, return `null` instead.

The [React useMemo hook](https://react.dev/reference/react/useMemo) caches a result based on an array of dependencies between re-renders to improve performance. Caching reduces the amount of computing required in a process, ultimately improving performance.

```js  theme={null}
const parsedContent = React.useMemo(() => {
  try {
    return JSON.parse(content);
  } catch (e) {
    return null;
  }
}, [content]);
```

### Handle file changes

Create a function which handles changes from the [react-json-view](https://www.npmjs.com/package/react-json-view) editor component. The `updated_src` property passed into this function is a JSON object.

Stringify the JSON object and then write it to the JSON file using the `writeChange` function.

Finally, update the `setContent` state to reflect the contents of the file.

```js  theme={null}
const handleChange = async ({ updated_src: newContent }) => {
  const stringified = JSON.stringify(newContent, null, 2);

  writeChange({
    from: 0,
    to: content.length,
    insert: stringified,
  });
};
```

### Build the UI

It's time to start building the UI.

First, handle loading and error states.

```js  theme={null}
function App() {
  ...

  if (status === "error") {
    return <main>
      <div className="notice error">{error.toString()}</div>
    </main>
  }
  else if (status === "loading") {
    return <main>
      <div className="notice">Loading...</div>
    </main>
  }
  else if (status === "ready") {
    return <main>Ready</main>
  }
}
```

[Install the Extension](/extensions/development/installation) by opening up the Command Bar (**cmd**/**ctrl** + k), navigating to **Extensions**, and selecting **From this Replit App**. The extension should load and display "Ready" almost instantly.

If you open the webview using the Preview tool, your extension should load for a few seconds and fail. Extensions should be developed and used within the correct pane rather than the webview.

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f2f3f48af52ab367ae7fef51f04b4860" alt="Loading state" data-og-width="365" width="365" data-og-height="181" height="181" data-path="images/extensions/examples/json-editor/load-nocss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8aac440bc485f7ba03a15ec9c43c0787 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=fae12007288073a918dbaee60e3c1135 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=fa68258c4b1b51a5489a04aab3536d27 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a66c679120d1efba6e443e0d1d64d0d5 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=92eefb87cecdb62ee922ddba56721dcf 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/load-nocss.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7d4031bfb9a5674328efc7030ab45829 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=520299873c41169d526aa3847c33c29b" alt="Error state" data-og-width="365" width="365" data-og-height="181" height="181" data-path="images/extensions/examples/json-editor/error-nocss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=f0b9703f27d43ee1b140fa62f4fe1a24 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6e43d53cb5e34b8c2ba95c174175f2e0 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=9c915f4dd8014dd0a6fc670220270c19 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=8dc6f63df6a156a27a5b1d7fd5689529 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d10450d87e8b6bf0e67b522c2f1adac6 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/error-nocss.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=bb47514b1fb3f1f49351b94b709bd2a5 2500w" />
</Frame>

If both `path` and `content` are valid strings, render the editor. If not, tell the user to select a file.

```js  theme={null}
else if (status === "ready") {
  return <main>
    {path && content ?
      <ReactJson
        style={{ width: '100vw', height: "100vh", padding: "1em" }}
        theme="ocean"
        displayDataTypes={false}
        src={parsedContent}
        onEdit={handleChange}
        onAdd={handleChange}
        onDelete={handleChange}
      /> :
      <div className="notice">
        Please select a file
      </div>
    }
  </main>
}
```

That's it. Now install and load your Extension, and it should work.

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=0cec3fc0772cbc28b75f9255c0723fa6" alt="Select a file" data-og-width="365" width="365" data-og-height="181" height="181" data-path="images/extensions/examples/json-editor/file-select-nocss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=84eb9d94af220d80553cf3ace0b9eb87 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d7e12f8c3009b7eb92410d29f61448b3 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2086d57fb6467a946b76501acc7ff2c2 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=79173abc039795462a745c5ea9f2ca0d 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=7e739ad00c95dbc0a743b54cb432a7ab 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/file-select-nocss.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=d07e217aaa4a7de7249e052297527984 2500w" />
</Frame>

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=a22c51eebcd63b8cef368bad556f3069" alt="Editor without CSS" data-og-width="544" width="544" data-og-height="320" height="320" data-path="images/extensions/examples/json-editor/editor-nocss.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=991b0edb37876c0b891999698ba9053a 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=2b358065a4215255feb916317228c6f1 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=55c47e17c7ff01019107e0cc6cf14ba2 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6d3d8be852d3291b4bfe1fe2ffbdcbe6 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=0f4ac1f989994040dfc0c6159bc03440 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/extensions/examples/json-editor/editor-nocss.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=024bc89ca5feb2875f6e4135eb17abe1 2500w" />
</Frame>

### Style your Extension

Right now, the Extension has barely any styles applied to it. To make it look more polished, paste the following into `App.css`:

```css  theme={null}
html,
body {
  margin: 0;
  padding: 0;
  height: 100%;
  width: 100%;
  display: flex;
  font-family: sans-serif;
  background: black;
  color: white;
}

#root,
main {
  flex-grow: 1;
  display: flex;
  width: 100%;
}

.notice {
  flex-grow: 1;
  align-self: center;
  justify-self: center;
  text-align: center;
  color: white;
  font-size: 24px;
}
```

***

Your Extension is now complete! [Install it](/extensions/development/installation), press the kebab menu on a JSON file in the file tree and then select "Open with JSON Editor" to start editing your JSON files with ease.

[See full solution](https://replit.com/@IroncladDev/JSON-editor-example?v=1).

<iframe src="https://replit.com/@IroncladDev/JSON-editor-example?embed=true" height="600" />
