# <CodeBlock />

> Easy-to-use component for rendering great code snippets.

```
import { CodeBlock } from 'basehub/react-code-block'
```

There are many syntax highlighting libraries in the JavaScript ecosystem. While this is a good thing, it can be exhausting for developers to shop for the right one. Prism, highlight.js, and Shiki are the most popular ones—an, in our opinion, Shiki is the best.

After building multiple websites with syntax highlighting, we’ve found ourselves copy-pasting a bunch of code and needing to re-read documentation over and over again. This is why we’ve built this.

## Props

These are the props supported by `<CodeBlock />`

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Type

Description

`snippets`

`Node[]`

**Required.** The JSON formatted content from the BaseHub RichText field. Accesible via `…json.content`

`theme`

`Blocks[]`

The list of blocks present in the content. Accesible via `…json.blocks`

`childrenTop`

`Handlers`

Custom handlers for native elements (such as `h1`, `p`, `img`) or custom components (using the component API Typename)

## Basic Usage

```
import { CodeBlock } from 'basehub/react-code-block'

const Post = () => {
  return (
    <CodeBlock
      theme="github-dark"
      snippets={[{ code: `const hello = "world"`, lang: 'js' }]}
    />
  )
}
```

## CSS Theme

```
import { CodeBlock } from 'basehub/react-code-block'

const Post = () => {
  return (
    <CodeBlock
      theme="github-dark"
      snippets={[{ code: `const hello = "world"`, lang: 'js' }]}
    />
  )
}
```

## Examples

*   From our docs: [https://github.com/basehub-ai/docs-template/blob/main/app/\_components/article/code-snippet/index.tsx#L21](https://github.com/basehub-ai/docs-template/blob/main/app/_components/article/code-snippet/index.tsx#L21)
    
*   From the marketing website template: [https://github.com/basehub-ai/marketing-website-template/blob/main/src/app/\_components/code-snippet/index.tsx](https://github.com/basehub-ai/marketing-website-template/blob/main/src/app/_components/code-snippet/index.tsx)