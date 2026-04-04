# .prettierrc.toml
trailingComma = "es5"
tabWidth = 4
semi = false
singleQuote = true
```

## Configuration Overrides

Overrides let you have different configuration for certain file extensions, folders and specific files.

JSON:

```json
{
  "semi": false,
  "overrides": [
    {
      "files": "*.test.js",
      "options": {
        "semi": true
      }
    },
    {
      "files": ["*.html", "legacy/**/*.js"],
      "options": {
        "tabWidth": 4
      }
    }
  ]
}
```

YAML:

```yaml
semi: false
overrides:
  - files: "*.test.js"
    options:
      semi: true
  - files:
      - "*.html"
      - "legacy/**/*.js"
    options:
      tabWidth: 4
```

`files` is required for each override, and may be a string or array of strings. `excludeFiles` may be optionally provided to exclude files for a given rule, and may also be a string or array of strings.

## Setting the [parser](options.md#parser) option

By default, Prettier automatically infers which parser to use based on the input file extension. Combined with `overrides` you can teach Prettier how to parse files it does not recognize.

For example, to get Prettier to format its own `.prettierrc` file, you can do:

```json
{
  "overrides": [
    {
      "files": ".prettierrc",
      "options": { "parser": "json" }
    }
  ]
}
```

You can also switch to the `flow` parser instead of the default `babel` for .js files:

```json
{
  "overrides": [
    {
      "files": "*.js",
      "options": {
        "parser": "flow"
      }
    }
  ]
}
```

**Note:** _Never_ put the `parser` option at the top level of your configuration. _Only_ use it inside `overrides`. Otherwise you effectively disable Prettier’s automatic file extension based parser inference. This forces Prettier to use the parser you specified for _all_ types of files – even when it doesn’t make sense, such as trying to parse a CSS file as JavaScript.

## Configuration Schema

If you’d like a JSON schema to validate your configuration, one is available here: [https://www.schemastore.org/prettierrc.json](https://www.schemastore.org/prettierrc.json).

## EditorConfig

If a [`.editorconfig` file](https://editorconfig.org/) is in your project, Prettier will parse it and convert its properties to the corresponding Prettier configuration. This configuration will be overridden by `.prettierrc`, etc.

:::note

Unlike the EditorConfig spec, the search for `.editorconfig` file will stop on the project root and won't proceed further.

:::

Here’s an annotated description of how different properties map to Prettier’s behavior:

```ini