# useSearch

> A React hook that instantiates your Search Client.

```
import { useSearch } from 'basehub/react-search'
```

## Arguments

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`_searchKey`

`string`

**Required.** The search key from the block where you want to do search. The client will have access to all indexed fields under the corresponding block (and its instances in a case of a component).

`queryBy`

`string[]`

**Required.** An array with the field keys you want to search by.

`saveRecentSearches`

`SaveRecentSearches`

An object that accepts a `key` and a `getStorage` callback. Useful when you want to save recent searches into localStorage or similar.

info:

BaseHub Search uses [TypeSense](https://typesense.org/) on the background. **You can check out all the search options on their** [**documentation**](https://typesense.org/docs/26.0/api/search.html#search)**.** Keep in mind that they’re all on _camelCase_ in the `useSearch` hook. E.g: `filter_by` is listed as `filterBy`.

## Examples

*   Documentation: [Step by step](https://docs.basehub.com/extras/search#building-the-frontend)
    
*   Also you can check out our search implementation for this Documentation template [on GitHub](https://github.com/basehub-ai/nextjs-docs/blob/main/app/_components/header/search/index.tsx)