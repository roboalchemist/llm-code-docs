# Source: https://juno.build/docs/guides/nodejs.md

# Use Juno in a NodeJS context

This guide explains how to use Juno from a client running in a non-interactive environment (e.g. NodeJS, scripts, or CI).

**Tip:**

You can find examples of NodeJS usage in the [example](https://github.com/junobuild/examples/tree/main/node) repository.

---

## Usage

The simplest and recommended way to interact with your Juno project is by using the [juno run](/docs/reference/cli.md#run) command provided by the CLI.

If you haven't installed it yet, run:

*   npm
*   yarn
*   pnpm

```
npm i -g @junobuild/cli
```

```
yarn global add @junobuild/cli
```

```
pnpm add -g @junobuild/cli
```

With `juno run`, you can write custom scripts that automatically inherit your environment (`mode`, `profile`, etc.) and [configuration](/docs/reference/configuration.md).

A script â written in JavaScript or TypeScript â must export a single `onRun` produced by `defineRun`. For example:

my-task.ts

```
import { defineRun } from "@junobuild/config";export const onRun = defineRun(({ mode, profile }) => ({  run: async ({ satelliteId, identity }) => {    console.log("Running task with:", {      mode,      profile,      satelliteId: satelliteId.toText(),      whoami: identity.getPrincipal().toText()    });  }}));
```

Run it with:

```
juno run --src ./my-task.ts
```

---

## Example

Suppose you want to fetch a document and export it to a file:

```
import { getDoc } from "@junobuild/core";import { defineRun } from "@junobuild/config";import { jsonReplacer } from "@dfinity/utils";import { writeFile } from "node:fs/promises";export const onRun = defineRun(({ mode }) => ({  run: async (context) => {    const key = mode === "staging" ? "123" : "456";    const doc = await getDoc({      collection: "demo",      key,      satellite: context    });    await writeFile("./mydoc.json", JSON.stringify(doc, jsonReplacer, 2));  }}));
```

This script retrieves a document using `getDoc`, selects the document ID based on the current `mode` (for example staging or production), and writes the result to `mydoc.json`, using `jsonReplacer` to handle types not supported by JSON such as `BigInt`.