# Source: https://lynxjs.org/help/example.md

# Managing Interactive Examples (`<Go>`)

Interactive examples allow users to preview and edit code directly in the documentation. This guide explains how to manage these examples using the dedicated workspace and the `<Go>` component.

## Overview

The interactive example system allows you to embed live, runnable Lynx code in your documentation. It consists of:

1. **Source Packages**: Examples are real npm packages managed in `packages/lynx-example-packages/`.
2. **Build Process**: A script bundles these packages into static assets for the website.
3. **`<Go>` Component**: A React component that renders the interactive editor and preview in your MDX files.

***

## 1. Using the `<Go>` Component

To embed an interactive example in your documentation, use the `<Go>` component.

### Basic Usage

Import `Go` from `@lynx` and provide the `example` ID (which corresponds to the package directory name).

```tsx
import { Go } from '@lynx';

<Go example="view" />;
```

### Component Props

| Prop               | Type     | Default          | Description                                                                                                 |
| :----------------- | :------- | :--------------- | :---------------------------------------------------------------------------------------------------------- |
| `example`          | `string` | **Required**     | The ID of the example to load (e.g., `"view"`). Matches the directory name in `docs/public/lynx-examples/`. |
| `defaultFile`      | `string` | `"package.json"` | The file path to display in the code editor initially.                                                      |
| `defaultEntryName` | `string` | -                | The specific entry point to run (if the example has multiple bundles).                                      |
| `img`              | `string` | -                | URL to a custom preview image (overrides the default `preview-image.png`).                                  |
| `highlight`        | `object` | -                | Line highlighting configuration. Format: `{ "path/to/file": "start-end" }`.                                 |
| `schema`           | `string` | -                | Custom schema URL pattern for the preview. Use `{{{url}}}` as a placeholder for the bundle URL.             |

### Advanced Example

```tsx
<Go
  example="view"
  defaultFile="src/App.tsx"
  defaultEntryName="main"
  highlight={{ 'src/App.tsx': '5-10' }}
/>
```

**This is an example below:  view**

**Bundle:** `dist/main.lynx.bundle` | Web: `dist/main.web.bundle`

```tsx 5-10
// Copyright 2024 The Lynx Authors. All rights reserved.
// Licensed under the Apache License Version 2.0 that can be found in the
// LICENSE file in the root directory of this source tree.

import type { ReactElement } from "react";

const RenderExample = () => {
  return (
    <view
      style={{
        borderLeftWidth: "15px",
        borderRightWidth: "60px",
        borderTopWidth: "100px",
        borderBottomWidth: "50px",
        borderColor: "green red",
        backgroundColor: "blue",
        width: "100vw",
        height: "500px",
      }}
    />
  );
};

const LayoutExample = () => {
  return (
    <view
      style={{
        width: "100vw",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        marginTop: "100px",
      }}
    >
      <text
        style={{
          fontSize: "50px",
          padding: "30px",
          background: "red",
        }}
      >
        Hello World
      </text>
      <text
        style={{
          fontSize: "50px",
          marginTop: "50px",
          padding: "30px",
          background: "green",
        }}
      >
        Hello Lynx
      </text>
    </view>
  );
};

export const App = () => {
  const examples: ReactElement[] = [
    <RenderExample />,
    <LayoutExample />,
  ];

  return (
    <scroll-view scroll-orientation="vertical" style="padding:5px;width:100%; height:100%;">
      <text className="title">View Examples</text>
      {examples.map((example, index) => example)}
    </scroll-view>
  );
};

```



***

## 2. Managing Example Packages

All interactive examples are managed as dependencies in the `packages/lynx-example-packages/` workspace.

### Directory Structure

```text
packages/lynx-example-packages/
├── package.json          # Manifest listing all example dependencies
├── pnpm-lock.yaml       # Lockfile for examples
└── node_modules/        # Where installed examples reside
    └── @lynx-example/   # Namespace for official examples
```

### Adding a New Example

To make a new example available to the `<Go>` component:

1. **Publish the Package**: Your example must be a valid npm package (e.g., `@lynx-example/my-feature`).
2. **Add Dependency**: Add the package to `packages/lynx-example-packages/package.json`.
3. **Install**: Run `pnpm install` in the workspace root to download the new example.
4. **Rebuild Assets**: The website build process will automatically detect and bundle the new example.

***

## 3. Build Architecture

For those interested in how it works under the hood:

- **Script**: `scripts/lynx-example.js` runs during the build.
- **Process**:
  1. Scans `node_modules/@lynx-example/` for packages.
  2. Identifies bundle files (`.lynx.bundle`, `.web.bundle`) and source code.
  3. Generates an `example-metadata.json` for each example.
  4. Copies assets to `docs/public/lynx-examples/`.
- **Runtime**: The `<Go>` component fetches this metadata at runtime to hydrate the editor and preview.
