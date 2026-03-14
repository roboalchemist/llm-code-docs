# Source: https://tsdown.dev/reference/api/Interface.ExeOptions.md

---
url: /reference/api/Interface.ExeOptions.md
---
# Interface: ExeOptions

Defined in: [src/features/exe.ts:16](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L16)

## Extends

* `ExeExtensionOptions`

## Properties

### fileName?

```ts
optional fileName: string | (chunk) => string;
```

Defined in: [src/features/exe.ts:22](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L22)

Output file name without any suffix or extension.
For example, do not include `.exe`, platform suffixes, or architecture suffixes.

***

### outDir?

```ts
optional outDir: string;
```

Defined in: [src/features/exe.ts:27](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L27)

Output directory for executables.

#### Default

```ts
'build'
```

***

### seaConfig?

```ts
optional seaConfig: Omit<SeaConfig, "main" | "output" | "mainFormat">;
```

Defined in: [src/features/exe.ts:17](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/exe.ts#L17)

***

### targets?

```ts
optional targets: ExeTarget[];
```

Defined in: [packages/exe/src/platform.ts:41](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/packages/exe/src/platform.ts#L41)

Cross-platform targets for building executables.
Requires `@tsdown/exe` to be installed.
When specified, builds an executable for each target platform/arch combination.

#### Example

```ts
targets: [
  { platform: 'linux', arch: 'x64', nodeVersion: '25.7.0' },
  { platform: 'darwin', arch: 'arm64', nodeVersion: '25.7.0' },
  { platform: 'win', arch: 'x64', nodeVersion: '25.7.0' },
]
```

#### Inherited from

```ts
ExeExtensionOptions.targets
```
