# Apollo Client Caching: Comprehensive Documentation

Source: https://www.apollographql.com/docs/react/caching/overview

## Overview

Apollo Client implements a sophisticated local caching mechanism through its `InMemoryCache`, which stores GraphQL query results in a "normalized, in-memory cache." This architecture enables rapid response to subsequent queries without network requests.

### Core Benefits

The caching system provides:
- **Immediate responses** to queries for already-cached data
- **Reduced network traffic** through intelligent cache reuse
- **Local state management** capabilities
- **Automatic data deduplication** via normalization

---

## How Data Storage Works

### Flat Lookup Table Architecture

Apollo Client organizes cached data as a flat lookup table of interconnected objects. While GraphQL responses often feature deeply nested structures, the cache flattens this hierarchy to optimize reads and updates.

**Example Response Structure:**
```json
{
  "data": {
    "person": {
      "__typename": "Person",
      "id": "cGVvcGxlOjE=",
      "name": "Luke Skywalker",
      "homeworld": {
        "__typename": "Planet",
        "id": "cGxhbmV0czox",
        "name": "Tatooine"
      }
    }
  }
}
```

This nested response contains two distinct objects that must be normalized before storage.

---

## Data Normalization Process

Normalization transforms nested response data into a flat, referenceable format through four steps:

### Step 1: Identify Objects

The cache recognizes all distinct objects in the response. From the example above, this includes:
- One `Person` object (id: `cGVvcGxlOjE=`)
- One `Planet` object (id: `cGxhbmV0czox`)

### Step 2: Generate Cache IDs

For each object identified, the cache generates a unique cache ID. The default format concatenates `__typename` and `id` (or `_id`) fields with a colon separator:

- `Person:cGVvcGxlOjE=`
- `Planet:cGxhbmV0czox`

**Note:** Objects lacking `id` or `_id` fields are cached directly within their parent, making the cache partially nested for those entries.

Custom cache ID formats can be configured for specific types.

### Step 3: Replace Object Fields with References

Nested object fields become reference pointers to their normalized counterparts:

**Before normalization:**
```json
{
  "__typename": "Person",
  "id": "cGVvcGxlOjE=",
  "name": "Luke Skywalker",
  "homeworld": {
    "__typename": "Planet",
    "id": "cGxhbmV0czox",
    "name": "Tatooine"
  }
}
```

**After normalization:**
```json
{
  "__typename": "Person",
  "id": "cGVvcGxlOjE=",
  "name": "Luke Skywalker",
  "homeworld": {
    "__ref": "Planet:cGxhbmV0czox"
  }
}
```

This approach enables multiple objects to reference the same cached entity without duplication.

### Step 4: Store Normalized Objects

Objects are deposited into the flat lookup table. When an incoming object shares a cache ID with an existing cached object, their fields merge according to these rules:

- **Incoming data overwrites** cached values for shared fields
- **Preserved fields** include those appearing in only the existing or only the incoming object

This merging strategy keeps local data synchronized as application state evolves.

---

## Practical Normalization Example

Consider a SWAPI API query:

```graphql
query {
  allPeople(first: 3) {
    people {
      id
      name
      homeworld {
        id
        name
      }
    }
  }
}
```

This returns three `Person` objects with corresponding `Planet` objects. If two people share the same homeworld, the cache stores only one `Planet` reference, with both people pointing to it via `__ref`.

**Result:**
- 3 cached `Person` objects
- 2 cached `Planet` objects (not 3, due to deduplication)
- Multiple references to the single shared planet instance

This normalization dramatically reduces memory usage and ensures consistency when planet data updates.

---

## Cache Visualization

The **Apollo Client Devtools** browser extension provides a Cache inspector displaying:
- All normalized objects in the cache
- Reference relationships between objects
- Individual field values and types
- Real-time cache state changes

This visual representation helps developers understand cache structure and debug caching behavior.

---

## Key Caching Features

### Automatic `__typename` Addition

Apollo Client automatically includes `__typename` fields in queries even when not explicitly requested. This enables the normalization process and type identification.

### Reference System

The `__ref` field notation indicates cache references:
```json
{"__ref": "TypeName:cacheId"}
```

### ROOT_QUERY Object

The cache maintains a special `ROOT_QUERY` object that tracks top-level query results and their relationships to normalized objects.

---

## Configuring Cache Behavior

Beyond default configuration, Apollo Client supports:

- **Custom cache ID formats** for specific object types
- **Field-level behavior customization** through field policies
- **Local-only fields** for client state management
- **Cache persistence** and hydration strategies
- **Garbage collection** and memory management

---

## Next Steps for Implementation

Developers should proceed to:

1. **Cache Configuration** — Learn specific configuration options for `InMemoryCache`
2. **Reading and Writing** — Master direct cache interaction patterns
3. **Local State Management** — Leverage the cache for application state
4. **Garbage Collection** — Understand automatic cleanup and eviction policies

---

## Summary

Apollo Client's normalization strategy transforms nested GraphQL responses into a flat, reference-based cache structure. This design optimizes query performance, reduces data duplication, and enables sophisticated local state management. Understanding normalization is fundamental to leveraging Apollo Client's caching capabilities effectively.
