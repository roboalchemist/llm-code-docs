# Source: https://img.ly/docs/cesdk/renderer/get-started/node-processing-a2e4dc/

---
title: "Headless Automation using the Node.js API before Export"
description: "Invoking CE.SDK Renderer from Node.js after processing a scene with the Node.js API"
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/get-started/node-processing-a2e4dc/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/renderer/guides-8d8b00/) > [Headless Automation](https://img.ly/docs/cesdk/renderer/get-started/node-processing-a2e4dc/)

---

This guide builds upon the web app developed in [the Express.js walkthrough](https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/) by adding size variant generation for the exported scenes using the **Node.js API** for CreativeEditor SDK.

> **Reading time:** 10 minutes
>
> **Resources:**
>
> - [View source on GitHub](https://github.com/imgly/cesdk-renderer-examples/blob/$UBQ_VERSION$/demo_expressapi_variants/README.md)

## Who is This Guide For?

This guide is for developers who:

- Need to **perform image exporting programmatically** in a **Linux server environment**.
- Make use of the powerful **scene manipulation capabilities** of the **Node.js SDK** for CreativeEditor SDK.
- Want to use a **NVIDIA GPU** for accelerating the export time of CE.SDK Designs.
- Use **Node.js** to create a web app that needs image or video export functionality.

## What You'll Achieve

- Generate multiple scene variants based on a reference scene file uploaded by the user.
- Apply text variable substitutions when exporting the scene variants.
- Generate a zip file of image exports of all the size variants of the input scene file.

> **Note:** Please note that there are special licensing requirements needed for patent
> coverage of H.264 and H.265 video codecs, using open-source H.264 codecs at
> your own risk is possible but requires opt-in via an override environment
> variable.

## Prerequisites

Before getting started, ensure you have:

- A working web app developed in the [previous guide](https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/)

## Step 1: Add a CE.SDK Node.js dependency

In order to manipulate the scene files and change their sizes according to size presets, we will need the CE.SDK Node.js API. Install it with npm:

```bash
npm install @cesdk/node@$UBQ_VERSION$ --save
```

## Step 2: Implement the new feature

First, we import body-parser and CE.SDK in the main JavaScript file:

```js file=@cesdk_renderer_examples/expressapi_variants/src/app.mjs reference-only
/* eslint-disable no-console */
import express from 'express';
import multer from 'multer';
import { execFile } from 'node:child_process';
import fs from 'node:fs';
import { promisify } from 'node:util';

import CreativeEngine from '@cesdk/node';

const rendererPath =
  process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/cesdk-renderer';
const rendererPwd = process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/';

const execFileAsync = promisify(execFile);
const app = express();
const port = 8080;

const engineConfig = {
  license: process.env.CESDK_LICENSE
};

const upload = multer({ dest: '/uploads/' });

app.post('/export', upload.single('scene'), async (req, res) => {
  const sceneFile = req.file;
  const inputPath = `/uploads/${sceneFile.filename}`;
  const variants = [];

  const engine = await CreativeEngine.init(engineConfig);
  try {
    await engine.addDefaultAssetSources();
    const scene = await engine.scene.loadFromURL(`file://${inputPath}`);

    // Generate the scene files for all variable substitutions
    for (const firstName of ['Alice', 'Bob', 'Charlotte', 'David']) {
      engine.variable.setString('firstName', firstName);
      const newScene = await engine.scene.saveToArchive();
      const variantScene = `${inputPath}-${firstName}.zip`;
      const variantPng = `/exports/${sceneFile.filename}-${firstName}.png`;
      await promisify(fs.writeFile)(variantScene, newScene);
      variants.push({ scene: variantScene, png: variantPng });
    }
  } catch (error) {
    console.error(`Error loading scene file: ${error}: ${error.stack}`);
    res.status(500).send(`Error loading scene file: ${error}: ${error.stack}`);
    return;
  } finally {
    engine.dispose();
  }

  // Export each scene file to a png in parallel
  await Promise.all(
    variants.map(async (variant) => {
      const { error, stdout, stderr } = await execFileAsync(
        rendererPath,
        ['--input', variant.scene, '--output', variant.png],
        { cwd: rendererPwd }
      );

      if (error) {
        console.error(error);
        res.status(500).send(`Error processing scene file: ${stderr}`);
        try {
          fs.unlinkSync(variant.scene);
          fs.unlinkSync(variant.png);
        } catch (error) {
          console.error(`Error deleting files: ${error}`);
        }
        throw error;
      }

      try {
        fs.unlinkSync(variant.scene);
      } catch (error) {
        console.error(`Error deleting input file: ${error}`);
      }
    })
  );

  // Zip the variants together
  const zipPath = `/exports/${sceneFile.filename}-variants.zip`;
  const { error, stdout, stderr } = await execFileAsync('/usr/bin/zip', [
    '-j',
    zipPath,
    ...variants.map((variant) => variant.png)
  ]);

  if (error) {
    console.error(error);
    res.status(500).send(`Error zipping variants: ${stderr}`);
    return;
  }

  res.setHeader('Content-Type', 'application/zip');
  res.setHeader(
    'Content-Disposition',
    `attachment; filename="${sceneFile.originalname.replace('.scene', '.zip')}"`
  );
  res.sendFile(zipPath, (err) => {
    try {
      fs.unlinkSync(zipPath);
    } catch (error) {
      console.error(`Error deleting output file: ${error}`);
    }
  });

  // End of app.post( ...
});

app.use(express.static('public'));

app.listen(port, () => {
  console.log(
    `CE.SDK Renderer Express variant generation API demo listening on port ${port}`
  );
});
```

```js highlight-new-imports
import CreativeEngine from '@cesdk/node';
```

We will need a new top-level constant for the CE.SDK Engine configuration:

```js highlight-new-setup
const engineConfig = {
  license: process.env.CESDK_LICENSE
};
```

We now have one input scene, but multiple intermediary scene files and output image files combined into a zip file, so we need to adjust the export endpoint:

```js highlight-endpoint
app.post('/export', upload.single('scene'), async (req, res) => {
  const sceneFile = req.file;
  const inputPath = `/uploads/${sceneFile.filename}`;
  const variants = [];
```

Let's intialize a new Engine for each request, in a highly loaded production setting you should consider caching the engine instances and reusing them once requests are handled:

```js highlight-engine-init
const engine = await CreativeEngine.init(engineConfig);
try {
  await engine.addDefaultAssetSources();
  const scene = await engine.scene.loadFromURL(`file://${inputPath}`);
```

Now, we can use the engine to generate new scene variants with changed text variable values and export each into an independent archive:

```js highlight-engine-vars
  // Generate the scene files for all variable substitutions
  for (const firstName of ['Alice', 'Bob', 'Charlotte', 'David']) {
    engine.variable.setString('firstName', firstName);
    const newScene = await engine.scene.saveToArchive();
    const variantScene = `${inputPath}-${firstName}.zip`;
    const variantPng = `/exports/${sceneFile.filename}-${firstName}.png`;
    await promisify(fs.writeFile)(variantScene, newScene);
    variants.push({ scene: variantScene, png: variantPng });
  }
} catch (error) {
  console.error(`Error loading scene file: ${error}: ${error.stack}`);
  res.status(500).send(`Error loading scene file: ${error}: ${error.stack}`);
  return;
} finally {
  engine.dispose();
}
```

We have saved all the scenes to export to the `variants` array, now we can export each one just like in the previous guide. We make use of Promise parallelism to run multiple exports in parallel:

```js highlight-export
  // Export each scene file to a png in parallel
  await Promise.all(
    variants.map(async (variant) => {
      const { error, stdout, stderr } = await execFileAsync(
        rendererPath,
        ['--input', variant.scene, '--output', variant.png],
        { cwd: rendererPwd }
      );

      if (error) {
        console.error(error);
        res.status(500).send(`Error processing scene file: ${stderr}`);
        try {
          fs.unlinkSync(variant.scene);
          fs.unlinkSync(variant.png);
        } catch (error) {
          console.error(`Error deleting files: ${error}`);
        }
        throw error;
      }

      try {
        fs.unlinkSync(variant.scene);
      } catch (error) {
        console.error(`Error deleting input file: ${error}`);
      }
    })
  );
```

The input files are also cleaned up immediately to avoid wasting disk space.

Downloading multiple files is not very convenient for the user, so let's zip the new scene files first into an archive using the system `zip` command:

```js highlight-zip
  // Zip the variants together
  const zipPath = `/exports/${sceneFile.filename}-variants.zip`;
  const { error, stdout, stderr } = await execFileAsync('/usr/bin/zip', [
    '-j',
    zipPath,
    ...variants.map((variant) => variant.png)
  ]);

  if (error) {
    console.error(error);
    res.status(500).send(`Error zipping variants: ${stderr}`);
    return;
  }
```

We can then return the zip to the user and clean up afterwards:

```js highlight-return
  res.setHeader('Content-Type', 'application/zip');
  res.setHeader(
    'Content-Disposition',
    `attachment; filename="${sceneFile.originalname.replace('.scene', '.zip')}"`
  );
  res.sendFile(zipPath, (err) => {
    try {
      fs.unlinkSync(zipPath);
    } catch (error) {
      console.error(`Error deleting output file: ${error}`);
    }
  });

  // End of app.post( ...
});
```

For more details on the Node.js API, please check the Node.js platform documentation.

## Step 3: Testing

Once again, we can rebuild and start the container with the form:

```bash
sudo docker compose up --build
```

Then, navigate to http://localhost:8080/index.html and upload a scene or archive file exported from the CE.SDK Editor.
It should use a text variable named `firstName` for the variant generation to work.
Then press `Generate variants` and soon, a zip file should being downloading in your browser with all the exported image variants.

## Troubleshooting & Common Errors

**❌ Error encountered while creating an EGL hardware-accelerated context, falling back to CPU rendering: EGL initialize error: UNKNOWN**

- Make sure the GPU setup instructions were followed, this error indicates that a hardware OpenGL context could not be created inside the container.
- When using Docker Compose, ensure your `docker-compose.yml` includes `runtime: nvidia`.
- When using `docker run`, ensure you're using **both** `--runtime=nvidia` and `--gpus all` flags together.
- This could also be expected if testing the container on a machine without a GPU.

**❌ Error: `Invalid license key`**

- Verify that your **license key** is correct and not expired, or remove the key entirely to get watermarked output.

**❌ Error: `Max concurrency reached`**

- The avlicensed variant of the Renderer only allows up to a certain number of instances running simultaneously, as negotiated in your contract. To avoid running into the limit, limit your max deployment size to below this limit, or implement an exponential backoff retry system.



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
