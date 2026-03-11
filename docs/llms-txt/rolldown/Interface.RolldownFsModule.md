# Source: https://rolldown.rs/reference/Interface.RolldownFsModule.md

---
url: /reference/Interface.RolldownFsModule.md
---
# Interface: RolldownFsModule

## Methods

### appendFile()

* **Type**: (`path`: `string`, `data`: `string` | `Uint8Array`<`ArrayBufferLike`>, `options?`: { `encoding?`: [`BufferEncoding`](TypeAlias.BufferEncoding.md) | `null`; `flag?`: `string` | `number`; `mode?`: `string` | `number`; }) => `Promise`<`void`>

#### Parameters

##### path

`string`

##### data

`string` | `Uint8Array`<`ArrayBufferLike`>

##### options?

###### encoding?

[`BufferEncoding`](TypeAlias.BufferEncoding.md) | `null`

###### flag?

`string` | `number`

###### mode?

`string` | `number`

#### Returns

`Promise`<`void`>

***

### copyFile()

* **Type**: (`source`: `string`, `destination`: `string`, `mode?`: `string` | `number`) => `Promise`<`void`>

#### Parameters

##### source

`string`

##### destination

`string`

##### mode?

`string` | `number`

#### Returns

`Promise`<`void`>

***

### lstat()

* **Type**: (`path`: `string`) => `Promise`<[`RolldownFileStats`](Interface.RolldownFileStats.md)>

#### Parameters

##### path

`string`

#### Returns

`Promise`<[`RolldownFileStats`](Interface.RolldownFileStats.md)>

***

### mkdir()

* **Type**: (`path`: `string`, `options?`: { `mode?`: `string` | `number`; `recursive?`: `boolean`; }) => `Promise`<`void`>

#### Parameters

##### path

`string`

##### options?

###### mode?

`string` | `number`

###### recursive?

`boolean`

#### Returns

`Promise`<`void`>

***

### mkdtemp()

* **Type**: (`prefix`: `string`) => `Promise`<`string`>

#### Parameters

##### prefix

`string`

#### Returns

`Promise`<`string`>

***

### readdir()

#### Call Signature

* **Type**: (`path`: `string`, `options?`: { `withFileTypes?`: `false`; }) => `Promise`<`string`\[]>

##### Parameters

###### path

`string`

###### options?

###### withFileTypes?

`false`

##### Returns

`Promise`<`string`\[]>

#### Call Signature

* **Type**: (`path`: `string`, `options?`: { `withFileTypes`: `true`; }) => `Promise`<[`RolldownDirectoryEntry`](Interface.RolldownDirectoryEntry.md)\[]>

##### Parameters

###### path

`string`

###### options?

###### withFileTypes

`true`

##### Returns

`Promise`<[`RolldownDirectoryEntry`](Interface.RolldownDirectoryEntry.md)\[]>

***

### readFile()

#### Call Signature

* **Type**: (`path`: `string`, `options?`: { `encoding?`: `null`; `flag?`: `string` | `number`; `signal?`: `AbortSignal`; }) => `Promise`<`Uint8Array`<`ArrayBufferLike`>>

##### Parameters

###### path

`string`

###### options?

###### encoding?

`null`

###### flag?

`string` | `number`

###### signal?

`AbortSignal`

##### Returns

`Promise`<`Uint8Array`<`ArrayBufferLike`>>

#### Call Signature

* **Type**: (`path`: `string`, `options?`: { `encoding`: [`BufferEncoding`](TypeAlias.BufferEncoding.md); `flag?`: `string` | `number`; `signal?`: `AbortSignal`; }) => `Promise`<`string`>

##### Parameters

###### path

`string`

###### options?

###### encoding

[`BufferEncoding`](TypeAlias.BufferEncoding.md)

###### flag?

`string` | `number`

###### signal?

`AbortSignal`

##### Returns

`Promise`<`string`>

***

### realpath()

* **Type**: (`path`: `string`) => `Promise`<`string`>

#### Parameters

##### path

`string`

#### Returns

`Promise`<`string`>

***

### rename()

* **Type**: (`oldPath`: `string`, `newPath`: `string`) => `Promise`<`void`>

#### Parameters

##### oldPath

`string`

##### newPath

`string`

#### Returns

`Promise`<`void`>

***

### rmdir()

* **Type**: (`path`: `string`, `options?`: { `recursive?`: `boolean`; }) => `Promise`<`void`>

#### Parameters

##### path

`string`

##### options?

###### recursive?

`boolean`

#### Returns

`Promise`<`void`>

***

### stat()

* **Type**: (`path`: `string`) => `Promise`<[`RolldownFileStats`](Interface.RolldownFileStats.md)>

#### Parameters

##### path

`string`

#### Returns

`Promise`<[`RolldownFileStats`](Interface.RolldownFileStats.md)>

***

### unlink()

* **Type**: (`path`: `string`) => `Promise`<`void`>

#### Parameters

##### path

`string`

#### Returns

`Promise`<`void`>

***

### writeFile()

* **Type**: (`path`: `string`, `data`: `string` | `Uint8Array`<`ArrayBufferLike`>, `options?`: { `encoding?`: [`BufferEncoding`](TypeAlias.BufferEncoding.md) | `null`; `flag?`: `string` | `number`; `mode?`: `string` | `number`; }) => `Promise`<`void`>

#### Parameters

##### path

`string`

##### data

`string` | `Uint8Array`<`ArrayBufferLike`>

##### options?

###### encoding?

[`BufferEncoding`](TypeAlias.BufferEncoding.md) | `null`

###### flag?

`string` | `number`

###### mode?

`string` | `number`

#### Returns

`Promise`<`void`>
