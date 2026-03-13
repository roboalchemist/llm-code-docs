# Source: https://blitzjs.com/docs/blitzjs-next

Title: @blitzjs/next

URL Source: https://blitzjs.com/docs/blitzjs-next

Published Time: Fri, 13 Mar 2026 19:25:07 GMT

Markdown Content:
@blitzjs/next
===============

🚀[Announcing Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)- Easily Deploy Blitz.js and Next.js to AWS 🚀

[Blitz home page](https://blitzjs.com/)

[Documentation](https://blitzjs.com/docs/get-started)[Showcase](https://blitzjs.com/showcase)[Releases](https://github.com/blitz-js/blitz/releases)[Swag](https://store.blitzjs.com/)[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)

Search Dark Mode

[](https://github.com/blitz-js/blitz)[](https://twitter.com/blitz_js)[](https://discord.blitzjs.com/)

* ![Image 1](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 3: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 4](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 6: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Introduction  
  * [Why Blitz?](https://blitzjs.com/docs/why-blitz)
  * [Get Started](https://blitzjs.com/docs/get-started)
  * [Learning Path](https://blitzjs.com/docs/learning-path)
  * [Tutorial](https://blitzjs.com/docs/tutorial)
  * [With Existing Next.js App](https://blitzjs.com/docs/blitz-with-next)
  * [Upgrading to Blitz 2.0](https://blitzjs.com/docs/upgrading-from-framework)

* ![Image 7](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 9: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 10](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 12: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Community  
  * [How the Community Operates](https://blitzjs.com/docs/how-the-community-operates)
  * [Manifesto](https://blitzjs.com/docs/manifesto)
  * [History](https://blitzjs.com/docs/community-history)
  * [How to Contribute](https://blitzjs.com/docs/contributing)
  * [Being a Maintainer](https://blitzjs.com/docs/maintainers)
  * [Code of Conduct](https://blitzjs.com/docs/code-of-conduct)
  * [Doc Translations](https://blitzjs.com/docs/translations)

* ![Image 13](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 15: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 16](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 18: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Basics  
  * [File Structure](https://blitzjs.com/docs/file-structure)
  * [Custom Environments](https://blitzjs.com/docs/custom-environments)
  * [Error Handling](https://blitzjs.com/docs/error-handling)
  * [Testing](https://blitzjs.com/docs/testing)
  * [HTTP Middleware](https://blitzjs.com/docs/middleware)
  * [Client Plugins](https://blitzjs.com/docs/client-plugin)
  * [Logging](https://blitzjs.com/docs/logging)
  * [Utilities](https://blitzjs.com/docs/utilities)
  * [Client and Server](https://blitzjs.com/docs/client-and-server)
  * [Troubleshooting](https://blitzjs.com/docs/troubleshooting)

* ![Image 19](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 21: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 22](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 23: Guides](https://blitzjs.com/_next/image?url=%2Fimg%2Frouting-white.svg&w=32&q=75)  Guides  
  * [Blitz Auth with Next.js](https://blitzjs.com/docs/blitz-auth-with-next)
  * [Usage Guide Next.js 13](https://blitzjs.com/docs/usage-next-13)

* ![Image 24](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 26: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 27](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 28: Framework Adapters](https://blitzjs.com/_next/image?url=%2Fimg%2Fpages-white.svg&w=32&q=75)  Framework Adapters  
  * [@blitzjs/next](https://blitzjs.com/docs/blitzjs-next)

    * [Overview](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-overview)
    * [Setup](https://blitzjs.com/docs/blitzjs-next#setup-blitzjs-next)
    * [Next Config](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-config)
    * [Client](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client)
    * [Example](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client-example)
    * [API](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client-api)
    * [Server](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server)
    * [Example](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-example)
    * [API](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-api)
    * [Custom Server](https://blitzjs.com/docs/blitzjs-next#custom-next-server)
    * [Wrappers](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-wrappers)
    * [Examples](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-wrapper-examples)
    * [Concepts](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-concepts)
    * [Authenticate user before page loads](https://blitzjs.com/docs/blitzjs-next#authenticate-users-on-page-load)
    * [Return types when data fetching on the server](https://blitzjs.com/docs/blitzjs-next#data-fetching-types)
    * [Handling errors on initial page load](https://blitzjs.com/docs/blitzjs-next#handle-errors-on-load)

* ![Image 29](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 31: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 32](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 34: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz Auth  
  * [Overview](https://blitzjs.com/docs/auth)
  * [Setup](https://blitzjs.com/docs/auth-setup)
  * [Configuration](https://blitzjs.com/docs/auth-config)
  * [Sessions](https://blitzjs.com/docs/session-management)
  * [Server-Side APIs](https://blitzjs.com/docs/auth-server)
  * [Client-Side APIs](https://blitzjs.com/docs/auth-client)
  * [Authorization & Security](https://blitzjs.com/docs/authorization)
  * [Third Party Login w/Passport.js](https://blitzjs.com/docs/passportjs)
  * [Third Party Login w/NextAuth](https://blitzjs.com/docs/next-auth)
  * [How To Impersonate Other Users](https://blitzjs.com/docs/impersonation)

* ![Image 35](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 37: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 38](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 40: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz RPC  
  * [Overview](https://blitzjs.com/docs/rpc-overview)
  * [Setup](https://blitzjs.com/docs/rpc-setup)
  * [Configuration](https://blitzjs.com/docs/rpc-config)
  * [Query Resolvers](https://blitzjs.com/docs/query-resolvers)
  * [Use Queries](https://blitzjs.com/docs/query-usage)
  * [Mutation Resolvers](https://blitzjs.com/docs/mutation-resolvers)
  * [Use Mutations](https://blitzjs.com/docs/mutation-usage)
  * [Client Utilities](https://blitzjs.com/docs/resolver-client-utilities)
  * [Server Utilities](https://blitzjs.com/docs/resolver-server-utilities)
  * [useQuery](https://blitzjs.com/docs/use-query)
  * [usePaginatedQuery](https://blitzjs.com/docs/use-paginated-query)
  * [useInfiniteQuery](https://blitzjs.com/docs/use-infinite-query)
  * [useMutation](https://blitzjs.com/docs/use-mutation)
  * [RPC Specification](https://blitzjs.com/docs/rpc-specification)

* ![Image 41](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 43: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 44](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 46: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Backend Architecture  
  * [Multitenancy](https://blitzjs.com/docs/multitenancy)

* ![Image 47](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 49: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 50](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 52: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Database  
  * [Overview](https://blitzjs.com/docs/database-overview)
  * [Run Postgres Locally](https://blitzjs.com/docs/postgres)
  * [Seeds](https://blitzjs.com/docs/database-seeds)
  * [Prisma Utilities](https://blitzjs.com/docs/prisma)

* ![Image 53](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 55: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 56](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 58: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Recipes  
  * [Using Recipes](https://blitzjs.com/docs/using-recipes)
  * [Writing Recipes](https://blitzjs.com/docs/writing-recipes)

* ![Image 59](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 61: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 62](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 64: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  CLI  
  * [Overview](https://blitzjs.com/docs/cli-overview)
  * [blitz new](https://blitzjs.com/docs/cli-new)
  * [blitz dev](https://blitzjs.com/docs/cli-dev)
  * [blitz start](https://blitzjs.com/docs/cli-start)
  * [blitz build](https://blitzjs.com/docs/cli-build)
  * [blitz prisma](https://blitzjs.com/docs/cli-prisma)
  * [blitz generate](https://blitzjs.com/docs/cli-generate)
  * [blitz codegen](https://blitzjs.com/docs/cli-codegen)
  * [blitz routes](https://blitzjs.com/docs/cli-routes)
  * [blitz console](https://blitzjs.com/docs/cli-console)
  * [blitz install](https://blitzjs.com/docs/cli-install)

* ![Image 65](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 67: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 68](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 70: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Templates  
  * [Blitz Templates](https://blitzjs.com/docs/templates)

[Back to Documentation Menu](https://blitzjs.com/docs)

@blitzjs/next
=============

### Topics

Jump to a Topic

[](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-overview)Overview
-----------------------------------------------------------------------

The `@blitzjs/next` adapter exposes functions & components specific for the Next.js framework.

[](https://blitzjs.com/docs/blitzjs-next#setup-blitzjs-next)Setup
-----------------------------------------------------------------

You can install `@blitzjs/next` by running the following command:

```bash
npm i @blitzjs/next # yarn add @blitzjs/next # pnpm add @blitzjs/next
```

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-config)Next Config

Blitz.js extends the `next.config.js` file by accepting a `blitz` property.

```ts
blitz?: {
  resolverPath?: ResolverPathOptions;
  customServer?: {
      hotReload?: boolean;
  };
};
```

##### Note

For more information on setting a custom `resolverPath`, read more at the [RPC Specification](https://blitzjs.com/docs/rpc-specification#url)

[](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client)Client
-------------------------------------------------------------------

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client-example)Example

Inside `src/blitz-client.ts`:

```ts
import { setupBlitzClient } from "@blitzjs/next"

export const { withBlitz } = setupBlitzClient({
  plugins: [],
})
```

Then inside `src/pages/_app.tsx` wrap `MyApp` function with the `withBlitz` HOC component.

```ts
import {
  ErrorFallbackProps,
  ErrorComponent,
  ErrorBoundary,
} from "@blitzjs/next"
import { AuthenticationError, AuthorizationError } from "blitz"
import type { AppProps } from "next/app"
import React, { Suspense } from "react"
import { withBlitz } from "src/blitz-client"

function RootErrorFallback({ error }: ErrorFallbackProps) {
  if (error instanceof AuthenticationError) {
    return <div>Error: You are not authenticated</div>
  } else if (error instanceof AuthorizationError) {
    return (
      <ErrorComponent
        statusCode={error.statusCode}
        title="Sorry, you are not authorized to access this"
      />
    )
  } else {
    return (
      <ErrorComponent
        statusCode={(error as any)?.statusCode || 400}
        title={error.message || error.name}
      />
    )
  }
}

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <ErrorBoundary FallbackComponent={RootErrorFallback}>
      <Component {...pageProps} />
    </ErrorBoundary>
  )
}

export default withBlitz(MyApp)
```

##### Note

An `<ErrorBoundary />` provider and `<ErrorComponent />` component is supplied by `@blitzjs/next`

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-client-api)API

```ts
setupBlitzClient({
  plugins: [],
})
```

#### Arguments

* `plugins:` An array of Blitz.js plugins
  * **Required**

#### Returns

An object with the `withBlitz` HOC wrapper

[](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server)Server
-------------------------------------------------------------------

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-example)Example

Inside `src/blitz-server.ts`

```ts
import { setupBlitzServer } from "@blitzjs/next"

export const { gSSP, gSP, api } = setupBlitzServer({
  plugins: [],
})
```

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-api)API

```ts
setupBlitzServer({
  plugins: [],
  onError?: (err) => void
})
```

#### Arguments

* `plugins:` An array of Blitz.js plugins
  * **Required**

* `onError:` Catch all errors _(Great for services like sentry)_

#### Returns

An object with the [`gSSP`](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-gssp), [`gSP`](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-gsp)&[`api`](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-api) wrappers.

### [](https://blitzjs.com/docs/blitzjs-next#custom-next-server)Custom Server

The Blitz CLI supports running custom Next.js servers. This means you can compile both javascript & typescript while using the Blitz.js CLI to inject env variables. By default, the CLI checks for `src/server/index.[ts | js]` or `src/server.[ts | js]`

For more information about custom Next.js servers, check the [`official docs`](https://nextjs.org/docs/advanced-features/custom-server)

[](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-server-wrappers)Wrappers
------------------------------------------------------------------------------

All Next.js wrapper functions are serialized with [`superjson`](https://github.com/blitz-js/superjson). That means you can use `Date`, `Map`, `Set`&`BigInt` when returning data. Another thing to note is that Blitz runs the middlewares from plugins before calling the Next.js request handler.

##### Note

The `gSSP`, `gSP`&`api` functions all pass down the context of the session if you're using the auth plugin. Read more about the auth plugin here [@blitzjs/auth](https://blitzjs.com/docs/auth).

### [](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-wrapper-examples)Examples

#### getStaticProps

```ts
import { gSP } from "src/blitz-server"

export const getStaticProps = gSP(async ({ ctx }) => {
  return {
    props: {
      data: {
        userId: ctx?.session.userId,
        session: {
          id: ctx?.session.userId,
          publicData: ctx?.session.$publicData,
        },
      },
    },
  }
})
```

#### getServerSideProps

```ts
import { gSSP } from "src/blitz-server"

export const getServerSideProps = gSSP(async ({ ctx }) => {
  return {
    props: {
      userId: ctx?.session.userId,
      publicData: ctx?.session.$publicData,
    },
  }
})
```

#### api

```ts
import { api } from "src/blitz-server"

export default api(async (req, res, ctx) => {
  res.status(200).json({ userId: ctx?.session.userId })
})
```

_For more information about Next.js API routes, visit their docs at [https://nextjs.org/docs/api-routes/introduction](https://nextjs.org/docs/api-routes/introduction)_

[](https://blitzjs.com/docs/blitzjs-next#blitzjs-next-concepts)Concepts
-----------------------------------------------------------------------

### [](https://blitzjs.com/docs/blitzjs-next#authenticate-users-on-page-load)Authenticate user before page loads

You may want to check if the user is logged in before your page loads. We’re going to use the `getCurrentUser` query inside `getServerSideProps()` by calling the query directly. Then you can check if the user is logged in on the server and use the built-in Next.js redirect property.

```ts
import { Routes, BlitzPage } from "@blitzjs/next"
import { gSSP } from "src/blitz-server"
import getCurrentUser from "src/users/queries/getCurrentUser"

export const getServerSideProps = gSSP(async ({ ctx }) => {
  const currentUser = await getCurrentUser(null, ctx)

  if (currentUser) {
    return {
      props: {
        user: currentUser,
      },
    }
  } else {
    return {
      redirect: {
        destination: Routes.LoginPage(),
        permanent: false,
      },
    }
  }
})
```

### [](https://blitzjs.com/docs/blitzjs-next#data-fetching-types)Return types when data fetching on the server

You can set the types returned from the Next.js data fetching functions. All Blitz.js wrappers for the Next.js functions accept a generic. Same with the `BlitzPage` type.

So for example, we can use some typescript utilities to help use get the types returned by `getCurrentUser()`

```ts
import { Routes, BlitzPage } from "@blitzjs/next"
import { gSSP } from "src/blitz-server"
import getCurrentUser from "src/users/queries/getCurrentUser"

type TCurrentUser = Awaited<ReturnType<typeof getCurrentUser>>

export const getServerSideProps = gSSP<{ user: TCurrentUser }>(
  async ({ ctx }) => {
    const currentUser = await getCurrentUser(null, ctx)

    if (currentUser) {
      return {
        props: {
          user: currentUser,
        },
      }
    } else {
      return {
        redirect: {
          destination: Routes.LoginPage(),
          permanent: false,
        },
      }
    }
  }
)

const Page: BlitzPage<{ user: TCurrentUser }> = ({ user }) => {
  return (
    <Layout title="Page">
      <div className="container">
        <p>User Page</p>
        {user && <p>{user.email}</p>}
      </div>
    </Layout>
  )
}

export default Page
```

### [](https://blitzjs.com/docs/blitzjs-next#handle-errors-on-load)Handling errors on initial page load

There’s an edge case where you may be throwing an error in a query that’s being called on an initial page load, causing a server error instead of hitting the `<ErrorBoundary />`. This is because when initially loading the page, there is no ErrorBoundary component rendered until `_app.tsx` is mounted. Though, this is expected behaviour, there is a workaround.

For an example, in a query where the user is not found you can create a `NotFoundError()` then return the status code.

```ts
export default resolver.pipe(resolver.zod(GetUser), async (input) => {
  const { id } = input

  const user = await db.user.findFirst({ where: { id } })

  if (!user) {
    const userError = new NotFoundError("User not found")
    return {
      error: userError.statusCode,
    }
  } else {
    return {
      user,
    }
  }
})
```

Then on the server (in this case `getServerSideProps()`) you can call the query and if the error key is found in the return object then show an error.

```ts
export const getServerSideProps = gSSP(async ({ ctx }) => {

  const user = await getUser({ 1 }, ctx)
  if("error" in user) {
    return { props: { error: user.error}}
  } else {
    return { props: { user }}
  }
})
```

You can also catch server errors in`_app.tsx` and show the errors with a toast component.

```tsx
function MyApp({ Component, pageProps }: AppProps) {
  const getLayout = Component.getLayout || ((page) => page)
  if (pageProps.error) {
    return <ToastComponent>{pageProps.error.statusCode}</ToastComponent>
  }
  return (
    <ErrorBoundary FallbackComponent={RootErrorFallback}>
      {getLayout(<Component {...pageProps} />)}
    </ErrorBoundary>
  )
}
```

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/blitzjs-next.mdx)

[Usage Guide Next.js 13](https://blitzjs.com/docs/usage-next-13)[Overview](https://blitzjs.com/docs/auth)

[](https://blitzjs.com/docs/blitzjs-next#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2026 Brandon Bayer and Blitz.js Contributors

![Image 71](https://cdn.usefathom.com/?h=https%3A%2F%2Fblitzjs.com&p=%2Fdocs%2Fblitzjs-next&r=&sid=NGIOZUKS&qs=%7B%7D&cid=7500757)
