# Source: https://blitzjs.com/docs/error-handling

Title: Error Handing - Blitz.js

URL Source: https://blitzjs.com/docs/error-handling

Markdown Content:
Error Handing - Blitz.js
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

* ![Image 7](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 9: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 10](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 11: Community](https://blitzjs.com/_next/image?url=%2Fimg%2Fpeople-white.svg&w=32&q=75)  Community  
  * [How the Community Operates](https://blitzjs.com/docs/how-the-community-operates)
  * [Manifesto](https://blitzjs.com/docs/manifesto)
  * [History](https://blitzjs.com/docs/community-history)
  * [How to Contribute](https://blitzjs.com/docs/contributing)
  * [Being a Maintainer](https://blitzjs.com/docs/maintainers)
  * [Code of Conduct](https://blitzjs.com/docs/code-of-conduct)
  * [Doc Translations](https://blitzjs.com/docs/translations)

* ![Image 12](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 14: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 15](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 16: Basics](https://blitzjs.com/_next/image?url=%2Fimg%2Fbasics-white.svg&w=32&q=75)  Basics  
  * [File Structure](https://blitzjs.com/docs/file-structure)
  * [Custom Environments](https://blitzjs.com/docs/custom-environments)
  * [Error Handling](https://blitzjs.com/docs/error-handling)

    * [Built-In Errors](https://blitzjs.com/docs/error-handling#built-in-errors)
    * [Catching and Handling Errors on the Client](https://blitzjs.com/docs/error-handling#catching-and-handling-errors-on-the-client)
    * [Handling Server Errors on the Client](https://blitzjs.com/docs/error-handling#handling-server-errors-on-the-client)
    * [Custom Errors](https://blitzjs.com/docs/error-handling#custom-errors)

  * [Testing](https://blitzjs.com/docs/testing)
  * [HTTP Middleware](https://blitzjs.com/docs/middleware)
  * [Client Plugins](https://blitzjs.com/docs/client-plugin)
  * [Logging](https://blitzjs.com/docs/logging)
  * [Utilities](https://blitzjs.com/docs/utilities)
  * [Client and Server](https://blitzjs.com/docs/client-and-server)
  * [Troubleshooting](https://blitzjs.com/docs/troubleshooting)

* ![Image 17](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 19: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 20](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 21: Guides](https://blitzjs.com/_next/image?url=%2Fimg%2Frouting-white.svg&w=32&q=75)  Guides  
  * [Blitz Auth with Next.js](https://blitzjs.com/docs/blitz-auth-with-next)
  * [Usage Guide Next.js 13](https://blitzjs.com/docs/usage-next-13)

* ![Image 22](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 24: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 25](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 27: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Framework Adapters  
  * [@blitzjs/next](https://blitzjs.com/docs/blitzjs-next)

* ![Image 28](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 30: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 31](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 33: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Blitz Auth  
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

Error Handing
=============

### Topics

Jump to a Topic

[](https://blitzjs.com/docs/error-handling#built-in-errors)Built-In Errors
--------------------------------------------------------------------------

Blitz comes with a number of useful errors you can use throughout your application.

* `AuthenticationError`
  * `name`: "AuthenticationError"
  * `statusCode`: 401
  * Default `message`: "You must be logged in to access this"

* `CSRFTokenMismatchError`
  * `name`: "CSRFTokenMismatchError"
  * `statusCode`: 401
  * Default `message`: "You must be logged in to access this"

* `AuthorizationError`
  * `name`: "AuthorizationError"
  * `statusCode`: 403
  * Default `message`: "You are not authorized to access this"

* `NotFoundError`
  * `name`: "NotFoundError"
  * `statusCode`: 404
  * Default `message`: "This could not be found"

* `RedirectError`
  * `name`: "RedirectError"
  * You can throw this error from a render function if you want to redirect the user while also preventing the user from seeing on the current render path. Our `ErrorBoundary` component will automatically handle this redirect for you.
  * Example: `throw new RedirectError('/login')`

To use, import from `blitz` and use like any JavaScript Error. If you're curious, you can [see the source code for these](https://github.com/blitz-js/blitz/blob/canary/packages/core/src/errors.ts).

```ts
import { AuthenticationError } from "blitz"

try {
  throw new AuthenticationError()
} catch (error) {
  if (error.name === "AuthenticationError") {
    // Handle this error appropriately, like show a login screen
    console.log(error.statusCode)
    console.log(error.message)
  }
}
```

You can throw these or any other errors from anywhere in your app, whether on the server or on the client.

[](https://blitzjs.com/docs/error-handling#catching-and-handling-errors-on-the-client)Catching and Handling Errors on the Client
--------------------------------------------------------------------------------------------------------------------------------

You handle errors on the client by using [`<ErrorBoundary>`](https://blitzjs.com/docs/error-boundary).

By default, new Blitz applications include a top-level `ErrorBoundary` and `FallbackComponent` in `pages/_app.tsx`.

It looks something like this:

```tsx
// app/pages/_app.tsx
import { AppProps, ErrorBoundary, ErrorComponent } from "@blitzjs/next"
import { useQueryErrorResetBoundary } from "@blitzjs/rpc"
import LoginForm from "app/auth/components/LoginForm"

export default function App({ Component, pageProps }: AppProps) {
  // This ensures the Blitz useQuery hooks will automatically refetch
  // data any time you reset the error boundary
  const { reset } = useQueryErrorResetBoundary()

  return (
    <ErrorBoundary FallbackComponent={RootErrorFallback} onReset={reset}>
      <Component {...pageProps} />
    </ErrorBoundary>
  )
}

function RootErrorFallback({ error, resetErrorBoundary }) {
  if (error.name === "AuthenticationError") {
    return <LoginForm onSuccess={resetErrorBoundary} />
  } else if (error.name === "AuthorizationError") {
    return (
      <ErrorComponent
        statusCode={error.statusCode}
        title="Sorry, you are not authorized to access this"
      />
    )
  } else {
    return (
      <ErrorComponent
        statusCode={error.statusCode || 400}
        title={error.message || error.name}
      />
    )
  }
}
```

That means all errors will at least be caught at the root level. However, you can also add `<ErrorBoundary>` anywhere else in your app for more localized error handling. To do this, declare a separate `useQueryErrorResetBoundary` in your component and pass it along to the local ErrorBoundary. If an error is caught by an `<ErrorBoundary>` somewhere down inside your app tree, then it will not reach the root ErrorBoundary unless you re-throw it.

### [](https://blitzjs.com/docs/error-handling#handling-server-errors-on-the-client)Handling Server Errors on the Client

A really awesome feature of Blitz is that you can throw any error from a Blitz query or mutation and then use an ErrorBoundary on the frontend to catch and handle it.

For example, with the above `_app.tsx`, you can throw `AuthenticationError` inside a Blitz query and then a login screen will automatically show in the client because that root ErrorBoundary is rendering `<LoginForm>` if `error.name === 'AuthenticationError'`.

### [](https://blitzjs.com/docs/error-handling#custom-errors)Custom Errors

For errors other than what Blitz provides, it's recommended to create custom Error classes. You can then add custom data attributes that help you handle the error.

Here's an example of how to create a custom error. It's a JavaScript class, so you can be as creative as you want.

```ts
import SuperJson from "superjson"

export class UsernameTakenError extends Error {
  name = "UsernameTakenError"
  constructor({ suggestedUserName }) {
    super()
    this.suggestedUserName = suggestedUserName
  }
}
// Register with SuperJson serializer so it's reconstructed on the client
SuperJson.registerClass(UsernameTakenError)
SuperJson.allowErrorProps("suggestedUserName")

throw new UsernameTakenError({ suggestedUserName: "second_best" })
```

Note that you **must register it with SuperJson** as shown above in order for `instanceof` to work on the client. And you must also tell SuperJson about any special error propertries you want to be serialized. By default custom error properties are omitted for security concerns.

Then on the client, you can use a `FallbackComponent` like above, or you can handle the error in your form submit handler like this.

```tsx
<Form
  onSubmit={async (values) => {
    try {
      await setUsername(values.username)
    } catch (error) {
      if (error instanceof UsernameTakenError) {
        setSuggestedUsername(error.suggestedUserName)
      }
    }
  }}
/>
```

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/error-handling.mdx)

[Custom Environments](https://blitzjs.com/docs/custom-environments)[Testing](https://blitzjs.com/docs/testing)

[](https://blitzjs.com/docs/error-handling#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2026 Brandon Bayer and Blitz.js Contributors
