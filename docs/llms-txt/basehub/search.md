# Search

> Learn how to add instant-search into your website.

BaseHub Search will help you create instant-search experiences _ala_ Algolia inside your website. There are two steps into building an awesome search experience:

1.  Indexing the content
    
2.  Building the frontend
    

BaseHub helps you with both of these tasks.

## Indexing the Content

BaseHub Search supports indexing blocks that are below [Components](https://docs.basehub.com/blocks/layout/component). By default, blocks won’t be indexed. To index a block, you’ll go to over to its Properties Panel and click on the “Index block“ toggle.

warning:

The “Index block” state is set in a Component, and will be inherited by the Instances. Make sure you go to a Component to toggle this state.

### Indexing Happens On Commit

In order for results to appear on your frontend, you’ll need to commit your changes. Toggling the “Index block” state is a “committable change.” Then, as you edit and add new content content, and commit, BaseHub Search will re-index and then your frontend will show the updated results.

## Building the Frontend

There are a couple of ways in which BaseHub helps you build your search frontend. First, you’ll needit exposes a `useSearch` hook to make the queries and manage state. Second, it exposes a `<SearchBox>` component that provides good UX defaults for you to render your search input, your results, and your highlights.

In order for all of this to work, you’ll first need to get a `_searchKey` from the GraphQL API, which is scoped to a specific Collection or Component.

![](https://assets.basehub.com/7b31fb4b/akjRW8Uqoh1mCPovvPzyX/cleanshot-2024-05-22-at-16.13.442x.png?width=3840&quality=90&format=auto)

Simplified graph of how the flow works.

Let’s imagine you have a Posts Collection and you want to build a frontend so search through it.

### Get a `_searchKey`

This is how you’ll get your `_searcKey`:

```
import { Pump } from "basehub/react-pump"
import { draftMode } from "next/headers"

const Page = async () => {
  return (
    <Pump
      next={{ revalidate: 30 }}
      draft={draftMode().isEnabled}
      queries={[
        {
          posts: {
            _searchKey: true,
            items: {
              _id: true,
              _title: true,
              // more post stuff...
            },
          },
        },
      ]}
    >
      {async ([data]) => {
        "use server"
        return (
          <>
            <Search _searchKey={data.posts._searchKey} />
            ...
          </>
        )
      }}
    </Pump>
  )
}

export default Page
```

### Build your `<Search>` component

You’re now ready to `useSearch` and `<SearchBox>` to build your UI.

```
'use client'
import { useSearch, SearchBox } from "basehub/react-search"

export const Search = ({
  _searchKey,
}: {
  _searchKey: string
}) => {
  const search = useSearch({
    _searchKey,
    queryBy: ["_title", "body", "excerpt"],
  })

  return (
    <SearchBox.Root search={search}>
      <SearchBox.Input />

      <SearchBox.Placeholder>
        Start typing to search.
      </SearchBox.Placeholder>

      <SearchBox.Empty>
        Nothing found for <b>{search.query}</b>
      </SearchBox.Empty>

      <SearchBox.HitList>
        {search.result?.hits.map((hit) => {
          return (
            <SearchBox.HitItem
              key={hit._key}
              hit={hit}
              href={`/blog/${hit.document._slug}`}
            >
              <SearchBox.HitSnippet fieldPath="_title" />
              <SearchBox.HitSnippet
                fieldPath="body"
                fallbackFieldPaths={["excerpt"]}
              />
            </SearchBox.HitItem>
          )
        })}
      </SearchBox.HitList>
    </SearchBox.Root>
  )
}
```

## Examples

1.  Simple, non real-world example
    
    *   GitHub Repo: [https://github.com/basehub-ai/nextjs-simple-search-example](https://github.com/basehub-ai/nextjs-simple-search-example/blob/main/app/page.tsx)
        
    *   BaseHub Repo: [https://basehub.com/basehub/simple-search-example](https://basehub.com/basehub/simple-search-example)
        
2.  Advanced example (the search that powers these docs)
    
    *   GitHub Repo: [https://github.com/basehub-ai/nextjs-docs](https://github.com/basehub-ai/nextjs-docs/blob/main/app/_components/header/search/index.tsx)
        
    *   BaseHub Repo: [https://basehub.com/basehub/docs](https://basehub.com/basehub/docs)
        

Watch JB integrate a search experience from scratch