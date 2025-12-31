# Source: https://docs.replit.com/extensions/api/commands.md

# commands API

> Register and manage custom commands for the Replit command bar and other extension points using the commands API module.

The `commands` api module allows you to register commands that can be run from the CLUI command bar and other contribution points.

## Usage

```ts  theme={null}
import { commands } from '@replit/extensions';
```

## Methods

### `commands.add`

Adds a command to the command system.

```ts  theme={null}
add(__namedParameters: AddCommandArgs): void
```

## Types

### ActionCommandArgs

```ts  theme={null}
undefined
```

### BaseCommandArgs

```ts  theme={null}
undefined
```

### CommandArgs

```ts  theme={null}
ActionCommandArgs | ContextCommandArgs
```

### CommandFnArgs

```ts  theme={null}
undefined
```

### CommandProxy

```ts  theme={null}
 |
```

### CommandsFn

```ts  theme={null}
(args: CommandFnArgs) => Promise
```

### ContextCommandArgs

```ts  theme={null}
undefined
```

### CreateCommand

```ts  theme={null}
(args: CommandFnArgs) => undefined
```

### Run

```ts  theme={null}
() => any
```

### SerializableValue

```ts  theme={null}
string | number | boolean |  | undefined |  |
```
