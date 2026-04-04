# Source: https://developers.webflow.com/code-components/webpack-configuration-overrides.mdx

***

title: Webpack Configuration Overrides
subtitle: >-
Customize your webpack configuration for advanced implementation of code
components
slug: webpack-configuration-overrides
description: Customize your webpack configuration for advanccode components
keywords: 'webpack, configuration, customization, code components'
------------------------------------------------------------------

This guide covers how to customize your webpack configuration for advanced implementation of code components.

## Overview

The CLI uses an internal webpack configuration optimized for Webflow's requirements, including Module Federation, CSS extraction, TypeScript/React support, and other optimizations. When you need to customize this configuration, you can provide an override configuration file that will be merged with the base configuration.

### Review the default configuration

To view the webpack configuration used to bundle your library, use the `--debug-bundler` flag when running `library` commands:

```shell
npx webflow library bundle --debug-bundler
```

This will output the final merged webpack configuration to help you understand how your overrides are being applied.

## Configuration file setup

<Steps>
  <Step title="Specify the configuration path">
    In your [`webflow.json` manifest file](/code-components/installation#webflowjson), add a `bundleConfig` property pointing to your configuration file:

    ```json title="webflow.json"
    {
      "library": {
        "name": "My Library",
        "components": ["./src/components/**/*.webflow.{js,ts,tsx}"],
        "bundleConfig": "./webpack.override.js"
      }
    }
    ```
  </Step>

  <Step title="Create your override configuration">
    Create a CommonJS module that exports your webpack configuration overrides, for example:

    ```javascript title="webpack.override.js"
    module.exports = {
      resolve: {
        extensions: [".js", ".ts", ".tsx", ".json"],
      },
      // ...other custom configurations go here
    };
    ```
  </Step>
</Steps>

## Configuration API

Your override configuration should follow the standard [Webpack Configuration API](https://webpack.js.org/configuration/) with the following important exceptions and special handling:

### Blocked properties

The following properties are **automatically filtered out** and can't be overridden for security and compatibility reasons:

| Property | Description                                                                                                                      |
| -------- | -------------------------------------------------------------------------------------------------------------------------------- |
| `entry`  | Specifies the entry points for the application bundle. Determines which files webpack starts building the dependency graph from. |
| `output` | Defines how and where webpack emits the bundled files, including output directory and filename patterns.                         |
| `target` | Sets the environment in which the bundle should run (e.g., `web`, `node`). Affects how webpack builds and optimizes the output.  |

If you attempt to override these properties, a warning will be logged and they will be ignored.

### Special property handling

#### Module rules

Instead of providing an array of rules, you must provide a **function** that receives the current rules and returns the modified rules array:

```javascript
module.exports = {
  module: {
    rules: (currentRules) => {
      // Your custom logic adding/modifying loaders goes here
      return modifiedRules;
    },
  },
};
```

#### Plugins

Your custom `plugins` array is merged with the default configuration using `webpack-merge`.

To prevent common build errors, the following plugins are automatically de-duplicated, ensuring only one instance is present in the final configuration:

* `ModuleFederationPlugin`
* `MiniCssExtractPlugin`

## Examples

### Add a new loader

To handle file types that build on existing configurations (like SCSS extending CSS), you can add a new rule that reuses parts of an existing loader chain. This ensures consistency and compatibility.

<Note title="Support for common CSS frameworks">
  Code components support popular CSS frameworks and libraries, including Tailwind CSS, styled-components, and Emotion, material UI, shadcn/ui, and more. For detailed guidance on using these frameworks with code components, see the [frameworks and libraries guide](/code-components/frameworks-and-libraries).
</Note>

The example below adds a rule for `.scss` files by finding the existing CSS rule and appending `sass-loader` to it:

```javascript title="webpack.override.js"
module.exports = {
  module: {
    rules: (currentRules) => {
      const currentCSSRule = currentRules.find(
        (rule) =>
          rule.test instanceof RegExp &&
          rule.test.test("test.css") &&
          Array.isArray(rule.use)
      );
      return [
        ...currentRules,
        {
          test: /\.scss$/,
          use: [...currentCSSRule.use, "sass-loader"],
        },
      ];
    },
  },
};
```

### Add a new rule

To process custom file types not handled by the default configuration, add a new rule. The following example adds `markdown-loader` to handle `.md` files:

```javascript title="webpack.override.js"
module.exports = {
  module: {
    rules: (currentRules) => {
      return [
        ...currentRules,
        {
          test: /\.md$/,
          use: ["markdown-loader"],
        },
      ];
    },
  },
};
```

### Extend an existing loader

You can modify the options for an existing loader to customize its behavior. This requires finding the specific rule and then updating its `options` object.

The following example shows how to modify the `css-loader` to change its configuration for CSS Modules:

```javascript title="webpack.override.js"
module.exports = {
  module: {
    // Override the existing rules to modify CSS processing
    rules: (currentRules) => {
      return currentRules.map((rule) => {
        // Find the rule that handles CSS files
        if (
          rule.test instanceof RegExp &&
          rule.test.test("test.css") &&
          Array.isArray(rule.use)
        ) {
          for (const [index, loader] of rule.use.entries()) {
            // Find the css-loader
            if (typeof loader === "object" && loader?.ident === "css-loader") {
              // Preserve existing options and add a custom configuration
              const options =
                typeof loader.options === "object" ? loader.options : {};
              rule.use[index] = {
                ...loader,
                options: {
                  ...options,
                  modules: {
                    exportLocalsConvention: "as-is", // Use original class names
                    namedExport: false, // ⚠️ Allow dot notation access
                  },
                },
              };
            }
          }
        }
        return rule;
      });
    },
  },
};
```

### Add custom plugins

To add custom build-time functionality, provide an array of plugins. This example shows how to add a custom plugin to the configuration:

```javascript title="webpack.override.js"
const MyCustomPlugin = require("./my-custom-plugin");

module.exports = {
  plugins: [
    new MyCustomPlugin({
      option: "value",
    }),
  ],
};
```

### Provide aliases

To create shorter, more convenient import paths, define aliases in the `resolve.alias` object. This example creates an `@` alias that points to the project's root directory:

```javascript title="webpack.override.js"
module.exports = {
  resolve: {
    alias: {
      "@": process.cwd(),
    },
  },
};
```

## Best practices

1. **Use functions for module rules**: Always provide a function for `module.rules` to ensure proper integration with existing rules
2. **Minimal changes**: Only override what you absolutely need to customize
3. **Check for conflicts**: Ensure your custom loaders don't conflict with existing ones

## Troubleshooting

<Accordion title="Configuration not loading">
  * Ensure the `bundleConfig` path in your `webflow.json` is correct and relative to your project root.
  * Verify your configuration file exports a valid object using `module.exports`.
</Accordion>

<Accordion title="Rules not working">
  * Make sure you're providing a function for `module.rules`, not an array.
  * Check that your rule matching logic correctly identifies the rules you want to modify.
</Accordion>

<Accordion title="Plugins conflicting">
  * Remember that `ModuleFederationPlugin` and `MiniCssExtractPlugin` are automatically de-duplicated.
  * Ensure custom plugins don't conflict with the base configuration.
</Accordion>

For more information about webpack configuration options, refer to the [official Webpack documentation](https://webpack.js.org/configuration/).
