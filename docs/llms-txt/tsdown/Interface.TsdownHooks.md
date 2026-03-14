# Source: https://tsdown.dev/reference/api/Interface.TsdownHooks.md

---
url: /reference/api/Interface.TsdownHooks.md
---
# Interface: TsdownHooks

Defined in: [src/features/hooks.ts:20](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L20)

Hooks for tsdown.

## Properties

### build:before()

```ts
build:before: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:31](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L31)

Invoked before each Rolldown build.
For dual-format builds, this hook is called for each format.
Useful for configuring or modifying the build context before bundling.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md) & [`RolldownContext`](Interface.RolldownContext.md)

#### Returns

`void` | `Promise`<`void`>

***

### build:done()

```ts
build:done: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:36](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L36)

Invoked after each tsdown build completes.
Use this hook for cleanup or post-processing tasks.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md) & `object`

#### Returns

`void` | `Promise`<`void`>

***

### build:prepare()

```ts
build:prepare: (ctx) => void | Promise<void>;
```

Defined in: [src/features/hooks.ts:25](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/hooks.ts#L25)

Invoked before each tsdown build starts.
Use this hook to perform setup or preparation tasks.

#### Parameters

##### ctx

[`BuildContext`](Interface.BuildContext.md)

#### Returns

`void` | `Promise`<`void`>
