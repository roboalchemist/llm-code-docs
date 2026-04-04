# <Pump />

> A React Server Component that queries BaseHub and can subcribe to real time changes seamlessly.

```
import { Pump } from 'basehub/react-pump'
```

Pump is a React Server Component, meaning, it can only be used within frameworks that support RSC ([Next.js only for now](https://react.dev/learn/start-a-new-react-project#bleeding-edge-react-frameworks)).

The power of Pump comes when you use [Next.js Draft Mode](https://nextjs.org/docs/app/building-your-application/configuring/draft-mode) alongside it. Pump lets developers write their queries and rendering logic in a simple and typesafe way, and get “content fast refresh” (live preview) out of the box, without affecting the website’s performance in any way.

info:

If you’re interested in how this works under the hood, or the reason behind its syntax, you can [read our blog post about it](https://basehub.com/blog/pump).

## Props

These are the props supported by `<Pump />` .

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Type

Description

`queries`

`QueryType[]`

**Required.** An array of BaseHub queries that will be fetched from the BaseHub API asynchronously

`draft`

`boolean`

If enabled, it will fetch from the draft API, what consumes the WIP data.

`token`

`string`

Lets you pass a BaseHub token explicitly. Useful for frameworks in which `process.env.BASEHUB_TOKEN` is not available.

`signal`

`AbortSignal`

Inherited from the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

`next`

`NextFetchCache`

[Next.js only](https://nextjs.org/docs/app/api-reference/functions/fetch#optionsnextrevalidate). Let’s you configure the cache.

`cache`

`RequestCache`

Inherited from the [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch).

## Example

This query will get `_sys.id` from the API. Most importantly, when Next.js Draft Mode is enabled, it’ll subscribe to content changes in real time.

```
import { Pump } from "basehub/react-pump"
import { draftMode } from "next/headers"

const Page = () => {
  return (
    <Pump
      queries={[{ _sys: { id: true } }]}
      draft={draftMode().isEnabled}
      next={{ revalidate: 30 }}
    >
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