# Source: https://docs.replit.com/extensions/api/replDb.md

# replDb API

> Learn how to use ReplDB, a key-value store for Replit Apps, to persist data in your extensions through simple read and write operations.

ReplDB is a simple key-value store available on all replit apps by default. Extensions can use ReplDB to store replit apps specific data.

## Usage

```ts  theme={null}
import { replDb } from '@replit/extensions';
```

## Methods

### `replDb.set`

Sets the value for a given key. Required [permissions](./manifest#scopetype): `repldb:read`, `repldb:write`.

```ts  theme={null}
set(args: { key: string, value: any }): Promise<void>
```

### `replDb.get`

Returns a value associated with the given key. Required [permissions](./manifest#scopetype): `repldb:read`.

```ts  theme={null}
get(args: { key: string }): Promise<string | { error: null | string }>
```

### `replDb.list`

Lists keys in the replDb. Accepts an optional `prefix`, which filters for keys beginning with the given prefix. Required [permissions](./manifest#scopetype): `repldb:read`.

```ts  theme={null}
list(args: { prefix: string }): Promise<{ keys: string[] } | { error: string }>
```

### `replDb.del`

Deletes a key in the replDb. Required [permissions](./manifest#scopetype): `repldb:read`, `repldb:write`.

```ts  theme={null}
del(args: { key: string }): Promise<void>
```
