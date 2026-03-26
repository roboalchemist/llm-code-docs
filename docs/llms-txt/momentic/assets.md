# Source: https://momentic.ai/docs/mobile-cli/commands/assets.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# assets

Manage and upload assets.

## `upload`

Upload an APK asset to Momentic Cloud. After upload, this asset can be used in
both the interactive editor and in test runs.

The file provided must exist on disk and be an Android APK (`.apk`).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```
</CodeGroup>

### Options

#### `--channel <channel>`

Release channel for the asset, such as `staging` or `dev`. This name affects how
the APK will be referenced by tests. Channels cannot be renamed after creation.

#### `--tag <tag>`

Version label within the channel. This could be a semantic version like `0.0.1`
or a floating tag like `latest`. If omitted, defaults to `latest`.

## `download`

Download a mobile asset (APK) from Momentic Cloud to the local machine.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```
</CodeGroup>

### Arguments

#### `[path]`

Optional path to download the asset to. Can be a directory or a file path. If
omitted, defaults to the current working directory. If a directory is provided,
the file will be named `<channel>-<tag>.apk`.

### Options

#### `--channel <channel>`

**Required**. Release channel for the asset to download.

#### `--tag <tag>`

**Required**. Version label within the channel to download.


Built with [Mintlify](https://mintlify.com).