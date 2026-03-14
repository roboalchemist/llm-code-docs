# Source: https://node-llama-cpp.withcat.ai/api/classes/Llama.md

---
url: /api/classes/Llama.md
---
# Class: Llama

Defined in: [bindings/Llama.ts:36](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L36)

## Properties

### onDispose

```ts
readonly onDispose: EventRelay<void>;
```

Defined in: [bindings/Llama.ts:74](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L74)

## Accessors

### disposed

#### Get Signature

```ts
get disposed(): boolean;
```

Defined in: [bindings/Llama.ts:188](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L188)

##### Returns

`boolean`

***

### classes

#### Get Signature

```ts
get classes(): LlamaClasses;
```

Defined in: [bindings/Llama.ts:192](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L192)

##### Returns

[`LlamaClasses`](../type-aliases/LlamaClasses.md)

***

### gpu

#### Get Signature

```ts
get gpu(): LlamaGpuType;
```

Defined in: [bindings/Llama.ts:199](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L199)

##### Returns

[`LlamaGpuType`](../type-aliases/LlamaGpuType.md)

***

### supportsGpuOffloading

#### Get Signature

```ts
get supportsGpuOffloading(): boolean;
```

Defined in: [bindings/Llama.ts:203](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L203)

##### Returns

`boolean`

***

### supportsMmap

#### Get Signature

```ts
get supportsMmap(): boolean;
```

Defined in: [bindings/Llama.ts:207](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L207)

##### Returns

`boolean`

***

### gpuSupportsMmap

#### Get Signature

```ts
get gpuSupportsMmap(): boolean;
```

Defined in: [bindings/Llama.ts:211](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L211)

##### Returns

`boolean`

***

### supportsMlock

#### Get Signature

```ts
get supportsMlock(): boolean;
```

Defined in: [bindings/Llama.ts:215](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L215)

##### Returns

`boolean`

***

### cpuMathCores

#### Get Signature

```ts
get cpuMathCores(): number;
```

Defined in: [bindings/Llama.ts:220](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L220)

The number of CPU cores that are useful for math

##### Returns

`number`

***

### maxThreads

#### Get Signature

```ts
get maxThreads(): number;
```

Defined in: [bindings/Llama.ts:231](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L231)

The maximum number of threads that can be used by the Llama instance.

If set to `0`, the Llama instance will have no limit on the number of threads.

See the `maxThreads` option of `getLlama` for more information.

##### Returns

`number`

#### Set Signature

```ts
set maxThreads(value: number): void;
```

Defined in: [bindings/Llama.ts:235](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L235)

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | `number` |

##### Returns

`void`

***

### numa

#### Get Signature

```ts
get numa(): LlamaNuma;
```

Defined in: [bindings/Llama.ts:242](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L242)

See the `numa` option of `getLlama` for more information

##### Returns

[`LlamaNuma`](../type-aliases/LlamaNuma.md)

***

### logLevel

#### Get Signature

```ts
get logLevel(): LlamaLogLevel;
```

Defined in: [bindings/Llama.ts:246](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L246)

##### Returns

[`LlamaLogLevel`](../enumerations/LlamaLogLevel.md)

#### Set Signature

```ts
set logLevel(value: LlamaLogLevel): void;
```

Defined in: [bindings/Llama.ts:250](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L250)

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |

##### Returns

`void`

***

### logger

#### Get Signature

```ts
get logger(): (level: LlamaLogLevel, message: string) => void;
```

Defined in: [bindings/Llama.ts:260](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L260)

##### Returns

```ts
(level: LlamaLogLevel, message: string): void;
```

###### Parameters

| Parameter | Type |
| ------ | ------ |
| `level` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |
| `message` | `string` |

###### Returns

`void`

#### Set Signature

```ts
set logger(value: (level: LlamaLogLevel, message: string) => void): void;
```

Defined in: [bindings/Llama.ts:264](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L264)

##### Parameters

| Parameter | Type |
| ------ | ------ |
| `value` | (`level`: [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md), `message`: `string`) => `void` |

##### Returns

`void`

***

### buildType

#### Get Signature

```ts
get buildType(): "localBuild" | "prebuilt";
```

Defined in: [bindings/Llama.ts:271](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L271)

##### Returns

`"localBuild"` | `"prebuilt"`

***

### cmakeOptions

#### Get Signature

```ts
get cmakeOptions(): Readonly<Record<string, string>>;
```

Defined in: [bindings/Llama.ts:275](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L275)

##### Returns

[`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<[`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`string`, `string`>>

***

### llamaCppRelease

#### Get Signature

```ts
get llamaCppRelease(): {
  repo: string;
  release: string;
};
```

Defined in: [bindings/Llama.ts:279](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L279)

##### Returns

```ts
{
  repo: string;
  release: string;
}
```

###### repo

```ts
readonly repo: string;
```

###### release

```ts
readonly release: string;
```

***

### systemInfo

#### Get Signature

```ts
get systemInfo(): string;
```

Defined in: [bindings/Llama.ts:283](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L283)

##### Returns

`string`

***

### vramPaddingSize

#### Get Signature

```ts
get vramPaddingSize(): number;
```

Defined in: [bindings/Llama.ts:295](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L295)

VRAM padding used for memory size calculations, as these calculations are not always accurate.
This is set by default to ensure stability, but can be configured when you call `getLlama`.

See `vramPadding` on `getLlama` for more information.

##### Returns

`number`

## Methods

### dispose()

```ts
dispose(): Promise<void>;
```

Defined in: [bindings/Llama.ts:170](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L170)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`void`>

***

### getVramState()

```ts
getVramState(): Promise<{
  total: number;
  used: number;
  free: number;
  unifiedSize: number;
}>;
```

Defined in: [bindings/Llama.ts:305](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L305)

The total amount of VRAM that is currently being used.

`unifiedSize` represents the amount of VRAM that is shared between the CPU and GPU.
On SoC devices, this is usually the same as `total`.

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`total`: `number`;
`used`: `number`;
`free`: `number`;
`unifiedSize`: `number`;
}>

***

### getSwapState()

```ts
getSwapState(): Promise<{
  maxSize: number;
  allocated: number;
  used: number;
}>;
```

Defined in: [bindings/Llama.ts:330](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L330)

Get the state of the swap memory.

**`maxSize`** - The maximum size of the swap memory that the system can allocate.
If the swap size is dynamic (like on macOS), this will be `Infinity`.

**`allocated`** - The total size allocated by the system for swap memory.

**`used`** - The amount of swap memory that is currently being used from the `allocated` size.

On Windows, this will return the info for the page file.

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<{
`maxSize`: `number`;
`allocated`: `number`;
`used`: `number`;
}>

***

### getGpuDeviceNames()

```ts
getGpuDeviceNames(): Promise<string[]>;
```

Defined in: [bindings/Llama.ts:356](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L356)

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`string`\[]>

***

### loadModel()

```ts
loadModel(options: LlamaModelOptions): Promise<LlamaModel>;
```

Defined in: [bindings/Llama.ts:364](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L364)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaModelOptions`](../type-aliases/LlamaModelOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaModel`](LlamaModel.md)>

***

### createGrammarForJsonSchema()

```ts
createGrammarForJsonSchema<T, Defs>(schema: Readonly<T> & GbnfJsonSchema<Defs>): Promise<LlamaJsonSchemaGrammar<T, Defs>>;
```

Defined in: [bindings/Llama.ts:384](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L384)

#### Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* | [`GbnfJsonBasicSchema`](../type-aliases/GbnfJsonBasicSchema.md) | [`GbnfJsonConstSchema`](../type-aliases/GbnfJsonConstSchema.md) | [`GbnfJsonEnumSchema`](../type-aliases/GbnfJsonEnumSchema.md) | [`GbnfJsonBasicStringSchema`](../type-aliases/GbnfJsonBasicStringSchema.md) | [`GbnfJsonFormatStringSchema`](../type-aliases/GbnfJsonFormatStringSchema.md) | [`GbnfJsonOneOfSchema`](../type-aliases/GbnfJsonOneOfSchema.md)<`Defs`> | [`GbnfJsonObjectSchema`](../type-aliases/GbnfJsonObjectSchema.md)<`string`, `Defs`> | [`GbnfJsonArraySchema`](../type-aliases/GbnfJsonArraySchema.md)<`Defs`> | `GbnfJsonRefSchema`<`Defs`> | - |
| `Defs` *extends* `GbnfJsonDefList`<`Defs`> | [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`any`, `any`> |

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `schema` | [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<`T`> & [`GbnfJsonSchema`](../type-aliases/GbnfJsonSchema.md)<`Defs`> |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaJsonSchemaGrammar`](LlamaJsonSchemaGrammar.md)<`T`, `Defs`>>

#### See

* [Using a JSON Schema Grammar](https://node-llama-cpp.withcat.ai/guide/grammar#json-schema) tutorial
* [Reducing Hallucinations When Using JSON Schema Grammar](https://node-llama-cpp.withcat.ai/guide/grammar#reducing-json-schema-hallucinations) tutorial

***

### getGrammarFor()

```ts
getGrammarFor(type: 
  | "json"
  | "json_arr"
  | "english"
  | "list"
  | "c"
  | "arithmetic"
  | "japanese"
  | "chess"): Promise<LlamaGrammar>;
```

Defined in: [bindings/Llama.ts:392](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L392)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `type` | | `"json"` | `"json_arr"` | `"english"` | `"list"` | `"c"` | `"arithmetic"` | `"japanese"` | `"chess"` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaGrammar`](LlamaGrammar.md)>

***

### createGrammar()

```ts
createGrammar(options: LlamaGrammarOptions): Promise<LlamaGrammar>;
```

Defined in: [bindings/Llama.ts:399](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L399)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `options` | [`LlamaGrammarOptions`](../type-aliases/LlamaGrammarOptions.md) |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaGrammar`](LlamaGrammar.md)>

#### See

[Using Grammar](https://node-llama-cpp.withcat.ai/guide/grammar) tutorial

***

### defaultConsoleLogger()

```ts
static defaultConsoleLogger(level: LlamaLogLevel, message: string): void;
```

Defined in: [bindings/Llama.ts:611](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/bindings/Llama.ts#L611)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `level` | [`LlamaLogLevel`](../enumerations/LlamaLogLevel.md) |
| `message` | `string` |

#### Returns

`void`
