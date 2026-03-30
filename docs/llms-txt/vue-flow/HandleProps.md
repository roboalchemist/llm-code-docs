# Source: https://vueflow.dev/typedocs/interfaces/HandleProps.md

---
url: /typedocs/interfaces/HandleProps.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Interface: HandleProps

## Properties

### connectable?

> `optional` **connectable**: [`HandleConnectable`](../type-aliases/HandleConnectable.md)

Enable/disable connecting to handle altogether

***

### connectableEnd?

> `optional` **connectableEnd**: `boolean`

Can this handle be used to *end* a connection

***

### connectableStart?

> `optional` **connectableStart**: `boolean`

Can this handle be used to *start* a connection

***

### id?

> `optional` **id**: `string`

Unique id of handle element

***

### isValidConnection?

> `optional` **isValidConnection**: [`ValidConnectionFunc`](../type-aliases/ValidConnectionFunc.md)

A valid connection func [ValidConnectionFunc](../type-aliases/ValidConnectionFunc.md)

***

### position?

> `optional` **position**: [`Position`](../enumerations/Position.md)

Handle position (top, bottom, left, right) [Position](../enumerations/Position.md)

***

### type?

> `optional` **type**: [`HandleType`](../type-aliases/HandleType.md)

Handle type (source / target) [HandleType](../type-aliases/HandleType.md)
