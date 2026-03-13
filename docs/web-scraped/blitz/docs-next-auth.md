# Source: https://blitzjs.com/docs/next-auth

Title: Third Party Login with NextAuth - Blitz.js

URL Source: https://blitzjs.com/docs/next-auth

Markdown Content:
Third Party Login with NextAuth - Blitz.js
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

    * [Setup](https://blitzjs.com/docs/next-auth#setup)
    * [1. Add the NextAuth Adapter for next.config.js](https://blitzjs.com/docs/next-auth#add-next-auth-adapter-next-config)
    * [2. Add the NextAuth API Route](https://blitzjs.com/docs/next-auth#add-the-nextauth-js-api-route)
    * [Config Structure](https://blitzjs.com/docs/next-auth#config)
    * [URLs](https://blitzjs.com/docs/next-auth#urls)
    * [SSL Proxy Configuration](https://blitzjs.com/docs/next-auth#ssl)
    * [3. Add a Next Auth Provider](https://blitzjs.com/docs/next-auth#2-add-a-next-auth-provider)
    * [3. Log in with this NextAuth Provider](https://blitzjs.com/docs/next-auth#3-log-in-with-this-next-auth-provider)
    * [Detailed Usage Instructions](https://blitzjs.com/docs/next-auth#detailed-usage-instructions)
    * [Create a Session](https://blitzjs.com/docs/next-auth#create-a-session)
    * [Return an Error](https://blitzjs.com/docs/next-auth#return-an-error)
    * [Showing the Error to the User](https://blitzjs.com/docs/next-auth#showing-the-error-to-the-user)
    * [Post Authentication Redirects](https://blitzjs.com/docs/next-auth#post-authentication-redirects)

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

Third Party Login with NextAuth
===============================

### Topics

Jump to a Topic

Blitz provides an adapter that allows you to use any [NextAuth Provider](https://next-auth.js.org/providers/) with Blitz session management in any Nextjs application. Blitz session management gives you a lot more flexibility & control than NextAuth does

[](https://blitzjs.com/docs/next-auth#setup)Setup
-------------------------------------------------

### [](https://blitzjs.com/docs/next-auth#add-next-auth-adapter-next-config)1. Add the NextAuth Adapter for `next.config.js`

```ts
const { withNextAuthAdapter } = require("@blitzjs/auth/next-auth")
const { withBlitz } = require("@blitzjs/next")

/**
 * @type {import('@blitzjs/next').BlitzConfig}
 **/
const config = {
  ...
}

module.exports = withBlitz(withNextAuthAdapter(config))
```

### [](https://blitzjs.com/docs/next-auth#add-the-nextauth-js-api-route)2. Add the NextAuth API Route

Add a new API route at `src/pages/api/auth/[...nextauth].ts` with the following contents.

```ts
// src/pages/api/auth/[...nextauth].ts
import { api } from "src/blitz-server"
import GithubProvider from "next-auth/providers/github"
import GoogleProvider from "next-auth/providers/google"
import { NextAuthAdapter } from "@blitzjs/auth/next-auth"
import db, { User } from "db"
import { Role } from "types"

// Has to be defined separately for `profile` to be correctly typed below
const providers = [
  GithubProvider({
    clientId: process.env.GITHUB_CLIENT_ID as string,
    clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
  }),
  GoogleProvider({
    clientId: process.env.GOOGLE_CLIENT_ID as string,
    clientSecret: process.env.GOOGLE_CLIENT_SECRET as string,
  }),
]

export default api(
  NextAuthAdapter({
    successRedirectUrl: "/",
    errorRedirectUrl: "/error",
    providers,
    callback: async (user, account, profile, session) => {
      ...
    },
  })
)
```

If you need, you can place the api route at a different path but the filename must be `[...nextauth].js` or `[...nextauth].ts`.

### [](https://blitzjs.com/docs/next-auth#config)Config Structure

```ts
export type BlitzNextAuthOptions = AuthOptions & {
  // Redirect after successfull authentification
  successRedirectUrl: string
  // Redirect after any intentional or other auth errors
  errorRedirectUrl: string
  secureProxy?: boolean
  callback: (
    user: User,
    account: Account,
    // Automatically Inferred From Providers Declared
    profile: Profile,
    session: SessionContext,
    provider: ProviderName
  ) => Promise<void | { redirectUrl: string }>
}
```

#### [](https://blitzjs.com/docs/next-auth#urls)URLs

The `NextAuth` adapter adds two API endpoints for each installed strategy. With the handler at `src/pages/api/auth/[...nextauth].ts`, it adds the following:

1. `/api/auth/[providerName]/login` - URL to initiate login
2. `/api/auth/[providerName]/callback` - Callback URL to complete login For example with `GitHubProvider` provider, the URLs for GitHub login will be:
3. `/api/auth/github/login` - URL to initiate login
4. `/api/auth/github/callback` - Callback URL to complete login You can determine the `provider` with the argument passed to the common callback.

#### [](https://blitzjs.com/docs/next-auth#ssl)SSL Proxy Configuration

You may need to set `secureProxy` option to `true` in case your app is located behind SSL proxy (Nginx). Proxy should be set to manage `forwarded` or `x-forwarded-proto` header correctly.

```ts
// src/pages/api/auth/[...nextauth].ts
import { NextAuthAdapter } from "@blitzjs/auth/next-auth"
import { api } from "src/blitz-server"
import db from "db"
export default api(
  NextAuthAdapter({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    secureProxy: true, 
    strategies: [
      /*...*/
    ],
  })
)
```

### [](https://blitzjs.com/docs/next-auth#2-add-a-next-auth-provider)3. Add a Next Auth Provider

Add a provider to the `providers` array argument for `NextAuthAdapter` in the API route, and then follow the providers documentation for further setup.

```ts
// src/pages/api/auth/[...nextauth].ts
import { api } from "src/blitz-server"
import GithubProvider from "next-auth/providers/github"
import { NextAuthAdapter, BlitzNextAuthOptions } from "@blitzjs/auth/next-auth"
import db, { User } from "db"
import { Role } from "types"

const config: BlitzNextAuthOptions = {
  successRedirectUrl: "/",
  errorRedirectUrl: "/",

  providers: [
    GithubProvider({
      clientId: process.env.GITHUB_CLIENT_ID as string,
      clientSecret: process.env.GITHUB_CLIENT_SECRET as string,
    }),
  ],
  callback: async (user, account, profile, session, provider) => {
    let newUser: User
    try {
      newUser = await db.user.findFirstOrThrow({
        where: { name: { equals: user.name } },
      })
    } catch (e) {
      newUser = await db.user.create({
        data: {
          email: user.email!,
          name: user.name || "unknown",
          role: "USER",
        },
      })
    }
    await session.$create({
      userId: newUser.id,
      role: newUser.role as Role,
      source: "github",
    })
    return { redirectUrl: "/github" }
    //if no return it will default to successRedirectUrl
  },

}
export default api(NextAuthAdapter(config))
```

Note: The above `GitHubProvider` example requires your `User` prisma model to have `email String @unique` and `name String`.

### [](https://blitzjs.com/docs/next-auth#3-log-in-with-this-next-auth-provider)3. Log in with this NextAuth Provider

Add a link to your app with URL format of `/api/auth/[providerName]/login`. For the above GitHub example, the link would be like this:

```tsx
<a href="/api/auth/github">Log In With GitHub</a>
```

[](https://blitzjs.com/docs/next-auth#detailed-usage-instructions)Detailed Usage Instructions
---------------------------------------------------------------------------------------------

Upon successful authentication with the third-party, the user will be redirected back to the above auth API route. When that happens, the `verify` callback will be called. When the `verify` callback is called, the user has been authenticated with the third-party, but **a session has not yet been created for your Blitz app**.

### [](https://blitzjs.com/docs/next-auth#create-a-session)Create a Session

**To create a new Blitz session**, you need to call the use the `session` argument passed to the callback function.

```ts
session.$create({
    ...
})
```

### [](https://blitzjs.com/docs/next-auth#return-an-error)Return an Error

If instead, you want to prevent creating a session because of some error, then throw an error inside the callback function. Blitz will catch the error and will attach it to the error redirect URL provided.

```ts
throw new YourAuthFailureError()
```

### [](https://blitzjs.com/docs/next-auth#showing-the-error-to-the-user)Showing the Error to the User

Any error during this process will be provided as the `authError` query parameter. For example with `errorRedirectUrl = '/'` and `done(new Error("it broke"))`, the user will be redirected to:

```bash
/?authError=it broke
```

### [](https://blitzjs.com/docs/next-auth#post-authentication-redirects)Post Authentication Redirects

There are four different ways to determine the redirect URL where a user should be sent after they are authenticated. They are listed here in order of priority. A URL provided with method #1 will override all other URLs.

* Add `redirectUrl` return to the required URL depending on the provider

```ts
return { redirectUrl: "/github" }
```

* Add a `redirectUrl` query parameter to the "initiate login" url

  * Example: `example.com/api/auth/github?redirectUrl=/dashboard`
  * Example: `example.com/api/auth/github?redirectUrl=${router.pathname}`

* Via the config passed to `NextAuthAdapter`

  * If success, it will use `config.successRedirectUrl`
  * If error, it will use `config.errorRedirectUrl`

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/next-auth.mdx)

[Third Party Login w/Passport.js](https://blitzjs.com/docs/passportjs)[How To Impersonate Other Users](https://blitzjs.com/docs/impersonation)

[](https://blitzjs.com/docs/next-auth#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2024 Brandon Bayer and Blitz.js Contributors
