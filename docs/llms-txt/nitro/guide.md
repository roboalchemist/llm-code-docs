# Source: https://nitro.build/raw/guide.md

# Getting Started

> Create web servers with all necessary features and deploy them wherever you prefer.

## Intro

Nitro is an open source framework to build web servers using [h3](https://v1.h3.dev) and lots of built-in features.
Nitro automatically makes your code compatible with any [deployment](/deploy) provider and runtime!

<note>

Nitro can be used standalone or as the server engine of full-stack frameworks such as [Nuxt](https://nuxt.com).

</note>

## Quick start

<tip>

Instead of setting up a local development environment, you can use the [online playground](https://stackblitz.com/github/nitrojs/nitro/tree/main/examples/hello-world).

</tip>

<note>

Make sure you have installed the recommended setup:

- Latest LTS version of either [Node.js](https://nodejs.org/en), [Bun](https://bun.sh/), or [Deno](https://deno.com/).
- [Visual Studio Code](https://code.visualstudio.com/)

</note>

Create a new project using starter template:

<pm-x command="giget@latest nitro nitro-app --install">

</pm-x>

```sh
cd nitro-app
```

Start the development server:

<pm-run script="dev">

</pm-run>

Nitro is ready at `http://localhost:3000/`!

<tip>

Check `.nitro/dev/index.mjs` if you want to know what is happening

</tip>

Build your production-ready server:

<pm-run script="build">

</pm-run>

Output is in the `.output` directory and ready to be deployed on almost any provider with no dependencies.

You can try it locally with:

<pm-run script="preview">

</pm-run>

<read-more>

You can find more examples in the Nitro repository: [nitrojs/nitro/examples](https://github.com/nitrojs/nitro/tree/main/examples)

</read-more>

## Directory structure

The starter template includes some important files to get you started.

### `server/routes/`

The `server/routes/` directory contains your application handlers. You can create subdirectories inside `server/routes/` dir to create nested handlers. The file name is the route path.

<read-more to="/guide/routing">

</read-more>

### `server/api/`

The `server/api/` directory is similar to `server/routes/` with the only difference that routes inside it will be prefixed with `/api/` for convenience.

<read-more to="/guide/routing">

</read-more>

### `server/utils/`

This directory contains your application utils with auto import support.

<read-more to="/guide/utils">

</read-more>

### `server/plugins/`

This directory contains your custom nitro plugins.

<read-more to="/guide/plugins">

</read-more>

### `nitro.config.ts`

The `nitro.config.ts` file contains the configuration for Nitro.

<read-more to="/guide/configuration">

</read-more>

### `tsconfig.json`

The `tsconfig.json` file contains the TypeScript configuration for your project.

<read-more to="/guide/typescript">

</read-more>

### `package.json`

The `package.json` file contains all the dependencies and scripts for your project.
