# Source: https://tsdown.dev/reference/api/Interface.PublintOptions.md

---
url: /reference/api/Interface.PublintOptions.md
---
# Interface: PublintOptions

Defined in: [src/features/pkg/publint.ts:11](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/pkg/publint.ts#L11)

## Extends

* `Omit`<`Options`, `"pack"` | `"pkgDir"`>

## Properties

### level?

```ts
optional level: "error" | "suggestion" | "warning";
```

Defined in: node\_modules/.pnpm/publint@0.3.18/node\_modules/publint/src/index.d.ts:159

The level of messages to log (default: `'suggestion'`).

* `suggestion`: logs all messages
* `warning`: logs only `warning` and `error` messages
* `error`: logs only `error` messages

#### Inherited from

```ts
Omit.level
```

***

### strict?

```ts
optional strict: boolean;
```

Defined in: node\_modules/.pnpm/publint@0.3.18/node\_modules/publint/src/index.d.ts:193

Report warnings as errors. This runs before `level` filters the result, which means that if
`level` is set to `'error'`, all warnings (elevated as errors) will still be reported.

#### Inherited from

```ts
Omit.strict
```
