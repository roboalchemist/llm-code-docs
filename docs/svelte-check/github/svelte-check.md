# Svelte Check - CLI Type Checker and Linter

Source: https://github.com/sveltejs/language-tools/tree/master/packages/svelte-check

Svelte Check provides CLI diagnostics checks for Svelte components. It's part of the Svelte Language Tools ecosystem and powers type checking and diagnostics alongside the Svelte VS Code extension.

## Overview

Svelte Check is a command-line tool that provides:

- **Unused CSS Detection** - Identifies unused CSS selectors in components
- **Svelte A11y Hints** - Accessibility checks and recommendations
- **JavaScript/TypeScript Compiler Errors** - Full type checking support
- **Integration with Language Server** - Uses the same language server as the official VSCode extension

## Requirements

- Node 16 or later

## Installation

### Local Installation (Recommended)

Install as a dev dependency in your project:

```bash
npm i svelte-check --save-dev
```

### Configuration in package.json

Add a script to your package.json:

```json
{
    "scripts": {
        "svelte-check": "svelte-check"
    },
    "devDependencies": {
        "svelte-check": "..."
    }
}
```

Run with:

```bash
npm run svelte-check
```

### Global Installation

Not recommended, but possible:

```bash
npm i svelte-check svelte -g
```

Then run:

1. Navigate to your project folder
2. Execute `svelte-check`

## Command-Line Options

### Workspace Configuration

| Flag | Description |
|------|-------------|
| `--workspace <path>` | Path to your workspace. All subdirectories except node_modules and those listed in `--ignore` are checked |
| `--tsconfig <path>` | Pass a path to a tsconfig or jsconfig file. The path can be relative to the workspace path or absolute. Doing this means that only files matched by the files/include/exclude pattern of the config file are diagnosed. It also means that errors from TypeScript and JavaScript files are reported. If not given, will do an upwards traversal looking for the next jsconfig/tsconfig.json |
| `--no-tsconfig` | Use this if you only want to check the Svelte files found in the current directory and below and ignore any JS/TS files (they will not be type-checked) |

### Watch Mode

| Flag | Description |
|------|-------------|
| `--watch` | Will not exit after one pass but keep watching files for changes and rerun diagnostics |
| `--preserveWatchOutput` | Do not clear the screen in watch mode |

### Ignoring Files

| Flag | Description |
|------|-------------|
| `--ignore <path1,path2>` | Only has an effect when used in conjunction with `--no-tsconfig`. Files/folders to ignore - relative to workspace root, comma-separated, inside quotes. Example: `--ignore "dist,build"`. When used in conjunction with `--tsconfig`, this will only have effect on the files watched, not on the files that are diagnosed, which is then determined by the `tsconfig.json` |

### Output Formats

| Flag | Description |
|------|-------------|
| `--output <human\|human-verbose\|machine\|machine-verbose>` | Output format for diagnostics |

### Diagnostic Control

| Flag | Description |
|------|-------------|
| `--fail-on-warnings` | Will also exit with error code when there are warnings |
| `--compiler-warnings <code1:error\|ignore,code2:error\|ignore>` | A list of Svelte compiler warning codes. Each entry defines whether that warning should be ignored or treated as an error. Warnings are comma-separated, between warning code and error level is a colon; all inside quotes. Example: `--compiler-warnings "css-unused-selector:ignore,unused-export-let:error"` |
| `--diagnostic-sources <js,svelte,css>` | A list of diagnostic sources which should run diagnostics on your code. Possible values are `js` (includes TS), `svelte`, `css`. Comma-separated, inside quotes. By default all are active. Example: `--diagnostic-sources "js,svelte"` |
| `--threshold <error\|warning>` | Filters the diagnostics to display. `error` will output only errors while `warning` will output warnings and errors. |

## Output Formats

### Human-Readable Output

Default format suitable for developers:

```
[filename] [line]:[column] - [message]
```

### Machine-Readable Output

Set `--output` to `machine` or `machine-verbose` for easier parsing by CI systems and tools.

Each row corresponds to a new record. Rows are made up of columns that are separated by a single space character. The first column of every row contains a timestamp in milliseconds.

#### Machine Output Format

```
[timestamp] START "[workspace path]"
[timestamp] ERROR "[filename]" [line]:[column] "[message]"
[timestamp] WARNING "[filename]" [line]:[column] "[message]"
[timestamp] COMPLETED [file_count] FILES [error_count] ERRORS [warning_count] WARNINGS [problem_files_count] FILES_WITH_PROBLEMS
```

Example:

```
1590680325583 START "/home/user/language-tools/packages/language-server/test/plugins/typescript/testfiles"
1590680326283 ERROR "codeactions.svelte" 1:16 "Cannot find module 'blubb' or its corresponding type declarations."
1590680326778 WARNING "imported-file.svelte" 0:37 "Component has unused export property 'prop'. If it is for external reference only, please consider using `export const prop`"
1590680326807 COMPLETED 20 FILES 21 ERRORS 1 WARNINGS 3 FILES_WITH_PROBLEMS
```

#### Machine-Verbose Output Format

Uses NDJSON (Newline-Delimited JSON) format with detailed diagnostic information:

```
[timestamp] {"type":"ERROR","filename":"[filename]","start":{"line":[line],"character":[char]},"end":{"line":[line],"character":[char]},"message":"[message]","code":[code],"source":"[source]"}
```

Example:

```
1590680326283 {"type":"ERROR","fn":"codeaction.svelte","start":{"line":1,"character":16},"end":{"line":1,"character":23},"message":"Cannot find module 'blubb' or its corresponding type declarations.","code":2307,"source":"js"}
1590680326778 {"type":"WARNING","filename":"imported-file.svelte","start":{"line":0,"character":37},"end":{"line":0,"character":51},"message":"Component has unused export property 'prop'. If it is for external reference only, please consider using `export const prop`","code":"unused-export-let","source":"svelte"}
```

### Error Codes

If the application experiences a runtime error:

```
[timestamp] FAILURE "[error message]"
```

## FAQ

### Why is there no option to only check specific files?

Svelte Check needs to know the whole project to do valid checks. If you alter a component property (`export let foo` to `export let bar`), but don't update the component usages, they all have errors - but you would not catch them if you only run checks on changed files.

### TypeScript Support

#### Using TypeScript with Svelte Check

To use TypeScript in your Svelte components, add the `lang="ts"` attribute to script tags:

```html
<script lang="ts">
    export let name: string;
</script>
```

#### Setup for TypeScript

Create a `svelte.config.js` file with preprocessor configuration:

ESM-style (for projects with `"type": "module"` in package.json):

```js
import sveltePreprocess from 'svelte-preprocess';

export default {
    preprocess: sveltePreprocess()
};
```

CJS-style:

```js
const sveltePreprocess = require('svelte-preprocess');

module.exports = {
    preprocess: sveltePreprocess()
};
```

#### Restarting the Language Server

When you update configuration, restart the language server in VS Code:
- Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
- Type `svelte restart`
- Select `Svelte: Restart Language Server`

### TypeScript Troubleshooting

#### Cannot use TypeScript even with `lang="ts"`

Make sure you've completed the setup steps in the TypeScript configuration section above.

#### Typing Reactive Assignments

If you get an "implicitly has type 'any'" error:

```html
<script lang="ts">
    export let data: { someKey: string | null };

    $: show = !!data.someKey; // ERROR: `show` has type `any`
</script>
```

Explicitly type the variable:

```html
<script lang="ts">
    export let data: { someKey: string | null };

    let show: boolean;
    $: show = !!data.someKey;
</script>
```

#### Importing Type-Only Imports

When using `svelte-preprocess` with `transpileOnly: true` or v4.x, import interfaces using the `import type` syntax:

```html
<script lang="ts">
    import type { SomeInterface } from './MyModule.ts';
</script>
```

You need at least TypeScript 3.8 for this syntax.

### Typing Component Events

Use `createEventDispatcher` with type arguments:

```html
<script lang="ts">
    import { createEventDispatcher } from 'svelte';

    const dispatch = createEventDispatcher<{
        checked: boolean;
        hello: string;
    }>();
</script>
```

### Preprocessor Configuration

See the [Preprocessor Setup Guide](https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/in-general.md) for configuration details.

Specific guides for:
- [SCSS/Less](https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/scss-less.md)
- [Other CSS Preprocessors & TailwindCSS](https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/other-css-preprocessors.md)
- [TypeScript](https://github.com/sveltejs/language-tools/blob/master/docs/preprocessors/typescript.md)

## Component Documentation

To add JSDoc-style documentation to your Svelte components that will appear in LSP-compatible editors:

```html
<!--
 @component
 Here's some documentation for this component. It will show up on hover for
 JavaScript/TypeScript projects using a LSP-compatible editor such as VSCode or
 Vim/Neovim with coc.nvim.

 - You can use markdown here.
 - You can use code blocks here.
 - JSDoc/TSDoc will be respected by LSP-compatible editors.
 - Indentation will be respected as much as possible.
-->

<main>
    <h1>Hello world</h1>
</main>
```

Single-line documentation:

```html
<!-- @component You can use a single line, too -->
```

Note: Only the last documentation comment will be used.

## CI/CD Integration

Svelte Check is perfect for integration into CI/CD pipelines:

```bash
npm run svelte-check
```

Use machine-readable output for parsing:

```bash
svelte-check --output machine
```

Exit with error on warnings:

```bash
svelte-check --fail-on-warnings
```

## Related Tools

- **Svelte VS Code Extension** - IDE integration using the same language server
- **svelte2tsx** - Converts Svelte files to legal TypeScript/JSX
- **svelte-language-server** - The underlying language server (LSP)

## Credits

Inspired by Vue's VTI (Vue Type Indicator), which laid the foundation for Svelte Check.

## See Also

- [Official GitHub Repository](https://github.com/sveltejs/language-tools)
- [Svelte Documentation](https://svelte.dev/)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
