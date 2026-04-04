# <Icon />

> A vector renderer for our icon block. Supports passing custom handlers for native svg elements.

```
import { Icon } from 'basehub/react-icon'
```

A React Component that understands Rich Text Blocks’ data model and helps you render them in your website. If used in frameworks that support server components, it can be used as a RSC and just render the final result in the client without sending all the bundle to the client.

## Props

These are the props supported by `<Icon />`

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Type

Description

`content`

`string`

**Required.** The content of the svg parsed as a string, following the return type from the BaseHub Icon block.

`components`

`Handlers`

Custom handlers for native svg elements (such as `path`, `rect`, `svg`).

## Example

```
import { Code, Heading, Link } from '@radix-ui/themes'
import NextLink from 'next/link'

export const ArticleBody = (props: ArticleFragment) => {
  return (
    <RichText
      content={props.content?.json.content}
      blocks={props.content?.json.blocks}
      components={{
        // native elements not present in this object will use the default handlers 
        h1: ({ children }) => (
          <Heading as="h1" size="3" weight="medium">
            {children}
          </Heading>
        ),
        h2: ({ children }) => (
          <Heading as="h2" size="2" weight="medium">
            {children}
          </Heading>
        ),
        h3: ({ children }) => (
          <Heading as="h3" size="2" weight="medium">
            {children}
          </Heading>
        ),
        a: ({ children, ...rest }) => (
          <Link asChild>
            <NextLink {...rest}>{children}</NextLink>
          </Link>
        ),
        // Custom component
        CodeSnippetComponent: ({ children, isInline }) => {
          if (!isInline) return null
          return <Code>{children}</Code>
        },
      }}
    />
  )
}
```

## Styling

The `<Icon />` component doesn’t come with styles. It's job is to render the block content as an svg element, but you'll need to add the styles yourself. You can either do so in your codebase, or in the svg you define in the Icon block at BaseHub.

there are a couple ways to style an icon:

1.  Use regular CSS
    
2.  Override each of the nodes with your own components
    

Moreover, all of these methods can be combined as you please.

### 1\. Just CSS

As an example:

sections/footer.module.css

```
.social-links {
  display: flex;
  gap: 6px;
  color: '#ededed';
  width: 24px;
  height: 24px;
}
```

### 2\. Overriding

In case you’re using tailwind, you can easily style them like this:

```
import { Icon } from "basehub/react-icon"

const PostBody = (props) => {
  return (
    <div>
      <Icon
        {...props}
        components={{
          svg: (props) => <svg {...props} className="size-6 text-gray/10" />,
          // rest...
        }}
      />
    </div>
  )
}
```