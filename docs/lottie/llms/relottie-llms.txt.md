# Source: https://developers.lottiefiles.com/relottie-llms.txt

# using reLottie

> `relottie` is an ecosystem for processing Lottie JSON files using plugins. It is built on `unified`, an engine for processing content with Abstract Syntax Trees (ASTs). `relottie` parses Lottie JSON into a **LAST (Lottie Abstract Syntax Tree)**, allowing for structured inspection and modification.

## Core Concepts

*   **LAST (Lottie Abstract Syntax Tree)**: A `unist`-compliant specification for representing Lottie JSON. Nodes have a `type` and a semantic `title` (e.g., `'layer-image'`, `'transform-opacity'`) that provides Lottie-specific meaning. The root node also has a `hasExpressions` flag for security awareness.
*   **Processor Pipeline**: `relottie` uses a `parse` -> `transform` -> `stringify` pipeline.
    1.  **Parse**: Input Lottie JSON string is parsed into a LAST tree (`@lottiefiles/relottie-parse`).
    2.  **Transform**: One or more transformer plugins run sequentially, inspecting or modifying the tree.
    3.  **Stringify**: The final LAST tree is converted back into a Lottie JSON string (`@lottiefiles/relottie-stringify`).
*   **VFile**: A virtual file representation that carries content and metadata (`vfile.data`) through the pipeline. Plugins attach their results (e.g., extracted metadata) to `vfile.data`.
*   **Tree Traversal**: Use `unist-util-visit` to navigate the LAST tree within a plugin to find and act upon specific nodes.

## Quick Start

1.  **Installation**:
    ```bash
    npm install @lottiefiles/relottie @lottiefiles/last unist-util-visit
    npm install unified vfile -D
    ```

2.  **Example Usage**:
    Create a processor, add a plugin, and process a Lottie JSON string.

    ```typescript
    import { relottie } from "@lottiefiles/relottie";
    import type { Plugin, Transformer } from "unified";
    import type { Root, Attribute, Primitive } from "@lottiefiles/last";
    import { TITLES } from "@lottiefiles/last";
    import { visit, EXIT } from "unist-util-visit";

    // A simple plugin to change the framerate
    const changeFrameratePlugin: Plugin<[{ fr: number }], Root> = (options) => {
      const transformer: Transformer<Root> = (tree) => {
        visit(tree, "attribute", (node: Attribute) => {
          if (node.title === TITLES.number.framerate) {
            (node.children[0] as Primitive).value = options!.fr;
            return EXIT;
          }
        });
      };
      return transformer;
    };

    const lottieJson = '{"v":"5.5.7","fr":30,"w":512,"h":512,"layers":[]}';

    const file = await relottie()
      .use(changeFrameratePlugin, { fr: 60 })
      .process(lottieJson);

    console.log(String(file));
    // Output: {"v":"5.5.7","fr":60,"w":512,"h":512,"layers":[]}
    ```

## Guides

### Analyzing Lottie Files
Use plugins to extract information without modifying the Lottie.

*   **`@lottiefiles/relottie-metadata`**: Extracts common properties like dimensions, framerate, duration, and colors used. The results are attached to `vfile.data.metadata`.
*   **`@lottiefiles/relottie-extract-features`**: Determines which Lottie features are used in the animation (e.g., `'layer-image'`, `'shape-rect'`). The results are a `Map` attached to `vfile.data['extract-features']`.

```typescript
import { relottie } from "@lottiefiles/relottie";
import relottieMetadata from "@lottiefiles/relottie-metadata";
import relottieExtractFeatures from "@lottiefiles/relottie-extract-features";

const file = await relottie()
  .use(relottieMetadata)
  .use(relottieExtractFeatures)
  .process(lottieJson);

// Access extracted data
console.log(file.data.metadata);
console.log(file.data['extract-features']);
```

### Modifying Lottie Files
Create custom transformer plugins to programmatically edit the LAST tree. Common patterns include:
*   **Changing Primitive Values**: Find a node (e.g., an `Attribute`) and update the `.value` of its child `Primitive` node.
*   **Adding Nodes**: Create new LAST nodes using `@lottiefiles/last-builder` and insert them into the `children` array of a parent.
*   **Removing Nodes**: Find a node and use its `parent` and `index` (provided by `unist-util-visit`) to `splice` it from the parent's `children` array.

### Using the CLI (`@lottiefiles/relottie-cli`)
Process Lottie files from the terminal. Useful for batch operations.

```bash
# Install
npm install -g @lottiefiles/relottie-cli

# Usage: process a file and output to stdout
relottie input.json

# Use a plugin and write to a new file
relottie input.json --use ./my-plugin.js -o output.json

# Output the LAST tree instead of Lottie JSON
relottie input.json --tree-out
```
Configuration can be managed via `.relottierc.js` or a `relottieConfig` key in `package.json`.

### Creating Plugins
A plugin is a function that returns a `transformer` function. The transformer receives the LAST `tree` and the `VFile`.

```typescript
import type { Plugin, Transformer } from "unified";
import type { Root } from "@lottiefiles/last";

const myPlugin: Plugin<[options?], Root> = (options = {}) => {
  const transformer: Transformer<Root> = (tree, file) => {
    // Traverse and modify the tree here
    // Attach results to file.data
  };
  return transformer;
};
```

## API Reference

### Core Plugins
*   **`@lottiefiles/relottie-parse`**: Parses Lottie JSON string into a LAST tree. It is built on the `momoa` JSON parser.
*   **`@lottiefiles/relottie-stringify`**: Serializes a LAST tree back into a Lottie JSON string. Can be configured with a `space` option for pretty-printing.

### Utility Plugins
*   **`@lottiefiles/relottie-metadata`**: Extracts metadata (dimensions, framerate, etc.).
*   **`@lottiefiles/relottie-extract-features`**: Analyzes and reports which Lottie features are used.

### LAST Builder (`@lottiefiles/last-builder`)
Provides helper functions (`rt`, `at`, `el`, `pt`, etc.) to programmatically construct LAST nodes, which is useful for generating Lottie files from scratch or for creating nodes within a transformer plugin.

### Security Considerations
`relottie` itself does not execute JavaScript expressions found in Lottie files. However, it's a security risk if those expressions are rendered by a player that executes them. The `Root` node of the LAST tree contains a `hasExpressions: boolean` flag to help identify animations that contain expressions so they can be handled with care.