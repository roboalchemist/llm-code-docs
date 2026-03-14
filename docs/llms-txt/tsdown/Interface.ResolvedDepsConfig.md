# Source: https://tsdown.dev/reference/api/Interface.ResolvedDepsConfig.md

---
url: /reference/api/Interface.ResolvedDepsConfig.md
---
# Interface: ResolvedDepsConfig

Defined in: [src/features/deps.ts:69](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L69)

## Properties

### alwaysBundle?

```ts
optional alwaysBundle: NoExternalFn;
```

Defined in: [src/features/deps.ts:71](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L71)

***

### neverBundle?

```ts
optional neverBundle: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/features/deps.ts:70](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L70)

***

### onlyBundle?

```ts
optional onlyBundle: false | (string | RegExp)[];
```

Defined in: [src/features/deps.ts:72](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L72)

***

### skipNodeModulesBundle

```ts
skipNodeModulesBundle: boolean
```

Defined in: [src/features/deps.ts:73](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L73)
