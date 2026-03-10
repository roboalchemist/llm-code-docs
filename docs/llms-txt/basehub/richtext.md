# <RichText />

> Our official rich text renderer. Supports passing custom handlers for native html elements and BaseHub components.

```
import { RichText } from 'basehub/react-rich-text'
```

A React Component that understands Rich Text Blocks’ data model and helps you render them in your website. If used in frameworks that support server components, it can be used as a RSC and just render the final result in the client without sending all the bundle to the client.

## Props

These are the props supported by `<RichText />`

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Type

Description

`content`

`Node[]`

**Required.** The JSON formatted content from the BaseHub RichText field. Accesible via `…json.content`

`blocks`

`Blocks[]`

The list of blocks present in the content. Accesible via `…json.blocks`

`components`

`Handlers`

Custom handlers for native elements (such as `h1`, `p`, `img`) or custom components.

note:

When you provide the value for the `content` property, the RichText component will retrieve your schema types and give you type-safety and auto-complete for the `components` property.

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

The `<RichText />` component doesn’t come with styles. It's job is to render the html notes, but you'll need to add the styles yourself. This is intentional, as websites often vary a lot between typographies, colors, and sizes.

there are a couple ways to style a rich text:

1.  Use regular CSS
    
2.  Use the [tailwindcss-typography](https://github.com/tailwindlabs/tailwindcss-typography) plugin (recommended)
    
3.  Override each of the nodes with your own components
    

Moreover, all of these methods can be combined as you please.

### 1\. Just CSS

As an example:

components/post-body.module.css

```
.post-body > *:first-child {
  margin-top: 0;
}

.post-body > *:last-child {
  margin-bottom: 0;
}

.post-body p {
  margin-bottom: 1em;
}

.post-body h1 {
  font-size: 2em;
  margin: 1.5em 0 0.5em;
}

.post-body h2 {
  font-size: 1.8em;
  margin: 1.4em 0 0.4em;
}

.post-body h3 {
  font-size: 1.4em;
  margin: 1.3em 0 0.3em;
}

.post-body ul, 
.post-body ol {
  margin: 0 0 1em 1.5em;
}

.post-body li {
  margin-bottom: 0.5em;
}

.post-body img {
  max-width: 100%;
  height: auto;
  margin: 1em 0;
}

.post-body blockquote {
  border-left: 4px solid #ddd;
  padding-left: 1em;
  margin: 1em 0;
  font-style: italic;
  color: #666;
}

.post-body pre {
  background-color: #f4f4f4;
  padding: 1em;
  overflow-x: auto;
  margin: 1em 0;
}

.post-body code {
  background-color: #f4f4f4;
  padding: 0.2em 0.4em;
  border-radius: 3px;
}
```

### 2\. With tailwind-typography (recommended)

Assuming you’re already using tailwind, using the typography plugin is fairly simple.

```
pnpm i @tailwindcss/typography --save-dev
```

Then in `tailwind.config.js`

```
/** @type {import('tailwindcss').Config} */
module.exports = {
  theme: {
    // ...
  },
  plugins: [
    require('@tailwindcss/typography'),
    // ...
  ],
}
```

And finally, you’ll use the `prose` class in the wrapping `<div>`

```
import { RichText } from "basehub/react-rich-text"

const PostBody = (props) => {
  return (
    <div className="prose">
      <RichText {...props} />
    </div>
  )
}
```

### 3\. Overriding / Using your own design system

If you already have components to render quotes, headings, paragraphs, etc, you can easily use them like this:

```
import { RichText } from "basehub/react-rich-text"
import {
  Heading,
  Blockquote,
  Paragraph,
} from "@my-design-system"

const PostBody = (props) => {
  return (
    <div>
      <RichText
        {...props}
        components={{
          p: (props) => <Paragraph {...props} />,
          h1: (props) => <Heading {...props} level={1} />,
          h2: (props) => <Heading {...props} level={2} />,
          h3: (props) => <Heading {...props} level={3} />,
          blockquote: (props) => <Blockquote {...props} />,
          // rest...
        }}
      />
    </div>
  )
}
```

Example: [https://github.com/basehub-ai/docs-template/blob/main/app/\_components/article/index.tsx#L182](https://github.com/basehub-ai/docs-template/blob/main/app/_components/article/index.tsx#L182)

## Custom Components

If you are using [Custom Blocks in your Rich Text](https://basehub.com/changelog/instantiate-components-inside-rich-text-blocks), you’ll need to add them to your query, and pass them via the `blocks` prop. Then, you’ll be able to set up the custom renderers for them (in a type-safe manner, by the way):

```
import { Pump } from "basehub/react-pump"
import { RichText } from "basehub/react-rich-text"
import Image from "next/image"
import { Callout, CodeSnippet } from './path-to/components'

const Page = async () => {
  return (
    <Pump
      draft={draftMode().isEnabled}
      next={{ revalidate: 60 }}
      queries={[
        {
          homepage: {
            subtitle: {
              json: {
                content: true,
                blocks: { 
                  __typename: true,
                  on_CalloutComponent: { 
                    _id: true,
                    intent: true,
                    text: true,
                  },
                  on_CodeSnippetComponent: { 
                    _id: true,
                    code: { 
                      code: true,
                      language: true,
                    },
                    fileName: true,
                  },
                } 
              }
            },
          },
        },
      ]}
    >
      {async ([{ homepage }]) => {
        "use server"
        return (
          <RichText
            blocks={homepage.subtitle.json.blocks} 
            components={{
              img: (props) => <Image {...props} />,
              CalloutComponent: (props) => <Callout data={props}>,
              CodeSnippetComponent: (props) => <CodeSnippet data={props}>,
            }}
          >
            {homepage.subtitle.json.content}
          </RichText>
        )
      }}
    </Pump>
  )
}

export default Page
```

## Internal Links

Similar to external hyperlinks, internal links in your rich text let you reference other blocks in an easy and type-safe manner.

```
import { Pump } from "basehub/react-pump"
import { RichText } from "basehub/react-rich-text"
import Image from "next/image"

const Page = async () => {
  return (
    <Pump
      queries={[
        {
          homepage: {
            subtitle: {
              json: {
                content: true,
                blocks: { 
                  __typename: true,
                  on_PostComponent: { 
                    _slug: true,
                  },
                },
              },
            },
          },
        },
      ]}
    >
      {async ([{ homepage }]) => {
        "use server"
        return (
          <RichText
            blocks={homepage.subtitle.json.blocks} 
            components={{
              img: (props) => <Image {...props} />,
              a: ({ internal, ...props }) => { 
                if (internal) { 
                  switch (internal.__typename) { 
                    case "PostComponent": 
                      return ( 
                        <a {...props} href={`/blog/${internal._slug}`} /> 
                      )  
                    default: 
                      return null
                  } 
                } else return <a {...props} /> 
              },
            }}
          >
            {homepage.subtitle.json.content}
          </RichText>
        )
      }}
    </Pump>
  )
}

export default Page
```