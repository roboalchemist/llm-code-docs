# Source: https://blitzjs.com/docs/passportjs

Title: Third Party Login with Passport.js - Blitz.js

URL Source: https://blitzjs.com/docs/passportjs

Markdown Content:
Third Party Login with Passport.js - Blitz.js
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

    * [Setup](https://blitzjs.com/docs/passportjs#setup)
    * [1. Add the Passport.js API Route](https://blitzjs.com/docs/passportjs#1-add-the-passport-js-api-route)
    * [2. Add a Passport Strategy](https://blitzjs.com/docs/passportjs#2-add-a-passport-strategy)
    * [3. Log in with this Passport Strategy](https://blitzjs.com/docs/passportjs#3-log-in-with-this-passport-strategy)
    * [Detailed Usage Instructions](https://blitzjs.com/docs/passportjs#detailed-usage-instructions)
    * [Create a Session](https://blitzjs.com/docs/passportjs#create-a-session)
    * [Return an Error](https://blitzjs.com/docs/passportjs#return-an-error)
    * [Showing the Error to the User](https://blitzjs.com/docs/passportjs#showing-the-error-to-the-user)
    * [Post Authentication Redirects](https://blitzjs.com/docs/passportjs#post-authentication-redirects)
    * [authenticateOptions](https://blitzjs.com/docs/passportjs#authenticate-options)
    * [Custom strategy name](https://blitzjs.com/docs/passportjs#custom-strategy-name)

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

Third Party Login with Passport.js
==================================

### Topics

Jump to a Topic

Blitz provides an adapter that lets you use an existing [Passport.js authentication strategy](http://www.passportjs.org/).

Currently only passport strategies that use a `verify` callback are supported. In the Twitter example below, the second argument to `TwitterStrategy()` is the `verify` callback.

[](https://blitzjs.com/docs/passportjs#setup)Setup
--------------------------------------------------

### [](https://blitzjs.com/docs/passportjs#1-add-the-passport-js-api-route)1. Add the Passport.js API Route

Add a new api route at `src/pages/api/auth/[...auth].ts` with the following contents.

```ts
// src/pages/api/auth/[...auth].ts
import { passportAuth } from "@blitzjs/auth"
import { api } from "src/blitz-server"
import db from "db"

export default api(
  passportAuth({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    strategies: [
      {
        strategy: new PassportStrategy(), // Provide initialized passport strategy here
      },
    ],
  })
)
```

If you need, you can place the api route at a different path but the filename must be `[...auth].js` or `[...auth].ts`.

#### URLs

The `passportAuth` adapter adds two API endpoints for each installed strategy.

With the handler at `src/pages/api/auth/[...auth].ts`, it adds the following:

1. `/api/auth/[strategyName]` - URL to initiate login
2. `/api/auth/[strategyName]/callback` - Callback URL to complete login

For example with `passport-twitter` strategy, the URLs for Twitter will be:

1. `/api/auth/twitter` - URL to initiate login
2. `/api/auth/twitter/callback` - Callback URL to complete login

You can determine the `strategyName` in the strategy's documentation by looking for this: `passport.authenticate('github')`. So in this case, the `strategyName` is `github`.

#### SSL Proxy Configuration

You may need to set `secureProxy` option to `true` in case your app is located behind SSL proxy (Nginx). Proxy should be set to manage `forwarded` or `x-forwarded-proto` header correctly.

```ts
// src/pages/api/auth/[...auth].ts
import { passportAuth } from "@blitzjs/auth"
import { api } from "src/blitz-server"
import db from "db"

export default api(
  passportAuth({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    secureProxy: true, 
    strategies: [
      /*...*/
    ],
  })
)
```

#### Access Middleware Context, Request and Response objects

You can access the middleware context and request and response objects by providing a callback to the `passportAuth` adapter. The argument of the callback is an object with the properties `ctx`, `req` and `res`. You can then access the session context via `ctx.session` or the request object if you need to include custom parameters in your passport strategies (e.g., invitation codes, referal codes).

```ts
// src/pages/api/auth/[...auth].ts
import { passportAuth } from "@blitzjs/auth"
import { api } from "src/blitz-server"
import db from "db"

export default api(
  passportAuth(({ ctx, req, res }) => ({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    strategies: [
      {
        strategy: new TwitterStrategy({
          consumerKey: process.env.TWITTER_CONSUMER_KEY as string,
          consumerSecret: process.env.TWITTER_CONSUMER_SECRET as string,
          /*...*/
        }),
      },
    ],
  }))
)
```

Note: If your environment variables are not typed, you must add a type assertion to each environment variable when using the callback (as shown in the example above).

### [](https://blitzjs.com/docs/passportjs#2-add-a-passport-strategy)2. Add a Passport Strategy

Add a strategy to the `strategies` array argument for `passportAuth` in the API route, and then follow the strategy's documentation for setup.

Here's an example of adding `passport-twitter`.

Note that the `callbackURL` uses the callback endpoint as described above (`/api/auth/twitter/callback`)

```ts
import { passportAuth } from "@blitzjs/auth"
import { api } from "src/blitz-server"
import db from "db"
import { Strategy as TwitterStrategy } from "passport-twitter"

export default api(
  passportAuth({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    strategies: [

      {
        strategy: new TwitterStrategy(
          {
            consumerKey: process.env.TWITTER_CONSUMER_KEY,
            consumerSecret: process.env.TWITTER_CONSUMER_SECRET,
            callbackURL:
              process.env.NODE_ENV === "production"
                ? "https://example.com/api/auth/twitter/callback"
                : "http://localhost:3000/api/auth/twitter/callback",
            includeEmail: true,
          },
          async function (_token, _tokenSecret, profile, done) {
            const email = profile.emails && profile.emails[0]?.value

            if (!email) {
              // This can happen if you haven't enabled email access in your twitter app permissions
              return done(
                new Error("Twitter OAuth response doesn't have email.")
              )
            }

            const user = await db.user.upsert({
              where: { email },
              create: {
                email,
                name: profile.displayName,
              },
              update: { email },
            })

            const publicData = {
              userId: user.id,
              roles: [user.role],
              source: "twitter",
            }
            done(undefined, { publicData })
          }
        ),
      },

    ],
  })
)
```

Note: The above `passport-twitter` example requires your `User` prisma model to have `email String @unique` and `name String`.

### [](https://blitzjs.com/docs/passportjs#3-log-in-with-this-passport-strategy)3. Log in with this Passport Strategy

Add a link to your app with URL format of `/api/auth/[strategyName]`.

For the above twitter example, the link would be like this:

```tsx
<a href="/api/auth/twitter">Log In With Twitter</a>
```

[](https://blitzjs.com/docs/passportjs#detailed-usage-instructions)Detailed Usage Instructions
----------------------------------------------------------------------------------------------

Upon successful authentication with the third-party, the user will be redirected back to the above auth API route. When that happens, the `verify` callback will be called.

When the `verify` callback is called, the user has been authenticated with the third-party, but **a session has not yet been created for your Blitz app**.

### [](https://blitzjs.com/docs/passportjs#create-a-session)Create a Session

**To create a new Blitz session**, you need to call the `done()` function from your `verify` callback.

```ts
done(undefined, result)
```

where `result` is an object of type `VerifyCallbackResult`

```ts
export type VerifyCallbackResult = {
  publicData: PublicData
  privateData?: Record<string, any>
  redirectUrl?: string
}
```

The Blitz adapter will then call `session.$create()` for you and redirect the user back to the correct place in your application.

### [](https://blitzjs.com/docs/passportjs#return-an-error)Return an Error

If instead, you want to prevent creating a session because of some error, then call `done()` with an error as the first argument. The user will then be redirected back to the correct location.

```ts
return done(new Error("it broke"))
```

### [](https://blitzjs.com/docs/passportjs#showing-the-error-to-the-user)Showing the Error to the User

Any error during this process will be provided as the `authError` query parameter.

For example with `errorRedirectUrl = '/'` and `done(new Error("it broke"))`, the user will be redirected to:

```bash
/?authError=it broke
```

### [](https://blitzjs.com/docs/passportjs#post-authentication-redirects)Post Authentication Redirects

There are four different ways to determine the redirect URL where a user should be sent after they are authenticated. They are listed here in order of priority. A URL provided with method #1 will override all other URLs.

1. Add `redirectUrl` to the `verify` callback result
    *   Example: `done(undefined, {publicData, redirectUrl: '/'})`

2. Add a `redirectUrl` query parameter to the "initiate login" url
    *Example: `example.com/api/auth/twitter?redirectUrl=/dashboard`
    *   Example: `example.com/api/auth/twitter?redirectUrl=${router.pathname}`

3. Via the config passed to `passportAuth`
    *If success, it will use `config.successRedirectUrl`
    *   If error, it will use `config.errorRedirectUrl`

4. If none of the above are provided, it will redirect to `/`

Note: If there is an error, methods #1 and #2 will override `config.errorRedirectUrl`

This should give you maximum flexibility to do anything you need. If this doesn't meet your needs, please open an issue on GitHub!

### [](https://blitzjs.com/docs/passportjs#authenticate-options)`authenticateOptions`

Some strategies have to call an option like `scope` or `successMessage` inside the `passport.authenticate()` method. Add these options to the `passportAuth` object like this:

```ts
import { passportAuth } from "@blitzjs/auth"
import { api } from "src/blitz-server"
import db from "db"
import { Strategy as Auth0Strategy } from "passport-auth0"

export default api(
  passportAuth({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    strategies: [
      {

        authenticateOptions: { scope: "openid email profile" },

        strategy: new Auth0Strategy(
          {
            domain: process.env.AUTH0_DOMAIN,
            clientID: process.env.AUTH0_CLIENT_ID,
            clientSecret: process.env.AUTH0_CLIENT_SECRET,
            callbackURL:
              process.env.NODE_ENV === "production"
                ? "https://example.com/api/auth/auth0/callback"
                : "http://localhost:3000/api/auth/auth0/callback",
          },
          async function (
            _token,
            _tokenSecret,
            extraParams,
            profile,
            done
          ) {
            const email = profile.emails && profile.emails[0]?.value

            if (!email) {
              // This can happen if you haven't enabled email access in your Auth0 app permissions
              return done(new Error("Auth response doesn't have email."))
            }

            const user = await db.user.upsert({
              where: { email },
              create: {
                email,
                name: profile.displayName,
              },
              update: { email },
            })

            const publicData = {
              userId: user.id,
              roles: [user.role],
              source: "auth0",
            }
            done(undefined, { publicData })
          }
        ),
      },
    ],
  })
)
```

Note: Without the `authenticateOptions` the `profile` parameter inside the `verify` function would not contain any values.

### [](https://blitzjs.com/docs/passportjs#custom-strategy-name)Custom strategy name

When creating auth API routes, Blitz will use a default strategy's name. For example, for a Twitter startegy, the API routes will be: `/api/auth/twitter` and `api/auth/twitter/callback`. If you want to override the name and provide a custom one, you can specify a `name` parameter:

```ts
export default api(
  passportAuth({
    successRedirectUrl: "/",
    errorRedirectUrl: "/",
    strategies: [
      {
        name: "custom-name", 
        strategy: new TwitterStrategy(
          // ...
```

The above configuration will result in `example.com/api/auth/custom-name` and `api/auth/custom-name/callback` API routes.

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/passportjs.mdx)

[Authorization & Security](https://blitzjs.com/docs/authorization)[Third Party Login w/NextAuth](https://blitzjs.com/docs/next-auth)

[](https://blitzjs.com/docs/passportjs#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2024 Brandon Bayer and Blitz.js Contributors
