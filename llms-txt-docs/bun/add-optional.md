# Source: https://bun.com/docs/guides/install/add-optional.md

# Add an optional dependency

To add an npm package as an optional dependency, use the `--optional` flag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun add zod --optional
```

***

This will add the package to `optionalDependencies` in `package.json`.

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "optionalDependencies": {
    "zod": "^3.0.0" // [!code ++]
  }
}
```

***

See [Docs > Package manager](https://bun.com/docs/cli/install) for complete documentation of Bun's package manager.
