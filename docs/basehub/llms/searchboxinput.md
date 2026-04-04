# <SearchBox.Input />

> Extends the native HTML Input and consumes the search context in order to fetch hits from the indexed data.

```
import { SearchBox } from 'basehub/react-search'

// -> SearchBox.Input
```

## Props

The `<SearchBox.Input />` extends the native `HTMLInputProps`.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`asChild`

`boolean`

Passes all its configuration to the immediate child. It’s a requirement for this that it has only one children.

## Examples

*   Documentation: [Step by step](https://docs.basehub.com/extras/search#building-the-frontend)
    
*   Also you can check out our search implementation for this Documentation template [on Github](https://github.com/basehub-ai/nextjs-docs/blob/main/app/_components/header/search/index.tsx)