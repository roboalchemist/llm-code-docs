# Source: https://tsdown.dev/reference/api/Interface.SeaConfig.md

---
url: /reference/api/Interface.SeaConfig.md
---
# Interface: SeaConfig

Defined in: [src/features/exe.ts:35](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L35)

See also [Node.js SEA Documentation](https://nodejs.org/api/single-executable-applications.html#generating-single-executable-applications-with---build-sea)

Note some default values are different from Node.js defaults to optimize for typical use cases (e.g. disabling experimental warning, enabling code cache). These can be overridden.

## Properties

### assets?

```ts
optional assets: Record<string, string>;
```

Defined in: [src/features/exe.ts:50](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L50)

***

### disableExperimentalSEAWarning?

```ts
optional disableExperimentalSEAWarning: boolean;
```

Defined in: [src/features/exe.ts:42](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L42)

#### Default

```ts
true
```

***

### execArgv?

```ts
optional execArgv: string[];
```

Defined in: [src/features/exe.ts:47](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L47)

***

### execArgvExtension?

```ts
optional execArgvExtension: "env" | "none" | "cli";
```

Defined in: [src/features/exe.ts:49](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L49)

#### Default

```ts
'env'
```

***

### executable?

```ts
optional executable: string;
```

Defined in: [src/features/exe.ts:38](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L38)

Optional, if not specified, uses the current Node.js binary

***

### main?

```ts
optional main: string;
```

Defined in: [src/features/exe.ts:36](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L36)

***

### mainFormat?

```ts
optional mainFormat: "commonjs" | "module";
```

Defined in: [src/features/exe.ts:40](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L40)

***

### output?

```ts
optional output: string;
```

Defined in: [src/features/exe.ts:39](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L39)

***

### useCodeCache?

```ts
optional useCodeCache: boolean;
```

Defined in: [src/features/exe.ts:46](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L46)

#### Default

```ts
false
```

***

### useSnapshot?

```ts
optional useSnapshot: boolean;
```

Defined in: [src/features/exe.ts:44](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L44)

#### Default

```ts
false
```
