# Source: https://docs.replit.com/extensions/api/session.md

# session API

> Access and manage the current user's coding session in the Replit workspace, including active file tracking and change listeners.

The session api provides you with information on the current user's coding session in the workspace.

## Usage

```ts  theme={null}
import { session } from '@replit/extensions';
```

## Methods

### `session.onActiveFileChange`

Sets up a listener to handle when the active file is changed

```ts  theme={null}
onActiveFileChange(listener: OnActiveFileChangeListener): DisposerFunction
```

### `session.getActiveFile`

Returns the current file the user is focusing

```ts  theme={null}
getActiveFile(): Promise<null | string>
```

## Types

### DisposerFunction

A cleanup/disposer function (void)

```ts  theme={null}
() => void
```

### OnActiveFileChangeListener

Fires when the current user switches to a different file/tool in the workspace.  Returns null if the current file/tool cannot be found in the filesystem.

```ts  theme={null}
(file: string | ) => void
```
