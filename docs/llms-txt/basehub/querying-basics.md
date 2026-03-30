# Querying Basics

> Learn how to build GraphQL queries with the generated client.

When you run `basehub`, you’ll be generating a GraphQL Client. What’s unique about this GraphQL client is that you’ll be defining the queries within your `.{js,ts}` files, instead of within `.graphql` ones. Most importantly, the output of your queries will be fully type safe.

Getting runtime type safety is a huge DX boost.

info:

Under the hood, we use [https://genql.dev/](https://genql.dev/), so make sure you check out that project out. If you want to see how a GraphQL query converts to a GenQL query, you can [check out their converter tool](https://genql.dev/converter).

## `basehub()`

This function let’s you fire off a single, direct query. Because of this, it’s perfect for **querying content that you don’t need to render**, like when defining `generateStaticParams` within a [dynamic Next.js page](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes).

```
import { basehub } from "basehub"

export const generateStaticParams = async () => {
  const { posts } = await basehub().query({
    posts: { items: { _slug: true } },
  })

  return posts.items.map((p) => {
    return { slug: p._slug }
  })
}
```

## `<Pump />`

Pump can subscribe to realtime changes from your dashboard, and re-compute the JSX so that you can have a Fast Refresh-like experience. Because of this, Pump is ideal for querying content that you’ll want to render—for example, titles, images, rich texts, etc.

```
import { Pump } from "basehub/react-pump"
import { draftMode } from "next/headers"

const Page = async () => {
  return (
    <Pump queries={[{ _sys: { id: true } }]}>
      {async ([data]) => {
        "use server"

        return (
          <pre>
            <code>{JSON.stringify(data, null, 2)}</code>
          </pre>
        )
      }}
    </Pump>
  )
}

export default Page
```

note:

Under the hood, Pump uses basehub() as its client. You can think of Pump is an abstraction over the more primitive basehub(), that helps you get that realtime editing experience.

With these two ways of querying in mind, let’s explore how to build our queries.

## Anatomy of a Query

Queries are JavaScript objects, where each key represents a key in the GraphQL schema, and the value is a boolean which decides weather you want to retrieve that key or not. Let’s take this query as an example:

```
import { basehub } from "basehub"

basehub().query({
  _sys: {
    id: true,
  },
  homepage: {
    title: true,
  },
  posts: {
    items: {
      _id: true,
      _slug: true,
      _title: true,
      publishedAt: true,
    },
  },
})
```

This query above will return the following result:

GraphQL Output

```
query {
  _sys {
    id
  }
  homepage {
    title
  }
  posts {
    items {
      _id
      _slug
      _title
      publishedAt
    }
  }
}
```

As you can see, GraphQL and TypeScript are not _that different_, and this is what our client is taking advantage of.

### Passing arguments

You can pass down arguments with `__args`:

```
import { basehub } from "basehub"

basehub().query({
  posts: {
    __args: { 
      filter: { 
        _sys_slug: { eq: "my-post-slug" },
      },
    },
    items: {
      _id: true,
      _slug: true,
      _title: true,
      publishedAt: true,
    },
  },
})
```

### Fragmenting

Fragments are very useful to define data dependencies inside your application. To define a fragment with our SDK, you’ll use `fragmentOn`:

```
import { basehub, fragmentOn } from "basehub"

export const PostFragment = fragmentOn("PostItem", {
  _id: true,
  _slug: true,
  _title: true,
  publishedAt: true,
})

// you can use it as a type as well
export type PostFragment = fragmentOn.infer<typeof PostFragment>

basehub().query({
  posts: {
    __args: {
      filter: {
        _sys_slug: { eq: "my-post-slug" },
      },
    },
    items: {
      _id: true,
      _slug: true,
      _title: true,
      publishedAt: true,
      ...PostFragment
    },
  },
})
```

#### Co-Locating Components with Their Data Dependency

A common pattern we enjoy using revolves around components defining thier own data dependencies. This works great with fragments, as we can easily define a fragment alongside a component and have it all be type safe.

```
// Let's imagine a Callout component:

import { fragmentOn } from "basehub"
import { RichText } from "basehub/react-rich-text"

export const CalloutFragment = fragmentOn("CalloutComponent", {
  _id: true,
  emoji: true,
  body: { json: { content: true } },
})

export const Callout = ({
  data,
}: {
  data: fragmentOn.infer<typeof CalloutFragment>
}) => {
  return (
    <div>
      <span>{data.emoji}</span>
      <RichText>{data.body.json.content}</RichText>
    </div>
  )
}
```

Then you could use this `CalloutFragment` paired with `<Callout />` , all type safe and with the data dependency co-located. If you update your Callout component and require more data from BaseHub, you can update the fragment and you’ll instantly get the data coming via props.

### Not Supported: Aliases

Aliases are a very useful GraphQL feature, which unfortunately is not currently supported. If you need this feature, contact us to help us prioritize.