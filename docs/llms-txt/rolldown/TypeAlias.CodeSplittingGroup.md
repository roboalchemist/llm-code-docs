# Source: https://rolldown.rs/reference/TypeAlias.CodeSplittingGroup.md

---
url: /reference/TypeAlias.CodeSplittingGroup.md
---
# Type Alias: CodeSplittingGroup

* **Type**: { `entriesAware?`: `boolean`; `entriesAwareMergeThreshold?`: `number`; `maxModuleSize?`: `number`; `maxSize?`: `number`; `minModuleSize?`: `number`; `minShareCount?`: `number`; `minSize?`: `number`; `name`: `string` | [`CodeSplittingNameFunction`](TypeAlias.CodeSplittingNameFunction.md); `priority?`: `number`; `test?`: `StringOrRegExp` | (`id`) => `boolean` | `void` | `undefined`; }

## Properties

### entriesAware?

* **Type**: `boolean`
* **Optional**

When `false` (default), all matching modules are merged into a single chunk.
Every entry that uses any of these modules must load the entire chunk — even
modules it doesn't need.

When `true`, matching modules are grouped by which entries actually import them.
Modules shared by the same set of entries go into the same chunk, while modules
shared by a different set go into a separate chunk. This way, each entry only
loads the code it actually uses.

Example: entries A, B, C all match a `"vendor"` group.

* `moduleX` is used by A, B, C
* `moduleY` is used by A, B only

With `entriesAware: false` → one `vendor.js` chunk with both modules; C loads `moduleY` unnecessarily.
With `entriesAware: true`  → `vendor.js` (moduleX, loaded by all) + `vendor2.js` (moduleY, loaded by A and B only).

#### Default

```ts
false
```

***

### entriesAwareMergeThreshold?

* **Type**: `number`
* **Optional**

Size threshold in bytes for merging small `entriesAware` subgroups into the
closest neighboring subgroup.

This option only works when [`entriesAware`](#entriesaware)
is `true`. Set to `0` to disable subgroup merging.

#### Default

```ts
0
```

***

### maxModuleSize?

* **Type**: `number`
* **Optional**

Controls whether a module can only be captured if its size in bytes is smaller than or equal to this value.

#### Default

```ts
Infinity
```

***

### maxSize?

* **Type**: `number`
* **Optional**

If the accumulated size in bytes of the captured modules by this group is larger than this value, this group will be split into multiple groups that each has size close to this value.

#### Default

```ts
Infinity
```

***

### minModuleSize?

* **Type**: `number`
* **Optional**

Controls whether a module can only be captured if its size in bytes is larger than or equal to this value.

#### Default

```ts
0
```

***

### minShareCount?

* **Type**: `number`
* **Optional**

Controls if a module should be captured based on how many entry chunks reference it.

#### Default

```ts
1
```

***

### minSize?

* **Type**: `number`
* **Optional**

Minimum size in bytes of the desired chunk. If the accumulated size of the captured modules by this group is smaller than this value, it will be ignored. Modules in this group will fall back to the `automatic chunking` if they are not captured by any other group.

#### Default

```ts
0
```

***

### name

* **Type**: `string` | [`CodeSplittingNameFunction`](TypeAlias.CodeSplittingNameFunction.md)

Name of the group. It will be also used as the name of the chunk and replace the `[name]` placeholder in the [`output.chunkFileNames`](Interface.OutputOptions.md#chunkfilenames) option.

For example,

```js
import { defineConfig } from 'rolldown';

export default defineConfig({
  output: {
    codeSplitting: {
      groups: [
        {
          name: 'libs',
          test: /node_modules/,
        },
      ],
    },
  },
});
```

will create a chunk named `libs-[hash].js` in the end.

It's ok to have the same name for different groups. Rolldown will deduplicate the chunk names if necessary.

#### Dynamic `name()`

If `name` is a function, it will be called with the module id as the argument. The function should return a string or `null`. If it returns `null`, the module will be ignored by this group.

Notice, each returned new name will be treated as a separate group.

For example,

```js
import { defineConfig } from 'rolldown';

export default defineConfig({
  output: {
    codeSplitting: {
      groups: [
        {
          name: (moduleId) => moduleId.includes('node_modules') ? 'libs' : 'app',
          minSize: 100 * 1024,
        },
      ],
    },
  },
});
```

:::warning
Constraints like `minSize`, `maxSize`, etc. are applied separately for different names returned by the function.
:::

***

### priority?

* **Type**: `number`
* **Optional**

Priority of the group. Group with higher priority will be chosen first to match modules and create chunks. When converting the group to a chunk, modules of that group will be removed from other groups.

If two groups have the same priority, the group whose index is smaller will be chosen.

#### Example

```js
import { defineConfig } from 'rolldown';

export default defineConfig({
  output: {
    codeSplitting: {
      groups: [
        {
          name: 'react',
          test: /node_modules[\\/]react/,
          priority: 2,
        },
        {
          name: 'other-libs',
          test: /node_modules/,
          priority: 1,
        },
      ],
    },
  },
});
```

#### Default

```ts
0
```

***

### test?

* **Type**: `StringOrRegExp` | (`id`) => `boolean` | `void` | `undefined`
* **Optional**

Controls which modules are captured in this group.

* If `test` is a string, the module whose id contains the string will be captured.
* If `test` is a regular expression, the module whose id matches the regular expression will be captured.
* If `test` is a function, modules for which `test(id)` returns `true` will be captured.
* If `test` is empty, any module will be considered as matched.

:::warning
When using regular expression, it's recommended to use `[\\/]` to match the path separator instead of `/` to avoid potential issues on Windows.

* ✅ Recommended: `/node_modules[\\/]react/`
* ❌ Not recommended: `/node_modules/react/`
  :::
