# Source: https://node-llama-cpp.withcat.ai/api/classes/LlamaJsonSchemaValidationError.md

---
url: /api/classes/LlamaJsonSchemaValidationError.md
---
# Class: LlamaJsonSchemaValidationError

Defined in: [utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts:23](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts#L23)

## Extends

* [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error)

## Constructors

### Constructor

```ts
new LlamaJsonSchemaValidationError(
   message: string, 
   object: any, 
   schema: GbnfJsonSchema): LlamaJsonSchemaValidationError;
```

Defined in: [utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts:27](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts#L27)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `message` | `string` |
| `object` | `any` |
| `schema` | [`GbnfJsonSchema`](../type-aliases/GbnfJsonSchema.md) |

#### Returns

`LlamaJsonSchemaValidationError`

#### Overrides

```ts
Error.constructor
```

## Properties

### object

```ts
readonly object: any;
```

Defined in: [utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts:24](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts#L24)

***

### schema

```ts
readonly schema: GbnfJsonSchema;
```

Defined in: [utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts:25](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/gbnfJson/utils/validateObjectAgainstGbnfSchema.ts#L25)
