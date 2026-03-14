# Source: https://node-llama-cpp.withcat.ai/api/classes/ChatModelFunctionsDocumentationGenerator.md

---
url: /api/classes/ChatModelFunctionsDocumentationGenerator.md
---
# Class: ChatModelFunctionsDocumentationGenerator

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:9](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L9)

Generate documentation about the functions that are available for a model to call.
Useful for generating a system message with information about the available functions as part of a chat wrapper.

## Constructors

### Constructor

```ts
new ChatModelFunctionsDocumentationGenerator(chatModelFunctions: 
  | ChatModelFunctions
  | undefined): ChatModelFunctionsDocumentationGenerator;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:13](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L13)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `chatModelFunctions` | | [`ChatModelFunctions`](../type-aliases/ChatModelFunctions.md) | `undefined` |

#### Returns

`ChatModelFunctionsDocumentationGenerator`

## Properties

### chatModelFunctions?

```ts
readonly optional chatModelFunctions: ChatModelFunctions;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:10](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L10)

***

### hasAnyFunctions

```ts
readonly hasAnyFunctions: boolean;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:11](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L11)

## Methods

### getTypeScriptFunctionSignatures()

```ts
getTypeScriptFunctionSignatures(options?: {
  documentParams?: boolean;
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:30](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L30)

Example:

```ts
// Retrieve the current date
function getDate();

// Retrieve the current time
function getTime(params: {hours: "24" | "12", seconds: boolean});
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `documentParams?`: `boolean`; } | - |
| `options.documentParams?` | `boolean` | Whether to document the parameters of the functions |

#### Returns

`string`

***

### getTypeScriptFunctionTypes()

```ts
getTypeScriptFunctionTypes(options?: {
  documentParams?: boolean;
  reservedFunctionNames?: string[];
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:73](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L73)

Example:

```ts
// Retrieve the current date
type getDate = () => any;

// Retrieve the current time
type getTime = (_: {hours: "24" | "12", seconds: boolean}) => any;
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `documentParams?`: `boolean`; `reservedFunctionNames?`: `string`\[]; } | - |
| `options.documentParams?` | `boolean` | Whether to document the parameters of the functions |
| `options.reservedFunctionNames?` | `string`\[] | Function names that are reserved and cannot be used |

#### Returns

`string`

***

### getLlama3\_1FunctionSignatures()

```ts
getLlama3_1FunctionSignatures(options?: {
  documentParams?: boolean;
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:120](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L120)

Example:

```
Use the function 'getDate' to: Retrieve the current date
{"name": "getDate", "description": "Retrieve the current date"}

Use the function 'getTime' to: Retrieve the current time
{"name": "getTime", "description": "Retrieve the current time", "parameters": {"type": "object", "properties": {"hours": {"enum": ["24", "12"]}, "seconds": {"type": "boolean"}}}}
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `documentParams?`: `boolean`; } | - |
| `options.documentParams?` | `boolean` | Whether to document the parameters of the functions |

#### Returns

`string`

***

### getLlama3\_2LightweightFunctionSignatures()

```ts
getLlama3_2LightweightFunctionSignatures(options?: {
  documentParams?: boolean;
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:162](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L162)

Example:

```
{"name": "getDate", "description": "Retrieve the current date"}

{"name": "getTime", "description": "Retrieve the current time", "parameters": {"type": "object", "properties": {"hours": {"enum": ["24", "12"]}, "seconds": {"type": "boolean"}}}}
```

#### Parameters

| Parameter | Type | Description |
| ------ | ------ | ------ |
| `options` | { `documentParams?`: `boolean`; } | - |
| `options.documentParams?` | `boolean` | Whether to document the parameters of the functions |

#### Returns

`string`

***

### getQwenFunctionSignatures()

```ts
getQwenFunctionSignatures(__namedParameters?: {
  documentParams?: boolean;
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:188](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L188)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

`string`

***

### getSeedFunctionSignatures()

```ts
getSeedFunctionSignatures(__namedParameters?: {
  documentParams?: boolean;
}): string;
```

Defined in: [chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts:194](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/chatWrappers/utils/ChatModelFunctionsDocumentationGenerator.ts#L194)

#### Parameters

| Parameter | Type |
| ------ | ------ |
| `__namedParameters` | { `documentParams?`: `boolean`; } |
| `__namedParameters.documentParams?` | `boolean` |

#### Returns

`string`
