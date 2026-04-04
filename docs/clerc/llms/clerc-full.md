# Clerc Documentation

Source: https://clerc.so1ve.dev/llms-full.txt

---

---

url: /reference/api/advanced-types.md
---

# @clerc/advanced-types

## Classes

[FlagValidationError](Class.FlagValidationError.md)

‐

## Functions

[Enum](Function.Enum.md)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

**Example**

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

**Throws**

If the value is not in the allowed values list

[Range](Function.Range.md)

Creates a range type function that validates the input is a number within the
specified range.

**Throws**

If the value is not a number or is outside the specified
range

[Regex](Function.Regex.md)

Creates a regex type function that validates the input against the provided
pattern.

**Throws**

If the value does not match the regex pattern

---

---

url: /reference/api/core.md
---

# @clerc/core

## Namespaces

[Parser](Namespace.Parser.md)

‐

[Types](Namespace.Types.md)

‐

## Classes

[Clerc](Class.Clerc.md)

‐

[InvalidCommandError](Class.InvalidCommandError.md)

‐

[InvalidParametersError](Class.InvalidParametersError.md)

‐

[MissingRequiredFlagError](Class.MissingRequiredFlagError.md)

‐

[MissingRequiredMetadataError](Class.MissingRequiredMetadataError.md)

‐

[NoCommandSpecifiedError](Class.NoCommandSpecifiedError.md)

‐

[NoSuchCommandError](Class.NoSuchCommandError.md)

‐

## Interfaces

[BaseContext](Interface.BaseContext.md)

‐

[Command](Interface.Command.md)

‐

[CommandCustomOptions](Interface.CommandCustomOptions.md)

‐

[CommandOptions](Interface.CommandOptions.md)

‐

[ContextStore](Interface.ContextStore.md)

‐

[CreateOptions](Interface.CreateOptions.md)

‐

[FlagCustomOptions](Interface.FlagCustomOptions.md)

‐

[InterceptorObject](Interface.InterceptorObject.md)

‐

[ParameterCustomOptions](Interface.ParameterCustomOptions.md)

‐

[ParseOptions](Interface.ParseOptions.md)

‐

[Plugin](Interface.Plugin.md)

‐

## Type Aliases

[ClercFlagDefinitionValue](TypeAlias.ClercFlagDefinitionValue.md)

‐

[ClercFlagOptions](TypeAlias.ClercFlagOptions.md)

‐

[ClercFlagsDefinition](TypeAlias.ClercFlagsDefinition.md)

‐

[CommandHandler](TypeAlias.CommandHandler.md)

‐

[CommandHandlerContext](TypeAlias.CommandHandlerContext.md)

‐

[CommandsMap](TypeAlias.CommandsMap.md)

‐

[CommandsRecord](TypeAlias.CommandsRecord.md)

‐

[CommandWithHandler](TypeAlias.CommandWithHandler.md)

‐

[ErrorHandler](TypeAlias.ErrorHandler.md)

‐

[InferParameters](TypeAlias.InferParameters.md)

‐

[Interceptor](TypeAlias.Interceptor.md)

‐

[InterceptorContext](TypeAlias.InterceptorContext.md)

‐

[InterceptorHandler](TypeAlias.InterceptorHandler.md)

‐

[InterceptorNext](TypeAlias.InterceptorNext.md)

Function to call the next interceptor in the chain. **MUST** be awaited.

[MakeEmitterEvents](TypeAlias.MakeEmitterEvents.md)

‐

[ParameterDefinitionValue](TypeAlias.ParameterDefinitionValue.md)

‐

[ParameterOptions](TypeAlias.ParameterOptions.md)

‐

## Variables

[DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

‐

[KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

‐

[PARAMETER](Variable.PARAMETER.md)

‐

[UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

‐

## Functions

[createStopAtFirstParameter](Function.createStopAtFirstParameter.md)

‐

[defineCommand](Function.defineCommand.md)

‐

[definePlugin](Function.definePlugin.md)

‐

[extractParameterInfo](Function.extractParameterInfo.md)

‐

[inferDefault](Function.inferDefault.md)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

[normalizeFlagValue](Function.normalizeFlagValue.md)

‐

[normalizeParameterValue](Function.normalizeParameterValue.md)

‐

[resolveCommand](Function.resolveCommand.md)

‐

## References

### InvalidSchemaError

Re-exports [InvalidSchemaError](Parser.Class.InvalidSchemaError.md)

---

---

url: /reference/api/parser.md
---

# @clerc/parser

## Classes

[InvalidSchemaError](Class.InvalidSchemaError.md)

‐

## Interfaces

[FlagDefaultValueFunction](Interface.FlagDefaultValueFunction.md)

‐

[ObjectInputType](Interface.ObjectInputType.md)

‐

[ParsedResult](Interface.ParsedResult.md)

The parsed result.

[ParserOptions](Interface.ParserOptions.md)

Configuration options for the parser.

[TypeFunction](Interface.TypeFunction.md)

Defines how a string input is converted to the target type T.

## Type Aliases

[BaseFlagOptions](TypeAlias.BaseFlagOptions.md)

‐

[FlagDefaultValue](TypeAlias.FlagDefaultValue.md)

‐

[FlagDefinitionValue](TypeAlias.FlagDefinitionValue.md)

‐

[FlagOptions](TypeAlias.FlagOptions.md)

‐

[FlagsDefinition](TypeAlias.FlagsDefinition.md)

‐

[IgnoreFunction](TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[InferFlags](TypeAlias.InferFlags.md)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

[RawInputType](TypeAlias.RawInputType.md)

‐

[TypeValue](TypeAlias.TypeValue.md)

‐

## Variables

[DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

‐

[KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

‐

[PARAMETER](Variable.PARAMETER.md)

‐

[UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

‐

## Functions

[appendDotValues](Function.appendDotValues.md)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

[coerceObjectValue](Function.coerceObjectValue.md)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

[createParser](Function.createParser.md)

‐

[inferDefault](Function.inferDefault.md)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

[parse](Function.parse.md)

‐

[setDotValues](Function.setDotValues.md)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

---

---

url: /reference/api/plugin-completions.md
---

# @clerc/plugin-completions

## Functions

[completionsPlugin](Function.completionsPlugin.md)

‐

---

---

url: /reference/api/plugin-friendly-error.md
---

# @clerc/plugin-friendly-error

## Interfaces

[FriendlyErrorPluginOptions](Interface.FriendlyErrorPluginOptions.md)

‐

## Functions

[friendlyErrorPlugin](Function.friendlyErrorPlugin.md)

‐

---

---

url: /reference/api/plugin-help.md
---

# @clerc/plugin-help

## Interfaces

[CommandHelpOptions](Interface.CommandHelpOptions.md)

‐

[FlagHelpOptions](Interface.FlagHelpOptions.md)

‐

[GroupsOptions](Interface.GroupsOptions.md)

Options for defining groups in help output.

[HelpOptions](Interface.HelpOptions.md)

‐

[HelpPluginOptions](Interface.HelpPluginOptions.md)

‐

## Type Aliases

[GroupDefinition](TypeAlias.GroupDefinition.md)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.

## Variables

[defaultFormatters](Variable.defaultFormatters.md)

‐

## Functions

[helpPlugin](Function.helpPlugin.md)

‐

---

---

url: /reference/api/plugin-not-found.md
---

# @clerc/plugin-not-found

## Interfaces

[NotFoundPluginOptions](Interface.NotFoundPluginOptions.md)

‐

## Functions

[notFoundPlugin](Function.notFoundPlugin.md)

‐

---

---

url: /reference/api/plugin-strict-flags.md
---

# @clerc/plugin-strict-flags

## Functions

[strictFlagsPlugin](Function.strictFlagsPlugin.md)

‐

---

---

url: /reference/api/plugin-update-notifier.md
---

# @clerc/plugin-update-notifier

## Interfaces

[UpdateNotifierPluginOptions](Interface.UpdateNotifierPluginOptions.md)

‐

## Functions

[updateNotifierPlugin](Function.updateNotifierPlugin.md)

Plugin to check for CLI updates using update-notifier.

**Example**

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

---

---

url: /reference/api/plugin-version.md
---

# @clerc/plugin-version

## Functions

[versionPlugin](Function.versionPlugin.md)

‐

---

---

url: /reference/api/utils.md
---

# @clerc/utils

## Type Aliases

[CamelCase](TypeAlias.CamelCase.md)

‐

[DeepPrettify](TypeAlias.DeepPrettify.md)

‐

[IsAny](TypeAlias.IsAny.md)

‐

[LiteralUnion](TypeAlias.LiteralUnion.md)

‐

[MaybeArray](TypeAlias.MaybeArray.md)

‐

[MaybeAsyncGetter](TypeAlias.MaybeAsyncGetter.md)

‐

[MaybeGetter](TypeAlias.MaybeGetter.md)

‐

[PartialRequired](TypeAlias.PartialRequired.md)

‐

[Prettify](TypeAlias.Prettify.md)

‐

[RequireExactlyOne](TypeAlias.RequireExactlyOne.md)

‐

[RequireExactlyOneOrNone](TypeAlias.RequireExactlyOneOrNone.md)

‐

[ToArray](TypeAlias.ToArray.md)

‐

[UnionToIntersection](TypeAlias.UnionToIntersection.md)

‐

## Variables

[isTruthy](Variable.isTruthy.md)

‐

## Functions

[camelCase](Function.camelCase.md)

Converts a dash- or space-separated string to camelCase.

Not using regexp for better performance, because this function is used in
parser.

[formatFlagName](Function.formatFlagName.md)

‐

[formatVersion](Function.formatVersion.md)

‐

[hasOwn](Function.hasOwn.md)

‐

[joinWithAnd](Function.joinWithAnd.md)

‐

[kebabCase](Function.kebabCase.md)

‐

[looseIsArray](Function.looseIsArray.md)

‐

[objectIsEmpty](Function.objectIsEmpty.md)

‐

[resolveAsyncValue](Function.resolveAsyncValue.md)

‐

[resolveValue](Function.resolveValue.md)

‐

[toArray](Function.toArray.md)

‐

---

---

url: /guide/advanced.md
---

# Advanced Usage

## Passing Custom Arguments

Clerc allows you to pass a custom array of arguments instead of using the default `process.argv` / `Deno.args`. This is useful for testing or specific environments.

```ts twoslash
// @include: imports
Cli().parse(["node", "my-cli", "greet"]); // Pass a custom array of arguments
```

Alternatively, you can also pass an argument object:

```ts twoslash
// @include: imports
Cli().parse({
  argv: ["greet"],
});
```

## Parse Only Without Execution

Sometimes you may want to parse commands and flags without immediately executing the command handler. Clerc provides an option to achieve this:

```ts twoslash
// @include: imports
const result = Cli().parse({
  run: false, // Parse only, do not execute
});
```

When you need to run, you can call:

```ts twoslash
// @include: imports
result.run(); // Execute the parsed command
```

---

---

url: /reference/api.md
---

# API Reference

## Packages

* [clerc](./clerc/)
* [@clerc/advanced-types](./advanced-types/)
* [@clerc/core](./core/)
* [@clerc/parser](./parser/)
* [@clerc/plugin-completions](./plugin-completions/)
* [@clerc/plugin-friendly-error](./plugin-friendly-error/)
* [@clerc/plugin-help](./plugin-help/)
* [@clerc/plugin-not-found](./plugin-not-found/)
* [@clerc/plugin-strict-flags](./plugin-strict-flags/)
* [@clerc/plugin-update-notifier](./plugin-update-notifier/)
* [@clerc/plugin-version](./plugin-version/)
* [@clerc/utils](./utils/)

---

---

url: /guide/caveats.md
---

# Caveats

This document describes important behaviors and caveats of Clerc's argument parser. Understanding these behaviors is essential for building reliable CLI applications and avoiding unexpected issues.

## Non-Greedy Parsing

::: warning Important
The Clerc parser is **non-greedy**. It only reads arguments **before the first flag** to determine which command to execute.
:::

### Why Non-Greedy?

Clerc uses non-greedy parsing for the following reasons:

1. **Predictable behavior**: Flags can appear anywhere after the command without affecting command resolution
2. **Compatibility**: This matches the behavior of most Unix CLI tools
3. **Flexibility**: Allows flags to be placed in any order after the command
4. **Simplicity**: Makes the parsing logic straightforward and easier to understand

### How It Works

When parsing command-line arguments, the parser follows this logic:

1. Read arguments from left to right
2. Stop reading command/subcommand tokens when encountering the first flag (starting with `-` or `--`)
3. Everything after the first flag is treated as flags and their values, or as parameters

### Examples

```bash
# Command is "build", --verbose is a flag
cli build --verbose

# Command is "build", --help is a flag, "foo" is a parameter (NOT a subcommand)
cli build --help foo

# NO command is matched! --help is encountered first, so "build" becomes a parameter
cli --help build

# Command is "deploy staging", --force is a flag
cli deploy staging --force

# Command is "deploy", --env is a flag, "staging" is a parameter (NOT a subcommand)
cli deploy --env staging
```

### Impact on Plugins

This non-greedy behavior affects how certain plugins work:

#### Help Plugin

The `--help` flag shows CLI help **only when** it immediately follows the CLI name with no additional arguments:

```bash
# ✅ Shows CLI help (--help immediately follows cli, no extra arguments)
cli --help

# ✅ Shows help for "build" command (command comes before --help)
cli build --help

# ❌ Throws error!
cli --help build
```

::: warning

`cli --help build` will throw an error because:

1. The parser encounters `--help` first, so no command is matched (tries to match root command)
2. No root command is registered
3. Therefore, an error is thrown

The key difference:

* `cli --help` → Help plugin intercepts and shows CLI help
* `cli --help build` → Tries to execute root command (which doesn't exist), throws error

:::

If you want to show help for a specific command, always place the command name **before** the `--help` flag:

```bash
# ✅ Correct: Shows help for "build"
cli build --help
```

Alternatively, use the `help` command:

```bash
# ✅ Always shows help for "build"
cli help build
```

#### Version Plugin

Similarly, for version flags:

```bash
# Shows version (no command matched)
cli --version

# Command "build" is matched, but --version flag may be ignored by the command
cli build --version
```

## Parsing Order

The parser processes arguments in the following order:

1. **Command Resolution**: Identify the command from arguments before the first flag
2. **Flag Parsing**: Parse all flags (both global and command-specific)
3. **Parameter Collection**: Remaining non-flag arguments become parameters
4. **Double Dash Handling**: Everything after `--` is collected as-is

### Double Dash (`--`)

The double dash `--` is a special marker that tells the parser to stop interpreting flags:

```bash
# "--foo" is passed as a parameter, not parsed as a flag
cli build -- --foo --bar
```

## Flag Value Resolution

Flags can receive values in multiple ways:

```bash
# Space-separated
cli build --output dist

# Equals sign
cli build --output=dist

# Colon (useful when value contains =)
cli build --define:KEY=VALUE
```

## Dot-Notation for Object Flags

For flags with `type: Object`, you can use dot notation to set nested values:

```bash
# Sets config.port to "8080"
cli --config.port 8080

# Sets config.server.host to "localhost"
cli --config.server.host localhost
```

### Boolean Value Handling

For dot-notation flags, special values are automatically converted:

| Input                         | Result               |
| ----------------------------- | -------------------- |
| `--config.enabled true`       | `{ enabled: true }`  |
| `--config.enabled false`      | `{ enabled: false }` |
| `--config.enabled` (no value) | `{ enabled: true }`  |
| `--config.enabled=true`       | `{ enabled: true }`  |
| `--config.enabled=false`      | `{ enabled: false }` |
| `--config.enabled=` (empty)   | `{ enabled: true }`  |

The conversion rules are:

* `"true"` or empty string → `true`
* `"false"` → `false`
* Other values remain as strings

::: warning Path Conflicts

When a path has already been set to a primitive value, subsequent nested paths will be **silently ignored**:

```bash
# --config.port.internal is ignored because config.port is already "8080"
cli --config.port 8080 --config.port.internal 9090
# Result: { config: { port: "8080" } }
```

To avoid this, ensure your paths don't conflict (i.e., don't set both `a.b` and `a.b.c`).

:::

### Default Values for Object Flags

::: warning Not Recommended

**We do not recommend using `default` values with Object flags that use dot-notation.**

:::

Object flags follow an **all-or-nothing** default behavior:

* If **no** dot-notation values are provided for the flag, the `default` value is used entirely
* If **any** dot-notation value is provided, the `default` is completely ignored (no merging)

```bash
# Example: env flag with default { NODE_ENV: "development", PORT: "3000" }

# No --env flags provided → Uses entire default
cli build
# Result: { NODE_ENV: "development", PORT: "3000" }

# Any --env flag provided → Default is completely ignored
cli build --env.PORT 8080
# Result: { PORT: "8080" }  ← NODE_ENV is NOT included!
```

#### Why Not Use Defaults with Dot-Notation?

Dot-notation is designed for **user-defined, runtime configuration values** (like environment variables, define macros, etc.) where:

* The keys are not known in advance
* Users specify exactly what they need
* There's no "standard set" of expected keys

This semantic mismatch with defaults causes several issues:

1. **Complex merge logic**: Shallow merge? Deep merge? User-configurable merge function? Each approach adds complexity
2. **Type inference complexity**: Merging object types requires intersection types and sophisticated type-level logic
3. **Unexpected behavior**: Users might expect `default` to act as "fallback values" for missing keys, but implementing this is non-trivial

#### Recommended Approach

Instead of using defaults with dot-notation, handle default values in your command handler:

```typescript twoslash
// @include: imports
cli
  .command("build", "Build the project")
  .flags({
    env: Object,
  })
  .on((context) => {
    const env = {
      NODE_ENV: "development",
      PORT: "3000",
      ...context.flags.env, // User-provided values override defaults
    };

    // Use env...
  });
```

This gives you full control over the merge logic and keeps type inference simple.

## Short Flag Combinations

Short flags can be combined:

```bash
# Equivalent to: -a -b -c
cli -abc

# -a and -b are boolean flags, -c takes "value"
cli -abc value
```

## Best Practices

1. **Place commands before flags**: Always write `cli command --flag` instead of `cli --flag command`

2. **Use explicit help command**: When in doubt, use `cli help command` instead of `cli --help command`

3. **Quote special characters**: Use quotes for values containing spaces or special characters

4. **Use `--` for pass-through arguments**: When passing arguments to child processes, use `--` to prevent parsing

```bash
# Pass "--watch" to the underlying tool, not to cli
cli build -- --watch
```

---

---

url: /reference/api/clerc/Class.Clerc.md
---

# Class: Clerc\<Commands, GlobalFlags>

Defined in: [packages/core/src/cli.ts:48](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L48)

## Type Parameters

`Commands` *extends* [`CommandsRecord`](TypeAlias.CommandsRecord.md)

`object`

`GlobalFlags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Accessors

### \_commands

#### Get Signature

```ts twoslash
// @include: imports
get _commands(): CommandsMap;
```

Defined in: [packages/core/src/cli.ts:101](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L101)

##### Returns

[`CommandsMap`](TypeAlias.CommandsMap.md)

***

### \_description

#### Get Signature

```ts twoslash
// @include: imports
get _description(): string;
```

Defined in: [packages/core/src/cli.ts:93](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L93)

##### Returns

`string`

***

### \_globalFlags

#### Get Signature

```ts twoslash
// @include: imports
get _globalFlags(): GlobalFlags;
```

Defined in: [packages/core/src/cli.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L105)

##### Returns

`GlobalFlags`

***

### \_name

#### Get Signature

```ts twoslash
// @include: imports
get _name(): string;
```

Defined in: [packages/core/src/cli.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L85)

##### Returns

`string`

***

### \_scriptName

#### Get Signature

```ts twoslash
// @include: imports
get _scriptName(): string;
```

Defined in: [packages/core/src/cli.ts:89](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L89)

##### Returns

`string`

***

### \_version

#### Get Signature

```ts twoslash
// @include: imports
get _version(): string;
```

Defined in: [packages/core/src/cli.ts:97](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L97)

##### Returns

`string`

***

### store

#### Get Signature

```ts twoslash
// @include: imports
get store(): Partial<ContextStore>;
```

Defined in: [packages/core/src/cli.ts:109](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L109)

##### Returns

`Partial`<`ContextStore`>

## Methods

### command()

#### Call Signature

```ts twoslash
// @include: imports
command(commands): this;
```

Defined in: [packages/core/src/cli.ts:196](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L196)

##### Parameters

`commands`

readonly [`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`any`, `any`, `any`>\[]

##### Returns

`this`

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(command): Clerc<Commands & Record<string, CommandWithHandler<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:197](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L197)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`command`

[`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`string`, [`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(name, options?): Clerc<Commands & Record<Name, Command<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:207](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L207)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`name`

`Name` *extends* keyof `Commands` ? \[`"COMMAND ALREADY EXISTS"`] : `Name`

`options?`

[`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`Name`, [`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(
   name,
   description,
options?): Clerc<Commands & Record<Name, Command<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:221](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L221)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`name`

`Name` *extends* keyof `Commands` ? \[`"COMMAND ALREADY EXISTS"`] : `Name`

`description`

`string`

`options?`

[`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`Name`, [`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

***

### description()

```ts twoslash
// @include: imports
description(description): this;
```

Defined in: [packages/core/src/cli.ts:129](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L129)

#### Parameters

`description`

`string`

#### Returns

`this`

***

### errorHandler()

```ts twoslash
// @include: imports
errorHandler(handler): this;
```

Defined in: [packages/core/src/cli.ts:147](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L147)

#### Parameters

`handler`

[`ErrorHandler`](TypeAlias.ErrorHandler.md)

#### Returns

`this`

***

### globalFlag()

#### Call Signature

```ts twoslash
// @include: imports
globalFlag<Name, Flag>(
   name,
   description,
options): Clerc<Commands, GlobalFlags & Record<Name, Flag>>;
```

Defined in: [packages/core/src/cli.ts:276](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L276)

##### Type Parameters

`Name` *extends* `string`

`Flag` *extends* [`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

##### Parameters

`name`

`Name`

`description`

`string`

`options`

`Flag`

##### Returns

`Clerc`<`Commands`, `GlobalFlags` & `Record`<`Name`, `Flag`>>

#### Call Signature

```ts twoslash
// @include: imports
globalFlag<Name, Flag>(name, options): Clerc<Commands, GlobalFlags & Record<Name, Flag>>;
```

Defined in: [packages/core/src/cli.ts:281](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L281)

##### Type Parameters

`Name` *extends* `string`

`Flag` *extends* [`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

##### Parameters

`name`

`Name`

`options`

`Flag`

##### Returns

`Clerc`<`Commands`, `GlobalFlags` & `Record`<`Name`, `Flag`>>

***

### interceptor()

```ts twoslash
// @include: imports
interceptor(interceptor): this;
```

Defined in: [packages/core/src/cli.ts:300](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L300)

#### Parameters

`interceptor`

[`Interceptor`](TypeAlias.Interceptor.md)<[`Command`](Interface.Command.md)<`string`, readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[], [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)>, `GlobalFlags`>

#### Returns

`this`

***

### name()

```ts twoslash
// @include: imports
name(name): this;
```

Defined in: [packages/core/src/cli.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L117)

#### Parameters

`name`

`string`

#### Returns

`this`

***

### on()

```ts twoslash
// @include: imports
on<Name>(name, handler): this;
```

Defined in: [packages/core/src/cli.ts:306](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L306)

#### Type Parameters

`Name` *extends* `string` | `number` | `symbol` | `string` & `Record`<`never`, `never`>

#### Parameters

`name`

`Name`

`handler`

[`CommandHandler`](TypeAlias.CommandHandler.md)<`Commands`\[`Name`], `GlobalFlags`>

#### Returns

`this`

***

### parse()

```ts twoslash
// @include: imports
parse<Run>(argvOrOptions): Run extends true ? Promise<void> : Clerc<Commands, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:410](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L410)

#### Type Parameters

`Run` *extends* `boolean`

`true`

#### Parameters

`argvOrOptions`

`string`\[] | [`ParseOptions`](Interface.ParseOptions.md)<`Run`>

`platformArgv`

#### Returns

`Run` *extends* `true` ? `Promise`<`void`> : `Clerc`<`Commands`, `GlobalFlags`>

***

### run()

```ts twoslash
// @include: imports
run(): Promise<void>;
```

Defined in: [packages/core/src/cli.ts:340](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L340)

#### Returns

`Promise`<`void`>

***

### scriptName()

```ts twoslash
// @include: imports
scriptName(scriptName): this;
```

Defined in: [packages/core/src/cli.ts:123](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L123)

#### Parameters

`scriptName`

`string`

#### Returns

`this`

***

### use()

```ts twoslash
// @include: imports
use(plugin): this;
```

Defined in: [packages/core/src/cli.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L141)

#### Parameters

`plugin`

[`Plugin`](Interface.Plugin.md)

#### Returns

`this`

***

### version()

```ts twoslash
// @include: imports
version(version): this;
```

Defined in: [packages/core/src/cli.ts:135](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L135)

#### Parameters

`version`

`string`

#### Returns

`this`

***

### create()

```ts twoslash
// @include: imports
static create(options?): Clerc;
```

Defined in: [packages/core/src/cli.ts:113](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L113)

#### Parameters

`options?`

[`CreateOptions`](Interface.CreateOptions.md)

#### Returns

`Clerc`

---

---

url: /reference/api/core/Class.Clerc.md
---

# Class: Clerc\<Commands, GlobalFlags>

Defined in: [packages/core/src/cli.ts:48](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L48)

## Type Parameters

`Commands` *extends* [`CommandsRecord`](TypeAlias.CommandsRecord.md)

`object`

`GlobalFlags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Accessors

### \_commands

#### Get Signature

```ts twoslash
// @include: imports
get _commands(): CommandsMap;
```

Defined in: [packages/core/src/cli.ts:101](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L101)

##### Returns

[`CommandsMap`](TypeAlias.CommandsMap.md)

***

### \_description

#### Get Signature

```ts twoslash
// @include: imports
get _description(): string;
```

Defined in: [packages/core/src/cli.ts:93](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L93)

##### Returns

`string`

***

### \_globalFlags

#### Get Signature

```ts twoslash
// @include: imports
get _globalFlags(): GlobalFlags;
```

Defined in: [packages/core/src/cli.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L105)

##### Returns

`GlobalFlags`

***

### \_name

#### Get Signature

```ts twoslash
// @include: imports
get _name(): string;
```

Defined in: [packages/core/src/cli.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L85)

##### Returns

`string`

***

### \_scriptName

#### Get Signature

```ts twoslash
// @include: imports
get _scriptName(): string;
```

Defined in: [packages/core/src/cli.ts:89](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L89)

##### Returns

`string`

***

### \_version

#### Get Signature

```ts twoslash
// @include: imports
get _version(): string;
```

Defined in: [packages/core/src/cli.ts:97](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L97)

##### Returns

`string`

***

### store

#### Get Signature

```ts twoslash
// @include: imports
get store(): Partial<ContextStore>;
```

Defined in: [packages/core/src/cli.ts:109](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L109)

##### Returns

`Partial`<`ContextStore`>

## Methods

### command()

#### Call Signature

```ts twoslash
// @include: imports
command(commands): this;
```

Defined in: [packages/core/src/cli.ts:196](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L196)

##### Parameters

`commands`

readonly [`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`any`, `any`, `any`>\[]

##### Returns

`this`

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(command): Clerc<Commands & Record<string, CommandWithHandler<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:197](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L197)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`command`

[`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`string`, [`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(name, options?): Clerc<Commands & Record<Name, Command<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:207](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L207)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`name`

`Name` *extends* keyof `Commands` ? \[`"COMMAND ALREADY EXISTS"`] : `Name`

`options?`

[`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`Name`, [`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

#### Call Signature

```ts twoslash
// @include: imports
command<Name, Parameters, Flags>(
   name,
   description,
options?): Clerc<Commands & Record<Name, Command<Name, Parameters, Flags>>, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:221](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L221)

##### Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

##### Parameters

`name`

`Name` *extends* keyof `Commands` ? \[`"COMMAND ALREADY EXISTS"`] : `Name`

`description`

`string`

`options?`

[`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

##### Returns

`Clerc`<`Commands` & `Record`<`Name`, [`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>, `GlobalFlags`>

***

### description()

```ts twoslash
// @include: imports
description(description): this;
```

Defined in: [packages/core/src/cli.ts:129](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L129)

#### Parameters

`description`

`string`

#### Returns

`this`

***

### errorHandler()

```ts twoslash
// @include: imports
errorHandler(handler): this;
```

Defined in: [packages/core/src/cli.ts:147](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L147)

#### Parameters

`handler`

[`ErrorHandler`](TypeAlias.ErrorHandler.md)

#### Returns

`this`

***

### globalFlag()

#### Call Signature

```ts twoslash
// @include: imports
globalFlag<Name, Flag>(
   name,
   description,
options): Clerc<Commands, GlobalFlags & Record<Name, Flag>>;
```

Defined in: [packages/core/src/cli.ts:276](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L276)

##### Type Parameters

`Name` *extends* `string`

`Flag` *extends* [`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

##### Parameters

`name`

`Name`

`description`

`string`

`options`

`Flag`

##### Returns

`Clerc`<`Commands`, `GlobalFlags` & `Record`<`Name`, `Flag`>>

#### Call Signature

```ts twoslash
// @include: imports
globalFlag<Name, Flag>(name, options): Clerc<Commands, GlobalFlags & Record<Name, Flag>>;
```

Defined in: [packages/core/src/cli.ts:281](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L281)

##### Type Parameters

`Name` *extends* `string`

`Flag` *extends* [`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

##### Parameters

`name`

`Name`

`options`

`Flag`

##### Returns

`Clerc`<`Commands`, `GlobalFlags` & `Record`<`Name`, `Flag`>>

***

### interceptor()

```ts twoslash
// @include: imports
interceptor(interceptor): this;
```

Defined in: [packages/core/src/cli.ts:300](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L300)

#### Parameters

`interceptor`

[`Interceptor`](TypeAlias.Interceptor.md)<[`Command`](Interface.Command.md)<`string`, readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[], [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)>, `GlobalFlags`>

#### Returns

`this`

***

### name()

```ts twoslash
// @include: imports
name(name): this;
```

Defined in: [packages/core/src/cli.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L117)

#### Parameters

`name`

`string`

#### Returns

`this`

***

### on()

```ts twoslash
// @include: imports
on<Name>(name, handler): this;
```

Defined in: [packages/core/src/cli.ts:306](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L306)

#### Type Parameters

`Name` *extends* `string` | `number` | `symbol` | `string` & `Record`<`never`, `never`>

#### Parameters

`name`

`Name`

`handler`

[`CommandHandler`](TypeAlias.CommandHandler.md)<`Commands`\[`Name`], `GlobalFlags`>

#### Returns

`this`

***

### parse()

```ts twoslash
// @include: imports
parse<Run>(argvOrOptions): Run extends true ? Promise<void> : Clerc<Commands, GlobalFlags>;
```

Defined in: [packages/core/src/cli.ts:410](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L410)

#### Type Parameters

`Run` *extends* `boolean`

`true`

#### Parameters

`argvOrOptions`

`string`\[] | [`ParseOptions`](Interface.ParseOptions.md)<`Run`>

`platformArgv`

#### Returns

`Run` *extends* `true` ? `Promise`<`void`> : `Clerc`<`Commands`, `GlobalFlags`>

***

### run()

```ts twoslash
// @include: imports
run(): Promise<void>;
```

Defined in: [packages/core/src/cli.ts:340](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L340)

#### Returns

`Promise`<`void`>

***

### scriptName()

```ts twoslash
// @include: imports
scriptName(scriptName): this;
```

Defined in: [packages/core/src/cli.ts:123](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L123)

#### Parameters

`scriptName`

`string`

#### Returns

`this`

***

### use()

```ts twoslash
// @include: imports
use(plugin): this;
```

Defined in: [packages/core/src/cli.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L141)

#### Parameters

`plugin`

[`Plugin`](Interface.Plugin.md)

#### Returns

`this`

***

### version()

```ts twoslash
// @include: imports
version(version): this;
```

Defined in: [packages/core/src/cli.ts:135](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L135)

#### Parameters

`version`

`string`

#### Returns

`this`

***

### create()

```ts twoslash
// @include: imports
static create(options?): Clerc;
```

Defined in: [packages/core/src/cli.ts:113](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L113)

#### Parameters

`options?`

[`CreateOptions`](Interface.CreateOptions.md)

#### Returns

`Clerc`

---

---

url: /reference/api/advanced-types/Class.FlagValidationError.md
---

# Class: FlagValidationError

Defined in: [packages/advanced-types/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?, options?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Types.Class.FlagValidationError.md
---

# Class: FlagValidationError

Defined in: [packages/advanced-types/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?, options?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Types.Class.FlagValidationError.md
---

# Class: FlagValidationError

Defined in: [packages/advanced-types/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new FlagValidationError(message?, options?): FlagValidationError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`FlagValidationError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.InvalidCommandError.md
---

# Class: InvalidCommandError

Defined in: [packages/core/src/errors.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L16)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidCommandError(message?): InvalidCommandError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`InvalidCommandError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new InvalidCommandError(message?, options?): InvalidCommandError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`InvalidCommandError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.InvalidCommandError.md
---

# Class: InvalidCommandError

Defined in: [packages/core/src/errors.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L16)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidCommandError(message?): InvalidCommandError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`InvalidCommandError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new InvalidCommandError(message?, options?): InvalidCommandError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`InvalidCommandError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.InvalidParametersError.md
---

# Class: InvalidParametersError

Defined in: [packages/core/src/errors.ts:24](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L24)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidParametersError(message?): InvalidParametersError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`InvalidParametersError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new InvalidParametersError(message?, options?): InvalidParametersError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`InvalidParametersError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.InvalidParametersError.md
---

# Class: InvalidParametersError

Defined in: [packages/core/src/errors.ts:24](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L24)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidParametersError(message?): InvalidParametersError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

#### Returns

`InvalidParametersError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

### Constructor

```ts twoslash
// @include: imports
new InvalidParametersError(message?, options?): InvalidParametersError;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1082

#### Parameters

`message?`

`string`

`options?`

`ErrorOptions`

#### Returns

`InvalidParametersError`

#### Inherited from

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Parser.Class.InvalidSchemaError.md
---

# Class: InvalidSchemaError

Defined in: [packages/parser/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidSchemaError(message): InvalidSchemaError;
```

Defined in: [packages/parser/src/errors.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L2)

#### Parameters

`message`

`string`

#### Returns

`InvalidSchemaError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Parser.Class.InvalidSchemaError.md
---

# Class: InvalidSchemaError

Defined in: [packages/parser/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidSchemaError(message): InvalidSchemaError;
```

Defined in: [packages/parser/src/errors.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L2)

#### Parameters

`message`

`string`

#### Returns

`InvalidSchemaError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/parser/Class.InvalidSchemaError.md
---

# Class: InvalidSchemaError

Defined in: [packages/parser/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new InvalidSchemaError(message): InvalidSchemaError;
```

Defined in: [packages/parser/src/errors.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/errors.ts#L2)

#### Parameters

`message`

`string`

#### Returns

`InvalidSchemaError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.MissingRequiredFlagError.md
---

# Class: MissingRequiredFlagError

Defined in: [packages/core/src/errors.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L26)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new MissingRequiredFlagError(flags): MissingRequiredFlagError;
```

Defined in: [packages/core/src/errors.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L27)

#### Parameters

`flags`

`string`\[]

#### Returns

`MissingRequiredFlagError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.MissingRequiredFlagError.md
---

# Class: MissingRequiredFlagError

Defined in: [packages/core/src/errors.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L26)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new MissingRequiredFlagError(flags): MissingRequiredFlagError;
```

Defined in: [packages/core/src/errors.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L27)

#### Parameters

`flags`

`string`\[]

#### Returns

`MissingRequiredFlagError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.MissingRequiredMetadataError.md
---

# Class: MissingRequiredMetadataError

Defined in: [packages/core/src/errors.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L18)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new MissingRequiredMetadataError(metadataName): MissingRequiredMetadataError;
```

Defined in: [packages/core/src/errors.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L19)

#### Parameters

`metadataName`

`string`

#### Returns

`MissingRequiredMetadataError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.MissingRequiredMetadataError.md
---

# Class: MissingRequiredMetadataError

Defined in: [packages/core/src/errors.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L18)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new MissingRequiredMetadataError(metadataName): MissingRequiredMetadataError;
```

Defined in: [packages/core/src/errors.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L19)

#### Parameters

`metadataName`

`string`

#### Returns

`MissingRequiredMetadataError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.NoCommandSpecifiedError.md
---

# Class: NoCommandSpecifiedError

Defined in: [packages/core/src/errors.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L10)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new NoCommandSpecifiedError(text): NoCommandSpecifiedError;
```

Defined in: [packages/core/src/errors.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L11)

#### Parameters

`text`

`string`

`"No command specified."`

#### Returns

`NoCommandSpecifiedError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.NoCommandSpecifiedError.md
---

# Class: NoCommandSpecifiedError

Defined in: [packages/core/src/errors.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L10)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new NoCommandSpecifiedError(text): NoCommandSpecifiedError;
```

Defined in: [packages/core/src/errors.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L11)

#### Parameters

`text`

`string`

`"No command specified."`

#### Returns

`NoCommandSpecifiedError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc/Class.NoSuchCommandError.md
---

# Class: NoSuchCommandError

Defined in: [packages/core/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new NoSuchCommandError(commandName, text): NoSuchCommandError;
```

Defined in: [packages/core/src/errors.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L2)

#### Parameters

`commandName`

`string`

`text`

`string`

#### Returns

`NoSuchCommandError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`commandName`

`public`

`string`

‐

‐

[packages/core/src/errors.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L3)

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/core/Class.NoSuchCommandError.md
---

# Class: NoSuchCommandError

Defined in: [packages/core/src/errors.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L1)

## Extends

* `Error`

## Constructors

### Constructor

```ts twoslash
// @include: imports
new NoSuchCommandError(commandName, text): NoSuchCommandError;
```

Defined in: [packages/core/src/errors.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L2)

#### Parameters

`commandName`

`string`

`text`

`string`

#### Returns

`NoSuchCommandError`

#### Overrides

```ts twoslash
// @include: imports
Error.constructor;
```

## Properties

&#x20;`cause?`

`public`

`unknown`

‐

```ts twoslash
// @include: imports
Error.cause;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es2022.error.d.ts:26

&#x20;`commandName`

`public`

`string`

‐

‐

[packages/core/src/errors.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/errors.ts#L3)

&#x20;`message`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.message;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1077

&#x20;`name`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.name;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1076

&#x20;`stack?`

`public`

`string`

‐

```ts twoslash
// @include: imports
Error.stack;
```

node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.es5.d.ts:1078

&#x20;`stackTraceLimit`

`static`

`number`

The `Error.stackTraceLimit` property specifies the number of stack frames
collected by a stack trace (whether generated by `new Error().stack` or
`Error.captureStackTrace(obj)`).

The default value is `10` but may be set to any valid JavaScript number. Changes
will affect any stack trace captured *after* the value has been changed.

If set to a non-number value, or set to a negative number, stack traces will
not capture any frames.

```ts twoslash
// @include: imports
Error.stackTraceLimit;
```

node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:68

## Methods

### captureStackTrace()

```ts twoslash
// @include: imports
static captureStackTrace(targetObject, constructorOpt?): void;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:52

Creates a `.stack` property on `targetObject`, which when accessed returns
a string representing the location in the code at which
`Error.captureStackTrace()` was called.

```js
const myObject = {};
Error.captureStackTrace(myObject);
myObject.stack; // Similar to `new Error().stack`
```

The first line of the trace will be prefixed with
`${myObject.name}: ${myObject.message}`.

The optional `constructorOpt` argument accepts a function. If given, all frames
above `constructorOpt`, including `constructorOpt`, will be omitted from the
generated stack trace.

The `constructorOpt` argument is useful for hiding implementation
details of error generation from the user. For instance:

```js
function a() {
  b();
}

function b() {
  c();
}

function c() {
  // Create an error without stack trace to avoid calculating the stack trace twice.
  const { stackTraceLimit } = Error;
  Error.stackTraceLimit = 0;
  const error = new Error();
  Error.stackTraceLimit = stackTraceLimit;

  // Capture the stack trace above function b
  Error.captureStackTrace(error, b); // Neither function c, nor b is included in the stack trace
  throw error;
}

a();
```

#### Parameters

`targetObject`

`object`

`constructorOpt?`

`Function`

#### Returns

`void`

#### Inherited from

```ts twoslash
// @include: imports
Error.captureStackTrace;
```

***

### isError()

```ts twoslash
// @include: imports
static isError(error): error is Error;
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.error.d.ts:23

Indicates whether the argument provided is a built-in Error instance or not.

#### Parameters

`error`

`unknown`

#### Returns

`error is Error`

#### Inherited from

```ts twoslash
// @include: imports
Error.isError;
```

***

### prepareStackTrace()

```ts twoslash
// @include: imports
static prepareStackTrace(err, stackTraces): any;
```

Defined in: node\_modules/.pnpm/@types+node@24.10.9/node\_modules/@types/node/globals.d.ts:56

#### Parameters

`err`

`Error`

`stackTraces`

`CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

```ts twoslash
// @include: imports
Error.prepareStackTrace;
```

---

---

url: /reference/api/clerc.md
---

# clerc

## Namespaces

[Parser](Namespace.Parser.md)

‐

[Types](Namespace.Types.md)

‐

## Classes

[Clerc](Class.Clerc.md)

‐

[InvalidCommandError](Class.InvalidCommandError.md)

‐

[InvalidParametersError](Class.InvalidParametersError.md)

‐

[MissingRequiredFlagError](Class.MissingRequiredFlagError.md)

‐

[MissingRequiredMetadataError](Class.MissingRequiredMetadataError.md)

‐

[NoCommandSpecifiedError](Class.NoCommandSpecifiedError.md)

‐

[NoSuchCommandError](Class.NoSuchCommandError.md)

‐

## Interfaces

[BaseContext](Interface.BaseContext.md)

‐

[Command](Interface.Command.md)

‐

[CommandCustomOptions](Interface.CommandCustomOptions.md)

‐

[CommandHelpOptions](Interface.CommandHelpOptions.md)

‐

[CommandOptions](Interface.CommandOptions.md)

‐

[ContextStore](Interface.ContextStore.md)

‐

[CreateOptions](Interface.CreateOptions.md)

‐

[FlagCustomOptions](Interface.FlagCustomOptions.md)

‐

[FlagHelpOptions](Interface.FlagHelpOptions.md)

‐

[FriendlyErrorPluginOptions](Interface.FriendlyErrorPluginOptions.md)

‐

[GroupsOptions](Interface.GroupsOptions.md)

Options for defining groups in help output.

[HelpOptions](Interface.HelpOptions.md)

‐

[HelpPluginOptions](Interface.HelpPluginOptions.md)

‐

[InterceptorObject](Interface.InterceptorObject.md)

‐

[NotFoundPluginOptions](Interface.NotFoundPluginOptions.md)

‐

[ParameterCustomOptions](Interface.ParameterCustomOptions.md)

‐

[ParseOptions](Interface.ParseOptions.md)

‐

[Plugin](Interface.Plugin.md)

‐

[UpdateNotifierPluginOptions](Interface.UpdateNotifierPluginOptions.md)

‐

## Type Aliases

[ClercFlagDefinitionValue](TypeAlias.ClercFlagDefinitionValue.md)

‐

[ClercFlagOptions](TypeAlias.ClercFlagOptions.md)

‐

[ClercFlagsDefinition](TypeAlias.ClercFlagsDefinition.md)

‐

[CommandHandler](TypeAlias.CommandHandler.md)

‐

[CommandHandlerContext](TypeAlias.CommandHandlerContext.md)

‐

[CommandsMap](TypeAlias.CommandsMap.md)

‐

[CommandsRecord](TypeAlias.CommandsRecord.md)

‐

[CommandWithHandler](TypeAlias.CommandWithHandler.md)

‐

[ErrorHandler](TypeAlias.ErrorHandler.md)

‐

[GroupDefinition](TypeAlias.GroupDefinition.md)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.

[InferParameters](TypeAlias.InferParameters.md)

‐

[Interceptor](TypeAlias.Interceptor.md)

‐

[InterceptorContext](TypeAlias.InterceptorContext.md)

‐

[InterceptorHandler](TypeAlias.InterceptorHandler.md)

‐

[InterceptorNext](TypeAlias.InterceptorNext.md)

Function to call the next interceptor in the chain. **MUST** be awaited.

[MakeEmitterEvents](TypeAlias.MakeEmitterEvents.md)

‐

[ParameterDefinitionValue](TypeAlias.ParameterDefinitionValue.md)

‐

[ParameterOptions](TypeAlias.ParameterOptions.md)

‐

## Variables

[defaultFormatters](Variable.defaultFormatters.md)

‐

[DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

‐

[KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

‐

[PARAMETER](Variable.PARAMETER.md)

‐

[UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

‐

## Functions

[Cli](Function.Cli.md)

‐

[completionsPlugin](Function.completionsPlugin.md)

‐

[createStopAtFirstParameter](Function.createStopAtFirstParameter.md)

‐

[defineCommand](Function.defineCommand.md)

‐

[definePlugin](Function.definePlugin.md)

‐

[extractParameterInfo](Function.extractParameterInfo.md)

‐

[friendlyErrorPlugin](Function.friendlyErrorPlugin.md)

‐

[helpPlugin](Function.helpPlugin.md)

‐

[inferDefault](Function.inferDefault.md)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

[normalizeFlagValue](Function.normalizeFlagValue.md)

‐

[normalizeParameterValue](Function.normalizeParameterValue.md)

‐

[notFoundPlugin](Function.notFoundPlugin.md)

‐

[resolveCommand](Function.resolveCommand.md)

‐

[strictFlagsPlugin](Function.strictFlagsPlugin.md)

‐

[updateNotifierPlugin](Function.updateNotifierPlugin.md)

Plugin to check for CLI updates using update-notifier.

**Example**

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

[versionPlugin](Function.versionPlugin.md)

‐

## References

### InvalidSchemaError

Re-exports [InvalidSchemaError](Parser.Class.InvalidSchemaError.md)

---

---

url: /guide/commands.md
---

# Commands

## Basic Usage

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command")
  .on("foo", (ctx) => {
    console.log("It works!");
  })
  .parse();
```

This creates a CLI application named `foo-cli` with a command called `foo`. When the user runs `foo-cli foo`, the CLI will output "It works!".

## Optional Description

The description parameter is optional. You can omit it if you don't need to document the command:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", {
    // No description, pass options directly
    flags: {
      output: {
        type: String,
        description: "Output file",
      },
    },
  })
  .on("foo", (ctx) => {
    console.log("It works!");
  })
  .parse();
```

Alternatively, you can use the traditional syntax with a description:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command", {
    flags: {
      output: {
        type: String,
        description: "Output file",
      },
    },
  })
  .parse();
```

## Aliases

### Overview

Command aliases allow users to invoke a command using an alternative name. This is useful for providing shorter or more intuitive command names.

### Single Alias

You can define a single alias for a command using a string:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command", {
    alias: "f",
  })
  .on("foo", (ctx) => {
    console.log("It works!");
  })
  .parse();
```

Now both `foo-cli foo` and `foo-cli f` will output "It works!".

### Multiple Aliases

You can define multiple aliases for a command using an array:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command", {
    alias: ["f", "bar", "baz"],
  })
  .on("foo", (ctx) => {
    console.log("It works!");
  })
  .parse();
```

Now `foo-cli foo`, `foo-cli f`, `foo-cli bar`, and `foo-cli baz` all work the same way.

### Practical Examples

#### Example: Git-like Abbreviations

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("git")
  .command("status", "Show working tree status", {
    alias: "st",
  })
  .on("status", (ctx) => {
    console.log("On branch main...");
  })
  .command("commit", "Record changes to repository", {
    alias: ["ci", "com"],
  })
  .on("commit", (ctx) => {
    console.log("Committing changes...");
  })
  .command("checkout", "Switch branches or restore files", {
    alias: "co",
  })
  .on("checkout", (ctx) => {
    console.log("Checking out...");
  })
  .parse();
```

Usage:

```sh
git st
git commit
git ci
git com
git checkout
git co
```

## Subcommands

You can define subcommands by using spaces in the command name:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("parent child", "A subcommand")
  .on("parent child", (ctx) => {
    console.log("Subcommand was called!");
  })
  .parse();
```

## Root Command

You can define a root command (a command with no name) to handle cases when no subcommand is specified:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("", "Root command")
  .on("", (ctx) => {
    console.log("Root command was called!");
  })
  .parse();
```

## Parameters

Please refer to the [Parameters Documentation](./parameters) for detailed information about parameter definition, constraints, and descriptions.

## Flags

Please refer to the [Flags Documentation](./flags).

## Ignore

Sometimes, you may want to ignore certain arguments or flags in the command line input. For example, this usage of `deno`:

```sh
deno run --allow-read script.ts --flag
```

Where `--flag` is passed directly to the script, not to `deno`.

You can achieve this usage by using the `ignore` property to specify which arguments or flags to ignore.

```ts twoslash
// @include: imports
import { PARAMETER } from "clerc";

let encounteredParameter = false;

const cli = Cli()
  .scriptName("deno")
  .description("Deno CLI")
  .version("1.0.0")
  .command("run", "Run script", {
    flags: {
      allowRead: {
        type: Boolean,
        description: "Allow file system read",
      },
    },
    parameters: ["<script>", "[args...]"],
    ignore: (type) => {
      if (type === PARAMETER && !encounteredParameter) {
        encounteredParameter = true;

        return false; // Don't ignore the first parameter (script name)
      }

      // Ignore the rest of the parameters
      return encounteredParameter;
    },
  })
  .on("run", (ctx) => {
    // Handle script execution
    ctx.ignored; // => ["--flag"]
    // ^?
  })
  .parse();
```

## Multiple Commands

You can register multiple commands at once by passing an array of command created by `defineCommand` to the `command()` method.

```ts twoslash
// @include: imports
import { defineCommand } from "clerc";

const commandA = defineCommand(
  {
    name: "foo",
    description: "Foo command",
  },
  (ctx) => {
    console.log("Foo command executed");
  },
);
const commandB = defineCommand(
  {
    name: "bar",
    description: "Bar command",
    flags: {
      flag: {
        type: Boolean,
        default: false,
      },
    },
  },
  (ctx) => {
    console.log("Bar command executed");
  },
);

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command([commandA, commandB])
  .parse();
```

## Advanced Usage

To separate the handler from the cli definition, you can use the `defineCommand` utility function:

```ts twoslash
// @include: imports
import { defineCommand } from "clerc";

const command = defineCommand({
  name: "test",
  description: "Test",
  flags: {},
  parameters: [],
  handler: (ctx) => {
    // Handler
  },
});

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command(command)
  .parse();
```

## Lazy Loading

Lazy loading allows you to defer the loading of command handlers until they are actually invoked. This is useful for reducing startup time and memory usage, especially when you have many commands or heavy handlers.

You can implement lazy loading by using dynamic imports (`await import()`) within the handler:

### Basic Lazy Loading

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("app")
  .description("An application with lazy loading")
  .version("1.0.0")
  .command("build", "Build the project", {
    flags: {
      production: {
        type: Boolean,
        description: "Build for production",
      },
    },
  })
  .on("build", async (ctx) => {
    // Handler is only loaded when the command is invoked
    const { buildProject } = await import("./handlers/build.js");
    await buildProject(ctx);
  })
  .command("deploy", "Deploy the application", {
    flags: {
      environment: {
        type: String,
        default: "staging",
        description: "Target environment",
      },
    },
  })
  .on("deploy", async (ctx) => {
    // Another handler loaded lazily
    const { deploy } = await import("./handlers/deploy.js");
    await deploy(ctx);
  })
  .parse();
```

### Lazy Loading with defineCommand

You can also combine lazy loading with the `defineCommand` utility:

```ts twoslash
// @include: imports
import { defineCommand } from "clerc";

const command = defineCommand({
  name: "migrate",
  description: "Run database migrations",
  flags: {},
  parameters: [],
  handler: async (ctx) => {
    // Handler loaded only when command is invoked
    const { runMigrations } = await import("./handlers/migrate.js");
    await runMigrations(ctx);
  },
});

const cli = Cli()
  .scriptName("app")
  .description("Application with lazy-loaded commands")
  .version("1.0.0")
  .command(command)
  .parse();
```

### Benefits

* **Faster startup time**: Only handlers for invoked commands are loaded
* **Lower memory usage**: Unused handlers don't consume memory
* **Better scalability**: Easy to add many commands without performance impact
* **Asynchronous operations**: Handlers can perform async operations like file I/O or network requests

### Example: Modular Command Structure

Directory structure:

```
project/
├── cli.ts
├── handlers/
│   ├── build.ts
│   ├── dev.ts
│   ├── deploy.ts
│   └── test.ts
```

`handlers/build.ts`:

```ts twoslash
// @include: imports
export async function buildProject(ctx) {
  if (ctx.flags.production) {
    console.log("Building for production...");
  } else {
    console.log("Building for development...");
  }
}
```

`cli.ts`:

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("app")
  .version("1.0.0")
  .command("build", "Build the project", {
    flags: {
      production: {
        type: Boolean,
        description: "Build for production",
      },
    },
  })
  .on("build", async (ctx) => {
    const { buildProject } = await import("./handlers/build.js");
    await buildProject(ctx);
  })
  .command("dev", "Start development server", {})
  .on("dev", async (ctx) => {
    const { startDev } = await import("./handlers/dev.js");
    await startDev(ctx);
  })
  .command("deploy", "Deploy application")
  .on("deploy", async (ctx) => {
    const { deploy } = await import("./handlers/deploy.js");
    await deploy(ctx);
  })
  .parse();
```

---

---

url: /official-plugins/plugin-completions.md
---

# @clerc/plugin-completions

A plugin to add command-line autocompletion functionality to your CLI, based on [@bomb.sh/tab](https://github.com/bombshell-dev/tab).

## 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-completions
```

```sh [yarn]
yarn add @clerc/plugin-completions
```

```sh [pnpm]
pnpm add @clerc/plugin-completions
```

:::

## 🚀 Usage

### Import

```ts twoslash
// @include: imports
import { completionsPlugin } from "@clerc/plugin-completions";
// Or import directly from clerc
import { completionsPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(completionsPlugin()) // Add the autocompletion plugin
  .command("start", "Start the service")
  .on("start", (ctx) => {
    console.log("Service started");
  })
  .command("stop", "Stop the service")
  .on("stop", (ctx) => {
    console.log("Service stopped");
  })
  .parse();
```

### Running Effect

```bash
# Generate autocompletion script for Bash
$ my-cli completions bash

# Execute directly to enable autocompletion
# PowerShell
$ my-cli completions powershell | Out-String | Invoke-Expression

# Bash
$ eval "$(my-cli completions bash)"

# Zsh
$ eval "$(my-cli completions zsh)"

# You can also specify the shell type with the --shell parameter
$ eval "$(my-cli completions --shell bash)"
```

## 📝 Features

### Automatic Completion Script Generation

The plugin automatically generates a full autocompletion script for your CLI, supporting:

* Command autocompletion
* Flag autocompletion

### Completion Logic

```sh
my-cli <TAB> # Complete available commands
my-cli command <TAB> # Complete subcommands of the specified command
my-cli -<TAB> # Complete all global short flags, e.g., -h, -V
my-cli --<TAB> # Complete all global long flags
my-cli command -<TAB> # Complete short flags for the specified command (including global flags), e.g., -h, -V
my-cli command --<TAB> # Complete all available flags for the specified command, including global flags
```

### Supported Shells

* **Bash** - Default shell for Linux and macOS
* **Zsh** - Default shell for macOS Catalina and later versions
* **Fish** - A modern shell
* **PowerShell** - Default shell for Windows

---

---

url: /guide/context.md
---

# Context

In both `handler` and `interceptor`, the first parameter received is a context object. The context keys are the same in both cases, only some values will differ.

## Types

```ts twoslash
// @include: imports
export interface BaseContext<
  C extends Command = Command,
  GF extends ClercFlagsDefinition = {},
> {
  resolved: boolean;
  command?: C;
  calledAs?: string;
  parameters: InferParameters<NonNullable<C["parameters"]>>;
  flags: InferFlagsWithGlobal<C, GF>;
  ignored: string[];
  rawParsed: ParsedResult<InferFlagsWithGlobal<C, GF>>;
  store: Partial<ContextStore>;
}
```

* `resolved`: A boolean value indicating whether a matching command was found.
* `command`: The currently parsed command object, or `undefined` if no matching command was found.
* `calledAs`: The command name the user invoked (which could be an alias).
* `parameters`: An object containing the parsed parameter values. It will be an empty object if no command was matched.
* `flags`: An object containing the parsed flag values. It will be an empty object if no command was matched.
* `ignored`: A string array containing arguments that were not parsed.
* `rawParsed`: An object containing the raw parsing result from the parser. This is useful for advanced use cases where you need access to information not exposed by the simplified context properties.
* `store`: A shared storage object that can be used to store data across different parts of the CLI application.

### rawParsed

The `rawParsed` property is of type `ParsedResult` and contains the complete parsing result from the parser. Please refer to [API Reference](https://clerc.so1ve.dev/reference/api/parser/Interface.ParsedResult).

The context for `handler` is a specialization of `BaseContext`. Its `resolved` property is always `true`, and the `command` property is always the current command object, and `calledAs` also always has a value.

---

---

url: /guide/error-handling.md
---

# Error Handling

Clerc supports registering an error handler function to handle errors that occur during command parsing, command runtime, and other processes.

## Example

```ts twoslash
// @include: imports
Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .errorHandler((error: any) => {
    console.error("An error occurred:", error.message);
    // You can perform other actions as needed, such as logging the error or cleaning up resources
  })
  .command("run", "Run the application")
  .on("run", (ctx) => {
    throw new Error("Testing error handling");
  })
  .parse();
```

---

---

url: /guide/flags.md
---

# Flags

Flags are used to provide additional configuration and parameters for commands. Clerc supports various types of options, including built-in JavaScript types such as Boolean, String, Number, and also custom types.

*Clerc*'s flag parsing is powered by [`@clerc/parser`](https://github.com/clercjs/clerc/blob/main/packages/parser) and has many features:

* Array and custom types
* Flag delimiters: `--flag value`, `--flag=value`, `--flag:value` and `--flag.value`
* Combined aliases: `-abcd 2` → `-a -b -c -d 2`
* [End-of-file](https://unix.stackexchange.com/a/11382): pass `--` to end parsing

Flags can be specified in the `flags` object property, where the key is the flag name and the value is either an flag type function or an object describing the flag.

It's recommended to use camelCase for flag names as it will be interpreted as parsing the equivalent kebab-case flag.

The flag type function can be any function that accepts a string and returns the parsed value. The default JavaScript constructors should cover most use cases: [String](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/String), [Number](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/Number), [Boolean](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Boolean/Boolean), etc.

The flag description object can be used to store additional information about the flag, such as `short`, `default`, and `description`. To accept multiple values for a flag, wrap the type function in an array.

All provided information will be used to generate better help documentation.

## Flag Short Names

Flag short names allow users to use single-character shortcuts for flags. This is useful for providing convenient shortcuts for commonly used flags.

### Defining Short Names

You can define a single-character short name for a flag using the `short` property:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("build", "Build the project", {
    flags: {
      output: {
        type: String,
        short: "o",
        description: "Output directory",
      },

      verbose: {
        type: Boolean,
        short: "v",
        description: "Enable verbose output",
      },
    },
  })
  .on("build", (ctx) => {
    // $ node cli.mjs build --output dist
    // $ node cli.mjs build -o dist
    // Both work the same way
    // $ node cli.mjs build --verbose
    // $ node cli.mjs build -v
    // Both enable verbose output
  })
  .parse();
```

### Validation Rules

* Flag names must be at least 2 characters long
* The `short` property must be exactly 1 character

### Combined Short Names

When using short names (single characters), they can be combined together:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("compress", "Compress files", {
    flags: {
      output: {
        type: String,
        short: "o",
        description: "Output file",
      },

      verbose: {
        type: Boolean,
        short: "v",
        description: "Verbose output",
      },

      recursive: {
        type: Boolean,
        short: "r",
        description: "Recursive mode",
      },
    },
  })
  .on("compress", (ctx) => {
    // $ node cli.mjs compress -vrh input.zip
    // Is equivalent to:
    // $ node cli.mjs compress -v -r -h input.zip
    // Which sets: verbose = true, recursive = true, and passes "input.zip" as a parameter
  })
  .parse();
```

## Basic Usage

```ts twoslash
// @include: imports
// $ node ./foo-cli.mjs echo --some-boolean --some-string hello --some-number 1 -n 2

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("echo", "Echo", {
    flags: {
      someBoolean: {
        type: Boolean,
        description: "Some boolean flag",
      },

      someString: {
        type: String,
        description: "Some string flag",
        default: "n/a",
      },

      someNumber: {
        // Wrap the type function in an array to allow multiple values
        type: [Number],
        short: "n",
        description: "Array of numbers. (e.g. -n 1 -n 2 -n 3)",
      },

      object: {
        type: Object,
        description: "An object flag. (e.g. --object.key value)",
      },

      counter: {
        type: [Boolean],
        description: "A counter flag. (e.g. -c -c -c)",
      },
    },
  })
  .on("echo", (ctx) => {
    ctx.flags;
    // ^?
    ctx.flags.someBoolean; // => true
    ctx.flags.someString; // => "hello"
    ctx.flags.someNumber; // => [1, 2]
    ctx.flags.object; // => { key: "value" }
    ctx.flags.counter; // => 2
  })
  .parse();
```

## Flag Description

The `description` property is optional and can be omitted if you don't need to document the flag:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("build", "Build the project", {
    flags: {
      verbose: {
        type: Boolean,
        // description is optional
      },

      output: {
        type: String,
        description: "Output directory", // or include it for better documentation
      },
    },
  })
  .parse();
```

## Required Flags

To make a flag required, you can set the `required` property to `true` in the flag description object:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("deploy", "Deploy the application", {
    flags: {
      env: {
        type: String,
        description: "Deployment environment",
        required: true, // This flag is required
      },
    },
  })
  .on("deploy", (ctx) => {
    ctx.flags.env; // This will always have a value
    //        ^?
  })
  .parse();
```

## Default Values

You can provide default values for flags using the `default` property in the flag description object:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("serve", "Start the server", {
    flags: {
      port: {
        type: Number,
        description: "Port number",
        default: 3000, // Default port is 3000
      },
    },
  })
  .on("serve", (ctx) => {
    ctx.flags.port; // If not provided, this will be 3000
    //        ^?
  })
  .parse();
```

:::warning
If a flag is marked as `required` and also has a `default` value, an `InvalidSchemaError` will be thrown at runtime, and a type error will be raised during type checking.
:::

## Flag Types

For detailed information about flag types, including built-in basic types (String, Boolean, Array, Counter, Object) and advanced types (Enum, Range, Regex), as well as custom type definitions, see the [Types](./types) guide.

```
```

```
```

---

---

url: /official-plugins/plugin-friendly-error.md
---

# @clerc/plugin-friendly-error

A plugin that provides more friendly error messages for your CLI when errors occur.

## 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-friendly-error
```

```sh [yarn]
yarn add @clerc/plugin-friendly-error
```

```sh [pnpm]
pnpm add @clerc/plugin-friendly-error
```

:::

## 🚀 Usage

### Import

```ts twoslash
// @include: imports
import { friendlyErrorPlugin } from "@clerc/plugin-friendly-error";
// or import directly from clerc
import { friendlyErrorPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(friendlyErrorPlugin()) // Add friendly error plugin
  .command("start", "Start service")
  .on("start", (ctx) => {
    // Simulate an error
    throw new Error("Service failed to start");
  })
  .parse();
```

### Running Effect

```bash
$ node my-cli start
# Outputs friendly error message instead of raw error stack
```

---

---

url: /reference/api/clerc/Parser.Function.appendDotValues.md
---

# Function: appendDotValues()

```ts twoslash
// @include: imports
function appendDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L117)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar")

`value`

`any`

The value to set or append (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/core/Parser.Function.appendDotValues.md
---

# Function: appendDotValues()

```ts twoslash
// @include: imports
function appendDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L117)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar")

`value`

`any`

The value to set or append (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/parser/Function.appendDotValues.md
---

# Function: appendDotValues()

```ts twoslash
// @include: imports
function appendDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:117](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L117)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar")

`value`

`any`

The value to set or append (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/utils/Function.camelCase.md
---

# Function: camelCase()

```ts twoslash
// @include: imports
function camelCase(str): string;
```

Defined in: [index.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L19)

Converts a dash- or space-separated string to camelCase.

Not using regexp for better performance, because this function is used in
parser.

## Parameters

`str`

`string`

## Returns

`string`

---

---

url: /reference/api/clerc/Function.Cli.md
---

# Function: Cli()

```ts twoslash
// @include: imports
function Cli(options?): Clerc;
```

Defined in: [packages/clerc/src/index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/clerc/src/index.ts#L8)

## Parameters

`options?`

[`CreateOptions`](Interface.CreateOptions.md)

## Returns

[`Clerc`](Class.Clerc.md)

---

---

url: /reference/api/clerc/Parser.Function.coerceObjectValue.md
---

# Function: coerceObjectValue()

```ts twoslash
// @include: imports
function coerceObjectValue(value): string | boolean;
```

Defined in: [packages/parser/src/utils.ts:77](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L77)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

## Parameters

`value`

`string`

The raw string value from CLI

## Returns

`string` | `boolean`

Coerced value (boolean or string)

---

---

url: /reference/api/core/Parser.Function.coerceObjectValue.md
---

# Function: coerceObjectValue()

```ts twoslash
// @include: imports
function coerceObjectValue(value): string | boolean;
```

Defined in: [packages/parser/src/utils.ts:77](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L77)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

## Parameters

`value`

`string`

The raw string value from CLI

## Returns

`string` | `boolean`

Coerced value (boolean or string)

---

---

url: /reference/api/parser/Function.coerceObjectValue.md
---

# Function: coerceObjectValue()

```ts twoslash
// @include: imports
function coerceObjectValue(value): string | boolean;
```

Defined in: [packages/parser/src/utils.ts:77](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L77)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

## Parameters

`value`

`string`

The raw string value from CLI

## Returns

`string` | `boolean`

Coerced value (boolean or string)

---

---

url: /reference/api/clerc/Function.completionsPlugin.md
---

# Function: completionsPlugin()

```ts twoslash
// @include: imports
function completionsPlugin(): Plugin;
```

Defined in: [packages/plugin-completions/src/index.ts:60](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L60)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-completions/Function.completionsPlugin.md
---

# Function: completionsPlugin()

```ts twoslash
// @include: imports
function completionsPlugin(): Plugin;
```

Defined in: [index.ts:60](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L60)

## Returns

`Plugin`

---

---

url: /reference/api/clerc/Parser.Function.createParser.md
---

# Function: createParser()

```ts twoslash
// @include: imports
function createParser<T>(options): object;
```

Defined in: [packages/parser/src/parse.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L28)

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

## Parameters

`options`

[`ParserOptions`](Parser.Interface.ParserOptions.md)<`T`>

## Returns

`object`

`parse`

`ParseFunction`<`T`>

[packages/parser/src/parse.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L30)

---

---

url: /reference/api/core/Parser.Function.createParser.md
---

# Function: createParser()

```ts twoslash
// @include: imports
function createParser<T>(options): object;
```

Defined in: [packages/parser/src/parse.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L28)

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

## Parameters

`options`

[`ParserOptions`](Parser.Interface.ParserOptions.md)<`T`>

## Returns

`object`

`parse`

`ParseFunction`<`T`>

[packages/parser/src/parse.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L30)

---

---

url: /reference/api/parser/Function.createParser.md
---

# Function: createParser()

```ts twoslash
// @include: imports
function createParser<T>(options): object;
```

Defined in: [packages/parser/src/parse.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L28)

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

## Parameters

`options`

[`ParserOptions`](Interface.ParserOptions.md)<`T`>

## Returns

`object`

`parse`

`ParseFunction`<`T`>

[packages/parser/src/parse.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L30)

---

---

url: /reference/api/clerc/Function.createStopAtFirstParameter.md
---

# Function: createStopAtFirstParameter()

```ts twoslash
// @include: imports
function createStopAtFirstParameter(): IgnoreFunction;
```

Defined in: [packages/core/src/ignore.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/ignore.ts#L4)

## Returns

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

---

---

url: /reference/api/core/Function.createStopAtFirstParameter.md
---

# Function: createStopAtFirstParameter()

```ts twoslash
// @include: imports
function createStopAtFirstParameter(): IgnoreFunction;
```

Defined in: [packages/core/src/ignore.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/ignore.ts#L4)

## Returns

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

---

---

url: /reference/api/clerc/Function.defineCommand.md
---

# Function: defineCommand()

```ts twoslash
// @include: imports
function defineCommand<Name, Parameters, Flags>(
  command,
  handler?,
): CommandWithHandler<Name, Parameters, Flags>;
```

Defined in: [packages/core/src/helpers.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/helpers.ts#L9)

## Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`command`

[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>

`handler?`

`NoInfer`<[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>>

## Returns

[`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>

---

---

url: /reference/api/core/Function.defineCommand.md
---

# Function: defineCommand()

```ts twoslash
// @include: imports
function defineCommand<Name, Parameters, Flags>(
  command,
  handler?,
): CommandWithHandler<Name, Parameters, Flags>;
```

Defined in: [packages/core/src/helpers.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/helpers.ts#L9)

## Type Parameters

`Name` *extends* `string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`command`

[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>

`handler?`

`NoInfer`<[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>>

## Returns

[`CommandWithHandler`](TypeAlias.CommandWithHandler.md)<`Name`, `Parameters`, `Flags`>

---

---

url: /reference/api/clerc/Function.definePlugin.md
---

# Function: definePlugin()

```ts twoslash
// @include: imports
function definePlugin(plugin): Plugin;
```

Defined in: [packages/core/src/plugin.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/plugin.ts#L3)

## Parameters

`plugin`

[`Plugin`](Interface.Plugin.md)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/core/Function.definePlugin.md
---

# Function: definePlugin()

```ts twoslash
// @include: imports
function definePlugin(plugin): Plugin;
```

Defined in: [packages/core/src/plugin.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/plugin.ts#L3)

## Parameters

`plugin`

[`Plugin`](Interface.Plugin.md)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/advanced-types/Function.Enum.md
---

# Function: Enum()

```ts twoslash
// @include: imports
function Enum<T>(...values): TypeFunction<T>;
```

Defined in: [packages/advanced-types/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L23)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

## Type Parameters

`T` *extends* `string`

## Parameters

...`values`

`T`\[]

Array of allowed string values

## Returns

`TypeFunction`<`T`>

A TypeFunction that validates and returns the input value

## Example

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

## Throws

If the value is not in the allowed values list

---

---

url: /reference/api/clerc/Types.Function.Enum.md
---

# Function: Enum()

```ts twoslash
// @include: imports
function Enum<T>(...values): TypeFunction<T>;
```

Defined in: [packages/advanced-types/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L23)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

## Type Parameters

`T` *extends* `string`

## Parameters

...`values`

`T`\[]

Array of allowed string values

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`T`>

A TypeFunction that validates and returns the input value

## Example

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

## Throws

If the value is not in the allowed values list

---

---

url: /reference/api/core/Types.Function.Enum.md
---

# Function: Enum()

```ts twoslash
// @include: imports
function Enum<T>(...values): TypeFunction<T>;
```

Defined in: [packages/advanced-types/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L23)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

## Type Parameters

`T` *extends* `string`

## Parameters

...`values`

`T`\[]

Array of allowed string values

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`T`>

A TypeFunction that validates and returns the input value

## Example

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

## Throws

If the value is not in the allowed values list

---

---

url: /reference/api/clerc/Function.extractParameterInfo.md
---

# Function: extractParameterInfo()

```ts twoslash
// @include: imports
function extractParameterInfo(key): ParameterInfo;
```

Defined in: [packages/core/src/parameter.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/parameter.ts#L33)

## Parameters

`key`

`string`

## Returns

`ParameterInfo`

---

---

url: /reference/api/core/Function.extractParameterInfo.md
---

# Function: extractParameterInfo()

```ts twoslash
// @include: imports
function extractParameterInfo(key): ParameterInfo;
```

Defined in: [packages/core/src/parameter.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/parameter.ts#L33)

## Parameters

`key`

`string`

## Returns

`ParameterInfo`

---

---

url: /reference/api/utils/Function.formatFlagName.md
---

# Function: formatFlagName()

```ts twoslash
// @include: imports
function formatFlagName(n): string;
```

Defined in: [index.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L85)

## Parameters

`n`

`string`

## Returns

`string`

---

---

url: /reference/api/utils/Function.formatVersion.md
---

# Function: formatVersion()

```ts twoslash
// @include: imports
function formatVersion(v): string;
```

Defined in: [index.ts:88](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L88)

## Parameters

`v`

`string`

## Returns

`string`

---

---

url: /reference/api/clerc/Function.friendlyErrorPlugin.md
---

# Function: friendlyErrorPlugin()

```ts twoslash
// @include: imports
function friendlyErrorPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-friendly-error/src/index.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L11)

## Parameters

`__namedParameters`

[`FriendlyErrorPluginOptions`](Interface.FriendlyErrorPluginOptions.md)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-friendly-error/Function.friendlyErrorPlugin.md
---

# Function: friendlyErrorPlugin()

```ts twoslash
// @include: imports
function friendlyErrorPlugin(__namedParameters): Plugin;
```

Defined in: [index.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L11)

## Parameters

`__namedParameters`

[`FriendlyErrorPluginOptions`](Interface.FriendlyErrorPluginOptions.md)

## Returns

`Plugin`

---

---

url: /reference/api/utils/Function.hasOwn.md
---

# Function: hasOwn()

```ts twoslash
// @include: imports
function hasOwn(obj, key): boolean;
```

Defined in: [index.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L105)

## Parameters

`obj`

`object`

`key`

`PropertyKey`

## Returns

`boolean`

---

---

url: /reference/api/clerc/Function.helpPlugin.md
---

# Function: helpPlugin()

```ts twoslash
// @include: imports
function helpPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-help/src/index.ts:107](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L107)

## Parameters

`__namedParameters`

[`HelpPluginOptions`](Interface.HelpPluginOptions.md)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-help/Function.helpPlugin.md
---

# Function: helpPlugin()

```ts twoslash
// @include: imports
function helpPlugin(__namedParameters): Plugin;
```

Defined in: [index.ts:107](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L107)

## Parameters

`__namedParameters`

[`HelpPluginOptions`](Interface.HelpPluginOptions.md)

## Returns

`Plugin`

---

---

url: /reference/api/clerc/Function.inferDefault.md
---

# Function: inferDefault()

```ts twoslash
// @include: imports
function inferDefault(type): unknown;
```

Defined in: [packages/parser/src/utils.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L22)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

## Parameters

`type`

[`TypeValue`](Parser.TypeAlias.TypeValue.md)

The type value (constructor or array of constructor)

## Returns

`unknown`

The inferred default value, or undefined if no implicit default

---

---

url: /reference/api/core/Function.inferDefault.md
---

# Function: inferDefault()

```ts twoslash
// @include: imports
function inferDefault(type): unknown;
```

Defined in: [packages/parser/src/utils.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L22)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

## Parameters

`type`

[`TypeValue`](Parser.TypeAlias.TypeValue.md)

The type value (constructor or array of constructor)

## Returns

`unknown`

The inferred default value, or undefined if no implicit default

---

---

url: /reference/api/parser/Function.inferDefault.md
---

# Function: inferDefault()

```ts twoslash
// @include: imports
function inferDefault(type): unknown;
```

Defined in: [packages/parser/src/utils.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L22)

Infers the implicit default value for a flag type based on its type
constructor. This is useful for help output to show the default values of
types that have built-in defaults.

* Boolean: false
* \[Boolean] (Counter): 0
* \[T] (Array): \[]
* Object: {}
* Others: undefined (no implicit default)

## Parameters

`type`

[`TypeValue`](TypeAlias.TypeValue.md)

The type value (constructor or array of constructor)

## Returns

`unknown`

The inferred default value, or undefined if no implicit default

---

---

url: /reference/api/utils/Function.joinWithAnd.md
---

# Function: joinWithAnd()

```ts twoslash
// @include: imports
function joinWithAnd(values): string;
```

Defined in: [index.ts:69](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L69)

## Parameters

`values`

`string`\[]

## Returns

`string`

---

---

url: /reference/api/utils/Function.kebabCase.md
---

# Function: kebabCase()

```ts twoslash
// @include: imports
function kebabCase<T>(s): string;
```

Defined in: [index.ts:82](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L82)

## Type Parameters

`T` *extends* `string`

## Parameters

`s`

`T`

## Returns

`string`

---

---

url: /reference/api/utils/Function.looseIsArray.md
---

# Function: looseIsArray()

```ts twoslash
// @include: imports
function looseIsArray<T>(arr): arr is readonly T[];
```

Defined in: [index.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L3)

## Type Parameters

`T`

## Parameters

`arr`

`any`

## Returns

`arr is readonly T[]`

---

---

url: /reference/api/clerc/Function.normalizeFlagValue.md
---

# Function: normalizeFlagValue()

```ts twoslash
// @include: imports
function normalizeFlagValue(flag): ClercFlagOptions;
```

Defined in: [packages/core/src/utils.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/utils.ts#L18)

## Parameters

`flag`

[`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

## Returns

[`ClercFlagOptions`](TypeAlias.ClercFlagOptions.md)

---

---

url: /reference/api/core/Function.normalizeFlagValue.md
---

# Function: normalizeFlagValue()

```ts twoslash
// @include: imports
function normalizeFlagValue(flag): ClercFlagOptions;
```

Defined in: [packages/core/src/utils.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/utils.ts#L18)

## Parameters

`flag`

[`ClercFlagDefinitionValue`](TypeAlias.ClercFlagDefinitionValue.md)

## Returns

[`ClercFlagOptions`](TypeAlias.ClercFlagOptions.md)

---

---

url: /reference/api/clerc/Function.normalizeParameterValue.md
---

# Function: normalizeParameterValue()

```ts twoslash
// @include: imports
function normalizeParameterValue(parameter): ParameterOptions;
```

Defined in: [packages/core/src/utils.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/utils.ts#L23)

## Parameters

`parameter`

[`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)

## Returns

[`ParameterOptions`](TypeAlias.ParameterOptions.md)

---

---

url: /reference/api/core/Function.normalizeParameterValue.md
---

# Function: normalizeParameterValue()

```ts twoslash
// @include: imports
function normalizeParameterValue(parameter): ParameterOptions;
```

Defined in: [packages/core/src/utils.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/utils.ts#L23)

## Parameters

`parameter`

[`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)

## Returns

[`ParameterOptions`](TypeAlias.ParameterOptions.md)

---

---

url: /reference/api/clerc/Function.notFoundPlugin.md
---

# Function: notFoundPlugin()

```ts twoslash
// @include: imports
function notFoundPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-not-found/src/index.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L19)

## Parameters

`__namedParameters`

[`NotFoundPluginOptions`](Interface.NotFoundPluginOptions.md)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-not-found/Function.notFoundPlugin.md
---

# Function: notFoundPlugin()

```ts twoslash
// @include: imports
function notFoundPlugin(__namedParameters): Plugin;
```

Defined in: [index.ts:19](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L19)

## Parameters

`__namedParameters`

[`NotFoundPluginOptions`](Interface.NotFoundPluginOptions.md)

## Returns

`Plugin`

---

---

url: /reference/api/utils/Function.objectIsEmpty.md
---

# Function: objectIsEmpty()

```ts twoslash
// @include: imports
function objectIsEmpty(obj): boolean;
```

Defined in: [index.ts:95](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L95)

## Parameters

`obj`

`Record`<`string`, `any`>

## Returns

`boolean`

---

---

url: /reference/api/clerc/Parser.Function.parse.md
---

# Function: parse()

```ts twoslash
// @include: imports
function parse<T>(
  args,
  options,
): ParsedResult<{ [K in string | number | symbol]: _InferFlags<T>[K] }>;
```

Defined in: [packages/parser/src/parse.ts:332](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L332)

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

## Parameters

`args`

`string`\[]

`options`

[`ParserOptions`](Parser.Interface.ParserOptions.md)<`T`>

## Returns

[`ParsedResult`](Parser.Interface.ParsedResult.md)<{ \[K in string | number | symbol]: \_InferFlags\<T>\[K] }>

---

---

url: /reference/api/core/Parser.Function.parse.md
---

# Function: parse()

```ts twoslash
// @include: imports
function parse<T>(
  args,
  options,
): ParsedResult<{ [K in string | number | symbol]: _InferFlags<T>[K] }>;
```

Defined in: [packages/parser/src/parse.ts:332](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L332)

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

## Parameters

`args`

`string`\[]

`options`

[`ParserOptions`](Parser.Interface.ParserOptions.md)<`T`>

## Returns

[`ParsedResult`](Parser.Interface.ParsedResult.md)<{ \[K in string | number | symbol]: \_InferFlags\<T>\[K] }>

---

---

url: /reference/api/parser/Function.parse.md
---

# Function: parse()

```ts twoslash
// @include: imports
function parse<T>(
  args,
  options,
): ParsedResult<{ [K in string | number | symbol]: _InferFlags<T>[K] }>;
```

Defined in: [packages/parser/src/parse.ts:332](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L332)

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

## Parameters

`args`

`string`\[]

`options`

[`ParserOptions`](Interface.ParserOptions.md)<`T`>

## Returns

[`ParsedResult`](Interface.ParsedResult.md)<{ \[K in string | number | symbol]: \_InferFlags\<T>\[K] }>

---

---

url: /reference/api/advanced-types/Function.Range.md
---

# Function: Range()

```ts twoslash
// @include: imports
function Range(min, max): TypeFunction<number>;
```

Defined in: [packages/advanced-types/src/index.ts:49](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L49)

Creates a range type function that validates the input is a number within the
specified range.

## Parameters

`min`

`number`

The minimum acceptable value (inclusive)

`max`

`number`

The maximum acceptable value (inclusive)

## Returns

`TypeFunction`<`number`>

A TypeFunction that validates the input value

## Throws

If the value is not a number or is outside the specified
range

---

---

url: /reference/api/clerc/Types.Function.Range.md
---

# Function: Range()

```ts twoslash
// @include: imports
function Range(min, max): TypeFunction<number>;
```

Defined in: [packages/advanced-types/src/index.ts:49](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L49)

Creates a range type function that validates the input is a number within the
specified range.

## Parameters

`min`

`number`

The minimum acceptable value (inclusive)

`max`

`number`

The maximum acceptable value (inclusive)

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`number`>

A TypeFunction that validates the input value

## Throws

If the value is not a number or is outside the specified
range

---

---

url: /reference/api/core/Types.Function.Range.md
---

# Function: Range()

```ts twoslash
// @include: imports
function Range(min, max): TypeFunction<number>;
```

Defined in: [packages/advanced-types/src/index.ts:49](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L49)

Creates a range type function that validates the input is a number within the
specified range.

## Parameters

`min`

`number`

The minimum acceptable value (inclusive)

`max`

`number`

The maximum acceptable value (inclusive)

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`number`>

A TypeFunction that validates the input value

## Throws

If the value is not a number or is outside the specified
range

---

---

url: /reference/api/advanced-types/Function.Regex.md
---

# Function: Regex()

```ts twoslash
// @include: imports
function Regex(pattern, description?): TypeFunction<string>;
```

Defined in: [packages/advanced-types/src/index.ts:74](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L74)

Creates a regex type function that validates the input against the provided
pattern.

## Parameters

`pattern`

`RegExp`

The regular expression pattern to validate against

`description?`

`string`

Optional description for display purposes

## Returns

`TypeFunction`<`string`>

A TypeFunction that validates the input value

## Throws

If the value does not match the regex pattern

---

---

url: /reference/api/clerc/Types.Function.Regex.md
---

# Function: Regex()

```ts twoslash
// @include: imports
function Regex(pattern, description?): TypeFunction<string>;
```

Defined in: [packages/advanced-types/src/index.ts:74](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L74)

Creates a regex type function that validates the input against the provided
pattern.

## Parameters

`pattern`

`RegExp`

The regular expression pattern to validate against

`description?`

`string`

Optional description for display purposes

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`string`>

A TypeFunction that validates the input value

## Throws

If the value does not match the regex pattern

---

---

url: /reference/api/core/Types.Function.Regex.md
---

# Function: Regex()

```ts twoslash
// @include: imports
function Regex(pattern, description?): TypeFunction<string>;
```

Defined in: [packages/advanced-types/src/index.ts:74](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/advanced-types/src/index.ts#L74)

Creates a regex type function that validates the input against the provided
pattern.

## Parameters

`pattern`

`RegExp`

The regular expression pattern to validate against

`description?`

`string`

Optional description for display purposes

## Returns

[`TypeFunction`](Parser.Interface.TypeFunction.md)<`string`>

A TypeFunction that validates the input value

## Throws

If the value does not match the regex pattern

---

---

url: /reference/api/utils/Function.resolveAsyncValue.md
---

# Function: resolveAsyncValue()

```ts twoslash
// @include: imports
function resolveAsyncValue<T>(value): Promise<T>;
```

Defined in: [index.ts:100](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L100)

## Type Parameters

`T`

## Parameters

`value`

[`MaybeAsyncGetter`](TypeAlias.MaybeAsyncGetter.md)<`T`>

## Returns

`Promise`<`T`>

---

---

url: /reference/api/clerc/Function.resolveCommand.md
---

# Function: resolveCommand()

```ts twoslash
// @include: imports
function resolveCommand(
  commandsMap,
  parameters,
):
  | [
      Command<
        string,
        readonly ParameterDefinitionValue[],
        ClercFlagsDefinition
      >,
      string,
    ]
  | [undefined, undefined];
```

Defined in: [packages/core/src/command.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/command.ts#L3)

## Parameters

`commandsMap`

[`CommandsMap`](TypeAlias.CommandsMap.md)

`parameters`

`string`\[]

## Returns

| \[[`Command`](Interface.Command.md)<`string`, readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[], [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)>, `string`]
| \[`undefined`, `undefined`]

---

---

url: /reference/api/core/Function.resolveCommand.md
---

# Function: resolveCommand()

```ts twoslash
// @include: imports
function resolveCommand(
  commandsMap,
  parameters,
):
  | [
      Command<
        string,
        readonly ParameterDefinitionValue[],
        ClercFlagsDefinition
      >,
      string,
    ]
  | [undefined, undefined];
```

Defined in: [packages/core/src/command.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/command.ts#L3)

## Parameters

`commandsMap`

[`CommandsMap`](TypeAlias.CommandsMap.md)

`parameters`

`string`\[]

## Returns

| \[[`Command`](Interface.Command.md)<`string`, readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[], [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)>, `string`]
| \[`undefined`, `undefined`]

---

---

url: /reference/api/utils/Function.resolveValue.md
---

# Function: resolveValue()

```ts twoslash
// @include: imports
function resolveValue<T>(value): T;
```

Defined in: [index.ts:98](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L98)

## Type Parameters

`T`

## Parameters

`value`

[`MaybeGetter`](TypeAlias.MaybeGetter.md)<`T`>

## Returns

`T`

---

---

url: /reference/api/clerc/Parser.Function.setDotValues.md
---

# Function: setDotValues()

```ts twoslash
// @include: imports
function setDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:96](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L96)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar.baz")

`value`

`any`

The value to set (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/core/Parser.Function.setDotValues.md
---

# Function: setDotValues()

```ts twoslash
// @include: imports
function setDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:96](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L96)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar.baz")

`value`

`any`

The value to set (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/parser/Function.setDotValues.md
---

# Function: setDotValues()

```ts twoslash
// @include: imports
function setDotValues(obj, path, value): void;
```

Defined in: [packages/parser/src/utils.ts:96](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/utils.ts#L96)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## Parameters

`obj`

`any`

The target object

`path`

`string`

Dot-separated path (e.g., "foo.bar.baz")

`value`

`any`

The value to set (used as-is, no type conversion)

## Returns

`void`

---

---

url: /reference/api/clerc/Function.strictFlagsPlugin.md
---

# Function: strictFlagsPlugin()

```ts twoslash
// @include: imports
function strictFlagsPlugin(): Plugin;
```

Defined in: [packages/plugin-strict-flags/src/index.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-strict-flags/src/index.ts#L7)

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-strict-flags/Function.strictFlagsPlugin.md
---

# Function: strictFlagsPlugin()

```ts twoslash
// @include: imports
function strictFlagsPlugin(): Plugin;
```

Defined in: [index.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-strict-flags/src/index.ts#L7)

## Returns

`Plugin`

---

---

url: /reference/api/utils/Function.toArray.md
---

# Function: toArray()

```ts twoslash
// @include: imports
function toArray<T>(a): T[];
```

Defined in: [index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L8)

## Type Parameters

`T`

## Parameters

`a`

[`MaybeArray`](TypeAlias.MaybeArray.md)<`T`>

## Returns

`T`\[]

---

---

url: /reference/api/clerc/Function.updateNotifierPlugin.md
---

# Function: updateNotifierPlugin()

```ts twoslash
// @include: imports
function updateNotifierPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-update-notifier/src/index.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L35)

Plugin to check for CLI updates using update-notifier.

## Parameters

`__namedParameters`

[`UpdateNotifierPluginOptions`](Interface.UpdateNotifierPluginOptions.md)

## Returns

[`Plugin`](Interface.Plugin.md)

## Example

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

---

---

url: /reference/api/plugin-update-notifier/Function.updateNotifierPlugin.md
---

# Function: updateNotifierPlugin()

```ts twoslash
// @include: imports
function updateNotifierPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-update-notifier/src/index.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L35)

Plugin to check for CLI updates using update-notifier.

## Parameters

`__namedParameters`

[`UpdateNotifierPluginOptions`](Interface.UpdateNotifierPluginOptions.md)

## Returns

`Plugin`

## Example

```ts twoslash
// @include: imports
import { Clerc } from "@clerc/core";
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

---

---

url: /reference/api/clerc/Function.versionPlugin.md
---

# Function: versionPlugin()

```ts twoslash
// @include: imports
function versionPlugin(__namedParameters): Plugin;
```

Defined in: [packages/plugin-version/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-version/src/index.ts#L20)

## Parameters

`__namedParameters`

`VersionPluginOptions`

## Returns

[`Plugin`](Interface.Plugin.md)

---

---

url: /reference/api/plugin-version/Function.versionPlugin.md
---

# Function: versionPlugin()

```ts twoslash
// @include: imports
function versionPlugin(__namedParameters): Plugin;
```

Defined in: [index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-version/src/index.ts#L20)

## Parameters

`__namedParameters`

`VersionPluginOptions`

## Returns

`Plugin`

---

---

url: /guide/getting-started.md
---

# Getting Started

:::warning

Clerc is ESM-only!

:::

## Installation

:::info

The `clerc` package exports a `Cli` function, which is equivalent to `Clerc.create().use(versionPlugin).use(helpPlugin)`. This provides a convenient way to create a CLI with both version and help plugins built-in.

If you need more control, you can use `Clerc.create()` directly and manually add plugins.

Note that the `clerc` package may be larger in size since it re-exports all official plugins. However, if your bundler supports tree-shaking, this shouldn't be an issue. To reduce bundle size, consider installing only `@clerc/core` and the plugins you need.

:::

:::code-group

```sh [npm]
npm install clerc
```

```sh [yarn]
yarn add clerc
```

```sh [pnpm]
pnpm add clerc
```

:::

## Simplest CLI Example

Install clerc, and create a file named `cli.mjs`:

```ts twoslash
// @include: imports
import { Cli } from "clerc";

Cli() // Create a new CLI with help and version plugins
  .name("foo") // Optional, CLI readable name
  .scriptName("foo") // CLI script name (the command used to run the CLI)
  .description("A foo CLI") // CLI description
  .version("0.0.0") // CLI version
  .command(
    "bar", // Command name
    "A bar command", // Command description
  )
  .on(
    "bar",
    (
      _ctx, // Command context, but we're not using it yet
    ) => {
      console.log("Hello, world from Clerc.js!");
    },
  )
  .parse(); // Parse arguments and run!
```

Then run: `node cli.mjs bar`. It should output in your shell: `Hello, world from Clerc.js!`

---

---

url: /guide/global-flags.md
---

# Global Flags

Clerc supports registering one or more global flags that can be used across all commands.

More details about flags can be found in the [Flags Documentation](./flags).

## Basic Usage

```ts twoslash
// @include: imports
Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .globalFlag("verbose", "Enable verbose output", {
    type: Boolean,
  }) // Global flag with description
  .command("run", "Run the application")
  .on("run", (ctx) => {
    if (ctx.flags.verbose) {
      console.log("Verbose mode enabled");
    }
    console.log("Running the application...");
  })
  .parse();
```

## Optional Description

The description parameter is optional. You can omit it if you don't need to document the flag:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .globalFlag("verbose", {
    type: Boolean,
    // No description provided
  })
  .globalFlag("debug", "Enable debug mode", {
    type: Boolean,
    // Or with description
  })
  .parse();
```

## Alternative Syntax

Starting from version 1.0.0, you can also use the alternative syntax where the second parameter is an options object instead of a string description:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  // Using options object directly
  .globalFlag("verbose", {
    type: Boolean,
    description: "Enable verbose output",
  })
  // Or without description
  .globalFlag("debug", {
    type: Boolean,
  })
  .parse();
```

---

---

url: /official-plugins/plugin-help.md
---

# @clerc/plugin-help

A plugin that adds help information to your CLI.

:::info

This plugin is built into the `Cli` function exported by the `clerc` package, so you don't need to install it separately to use it.

:::

## Standalone Usage

### 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-help
```

```sh [yarn]
yarn add @clerc/plugin-help
```

```sh [pnpm]
pnpm add @clerc/plugin-help
```

:::

### 🚀 Usage

#### Import

```ts twoslash
// @include: imports
import { helpPlugin } from "@clerc/plugin-help";
// or import directly from clerc
import { helpPlugin } from "clerc";
```

#### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(helpPlugin()) // Add help plugin
  .command("hello", "Greeting command")
  .on("hello", (ctx) => {
    console.log("Hello, World!");
  })
  .parse();
```

## Running Effect

```bash
# Show main help, displays root command help when there is a root command, otherwise shows CLI's own help
$ node my-cli --help
# Show CLI's own help
$ node my-cli help

# Show help for a specific command
$ node my-cli hello --help
$ node my-cli help hello
```

## 📝 Features

### Auto-generate Help

The plugin automatically generates beautiful help information for your CLI, including:

* CLI name, version information, and description
* List of available commands
* List of command parameters
* Command options
* Global options
* Custom notes and examples

## Advanced Usage

### Command and Flag Groups

The help plugin supports organizing commands and flags into logical groups using the `groups` option. This makes your help output more organized and easier to navigate.

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(
    helpPlugin({
      groups: {
        commands: [
          ["dev", "Development Commands"],
          ["build", "Build Commands"],
          ["test", "Testing Commands"],
        ],
        flags: [
          ["input", "Input Options"],
          ["output", "Output Options"],
          ["config", "Configuration Options"],
        ],
        globalFlags: [
          ["help", "Help Options"],
          ["version", "Version Options"],
        ],
      },
    }),
  )
  .command("dev", "Start development server", {
    help: {
      group: "dev", // Assign to "dev" group
    },
  })
  .command("build", "Build the application", {
    help: {
      group: "build", // Assign to "build" group
    },
  })
  .command("test", "Run tests", {
    help: {
      group: "test", // Assign to "test" group
    },
  })
  .parse();
```

### Custom Command Help

You can set the `help` option to customize the help information for each command:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(helpPlugin())
  .command("deploy", "Deploy command", {
    help: {
      show: true, // Show this command in help (default: true)
      notes: [
        "This is a command for deploying applications.",
        "You can use different options to control deployment behavior.",
      ],
      examples: [
        ["my-cli deploy --env production", "Deploy to production environment"],
        [
          "my-cli deploy --env staging --force",
          "Deploy to staging environment and force execution",
        ],
      ],
    },
  })
  .parse();
```

### Hiding Flags from Help

You can hide specific flags from help output by setting `show: false` in the flag's `help` option. This is useful for internal or deprecated flags that you don't want to expose to users.

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(helpPlugin())
  .command("build", "Build the application", {
    flags: {
      output: {
        type: String,
        description: "Output directory",
      },
      internalDebug: {
        type: Boolean,
        description: "Internal debug mode",
        help: { show: false }, // Hidden from help output
      },
    },
  })
  // Hide a global flag
  .globalFlag("trace", "Enable tracing", {
    type: Boolean,
    help: { show: false },
  })
  .parse();
```

When all flags in a group have `show: false`, the entire group section will be hidden. Similarly, if all flags (or global flags) are hidden, the entire "Flags" or "Global Flags" section will not be displayed.

### Plugin Options

You can customize the behavior of the help plugin by passing options:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(
    helpPlugin({
      command: true, // Enable help command
      flag: true, // Enable --help global option
      showHelpWhenNoCommandSpecified: true, // Show help when no command is specified
      notes: [
        "Welcome to my CLI application!",
        "Use --help to see available commands and options.",
      ],
      examples: [
        ["my-cli --help", "Show help information"],
        ["my-cli hello", "Execute greeting command"],
      ],
      header: "Welcome to My CLI application!", // Custom header
      footer: "Thank you for using My CLI application!", // Custom footer
      formatters: {
        // Custom type formatting functions
        formatTypeValue: (type) => {
          if (typeof type === "function") {
            return type.name;
          }

          return `Array<${type[0].name}>`;
        },
      },
    }),
  )
  .parse();
```

### Using cli.store.help

The help plugin also provides a shared API that allows you to dynamically modify properties like help groups at runtime.

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(
    helpPlugin({
      groups: {
        commands: [
          ["dev", "Development Commands"],
          ["build", "Build Commands"],
        ],
        flags: [
          ["input", "Input Options"],
          ["output", "Output Options"],
        ],
      },
    }),
  )
  .command("dev", "Start development server", {
    help: {
      group: "dev", // Assign to the "dev" group
    },
  })
  .command("build", "Build the application", {
    help: {
      group: "build", // Assign to the "build" group
    },
  })
  .on("dev", (ctx) => {
    console.log("Development server started");
  })
  .on("build", (ctx) => {
    console.log("Application built");
  })
  .parse();

cli.store.help.addGroup({
  commands: [["test", "Test"]],
});
```

#### Store API Methods

* `ctx.store.help.addGroup(options)`: Dynamically add help groups at runtime
  * `options.commands`: Array of `[key, name]` tuples for command groups
  * `options.flags`: Array of `[key, name]` tuples for flag groups
  * `options.globalFlags`: Array of `[key, name]` tuples for global flag groups

This allows you to organize your help output into logical sections, making it easier for users to find relevant commands and options.

---

---

url: /guide/interceptors.md
---

# Interceptors

Interceptors are functions that run before or after the command handler is called, similar to middleware in web development.

## Usage

You can add interceptors to your CLI using the `interceptor` method:

```ts twoslash
// @include: imports
import { Clerc } from "clerc";

const cli = Clerc.create()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command")
  .interceptor(async (ctx, next) => {
    console.log("Before foo");
    // You can access the context
    console.log(!!ctx.command); // Was a matching command found?
    await next(); // Call next to continue execution
    console.log("After foo");
  })
  .parse();
```

:::warning

Attention! When calling `next`, make sure to use `await`, otherwise errors might not be caught properly!

:::

## Order

The `interceptor` method accepts either a function or an object:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command")
  .interceptor({
    enforce: "normal", // Default, or "pre", "post"
    handler: async (ctx, next) => {
      console.log("Before foo");
      // You can access the context
      console.log(!!ctx.command); // Was a matching command found?
      await next(); // Call next to continue execution
      console.log("After foo");
    },
  })
  .parse();
```

Therefore, the execution order is as follows:

1. Pre interceptors
2. Normal interceptors
3. Post interceptors

## Calling After the Command Handler

By performing operations after calling `next()`, you can execute some actions after the command handler is called:

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command")
  .interceptor(async (ctx, next) => {
    console.log("Before foo");
    // You can access the context
    console.log(!!ctx.command); // Was a matching command found?
    await next(); // Call next to continue execution
    console.log("After foo");
  })
  .on("foo", (ctx) => {
    console.log("It ran!");
  })
  .parse();

// The output is:
// Before foo
// It ran!
// After foo
```

## Context Type

The context type for interceptors is `InterceptorContext`, which is currently an alias for `BaseContext`, but provides better IDE type display. [See the context documentation](./context) for more information.

## Behavior of Accessing Options and Arguments in Interceptors

In interceptors, you can access `ctx.flags` and `ctx.parameters`. However, be aware that required flag and argument validation errors are only thrown before the command handler is called. This means that if you access a required flag in an interceptor and the user did not provide it, the flag will not be present in `ctx.flags`, and an error will only be thrown later when the command handler is invoked.

---

---

url: /reference/api/clerc/Interface.BaseContext.md
---

# Interface: BaseContext\<C, GF>

Defined in: [packages/core/src/types/context.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L22)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`calledAs?`

`string`

[packages/core/src/types/context.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L27)

&#x20;`command?`

`C`

[packages/core/src/types/context.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L26)

&#x20;`flags`

`InferFlagsWithGlobal`<`C`, `GF`>

[packages/core/src/types/context.ts:29](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L29)

&#x20;`ignored`

`string`\[]

[packages/core/src/types/context.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L30)

&#x20;`parameters`

[`InferParameters`](TypeAlias.InferParameters.md)<`NonNullable`<`C`\[`"parameters"`]>>

[packages/core/src/types/context.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L28)

&#x20;`rawParsed`

[`ParsedResult`](Parser.Interface.ParsedResult.md)<`InferFlagsWithGlobal`<`C`, `GF`>>

[packages/core/src/types/context.ts:31](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L31)

&#x20;`store`

`Partial`<[`ContextStore`](Interface.ContextStore.md)>

[packages/core/src/types/context.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L32)

---

---

url: /reference/api/core/Interface.BaseContext.md
---

# Interface: BaseContext\<C, GF>

Defined in: [packages/core/src/types/context.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L22)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`calledAs?`

`string`

[packages/core/src/types/context.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L27)

&#x20;`command?`

`C`

[packages/core/src/types/context.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L26)

&#x20;`flags`

`InferFlagsWithGlobal`<`C`, `GF`>

[packages/core/src/types/context.ts:29](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L29)

&#x20;`ignored`

`string`\[]

[packages/core/src/types/context.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L30)

&#x20;`parameters`

[`InferParameters`](TypeAlias.InferParameters.md)<`NonNullable`<`C`\[`"parameters"`]>>

[packages/core/src/types/context.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L28)

&#x20;`rawParsed`

[`ParsedResult`](Parser.Interface.ParsedResult.md)<`InferFlagsWithGlobal`<`C`, `GF`>>

[packages/core/src/types/context.ts:31](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L31)

&#x20;`store`

`Partial`<[`ContextStore`](Interface.ContextStore.md)>

[packages/core/src/types/context.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L32)

---

---

url: /reference/api/clerc/Interface.Command.md
---

# Interface: Command\<Name, Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L26)

## Extends

* [`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

[`CommandOptions`](Interface.CommandOptions.md).[`alias`](Interface.CommandOptions.md#alias)

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`completions`](Interface.CommandOptions.md#completions)

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

‐

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

‐

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`description?`

`string`

‐

‐

[packages/core/src/types/command.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L33)

&#x20;`flags?`

`Flags`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`flags`](Interface.CommandOptions.md#flags-1)

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`help`](Interface.CommandOptions.md#help)

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

[`CommandOptions`](Interface.CommandOptions.md).[`ignore`](Interface.CommandOptions.md#ignore)

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`name`

`Name`

‐

‐

[packages/core/src/types/command.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L32)

&#x20;`parameters?`

`Parameters`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`parameters`](Interface.CommandOptions.md#parameters-1)

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)

---

---

url: /reference/api/core/Interface.Command.md
---

# Interface: Command\<Name, Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L26)

## Extends

* [`CommandOptions`](Interface.CommandOptions.md)<`Parameters`, `Flags`>

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

[`CommandOptions`](Interface.CommandOptions.md).[`alias`](Interface.CommandOptions.md#alias)

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`completions`](Interface.CommandOptions.md#completions)

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

‐

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

‐

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`description?`

`string`

‐

‐

[packages/core/src/types/command.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L33)

&#x20;`flags?`

`Flags`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`flags`](Interface.CommandOptions.md#flags-1)

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

`CommandHelpOptions`

Help options for the command.

[`CommandOptions`](Interface.CommandOptions.md).[`help`](Interface.CommandOptions.md#help)

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

[`CommandOptions`](Interface.CommandOptions.md).[`ignore`](Interface.CommandOptions.md#ignore)

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`name`

`Name`

‐

‐

[packages/core/src/types/command.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L32)

&#x20;`parameters?`

`Parameters`

‐

[`CommandOptions`](Interface.CommandOptions.md).[`parameters`](Interface.CommandOptions.md#parameters-1)

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)

---

---

url: /reference/api/clerc/Interface.CommandCustomOptions.md
---

# Interface: CommandCustomOptions

Defined in: [packages/core/src/types/command.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L8)

## Extended by

* [`CommandOptions`](Interface.CommandOptions.md)

## Properties

&#x20;`completions?`

`object`

Completions options for the command.

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

---

---

url: /reference/api/core/Interface.CommandCustomOptions.md
---

# Interface: CommandCustomOptions

Defined in: [packages/core/src/types/command.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L8)

---

---

url: /reference/api/clerc/Interface.CommandHelpOptions.md
---

# Interface: CommandHelpOptions

Defined in: [packages/plugin-help/src/index.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L28)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

‐

[packages/plugin-help/src/index.ts:37](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L37)

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

‐

[packages/plugin-help/src/index.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L32)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[`HelpOptions`](Interface.HelpOptions.md).[`show`](Interface.HelpOptions.md#show)

[packages/plugin-help/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/plugin-help/Interface.CommandHelpOptions.md
---

# Interface: CommandHelpOptions

Defined in: [index.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L28)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

‐

[index.ts:37](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L37)

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

‐

[index.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L32)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[`HelpOptions`](Interface.HelpOptions.md).[`show`](Interface.HelpOptions.md#show)

[index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/clerc/Interface.CommandOptions.md
---

# Interface: CommandOptions\<Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L10)

## Extends

* [`CommandCustomOptions`](Interface.CommandCustomOptions.md)

## Extended by

* [`Command`](Interface.Command.md)

## Type Parameters

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

‐

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

[`CommandCustomOptions`](Interface.CommandCustomOptions.md).[`completions`](Interface.CommandCustomOptions.md#completions)

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

‐

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

‐

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`flags?`

`Flags`

‐

‐

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

[`CommandHelpOptions`](Interface.CommandHelpOptions.md)

Help options for the command.

[`CommandCustomOptions`](Interface.CommandCustomOptions.md).[`help`](Interface.CommandCustomOptions.md#help)

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

‐

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`parameters?`

`Parameters`

‐

‐

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)

---

---

url: /reference/api/core/Interface.CommandOptions.md
---

# Interface: CommandOptions\<Parameters, Flags>

Defined in: [packages/core/src/types/command.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L10)

## Extends

* `CommandCustomOptions`

## Extended by

* [`Command`](Interface.Command.md)

## Type Parameters

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Properties

&#x20;`alias?`

`MaybeArray`<`string`>

‐

‐

[packages/core/src/types/command.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L15)

&#x20;`completions?`

`object`

Completions options for the command.

```ts twoslash
// @include: imports
CommandCustomOptions.completions;
```

[packages/plugin-completions/src/index.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L17)

`completions.handler?`

(`command`) => `void`

Handler to provide custom completions for the command.

‐

[packages/plugin-completions/src/index.ts:27](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L27)

`completions.show?`

`boolean`

Whether to show the command in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

‐

[packages/plugin-completions/src/index.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L23)

&#x20;`flags?`

`Flags`

‐

‐

[packages/core/src/types/command.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L17)

&#x20;`help?`

`CommandHelpOptions`

Help options for the command.

```ts twoslash
// @include: imports
CommandCustomOptions.help;
```

[packages/plugin-help/src/index.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L47)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in ignored.

‐

[packages/core/src/types/command.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L23)

&#x20;`parameters?`

`Parameters`

‐

‐

[packages/core/src/types/command.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L16)

---

---

url: /reference/api/clerc/Interface.ContextStore.md
---

# Interface: ContextStore

Defined in: [packages/core/src/types/context.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L20)

## Properties

&#x20;`help`

`object`

‐

[packages/plugin-help/src/store.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/store.ts#L7)

`help.addGroup`

(`options`) => `void`

‐

[packages/plugin-help/src/store.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/store.ts#L8)

&#x20;`updateNotifier?`

`UpdateNotifier`

The update-notifier instance, available if plugin-update-notifier is
used.

[packages/plugin-update-notifier/src/index.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L18)

---

---

url: /reference/api/core/Interface.ContextStore.md
---

# Interface: ContextStore

Defined in: [packages/core/src/types/context.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/context.ts#L20)

## Properties

&#x20;`help`

`object`

‐

[packages/plugin-help/src/store.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/store.ts#L7)

`help.addGroup`

(`options`) => `void`

‐

[packages/plugin-help/src/store.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/store.ts#L8)

&#x20;`updateNotifier?`

`UpdateNotifier`

The update-notifier instance, available if plugin-update-notifier is
used.

[packages/plugin-update-notifier/src/index.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L18)

---

---

url: /reference/api/clerc/Interface.CreateOptions.md
---

# Interface: CreateOptions

Defined in: [packages/core/src/cli.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L36)

## Properties

&#x20;`description?`

`string`

[packages/core/src/cli.ts:39](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L39)

&#x20;`name?`

`string`

[packages/core/src/cli.ts:37](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L37)

&#x20;`scriptName?`

`string`

[packages/core/src/cli.ts:38](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L38)

&#x20;`version?`

`string`

[packages/core/src/cli.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L40)

---

---

url: /reference/api/core/Interface.CreateOptions.md
---

# Interface: CreateOptions

Defined in: [packages/core/src/cli.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L36)

## Properties

&#x20;`description?`

`string`

[packages/core/src/cli.ts:39](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L39)

&#x20;`name?`

`string`

[packages/core/src/cli.ts:37](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L37)

&#x20;`scriptName?`

`string`

[packages/core/src/cli.ts:38](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L38)

&#x20;`version?`

`string`

[packages/core/src/cli.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L40)

---

---

url: /reference/api/clerc/Interface.FlagCustomOptions.md
---

# Interface: FlagCustomOptions

Defined in: [packages/core/src/types/flag.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L3)

## Properties

&#x20;`completions?`

`object`

Completions options for the flag.

[packages/plugin-completions/src/index.ts:34](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L34)

`completions.handler?`

`OptionHandler`

Handler to provide custom completions for the flag.

[packages/plugin-completions/src/index.ts:44](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L44)

`completions.show?`

`boolean`

Whether to show the flag in completions output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-completions/src/index.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L40)

&#x20;`help?`

[`FlagHelpOptions`](Interface.FlagHelpOptions.md)

Help options for the flag.

[packages/plugin-help/src/index.ts:54](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L54)

---

---

url: /reference/api/core/Interface.FlagCustomOptions.md
---

# Interface: FlagCustomOptions

Defined in: [packages/core/src/types/flag.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L3)

---

---

url: /reference/api/clerc/Parser.Interface.FlagDefaultValueFunction.md
---

# Interface: FlagDefaultValueFunction()\<T>

Defined in: [packages/parser/src/types.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L5)

## Type Parameters

`T`

```ts twoslash
// @include: imports
FlagDefaultValueFunction(): T;
```

Defined in: [packages/parser/src/types.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L6)

## Returns

`T`

## Properties

&#x20;`display?`

`string`

[packages/parser/src/types.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L7)

---

---

url: /reference/api/core/Parser.Interface.FlagDefaultValueFunction.md
---

# Interface: FlagDefaultValueFunction()\<T>

Defined in: [packages/parser/src/types.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L5)

## Type Parameters

`T`

```ts twoslash
// @include: imports
FlagDefaultValueFunction(): T;
```

Defined in: [packages/parser/src/types.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L6)

## Returns

`T`

## Properties

&#x20;`display?`

`string`

[packages/parser/src/types.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L7)

---

---

url: /reference/api/parser/Interface.FlagDefaultValueFunction.md
---

# Interface: FlagDefaultValueFunction()\<T>

Defined in: [packages/parser/src/types.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L5)

## Type Parameters

`T`

```ts twoslash
// @include: imports
FlagDefaultValueFunction(): T;
```

Defined in: [packages/parser/src/types.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L6)

## Returns

`T`

## Properties

&#x20;`display?`

`string`

[packages/parser/src/types.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L7)

---

---

url: /reference/api/clerc/Interface.FlagHelpOptions.md
---

# Interface: FlagHelpOptions

Defined in: [packages/plugin-help/src/index.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L40)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[`HelpOptions`](Interface.HelpOptions.md).[`show`](Interface.HelpOptions.md#show)

[packages/plugin-help/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/plugin-help/Interface.FlagHelpOptions.md
---

# Interface: FlagHelpOptions

Defined in: [index.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L40)

## Extends

* [`HelpOptions`](Interface.HelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[`HelpOptions`](Interface.HelpOptions.md).[`group`](Interface.HelpOptions.md#group)

[index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[`HelpOptions`](Interface.HelpOptions.md).[`show`](Interface.HelpOptions.md#show)

[index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/clerc/Interface.FriendlyErrorPluginOptions.md
---

# Interface: FriendlyErrorPluginOptions

Defined in: [packages/plugin-friendly-error/src/index.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L7)

## Properties

&#x20;`target?`

(`str`) => `void`

[packages/plugin-friendly-error/src/index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L8)

---

---

url: /reference/api/plugin-friendly-error/Interface.FriendlyErrorPluginOptions.md
---

# Interface: FriendlyErrorPluginOptions

Defined in: [index.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L7)

## Properties

&#x20;`target?`

(`str`) => `void`

[index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-friendly-error/src/index.ts#L8)

---

---

url: /reference/api/clerc/Interface.GroupsOptions.md
---

# Interface: GroupsOptions

Defined in: [packages/plugin-help/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L18)

Options for defining groups in help output.

## Properties

&#x20;`commands?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for commands. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L22)

&#x20;`flags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for command-specific flags. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L26)

&#x20;`globalFlags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for global flags. Each group is defined as `[key, name]`.

[packages/plugin-help/src/types.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L30)

---

---

url: /reference/api/plugin-help/Interface.GroupsOptions.md
---

# Interface: GroupsOptions

Defined in: [types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L18)

Options for defining groups in help output.

## Properties

&#x20;`commands?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for commands. Each group is defined as `[key, name]`.

[types.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L22)

&#x20;`flags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for command-specific flags. Each group is defined as `[key, name]`.

[types.ts:26](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L26)

&#x20;`globalFlags?`

[`GroupDefinition`](TypeAlias.GroupDefinition.md)\[]

Groups for global flags. Each group is defined as `[key, name]`.

[types.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L30)

---

---

url: /reference/api/clerc/Interface.HelpOptions.md
---

# Interface: HelpOptions

Defined in: [packages/plugin-help/src/index.ts:14](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L14)

## Extended by

* [`CommandHelpOptions`](Interface.CommandHelpOptions.md)
* [`FlagHelpOptions`](Interface.FlagHelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[packages/plugin-help/src/index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/plugin-help/Interface.HelpOptions.md
---

# Interface: HelpOptions

Defined in: [index.ts:14](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L14)

## Extended by

* [`CommandHelpOptions`](Interface.CommandHelpOptions.md)
* [`FlagHelpOptions`](Interface.FlagHelpOptions.md)

## Properties

&#x20;`group?`

`string`

The group this item belongs to. The group must be defined in the `groups`
option of `helpPlugin()`.

[index.ts:25](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L25)

&#x20;`show?`

`boolean`

Whether to show this item in help output.

**Default**

```ts twoslash
// @include: imports
true;
```

[index.ts:20](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L20)

---

---

url: /reference/api/clerc/Interface.HelpPluginOptions.md
---

# Interface: HelpPluginOptions

Defined in: [packages/plugin-help/src/index.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L58)

## Properties

&#x20;`command?`

`boolean`

Whether to register the `help` command.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:64](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L64)

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

[packages/plugin-help/src/index.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L85)

&#x20;`flag?`

`boolean`

Whether to register the `--help` global flag.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L70)

&#x20;`footer?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Footer to show after the help output.

[packages/plugin-help/src/index.ts:93](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L93)

&#x20;`formatters?`

`Partial`<`Formatters`>

Custom formatters for rendering help.

[packages/plugin-help/src/index.ts:97](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L97)

&#x20;`groups?`

[`GroupsOptions`](Interface.GroupsOptions.md)

Group definitions for commands and flags. Groups allow organizing commands
and flags into logical sections in help output. Each group is defined as
`[key, name]` where `key` is the identifier used in help options and `name`
is the display name shown in help output.

[packages/plugin-help/src/index.ts:104](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L104)

&#x20;`header?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Header to show before the help output.

[packages/plugin-help/src/index.ts:89](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L89)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

[packages/plugin-help/src/index.ts:80](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L80)

&#x20;`showHelpWhenNoCommandSpecified?`

`boolean`

Whether to show help when no command is specified.

**Default**

```ts twoslash
// @include: imports
true;
```

[packages/plugin-help/src/index.ts:76](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L76)

---

---

url: /reference/api/plugin-help/Interface.HelpPluginOptions.md
---

# Interface: HelpPluginOptions

Defined in: [index.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L58)

## Properties

&#x20;`command?`

`boolean`

Whether to register the `help` command.

**Default**

```ts twoslash
// @include: imports
true;
```

[index.ts:64](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L64)

&#x20;`examples?`

`MaybeAsyncGetter`<\[`string`, `string`]\[]>

Examples to show in the help output. Each example is a tuple of `[command,
description]`.

[index.ts:85](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L85)

&#x20;`flag?`

`boolean`

Whether to register the `--help` global flag.

**Default**

```ts twoslash
// @include: imports
true;
```

[index.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L70)

&#x20;`footer?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Footer to show after the help output.

[index.ts:93](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L93)

&#x20;`formatters?`

`Partial`<`Formatters`>

Custom formatters for rendering help.

[index.ts:97](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L97)

&#x20;`groups?`

[`GroupsOptions`](Interface.GroupsOptions.md)

Group definitions for commands and flags. Groups allow organizing commands
and flags into logical sections in help output. Each group is defined as
`[key, name]` where `key` is the identifier used in help options and `name`
is the display name shown in help output.

[index.ts:104](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L104)

&#x20;`header?`

`MaybeAsyncGetter`<`string` | `void` | `undefined`>

Header to show before the help output.

[index.ts:89](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L89)

&#x20;`notes?`

`MaybeAsyncGetter`<`string`\[]>

Notes to show in the help output.

[index.ts:80](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L80)

&#x20;`showHelpWhenNoCommandSpecified?`

`boolean`

Whether to show help when no command is specified.

**Default**

```ts twoslash
// @include: imports
true;
```

[index.ts:76](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/index.ts#L76)

---

---

url: /reference/api/clerc/Interface.InterceptorObject.md
---

# Interface: InterceptorObject\<C, GF>

Defined in: [packages/core/src/types/interceptor.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L28)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`enforce?`

`"pre"` | `"normal"` | `"post"`

[packages/core/src/types/interceptor.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L32)

&#x20;`handler`

[`InterceptorHandler`](TypeAlias.InterceptorHandler.md)<`C`, `GF`>

[packages/core/src/types/interceptor.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L33)

---

---

url: /reference/api/core/Interface.InterceptorObject.md
---

# Interface: InterceptorObject\<C, GF>

Defined in: [packages/core/src/types/interceptor.ts:28](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L28)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Properties

&#x20;`enforce?`

`"pre"` | `"normal"` | `"post"`

[packages/core/src/types/interceptor.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L32)

&#x20;`handler`

[`InterceptorHandler`](TypeAlias.InterceptorHandler.md)<`C`, `GF`>

[packages/core/src/types/interceptor.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L33)

---

---

url: /reference/api/clerc/Interface.NotFoundPluginOptions.md
---

# Interface: NotFoundPluginOptions

Defined in: [packages/plugin-not-found/src/index.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L10)

## Properties

&#x20;`distanceThreshold?`

`number`

Distance threshold for suggesting commands.

**Default**

```ts twoslash
// @include: imports
5;
```

[packages/plugin-not-found/src/index.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L16)

---

---

url: /reference/api/plugin-not-found/Interface.NotFoundPluginOptions.md
---

# Interface: NotFoundPluginOptions

Defined in: [index.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L10)

## Properties

&#x20;`distanceThreshold?`

`number`

Distance threshold for suggesting commands.

**Default**

```ts twoslash
// @include: imports
5;
```

[index.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-not-found/src/index.ts#L16)

---

---

url: /reference/api/clerc/Parser.Interface.ObjectInputType.md
---

# Interface: ObjectInputType

Defined in: [packages/parser/src/types.ts:115](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L115)

## Indexable

```ts twoslash
// @include: imports
[key: string]: RawInputType | ObjectInputType
```

---

---

url: /reference/api/core/Parser.Interface.ObjectInputType.md
---

# Interface: ObjectInputType

Defined in: [packages/parser/src/types.ts:115](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L115)

## Indexable

```ts twoslash
// @include: imports
[key: string]: RawInputType | ObjectInputType
```

---

---

url: /reference/api/parser/Interface.ObjectInputType.md
---

# Interface: ObjectInputType

Defined in: [packages/parser/src/types.ts:115](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L115)

## Indexable

```ts twoslash
// @include: imports
[key: string]: RawInputType | ObjectInputType
```

---

---

url: /reference/api/clerc/Interface.ParameterCustomOptions.md
---

# Interface: ParameterCustomOptions

Defined in: [packages/core/src/types/parameter.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L4)

## Properties

&#x20;`completions?`

`object`

Completions options for the parameter.

[packages/plugin-completions/src/index.ts:51](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L51)

`completions.handler?`

`ArgumentHandler`

Handler to provide custom completions for the parameter.

[packages/plugin-completions/src/index.ts:55](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-completions/src/index.ts#L55)

---

---

url: /reference/api/core/Interface.ParameterCustomOptions.md
---

# Interface: ParameterCustomOptions

Defined in: [packages/core/src/types/parameter.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L4)

---

---

url: /reference/api/clerc/Parser.Interface.ParsedResult.md
---

# Interface: ParsedResult\<TFlags>

Defined in: [packages/parser/src/types.ts:124](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L124)

The parsed result.

## Type Parameters

`TFlags` *extends* `Record`<`string`, `any`>

The specific flags type inferred from ParserOptions.

## Properties

&#x20;`doubleDash`

`string`\[]

Arguments after the `--` delimiter.

[packages/parser/src/types.ts:132](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L132)

&#x20;`flags`

`TFlags`

The parsed flags. This is a strongly-typed object whose structure is
inferred from the `flags` configuration in ParserOptions.

[packages/parser/src/types.ts:137](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L137)

&#x20;`ignored`

`string`\[]

Arguments that were not parsed due to ignore callback.

[packages/parser/src/types.ts:153](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L153)

&#x20;`missingRequiredFlags`

`string`\[]

List of required flags that were not provided.

[packages/parser/src/types.ts:157](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L157)

&#x20;`parameters`

`string`\[]

Positional arguments or commands.

[packages/parser/src/types.ts:128](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L128)

&#x20;`raw`

`string`\[]

The raw command-line arguments.

[packages/parser/src/types.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L141)

&#x20;`rawUnknown`

`string`\[]

Raw arguments for unknown flags (original string form).

[packages/parser/src/types.ts:149](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L149)

&#x20;`unknown`

`Record`<`string`, [`RawInputType`](Parser.TypeAlias.RawInputType.md)>

Unknown flags encountered during parsing.

[packages/parser/src/types.ts:145](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L145)

---

---

url: /reference/api/core/Parser.Interface.ParsedResult.md
---

# Interface: ParsedResult\<TFlags>

Defined in: [packages/parser/src/types.ts:124](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L124)

The parsed result.

## Type Parameters

`TFlags` *extends* `Record`<`string`, `any`>

The specific flags type inferred from ParserOptions.

## Properties

&#x20;`doubleDash`

`string`\[]

Arguments after the `--` delimiter.

[packages/parser/src/types.ts:132](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L132)

&#x20;`flags`

`TFlags`

The parsed flags. This is a strongly-typed object whose structure is
inferred from the `flags` configuration in ParserOptions.

[packages/parser/src/types.ts:137](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L137)

&#x20;`ignored`

`string`\[]

Arguments that were not parsed due to ignore callback.

[packages/parser/src/types.ts:153](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L153)

&#x20;`missingRequiredFlags`

`string`\[]

List of required flags that were not provided.

[packages/parser/src/types.ts:157](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L157)

&#x20;`parameters`

`string`\[]

Positional arguments or commands.

[packages/parser/src/types.ts:128](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L128)

&#x20;`raw`

`string`\[]

The raw command-line arguments.

[packages/parser/src/types.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L141)

&#x20;`rawUnknown`

`string`\[]

Raw arguments for unknown flags (original string form).

[packages/parser/src/types.ts:149](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L149)

&#x20;`unknown`

`Record`<`string`, [`RawInputType`](Parser.TypeAlias.RawInputType.md)>

Unknown flags encountered during parsing.

[packages/parser/src/types.ts:145](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L145)

---

---

url: /reference/api/parser/Interface.ParsedResult.md
---

# Interface: ParsedResult\<TFlags>

Defined in: [packages/parser/src/types.ts:124](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L124)

The parsed result.

## Type Parameters

`TFlags` *extends* `Record`<`string`, `any`>

The specific flags type inferred from ParserOptions.

## Properties

&#x20;`doubleDash`

`string`\[]

Arguments after the `--` delimiter.

[packages/parser/src/types.ts:132](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L132)

&#x20;`flags`

`TFlags`

The parsed flags. This is a strongly-typed object whose structure is
inferred from the `flags` configuration in ParserOptions.

[packages/parser/src/types.ts:137](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L137)

&#x20;`ignored`

`string`\[]

Arguments that were not parsed due to ignore callback.

[packages/parser/src/types.ts:153](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L153)

&#x20;`missingRequiredFlags`

`string`\[]

List of required flags that were not provided.

[packages/parser/src/types.ts:157](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L157)

&#x20;`parameters`

`string`\[]

Positional arguments or commands.

[packages/parser/src/types.ts:128](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L128)

&#x20;`raw`

`string`\[]

The raw command-line arguments.

[packages/parser/src/types.ts:141](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L141)

&#x20;`rawUnknown`

`string`\[]

Raw arguments for unknown flags (original string form).

[packages/parser/src/types.ts:149](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L149)

&#x20;`unknown`

`Record`<`string`, [`RawInputType`](TypeAlias.RawInputType.md)>

Unknown flags encountered during parsing.

[packages/parser/src/types.ts:145](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L145)

---

---

url: /reference/api/clerc/Interface.ParseOptions.md
---

# Interface: ParseOptions\<Run>

Defined in: [packages/core/src/cli.ts:43](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L43)

## Type Parameters

`Run` *extends* `boolean`

`true`

## Properties

&#x20;`argv?`

`string`\[]

[packages/core/src/cli.ts:44](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L44)

&#x20;`run?`

`Run`

[packages/core/src/cli.ts:45](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L45)

---

---

url: /reference/api/core/Interface.ParseOptions.md
---

# Interface: ParseOptions\<Run>

Defined in: [packages/core/src/cli.ts:43](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L43)

## Type Parameters

`Run` *extends* `boolean`

`true`

## Properties

&#x20;`argv?`

`string`\[]

[packages/core/src/cli.ts:44](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L44)

&#x20;`run?`

`Run`

[packages/core/src/cli.ts:45](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/cli.ts#L45)

---

---

url: /reference/api/clerc/Parser.Interface.ParserOptions.md
---

# Interface: ParserOptions\<T>

Defined in: [packages/parser/src/types.ts:92](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L92)

Configuration options for the parser.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

`object`

## Properties

&#x20;`delimiters?`

`string`\[]

Delimiters to split flag names and values.

**Default**

```ts twoslash
// @include: imports
["=", ":"];
```

[packages/parser/src/types.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L105)

&#x20;`flags?`

`T`

Detailed configuration for flags. Supports the full object syntax or a type
constructor as a shorthand. The key is the flag name (e.g., "file" for
"--file").

[packages/parser/src/types.ts:98](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L98)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[packages/parser/src/types.ts:111](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L111)

---

---

url: /reference/api/core/Parser.Interface.ParserOptions.md
---

# Interface: ParserOptions\<T>

Defined in: [packages/parser/src/types.ts:92](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L92)

Configuration options for the parser.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

`object`

## Properties

&#x20;`delimiters?`

`string`\[]

Delimiters to split flag names and values.

**Default**

```ts twoslash
// @include: imports
["=", ":"];
```

[packages/parser/src/types.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L105)

&#x20;`flags?`

`T`

Detailed configuration for flags. Supports the full object syntax or a type
constructor as a shorthand. The key is the flag name (e.g., "file" for
"--file").

[packages/parser/src/types.ts:98](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L98)

&#x20;`ignore?`

[`IgnoreFunction`](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[packages/parser/src/types.ts:111](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L111)

---

---

url: /reference/api/parser/Interface.ParserOptions.md
---

# Interface: ParserOptions\<T>

Defined in: [packages/parser/src/types.ts:92](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L92)

Configuration options for the parser.

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

`object`

## Properties

&#x20;`delimiters?`

`string`\[]

Delimiters to split flag names and values.

**Default**

```ts twoslash
// @include: imports
["=", ":"];
```

[packages/parser/src/types.ts:105](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L105)

&#x20;`flags?`

`T`

Detailed configuration for flags. Supports the full object syntax or a type
constructor as a shorthand. The key is the flag name (e.g., "file" for
"--file").

[packages/parser/src/types.ts:98](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L98)

&#x20;`ignore?`

[`IgnoreFunction`](TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[packages/parser/src/types.ts:111](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L111)

---

---

url: /reference/api/clerc/Interface.Plugin.md
---

# Interface: Plugin

Defined in: [packages/core/src/types/plugin.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/plugin.ts#L3)

## Properties

&#x20;`setup`

(`cli`) => `void`

[packages/core/src/types/plugin.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/plugin.ts#L4)

---

---

url: /reference/api/core/Interface.Plugin.md
---

# Interface: Plugin

Defined in: [packages/core/src/types/plugin.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/plugin.ts#L3)

## Properties

&#x20;`setup`

(`cli`) => `void`

[packages/core/src/types/plugin.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/plugin.ts#L4)

---

---

url: /reference/api/clerc/Parser.Interface.TypeFunction.md
---

# Interface: TypeFunction()\<T>

Defined in: [packages/parser/src/types.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L17)

Defines how a string input is converted to the target type T.

## Type Parameters

`T`

`unknown`

The target type.

```ts twoslash
// @include: imports
TypeFunction(value): T;
```

Defined in: [packages/parser/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L18)

Defines how a string input is converted to the target type T.

## Parameters

`value`

`string`

## Returns

`T`

## Properties

&#x20;`display?`

`string`

Optional display name for the type, useful in help output. If provided,
this will be shown instead of the function name.

[packages/parser/src/types.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L23)

---

---

url: /reference/api/core/Parser.Interface.TypeFunction.md
---

# Interface: TypeFunction()\<T>

Defined in: [packages/parser/src/types.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L17)

Defines how a string input is converted to the target type T.

## Type Parameters

`T`

`unknown`

The target type.

```ts twoslash
// @include: imports
TypeFunction(value): T;
```

Defined in: [packages/parser/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L18)

Defines how a string input is converted to the target type T.

## Parameters

`value`

`string`

## Returns

`T`

## Properties

&#x20;`display?`

`string`

Optional display name for the type, useful in help output. If provided,
this will be shown instead of the function name.

[packages/parser/src/types.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L23)

---

---

url: /reference/api/parser/Interface.TypeFunction.md
---

# Interface: TypeFunction()\<T>

Defined in: [packages/parser/src/types.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L17)

Defines how a string input is converted to the target type T.

## Type Parameters

`T`

`unknown`

The target type.

```ts twoslash
// @include: imports
TypeFunction(value): T;
```

Defined in: [packages/parser/src/types.ts:18](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L18)

Defines how a string input is converted to the target type T.

## Parameters

`value`

`string`

## Returns

`T`

## Properties

&#x20;`display?`

`string`

Optional display name for the type, useful in help output. If provided,
this will be shown instead of the function name.

[packages/parser/src/types.ts:23](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L23)

---

---

url: /reference/api/clerc/Interface.UpdateNotifierPluginOptions.md
---

# Interface: UpdateNotifierPluginOptions

Defined in: [packages/plugin-update-notifier/src/index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L8)

## Extends

* `EnhancedNotifierSettings`

## Properties

&#x20;`distTag?`

`string`

Which dist-tag to use to find the latest version

**Default**

```ts twoslash
// @include: imports
"latest";
```

```ts twoslash
// @include: imports
EnhancedNotifierSettings.distTag;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:24

&#x20;`notify?`

`EnhancedNotifyOptions`

‐

‐

[packages/plugin-update-notifier/src/index.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L9)

&#x20;\~~`packageName?`~~

`string`

**Deprecated**

use `pkg.name`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageName;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:29

&#x20;\~~`packageVersion?`~~

`string`

**Deprecated**

use `pkg.version`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageVersion;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:33

&#x20;`pkg`

`Package`

‐

```ts twoslash
// @include: imports
EnhancedNotifierSettings.pkg;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:25

&#x20;`shouldNotifyInNpmScript?`

`boolean`

Allows notification to be shown when running as an npm script

```ts twoslash
// @include: imports
EnhancedNotifierSettings.shouldNotifyInNpmScript;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:37

&#x20;`updateCheckInterval?`

`number`

How often to check for updates

```ts twoslash
// @include: imports
EnhancedNotifierSettings.updateCheckInterval;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:35

---

---

url: /reference/api/plugin-update-notifier/Interface.UpdateNotifierPluginOptions.md
---

# Interface: UpdateNotifierPluginOptions

Defined in: [packages/plugin-update-notifier/src/index.ts:8](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L8)

## Extends

* `EnhancedNotifierSettings`

## Properties

&#x20;`distTag?`

`string`

Which dist-tag to use to find the latest version

**Default**

```ts twoslash
// @include: imports
"latest";
```

```ts twoslash
// @include: imports
EnhancedNotifierSettings.distTag;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:24

&#x20;`notify?`

`EnhancedNotifyOptions`

‐

‐

[packages/plugin-update-notifier/src/index.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-update-notifier/src/index.ts#L9)

&#x20;\~~`packageName?`~~

`string`

**Deprecated**

use `pkg.name`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageName;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:29

&#x20;\~~`packageVersion?`~~

`string`

**Deprecated**

use `pkg.version`

```ts twoslash
// @include: imports
EnhancedNotifierSettings.packageVersion;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:33

&#x20;`pkg`

`Package`

‐

```ts twoslash
// @include: imports
EnhancedNotifierSettings.pkg;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:25

&#x20;`shouldNotifyInNpmScript?`

`boolean`

Allows notification to be shown when running as an npm script

```ts twoslash
// @include: imports
EnhancedNotifierSettings.shouldNotifyInNpmScript;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:37

&#x20;`updateCheckInterval?`

`number`

How often to check for updates

```ts twoslash
// @include: imports
EnhancedNotifierSettings.updateCheckInterval;
```

node\_modules/.pnpm/@types+update-notifier@6.0.8/node\_modules/@types/update-notifier/update-notifier.d.ts:35

---

---

url: /official-plugins/plugin-not-found.md
---

# @clerc/plugin-not-found

A plugin that displays friendly error messages and suggests possible commands when a command is not found.

## 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-not-found
```

```sh [yarn]
yarn add @clerc/plugin-not-found
```

```sh [pnpm]
pnpm add @clerc/plugin-not-found
```

:::

## 🚀 Usage

### Import

```ts twoslash
// @include: imports
import { notFoundPlugin } from "@clerc/plugin-not-found";
// or import directly from clerc
import { notFoundPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(notFoundPlugin()) // Add not found plugin
  .command("start", "Start service")
  .on("start", (ctx) => {
    console.log("Service started");
  })
  .parse();
```

### Running Effect

```bash
# When user enters a non-existent command
$ node my-cli star
# Command "star" not found.
# Did you mean "start"?
```

---

---

url: /guide/parameters.md
---

# Parameters

Parameters (also known as *positional arguments*) are names that correspond to argument values. Think of parameters as variable names and argument values as values associated with variables.

This guide covers parameter definitions, types, and descriptions.

## Basic Parameter Definition

You can define parameters in the `parameters` array property to access specific arguments by name. Parameters can be defined in the following formats:

* **Required parameters** are denoted by angle brackets (e.g., `<parameter name>`).
* **Optional parameters** are denoted by square brackets (e.g., `[parameter name]`).
* **Spread parameters** are denoted by the `...` suffix (e.g., `<parameter name...>` or `[parameter name...]`).

Note that required parameters **cannot come after optional parameters**, and spread parameters must be placed last.

Parameters can be accessed using camelCase notation on the `ctx.parameters` property.

Example:

```ts twoslash
// @include: imports
// $ node ./foo-cli.mjs a b c d

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("foo", "A foo command", {
    parameters: [
      "<required parameter>",
      "[optional parameter]",
      "[optional spread...]",
    ],
  })
  .on("foo", (ctx) => {
    ctx.parameters;
    //  ^?
    ctx.parameters.requiredParameter; // => "a"
    ctx.parameters.optionalParameter; // => "b"
    ctx.parameters.optionalSpread; // => ["c", "d"]
  })
  .parse();
```

## Parameter Objects

For more advanced parameter configuration, you can use parameter objects instead of simple strings. Parameter objects allow you to:

* Add a type to validate and convert parameter values
* Add a description for documentation and help output

### Basic Parameter Object

```ts twoslash
// @include: imports
const cli = Cli()
  .scriptName("config-cli")
  .description("Configuration tool")
  .version("1.0.0")
  .command("set", "Set a configuration value", {
    parameters: [
      {
        key: "<key>",
        description: "Configuration key name",
      },
      {
        key: "<value>",
        description: "Configuration value",
        type: String,
      },
    ],
  })
  .on("set", (ctx) => {
    console.log(`Setting ${ctx.parameters.key} to ${ctx.parameters.value}`);
  })
  .parse();
```

## Parameter Types

Parameter types allow you to validate, convert, and parse parameter values, and provide valid options in help documentation. Parameter types use the same functions as [flag types](./types), meaning you can share the same type definitions between parameters and flags. When a type is specified for a parameter, the parsed value will be automatically converted to the type.

By default, the parameter type is `String`.

For comprehensive information about all available types, see the [Types](./types) guide.

## End-of-File

The end-of-file (`--`) (also known as *flag terminator*) allows users to pass a portion of arguments. This is useful for arguments that should be parsed separately from other arguments or arguments that look like flags.

An example is [`npm run`](https://docs.npmjs.com/cli/v8/commands/npm-run-script):

```sh
npm run <script> -- <script arguments>
```

The `--` indicates that all arguments after it should be passed to the *script* rather than *npm*.

You can specify `--` in the `parameters` array to parse flag terminator arguments.

:::warning

You can only define one `--` parameter in the `parameters` array. If multiple `--` parameters are defined, only the first one will be considered, and the rest will be ignored.

You can only define `--` in string format; defining it as a parameter object will not work.

:::

Example:

```ts twoslash
// @include: imports
// $ node ./foo-cli.mjs echo -- hello world

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .command("echo", "Echo", {
    parameters: ["<script>", "--", "[arguments...]"],
  })
  .on("echo", (ctx) => {
    ctx.parameters;
    //  ^?
    ctx.parameters.script; // => "echo"
    ctx.parameters.arguments; // => ["hello", "world"]
  })
  .parse();
```

---

---

url: /reference/api/clerc/Namespace.Parser.md
---

# Parser

## Classes

[InvalidSchemaError](Parser.Class.InvalidSchemaError.md)

‐

## Interfaces

[FlagDefaultValueFunction](Parser.Interface.FlagDefaultValueFunction.md)

‐

[ObjectInputType](Parser.Interface.ObjectInputType.md)

‐

[ParsedResult](Parser.Interface.ParsedResult.md)

The parsed result.

[ParserOptions](Parser.Interface.ParserOptions.md)

Configuration options for the parser.

[TypeFunction](Parser.Interface.TypeFunction.md)

Defines how a string input is converted to the target type T.

## Type Aliases

[BaseFlagOptions](Parser.TypeAlias.BaseFlagOptions.md)

‐

[FlagDefaultValue](Parser.TypeAlias.FlagDefaultValue.md)

‐

[FlagDefinitionValue](Parser.TypeAlias.FlagDefinitionValue.md)

‐

[FlagOptions](Parser.TypeAlias.FlagOptions.md)

‐

[FlagsDefinition](Parser.TypeAlias.FlagsDefinition.md)

‐

[IgnoreFunction](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[InferFlags](Parser.TypeAlias.InferFlags.md)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

[RawInputType](Parser.TypeAlias.RawInputType.md)

‐

[TypeValue](Parser.TypeAlias.TypeValue.md)

‐

## Functions

[appendDotValues](Parser.Function.appendDotValues.md)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

[coerceObjectValue](Parser.Function.coerceObjectValue.md)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

[createParser](Parser.Function.createParser.md)

‐

[parse](Parser.Function.parse.md)

‐

[setDotValues](Parser.Function.setDotValues.md)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## References

### DOUBLE\_DASH

Re-exports [DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

***

### inferDefault

Re-exports [inferDefault](Function.inferDefault.md)

***

### KNOWN\_FLAG

Re-exports [KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

***

### PARAMETER

Re-exports [PARAMETER](Variable.PARAMETER.md)

***

### UNKNOWN\_FLAG

Re-exports [UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

---

---

url: /reference/api/core/Namespace.Parser.md
---

# Parser

## Classes

[InvalidSchemaError](Parser.Class.InvalidSchemaError.md)

‐

## Interfaces

[FlagDefaultValueFunction](Parser.Interface.FlagDefaultValueFunction.md)

‐

[ObjectInputType](Parser.Interface.ObjectInputType.md)

‐

[ParsedResult](Parser.Interface.ParsedResult.md)

The parsed result.

[ParserOptions](Parser.Interface.ParserOptions.md)

Configuration options for the parser.

[TypeFunction](Parser.Interface.TypeFunction.md)

Defines how a string input is converted to the target type T.

## Type Aliases

[BaseFlagOptions](Parser.TypeAlias.BaseFlagOptions.md)

‐

[FlagDefaultValue](Parser.TypeAlias.FlagDefaultValue.md)

‐

[FlagDefinitionValue](Parser.TypeAlias.FlagDefinitionValue.md)

‐

[FlagOptions](Parser.TypeAlias.FlagOptions.md)

‐

[FlagsDefinition](Parser.TypeAlias.FlagsDefinition.md)

‐

[IgnoreFunction](Parser.TypeAlias.IgnoreFunction.md)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

[InferFlags](Parser.TypeAlias.InferFlags.md)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

[RawInputType](Parser.TypeAlias.RawInputType.md)

‐

[TypeValue](Parser.TypeAlias.TypeValue.md)

‐

## Functions

[appendDotValues](Parser.Function.appendDotValues.md)

Similar to setDotValues but handles duplicate keys by converting to arrays.
Does NOT apply type conversion - value is set as-is. Useful for flags that
can be specified multiple times.

[coerceObjectValue](Parser.Function.coerceObjectValue.md)

Default value coercion for Object type. Converts "true" / "" to true, "false"
to false, other values remain unchanged.

[createParser](Parser.Function.createParser.md)

‐

[parse](Parser.Function.parse.md)

‐

[setDotValues](Parser.Function.setDotValues.md)

Sets a value at a nested path in an object, creating intermediate objects as
needed. Does NOT apply type conversion - value is set as-is. Overwrites
existing values.

## References

### DOUBLE\_DASH

Re-exports [DOUBLE\_DASH](Variable.DOUBLE_DASH.md)

***

### inferDefault

Re-exports [inferDefault](Function.inferDefault.md)

***

### KNOWN\_FLAG

Re-exports [KNOWN\_FLAG](Variable.KNOWN_FLAG.md)

***

### PARAMETER

Re-exports [PARAMETER](Variable.PARAMETER.md)

***

### UNKNOWN\_FLAG

Re-exports [UNKNOWN\_FLAG](Variable.UNKNOWN_FLAG.md)

---

---

url: /guide/plugins.md
---

# Plugins

A plugin is a function that can accept a `Clerc` instance and extend it.

:::info

The plugin system allows you to add rich functionality according to your needs.

:::

## Usage

```ts twoslash
// @include: imports
import { definePlugin } from "clerc";

const plugin = definePlugin({
  setup: (cli) =>
    cli.command("foo", "A foo command").on("foo", (ctx) => {
      console.log("It works!");
    }),
});

const cli = Cli()
  .scriptName("foo-cli")
  .description("A simple CLI")
  .version("1.0.0")
  .use(plugin)
  .parse();
```

## Development

In the `setup` function, you can directly get the `Clerc` instance and perform various configurations and extensions on it, such as adding commands, event listeners, etc.

```ts twoslash
// @include: imports
import { definePlugin } from "clerc";

export const myPlugin = definePlugin({
  setup: (cli) => {
    // Extend the cli here
    return cli.command("bar", "A bar command").on("bar", (ctx) => {
      console.log("Bar command executed!");
    });
  },
});
```

## Extending Custom Option Types

If your plugin needs to add custom types for commands, flags or parameters, you can use the following method:

```ts twoslash
// @include: imports
declare module "@clerc/core" {
  // For adding custom types to commands
  export interface CommandCustomOptions {
    foo: string;
  }

  // For adding custom types to options
  export interface FlagCustomOptions {
    foo: string;
  }

  // For adding custom types to parameters
  export interface ParameterCustomOptions {
    foo: string;
  }
}
```

## Publishing Plugins

While not mandatory, it is recommended that you follow the following conventions when publishing plugins to make it easier for users to identify and use your plugins:

* Use `clerc-plugin-<name>` as the package name.
* Add the keyword `clerc-plugin` in `package.json`.

---

---

url: /official-plugins/plugin-strict-flags.md
---

# @clerc/plugin-strict-flags

A plugin that throws an error when unknown flags are passed.

## 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-strict-flags
```

```sh [yarn]
yarn add @clerc/plugin-strict-flags
```

```sh [pnpm]
pnpm add @clerc/plugin-strict-flags
```

:::

## 🚀 Usage

### Import

```ts twoslash
// @include: imports
import { strictFlagsPlugin } from "@clerc/plugin-strict-flags";
// or import directly from clerc
import { strictFlagsPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(strictFlagsPlugin()) // Add strict flags plugin
  .command("start", "Start service", {
    flags: {
      port: {
        type: Number,
        description: "Service port",
        default: 3000,
      },
      host: {
        type: String,
        description: "Service host",
        default: "localhost",
      },
    },
  })
  .on("start", (ctx) => {
    console.log(`Starting service on ${ctx.flags.host}:${ctx.flags.port}`);
  })
  .parse();
```

### Running Effect

```bash
# Correct usage
$ node my-cli start --port 8080 --host 0.0.0.0
# Output: Starting service on 0.0.0.0:8080

# Passing unknown flags will throw an error
$ node my-cli start --port 8080 --unknown-flag
# Unexpected flag: --unknown-flag
```

---

---

url: /reference/api/clerc/Parser.TypeAlias.BaseFlagOptions.md
---

# Type Alias: BaseFlagOptions\<T>

```ts twoslash
// @include: imports
type BaseFlagOptions<T> = FlagRequiredOrDefault & object;
```

Defined in: [packages/parser/src/types.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L58)

## Type Declaration

`short?`

`string`

Short flag alias (single character).

[packages/parser/src/types.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L70)

`type`

`T`

The type constructor or a function to convert the string value. To
support multiple occurrences of a flag (e.g., --file a --file b), wrap
the type in an array: \[String], \[Number]. e.g., String, Number, \[String],
(val) => val.split(',')

[packages/parser/src/types.ts:66](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L66)

## Type Parameters

`T` *extends* [`TypeValue`](Parser.TypeAlias.TypeValue.md)

[`TypeValue`](Parser.TypeAlias.TypeValue.md)

---

---

url: /reference/api/core/Parser.TypeAlias.BaseFlagOptions.md
---

# Type Alias: BaseFlagOptions\<T>

```ts twoslash
// @include: imports
type BaseFlagOptions<T> = FlagRequiredOrDefault & object;
```

Defined in: [packages/parser/src/types.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L58)

## Type Declaration

`short?`

`string`

Short flag alias (single character).

[packages/parser/src/types.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L70)

`type`

`T`

The type constructor or a function to convert the string value. To
support multiple occurrences of a flag (e.g., --file a --file b), wrap
the type in an array: \[String], \[Number]. e.g., String, Number, \[String],
(val) => val.split(',')

[packages/parser/src/types.ts:66](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L66)

## Type Parameters

`T` *extends* [`TypeValue`](Parser.TypeAlias.TypeValue.md)

[`TypeValue`](Parser.TypeAlias.TypeValue.md)

---

---

url: /reference/api/parser/TypeAlias.BaseFlagOptions.md
---

# Type Alias: BaseFlagOptions\<T>

```ts twoslash
// @include: imports
type BaseFlagOptions<T> = FlagRequiredOrDefault & object;
```

Defined in: [packages/parser/src/types.ts:58](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L58)

## Type Declaration

`short?`

`string`

Short flag alias (single character).

[packages/parser/src/types.ts:70](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L70)

`type`

`T`

The type constructor or a function to convert the string value. To
support multiple occurrences of a flag (e.g., --file a --file b), wrap
the type in an array: \[String], \[Number]. e.g., String, Number, \[String],
(val) => val.split(',')

[packages/parser/src/types.ts:66](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L66)

## Type Parameters

`T` *extends* [`TypeValue`](TypeAlias.TypeValue.md)

[`TypeValue`](TypeAlias.TypeValue.md)

---

---

url: /reference/api/utils/TypeAlias.CamelCase.md
---

# Type Alias: CamelCase\<S>

```ts twoslash
// @include: imports
type CamelCase<S> = S extends `${infer Head} ${infer Tail}`
  ? `${Head}${Capitalize<CamelCase<Tail>>}`
  : S extends `${infer Head}-${infer Tail}`
    ? `${Head}${Capitalize<CamelCase<Tail>>}`
    : S;
```

Defined in: [types/index.ts:16](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L16)

## Type Parameters

`S` *extends* `string`

---

---

url: /reference/api/clerc/TypeAlias.ClercFlagDefinitionValue.md
---

# Type Alias: ClercFlagDefinitionValue

```ts twoslash
// @include: imports
type ClercFlagDefinitionValue = ClercFlagOptions | TypeValue;
```

Defined in: [packages/core/src/types/flag.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L9)

---

---

url: /reference/api/core/TypeAlias.ClercFlagDefinitionValue.md
---

# Type Alias: ClercFlagDefinitionValue

```ts twoslash
// @include: imports
type ClercFlagDefinitionValue = ClercFlagOptions | TypeValue;
```

Defined in: [packages/core/src/types/flag.ts:9](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L9)

---

---

url: /reference/api/clerc/TypeAlias.ClercFlagOptions.md
---

# Type Alias: ClercFlagOptions

```ts twoslash
// @include: imports
type ClercFlagOptions = FlagOptions & object & FlagCustomOptions;
```

Defined in: [packages/core/src/types/flag.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L5)

## Type Declaration

`description?`

`string`

[packages/core/src/types/flag.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L6)

---

---

url: /reference/api/core/TypeAlias.ClercFlagOptions.md
---

# Type Alias: ClercFlagOptions

```ts twoslash
// @include: imports
type ClercFlagOptions = FlagOptions & object & FlagCustomOptions;
```

Defined in: [packages/core/src/types/flag.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L5)

## Type Declaration

`description?`

`string`

[packages/core/src/types/flag.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L6)

---

---

url: /reference/api/clerc/TypeAlias.ClercFlagsDefinition.md
---

# Type Alias: ClercFlagsDefinition

```ts twoslash
// @include: imports
type ClercFlagsDefinition = Record<string, ClercFlagDefinitionValue>;
```

Defined in: [packages/core/src/types/flag.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L11)

---

---

url: /reference/api/core/TypeAlias.ClercFlagsDefinition.md
---

# Type Alias: ClercFlagsDefinition

```ts twoslash
// @include: imports
type ClercFlagsDefinition = Record<string, ClercFlagDefinitionValue>;
```

Defined in: [packages/core/src/types/flag.ts:11](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/flag.ts#L11)

---

---

url: /reference/api/clerc/TypeAlias.CommandHandler.md
---

# Type Alias: CommandHandler()\<C, GF>

```ts twoslash
// @include: imports
type CommandHandler<C, GF> = (context) => void;
```

Defined in: [packages/core/src/types/command.ts:62](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L62)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`context`

[`CommandHandlerContext`](TypeAlias.CommandHandlerContext.md)<`C`, `GF`>

## Returns

`void`

---

---

url: /reference/api/core/TypeAlias.CommandHandler.md
---

# Type Alias: CommandHandler()\<C, GF>

```ts twoslash
// @include: imports
type CommandHandler<C, GF> = (context) => void;
```

Defined in: [packages/core/src/types/command.ts:62](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L62)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

## Parameters

`context`

[`CommandHandlerContext`](TypeAlias.CommandHandlerContext.md)<`C`, `GF`>

## Returns

`void`

---

---

url: /reference/api/clerc/TypeAlias.CommandHandlerContext.md
---

# Type Alias: CommandHandlerContext\<C, GF>

```ts twoslash
// @include: imports
type CommandHandlerContext<C, GF> = DeepPrettify<
  PartialRequired<BaseContext<C, GF>, "command" | "calledAs"> & object
>;
```

Defined in: [packages/core/src/types/command.ts:54](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L54)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/core/TypeAlias.CommandHandlerContext.md
---

# Type Alias: CommandHandlerContext\<C, GF>

```ts twoslash
// @include: imports
type CommandHandlerContext<C, GF> = DeepPrettify<
  PartialRequired<BaseContext<C, GF>, "command" | "calledAs"> & object
>;
```

Defined in: [packages/core/src/types/command.ts:54](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L54)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/clerc/TypeAlias.CommandsMap.md
---

# Type Alias: CommandsMap

```ts twoslash
// @include: imports
type CommandsMap = Map<string, Command>;
```

Defined in: [packages/core/src/types/command.ts:46](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L46)

---

---

url: /reference/api/core/TypeAlias.CommandsMap.md
---

# Type Alias: CommandsMap

```ts twoslash
// @include: imports
type CommandsMap = Map<string, Command>;
```

Defined in: [packages/core/src/types/command.ts:46](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L46)

---

---

url: /reference/api/clerc/TypeAlias.CommandsRecord.md
---

# Type Alias: CommandsRecord

```ts twoslash
// @include: imports
type CommandsRecord = Record<string, Command>;
```

Defined in: [packages/core/src/types/command.ts:45](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L45)

---

---

url: /reference/api/core/TypeAlias.CommandsRecord.md
---

# Type Alias: CommandsRecord

```ts twoslash
// @include: imports
type CommandsRecord = Record<string, Command>;
```

Defined in: [packages/core/src/types/command.ts:45](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L45)

---

---

url: /reference/api/clerc/TypeAlias.CommandWithHandler.md
---

# Type Alias: CommandWithHandler\<Name, Parameters, Flags>

```ts twoslash
// @include: imports
type CommandWithHandler<Name, Parameters, Flags> = Command<
  Name,
  Parameters,
  Flags
> &
  object;
```

Defined in: [packages/core/src/types/command.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L36)

## Type Declaration

`handler?`

[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>

[packages/core/src/types/command.ts:42](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L42)

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/core/TypeAlias.CommandWithHandler.md
---

# Type Alias: CommandWithHandler\<Name, Parameters, Flags>

```ts twoslash
// @include: imports
type CommandWithHandler<Name, Parameters, Flags> = Command<
  Name,
  Parameters,
  Flags
> &
  object;
```

Defined in: [packages/core/src/types/command.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L36)

## Type Declaration

`handler?`

[`CommandHandler`](TypeAlias.CommandHandler.md)<[`Command`](Interface.Command.md)<`Name`, `Parameters`, `Flags`>>

[packages/core/src/types/command.ts:42](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L42)

## Type Parameters

`Name` *extends* `string`

`string`

`Parameters` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

`Flags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/utils/TypeAlias.DeepPrettify.md
---

# Type Alias: DeepPrettify\<T, E>

```ts twoslash
// @include: imports
type DeepPrettify<T, E> = ConditionalDeepPrettify<
  T,
  E | NonRecursiveType | MapsSetsOrArrays,
  object
>;
```

Defined in: [types/type-fest.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L32)

## Type Parameters

`T`

‐

`E`

`never`

---

---

url: /reference/api/clerc/TypeAlias.ErrorHandler.md
---

# Type Alias: ErrorHandler()

```ts twoslash
// @include: imports
type ErrorHandler = (error) => void;
```

Defined in: [packages/core/src/types/clerc.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/clerc.ts#L1)

## Parameters

`error`

`unknown`

## Returns

`void`

---

---

url: /reference/api/core/TypeAlias.ErrorHandler.md
---

# Type Alias: ErrorHandler()

```ts twoslash
// @include: imports
type ErrorHandler = (error) => void;
```

Defined in: [packages/core/src/types/clerc.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/clerc.ts#L1)

## Parameters

`error`

`unknown`

## Returns

`void`

---

---

url: /reference/api/clerc/Parser.TypeAlias.FlagDefaultValue.md
---

# Type Alias: FlagDefaultValue\<T>

```ts twoslash
// @include: imports
type FlagDefaultValue<T> = T | FlagDefaultValueFunction<T>;
```

Defined in: [packages/parser/src/types.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L10)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/core/Parser.TypeAlias.FlagDefaultValue.md
---

# Type Alias: FlagDefaultValue\<T>

```ts twoslash
// @include: imports
type FlagDefaultValue<T> = T | FlagDefaultValueFunction<T>;
```

Defined in: [packages/parser/src/types.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L10)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/parser/TypeAlias.FlagDefaultValue.md
---

# Type Alias: FlagDefaultValue\<T>

```ts twoslash
// @include: imports
type FlagDefaultValue<T> = T | FlagDefaultValueFunction<T>;
```

Defined in: [packages/parser/src/types.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L10)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/clerc/Parser.TypeAlias.FlagDefinitionValue.md
---

# Type Alias: FlagDefinitionValue

```ts twoslash
// @include: imports
type FlagDefinitionValue = FlagOptions | TypeValue;
```

Defined in: [packages/parser/src/types.ts:86](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L86)

---

---

url: /reference/api/core/Parser.TypeAlias.FlagDefinitionValue.md
---

# Type Alias: FlagDefinitionValue

```ts twoslash
// @include: imports
type FlagDefinitionValue = FlagOptions | TypeValue;
```

Defined in: [packages/parser/src/types.ts:86](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L86)

---

---

url: /reference/api/parser/TypeAlias.FlagDefinitionValue.md
---

# Type Alias: FlagDefinitionValue

```ts twoslash
// @include: imports
type FlagDefinitionValue = FlagOptions | TypeValue;
```

Defined in: [packages/parser/src/types.ts:86](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L86)

---

---

url: /reference/api/clerc/Parser.TypeAlias.FlagOptions.md
---

# Type Alias: FlagOptions

```ts twoslash
// @include: imports
type FlagOptions =
  | (BaseFlagOptions<BooleanConstructor> & object)
  | (BaseFlagOptions & object);
```

Defined in: [packages/parser/src/types.ts:72](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L72)

---

---

url: /reference/api/core/Parser.TypeAlias.FlagOptions.md
---

# Type Alias: FlagOptions

```ts twoslash
// @include: imports
type FlagOptions =
  | (BaseFlagOptions<BooleanConstructor> & object)
  | (BaseFlagOptions & object);
```

Defined in: [packages/parser/src/types.ts:72](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L72)

---

---

url: /reference/api/parser/TypeAlias.FlagOptions.md
---

# Type Alias: FlagOptions

```ts twoslash
// @include: imports
type FlagOptions =
  | (BaseFlagOptions<BooleanConstructor> & object)
  | (BaseFlagOptions & object);
```

Defined in: [packages/parser/src/types.ts:72](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L72)

---

---

url: /reference/api/clerc/Parser.TypeAlias.FlagsDefinition.md
---

# Type Alias: FlagsDefinition

```ts twoslash
// @include: imports
type FlagsDefinition = Record<string, FlagDefinitionValue>;
```

Defined in: [packages/parser/src/types.ts:87](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L87)

---

---

url: /reference/api/core/Parser.TypeAlias.FlagsDefinition.md
---

# Type Alias: FlagsDefinition

```ts twoslash
// @include: imports
type FlagsDefinition = Record<string, FlagDefinitionValue>;
```

Defined in: [packages/parser/src/types.ts:87](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L87)

---

---

url: /reference/api/parser/TypeAlias.FlagsDefinition.md
---

# Type Alias: FlagsDefinition

```ts twoslash
// @include: imports
type FlagsDefinition = Record<string, FlagDefinitionValue>;
```

Defined in: [packages/parser/src/types.ts:87](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L87)

---

---

url: /reference/api/clerc/TypeAlias.GroupDefinition.md
---

# Type Alias: GroupDefinition

```ts twoslash
// @include: imports
type GroupDefinition = [string, string];
```

Defined in: [packages/plugin-help/src/types.ts:13](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L13)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.

---

---

url: /reference/api/plugin-help/TypeAlias.GroupDefinition.md
---

# Type Alias: GroupDefinition

```ts twoslash
// @include: imports
type GroupDefinition = [string, string];
```

Defined in: [types.ts:13](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/types.ts#L13)

A group definition as a tuple of \[key, displayName]. The key is used in help
options to assign items to groups. The displayName is shown in the help
output.

---

---

url: /reference/api/clerc/Parser.TypeAlias.IgnoreFunction.md
---

# Type Alias: IgnoreFunction()

```ts twoslash
// @include: imports
type IgnoreFunction = (type, arg) => boolean;
```

Defined in: [packages/parser/src/types.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L35)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

## Parameters

`type`

| *typeof* [`KNOWN_FLAG`](Variable.KNOWN_FLAG.md) | *typeof* [`UNKNOWN_FLAG`](Variable.UNKNOWN_FLAG.md) | *typeof* [`PARAMETER`](Variable.PARAMETER.md)

The type of the current argument: 'known-flag' or
'unknown-flag' for flags, 'parameter' for positional arguments

`arg`

`string`

The current argument being processed

## Returns

`boolean`

True to stop parsing, false to continue

---

---

url: /reference/api/core/Parser.TypeAlias.IgnoreFunction.md
---

# Type Alias: IgnoreFunction()

```ts twoslash
// @include: imports
type IgnoreFunction = (type, arg) => boolean;
```

Defined in: [packages/parser/src/types.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L35)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

## Parameters

`type`

| *typeof* [`KNOWN_FLAG`](Variable.KNOWN_FLAG.md) | *typeof* [`UNKNOWN_FLAG`](Variable.UNKNOWN_FLAG.md) | *typeof* [`PARAMETER`](Variable.PARAMETER.md)

The type of the current argument: 'known-flag' or
'unknown-flag' for flags, 'parameter' for positional arguments

`arg`

`string`

The current argument being processed

## Returns

`boolean`

True to stop parsing, false to continue

---

---

url: /reference/api/parser/TypeAlias.IgnoreFunction.md
---

# Type Alias: IgnoreFunction()

```ts twoslash
// @include: imports
type IgnoreFunction = (type, arg) => boolean;
```

Defined in: [packages/parser/src/types.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L35)

A callback function to conditionally stop parsing. When it returns true,
parsing stops and remaining arguments are preserved in `ignored`.

## Parameters

`type`

| *typeof* [`KNOWN_FLAG`](Variable.KNOWN_FLAG.md) | *typeof* [`UNKNOWN_FLAG`](Variable.UNKNOWN_FLAG.md) | *typeof* [`PARAMETER`](Variable.PARAMETER.md)

The type of the current argument: 'known-flag' or
'unknown-flag' for flags, 'parameter' for positional arguments

`arg`

`string`

The current argument being processed

## Returns

`boolean`

True to stop parsing, false to continue

---

---

url: /reference/api/clerc/Parser.TypeAlias.InferFlags.md
---

# Type Alias: InferFlags\<T>

```ts twoslash
// @include: imports
type InferFlags<T> = Prettify<_InferFlags<T>>;
```

Defined in: [packages/parser/src/types.ts:208](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L208)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

The type of the flags configuration object.

---

---

url: /reference/api/core/Parser.TypeAlias.InferFlags.md
---

# Type Alias: InferFlags\<T>

```ts twoslash
// @include: imports
type InferFlags<T> = Prettify<_InferFlags<T>>;
```

Defined in: [packages/parser/src/types.ts:208](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L208)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

## Type Parameters

`T` *extends* [`FlagsDefinition`](Parser.TypeAlias.FlagsDefinition.md)

The type of the flags configuration object.

---

---

url: /reference/api/parser/TypeAlias.InferFlags.md
---

# Type Alias: InferFlags\<T>

```ts twoslash
// @include: imports
type InferFlags<T> = Prettify<_InferFlags<T>>;
```

Defined in: [packages/parser/src/types.ts:208](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L208)

An advanced utility type that infers the exact type of the `flags` object in
the parsed result, based on the provided `flags` configuration object T.

## Type Parameters

`T` *extends* [`FlagsDefinition`](TypeAlias.FlagsDefinition.md)

The type of the flags configuration object.

---

---

url: /reference/api/clerc/TypeAlias.InferParameters.md
---

# Type Alias: InferParameters\<T>

```ts twoslash
// @include: imports
type InferParameters<T> = T extends readonly infer U[] ? Prettify<UnionToIntersection<InferParameter<U>>> : never;
```

Defined in: [packages/core/src/types/parameter.ts:24](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L24)

## Type Parameters

`T` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

---

---

url: /reference/api/core/TypeAlias.InferParameters.md
---

# Type Alias: InferParameters\<T>

```ts twoslash
// @include: imports
type InferParameters<T> = T extends readonly infer U[] ? Prettify<UnionToIntersection<InferParameter<U>>> : never;
```

Defined in: [packages/core/src/types/parameter.ts:24](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L24)

## Type Parameters

`T` *extends* readonly [`ParameterDefinitionValue`](TypeAlias.ParameterDefinitionValue.md)\[]

---

---

url: /reference/api/clerc/TypeAlias.Interceptor.md
---

# Type Alias: Interceptor\<C, GF>

```ts twoslash
// @include: imports
type Interceptor<C, GF> = InterceptorHandler<C, GF> | InterceptorObject<C, GF>;
```

Defined in: [packages/core/src/types/interceptor.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L36)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

---

---

url: /reference/api/core/TypeAlias.Interceptor.md
---

# Type Alias: Interceptor\<C, GF>

```ts twoslash
// @include: imports
type Interceptor<C, GF> = InterceptorHandler<C, GF> | InterceptorObject<C, GF>;
```

Defined in: [packages/core/src/types/interceptor.ts:36](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L36)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

---

---

url: /reference/api/clerc/TypeAlias.InterceptorContext.md
---

# Type Alias: InterceptorContext\<C, GF>

```ts twoslash
// @include: imports
type InterceptorContext<C, GF> = DeepPrettify<BaseContext<C, GF>>;
```

Defined in: [packages/core/src/types/interceptor.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L7)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

---

---

url: /reference/api/core/TypeAlias.InterceptorContext.md
---

# Type Alias: InterceptorContext\<C, GF>

```ts twoslash
// @include: imports
type InterceptorContext<C, GF> = DeepPrettify<BaseContext<C, GF>>;
```

Defined in: [packages/core/src/types/interceptor.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L7)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

---

---

url: /reference/api/clerc/TypeAlias.InterceptorHandler.md
---

# Type Alias: InterceptorHandler()\<C, GF>

```ts twoslash
// @include: imports
type InterceptorHandler<C, GF> = (context, next) => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L17)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Parameters

`context`

[`InterceptorContext`](TypeAlias.InterceptorContext.md)<`C`, `GF`>

`next`

[`InterceptorNext`](TypeAlias.InterceptorNext.md)

## Returns

`void` | `Promise`<`void`>

---

---

url: /reference/api/core/TypeAlias.InterceptorHandler.md
---

# Type Alias: InterceptorHandler()\<C, GF>

```ts twoslash
// @include: imports
type InterceptorHandler<C, GF> = (context, next) => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:17](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L17)

## Type Parameters

`C` *extends* [`Command`](Interface.Command.md)

[`Command`](Interface.Command.md)

`GF` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

`object`

## Parameters

`context`

[`InterceptorContext`](TypeAlias.InterceptorContext.md)<`C`, `GF`>

`next`

[`InterceptorNext`](TypeAlias.InterceptorNext.md)

## Returns

`void` | `Promise`<`void`>

---

---

url: /reference/api/clerc/TypeAlias.InterceptorNext.md
---

# Type Alias: InterceptorNext()

```ts twoslash
// @include: imports
type InterceptorNext = () => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L15)

Function to call the next interceptor in the chain. **MUST** be awaited.

## Returns

`void` | `Promise`<`void`>

---

---

url: /reference/api/core/TypeAlias.InterceptorNext.md
---

# Type Alias: InterceptorNext()

```ts twoslash
// @include: imports
type InterceptorNext = () => void | Promise<void>;
```

Defined in: [packages/core/src/types/interceptor.ts:15](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/interceptor.ts#L15)

Function to call the next interceptor in the chain. **MUST** be awaited.

## Returns

`void` | `Promise`<`void`>

---

---

url: /reference/api/utils/TypeAlias.IsAny.md
---

# Type Alias: IsAny\<T>

```ts twoslash
// @include: imports
type IsAny<T> = 0 extends 1 & T ? true : false;
```

Defined in: [types/type-fest.ts:38](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L38)

## Type Parameters

`T`

---

---

url: /reference/api/utils/TypeAlias.LiteralUnion.md
---

# Type Alias: LiteralUnion\<LiteralType, BaseType>

```ts twoslash
// @include: imports
type LiteralUnion<LiteralType, BaseType> =
  | LiteralType
  | (BaseType & Record<never, never>);
```

Defined in: [types/type-fest.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L3)

## Type Parameters

`LiteralType`

`BaseType`

---

---

url: /reference/api/clerc/TypeAlias.MakeEmitterEvents.md
---

# Type Alias: MakeEmitterEvents\<Commands, GlobalFlags>

```ts twoslash
// @include: imports
type MakeEmitterEvents<Commands, GlobalFlags> = {
  [K in keyof Commands]: [CommandHandlerContext<Commands[K], GlobalFlags>];
};
```

Defined in: [packages/core/src/types/command.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L47)

## Type Parameters

`Commands` *extends* [`CommandsRecord`](TypeAlias.CommandsRecord.md)

‐

`GlobalFlags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/core/TypeAlias.MakeEmitterEvents.md
---

# Type Alias: MakeEmitterEvents\<Commands, GlobalFlags>

```ts twoslash
// @include: imports
type MakeEmitterEvents<Commands, GlobalFlags> = {
  [K in keyof Commands]: [CommandHandlerContext<Commands[K], GlobalFlags>];
};
```

Defined in: [packages/core/src/types/command.ts:47](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/command.ts#L47)

## Type Parameters

`Commands` *extends* [`CommandsRecord`](TypeAlias.CommandsRecord.md)

‐

`GlobalFlags` *extends* [`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

[`ClercFlagsDefinition`](TypeAlias.ClercFlagsDefinition.md)

---

---

url: /reference/api/utils/TypeAlias.MaybeArray.md
---

# Type Alias: MaybeArray\<T>

```ts twoslash
// @include: imports
type MaybeArray<T> = T | T[];
```

Defined in: [types/index.ts:2](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L2)

## Type Parameters

`T`

---

---

url: /reference/api/utils/TypeAlias.MaybeAsyncGetter.md
---

# Type Alias: MaybeAsyncGetter\<T>

```ts twoslash
// @include: imports
type MaybeAsyncGetter<T> = T | () => T | Promise<T>;
```

Defined in: [types/index.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L4)

## Type Parameters

`T`

---

---

url: /reference/api/utils/TypeAlias.MaybeGetter.md
---

# Type Alias: MaybeGetter\<T>

```ts twoslash
// @include: imports
type MaybeGetter<T> = T | () => T;
```

Defined in: [types/index.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L3)

## Type Parameters

`T`

---

---

url: /reference/api/clerc/TypeAlias.ParameterDefinitionValue.md
---

# Type Alias: ParameterDefinitionValue

```ts twoslash
// @include: imports
type ParameterDefinitionValue = string | ParameterOptions;
```

Defined in: [packages/core/src/types/parameter.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L35)

---

---

url: /reference/api/core/TypeAlias.ParameterDefinitionValue.md
---

# Type Alias: ParameterDefinitionValue

```ts twoslash
// @include: imports
type ParameterDefinitionValue = string | ParameterOptions;
```

Defined in: [packages/core/src/types/parameter.ts:35](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L35)

---

---

url: /reference/api/clerc/TypeAlias.ParameterOptions.md
---

# Type Alias: ParameterOptions

```ts twoslash
// @include: imports
type ParameterOptions = object & ParameterCustomOptions;
```

Defined in: [packages/core/src/types/parameter.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L30)

## Type Declaration

`description?`

`string`

[packages/core/src/types/parameter.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L32)

`key`

`string`

[packages/core/src/types/parameter.ts:31](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L31)

`type?`

[`TypeFunction`](Parser.Interface.TypeFunction.md)

[packages/core/src/types/parameter.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L33)

---

---

url: /reference/api/core/TypeAlias.ParameterOptions.md
---

# Type Alias: ParameterOptions

```ts twoslash
// @include: imports
type ParameterOptions = object & ParameterCustomOptions;
```

Defined in: [packages/core/src/types/parameter.ts:30](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L30)

## Type Declaration

`description?`

`string`

[packages/core/src/types/parameter.ts:32](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L32)

`key`

`string`

[packages/core/src/types/parameter.ts:31](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L31)

`type?`

[`TypeFunction`](Parser.Interface.TypeFunction.md)

[packages/core/src/types/parameter.ts:33](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/core/src/types/parameter.ts#L33)

---

---

url: /reference/api/utils/TypeAlias.PartialRequired.md
---

# Type Alias: PartialRequired\<T, K>

```ts twoslash
// @include: imports
type PartialRequired<T, K> = T & { [P in K]-?: T[P] };
```

Defined in: [types/index.ts:6](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L6)

## Type Parameters

`T`

`K` *extends* keyof `T`

---

---

url: /reference/api/utils/TypeAlias.Prettify.md
---

# Type Alias: Prettify\<T>

```ts twoslash
// @include: imports
type Prettify<T> = { [K in keyof T]: T[K] } & object;
```

Defined in: [types/type-fest.ts:7](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L7)

## Type Parameters

`T`

---

---

url: /reference/api/clerc/Parser.TypeAlias.RawInputType.md
---

# Type Alias: RawInputType

```ts twoslash
// @include: imports
type RawInputType = string | boolean;
```

Defined in: [packages/parser/src/types.ts:114](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L114)

---

---

url: /reference/api/core/Parser.TypeAlias.RawInputType.md
---

# Type Alias: RawInputType

```ts twoslash
// @include: imports
type RawInputType = string | boolean;
```

Defined in: [packages/parser/src/types.ts:114](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L114)

---

---

url: /reference/api/parser/TypeAlias.RawInputType.md
---

# Type Alias: RawInputType

```ts twoslash
// @include: imports
type RawInputType = string | boolean;
```

Defined in: [packages/parser/src/types.ts:114](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L114)

---

---

url: /reference/api/utils/TypeAlias.RequireExactlyOne.md
---

# Type Alias: RequireExactlyOne\<T, Keys>

```ts twoslash
// @include: imports
type RequireExactlyOne<T, Keys> = {
  [K in Keys]-?: Required<Pick<T, K>> &
    Partial<Record<Exclude<Keys, K>, never>>;
}[Keys] &
  Omit<T, Keys>;
```

Defined in: [types/type-fest.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L40)

## Type Parameters

`T`

‐

`Keys` *extends* keyof `T`

keyof `T`

---

---

url: /reference/api/utils/TypeAlias.RequireExactlyOneOrNone.md
---

# Type Alias: RequireExactlyOneOrNone\<T, Keys>

```ts twoslash
// @include: imports
type RequireExactlyOneOrNone<T, Keys> =
  | ({
      [K in Keys]-?: Required<Pick<T, K>> &
        Partial<Record<Exclude<Keys, K>, never>>;
    }[Keys] &
      Omit<T, Keys>)
  | (Partial<Record<Keys, never>> & Omit<T, Keys>);
```

Defined in: [types/type-fest.ts:46](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/type-fest.ts#L46)

## Type Parameters

`T`

‐

`Keys` *extends* keyof `T`

keyof `T`

---

---

url: /reference/api/utils/TypeAlias.ToArray.md
---

# Type Alias: ToArray\<T>

```ts twoslash
// @include: imports
type ToArray<T> = T extends any[] ? T : [T];
```

Defined in: [types/index.ts:1](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L1)

## Type Parameters

`T`

---

---

url: /reference/api/clerc/Parser.TypeAlias.TypeValue.md
---

# Type Alias: TypeValue\<T>

```ts twoslash
// @include: imports
type TypeValue<T> = TypeFunction<T> | readonly [TypeFunction<T>];
```

Defined in: [packages/parser/src/types.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L40)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/core/Parser.TypeAlias.TypeValue.md
---

# Type Alias: TypeValue\<T>

```ts twoslash
// @include: imports
type TypeValue<T> = TypeFunction<T> | readonly [TypeFunction<T>];
```

Defined in: [packages/parser/src/types.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L40)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/parser/TypeAlias.TypeValue.md
---

# Type Alias: TypeValue\<T>

```ts twoslash
// @include: imports
type TypeValue<T> = TypeFunction<T> | readonly [TypeFunction<T>];
```

Defined in: [packages/parser/src/types.ts:40](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/types.ts#L40)

## Type Parameters

`T`

`unknown`

---

---

url: /reference/api/utils/TypeAlias.UnionToIntersection.md
---

# Type Alias: UnionToIntersection\<U>

```ts twoslash
// @include: imports
type UnionToIntersection<U> = U extends any
  ? (k) => void
  : never extends (k) => void
    ? I
    : never;
```

Defined in: [types/index.ts:10](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/types/index.ts#L10)

## Type Parameters

`U`

---

---

url: /guide/types.md
---

# Types

Types allow you to validate, convert, and parse values for both flags and parameters. Clerc provides several built-in type functions and supports custom types.

## Built-in Basic Types

Clerc supports the standard JavaScript type constructors for common use cases:

* **String**: For string values (default value: `undefined`)
* **Number**: For numeric values (can be used directly)
* **Boolean**: For boolean switches (default value: `false`)
* **Object**: For key-value pairs (default value: `{}`)

### String Type

The `String` type is used for flags and parameters that accept string values. This is the most basic type.

**Default value behavior:** If not specified, its value is `undefined` (unless a `default` property is set).

```ts twoslash
// @include: imports
const cli = Cli()
  .command("greet", "Greet someone", {
    flags: {
      name: {
        type: String,
        description: "User name",
        default: "World",
      },

      message: {
        type: String,
        short: "m",
        description: "Greeting message",
      },
    },
  })
  .on("greet", (ctx) => {
    console.log(`${ctx.flags.message}, ${ctx.flags.name}!`);
    // $ node cli.mjs greet --name John --message Hello
    // Hello, John!
    // $ node cli.mjs greet --message Hello
    // ctx.flags.message => "Hello"
    // ctx.flags.name => "World" (uses default value)
  })
  .parse();
```

### Boolean Type

The `Boolean` type is used for creating boolean switch flags. By default, simply mentioning the flag name sets it to `true`.

**Default value behavior:** If the flag is not specified, its value is `false`.

```ts twoslash
// @include: imports
const cli = Cli()
  .command("build", "Build the project", {
    flags: {
      production: {
        type: Boolean,
        description: "Build for production",
      },

      watch: {
        type: Boolean,
        short: "w",
        description: "Enable watch mode",
      },
    },
  })
  .on("build", (ctx) => {
    // $ node cli.mjs build --production --watch
    ctx.flags.production; // => true
    ctx.flags.watch; // => true

    // $ node cli.mjs build
    ctx.flags.production; // => false
    ctx.flags.watch; // => false
  })
  .parse();
```

#### Boolean's Negatable Property

The Boolean type supports a `negatable` property that allows you to decide whether to enable negated flags. By default, `negatable` is `true`, which means `--no-flag` will set the `flag` flag to `false`.

```ts twoslash
// @include: imports
const cli = Cli()
  .command("start", "Start the application", {
    flags: {
      color: {
        type: Boolean,
        negatable: true, // default
        description: "Enable color output",
        default: true,
      },

      cache: {
        type: Boolean,
        negatable: false, // disable negation form
        description: "Enable caching",
        default: true,
      },
    },
  })
  .on("start", (ctx) => {
    // $ node cli.mjs start
    ctx.flags.color; // => true
    ctx.flags.cache; // => true

    // $ node cli.mjs start --no-color --no-cache
    ctx.flags.color; // => false
    ctx.flags.cache; // => true

    // You must use --cache=false to disable caching
    // $ node cli.mjs start --cache=false
    ctx.flags.cache; // => false
  })
  .parse();
```

### Array Type

The `Array` type is used for flags and parameters that accept multiple values. Define it by wrapping the type function in an array:

**Default value behavior:** If not specified, its value is `[]` (empty array).

```ts twoslash
// @include: imports
const cli = Cli()
  .command("copy", "Copy files", {
    flags: {
      // Use [String] to accept multiple string values
      include: {
        type: [String],
        short: "i",
        description: "File patterns to include",
      },

      // Use [Number] to accept multiple numeric values
      ports: {
        type: [Number],
        short: "p",
        description: "Ports to listen on",
      },
    },
  })
  .on("copy", (ctx) => {
    // $ node cli.mjs copy -i "*.js" -i "*.ts" -p 3000 -p 3001
    ctx.flags.include; // => ["*.js", "*.ts"]
    ctx.flags.ports; // => [3000, 3001]

    // $ node cli.mjs copy
    ctx.flags.include; // => []
    ctx.flags.ports; // => []
  })
  .parse();
```

### Counter Type

The counter type is used to count how many times a flag is specified. This can be implemented by using the `[Boolean]` type:

**Default value behavior:** If not specified, its value is `0`.

```ts twoslash
// @include: imports
const cli = Cli()
  .command("log", "Display logs", {
    flags: {
      // [Boolean] type counts how many times the flag is used
      verbose: {
        type: [Boolean],
        short: "v",
        description: "Verbosity level (-v, -vv, -vvv)",
      },
    },
  })
  .on("log", (ctx) => {
    // $ node cli.mjs log -v
    ctx.flags.verbose; // => 1

    // $ node cli.mjs log -vvv
    ctx.flags.verbose; // => 3

    // $ node cli.mjs log -v -v -v
    ctx.flags.verbose; // => 3

    // $ node cli.mjs log
    ctx.flags.verbose; // => 0
  })
  .parse();
```

### Object Type

The `Object` type is used for flags that accept key-value pairs. Use dots or other delimiters to specify object properties:

**Default value behavior:** If not specified, its value is `{}` (empty object).

```ts twoslash
// @include: imports
const cli = Cli()
  .command("config", "Configure the application", {
    flags: {
      define: {
        type: Object,
        short: "d",
        description: "Define environment variables",
      },
    },
  })
  .on("config", (ctx) => {
    // $ node cli.mjs config --define.apiUrl http://api.example.com --define.debug
    ctx.flags.define; // => { apiUrl: "http://api.example.com", debug: true }

    // $ node cli.mjs config
    ctx.flags.define; // => {}
  })
  .parse();
```

:::info

If you want to pass key-value pairs like `K=V`, you can use the colon delimiter in the command line:

```bash
node cli.mjs config --define:env=production --define:version=1.0.0
```

Actually, `--define=env=production` also works fine, it's just not as intuitive.

:::

#### Advanced Object Type with `objectType()`

For more control over object flag parsing, type conversion, and default value merging, you can use the `objectType()` function from `@clerc/parser`:

```ts twoslash
// @include: imports
import { coerceObjectValue, objectType, setDotValues } from "@clerc/parser";

// or import { objectType, setDotValues, coerceObjectValue } from "clerc";

const cli = Cli()
  .command("dev", "Start development server", {
    flags: {
      env: {
        type: objectType<{ PORT?: number; DEBUG?: boolean; HOST?: string }>({
          setValue: (object, path, value) => {
            // Custom type conversion based on field name
            if (path === "PORT") {
              setDotValues(object, path, Number(value));
            } else if (path === "DEBUG") {
              setDotValues(object, path, value === "true");
            } else {
              // For other fields, use default coercion
              setDotValues(object, path, coerceObjectValue(value));
            }
          },
        }),
        default: { PORT: 3000, HOST: "0.0.0.0" }, // Default values
      },
    },
  })
  .on("dev", (ctx) => {
    // $ node cli.mjs dev --env.PORT 8080 --env.DEBUG true
    ctx.flags.env.PORT; // => 8080 (number)
    ctx.flags.env.DEBUG; // => true (boolean)
    ctx.flags.env.HOST; // => "0.0.0.0" (merged from default)
  })
  .parse();
```

**Key features:**

1. **Type-safe generic support**: Specify the expected object structure with `objectType<T>()`
2. **Custom value transformation**: The `setValue` function receives:
   * `object`: The current object being built
   * `path`: The dot-separated path (e.g., `"PORT"` or `"foo.bar"`)
   * `value`: The raw CLI string value
3. **Automatic default merging**: When you provide a `default` value in the flag config, it automatically merges with user-provided values (shallow merge by default)
4. **Helper functions**: Use `setDotValues`, `appendDotValues`, and `coerceObjectValue` for common operations

**Default behavior (without custom `setValue`):**

```ts twoslash
// @include: imports
import { objectType } from "@clerc/parser";

// or import { objectType } from "clerc";

const cli = Cli()
  .command("config", "Configure settings", {
    flags: {
      settings: {
        type: objectType(), // Uses default behavior
        default: { theme: "dark", language: "en" },
      },
    },
  })
  .on("config", (ctx) => {
    // $ node cli.mjs config --settings.name app --settings.version 1.0.0
    ctx.flags.settings; // => { name: "app", version: "1.0.0", theme: "dark", language: "en" }

    // $ node cli.mjs config --settings.tags a --settings.tags b
    ctx.flags.settings; // => { tags: ["a", "b"], theme: "dark", language: "en" }
    // Duplicate keys become arrays, default values are merged
  })
  .parse();
```

The default behavior automatically:

* Converts `"true"` or empty values to boolean `true`
* Converts `"false"` to boolean `false`
* Handles duplicate keys by creating arrays
* **Merges external `default` values** with user-provided values (shallow merge)

**Custom merge logic:**

By default, `objectType` performs a shallow merge when combining default values with user-provided values. You can customize this behavior with the `mergeObject` option:

```ts twoslash
// @include: imports
import { objectType } from "@clerc/parser";

const cli = Cli()
  .command("start", "Start the server", {
    flags: {
      config: {
        type: objectType({
          mergeObject: (target, defaults) => {
            // Custom merge logic: deep merge nested objects
            for (const [key, val] of Object.entries(defaults)) {
              if (
                typeof val === "object" &&
                val !== null &&
                typeof target[key] === "object"
              ) {
                // Deep merge nested objects
                Object.assign(target[key], val, target[key]);
              } else if (!(key in target)) {
                // Add missing keys from defaults
                target[key] = val;
              }
            }
          },
        }),
        default: { db: { host: "localhost", port: 5432 }, cache: { ttl: 300 } },
      },
    },
  })
  .on("start", (ctx) => {
    // $ node cli.mjs start --config.db.host example.com
    ctx.flags.config;
    // => { db: { host: "example.com", port: 5432 }, cache: { ttl: 300 } }
    // Deep merge preserves db.port from default
  })
  .parse();
```

**Utility functions:**

* `setDotValues(object, path, value)`: Sets a value at a nested path (overwrites existing values)
* `appendDotValues(object, path, value)`: Sets a value at a nested path (converts duplicates to arrays)
* `coerceObjectValue(value)`: Default boolean coercion (`"true"` → `true`, `"false"` → `false`)

:::tip

The `objectType()` function provides a more powerful and type-safe alternative to the basic `Object` type, especially when you need:

* Custom type conversions per field
* Better TypeScript type inference
* Integration with schema validation libraries

:::

## Built-in Advanced Types

Clerc provides some built-in advanced type functions to facilitate common needs:

* `Enum`: Restrict flag and parameter values to a predefined set.
* `Range`: Restrict numeric values to a specific range and convert to numbers.
* `Regex`: Validate values against a regular expression pattern.

These type functions can be used for both flags and parameters, allowing you to share the same type definitions across your CLI:

```ts twoslash
// @include: imports
import { Types } from "clerc";

Cli()
  .command("serve", "Start the server", {
    flags: {
      mode: {
        type: Types.Enum("development", "production", "test"),
        default: "development" as const,
        description: "Set the application mode",
      },
    },
    parameters: [
      {
        key: "[port]",
        type: Types.Range(1024, 65_535),
        description: "Port number",
      },
    ],
  })
  .on("serve", (ctx) => {
    ctx.flags.mode;
    //        ^?
    ctx.parameters.port;
    //             ^?
  })
  .parse();
```

### Enum Type

Restrict flag or parameter values to a predefined set of options:

```ts twoslash
// @include: imports
import { Types } from "clerc";

const cli = Cli()
  .scriptName("build-cli")
  .description("Build tool")
  .version("1.0.0")
  .command("config", "Configure build settings", {
    flags: {
      format: {
        type: Types.Enum("json", "yaml", "toml"),
        description: "Output format",
      },
    },
    parameters: [
      {
        key: "<setting>",
        type: Types.Enum("output", "target", "format"),
        description: "Setting name",
      },
      {
        key: "<value>",
        description: "Setting value",
      },
    ],
  })
  .on("config", (ctx) => {
    console.log(`Setting ${ctx.parameters.setting} = ${ctx.parameters.value}`);
  })
  .parse();
```

Usage:

```bash
$ build-cli config --format json output dist
$ build-cli config --format yaml target es2020
$ build-cli config --format invalid value
# Error: Invalid value: invalid. Must be one of: json, yaml, toml
```

### Range Type

Restrict numeric values to a specific range and convert to numbers:

```ts twoslash
// @include: imports
import { Types } from "clerc";

const cli = Cli()
  .scriptName("server-cli")
  .description("Server management tool")
  .version("1.0.0")
  .command("start", "Start the server", {
    flags: {
      port: {
        type: Types.Range(1024, 65_535),
        description: "Port number",
      },
    },
    parameters: [
      {
        key: "[timeout]",
        type: Types.Range(1, 3600),
        description: "Timeout in seconds",
      },
    ],
  })
  .on("start", (ctx) => {
    const port = ctx.flags.port ?? 3000;
    console.log(`Starting server on port ${port}`);
  })
  .parse();
```

Usage:

```bash
$ server-cli start --port 3000
$ server-cli start --port 8080
$ server-cli start --port 100
# Error: Invalid value: 100. Must be a number between 1024 and 65535
```

### Regex Type

Validate values against a regular expression pattern:

```ts twoslash
// @include: imports
import { Types } from "clerc";

const cli = Cli()
  .scriptName("git-clone")
  .description("Clone repository")
  .version("1.0.0")
  .command("clone", "Clone a repository", {
    parameters: [
      {
        key: "<repo>",
        type: Types.Regex(/^[\w\-.]+\/[\w\-.]+$/, "owner/repo format"),
        description: "Repository in owner/repo format",
      },
    ],
  })
  .on("clone", (ctx) => {
    console.log(`Cloning ${ctx.parameters.repo}`);
  })
  .parse();
```

Usage:

```bash
$ git-clone clone clercjs/clerc
$ git-clone clone myorg/myrepo
$ git-clone clone invalid
# Error: Invalid value: invalid. Must match: owner/repo format
```

## Custom Types

You can create custom type functions by providing a function that accepts a string argument and returns the parsed value.

### Type Display Property

Custom type functions can include an optional `display` property that provides a user-friendly name for the type in help output. This is especially useful for complex types where the function name doesn't clearly describe what the type accepts.

```ts twoslash
// @include: imports
// Custom type function that parses a comma-separated string into an array of strings
const CommaSeparatedList = (value: string): string[] =>
  value.split(",").map((item) => item.trim());

// Add a display property for better help documentation
CommaSeparatedList.display = "item1,item2,...";

const cli = Cli()
  .scriptName("custom-cli")
  .description("A CLI using a custom type")
  .version("1.0.0")
  .command("list", "Display list", {
    flags: {
      items: {
        type: CommaSeparatedList,
        default: [] as string[],
        description: "Comma-separated list of strings",
      },
    },
  })
  .on("list", (ctx) => {
    console.log("Items:", ctx.flags.items);
    //                              ^?
  })
  .parse();
```

The `display` property is used by the help system to show a more descriptive type name instead of the function name. For example, instead of showing "CommaSeparatedList" in the help output, it would show "item1,item2,...".

### Basic Custom Type Example

```ts twoslash
// @include: imports
// Custom type function that parses a comma-separated string into an array of strings
const CommaSeparatedList = (value: string): string[] =>
  value.split(",").map((item) => item.trim());

const cli = Cli()
  .scriptName("custom-cli")
  .description("A CLI using a custom type")
  .version("1.0.0")
  .command("list", "Display list", {
    flags: {
      items: {
        type: CommaSeparatedList,
        default: [] as string[],
        description: "Comma-separated list of strings",
      },
    },
  })
  .on("list", (ctx) => {
    console.log("Items:", ctx.flags.items);
    //                              ^?
  })
  .parse();
```

Custom type functions can also be used with array syntax to accept multiple values:

```ts twoslash
// @include: imports
const cli = Cli()
  .command("process", "Process files", {
    flags: {
      // Use [CommaSeparatedList] to accept multiple comma-separated lists
      patterns: {
        type: [CommaSeparatedList],
        short: "p",
        description: "File patterns (comma-separated)",
      },
    },
  })
  .on("process", (ctx) => {
    // $ node cli.mjs process -p "*.js,*.ts" -p "src/**"
    ctx.flags.patterns; // => [["*.js", "*.ts"], ["src/**"]]
  })
  .parse();
```

### Using Custom Types with Parameters

Custom type functions with display properties can also be used for parameters, providing better help documentation:

```ts twoslash
// @include: imports
// Custom type function for parsing version numbers
function Version(value: string): string {
  if (!/^\d+\.\d+\.\d+$/.test(value)) {
    throw new Error(`Invalid version format: ${value}. Expected format: x.y.z`);
  }

  return value;
}

// Add display property for help documentation
Version.display = "x.y.z";

const cli = Cli()
  .scriptName("release-cli")
  .description("Release management tool")
  .version("1.0.0")
  .command("publish", "Publish a new version", {
    parameters: [
      {
        key: "<version>",
        type: Version,
        description: "Version number to publish",
      },
      {
        key: "[channel]",
        type: Types.Enum("stable", "beta", "alpha"),
        description: "Release channel",
      },
    ],
  })
  .on("publish", (ctx) => {
    console.log(
      `Publishing version ${ctx.parameters.version} to ${ctx.parameters.channel || "stable"} channel`,
    );
  })
  .parse();
```

In the help output, instead of showing "Version" as the type, it will show "x.y.z", making it clearer what format is expected.

---

---

url: /reference/api/clerc/Namespace.Types.md
---

# Types

## Classes

[FlagValidationError](Types.Class.FlagValidationError.md)

‐

## Functions

[Enum](Types.Function.Enum.md)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

**Example**

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

**Throws**

If the value is not in the allowed values list

[Range](Types.Function.Range.md)

Creates a range type function that validates the input is a number within the
specified range.

**Throws**

If the value is not a number or is outside the specified
range

[Regex](Types.Function.Regex.md)

Creates a regex type function that validates the input against the provided
pattern.

**Throws**

If the value does not match the regex pattern

---

---

url: /reference/api/core/Namespace.Types.md
---

# Types

## Classes

[FlagValidationError](Types.Class.FlagValidationError.md)

‐

## Functions

[Enum](Types.Function.Enum.md)

Creates a Enum type function that validates the input against allowed values.
The display name will be formatted as "value1 | value2 | ..." for help
output.

**Example**

```typescript twoslash
// @include: imports
const format = Enum(["json", "yaml", "xml"]);
// Help output will show: json | yaml | xml
```

**Throws**

If the value is not in the allowed values list

[Range](Types.Function.Range.md)

Creates a range type function that validates the input is a number within the
specified range.

**Throws**

If the value is not a number or is outside the specified
range

[Regex](Types.Function.Regex.md)

Creates a regex type function that validates the input against the provided
pattern.

**Throws**

If the value does not match the regex pattern

---

---

url: /members.md
---

---

---

url: /official-plugins/plugin-update-notifier.md
---

# @clerc/plugin-update-notifier

A plugin to check for CLI updates using `update-notifier`.

## 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-update-notifier
```

```sh [yarn]
yarn add @clerc/plugin-update-notifier
```

```sh [pnpm]
pnpm add @clerc/plugin-update-notifier
```

:::

## 🚀 Usage

### Import

```ts twoslash
// @include: imports
import { updateNotifierPlugin } from "@clerc/plugin-update-notifier";
// or import directly from clerc
import { updateNotifierPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
import pkg from "./package.json";

Clerc.create().use(updateNotifierPlugin({ pkg })).parse();
```

## ⚙️ Options

The `updateNotifierPlugin` accepts an object with the following options:

### `pkg`

* Type: `object`
* **Required**

The `package.json` object of your CLI.

### `position`

* Type: `"pre" | "post"`
* Default: `"pre"`

Position of the update notification. `'pre'` shows before command execution, `'post'` shows after.

### `notify`

* Type: `EnhancedNotifyOptions`

Options for `notifier.notify()`. It inherits from `update-notifier`'s `NotifyOptions`, but the `message` property can also be a function that receives the `UpdateNotifier` instance.

```ts twoslash
// @include: imports
updateNotifierPlugin({
  pkg,
  notify: {
    message: (notifier) => `Update available: ${notifier.update.latest}`,
  },
});
```

### Other Options

Other options are passed directly to `update-notifier`. See [update-notifier documentation](https://github.com/sindresorhus/update-notifier#notifier--updatenotifieroptions) for more details.

## 🛠️ Context

This plugin adds the `updateNotifier` instance to the `cli.store`.

```ts twoslash
// @include: imports
cli.interceptor({
  handler: (ctx, next) => {
    console.log(ctx.store.updateNotifier);

    return next();
  },
});
```

---

---

url: /reference/api/clerc/Variable.defaultFormatters.md
---

# Variable: defaultFormatters

```ts twoslash
// @include: imports
const defaultFormatters: Formatters;
```

Defined in: [packages/plugin-help/src/formatters.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/formatters.ts#L4)

---

---

url: /reference/api/plugin-help/Variable.defaultFormatters.md
---

# Variable: defaultFormatters

```ts twoslash
// @include: imports
const defaultFormatters: Formatters;
```

Defined in: [formatters.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/plugin-help/src/formatters.ts#L4)

---

---

url: /reference/api/clerc/Variable.DOUBLE_DASH.md
---

# Variable: DOUBLE\_DASH

```ts twoslash
// @include: imports
const DOUBLE_DASH: "--" = "--";
```

Defined in: [packages/parser/src/parse.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L22)

---

---

url: /reference/api/core/Variable.DOUBLE_DASH.md
---

# Variable: DOUBLE\_DASH

```ts twoslash
// @include: imports
const DOUBLE_DASH: "--" = "--";
```

Defined in: [packages/parser/src/parse.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L22)

---

---

url: /reference/api/parser/Variable.DOUBLE_DASH.md
---

# Variable: DOUBLE\_DASH

```ts twoslash
// @include: imports
const DOUBLE_DASH: "--" = "--";
```

Defined in: [packages/parser/src/parse.ts:22](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/parse.ts#L22)

---

---

url: /reference/api/utils/Variable.isTruthy.md
---

# Variable: isTruthy()

```ts twoslash
// @include: imports
const isTruthy: <T>(item) => item is Exclude<T, false | null | undefined>;
```

Defined in: [index.ts:91](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/utils/src/index.ts#L91)

## Type Parameters

`T`

## Parameters

`item`

`T`

## Returns

item is Exclude\<T, false | null | undefined>

---

---

url: /reference/api/clerc/Variable.KNOWN_FLAG.md
---

# Variable: KNOWN\_FLAG

```ts twoslash
// @include: imports
const KNOWN_FLAG: "known-flag" = "known-flag";
```

Defined in: [packages/parser/src/iterator.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L3)

---

---

url: /reference/api/core/Variable.KNOWN_FLAG.md
---

# Variable: KNOWN\_FLAG

```ts twoslash
// @include: imports
const KNOWN_FLAG: "known-flag" = "known-flag";
```

Defined in: [packages/parser/src/iterator.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L3)

---

---

url: /reference/api/parser/Variable.KNOWN_FLAG.md
---

# Variable: KNOWN\_FLAG

```ts twoslash
// @include: imports
const KNOWN_FLAG: "known-flag" = "known-flag";
```

Defined in: [packages/parser/src/iterator.ts:3](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L3)

---

---

url: /reference/api/clerc/Variable.PARAMETER.md
---

# Variable: PARAMETER

```ts twoslash
// @include: imports
const PARAMETER: "parameter" = "parameter";
```

Defined in: [packages/parser/src/iterator.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L5)

---

---

url: /reference/api/core/Variable.PARAMETER.md
---

# Variable: PARAMETER

```ts twoslash
// @include: imports
const PARAMETER: "parameter" = "parameter";
```

Defined in: [packages/parser/src/iterator.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L5)

---

---

url: /reference/api/parser/Variable.PARAMETER.md
---

# Variable: PARAMETER

```ts twoslash
// @include: imports
const PARAMETER: "parameter" = "parameter";
```

Defined in: [packages/parser/src/iterator.ts:5](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L5)

---

---

url: /reference/api/clerc/Variable.UNKNOWN_FLAG.md
---

# Variable: UNKNOWN\_FLAG

```ts twoslash
// @include: imports
const UNKNOWN_FLAG: "unknown-flag" = "unknown-flag";
```

Defined in: [packages/parser/src/iterator.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L4)

---

---

url: /reference/api/core/Variable.UNKNOWN_FLAG.md
---

# Variable: UNKNOWN\_FLAG

```ts twoslash
// @include: imports
const UNKNOWN_FLAG: "unknown-flag" = "unknown-flag";
```

Defined in: [packages/parser/src/iterator.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L4)

---

---

url: /reference/api/parser/Variable.UNKNOWN_FLAG.md
---

# Variable: UNKNOWN\_FLAG

```ts twoslash
// @include: imports
const UNKNOWN_FLAG: "unknown-flag" = "unknown-flag";
```

Defined in: [packages/parser/src/iterator.ts:4](https://github.com/clercjs/clerc/blob/949388bc2adb5446180f4a4051142214ef707ff8/packages/parser/src/iterator.ts#L4)

---

---

url: /official-plugins/plugin-version.md
---

# @clerc/plugin-version

A plugin that adds a version command to your CLI.

:::info

This plugin is built into the `Cli` function exported by the `clerc` package, so you don't need to install it separately to use it.

:::

## Standalone Usage

### 📦 Installation

:::code-group

```sh [npm]
npm install @clerc/plugin-version
```

```sh [yarn]
yarn add @clerc/plugin-version
```

```sh [pnpm]
pnpm add @clerc/plugin-version
```

:::

### 🚀 Usage

#### Import

```ts twoslash
// @include: imports
import { versionPlugin } from "@clerc/plugin-version";
// or import directly from clerc
import { versionPlugin } from "clerc";
```

### Basic Usage

```ts twoslash
// @include: imports
const cli = Clerc.create()
  .scriptName("my-cli")
  .description("My CLI application")
  .version("1.0.0")
  .use(versionPlugin()) // Add version plugin
  .parse();
```

## Running Effect

```bash
# Display version information
$ node my-cli --version
# or
$ node my-cli version

# Output: v1.0.0
```
