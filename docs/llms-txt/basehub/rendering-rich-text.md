# Rendering Rich Text

> Fragments let you construct sets of fields, and then include them in queries where you need to.

The GraphQL API can return your Rich Text Blocks’ data in multiple formats:

1.  **Plain Text**, will ignore all formatting, media, and custom components, easy to render.
    
2.  **HTML**, will ignore custom components, easy to render.
    
3.  **Markdown**, will ignore custom components, needs a markdown to HTML parser to render.
    
4.  **JSON**, comes with everything, but needs something that understand and processes it.
    

In the case of the JSON format, the response will be an AST based on the [TipTap editor spec](https://tiptap.dev/docs/editor/guide/output#option-1-json). Because of the complexities associated with processing this JSON format, we’ve built a React Component called `<RichText />` that will help us render our Rich Text content. This is how it works:

```
import { Pump } from "basehub/react-pump"
import { RichText } from "basehub/react-rich-text"

const Page = async () => {
  return (
    <Pump
      queries={[
        {
          homepage: {
            subtitle: { 
              json: { 
                content: true,
              },
            },
          },
        },
      ]}
    >
      {async ([{ homepage }]) => {
        "use server"
        return <RichText>{homepage.subtitle.json.content}</RichText>
      }}
    </Pump>
  )
}

export default Page
```

## Component Overrides

When using the `<RichText />` component, you can simply pass the JSON content into it via `children`, and it’ll get rendered. If you want to use a custom handler for a certain HTML node (imagine using Next.js’ `<Image />` to render images), you’d use the `components` prop.

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
            components={{ 
              img: (props) => <Image {...props} />,
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

note:

`<RichText />` will return the HTML for each node of content, without any `<div>` wrapping everything nor any styles. We recommend using something like [Tailwind Typography](https://tailwindcss.com/docs/typography-plugin#installation) for quick prose styling, or of course, writing your own CSS.

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

We hope this removes a bit of friction from the sill tough task of rendering Rich Text data.

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