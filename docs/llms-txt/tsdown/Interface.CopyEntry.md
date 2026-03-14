# Source: https://tsdown.dev/reference/api/Interface.CopyEntry.md

---
url: /reference/api/Interface.CopyEntry.md
---
# Interface: CopyEntry

Defined in: [src/features/copy.ts:8](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L8)

## Properties

### flatten?

```ts
optional flatten: boolean;
```

Defined in: [src/features/copy.ts:23](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L23)

Whether to flatten the copied files (not preserving directory structure).

#### Default

```ts
true
```

***

### from

```ts
from: string | string[];
```

Defined in: [src/features/copy.ts:12](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L12)

Source path or glob pattern.

***

### rename?

```ts
optional rename: string | (name, extension, fullPath) => string;
```

Defined in: [src/features/copy.ts:32](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L32)

Change destination file or folder name.

***

### to?

```ts
optional to: string;
```

Defined in: [src/features/copy.ts:17](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L17)

Destination path.
If not specified, defaults to the output directory ("outDir").

***

### verbose?

```ts
optional verbose: boolean;
```

Defined in: [src/features/copy.ts:28](https://github.com/rolldown/tsdown/blob/ab8446b3f531fbd1b751ef53b3be7c3ec85eec35/src/features/copy.ts#L28)

Output copied items to console.

#### Default

```ts
false
```
