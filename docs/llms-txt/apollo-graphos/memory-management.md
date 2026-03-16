# Source: https://www.apollographql.com/docs/react/caching/memory-management.md

# Memory management

## Cache Sizes

For better performance, Apollo Client caches (or, in other words, memoizes) many
internally calculated values.
In most cases, these values are cached in [weak caches](https://en.wikipedia.org/wiki/Weak_reference), which means that if the
source object is garbage-collected, the cached value will be garbage-collected,
too.

These caches are also Least Recently Used (LRU) caches, meaning that if the cache is full,
the least recently used value will be garbage-collected.

Depending on your application, you might want to tweak the cache size to fit your
needs.

You can set your cache size [before (recommended)](https://www.apollographql.com/docs/react/caching/memory-management.md#setting-cache-sizes-before-loading-the-apollo-client-library) or [after](https://www.apollographql.com/docs/react/caching/memory-management.md#adjusting-cache-sizes-after-loading-the-apollo-client-library) loading the Apollo Client library.

### Setting cache sizes before loading the Apollo Client library

Setting cache sizes before loading the Apollo Client library is recommended because some caches are already initialized when the library is loaded. Changed cache sizes only
affect caches created after the fact, so you'd have to write additional runtime code to recreate these caches after changing their size.

```ts
import type { CacheSizes } from "@apollo/client/utilities";

globalThis[Symbol.for("apollo.cacheSize")] = {
  parser: 100,
  "fragmentRegistry.lookup": 500,
} satisfies Partial<CacheSizes>;
```

### Adjusting cache sizes after loading the Apollo Client library

You can also adjust cache sizes after loading the library.

```js
import { cacheSizes } from "@apollo/client/utilities";
import { print } from "@apollo/client";

cacheSizes.print = 100;
// cache sizes changed this way will only take effect for caches
// created after the cache size has been changed, so we need to
// reset the cache for it to be effective

print.reset();
```

### Choosing appropriate cache sizes

All configurable caches hold memoized values. If an item is cache-collected, it incurs only a small performance impact and doesn't cause data loss. A smaller cache size might save you memory.

You should choose cache sizes appropriate for storing a reasonable number of values rather than every value. To prevent too much recalculation, choose cache sizes that are at least large enough to hold memoized values for all hooks/queries on the screen at any given time.

To choose good sizes for our memoization caches, you need to know what they
use as source values, and have a general understanding of the data flow inside of
Apollo Client.

For most memoized values, the source value is a parsed GraphQL document—
a `DocumentNode`. There are two types:

* **User-supplied `DocumentNode`s** are created
  by the user, for example by using the `gql` template literal tag.
  This is the `QUERY`, `MUTATION`, or `SUBSCRIPTION` argument passed
  into a [`useQuery` hook](https://www.apollographql.com/docs/react/data/queries/#usequery-api) or as the `query` option to `client.query`.
* **Transformed `DocumentNode`s** are derived from
  user-supplied `DocumentNode`s, for example, by applying [`DocumentTransform`s](https://www.apollographql.com/docs/react/data/document-transforms/) to them.

As a rule of thumb, you should set the cache sizes for caches using a transformed
`DocumentNode` at least to the same size as for caches using a user-supplied
`DocumentNode`. If your application uses a custom `DocumentTransform` that does
not always transform the same input to the same output, you should set the cache
size for caches using a Transformed `DocumentNode` to a higher value than for
caches using a user-supplied `DocumentNode`.

By default, Apollo Client uses a base value of 1000 cached objects for caches using
user-supplied `DocumentNode` instances, and scales other cache sizes relative
to that. For example, the default base value of 1000 for user-provided `DocumentNode`s would scale to 2000, 4000, etc. for transformed `DocumentNode`s, depending on the transformation performed.

This base value should be plenty for most applications, but you can tweak them if you have different requirements.

#### Measuring cache usage

Since estimating appropriate cache sizes for your application can be hard, Apollo Client
exposes an API for cache usage measurement.
This way, you can click around in your application and then take a look at the
actual usage of the memoizing caches.

Keep in mind that this API is primarily meant for usage with the Apollo DevTools
(an integration is coming soon), and the API may change at any
point in time.
It is also only included in development builds, not in production builds.

The cache usage API is only meant for manual measurements. Don't rely on it in production code or tests.

TypeScript

```
 console.log(client.getMemoryInternals());
```

Logs output in the following JSON format:

Read more...

JSON

```
 {
   "limits": {
     "canonicalStringify": 1000,
     "print": 2000,
     "documentTransform.cache": 2000,
     "queryManager.getDocumentInfo": 2000,
     "PersistedQueryLink.persistedQueryHashes": 2000,
     "fragmentRegistry.transform": 2000,
     "fragmentRegistry.lookup": 1000,
     "fragmentRegistry.findFragmentSpreads": 4000,
     "cache.fragmentQueryDocuments": 1000,
     "removeTypenameFromVariables.getVariableDefinitions": 2000,
     "inMemoryCache.maybeBroadcastWatch": 5000,
     "inMemoryCache.executeSelectionSet": 10000,
     "inMemoryCache.executeSubSelectedArray": 5000
   },
   "sizes": {
     "canonicalStringify": 4,
     "print": 14,
     "addTypenameDocumentTransform": [
       {
         "cache": 14
       }
     ],
     "queryManager": {
       "getDocumentInfo": 14,
       "documentTransforms": [
         {
           "cache": 14
         },
         {
           "cache": 14
         }
       ]
     },
     "fragmentRegistry": {
       "findFragmentSpreads": 34,
       "lookup": 20,
       "transform": 14
     },
     "cache": {
       "fragmentQueryDocuments": 22
     },
     "inMemoryCache": {
       "executeSelectionSet": 4345,
       "executeSubSelectedArray": 1206,
       "maybeBroadcastWatch": 32
     },
     "links": [
       {
         "PersistedQueryLink": {
           "persistedQueryHashes": 14
         }
       },
       {
         "removeTypenameFromVariables": {
           "getVariableDefinitions": 14
         }
       }
     ]
   }
 }
```

### Cache options

###### [`"cache.fragmentQueryDocuments"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22cache.fragmentquerydocuments%22)

`number`

Cache size for the `getFragmentDoc` method of [`ApolloCache`](https://github.com/apollographql/apollo-client/blob/main/src/cache/core/cache.ts).

This function is called with user-provided fragment definitions.

Read more...

This function is called from `readFragment` with user-provided fragment definitions.

###### [`"documentTransform.cache"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22documenttransform.cache%22)

`number`

Cache size for the cache of [`DocumentTransform`](https://github.com/apollographql/apollo-client/blob/main/src/utilities/graphql/DocumentTransform.ts) instances with the `cache` option set to `true`.

Can be called with user-defined or already-transformed `DocumentNode`s.

Read more...

The cache size here should be chosen with other `DocumentTransform`s in mind. For example, if there was a `DocumentTransform` that would take `x` `DocumentNode`s, and returned a differently-transformed `DocumentNode` depending if the app is online or offline, then we assume that the cache returns `2*x` documents. If that were concatenated with another `DocumentTransform` that would also duplicate the cache size, you'd need to account for `4*x` documents returned by the second transform.

Due to an implementation detail of Apollo Client, if you use custom document transforms you should always add `n` (the "base" number of user-provided Documents) to the resulting cache size.

If we assume that the user-provided transforms receive `n` documents and return `n` documents, the cache size should be `2*n`.

If we assume that the chain of user-provided transforms receive `n` documents and return `4*n` documents, the cache size should be `5*n`.

This size should also then be used in every other cache that mentions that it operates on a "transformed" `DocumentNode`.

###### [`"fragmentRegistry.findFragmentSpreads"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22fragmentregistry.findfragmentspreads%22)

`number`

Cache size for the `findFragmentSpreads` method of [`FragmentRegistry`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/fragmentRegistry.ts).

This function is called with transformed `DocumentNode`s, as well as recursively with every fragment spread referenced within that, or a fragment referenced by a fragment spread.

Read more...

Note: This function is a dependency of `fragmentRegistry.transform`, so having too small of cache size here might involuntarily invalidate values in the `transform` cache.

###### [`"fragmentRegistry.lookup"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22fragmentregistry.lookup%22)

`number`

A cache inside of [`FragmentRegistry`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/fragmentRegistry.ts).

This function is called with fragment names in the form of a string.

Read more...

The size of this case should be chosen with the number of fragments in your application in mind.

Note: This function is a dependency of `fragmentRegistry.transform`, so having too small of a cache size here might involuntarily invalidate values in the `transform` cache.

###### [`"fragmentRegistry.transform"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22fragmentregistry.transform%22)

`number`

A cache inside of [`FragmentRegistry`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/fragmentRegistry.ts).

Can be called with user-defined or already-transformed `DocumentNode`s.

###### [`"inMemoryCache.executeSelectionSet"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22inmemorycache.executeselectionset%22)

`number`

Cache size for the `executeSelectionSet` method on [`StoreReader`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/readFromStore.ts).

Read more...

Every object that is read from the cache will be cached here, so it is recommended to set this to a high value.

###### [`"inMemoryCache.executeSubSelectedArray"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22inmemorycache.executesubselectedarray%22)

`number`

Cache size for the `executeSubSelectedArray` method on [`StoreReader`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/readFromStore.ts).

Read more...

Every array that is read from the cache will be cached here, so it is recommended to set this to a high value.

###### [`"inMemoryCache.maybeBroadcastWatch"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22inmemorycache.maybebroadcastwatch%22)

`number`

Cache size for the `maybeBroadcastWatch` method on [`InMemoryCache`](https://github.com/apollographql/apollo-client/blob/main/src/cache/inmemory/inMemoryCache.ts).

Read more...

This method is used for dependency tracking in the `InMemoryCache` and prevents from unnecessary re-renders. It is recommended to keep this value significantly higher than the number of possible subscribers you will have active at the same time in your application at any time.

###### [`"PersistedQueryLink.persistedQueryHashes"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22persistedquerylink.persistedqueryhashes%22)

`number`

A cache inside of [`PersistedQueryLink`](https://github.com/apollographql/apollo-client/blob/main/src/link/persisted-queries/index.ts).

It is called with transformed `DocumentNode`s.

Read more...

This cache is used to cache the hashes of persisted queries.

###### [`"queryManager.getDocumentInfo"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22querymanager.getdocumentinfo%22)

`number`

A cache inside of [`QueryManager`](https://github.com/apollographql/apollo-client/blob/main/src/core/QueryManager.ts).

It is called with transformed `DocumentNode`s.

###### [`"removeTypenameFromVariables.getVariableDefinitions"`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-%22removetypenamefromvariables.getvariabledefinitions%22)

`number`

Cache used in [`removeTypenameFromVariables`](https://github.com/apollographql/apollo-client/blob/main/src/link/remove-typename/removeTypenameFromVariables.ts).

This function is called transformed `DocumentNode`s.

###### [`canonicalStringify`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-canonicalstringify)

`number`

Cache used by [`canonicalStringify`](https://github.com/apollographql/apollo-client/blob/main/src/utilities/common/canonicalStringify.ts).

Read more...

This cache contains the sorted keys of objects that are stringified by `canonicalStringify`. It uses the stringified unsorted keys of objects as keys. The cache will not grow beyond the size of different object **shapes** encountered in an application, no matter how much actual data gets stringified.

###### [`checkDocument`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-checkdocument)

`number`

Used by the internal `checkDocument` that traverses GraphQL documents and throws an error if the document is invalid. if they are not valid.

###### [`print`](https://www.apollographql.com/docs/react/caching/memory-management.md#cachesizes-interface-print)

`number`

Cache size for the [`print`](https://github.com/apollographql/apollo-client/blob/main/src/utilities/graphql/print.ts) function.

It is called with transformed `DocumentNode`s.

Read more...

This method is called to transform a GraphQL query AST parsed by `gql` back into a GraphQL string.
