# Source: https://bun.com/docs/guides/install/add-peer.md

# Add a peer dependency

To add an npm package as a peer dependency, use the `--peer` flag.

```sh terminal icon="terminal" theme={"theme":{"light":"github-light","dark":"dracula"}}
bun add @types/bun --peer
```

***

This will add the package to `peerDependencies` in `package.json`.

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "peerDependencies": {
    "@types/bun": "^1.3.2" // [!code ++]
  }
}
```

***

Running `bun install` will install peer dependencies by default, unless marked optional in `peerDependenciesMeta`.

```json package.json icon="file-json" theme={"theme":{"light":"github-light","dark":"dracula"}}
{
  "peerDependencies": {
    "@types/bun": "^1.3.2"
  },
  "peerDependenciesMeta": {
    "@types/bun": { // [!code ++]
      "optional": true // [!code ++]
    } // [!code ++]
  }
}
```

***

See [Docs > Package manager](https://bun.com/docs/cli/install) for complete documentation of Bun's package manager.
