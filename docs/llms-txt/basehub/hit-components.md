# Hit Components

> Use cases and APIReference for HitList, HitItem, HitSnippet

## <SearchBox.HitList /> Props

```
import { SearchBox } from 'basehub/react-search'

// -> SearchBox.HitList
```

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`asChild`

`boolean`

Passes all its configuration to the immediate child. It’s a requirement for this that it has only one children.

## <SearchBox.HitItem /> Props

```
import { SearchBox } from 'basehub/react-search'

// -> SearchBox.HitItem
```

The `<SearchBox.HitItem />` extends the native `HTMLDivProps`.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`asChild`

`boolean`

Passes all its configuration to the immediate child. It’s a requirement for this that it has only one children.

`hit`

`Hit`

The hit element from the search results.

`href`

`string`

The link to the hit result, can be any string, but most often than not, you will use the hit result to build the final URL.

check:

Both HitList and HitItem provide keyboard navigation out-of-the-box.

## <SearchBox.HitSnippet /> Props

```
import { SearchBox } from 'basehub/react-search'

// -> SearchBox.HitSnippet
```

The HitSnippet works as sugar syntax to render specific fields of the hit object with ease.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Key

Type

Description

`fieldPath`

`string`

**Required.** The specific field name in the hit object. e.g: `_title`

`fallbackFieldPaths`

`string[]`

If the `fieldPath` is `undefined` or doesn’t have a match with the query, you can provide a list of fallback paths to render in its place.

`components`

`{ container, mark, text }`

An optional set of react elements that can be passed to customize the final UI for the snippet.