# Source: https://docs.redwoodjs.com/docs/prerender

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Prerender]

[Version: 8.8]

On this page

<div>

# Prerender

</div>

Prerendering is great for providing a faster experience for your end users. Your pages will be rendered at build-time, saving your user\'s browser from having to do that job.

We thought a lot about what the developer experience should be for route-based prerendering. The result is one of the smallest APIs imaginable!

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]How\'s Prerendering different from SSR/SSG/SWR/ISSG/\...?

As Danny said in his [Prerender demo](https://www.youtube.com/watch?v=iorKyMlASZc&t=2844s) at our Community Meetup, the thing all of these have in common is that they render your markup in a Node.js context to produce HTML. The difference is when (build or runtime) and how often.

Redwood currently supports prerendering at *build* time. So before you deploy your web side, Redwood will render your pages into HTML, and once the JavaScript has been loaded on the browser, the page becomes dynamic.

## Prerendering a Page[​](#prerendering-a-page "Direct link to Prerendering a Page") 

Prerendering a page is as easy as it gets. Just add the `prerender` prop to the Route that you want to prerender:

Routes.js

``` 
<Route path="/" page= name="home" prerender/>
```

Then run `yarn rw build` and enjoy the performance boost!

### Prerendering all pages in a Set[​](#prerendering-all-pages-in-a-set "Direct link to Prerendering all pages in a Set") 

Just add the `prerender` prop to the Set that wraps all Pages you want to prerender:

Routes.js

``` 
<Set prerender>
  <Route path="/" page= name="home" />
  <Route path="/about" page= name="hello" />
</Set>
```

### Not found page[​](#not-found-page "Direct link to Not found page") 

You can also prerender your not found page (a.k.a your 404 page). Just add---you guessed it---the `prerender` prop:

``` 
-      <Route notfound page= />
+      <Route notfound page= prerender/>
```

This will prerender your NotFoundPage to `404.html` in your dist folder. Note that there\'s no need to specify a path.

## Private Routes[​](#private-routes "Direct link to Private Routes") 

For Private Routes, Redwood prerenders your Private Routes\' `whileLoadingAuth` prop:

``` 
<PrivateSet>
  // Loading is shown while we're checking to see if the user's logged in
  <Route path="/super-secret-admin-dashboard" page= name="ssad" whileLoadingAuth= prerender/>
</PrivateSet>
```

### Rendering skeletons while authenticating[​](#rendering-skeletons-while-authenticating "Direct link to Rendering skeletons while authenticating") 

Sometimes you want to render the shell of the page, while you wait for your authentication checks to happen. This can make the experience feel a lot snappier to the user, since they don\'t wait on a blank screen while their credentials are checked.

To do this, make use of the `whileLoadingAuth` prop on `<PrivateSet>` in your Routes file. For example, if we have a dashboard that you need to be logged in to access:

``` 
// This renders the layout with skeleton loaders in the content area
const DashboardLoader = () => <DashboardLayout skeleton />

const Routes = () =>  name="home" prerender />
       <Set
        private
        wrap=
        unauthenticated="login"
        // 👇 tell the router to render the shell until the user has been authenticated
        whileLoadingAuth=
        prerender
      >
        <Route path="/dashboard" page= name="dashboard"/>
      
```

## Dynamic routes & Route Hooks[​](#dynamic-routes--route-hooks "Direct link to Dynamic routes & Route Hooks") 

Let\'s say you have a route like this

``` 
<Route path="/blog-post/" page= name="blogPost" prerender />
```

To be able to prerender this route you need to let Redwood know what `id`s to use. Why? Because when we are prerendering your pages - at build time - we don\'t know the full URL i.e. `site.com/blog-post/1` vs `site.com/blog-post/3`. It\'s up to you to decide whether you want to prerender *all* of the ids, or if there are too many to do that, if you want to only prerender the most popular or most likely ones.

You do this by creating a `BlogPostPage.routeHooks.js` file next to the page file itself (so next to `BlogPostPage.js` in this case). It should export a function called `routeParameters` that returns an array of objects that specify the route parameters that should be used for prerendering.

So for example, for the route `/blogPost/` - you would return `[ ,  ]` which would tell Redwood to prerender `/blogPost/55` and `/blogPost/77`

A single Page component can be used for different routes too! Metadata about the current route will be passed as an argument to `routeParameters` so you can return different route parameters depending on what route it is, if you need to. An example will hopefully make all this clearer.

For the example route above, all you need is this:

BlogPostPage.routeHooks.js

``` 
export function routeParameters() , , ]
}
```

Or, if you wanted to get fancy

BlogPostPage.routeHooks.js

``` 
export function routeParameters(route)  and
  // /blogPost/ we can choose what parameters to pass to each route during
  // prerendering
  if (route.name === 'odd') , , ]
  } else , , ]
  }
}
```

With the config above three separate pages will be written: `web/dist/blog-post/1.html`, `web/dist/blog-post/2.html`, `web/dist/blog-post/3.html`. A word of warning - if it\'s just a few pages like this, it\'s no problem - but this can easily and quickly explode to thousands of pages, which could slow down your builds and deployments significantly (and make them costly, depending on how you\'re billed).

In these routeHooks scripts you have full access to your database using prisma and all your services, should you need it. You use `import  from '$api/src/lib/db'` to get access to the `db` object.

BlogPostPage.routeHooks.js

``` 
import  from '$api/src/lib/db'

export async function routeParameters() )).map((post) => ())
}
```

Take note of the special syntax for the import, with a dollar-sign in front of api. This lets our tooling (typescript and babel) know that you want to break out of the web side the page is in to access code on the api side. This only works in the routeHook scripts (and scripts in the root /scripts directory).

------------------------------------------------------------------------

## Prerender Utils[​](#prerender-utils "Direct link to Prerender Utils") 

Sometimes you need more fine-grained control over whether something gets prerendered. This may be because the component or library you\'re using needs access to browser APIs like `window` or `localStorage`. Redwood has three utils to help you handle these situations:

-   `<BrowserOnly>`
-   `useIsBrowser`
-   `isBrowser`

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]Heads-up!

If you\'re prerendering a page that uses a third-party library, make sure it\'s \"universal\". If it\'s not, try calling the library after doing a browser check using one of the utils above.

Look for these key words when choosing a library: *universal module, SSR compatible, server compatible*---all these indicate that the library also works in Node.js.

### `<BrowserOnly/>` component[​](#browseronly-component "Direct link to browseronly-component") 

This higher-order component is great for JSX:

``` 
import  from '@redwoodjs/prerender/browserUtils'

const MyFancyComponent = () => 
```

### `useIsBrowser` hook[​](#useisbrowser-hook "Direct link to useisbrowser-hook") 

If you prefer hooks, you can use the `useIsBrowser` hook:

``` 
import  from '@redwoodjs/prerender/browserUtils'

const MySpecialComponent = () => 
    </div>
  )
}
```

### `isBrowser` boolean[​](#isbrowser-boolean "Direct link to isbrowser-boolean") 

If you need to guard against prerendering outside React, you can use the `isBrowser` boolean. This is especially handy when running initializing code that only works in the browser:

``` 
import  from '@redwoodjs/prerender/browserUtils'

if (isBrowser) 
```

### Debugging[​](#debugging "Direct link to Debugging") 

If you just want to debug your app, or check for possible prerendering errors, after you\'ve built it, you can run this command:

``` 
yarn rw prerender --dry-run
```

We\'re actively looking for feedback! Do let us know if: everything built ok? you encountered specific libraries that you were using that didn't work?

------------------------------------------------------------------------

## Images and Assets[​](#images-and-assets "Direct link to Images and Assets") 

Images and assets continue to work the way they used to. For more, see [this doc](/docs/assets-and-files).

Note that there\'s a subtlety in how SVGs are handled. Importing an SVG and using it in a component works great:

``` 
import logo from './my-logo.svg'

function Header() 
```

But re-exporting the SVG as a component requires a small change:

``` 
// ❌ due to how Redwood handles SVGs, this syntax isn't supported.
import Logo from './Logo.svg'
export default Logo
```

``` 
// ✅ use this instead.
import Logo from './Logo.svg'

const LogoComponent = () => <Logo />

export default LogoComponent
```

------------------------------------------------------------------------

## Cell prerendering[​](#cell-prerendering "Direct link to Cell prerendering") 

As of v3.x, Redwood supports prerendering your Cells with the data you were querying. There\'s no special config to do here, but a couple of things to note:

#### 1. Prerendering always happens as an unauthenticated user[​](#1-prerendering-always-happens-as-an-unauthenticated-user "Direct link to 1. Prerendering always happens as an unauthenticated user") 

Because prerendering happens at *build* time, before any authentication is set, all your queries on a Route marked for prerender will be made as a public user

#### 2. We use your graphql handler to make queries during prerendering[​](#2-we-use-your-graphql-handler-to-make-queries-during-prerendering "Direct link to 2. We use your graphql handler to make queries during prerendering") 

When prerendering we look for your graphql function defined in `./api/src/functions/graphql.` and use it to run queries against it.

### Common Warnings & Errors[​](#common-warnings--errors "Direct link to Common Warnings & Errors") 

#### Could not load your GraphQL handler - the Loading fallback[​](#could-not-load-your-graphql-handler---the-loading-fallback "Direct link to Could not load your GraphQL handler - the Loading fallback") 

During builds if you encounter this warning

``` 
⚠️ Could not load your GraphQL handler.
Your Cells have been prerendered in the "Loading" state.
```

It could mean one of two things:

a\) We couldn\'t locate the GraphQL handler at the usual path

or

b\) There was an error when trying to import your GraphQL handler - maybe due to missing dependencies or an error in the code

If you\'ve moved this GraphQL function, or we encounter an error executing it, it won\'t break your builds. All your Cells will be prerendered in their `Loading` state, and will update once the JavaScript loads on the browser. This is effectively skipping prerendering your Cells, but they\'ll still work!

#### Cannot prerender the query  as it requires auth.[​](#cannot-prerender-the-query-queryname-as-it-requires-auth "Direct link to Cannot prerender the query  as it requires auth.") as it requires auth."} 

This error happens during builds when you have a Cell on a page you\'re prerendering that makes a query marked with `@requireAuth` in your SDL.

During prerender you are not logged in ([see point 1](#1-prerendering-always-happens-as-an-unauthenticated-user)), so you\'ll have to conditionally render the Cell - for example:

``` 
import  from '@redwoodjs/auth'

const HomePage = () =>  = useAuth

  return (
    <>
      
    </>
```

------------------------------------------------------------------------

## Optimization Tips[​](#optimization-tips "Direct link to Optimization Tips") 

### Dynamically loading large libraries[​](#dynamically-loading-large-libraries "Direct link to Dynamically loading large libraries") 

If you dynamically load third-party libraries that aren\'t part of your JS bundle, using these prerendering utils can help you avoid loading them at build time:

``` 
import  from '@redwoodjs/prerender/browserUtils'

const ComponentUsingAnExternalLibrary = () => 

  return (
    // ...
  )
```

### Configuring redirects[​](#configuring-redirects "Direct link to Configuring redirects") 

Depending on what pages you\'re prerendering, you may want to change your redirect settings. Keep in mind your redirect settings will vary a lot based on what routes you are prerendering, and the settings of your deployment provider.

Using Netlify as an example:

If you prerender your `notFoundPage`, and all your other routes

<div>

You can remove the default redirect to index in your `netlify.toml`. This means the browser will accurately receive 404 statuses when navigating to a route that doesn\'t exist:

``` 
[[redirects]]
- from = "/*"
- to = "/index.html"
- status = 200
```

This makes your app behave much more like a traditional website, where all the possible routes are defined up front. But take care to make sure you are prerendering all your pages, otherwise you will receive 404s on pages that do exist, but that Netlify hasn\'t been told about.

</div>

If you don\'t prerender your 404s, but prerender all your other pages

<div>

You can add a 404 redirect if you want:

``` 
[[redirects]]
  from = "/*"
  to = "/index.html"
- status = 200
+ status = 404
```

This makes your app behave much more like a traditional website, where all the possible routes are defined up front. But take care to make sure you are prerendering all your pages, otherwise you will receive 404s on pages that do exist, but that Netlify hasn\'t been told about.

</div>

### Flash after page load[​](#flash-after-page-load "Direct link to Flash after page load") 

You might notice a flash after page load. Prerendering pages still has various benefits (such as SEO), but may seem jarring to users if there\'s a flash.

A quick workaround for this is to make sure whatever page you\'re seeing the flash on isn\'t dynamically loaded i.e. prevent code splitting. You can do this by explicitly importing the page in `Routes.js`:

``` 
import  from '@redwoodjs/router'
// We don't want HomePage to be dynamically loaded
import HomePage from 'src/pages/HomePage'

const Routes = () =>  name="hello" prerender />
      <Route path="/about" page= name="hello" />
      <Route notfound page= />
    </Router>
  )
}

export default Routes
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/prerender.md)