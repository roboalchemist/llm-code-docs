# Source: https://docs.replit.com/extensions/api/exec.md

# exec API

> Learn how to run shell commands in Replit Apps using the exec API module. Includes methods for spawning processes and executing commands.

The `exec` api module allows you to execute arbitrary shell commands.

## Usage

```ts  theme={null}
import { exec } from '@replit/extensions';
```

## Methods

### `exec.spawn`

Spawns a command, with given arguments and environment variables. Takes in callbacks,
and returns an object containing a promise that resolves when the command exits, and
a dispose function to kill the process.

```ts  theme={null}
spawn(options: SpawnOptions): SpawnOutput
```

### `exec.exec`

Executes a command in the shell, with given arguments and environment variables

```ts  theme={null}
exec(command: string, options: { env: Record<string, string> }): Promise<ExecResult>
```

## Types

### BaseSpawnOptions

| Property     | Type                     |
| ------------ | ------------------------ |
| args         | `string[]`               |
| env?         | `Record<string, string>` |
| splitStderr? | `boolean`                |

### CombinedStderrSpawnOptions

| Property     | Type                     |
| ------------ | ------------------------ |
| args         | `string[]`               |
| env?         | `Record<string, string>` |
| onOutput?    | `Function`               |
| splitStderr? | `false`                  |

### ExecResult

| Property | Type     |
| -------- | -------- |
| exitCode | `number` |
| output   | `string` |

### SpawnOutput

| Property      | Type                   |
| ------------- | ---------------------- |
| dispose       | `Function`             |
| resultPromise | `Promise<SpawnResult>` |

### SpawnResult

| Property | Type            |
| -------- | --------------- |
| error    | `null │ string` |
| exitCode | `number`        |

### SplitStderrSpawnOptions

| Property    | Type                                      |
| ----------- | ----------------------------------------- |
| args        | `string[]`                                |
| env?        | `Record<string, string>`                  |
| onStdErr?   | [`OutputStrCallback`](#outputstrcallback) |
| onStdOut?   | [`OutputStrCallback`](#outputstrcallback) |
| splitStderr | `true`                                    |

### OutputStrCallback

```ts  theme={null}
(output: string) => void
```

### SpawnOptions

```ts  theme={null}
SplitStderrSpawnOptions | CombinedStderrSpawnOptions
```
