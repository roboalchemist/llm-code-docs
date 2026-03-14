# Source: https://tsdown.dev/reference/api/Interface.UnusedOptions.md

---
url: /reference/api/Interface.UnusedOptions.md
---
# Interface: UnusedOptions

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:5

## Properties

### depKinds?

```ts
optional depKinds: DepKind[];
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:22

#### Default

```ts
;['dependencies', 'peerDependencies']
```

***

### exclude?

```ts
optional exclude: FilterPattern;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:8

***

### ignore?

```ts
optional ignore: string[] | Partial<Record<DepKind, string[]>>;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:9

***

### include?

```ts
optional include: FilterPattern;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:7

***

### level?

```ts
optional level: "error" | "warning";
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:18

Specifies the severity level of the check.

* `'error'`: Causes the build to fail.
* `'warning'`: Displays a warning in the console.

#### Default

```ts
'warning'
```

***

### root?

```ts
optional root: string;
```

Defined in: node\_modules/.pnpm/unplugin-unused@0.5.7/node\_modules/unplugin-unused/dist/options-DC5dXKG8.d.mts:6
