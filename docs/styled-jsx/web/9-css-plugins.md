# CSS Preprocessing with Plugins

styled-jsx supports CSS preprocessing via a plugin system. Plugins enable using popular preprocessors like Sass, Less, Stylus, and PostCSS at compile time.

## How Plugins Work

Plugins are regular JavaScript modules that export a function:

```typescript
function plugin(css: string, options: Object): string
```

**Parameters:**
- `css` — CSS string to process
- `options` — User options + Babel options

**Return:** Modified CSS string

Plugins are applied in definition order (left to right) before styles are scoped.

## Registering Plugins

Add a `plugins` array to your `styled-jsx/babel` configuration:

```json
{
  "plugins": [
    [
      "styled-jsx/babel",
      {
        "plugins": [
          "my-styled-jsx-plugin-package",
          "/full/path/to/local/plugin"
        ]
      }
    ]
  ]
}
```

Plugins are resolved as npm packages or file paths.

## Plugin Options

Pass options to plugins as an array:

```json
{
  "plugins": [
    [
      "styled-jsx/babel",
      {
        "plugins": [
          ["my-styled-jsx-plugin-package", { "exampleOption": true }]
        ],
        "sourceMaps": true
      }
    ]
  ]
}
```

Each plugin receives an `options` object as the second argument:

```js
module.exports = (css, options) => {
  // options.exampleOption === true
  // options.babel contains Babel-specific options
  return modifiedCss
}
```

## Options Object Structure

```js
{
  // User-provided options
  exampleOption: true,

  // Babel options
  babel: {
    sourceMaps: boolean,
    vendorPrefixes: boolean,
    isGlobal: boolean,
    filename: ?string,  // Only when Babel CLI or Webpack used
    location: {
      start: { line: number, column: number },
      end: { line: number, column: number }
    }
  }
}
```

## Important: Template Literal Placeholders

When applying plugins, styled-jsx replaces template literal expressions with placeholders:

```css
/* Expression is replaced with placeholder */
%%styled-jsx-placeholder-ExprNumber%%
```

This allows CSS parsers to work with valid CSS. **Plugins don't transform expressions** — dynamic styles remain as-is.

## Official Example Plugins

- [styled-jsx-plugin-sass](https://github.com/giuseppeg/styled-jsx-plugin-sass) — Sass preprocessor
- [styled-jsx-plugin-postcss](https://github.com/giuseppeg/styled-jsx-plugin-postcss) — PostCSS integration
- [styled-jsx-plugin-stylelint](https://github.com/giuseppeg/styled-jsx-plugin-stylelint) — Stylelint linting
- [styled-jsx-plugin-less](https://github.com/erasmo-marin/styled-jsx-plugin-less) — Less preprocessor
- [styled-jsx-plugin-stylus](https://github.com/omardelarosa/styled-jsx-plugin-stylus) — Stylus preprocessor

## Creating a Plugin

A simple plugin example that adds vendor prefixes:

```js
// my-plugin.js
module.exports = (css, options) => {
  // Check if this is a global style
  if (options.babel.isGlobal) {
    // Transform CSS
    return css.replace(/display: flex/g, 'display: -webkit-flex')
  }
  return css
}
```

## Plugin Naming Convention

When publishing a plugin, use this naming convention:

```
styled-jsx-plugin-<your-plugin-name>
```

Add keywords: `styled-jsx` and `styled-jsx-plugin`

## Next.js Integration

To use plugins in Next.js, create a `.babelrc` file:

```json
{
  "presets": [
    [
      "next/babel",
      {
        "styled-jsx": {
          "plugins": ["styled-jsx-plugin-postcss"]
        }
      }
    ]
  ]
}
```

Ensure you're using a version of Next.js that supports passing options to styled-jsx.

## Execution Order

Plugins are applied in left-to-right order before scoping:

```json
{
  "plugins": [
    [
      "styled-jsx/babel",
      {
        "plugins": [
          "plugin-a",  // Runs first
          "plugin-b",  // Runs second
          "plugin-c"   // Runs third
        ]
      }
    ]
  ]
}
```

Each plugin receives the output of the previous plugin.

## Example: Using PostCSS

```json
{
  "plugins": [
    [
      "styled-jsx/babel",
      {
        "plugins": ["styled-jsx-plugin-postcss"]
      }
    ]
  ]
}
```

Create a `postcss.config.js`:

```js
module.exports = {
  plugins: [
    require('autoprefixer'),
    require('cssnano')
  ]
}
```

Now styles are automatically prefixed and minified before being scoped.
