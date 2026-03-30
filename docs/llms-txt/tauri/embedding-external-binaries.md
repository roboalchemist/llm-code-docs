# Embedding External Binaries

You may need to embed external binaries to add additional functionality to your application or prevent users from installing additional dependencies (e.g., Node.js or Python). We call this binary a `sidecar`.

Binaries are executables written in any programming language. Common use cases are Python CLI applications or API servers bundled using `pyinstaller`.

To bundle the binaries of your choice, you can add the `externalBin` property to the `tauri > bundle` object in your `tauri.conf.json`.
The `externalBin` configuration expects a list of strings targeting binaries either with absolute or relative paths.

Here is a Tauri configuration snippet to illustrate a sidecar configuration:

```json title="src-tauri/tauri.conf.json"
{
  "bundle": {
    "externalBin": [
      "/absolute/path/to/sidecar",
      "../relative/path/to/binary",
      "binaries/my-sidecar"
    ]
  }
}
```

:::note

The relative paths are relative to the `tauri.conf.json` file which is in the `src-tauri` directory.
So `binaries/my-sidecar` would represent `<PROJECT ROOT>/src-tauri/binaries/my-sidecar`.

:::

To make the external binary work on each supported architecture, a binary with the same name and a `-$TARGET_TRIPLE` suffix must exist on the specified path.
For instance, `"externalBin": ["binaries/my-sidecar"]` requires a `src-tauri/binaries/my-sidecar-x86_64-unknown-linux-gnu` executable on Linux or `src-tauri/binaries/my-sidecar-aarch64-apple-darwin` on Mac OS with Apple Silicon.

You can find your **current** platform's `-$TARGET_TRIPLE` suffix by running the following command:

```sh
rustc --print host-tuple
```

This directly outputs your host's target triple (e.g., `x86_64-unknown-linux-gnu` or `aarch64-apple-darwin`).

:::note
The `--print host-tuple` flag was added in Rust 1.84.0. If you're using an older version, you'll need to parse the output of `rustc -Vv` instead:

```sh