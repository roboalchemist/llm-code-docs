# Source: https://tsdown.dev/reference/api/Interface.ReportOptions.md

---
url: /reference/api/Interface.ReportOptions.md
---
# Interface: ReportOptions

Defined in: [src/features/report.ts:30](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L30)

## Properties

### brotli?

```ts
optional brotli: boolean;
```

Defined in: [src/features/report.ts:45](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L45)

Enable/disable brotli-compressed size reporting.
Compressing large output files can be slow, so disabling this may increase build performance for large projects.

#### Default

```ts
false
```

***

### gzip?

```ts
optional gzip: boolean;
```

Defined in: [src/features/report.ts:37](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L37)

Enable/disable gzip-compressed size reporting.
Compressing large output files can be slow, so disabling this may increase build performance for large projects.

#### Default

```ts
true
```

***

### maxCompressSize?

```ts
optional maxCompressSize: number;
```

Defined in: [src/features/report.ts:51](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/report.ts#L51)

Skip reporting compressed size for files larger than this size.

#### Default

```ts
1_000_000 // 1MB
```
