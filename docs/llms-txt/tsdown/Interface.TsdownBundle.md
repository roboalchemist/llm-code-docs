# Source: https://tsdown.dev/reference/api/Interface.TsdownBundle.md

---
url: /reference/api/Interface.TsdownBundle.md
---
# Interface: TsdownBundle

Defined in: [src/utils/chunks.ts:7](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L7)

## Extends

* `AsyncDisposable`

## Properties

### chunks

```ts
chunks: RolldownChunk[];
```

Defined in: [src/utils/chunks.ts:8](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L8)

***

### config

```ts
config: ResolvedConfig
```

Defined in: [src/utils/chunks.ts:9](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L9)

***

### inlinedDeps

```ts
inlinedDeps: Map<string, Set<string>>
```

Defined in: [src/utils/chunks.ts:10](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/utils/chunks.ts#L10)

## Methods

### \[asyncDispose]\()

```ts
asyncDispose: PromiseLike<void>
```

Defined in: node\_modules/.pnpm/typescript@5.9.3/node\_modules/typescript/lib/lib.esnext.disposable.d.ts:40

#### Returns

`PromiseLike`<`void`>

#### Inherited from

```ts
AsyncDisposable.[asyncDispose]
```
