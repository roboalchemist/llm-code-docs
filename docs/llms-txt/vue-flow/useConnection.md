# Source: https://vueflow.dev/typedocs/functions/useConnection.md

---
url: /typedocs/functions/useConnection.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Function: useConnection()

> **useConnection**(): `object`

Composable for accessing the currently ongoing connection.

## Returns

`object`

current connection: startHandle, endHandle, status, position

### endHandle

> **endHandle**: `Ref`<`null` | [`ConnectingHandle`](../interfaces/ConnectingHandle.md)>

### position

> **position**: `Ref`<[`XYPosition`](../interfaces/XYPosition.md)>

### startHandle

> **startHandle**: `Ref`<`null` | [`ConnectingHandle`](../interfaces/ConnectingHandle.md)>

### status

> **status**: `Ref`<`null` | [`ConnectionStatus`](../type-aliases/ConnectionStatus.md)>
