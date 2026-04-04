# Babel Configuration

The `styled-jsx/babel` plugin accepts several configuration options:

## optimizeForSpeed

Enables a blazing fast and optimized CSS rules injection system based on CSSOM APIs.

```json
{
  "plugins": [["styled-jsx/babel", { "optimizeForSpeed": true }]]
}
```

**Details:**
- Automatically enabled in production (`process.env.NODE_ENV === 'production'`)
- When enabled, source maps cannot be generated
- Styles cannot be edited via DevTools
- Use only when you don't need debugging capabilities

## sourceMaps

Generates source maps for styles (default: `false`)

```json
{
  "plugins": [["styled-jsx/babel", { "sourceMaps": true }]]
}
```

**Note:** Source maps are incompatible with `optimizeForSpeed`.

## styleModule

Specifies the module that transpiled files should import (default: `styled-jsx/style`)

```json
{
  "plugins": [["styled-jsx/babel", { "styleModule": "styled-jsx/style" }]]
}
```

This rarely needs to be changed unless you're doing advanced customizations.

## vendorPrefixes

Turn on/off automatic vendor prefixing (default: `true`)

```json
{
  "plugins": [["styled-jsx/babel", { "vendorPrefixes": true }]]
}
```

When enabled, vendor-prefixed versions of CSS properties are automatically added for browser compatibility.

## Complete Configuration Example

```json
{
  "plugins": [
    [
      "styled-jsx/babel",
      {
        "optimizeForSpeed": false,
        "sourceMaps": true,
        "styleModule": "styled-jsx/style",
        "vendorPrefixes": true
      }
    ]
  ]
}
```

## Environment-Specific Configuration

Use Babel's `env` option to apply different settings per environment:

```json
{
  "env": {
    "production": {
      "plugins": [
        ["styled-jsx/babel", { "optimizeForSpeed": true }]
      ]
    },
    "development": {
      "plugins": [
        ["styled-jsx/babel", { "sourceMaps": true }]
      ]
    }
  }
}
```
