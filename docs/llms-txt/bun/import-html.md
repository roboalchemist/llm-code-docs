# Source: https://bun.com/docs/guides/runtime/import-html.md

# Import a HTML file as text

To import a `.html` file in Bun as a text file, use the `type: "text"` attribute in the import statement.

```ts
import html from "./file.html" with { type: "text" };

console.log(html); // <!DOCTYPE html><html><head>...
```

This can also be used with hot module reloading and/or watch mode to force Bun to reload whenever the `./file.html` file changes.

```json
{
  "type": "module",
  "exports": {
    "html": "<!DOCTYPE html><html><head>..."
  }
}
```

```json
{
  "type": "hot-module-reload",
  "imports": [
    {
      "path": "./file.html",
      "options": {
        "type": "text"
      }
    }
  ]
}
```