# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaJsonSchemaGrammar.md

---
url: /api/classes/LlamaJsonSchemaGrammar.md
---
# Class: LlamaJsonSchemaGrammar\<T, Defs>

Defined in: [evaluator/LlamaJsonSchemaGrammar.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaJsonSchemaGrammar.ts#L13)

## See

* [Using a JSON Schema Grammar](https://node-llama-cpp.withcat.ai/guide/grammar#json-schema) tutorial
* [Reducing Hallucinations When Using JSON Schema Grammar](https://node-llama-cpp.withcat.ai/guide/grammar#reducing-json-schema-hallucinations) tutorial

## Extends

* [`LlamaGrammar`](LlamaGrammar.md)

## Type Parameters

| Type Parameter | Default type |
| ------ | ------ |
| `T` *extends* [`GbnfJsonSchema`](../type-aliases/GbnfJsonSchema.md)<`Defs`> | - |
| `Defs` *extends* `GbnfJsonDefList`<`Defs`> | [`Record`](https://www.typescriptlang.org/docs/handbook/utility-types.html#recordkeys-type)<`any`, `any`> |

## Constructors

### Constructor

```ts
new LlamaJsonSchemaGrammar<T, Defs>(llama: Llama, schema: Readonly<T> & GbnfJsonSchema<Defs>): LlamaJsonSchemaGrammar<T, Defs>;
```

Defined in: [evaluator/LlamaJsonSchemaGrammar.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaJsonSchemaGrammar.ts#L23)

Prefer to create a new instance of this class by using `llama.createGrammarForJsonSchema(...)`.

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `llama` | [`Llama`](Llama.md) |
| `schema` | [`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<`T`> & [`GbnfJsonSchema`](../type-aliases/GbnfJsonSchema.md)<`Defs`> |

#### Returns

`LlamaJsonSchemaGrammar`<`T`, `Defs`>

#### Deprecated

Use `llama.createGrammarForJsonSchema(...)` instead.

#### Overrides

[`LlamaGrammar`](LlamaGrammar.md).[`constructor`](LlamaGrammar.md#constructor)

## Accessors

### grammar

#### Get Signature

```ts
get grammar(): string;
```

Defined in: [evaluator/LlamaGrammar.ts:64](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L64)

##### Returns

`string`

#### Inherited from

[`LlamaGrammar`](LlamaGrammar.md).[`grammar`](LlamaGrammar.md#grammar)

***

### rootRuleName

#### Get Signature

```ts
get rootRuleName(): string;
```

Defined in: [evaluator/LlamaGrammar.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L68)

##### Returns

`string`

#### Inherited from

[`LlamaGrammar`](LlamaGrammar.md).[`rootRuleName`](LlamaGrammar.md#rootrulename)

***

### stopGenerationTriggers

#### Get Signature

```ts
get stopGenerationTriggers(): readonly (
  | string
  | LlamaText
  | readonly (string | Token)[])[];
```

Defined in: [evaluator/LlamaGrammar.ts:72](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L72)

##### Returns

readonly (
| `string`
| [`LlamaText`](LlamaText.md)
| readonly (`string` | [`Token`](../type-aliases/Token.md))\[])\[]

#### Inherited from

[`LlamaGrammar`](LlamaGrammar.md).[`stopGenerationTriggers`](LlamaGrammar.md#stopgenerationtriggers)

***

### trimWhitespaceSuffix

#### Get Signature

```ts
get trimWhitespaceSuffix(): boolean;
```

Defined in: [evaluator/LlamaGrammar.ts:76](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L76)

##### Returns

`boolean`

#### Inherited from

[`LlamaGrammar`](LlamaGrammar.md).[`trimWhitespaceSuffix`](LlamaGrammar.md#trimwhitespacesuffix)

***

### schema

#### Get Signature

```ts
get schema(): Readonly<T>;
```

Defined in: [evaluator/LlamaJsonSchemaGrammar.ts:35](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaJsonSchemaGrammar.ts#L35)

##### Returns

[`Readonly`](https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlytype)<`T`>

## Methods

### getFor()

```ts
static getFor(llama: Llama, type: 
  | "json"
  | "json_arr"
  | "english"
  | "list"
  | "c"
  | "arithmetic"
  | "japanese"
  | "chess"): Promise<LlamaGrammar>;
```

Defined in: [evaluator/LlamaGrammar.ts:88](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L88)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `llama` | [`Llama`](Llama.md) |
| `type` | | `"json"` | `"json_arr"` | `"english"` | `"list"` | `"c"` | `"arithmetic"` | `"japanese"` | `"chess"` |

#### Returns

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<[`LlamaGrammar`](LlamaGrammar.md)>

#### Inherited from

[`LlamaGrammar`](LlamaGrammar.md).[`getFor`](LlamaGrammar.md#getfor)

***

### parse()

```ts
parse(json: string): GbnfJsonSchemaToType<T>;
```

Defined in: [evaluator/LlamaJsonSchemaGrammar.ts:39](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaJsonSchemaGrammar.ts#L39)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `json` | `string` |

#### Returns

[`GbnfJsonSchemaToType`](../type-aliases/GbnfJsonSchemaToType.md)<`T`>
