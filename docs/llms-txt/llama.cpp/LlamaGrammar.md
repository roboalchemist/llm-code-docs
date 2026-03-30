# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaGrammar.md

---
url: /api/classes/LlamaGrammar.md
---
# Class: LlamaGrammar

Defined in: [evaluator/LlamaGrammar.ts:31](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L31)

## See

[Using Grammar](https://node-llama-cpp.withcat.ai/guide/grammar) tutorial

## Extended by

* [`LlamaJsonSchemaGrammar`](LlamaJsonSchemaGrammar.md)

## Constructors

### Constructor

```ts
new LlamaGrammar(llama: Llama, options: LlamaGrammarOptions): LlamaGrammar;
```

Defined in: [evaluator/LlamaGrammar.ts:50](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L50)

> GBNF files are supported.
> More info here: [
> github:ggml-org/llama.cpp:grammars/README.md
> ](https://github.com/ggml-org/llama.cpp/blob/f5fe98d11bdf9e7797bcfb05c0c3601ffc4b9d26/grammars/README.md)

Prefer to create a new instance of this class by using `llama.createGrammar(...)`.

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `llama` | [`Llama`](Llama.md) | - |
| `options` | [`LlamaGrammarOptions`](../type-aliases/LlamaGrammarOptions.md) | - |

#### Returns

`LlamaGrammar`

#### Deprecated

Use `llama.createGrammar(...)` instead.

## Accessors

### grammar

#### Get Signature

```ts
get grammar(): string;
```

Defined in: [evaluator/LlamaGrammar.ts:64](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L64)

##### Returns

`string`

***

### rootRuleName

#### Get Signature

```ts
get rootRuleName(): string;
```

Defined in: [evaluator/LlamaGrammar.ts:68](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L68)

##### Returns

`string`

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

***

### trimWhitespaceSuffix

#### Get Signature

```ts
get trimWhitespaceSuffix(): boolean;
```

Defined in: [evaluator/LlamaGrammar.ts:76](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/evaluator/LlamaGrammar.ts#L76)

##### Returns

`boolean`

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

[`Promise`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Promise)<`LlamaGrammar`>
