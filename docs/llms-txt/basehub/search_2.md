# search

> Core method to perform a search query.

```
import { search } from 'basehub/search'
```

info:

Using React? Check out our [React helpers right here](https://docs.basehub.com/api-reference/javascript-sdk/react/search).

## Arguments

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`_searchKey`

`string | null`

The search key (comes from the GraphQL API).

`query`

`string`

The query (typically comes from user input).

`options`

`SearchOptions`

Stuff like `queryBy`, `filterBy`, and more.