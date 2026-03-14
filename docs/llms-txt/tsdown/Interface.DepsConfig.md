# Source: https://tsdown.dev/reference/api/Interface.DepsConfig.md

---
url: /reference/api/Interface.DepsConfig.md
---
# Interface: DepsConfig

Defined in: [src/features/deps.ts:35](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L35)

## Properties

### alwaysBundle?

```ts
optional alwaysBundle:
  | Arrayable<string | RegExp>
  | NoExternalFn;
```

Defined in: [src/features/deps.ts:44](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L44)

Force dependencies to be bundled, even if they are in `dependencies` or `peerDependencies`.

***

### neverBundle?

```ts
optional neverBundle: string | RegExp | (string | RegExp)[] | ExternalOptionFunction;
```

Defined in: [src/features/deps.ts:40](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L40)

Mark dependencies as external (not bundled).
Accepts strings, regular expressions, or Rolldown's `ExternalOption`.

***

### ~~onlyAllowBundle?~~

```ts
optional onlyAllowBundle: false | Arrayable<string | RegExp>;
```

Defined in: [src/features/deps.ts:58](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L58)

#### Deprecated

Use [onlyBundle](#onlybundle) instead.

***

### onlyBundle?

```ts
optional onlyBundle: false | Arrayable<string | RegExp>;
```

Defined in: [src/features/deps.ts:54](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L54)

Whitelist of dependencies allowed to be bundled from `node_modules`.
Throws an error if any unlisted dependency is bundled.

* `undefined` (default): Show warnings for bundled dependencies.
* `false`: Suppress all warnings about bundled dependencies.

Note: Be sure to include all required sub-dependencies as well.

***

### skipNodeModulesBundle?

```ts
optional skipNodeModulesBundle: boolean;
```

Defined in: [src/features/deps.ts:66](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/deps.ts#L66)

Skip bundling all `node_modules` dependencies.

**Note:** This option cannot be used together with `alwaysBundle`.

#### Default

```ts
false
```
