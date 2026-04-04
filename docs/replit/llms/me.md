# Source: https://docs.replit.com/extensions/api/me.md

# me API

> Access information about the current extension context, including file paths for file handlers and extension-specific data.

The `me` api module exposes information specific to the current extension.

## Usage

```ts  theme={null}
import { me } from '@replit/extensions';
```

## Methods

### `me.filePath`

Returns the path to the current file the extension is opened with, if it is a [File Handler](/extensions#file-handler-file-editors-and-icons).

```ts  theme={null}
filePath(): Promise<string>
```
