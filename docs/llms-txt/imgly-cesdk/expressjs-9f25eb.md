# Source: https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/

---
title: "Integrating into an Express.js Web Application"
description: "Invoking CE.SDK Renderer from Node.js"
platform: renderer
url: "https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/"
---

> This is one page of the CE.SDK Renderer documentation. For a complete overview, see the [Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md). For all docs in one file, see [llms-full.txt](https://img.ly/docs/cesdk/renderer/llms-full.txt).

**Navigation:** [Guides](https://img.ly/docs/cesdk/renderer/guides-8d8b00/) > [Express.js Webservice](https://img.ly/docs/cesdk/renderer/get-started/expressjs-9f25eb/)

---

This guide walks you through integrating export functionality via the **CE.SDK Renderer** inside an **Express.js web app**.
We strongly recommend following the [server setup guide](https://img.ly/docs/cesdk/renderer/get-started/commandline-4230bf/) first.

> **Reading time:** 10 minutes
>
> **Resources:**
>
> - [View source on GitHub](https://github.com/imgly/cesdk-renderer-examples/blob/$UBQ_VERSION$/demo_expressapi/README.md)

## Who is This Guide For?

This guide is for developers who:

- Need to **perform image exporting programmatically** in a **Linux server environment**.
- Want to use a **NVIDIA GPU** for accelerating the export time of CE.SDK Designs.
- Use **Node.js** to create a web app that needs image or video export functionality.

## What You'll Achieve

- Create a Docker container adding a Node.js runtime on top of the CE.SDK Renderer system image.
- Wire up a HTTP endpoint in Express.js to export an image with the CE.SDK Renderer.

> **Note:** Please note that there are special licensing requirements needed for patent
> coverage of H.264 and H.265 video codecs, using open-source H.264 codecs at
> your own risk is possible but requires opt-in via an override environment
> variable.

## Prerequisites

Before getting started, ensure you have:

- A server or virtual machine running **Ubuntu 24.04 LTS**, preferably with a GPU (Image exports are possible without GPU acceleration)
- Ability to run the **CE.SDK Renderer** Docker container on your server and a pulled copy of the container image on your development machine.
- **Node.js** (v20 or later) and **npm** installed.

## Step 1: Create a new Express project

Create a new JavaScript project and add Express.js as a dependency:

```bash
# Write app/main.mjs when asked for the entrypoint
npm init --init-type module
npm install express@5 --save
# For HTML form parsing
npm install multer@2 --save
```

Create a simple hello world API endpoint in `app/main.mjs`:

```js
import express from 'express';
import multer from 'multer';

const app = express();
const port = 8080;

app.use(express.static('public'));

app.listen(port, () => {
  console.log(`CE.SDK Renderer Express API demo listening on port ${port}`);
});
```

And create the corresponding `public/index.html` file:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>CE.SDK Renderer Express API Demo</title>
  </head>
  <body>
    Hello, world!
  </body>
</html>
```

Start the server with `node src/app.mjs` and make sure the `index.html` file gets correctly served.

## Step 2: Package into a Docker container

In order to make use of the CE.SDK Renderer from the web app, we can install Node.js into a new container based on the Processor container and copy our app into it.
Create the following `Dockerfile` to achieve this goal:

```dockerfile file=@cesdk_renderer_examples/expressapi/Dockerfile
FROM docker.io/imgly/cesdk-renderer:latest

USER root

ARG NODE_VERSION=20.19.4
RUN mkdir -p /opt/node
WORKDIR /opt/node
RUN curl -fsSL https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.xz -o node.tar.xz \
 && tar -Jxf node.tar.xz --strip-components=1 \
 && rm node.tar.xz \
 && /opt/node/bin/node --version

ENV PATH="/opt/node/bin:$PATH"

COPY . /app
WORKDIR /app
RUN npm install --production
RUN mkdir -p /uploads /exports
RUN chmod 0777 /uploads /exports

USER containeruser
EXPOSE 8080
ENTRYPOINT [ "/bin/sh", "-c", "/opt/node/bin/node src/app.mjs" ]
```

We will also need a `.dockerignore` file to exclude unnecessary files from polluting the container:

```
Dockerfile
.gitignore
node_modules
docker-compose.yml
```

For convenience, we can use [Docker Compose](https://docs.docker.com/compose/) with a `docker-compose.yml` file to quickly rebuild and start an updated version of the container:

```yaml file=@cesdk_renderer_examples/expressapi/docker-compose.yml
services:
  app:
    platform: linux/amd64
    build: .
    environment:
      - CESDK_LICENSE=${CESDK_LICENSE}
    ports:
      - "8080:8080"
    # GPU acceleration - remove if running on a system without NVIDIA GPU
    runtime: nvidia
```

### Optional: .env (License key)

If you already have a license key, put it in the `.env` file for later usage by the container.
If you don't, you can skip this step and you'll get a watermarked output file.

```bash
CESDK_LICENSE=my.license.key
```

### Build and start the container

Run the following command to build and start the container, making use of our compose file:

```bash
sudo docker compose up --build
```

Then, navigate to http://localhost:8080/index.html and make sure you can see the webpage we have created.
You can terminate the server at any point with `Ctrl+C` in the shell.

## Step 3: Invoke the processor from Node.js

Let's walk through the steps needed to create a simple HTML POST form where the user can submit a scene file or archive, and get an exported png in return.

First, we'll need to import some additional library functions:

```js file=@cesdk_renderer_examples/expressapi/src/app.mjs reference-only
/* eslint-disable no-console */
import express from 'express';
import multer from 'multer';
import { execFile } from 'node:child_process';
import fs from 'node:fs';
import { promisify } from 'node:util';

const rendererPath =
  process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/cesdk-renderer';
const rendererPwd = process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/';

const execFileAsync = promisify(execFile);
const app = express();
const port = 8080;
const upload = multer({ dest: '/uploads/' });

app.post('/export', upload.single('scene'), async (req, res) => {
  const sceneFile = req.file;
  const inputPath = `/uploads/${sceneFile.filename}`;
  const outputPath = `/exports/${sceneFile.filename}.png`;

  const { error, stdout, stderr } = await execFileAsync(
    rendererPath,
    ['--input', inputPath, '--output', outputPath],
    { cwd: rendererPwd }
  );

  if (error) {
    console.error(error);
    res.status(500).send(`Error processing scene file: ${stderr}`);
    try {
      fs.unlinkSync(inputPath);
      fs.unlinkSync(outputPath);
    } catch (error) {
      console.error(`Error deleting files: ${error}`);
    }
    return;
  }

  try {
    fs.unlinkSync(inputPath);
  } catch (error) {
    console.error(`Error deleting input file: ${error}`);
  }
  res.setHeader('Content-Type', 'image/png');
  res.setHeader(
    'Content-Disposition',
    `inline; filename="${sceneFile.originalname.replace('.scene', '.png')}"`
  );
  res.sendFile(outputPath, (err) => {
    try {
      fs.unlinkSync(outputPath);
    } catch (error) {
      console.error(`Error deleting output file: ${error}`);
    }
  });
});

app.use(express.static('public'));

app.listen(port, () => {
  console.log(`CE.SDK Renderer Express API demo listening on port ${port}`);
});
```

```js highlight-imports
import express from 'express';
import multer from 'multer';
import { execFile } from 'node:child_process';
import fs from 'node:fs';
import { promisify } from 'node:util';
```

Let's define a few helpful top-level constants:

```js highlight-constants
const rendererPath =
  process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/cesdk-renderer';
const rendererPwd = process.env.CESDK_RENDERER_PATH || '/opt/cesdk-renderer/';

const execFileAsync = promisify(execFile);
const app = express();
const port = 8080;
const upload = multer({ dest: '/uploads/' });
```

Now we can start on a POST route handler for scene exports:

```js highlight-post
app.post('/export', upload.single('scene'), async (req, res) => {
  const sceneFile = req.file;
  const inputPath = `/uploads/${sceneFile.filename}`;
  const outputPath = `/exports/${sceneFile.filename}.png`;
```

The middleware handles file upload and unique naming for us, so at this point we are ready to execute the Processor and generate a png image:

```js highlight-exec
const { error, stdout, stderr } = await execFileAsync(
  rendererPath,
  ['--input', inputPath, '--output', outputPath],
  { cwd: rendererPwd }
);
```

We specify the input and output paths explicity, and for this example we override the scene DPI to value of 300 to be ready for a low-resolution print.
For more flexibility of where this demo can be ran, we allow the use of any render device - by default GPU rendering is enforced to prevent falling into a low performance mode by accidental misconfiguration.

The Processor accepts both scene files and full archives, and it automatically detects the input file type based on its contents.

Because we await the `execFileAsync` call, we are now ready to proceed with simple error handling:

```js highlight-error
if (error) {
  console.error(error);
  res.status(500).send(`Error processing scene file: ${stderr}`);
  try {
    fs.unlinkSync(inputPath);
    fs.unlinkSync(outputPath);
  } catch (error) {
    console.error(`Error deleting files: ${error}`);
  }
  return;
}
```

And if the export succeeds, we want to delete the input file, forward the output file in the output response and delete the output file once the response has been sent to avoid polluting the filesystem:

```js highlight-result
  try {
    fs.unlinkSync(inputPath);
  } catch (error) {
    console.error(`Error deleting input file: ${error}`);
  }
  res.setHeader('Content-Type', 'image/png');
  res.setHeader(
    'Content-Disposition',
    `inline; filename="${sceneFile.originalname.replace('.scene', '.png')}"`
  );
  res.sendFile(outputPath, (err) => {
    try {
      fs.unlinkSync(outputPath);
    } catch (error) {
      console.error(`Error deleting output file: ${error}`);
    }
  });
});
```

Now we just need to modify the body of the `index.html` file to have a simple file upload form matching our API definition:

```html
<body>
  <form id="form" method="post" enctype="multipart/form-data" action="export">
    <input type="file" name="scene" accept=".scene" /> <br />
    <input type="submit" value="Export png" />
  </form>
</body>
```

### Testing

Once again, we can rebuild and start the container with the form:

```bash
sudo docker compose up --build
```

Then, navigate to http://localhost:8080/index.html and upload a scene or archive file exported from the CE.SDK Editor to get a png rendered in our browser in return.

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

## Next Steps

Congratulations! You've successfully exported a scene with the **CE.SDK Renderer** from **a Node.js API**. Next, explore:

- [Integrating with CE.SDK for Node.js to combine programmatic scene
  manipulation with efficient exports](https://img.ly/docs/cesdk/renderer/get-started/node-processing-a2e4dc/)



---

## More Resources

- **[Renderer Documentation Index](https://img.ly/docs/cesdk/renderer.md)** - Browse all Renderer documentation
- **[Complete Documentation](https://img.ly/docs/cesdk/renderer/llms-full.txt)** - Full documentation in one file (for LLMs)
- **[Web Documentation](https://img.ly/docs/cesdk/renderer/)** - Interactive documentation with examples
- **[Support](mailto:support@img.ly)** - Contact IMG.LY support
