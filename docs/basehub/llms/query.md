# query

> The main method to consume data from your BaseHub repositories.

```
import { basehub } from 'basehub'

basehub().query({  })
```

When your token is setup, `basehub.query()` will query the data from the token’s repository. 

Inside the query object, you can pass any parameter that the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch) allows. That includes the [Next.js revalidate parameters](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnextrevalidate).

You can check out its usage in the [GraphiQL Explorer](https://docs.basehub.com/api-reference/graphql-api/explorer) linked to your schema.

Our `<Pump/>` [component](https://docs.basehub.com/api-reference/javascript-sdk/react/pump-component) uses `basehub.query()` behind the scenes to retrieve the data, that’s way its props are so similar. The great advantage `<Pump/>` has it’s that it will stream your updates in real time while on draft mode.

## Examples

Let’s see some common query patterns. Remember, the specific query keys you use will depend on your repository's structure, not on static API definitions.

### Get a document block

```
basehub().query({
  homepage: {
    title: true,
    description: {
      json: { content: true },
    },
  },
})
```

### Get a list of posts

```
basehub().query({
  posts: {
    items: {
      _id: true,
      _title: true,
      _slug: true,
      // more fields here...
    },
  },
})
```

### Get the first item in a list

```
basehub().query({
  posts: {
    __args: { first: 1 },
    items: {
      _id: true,
      _title: true,
      _slug: true,
      // more fields here...
    },
  },
})
```

### Filter by `_slug`

```
basehub().query({
  posts: {
    __args: {
      first: 1,
      filter: { _sys_slug: "your-post-slug" },
    },
    items: {
      _id: true,
      _title: true,
      _slug: true,
      // more fields here...
    },
  },
})
```

### Order by created date

```
basehub().query({
  posts: {
    __args: {
      orderBy: "_sys_createdAt__DESC",
    },
    items: {
      _id: true,
      _title: true,
      _slug: true,
      // more fields here...
    },
  },
})
```

### Create and use a fragment

```
import { basehub, fragmentOn } from "basehub"

const buttonFragment = fragmentOn("ButtonComponent", {
  label: true,
  href: true,
  variant: true,
})

basehub().query({
  homepage: {
    title: true,
    description: {
      json: { content: true },
    },
    cta: buttonFragment,
  },
})
```

### Query a union

```
basehub().query({
  dynamicPages: {
    items: {
      pathname: true,
      sections: { 
        __typename: true, // required
        on_HeroSectionComponent: {          
          title: true,
          subtitle: true,
          // more fields
        },
        on_FeatureSectionComponent: {          
          title: true,
          subtitle: true,
          // more fields
        },
      },
    },
  },
})
```