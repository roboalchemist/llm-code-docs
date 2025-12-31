# Source: https://docs.redwoodjs.com/docs/auth/clerk

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Authentication](/docs/authentication)
-   [Clerk]

[Version: 8.8]

On this page

<div>

# Clerk Authentication

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Did you set up Clerk a while ago?

If you set up Clerk a while ago, you may be using a deprecated `authDecoder` that\'s subject to rate limiting. This decoder will be removed in the next major. There\'s a new decoder you can use right now! See the [migration guide](https://github.com/redwoodjs/redwood/releases/tag/v5.3.2) for how to upgrade.

To get started, run the setup command:

``` 
yarn rw setup auth clerk
```

This installs all the packages, writes all the files, and makes all the code modifications you need. For a detailed explanation of all the api- and web-side changes that aren\'t exclusive to Clerk, see the top-level [Authentication](/docs/authentication) doc. But for now, let\'s focus on Clerk\'s side of things.

If you don\'t have a Clerk account yet, now\'s the time to make one: navigate to [https://clerk.dev](https://clerk.dev), sign up, and create an application. The defaults are good enough to get us going, but feel free to configure things as you wish. We\'ll get the application\'s API keys from its dashboard next.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]we\'ll only focus on the development instance

By default, Clerk applications have two instances, \"Development\" and \"Production\". We\'ll only focus on the \"Development\" instance here, which is used for local development. When you\'re ready to deploy, switch the instance the dashboard is displaying by clicking \"Development\" in the header at the top. How you get your API keys to production depends on your deploy provider.

After you create the application, you should be redirected to its dashboard where you should see the RedwoodJS logo. Click on it and copy the two API keys it shows into your project\'s `.env` file:

.env

``` 
CLERK_PUBLISHABLE_KEY="..."
CLERK_SECRET_KEY="..."
```

Lastly, in your project\'s `redwood.toml` file, include `CLERK_PUBLISHABLE_KEY` in the list of env vars that should be available to the web side:

redwood.toml

``` 
[web]
  # ...
  includeEnvironmentVariables = [
    "CLERK_PUBLISHABLE_KEY",
  ]
```

That should be enough; now, things should just work. Let\'s make sure: if this is a brand new project, generate a home page:

``` 
yarn rw g page Home /
```

There we\'ll try to sign up by destructuring `signUp` from the `useAuth` hook (import that from `'src/auth'`). We\'ll also destructure and display `isAuthenticated` to see if it worked:

web/src/pages/HomePage/HomePage.tsx

``` 
import  from 'src/auth'

const HomePage = () =>  = useAuth()

  return (
    <>
      

      <p>)}</p>
      <button onClick=>sign up</button>
    </>
  )
}
```

Clicking sign up should open a sign-up box and after you sign up, you should see `` on the page.

## Customizing the session token[​](#customizing-the-session-token "Direct link to Customizing the session token") 

There\'s not a lot to the default session token. Besides the standard claims, the only thing it really has is the user\'s `id`. Eventually, you\'ll want to customize it so that you can get back more information from Clerk. You can do so by navigating to the \"Sessions\" section in the nav on the left, then clicking on \"Edit\" in the \"Customize session token\" box:

![clerk_customize_session_token](https://github.com/redwoodjs/redwood/assets/32992335/6d30c616-b4d2-4b44-971b-8addf3b79e5a)

As long as you\'re using the `clerkJwtDecoder` all the properties you add will be available to the `getCurrentUser` function:

api/src/lib/auth.ts

``` 
export const getCurrentUser = async (
  decoded, // 👈 All the claims you add will be available on the `decoded` object
  // ...
) => 
```

## Avoiding feature duplication[​](#avoiding-feature-duplication "Direct link to Avoiding feature duplication") 

Redwood\'s Clerk integration is based on [Clerk\'s React SDK](https://clerk.dev/docs/reference/clerk-react/installation). This means that there\'s some duplication between the features in the SDK and the ones in `@redwoodjs/auth-clerk-web`. For example, the SDK ha a `SignedOut` component that redirects a user away from a private page---very much like wrapping a route with Redwood\'s `Private` component. We recommend you use Redwood\'s way of doing things as much as possible since it\'s much more likely to get along with the rest of the framework.

## Deep dive: the `ClerkStatusUpdater` component[​](#deep-dive-the-clerkstatusupdater-component "Direct link to deep-dive-the-clerkstatusupdater-component") 

With Clerk, there\'s a bit more going on in the `web/src/auth.tsx` file than other auth providers. This is because Clerk is a bit unlike the other auth providers Redwood integrates with in that it puts an instance of its client SDK on the browser\'s `window` object. That means Redwood has to wait for it to be ready. With other providers, Redwood instantiates their client SDK in `web/src/auth.ts`, then passes it to `createAuth`. With Clerk, instead Redwood uses Clerk components and hooks, like `ClerkLoaded` and `useUser`, to update Redwood\'s auth context with the client when it\'s ready.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/auth/clerk.md)