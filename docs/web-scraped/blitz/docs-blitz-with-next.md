# Source: https://blitzjs.com/docs/blitz-with-next

Title: Add Blitz.js to an Existing Next.js Project

URL Source: https://blitzjs.com/docs/blitz-with-next

Markdown Content:
Add Blitz.js to an Existing Next.js Project
===============

🚀[Announcing Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)- Easily Deploy Blitz.js and Next.js to AWS 🚀

[Blitz home page](https://blitzjs.com/)

[Documentation](https://blitzjs.com/docs/get-started)[Showcase](https://blitzjs.com/showcase)[Releases](https://github.com/blitz-js/blitz/releases)[Swag](https://store.blitzjs.com/)[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)

Search Dark Mode

[](https://github.com/blitz-js/blitz)[](https://twitter.com/blitz_js)[](https://discord.blitzjs.com/)

* ![Image 1](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 3: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 4](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 5: Introduction](https://blitzjs.com/_next/image?url=%2Fimg%2Fintroduction-white.svg&w=32&q=75)  Introduction  
  * [Why Blitz?](https://blitzjs.com/docs/why-blitz)
  * [Get Started](https://blitzjs.com/docs/get-started)
  * [Learning Path](https://blitzjs.com/docs/learning-path)
  * [Tutorial](https://blitzjs.com/docs/tutorial)
  * [With Existing Next.js App](https://blitzjs.com/docs/blitz-with-next)

    * [Adding required dependencies](https://blitzjs.com/docs/blitz-with-next#adding-dependencies)
    * [Blitz server setup](https://blitzjs.com/docs/blitz-with-next#blitz-server-setup)
    * [Blitz client setup](https://blitzjs.com/docs/blitz-with-next#blitz-client-setup)
    * [Use withBlitz in your App component](https://blitzjs.com/docs/blitz-with-next#use-withblitz-in-app-component)
    * [Modifying next.config.js file](https://blitzjs.com/docs/blitz-with-next#modifying-next-config-file)
    * [Adding plugins](https://blitzjs.com/docs/blitz-with-next#adding-plugins)

  * [Upgrading to Blitz 2.0](https://blitzjs.com/docs/upgrading-from-framework)

* ![Image 6](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 8: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 9](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 10: Community](https://blitzjs.com/_next/image?url=%2Fimg%2Fpeople-white.svg&w=32&q=75)  Community  
  * [How the Community Operates](https://blitzjs.com/docs/how-the-community-operates)
  * [Manifesto](https://blitzjs.com/docs/manifesto)
  * [History](https://blitzjs.com/docs/community-history)
  * [How to Contribute](https://blitzjs.com/docs/contributing)
  * [Being a Maintainer](https://blitzjs.com/docs/maintainers)
  * [Code of Conduct](https://blitzjs.com/docs/code-of-conduct)
  * [Doc Translations](https://blitzjs.com/docs/translations)

* ![Image 11](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 13: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 14](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 15: Basics](https://blitzjs.com/_next/image?url=%2Fimg%2Fbasics-white.svg&w=32&q=75)  Basics  
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

* ![Image 16](blob:http://localhost/2ab1a6bbd270865568c2458a680487e3) ![Image 18: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  ![Image 19](blob:http://localhost/a413908070606583258e7d72e6911dbb) ![Image 21: Templates](blob:http://localhost/b9a31d3949b1882a09ed2f8508d538f3)  Guides  
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

Add Blitz.js to an Existing Next.js Project
===========================================

### Topics

Jump to a Topic

If you have an existing Next.js project and would like to use some or all of Blitz Toolkit, this page will provide you with information on setting it up. A few steps are required, and we'll go through them one by one.

[](https://blitzjs.com/docs/blitz-with-next#adding-dependencies)Adding required dependencies
--------------------------------------------------------------------------------------------

```bash
yarn add blitz @blitzjs/next

# or

pnpm add blitz @blitzjs/next

# or

npm i blitz @blitzjs/next
```

[](https://blitzjs.com/docs/blitz-with-next#blitz-server-setup)Blitz server setup
---------------------------------------------------------------------------------

If you want to use Blitz's server functionalities like auth, middlewares, rpc, you'd need to create a `blitz-server.ts` file somewhere in your project, e.g. in `src/blitz-server.ts`. We'll cover how to add plugins later.

```ts
import { setupBlitzServer } from "@blitzjs/next"

const {
  /* plugins' exports */
} = setupBlitzServer({
  plugins: [
    // plugins will go here
  ],
})
```

[](https://blitzjs.com/docs/blitz-with-next#blitz-client-setup)Blitz client setup
---------------------------------------------------------------------------------

Now, if you want Blitz's client functionalities, you'll have to create a `blitz-client.ts` file. It can be next to the `blitz-server.ts` in `src/blitz-client.ts`.

```ts
import { setupBlitzClient } from "@blitzjs/next"

export const { withBlitz } = setupBlitzClient({
  plugins: [
    // plugins will go here
  ],
})
```

The `withBlitz` function will be needed to wrap your components with Blitz's client side functionality.

[](https://blitzjs.com/docs/blitz-with-next#use-withblitz-in-app-component)Use `withBlitz` in your App component
----------------------------------------------------------------------------------------------------------------

To use Blitz on the client, you also have to use the `withBlitz` function in your App component.

```ts
import { withBlitz } from "src/blitz-client"

function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />
}

export default withBlitz(App)
```

[](https://blitzjs.com/docs/blitz-with-next#modifying-next-config-file)Modifying `next.config.js` file
------------------------------------------------------------------------------------------------------

Next.js requires you to manually type out page locations. Blitz comes with a [Route Manifest](https://blitzjs.com/docs/route-manifest), so you can do:

```tsx
<Link href={Routes.ProductsPage({ productId: 123 })} />
// instead of
<Link href={`/products/${123}`} />
```

To enable it, you have to wrap your config with `withBlitz` in the `next.config.js` file:

```js
const { withBlitz } = require("@blitzjs/next")

module.exports = withBlitz()
```

[](https://blitzjs.com/docs/blitz-with-next#adding-plugins)Adding plugins
-------------------------------------------------------------------------

Now that you're all set with the basic setup, you can add plugins that you want to use in your app. There are a few places to check out:

1. [`@blitzjs/auth`](https://blitzjs.com/docs/auth-setup) — it covers how to setup auth plugin as well as how to use Blitz auth system.
2. [`@blitzjs/rpc`](https://blitzjs.com/docs/rpc-setup) — check it out to learn how to set up Blitz's Zero API Layer and to learn more about it.

Finally, you can check out more detailed information about the [`@blitzjs/next` adapter](https://blitzjs.com/docs/blitzjs-next) to learn how to use Blitz functionalities inside of `getServerSideProps`, `getStaticProps`, Next API Routes, and other places.

* * *

[Idea for improving this page? Edit it on GitHub.](https://github.com/blitz-js/blitzjs.com/edit/main/app/pages/docs/blitz-with-next.mdx)

[Tutorial](https://blitzjs.com/docs/tutorial)[Upgrading to Blitz 2.0](https://blitzjs.com/docs/upgrading-from-framework)

[](https://blitzjs.com/docs/blitz-with-next#top)

Want to receive the latest news and updates from the Blitz team? Sign up for our newsletter!

### Docs

[All Docs](https://blitzjs.com/docs)[Get Started](https://blitzjs.com/docs/get-started)[How To Contribute](https://blitzjs.com/docs/contributing)

### Community

[Discord](https://discord.blitzjs.com/)[Forum Discussions](https://github.com/blitz-js/blitz/discussions)[Twitter](https://twitter.com/blitz_js)[Showcase](https://blitzjs.com/showcase)

### Other

[Deploy with Flightcontrol](https://flightcontrol.dev/?ref=blitzjs)[GitHub](https://github.com/blitz-js/blitz)[Wiki](https://github.com/blitz-js/blitz/wiki)[Swag](https://store.blitzjs.com/)

[Hosted on Vercel](https://vercel.com/?utm_source=blitzjs)

Copyright © 2026 Brandon Bayer and Blitz.js Contributors
