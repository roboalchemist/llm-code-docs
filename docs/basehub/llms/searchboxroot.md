# <SearchBox.Root />

> The Search wrapper works as a provider and comes with some optional props that can come in handy.

```
import { SearchBox } from 'basehub/react-search'

// -> SearchBox.Root
```

## Props

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`search`

`UseSearchResult`

**Required.** The search client generated with [useSearch](https://docs.basehub.com/api-reference/javascript-sdk/react/search/usesearch).

`onHitSelect`

`(hit: Hit) => void`

Optional callback triggered on any hit selection.

## Examples

*   Documentation: [Step by step](https://docs.basehub.com/extras/search#building-the-frontend)
    
*   Also you can check out our search implementation for this Documentation template [on Github](https://github.com/basehub-ai/nextjs-docs/blob/main/app/_components/header/search/index.tsx)