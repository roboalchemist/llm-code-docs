# Source: https://vueflow.dev/typedocs/classes/VueFlowError.md

---
url: /typedocs/classes/VueFlowError.md
---
[**@vue-flow/monorepo**](../index.md) • **Docs**

***

# Class: VueFlowError\<T, Args>

## Extends

* `Error`

## Type Parameters

• **T** *extends* [`ErrorCode`](../enumerations/ErrorCode.md) = [`ErrorCode`](../enumerations/ErrorCode.md)

• **Args** *extends* `ErrorArgs`<`T`> = `ErrorArgs`<`T`>

## Constructors

### new VueFlowError()

> **new VueFlowError**<`T`, `Args`>(`code`, ...`args`): [`VueFlowError`](VueFlowError.md)<`T`, `Args`>

#### Parameters

• **code**: `T`

• ...**args**: `Args`

#### Returns

[`VueFlowError`](VueFlowError.md)<`T`, `Args`>

#### Overrides

`Error.constructor`

## Properties

### args

> **args**: `Args`

***

### cause?

> `optional` **cause**: `unknown`

#### Inherited from

`Error.cause`

***

### code

> **code**: `T`

***

### message

> **message**: `string`

#### Inherited from

`Error.message`

***

### name

> **name**: `string` = `'VueFlowError'`

#### Overrides

`Error.name`

***

### stack?

> `optional` **stack**: `string`

#### Inherited from

`Error.stack`

***

### prepareStackTrace()?

> `static` `optional` **prepareStackTrace**: (`err`, `stackTraces`) => `any`

Optional override for formatting stack traces

#### Parameters

• **err**: `Error`

• **stackTraces**: `CallSite`\[]

#### Returns

`any`

#### See

https://v8.dev/docs/stack-trace-api#customizing-stack-traces

#### Inherited from

`Error.prepareStackTrace`

***

### stackTraceLimit

> `static` **stackTraceLimit**: `number`

#### Inherited from

`Error.stackTraceLimit`

## Methods

### captureStackTrace()

> `static` **captureStackTrace**(`targetObject`, `constructorOpt`?): `void`

Create .stack property on a target object

#### Parameters

• **targetObject**: `object`

• **constructorOpt?**: `Function`

#### Returns

`void`

#### Inherited from

`Error.captureStackTrace`
