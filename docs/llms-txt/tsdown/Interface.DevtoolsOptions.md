# Source: https://tsdown.dev/reference/api/Interface.DevtoolsOptions.md

---
url: /reference/api/Interface.DevtoolsOptions.md
---
# Interface: DevtoolsOptions

Defined in: [src/features/devtools.ts:5](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L5)

## Extends

* `NonNullable`<`InputOptions`\[`"devtools"`]>

## Properties

### clean?

```ts
optional clean: boolean;
```

Defined in: [src/features/devtools.ts:18](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L18)

Clean devtools stale sessions.

#### Default

```ts
true
```

***

### sessionId?

```ts
optional sessionId: string;
```

Defined in: node\_modules/.pnpm/rolldown@1.0.0-rc.9/node\_modules/rolldown/dist/shared/define-config-cG45vHwf.d.mts:3700

#### Inherited from

```ts
NonNullable.sessionId
```

***

### ui?

```ts
optional ui: boolean | Partial<StartOptions>;
```

Defined in: [src/features/devtools.ts:11](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/devtools.ts#L11)

**\[experimental]** Enable devtools integration. `@vitejs/devtools` must be installed as a dependency.

Defaults to true, if `@vitejs/devtools` is installed.
