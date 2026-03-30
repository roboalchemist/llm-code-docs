# Environments & Caching

> Understand the different environments and caching strategies you can leverage to improve your content editing experience.

## Environments

Setting up your application so that it handles all of the environments in a seamless fashion is a very important part of integrating with BaseHub.

### Local Environment

When developing in localhost, you’ll be writing new code and iterating over your content. This means adding new blocks, changing those blocks’ constraints, writing content and more—all at the same time.

In order to _not break your flow_, you’ll want two things:

1.  For the schema in BaseHub to be in sync with your IDE, and
    
2.  For the content to update as you write, without needing to commit it yet.
    

We bundled these two needs into one command:

```
basehub dev
```

This command generates the type-safe SDK and keeps it in sync with changes you make in basehub.com (this is called `--watch` mode); and also sets up the SDK so that it queries Draft content from your repository.

This is why we recommend you run it _in parallel_ to `next dev`.

```
"scripts": {
  "dev": "basehub dev & next dev",
  "build": "basehub && next build",
  "start": "next start",
  "lint": "next lint"
},
```

_Notice the single_ `&`_._

### Preview Environment

Setting up an easy way for editors to preview content before committing it into production is essential. We’ve designed our preview workflow with these three pillars in mind:

1.  Content should render in real time, as you write.
    
2.  Preview should be easy for developers to integrate.
    
3.  The integration should never degrade production performance _in any way_.
    

We achieve this is by using a couple of BaseHub components, `<Pump />` and `<Toolbar />`, in combination to Next.js’ `draftMode`. Additionally, to bridge the gap between basehub.com (the dashboard) and your website, you’ll need to set up the “Preview” Button.

\[data-radix-scroll-area-viewport\]{scrollbar-width:none;-ms-overflow-style:none;-webkit-overflow-scrolling:touch;}\[data-radix-scroll-area-viewport\]::-webkit-scrollbar{display:none}

Name

Description

Author

`<Pump />`

Queries the API. Receives a `draft` prop that controls weather it’ll hit draft content and subscribe to real time changes, or just hit production.

BaseHub

`draftMode`

Allows you to detect Draft Mode inside a Server Component.

Next.js

`<Toolbar />`

Helper to turn on/off Draft Mode within your site, with zero-config.

BaseHub

Preview Button

Links from a BaseHub block into where that block is being rendered in your website.

BaseHub

This is how a simple code example can look like:

app/layout.tsx

```
import { Toolbar } from 'basehub/next-toolbar'

export default function RootLayout({
  children,
}: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        <main>{children}</main>
        <Toolbar />
      </body>
    </html>
  )
}
```

Finally, we need to set up our Preview Buttons.

See how to set up Preview Buttons, and the whole preview environment really.

### Production Environment

Once we’ve set up Local and Preview environments, most of the hard work is done. The only thing you need to make sure when going to production is for the SDK to be generated before the build step of your application.

```
"scripts": {
  "dev": "basehub dev & next dev",
  "build": "basehub && next build",
  "start": "next start",
  "lint": "next lint"
},
```

That should be it. You’re ready to deploy your website.

warning:

Using [Turborepo](https://turbo.build/repo) or a similar monorepo manager? You need to add `.basehub` to `turbo.json`'s build outputs, so it can keep track of schema changes.

```
"tasks": {
    "build": {
      "outputs": [".basehub/**"]  
    },
  }
```

## Caching

By default, [Next.js will try to cache all of our requests made with](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#opting-out-of-data-caching) `fetch`—and that includes BaseHub. While this makes subsequent requests to BaseHub much faster, it’ll essentially make your website’s content fully static, instead of reflecting the latest content changes from your BaseHub Repo.

This introduces a new task for the developer, which is to purge that cache when content from BaseHub changes. These are some of the options you have:

### On-Demand Revalidation (Recommended)

The absolute best method of revalidation is “on-demand”. As its name implies, it consists of purging the cached data at the exact moment a change occurs. This provides the best experience for editors, as they won’t need to refresh the website for several seconds to see their content live; and also keeps server costs down, as the server itself won’t need to constantly check with our API to see if something has changed.

BaseHub provides automatic on-demand revalidation in a fine-grained manner.

*   Automatic: without the need of constant developer setup.
    
*   Fine-grained: with every query being revalidated individually—in contrast to an “all or nothing” approach.
    

This is how:

### Mount the <Toolbar /> in `layout.tsx`

This will add a Server Action to revalidate the specific tags `basehub()` will set to each query.

```
// app/layout.tsx
import { Toolbar } from "basehub/next-toolbar"

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>
        {/* Layout UI */}
        <main>{children}</main>
        <Toolbar />
      </body>
    </html>
  )
}
```

### Fill in the Website URL input in BaseHub

This will help our servers know where to go to to revalidate the queries.

![](https://assets.basehub.com/7b31fb4b/4dc74fb9bbf1a5d52c36b5649b537665/cleanshot-2024-10-12-at-11.04.212x.png?width=3840&quality=90&format=auto)

In the Readme, top right

### Just use it

That should be all! Make sure you don’t pass other cache-related props (such as `revalidate` or `cache`), as that will opt the query out of automatic on-demand revalidation.

As you may notice, we’re also not passing `draftMode().isEnabled` via props, as this is no longer required as of `basehub@7.5.10`—we now automatically infer draft mode for you.

```
import { Pump } from "basehub/react-pump"
import { basehub } from "basehub"

const Page = async () => {
  // works with basehub and with Pump
  const data = await basehub().query({ __typename: true })

  return (
    <Pump queries={[{ __typename: true }]}>
      {async ([data]) => {
        "use server"

        return <pre>{JSON.stringify(data, null, 2)}</pre>
      }}
    </Pump>
  )
}

export default Page
```

info:

Wondering **how does this all work?** When `basehub().query` is ran, we hash the query being sent and use it as a cache tag. We send this cache tag to our servers (alongside the query itself).

The server now runs the query and computes the response. It will then hash the response, and store the cache tag, the original query, and the response hash in our database.

On commit, we’ll get all of the queries we’ve been collecting and run them again against the newly committed tree of blocks. Now, one by one, we run them, compute the response hash, and compare it against the one we previously returned to the user. If response hashes don’t match, we need to revalidate the query.

To revalidate the query, we spin up a headless browser that navigates to your Website URL and executes the Server Action our `<Toolbar />` created.

Read the [full writeup in our blog](https://basehub.com/blog/automatic-on-demand-revalidation-for-nextjs-how-it-works) to learn more.

### Time-Based Revalidation

Another conventional way to revalidate content is to use Next.js’ [time-based](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#time-based-revalidation) `revalidate` [caching option](https://nextjs.org/docs/app/building-your-application/data-fetching/fetching-caching-and-revalidating#time-based-revalidation).

```
import { Pump } from "basehub/react-pump"

const Page = async () => {
  return (
    <Pump
      next={{ revalidate: 30 }} 
      queries={[{ __typename: true }]}
    >
      {async ([data]) => {
        "use server"
        // `data` will be stale after 30 seconds

        return <pre>{JSON.stringify(data, null, 2)}</pre>
      }}
    </Pump>
  )
}

export default Page
```

While this is very easy to set up, automatic on-demand revalidation is always better, as editors won’t need to refresh the website for several seconds to see their content live; will keep server costs down, as the server itself won’t need to constantly check with our API to see if something has changed; and will simply remove one task from developers’ hands.