# Source: https://img.ly/docs/cesdk/electron/get-started/electron/new-project-c2123i/

---
title: "New Electron Project"
description: "Setting up CE.SDK in a new Electron project"
platform: electron
url: "https://img.ly/docs/cesdk/electron/get-started/electron/new-project-c2123i/"
---

> This is one page of the CE.SDK Electron documentation. For a complete overview, see the [Electron Documentation Index](https://img.ly/docs/cesdk/electron.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/electron/llms-full.txt).

---

This guide walks you through integrating the **CreativeEditor SDK (CE.SDK)**
into a new Electron application. You’ll launch a native desktop editor window
running CE.SDK — ideal for image editing, creative automation, or
template-based workflows.

## Who Is This Guide For?

This guide is for developers who:

- Are building a new **Electron desktop application**.
- Want to embed a **powerful web-based editor** inside a native window.
- Prefer a quick, minimal boilerplate setup to get started.

## What You’ll Achieve

- Create a working Electron app using Vite.
- Embed and launch CE.SDK using ES module syntax.
- Load templates and asset libraries from the IMG.LY CDN.

## Prerequisites

Before starting, ensure you have:

- **Node.js v20+**.
- **npm** or **yarn**.
- A valid **CE.SDK license key** ([Get a free trial](https://img.ly/forms/free-trial)).

## Step 1: Initialize a New Project

Create a new Electron app using Vite:

```
npm create vite@latest my-electron-app
```

When prompted:

- Select **Framework > Others (variant: Electron)**.
- Select **Vanilla** as the project template.

Once the project is created, navigate to the project directory and install dependencies:

```
cd my-electron-app
npm install
```

Your project structure should now resemble the following:

```
. 📂 my-electron-app
├── 📂 electron/
│   ├── 📄 electron-env.d.ts
│   ├── 📄 main.ts
│   ├── 📄 preload.ts
├── 📄 electron-builder.json5
├── 📄 index.html
├── 📄 package-lock.json
├── 📄 package.json
├── 📂 public/
└── 📂 src/
    ├── 📄 counter.ts
    ├── 📄 main.ts
    ├── 📄 style.css
    ├── 📄 typescript.svg
    ├── 📄 vite-env.d.ts
├── 📄 tsconfig.json
└── 📄 vite.config.ts
```

## Step 2: Install CE.SDK

Install the CE.SDK package via npm:

```
npm install @cesdk/cesdk-js
```

This installs the CE.SDK as an ES module, which is compatible with the project’s default ES module setup.

## Step 3: Modify `index.html` to Load CE.SDK

Open the `index.html` file and update it to load CE.SDK as an ES module. Replace the existing content with the following:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Vite + CE.SDK</title>
    <style>
      body {
        margin: 0;
        overflow: hidden;
      }
      html {
        overscroll-behavior-x: contain;
      }
    </style>
  </head>
  <body>
    
    <div id="cesdk_container" style="width: 100%; height: 100vh;"></div>

    
    <script type="module">
      import CreativeEditorSDK from '@cesdk/cesdk-js';

      window.addEventListener('DOMContentLoaded', async () => {
        const config = {
          // license: 'YOUR_CESDK_LICENSE_KEY', // Replace with your CE.SDK license key
          baseURL:
            'https://cdn.img.ly/packages/imgly/cesdk-js/$UBQ_VERSION$/assets',
        };

        // Initialize and mount the editor
        const instance = await CreativeEditorSDK.create(
          '#cesdk_container',
          config,
        );

        await instance.addDefaultAssetSources();
        await instance.addDemoAssetSources({
          sceneMode: 'Design',
          withUploadAssetSources: true,
        });
        await instance.actions.run('scene.create');
      });
    </script>
  </body>
</html>
```

> **Warning:** **Note:** For convenience, CE.SDK serves assets (e.g., images, stickers,
> fonts) from IMG.LY’s CDN by default. In production, you should serve assets
> from your own server.

## Step 5: Start Your Electron App

Now, run your Electron app in development mode:

```
npm run dev
```

You should see a native Electron window open with the CE.SDK editor embedded inside it.

## Troubleshooting & Common Errors

❌ **`CreativeEditorSDK.create is not a function`**

This happens when you use `require()` instead of ES module `import`. Fix by using `<script type="module">` in your HTML.

❌ **Invalid license key**

Use a valid [trial or production license key](https://img.ly/forms/free-trial).

❌ **Blank screen or editor fails to load**

Check that `index.html` exists in your root directory and is correctly referenced in `main.ts` via `win.loadFile()`.

## Next Steps

Congratulations! You now have a fully working Electron app with CE.SDK integrated using ES module syntax. When you’re ready, take some time to explore CE.SDK further:

- [Configure CE.SDK with your own assets](https://img.ly/docs/cesdk/electron/serve-assets-b0827c/)
- [Customize the UI or localize the editor](https://img.ly/docs/cesdk/electron/user-interface/localization-508e20/)



---

## More Resources

- **[Electron Documentation Index](https://img.ly/docs/cesdk/electron.md)** - Browse all Electron documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/electron/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/electron/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
