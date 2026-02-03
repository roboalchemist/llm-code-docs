# Source: https://nuxt.com/raw/docs/3.x/getting-started/installation.md

# Source: https://nuxt.com/raw/docs/4.x/getting-started/installation.md

# Installation

> Get started with Nuxt quickly with our online starters or start locally with your terminal.

## Play Online

If you just want to play around with Nuxt in your browser without setting up a project, you can use one of our online sandboxes:

<card-group>
<card icon="i-simple-icons-stackblitz" target="_blank" title="Open on StackBlitz" to="https://nuxt.new/s/v4">



</card>

<card icon="i-simple-icons-codesandbox" target="_blank" title="Open on CodeSandbox" to="https://nuxt.new/c/v4">



</card>
</card-group>

Or follow the steps below to set up a new Nuxt project on your computer.

## New Project

### Prerequisites

- **Node.js** - [`20.x`](https://nodejs.org/en) or newer (but we recommend the [active LTS release](https://github.com/nodejs/release#release-schedule))
- **Text editor** - There is no IDE requirement, but we recommend [Visual Studio Code](https://code.visualstudio.com/) with the [official Vue extension](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (previously known as Volar) or [WebStorm](https://www.jetbrains.com/webstorm/), which, along with [other JetBrains IDEs](https://www.jetbrains.com/ides/), offers great Nuxt support right out-of-the-box.
- **Terminal** - In order to run Nuxt commands

<note>
<details>
<summary>

Additional notes for an optimal setup:

</summary>

- **Node.js**: Make sure to use an even numbered version (20, 22, etc.)
- **WSL**: If you are using Windows and experience slow HMR, you may want to try using [WSL (Windows Subsystem for Linux)](https://learn.microsoft.com/en-us/windows/wsl/install) which may solve some performance issues.
- **Windows slow DNS resolution**: Instead of using `localhost:3000` for local dev server on Windows, use `127.0.0.1` for much faster loading experience on browsers.

</details>
</note>

Open a terminal (if you're using [Visual Studio Code](https://code.visualstudio.com), you can open an [integrated terminal](https://code.visualstudio.com/docs/terminal/basics)) and use the following command to create a new starter project:

<code-group sync="pm">

```bash [npm]
npm create nuxt@latest <project-name>
```

```bash [yarn]
yarn create nuxt <project-name>
```

```bash [pnpm]
pnpm create nuxt@latest <project-name>
```

```bash [bun]
bun create nuxt@latest <project-name>
```

```bash [deno]
deno -A npm:create-nuxt@latest <project-name>
```

</code-group>

<tip>

Alternatively, you can find other starters or themes by opening [nuxt.new](https://nuxt.new) and following the instructions there.

</tip>

Open your project folder in Visual Studio Code:

```bash [Terminal]
code <project-name>
```

Or change directory into your new project from your terminal:

```bash
cd <project-name>
```

## Development Server

Now you'll be able to start your Nuxt app in development mode:

<code-group sync="pm">

```bash [npm]
npm run dev -- -o
```

```bash [yarn]
yarn dev --open
```

```bash [pnpm]
pnpm dev -o
```

```bash [bun]
bun run dev -o

# To use the Bun runtime during development
# bun --bun run dev -o
```

```bash [deno]
deno run dev -o
```

</code-group>

<tip icon="i-lucide-circle-check">

Well done! A browser window should automatically open for [http://localhost:3000](http://localhost:3000).

</tip>

## Next Steps

Now that you've created your Nuxt project, you are ready to start building your application.

<read-more title="Nuxt Concepts" to="/docs/4.x/guide/concepts">



</read-more>
