# Source: https://blitzjs.com/docs/auth-server

Title: Auth Server-Side APIs - Blitz.js

URL Source: https://blitzjs.com/docs/auth-server

Published Time: Fri, 13 Mar 2026 19:25:52 GMT

Markdown Content:
Auth Server-Side APIs - Blitz.js
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

* ![Image 29](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 31: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 32](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 33: Blitz Auth](https://blitzjs.com/_next/image?url=%2Fimg%2Fshield-white.svg&w=32&q=75)  Blitz Auth  
  * [Overview](https://blitzjs.com/docs/auth)
  * [Setup](https://blitzjs.com/docs/auth-setup)
  * [Configuration](https://blitzjs.com/docs/auth-config)
  * [Sessions](https://blitzjs.com/docs/session-management)
  * [Server-Side APIs](https://blitzjs.com/docs/auth-server)

    * [In Queries & Mutations](https://blitzjs.com/docs/auth-server#in-queries-and-mutations)
    * [getServerSideProps](https://blitzjs.com/docs/auth-server#get-server-side-props)
    * [App Router API Routes](https://blitzjs.com/docs/auth-server#app-api-routes)
    * [withBlitzAuth API](https://blitzjs.com/docs/auth-server#with-blitz-auth-api)
    * [Pages Router API Routes](https://blitzjs.com/docs/auth-server#pages-api-routes)
    * [generateToken()](https://blitzjs.com/docs/auth-server#generate-token)
    * [hash256()](https://blitzjs.com/docs/auth-server#hash256)
    * [SecurePassword](https://blitzjs.com/docs/auth-server#secure-password)
    * [setPublicDataForUser()](https://blitzjs.com/docs/auth-server#set-public-data-for-user)
    * [getSession](https://blitzjs.com/docs/auth-server#get-session)
    * [SessionContext.setSession](https://blitzjs.com/docs/auth-server#session-context-set-session)

  * [Client-Side APIs](https://blitzjs.com/docs/auth-client)
  * [Authorization & Security](https://blitzjs.com/docs/authorization)
  * [Third Party Login w/Passport.js](https://blitzjs.com/docs/passportjs)
  * [Third Party Login w/NextAuth](https://blitzjs.com/docs/next-auth)
  * [How To Impersonate Other Users](https://blitzjs.com/docs/impersonation)

* ![Image 34](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 36: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 37](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 39: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz RPC  
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

* ![Image 40](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 42: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 43](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 45: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Backend Architecture  
  * [Multitenancy](https://blitzjs.com/docs/multitenancy)

* ![Image 46](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 48: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 49](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 51: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Database  
  * [Overview](https://blitzjs.com/docs/database-overview)
  * [Run Postgres Locally](https://blitzjs.com/docs/postgres)
  * [Seeds](https://blitzjs.com/docs/database-seeds)
  * [Prisma Utilities](https://blitzjs.com/docs/prisma)

* ![Image 52](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 54: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 55](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 57: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Recipes  
  * [Using Recipes](https://blitzjs.com/docs/using-recipes)
  * [Writing Recipes](https://blitzjs.com/docs/writing-recipes)

* ![Image 58](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 60: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 61](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 63: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  CLI  
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

* ![Image 64](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 66: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 67](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 69: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Templates  
  * [Blitz Templates](https://blitzjs.com/docs/templates)

[Back to Documentation Menu](https://blitzjs.com/docs)

Auth Server-Side APIs
=====================

### Topics

Jump to a Topic

[](https://blitzjs.com/docs/auth-server#in-queries-and-mutations)In Queries & Mutations
---------------------------------------------------------------------------------------

`SessionContext` is available off of `ctx` which is provided as the second parameter to all queries and mutations.

```ts
// src/queries/someQuery.ts
import { Ctx } from "blitz"

export default async function someQuery(input: any, ctx: Ctx) {
  // Access the SessionContext class
  ctx.session.userId
  ctx.session.role
  ctx.session.$create(/*...*/)

  return
}
```

[](https://blitzjs.com/docs/auth-server#get-server-side-props)`getServerSideProps`
----------------------------------------------------------------------------------

You can get the session context inside `getServerSideProps` by wrapping it with the `gSSP` function exported from `src/blitz-server`:

```ts
import { SessionContext } from "@blitzjs/auth"
import { gSSP } from "src/blitz-server"

type Props = {
  userId: unknown
  publicData: SessionContext["$publicData"]
}

export const getServerSideProps = gSSP<Props>(async ({ ctx }) => {
  const { session } = ctx
  return {
    props: {
      userId: session.userId,
      publicData: session.$publicData,
      publishedAt: new Date(0),
    },
  }
})

function PageWithGssp(props: Props) {
  return <div>{JSON.stringify(props, null, 2)}</div>
}

export default PageWithGssp
```

[](https://blitzjs.com/docs/auth-server#app-api-routes)App Router API Routes
----------------------------------------------------------------------------

You can get the session context inside API routes by wrapping it with the `withBlitzAuth` function exported from `src/blitz-server`:

```ts
//app/api/logout/route.ts
import { withBlitzAuth } from "app/blitz-server"

export const POST = withBlitzAuth(async (_request, _params, ctx) => {
  const session = ctx.session
  await session.$revoke()
  return new Response(
    JSON.stringify({
      userId: session.userId,
    }),
    { status: 200 }
  )
})
```

#### [](https://blitzjs.com/docs/auth-server#with-blitz-auth-api)`withBlitzAuth` API

The function supports both single handler as an input as well as an object of handlers and has the following signature:

```ts
function withBlitzAuth(handlers: { [method: string]: Handler })
```

##### Arguments

* `handlers: { [method: string]: Handler })` - An object of handlers where the key is the HTTP method and the value is the handler function.

```ts
type Handler = (
  request: Request,
  params: Record<string, string>,
  ctx: { session: SessionContext }
) => Promise<Response>
```

##### Returns

* `{ [method: string]: Handler }` - The wrapper function returns an object of handlers where the key is the HTTP method and the value is the handler function wrapped with the session management of `@blitzjs/auth`.

##### Example Usage with single handler

```ts
//app/api/logout/route.ts
import { withBlitzAuth } from "app/blitz-server"

export const { POST } = withBlitzAuth({
  POST: async (_request, _params, { session }) => {
    // logout the user
    await session.$revoke()
    return new Response(
      JSON.stringify({
        userId: session.userId,
      }),
      { status: 200 }
    )
  },
})
```

##### Example Usage with multiple handlers

```ts
//app/api/multiple/route.ts
import { withBlitzAuth } from "app/blitz-server"

export const { GET, POST } = withBlitzAuth({
  GET: async (_request, _params, { session }) => {
    return new Response(
      JSON.stringify({
        userId: session.userId,
      }),
      { status: 200 }
    )
  },
  POST: async (_request, _params, { session }) => {
    return new Response(
      JSON.stringify({
        userId: session.userId,
      }),
      { status: 200 }
    )
  },
})
```

[](https://blitzjs.com/docs/auth-server#pages-api-routes)Pages Router API Routes
--------------------------------------------------------------------------------

You can get the session context inside API routes by wrapping it with the `api` function exported from `src/blitz-server`:

```ts
import { api } from "src/blitz-server"
import db from "db"

export default api(async (_req, res, ctx) => {
  ctx.session.$authorize()
  const publicData = ctx.session.$publicData

  res.status(200).json({
    userId: ctx.session.userId,
    publicData: { ...publicData },
  })
})
```

[](https://blitzjs.com/docs/auth-server#generate-token)`generateToken()`
------------------------------------------------------------------------

#### `generateToken(numberOfCharacters: number = 32) => string`

This is a convenience wrapper around [nanoid](https://github.com/ai/nanoid) for generating tokens for things like password resets.

#### Example Usage

```ts
import { generateToken } from "@blitzjs/auth"

const token = generateToken()
```

[](https://blitzjs.com/docs/auth-server#hash256)`hash256()`
-----------------------------------------------------------

#### `hash256(value: string) => string`

This is a convenience wrapper that uses the node [crypto](https://nodejs.org/api/crypto.html) module to hash a string with the `sha256` algorithm. It is used for things like hashing password reset tokens before saving them in the database.

Hash256 is also useful for storing strings like API keys in the database because the returned hash will always be the same for a given string. Therefore, you can still verify that an API key exists in the database when the only value you have to reference is the hashed key.

#### Example Usage

```ts
import { hash256 } from "@blitzjs/auth"

const hashedToken = hash256(token)
```

[](https://blitzjs.com/docs/auth-server#secure-password)`SecurePassword`
------------------------------------------------------------------------

`SecurePassword` is a convenience wrapper around [secure-password](https://github.com/emilbayes/secure-password) to provide a nice way to hash passwords and verify password hashes.

```ts
import { SecurePassword } from "@blitzjs/auth"

await SecurePassword.hash(password)
await SecurePassword.verify(passwordHash, password)
```

#### `SecurePassword.hash(password: string) => Promise<string>`

This is used when a user sets a new password.

It takes a password string and returns a secure hash for storing in your database.

`SecurePassword.hash` will return a different hash when given the same string, hence the necessity of `SecurePassword.verify` to compare hashes.

#### `SecurePassword.verify(passwordHash: string, password: string) => Promise<ResultCode>`

This is used when a user logs in to verify they used the correct password.

It takes a password hash from your database and the given password. It will verify the given password is correct and return a result code, or if incorrect, it will throw `AuthenticationError`.

##### Result Codes

**`SecurePassword.VALID`**

The password was verified and is valid

**`SecurePassword.VALID_NEEDS_REHASH`**

The password was verified and is valid, but needs to be rehashed with new parameters

**`SecurePassword.HASH_BYTES`**

Size of the `hash` Buffer returned by `hash` and `hashSync` and used by `verify` and `verifySync`.

#### Example Usage

```ts
import { AuthenticationError } from "blitz"
import { SecurePassword } from "@blitzjs/auth"
import db from "db"

export const authenticateUser = async (
  email: string,
  password: string
) => {
  const user = await db.user.findFirst({ where: { email } })
  if (!user) throw new AuthenticationError()

  const result = await SecurePassword.verify(
    user.hashedPassword,
    password
  )

  if (result === SecurePassword.VALID_NEEDS_REHASH) {
    // Upgrade hashed password with a more secure hash
    const improvedHash = await SecurePassword.hash(password)
    await db.user.update({
      where: { id: user.id },
      data: { hashedPassword: improvedHash },
    })
  }

  const { hashedPassword, ...rest } = user
  return rest
}
```

[](https://blitzjs.com/docs/auth-server#set-public-data-for-user)`setPublicDataForUser()`
-----------------------------------------------------------------------------------------

#### `setPublicDataForUser(userId: PublicData['userId'], publicData: Record<any, any>) => void`

This can be used to update the `publicData` of a user's sessions. It can be useful when changing a user's role, since the new permissions can be enforced as soon as the user is doing the next request.

#### Example Usage

```ts
import { setPublicDataForUser } from "@blitzjs/auth"
import db from "db"

export const updateUserRole = async (
  userId: PublicData["userId"],
  role: string
) => {
  // update the user's role
  await db.user.update({ where: { id: userId }, data: { role } })
  // update role in all active sessions
  await setPublicDataForUser(userId, { role })
}
```

##### Note

The following methods are meant for internal usage or for advanced use cases. They are not needed for general use.

[](https://blitzjs.com/docs/auth-server#get-session)`getSession`
----------------------------------------------------------------

This function is used internally by Blitz to get the session context from the request either from an `IncomingMessage` and `ServerResponse` pair or from a `Request` object.

#### Arguments

* `req: IncomingMessage | Request` - The request object from the server.
* `res: ServerResponse | never` - The response object from the server.
* `isRsc: boolean` - A boolean that determines if the request is for a resource.

#### Returns

* `SessionContext` - The session context object.

[](https://blitzjs.com/docs/auth-server#session-context-set-session)`SessionContext.setSession`
-----------------------------------------------------------------------------------------------

This function is used along with [getSession](https://blitzjs.com/docs/auth-server#get-session) to set the session context on the response object after the session has been created or updated.

#### Arguments

* `response: Response | ServerResponse` - The response object from the server.

#### Returns

* `void`

#### Example Usage

##### With `Request`

```ts
async function handler(request: Request, params: Record<string, string>) {
  const session = await getSession(request)
  const response = await handler(request, params, { session })
  session.setSession(response)
  return response
}
```

##### With `IncomingMessage` and `ServerResponse`

```ts
async function handler(req: IncomingMessage, res: ServerResponse) {
  const session = await getSession(req, res)
  await handler(req, res, { session })
  session.setSession(res)
}
```

* `handler` is a function that processes the request and can mutate the session state
* The `response` | `res` will contain the session state after the handler has been processed

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/auth-server.mdx)

[Sessions](https://blitzjs.com/docs/session-management)[Client-Side APIs](https://blitzjs.com/docs/auth-client)

[](https://blitzjs.com/docs/auth-server#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2026 Brandon Bayer and Blitz.js Contributors
