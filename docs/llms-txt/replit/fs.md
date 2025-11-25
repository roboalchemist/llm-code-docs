# Source: https://docs.replit.com/extensions/api/fs.md

# fs API

> Create, read, modify, and watch files and directories in your Replit App using the filesystem API methods and types.

The fs or filesystem API allows you to create, read, and modify files on the replit app's filesystem.

## Usage

```ts  theme={null}
import { fs } from '@replit/extensions';
```

## Methods

### `fs.readFile`

Reads the file specified at `path` and returns an object containing the contents, or an object containing an error if there was one. Required [permissions](./manifest#scopetype): `read`.

```ts  theme={null}
readFile(path: string, encoding: null | "utf8" | "binary"): Promise<{ content: string } | { error: string }>
```

### `fs.writeFile`

Writes the file specified at `path` with the contents `content`. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
writeFile(path: string, content: string | Blob): Promise<{ success: boolean } | { error: string }>
```

### `fs.readDir`

Reads the directory specified at `path` and returns an object containing the contents, or an object containing an error if there was one. Required [permissions](./manifest#scopetype): `read`.

```ts  theme={null}
readDir(path: string): Promise<{ children: DirectoryChildNode[], error: string }>
```

### `fs.createDir`

Creates a directory at the specified path. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
createDir(path: string): Promise<{ error: null | string, success: boolean }>
```

### `fs.deleteFile`

Deletes the file at the specified path. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
deleteFile(path: string): Promise<{} | { error: string }>
```

### `fs.deleteDir`

Deletes the directory at the specified path. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
deleteDir(path: string): Promise<{} | { error: string }>
```

### `fs.move`

Moves the file or directory at `from` to `to`. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
move(path: string, to: string): Promise<{ error: null | string, success: boolean }>
```

### `fs.copyFile`

Copies the file at `from` to `to`. Required [permissions](./manifest#scopetype): `read`, `write-exec`.

```ts  theme={null}
copyFile(path: string, to: string): Promise<{ error: null | string, success: boolean }>
```

### `fs.watchFile`

Watches the file at `path` for changes with the provided `listeners`. Returns a dispose method which cleans up the listeners. Required [permissions](./manifest#scopetype): `read`.

```ts  theme={null}
watchFile(path: string, listeners: WatchFileListeners<string>, encoding: "utf8" | "binary"): Promise<DisposerFunction>
```

### `fs.watchDir`

Watches file events (move, create, delete) in the specified directory at the given `path`. Returns a dispose method which cleans up the listeners. Required [permissions](./manifest#scopetype): `read`.

```ts  theme={null}
watchDir(path: string, listeners: WatchDirListeners): Promise<DisposerFunction>
```

### `fs.watchTextFile`

Watches a text file at `path` for changes with the provided `listeners`. Returns a dispose method which cleans up the listeners.

Use this for watching text files, and receive changes as versioned operational transform (OT) operations annotated with their source.

Required [permissions](./manifest#scopetype): `read`.

```ts  theme={null}
watchTextFile(path: string, listeners: WatchTextFileListeners): Function
```

## Types

### ChangeEventType

A file change event type

| Property | Type |
| -------- | ---- |

### DeleteEvent

Fired when a file is deleted

| Property  | Type                |
| --------- | ------------------- |
| eventType | `Delete`            |
| node      | [`FsNode`](#fsnode) |

### DirectoryChildNode

A directory child node - a file or a folder.

| Property | Type                        |
| -------- | --------------------------- |
| filename | `string`                    |
| type     | [`FsNodeType`](#fsnodetype) |

### FsNode

A base interface for nodes, just includes
the type of the node and the path, This interface
does not expose the node's content/children

| Property | Type                        |
| -------- | --------------------------- |
| path     | `string`                    |
| type     | [`FsNodeType`](#fsnodetype) |

### FsNodeType

A Filesystem node type

| Property | Type |
| -------- | ---- |

### MoveEvent

Fired when a file is moved

| Property  | Type                |
| --------- | ------------------- |
| eventType | `Move`              |
| node      | [`FsNode`](#fsnode) |
| to        | `string`            |

### TextChange

A written text change for the WriteChange function exposed by WatchTextFileListeners.onReady

| Property | Type     |
| -------- | -------- |
| from     | `number` |
| insert?  | `string` |
| to?      | `number` |

### TextFileOnChangeEvent

Signifies a change when a text file's text content is updated

| Property      | Type                          |
| ------------- | ----------------------------- |
| changes       | [`TextChange[]`](#textchange) |
| latestContent | `string`                      |

### TextFileReadyEvent

A set of listeners and values exposed by WatchTextFileListeners.onReady

| Property         | Type                                    |
| ---------------- | --------------------------------------- |
| getLatestContent | [`GetLatestContent`](#getlatestcontent) |
| initialContent   | `string`                                |
| writeChange      | [`WriteChange`](#writechange)           |

### WatchDirListeners

A set of listeners for watching a directory

| Property        | Type                                                                |
| --------------- | ------------------------------------------------------------------- |
| onChange        | [`WatchDirOnChangeListener`](#watchdironchangelistener)             |
| onError         | [`WatchDirOnErrorListener`](#watchdironerrorlistener)               |
| onMoveOrDelete? | [`WatchDirOnMoveOrDeleteListener`](#watchdironmoveordeletelistener) |

### WatchFileListeners

A set of listeners for watching a non-text file\<`T extends string | Blob = string`>

| Property        | Type                                                                  |
| --------------- | --------------------------------------------------------------------- |
| onChange        | [`WatchFileOnChangeListener<T>`](#watchfileonchangelistener)          |
| onError?        | [`WatchFileOnErrorListener`](#watchfileonerrorlistener)               |
| onMoveOrDelete? | [`WatchFileOnMoveOrDeleteListener`](#watchfileonmoveordeletelistener) |

### WatchTextFileListeners

A set of listeners for watching a text file

| Property        | Type                                                                          |
| --------------- | ----------------------------------------------------------------------------- |
| onChange?       | [`WatchTextFileOnChangeListener`](#watchtextfileonchangelistener)             |
| onError?        | [`WatchTextFileOnErrorListener`](#watchtextfileonerrorlistener)               |
| onMoveOrDelete? | [`WatchTextFileOnMoveOrDeleteListener`](#watchtextfileonmoveordeletelistener) |
| onReady         | [`WatchTextFileOnReadyListener`](#watchtextfileonreadylistener)               |

### ChangeEventType

A file change event type

```ts  theme={null}
Create = 'CREATE'
Delete = 'DELETE'
Modify = 'MODIFY'
Move = 'MOVE'
```

### FsNodeType

A Filesystem node type

```ts  theme={null}
Directory = 'DIRECTORY'
File = 'FILE'
```

### DisposerFunction

A cleanup/disposer function (void)

```ts  theme={null}
() => void
```

### FsNodeArray

```ts  theme={null}
Array<FsNode>
```

### GetLatestContent

Returns the latest content of a watched file as a string

```ts  theme={null}
() => string
```

### WatchDirOnChangeListener

Fires when a directory's child nodes change

```ts  theme={null}
(children: FsNodeArray) => void
```

### WatchDirOnErrorListener

Fires when watching a directory fails

```ts  theme={null}
(err: Error, extraInfo: Record) => void
```

### WatchDirOnMoveOrDeleteListener

Fires when a watched directory is moved or deleted

```ts  theme={null}
(event: DeleteEvent | MoveEvent) => void
```

### WatchFileOnChangeListener

Fires when a non-text file is changed

```ts  theme={null}
(newContent: T) => void
```

### WatchFileOnErrorListener

Fires when watching a non-text file fails

```ts  theme={null}
(error: string) => void
```

### WatchFileOnMoveOrDeleteListener

Fires when a non-text file is moved or deleted

```ts  theme={null}
(moveOrDeleteEvent: MoveEvent | DeleteEvent) => void
```

### WatchTextFileOnChangeListener

Fires when a watched text file's text content is updated

```ts  theme={null}
(changeEvent: TextFileOnChangeEvent) => void
```

### WatchTextFileOnErrorListener

Fires when watching a text file fails

```ts  theme={null}
(error: string) => void
```

### WatchTextFileOnMoveOrDeleteListener

Fires when a watched text file is moved or deleted

```ts  theme={null}
(moveOrDeleteEvent: MoveEvent | DeleteEvent) => void
```

### WatchTextFileOnReadyListener

Fires when a text file watcher is ready

```ts  theme={null}
(readyEvent: TextFileReadyEvent) => void
```

### WriteChange

Writes a change to a watched file using the TextChange interface

```ts  theme={null}
(changes: TextChange | Array<TextChange>) => void
```
