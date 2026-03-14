# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/cargo-private-packages.md

# Cargo - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. Follow the steps below to configure private Cargo packages.

1. Navigate to the [autofix settings](https://app.aikido.dev/issues/fix/settings) page and click on "*Connect Registry*"
2. Select *Cargo*

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FuXqkBSsQEpPGLwxQZo2K%2Fimage.png?alt=media&#x26;token=7775f433-3a26-4c78-bf71-7841d49b4189" alt=""><figcaption></figcaption></figure>

1. Cargo uses the `CARGO_REGISTRIES_<INDEX_NAME>_TOKEN` environment variables for token-based authentication to a registry named `<INDEX_NAME>`.&#x20;

For example for the following `config.toml` file:

```
[registries.example]
index = "https://example.com/git/index"
```

You can use `CARGO_REGISTRIES_EXAMPLE_TOKEN` to set the token for the example registry.

1. Click on "*Save*"
