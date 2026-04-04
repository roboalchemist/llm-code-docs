# Source: https://rolldown.rs/reference/Class.TsconfigCache.md

---
url: /reference/Class.TsconfigCache.md
---
# Class: TsconfigCache

Cache for tsconfig resolution to avoid redundant file system operations.

The cache stores resolved tsconfig configurations keyed by their file paths.
When transforming multiple files in the same project, tsconfig lookups are
deduplicated, improving performance.

## Constructors

### Constructor

* **Type**: () => `TsconfigCache`
* **Experimental**

Create a new transform cache with auto tsconfig discovery enabled.

#### Returns

`TsconfigCache`

## Methods

### clear()

* **Type**: () => `void`
* **Experimental**

Clear the cache.

Call this when tsconfig files have changed to ensure fresh resolution.

#### Returns

`void`

***

### size()

* **Type**: () => `number`
* **Experimental**

Get the number of cached entries.

#### Returns

`number`
