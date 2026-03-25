# Source: https://node-llama-cpp.withcat.ai/api/classes/InsufficientMemoryError.md

---
url: /api/classes/InsufficientMemoryError.md
---
# Class: InsufficientMemoryError

Defined in: [utils/InsufficientMemoryError.ts:1](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/InsufficientMemoryError.ts#L1)

## Extends

* [`Error`](https://developer.mozilla.org/docs/Web/JavaScript/Reference/Global_Objects/Error)

## Constructors

### Constructor

```ts
new InsufficientMemoryError(message?: string): InsufficientMemoryError;
```

Defined in: [utils/InsufficientMemoryError.ts:2](https://github.com/withcatai/node-llama-cpp/blob/89314022104def53c5fe5c13cb1ceca25b77a8e2/src/utils/InsufficientMemoryError.ts#L2)

#### Parameters

| Parameter | Type | Default value |
| ------ | ------ | ------ |
| `message` | `string` | `"Insufficient memory"` |

#### Returns

`InsufficientMemoryError`

#### Overrides

```ts
Error.constructor
```
