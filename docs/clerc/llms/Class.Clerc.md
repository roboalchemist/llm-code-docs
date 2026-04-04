# Source: https://clerc.so1ve.dev/reference/api/core/Class.Clerc.md

# Source: https://clerc.so1ve.dev/reference/api/clerc/Class.Clerc.md

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
