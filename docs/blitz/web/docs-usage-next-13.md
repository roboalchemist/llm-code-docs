# Source: https://blitzjs.com/docs/usage-next-13

Title: Usage Guide - Next.js 13 with Blitz Toolkit

URL Source: https://blitzjs.com/docs/usage-next-13

Markdown Content:
Usage Guide - Next.js 13 with Blitz Toolkit
===============

🚀[Announcing Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)- Easily Deploy Blitz.js and Next.js to AWS 🚀

[Blitz home page](https://blitzjs.com/)

[Documentation](https://blitzjs.com/docs)[Showcase](https://blitzjs.com/showcase)[Releases](https://github.com/blitz-js/blitz/releases)[Swag](https://store.blitzjs.com/)[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)

Search

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

* ![Image 19](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 21: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 22](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 24: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Guides  
  * [Blitz Auth with Next.js](https://blitzjs.com/docs/blitz-auth-with-next)
  * [Usage Guide Next.js 13](https://blitzjs.com/docs/usage-next-13)

    * [Migration Guide](https://blitzjs.com/docs/usage-next-13#migration-guide)
    * [Upgrading Guide](https://blitzjs.com/docs/usage-next-13#upgrading-guide)
    * [Codemods](https://blitzjs.com/docs/usage-next-13#nextjs-codemods)
    * [Support with the App Router (Beta)](https://blitzjs.com/docs/usage-next-13#app-directory)
    * [Required changes](https://blitzjs.com/docs/usage-next-13#required-changes)
    * [BlitzProvider](https://blitzjs.com/docs/usage-next-13#blitz-provider)
    * [Blitz Auth](https://blitzjs.com/docs/usage-next-13#blitz-auth)
    * [Blitz RPC](https://blitzjs.com/docs/usage-next-13#blitz-rpc)

* ![Image 25](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 27: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 28](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 30: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Framework Adapters  
  * [@blitzjs/next](https://blitzjs.com/docs/blitzjs-next)

* ![Image 31](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 33: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 34](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 36: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz Auth  
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

* ![Image 37](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 39: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 40](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 42: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz RPC  
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

* ![Image 43](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 45: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 46](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 48: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Backend Architecture  
  * [Multitenancy](https://blitzjs.com/docs/multitenancy)

* ![Image 49](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 51: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 52](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 54: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Database  
  * [Overview](https://blitzjs.com/docs/database-overview)
  * [Run Postgres Locally](https://blitzjs.com/docs/postgres)
  * [Seeds](https://blitzjs.com/docs/database-seeds)
  * [Prisma Utilities](https://blitzjs.com/docs/prisma)

* ![Image 55](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 57: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 58](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 60: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Recipes  
  * [Using Recipes](https://blitzjs.com/docs/using-recipes)
  * [Writing Recipes](https://blitzjs.com/docs/writing-recipes)

* ![Image 61](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 63: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 64](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 66: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  CLI  
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

* ![Image 67](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 69: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 70](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 72: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Templates  
  * [Blitz Templates](https://blitzjs.com/docs/templates)

[Back to Documentation Menu](https://blitzjs.com/docs)

Usage Guide - Next.js 13 with Blitz Toolkit
===========================================

### Topics

Jump to a Topic

### [](https://blitzjs.com/docs/usage-next-13#migration-guide)Migration Guide

Blitz **does not require any breaking changes** with the major upgrade of `Next 12` ➔ `Next 13` for usage with the `pages` directory. You can even continue to use the old blitz layout with all your files in `app`. But you'll need to rename that directory if you want to use the new Next.js app router.

The migration guide provided by the Next.js Team can then be followed to completely upgrade your Next 12 application

#### [](https://blitzjs.com/docs/usage-next-13#upgrading-guide)Upgrading Guide

[https://nextjs.org/docs/upgrading#upgrading-from-12-to-13](https://nextjs.org/docs/upgrading#upgrading-from-12-to-13)

#### [](https://blitzjs.com/docs/usage-next-13#nextjs-codemods)Codemods

[https://nextjs.org/docs/advanced-features/codemods](https://nextjs.org/docs/advanced-features/codemods)

### [](https://blitzjs.com/docs/usage-next-13#app-directory)Support with the App Router (Beta)

To support the new paradigm of Next that uses [React Server Side Components](https://github.com/reactjs/rfcs/blob/main/text/0188-server-components.md), the following methods and hooks have been implemented to work in the new `app` directory

#### [](https://blitzjs.com/docs/usage-next-13#required-changes)Required changes

Add the new `use client` directive to the following files:

1. `src/blitz-client.(ts|js)`
2. All Files with usage of `useQuery`, `useInfiniteQuery`, `usePaginatedQuery`, `useMutation`, `Hydrate` and other React Query client side hooks.

**What not to change:**

`/pags/api/rpc/[[...blitz]].ts` stays in the `/pages` folder.

#### Recommendations

* For Blitz apps that have their pages at `/src/pages` it is recommended to colocate the app directory at `/src/app`. However, a root `/app` App directory is also supported. More on the new NextJS file structure at ["Project Organization and File Colocation"](https://nextjs.org/docs/app/building-your-application/routing/colocation#src-directory).

#### [](https://blitzjs.com/docs/usage-next-13#blitz-provider)BlitzProvider

This provider should wrap the app and should be placed at the `(root)/layout.ts` file.

**Setup**

```ts
// src/blitz-client.ts

"use client"
import {AuthClientPlugin} from "@blitzjs/auth"
import {setupBlitzClient} from "@blitzjs/next"
import {BlitzRpcPlugin} from "@blitzjs/rpc"
import { authConfig } from './blitz-auth-config'

export const {withBlitz, BlitzProvider} = setupBlitzClient({
  plugins: [
    AuthClientPlugin(authConfig),
    BlitzRpcPlugin({}),
  ],
})
```

The `authConfig` needs to be in a separate file that is imported in `blitz-client.ts` as well as `blitz-server.ts`:

```ts
// src/blitz-auth-config.ts
import { AuthPluginClientOptions } from '@blitzjs/auth'

export const authConfig: AuthPluginClientOptions = {
  cookiePrefix: "blitz-auth-with-next-app",
}
```

**In root layout.ts file**

```tsx
// src/layout.ts
import { BlitzProvider } from "src/blitz-client"

export default function RootLayout({children}: {children: React.ReactNode}) {
  return (
    <html lang="en">
      <head>
        ...
      </head>
      <body>
        <BlitzProvider>
          ...
        </BlitzProvider>
      </body>
    </html>
  )
}
```

#### [](https://blitzjs.com/docs/usage-next-13#blitz-auth)Blitz Auth

##### getBlitzContext

This function will use the cookies and headers provided by the server component and returns the current session.

###### API

```ts
getBlitzContext() => Ctx
```

###### Usage

Example Usage in React Server Component in app directory in Next 13

**Setup**

```tsx
// src/blitz-server.ts
export const { ... , useAuthenticatedBlitzContext} = setupBlitzServer({
  ...
})
```

**In a RSC page or layout**

```tsx
import {getBlitzContext} from "src/blitz-server"
import getCurrentUser from "src/users/queries/getCurrentUser"

export default async function Home() {
  const ctx = await getBlitzContext()
  const user = await getCurrentUser(null, ctx)
  return(
    <>
        ...
    </>
  )
}
```

##### useAuthenticatedBlitzContext

1. This hook is implemented as the replacement of the [**BlitzPage Security Auth Utilities**](https://blitzjs.com/docs/authorization#secure-your-pages) provided for the pages directory to work with React Server Components in the Next 13 `app` directory

2. It can be used in any asynchronous server component be it in `page.ts` or in the layouts in `layout.ts`

##### API

```tsx
useAuthenticatedBlitzContext({
  redirectTo,
  redirectAuthenticatedTo,
  role,
}: {
  redirectTo?: string | RouteUrlObject
  redirectAuthenticatedTo?: string | RouteUrlObject | ((ctx: Ctx) => string | RouteUrlObject)
  role?: string | string[]
}): Promise<void>
```

##### Explaintation of each parameter

1. `redirectTo`

The `URL` or `Route` object passed to this parameter will be used to `redirect`**unauthenticated** users (logged-out) and the users whose roles does not satisfy the required roles mentioned in the `roles` parameter

1. `role`

This parameter takes a role (as string) or multipe roles to be used to **authorize** user access to a particular page or layout

1. `redirectAuthenticatedTo`

The `URL` or `Route` object passed to this parameter will be used to `redirect`**authenticated** (logged-in) users.

##### Usage

Example Usage in React Server Component in app directory in Next 13

**Setup**

```tsx
// src/blitz-server.ts
export const { ... , useAuthenticatedBlitzContext} = setupBlitzServer({
  ...
})
```

**In a RSC Page or Layout**

```tsx
import {useAuthenticatedBlitzContext} from "src/blitz-server"
...
await useAuthenticatedBlitzContext({
    redirectTo: "/auth/login",
    role: ["admin"],
    redirectAuthenticatedTo: "/dashboard",
})
```

#### [](https://blitzjs.com/docs/usage-next-13#blitz-rpc)Blitz RPC

The following method are to be used to invoke a resolver in a react server component

##### Using `invoke`

Let's say there is a requirement to query a resolver in the `(root)/page.js` file to check the details of the current user

First import the `invoke` function from the `blitz-server` file.

Note we cannot directly import `invoke` from `@blitzjs/rpc` due to the necessity to run the required middleware in order to make it work effectively.

**Setup**

```tsx
// src/blitz-server.ts
import {RpcServerPlugin} from "@blitzjs/rpc"
...
export const {... , invoke} = setupBlitzServer({
  plugins: [
    ...
    RpcServerPlugin({}),
  ]
  ...
})
```

**In a RSC Page or Layout**

```tsx
import {invoke} from "src/blitz-server"
import getCurrentUser from "src/users/queries/getCurrentUser"
```

Now, we can directly invoke the resolver using the invoke function

```tsx
const user = await invoke(getCurrentUser, null)
```

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/usage-next-13.mdx)

[Blitz Auth with Next.js](https://blitzjs.com/docs/blitz-auth-with-next)[@blitzjs/next](https://blitzjs.com/docs/blitzjs-next)

[](https://blitzjs.com/docs/usage-next-13#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2024 Brandon Bayer and Blitz.js Contributors
