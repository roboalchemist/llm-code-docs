# Source: https://vueflow.dev/typedocs/type-aliases/HandleConnectable.md

---
url: /typedocs/type-aliases/HandleConnectable.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Type Alias: HandleConnectable

> **HandleConnectable**: `boolean` | `number` | `"single"` | [`HandleConnectableFunc`](HandleConnectableFunc.md)

set to true to allow unlimited connections,
single for only one connection
or use a cb function to determine connect-ability

if set to single and the handle already has more than one connection, it will act the same as setting it to false
