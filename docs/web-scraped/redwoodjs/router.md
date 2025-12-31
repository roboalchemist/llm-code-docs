# Source: https://docs.redwoodjs.com/docs/router

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Router]

[Version: 8.8]

On this page

<div>

# Router

</div>

This is the built-in router for Redwood apps. It takes inspiration from Ruby on Rails, React Router, and Reach Router, but is very opinionated in its own way.

The router is designed to list all routes in a single file, with limited nesting. We prefer this design, as it makes it very easy to track which routes map to which pages.

## Router and Route[​](#router-and-route "Direct link to Router and Route") 

The first thing you need is a `Router`. It will contain all of your routes. The router will attempt to match the current URL to each route in turn, and only render those with a matching `path`. The only exception to this is the `notfound` route, which can be placed anywhere in the list and only matches when no other routes do.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]The `notfound` route can\'t be nested in a `Set`

If you want to wrap your custom notfound page in a `Layout`, then you should add the `Layout` to the page instead. See [customizing the NotFoundPage](#customizing-the-notfoundpage).

Each route is specified with a `Route`. Our first route will tell the router what to render when no other route matches:

Routes.jsx

``` 
import  from '@redwoodjs/router'

const Routes = () => (
  <Router>
    <Route notfound page= />
  </Router>
)

export default Routes
```

The router expects a single `Route` with a `notfound` prop. When no other route is found to match, the component in the `page` prop will be rendered.

To create a route to a normal Page, you\'ll pass three props: `path`, `page`, and `name`:

Routes.jsx

``` 
<Route path="/" page= name="home" />
```

The `path` prop specifies the URL path to match, starting with the beginning slash. The `page` prop specifies the Page component to render when the path is matched. The `name` prop is used to specify the name of the *named route function*.

## Private Routes[​](#private-routes "Direct link to Private Routes") 

Some pages should only be visible to authenticated users. We support this using the `PrivateSet` component. Read more [further down](#privateset).

## Redirect Routes[​](#redirect-routes "Direct link to Redirect Routes") 

If you move a page you might still want to keep the old route around, so that old links to your site keep working. To this end RedwoodJS supports the `redirect` prop on routes, which allows you to specify the name of the route you want to redirect to:

Routes.jsx

``` 
<Route path="/blog/" redirect="post" />
<Route path="/posts/" page="PostPage" name="post" />
```

When doing redirects the original path parameters are also passed to the page the user is redirected to. So, in the example above, if a user goes to `/blog/5` they will be redirected to `/posts/5`.

For redirect routes the `name` prop is optional. If you want to be able to keep using old route names in your code you can keep the name around. If you want to update them all you can remove the name prop and you\'ll get TypeScript errors everywhere it\'s used. You can also decide to reuse the name for your new route, and all existing links in your code will continue to just work.

If you prefer, you can also specify the path of the route you want to redirect to:

Routes.jsx

``` 
<Route path="/blog/" redirect="/posts/" />
<Route path="/posts/" page="PostPage" name="post" />
```

## Sets of Routes[​](#sets-of-routes "Direct link to Sets of Routes") 

You can group Routes into sets using the `Set` component. `Set` allows you to wrap a set of Routes in another component or array of components---usually a Context, a Layout, or both:

Routes.jsx

``` 
import  from '@redwoodjs/router'
import BlogContext from 'src/contexts/BlogContext'
import BlogLayout from 'src/layouts/BlogLayout'

const Routes = () => >
        <Route path="/" page= name="home" />
        <Route path="/about" page= name="about" />
        <Route path="/contact" page= name="contact" />
        <Route path="/blog-post/" page= name="blogPost" />
      </Set>
    </Router>
  )
}

export default Routes
```

The `wrap` prop accepts a single component or an array of components. Components are rendered in the same order they\'re passed, so in the example above, Set expands to:

``` 
<BlogContext>
  <BlogLayout>
    <Route path="/" page= name="home" />
    // ...
  </BlogLayout>
</BlogContext>
```

Conceptually, this fits with how we think about Context and Layouts as things that wrap Pages and contain content that's outside the scope of the Pages themselves. Crucially, since they\'re higher in the tree, `BlogContext` and `BlogLayout` won\'t rerender across Pages in the same Set.

There\'s a lot of flexibility here. You can even nest `Sets` to great effect:

Routes.jsx

``` 
import  from '@redwoodjs/router'
import BlogContext from 'src/contexts/BlogContext'
import BlogLayout from 'src/layouts/BlogLayout'
import BlogNavLayout from 'src/layouts/BlogNavLayout'

const Routes = () => >
        <Route path="/" page= name="home" />
        <Route path="/about" page= name="about" />
        <Route path="/contact" page= name="contact" />
        <Set wrap=>
          <Route path="/blog-post/" page= name="blogPost" />
        </Set>
      </Set>
    </Router>
  )
}
```

### Forwarding props[​](#forwarding-props "Direct link to Forwarding props") 

All props you give to `<Set>` (except for `wrap`) will be passed to the wrapper components.

So this\...

``` 
<Set wrap= theme="dark">
  <Route path="/" page= name="home" />
</Set>
```

becomes\...

``` 
<MainLayout theme="dark">
  <Route path="/" page= name="home" />
</MainLayout>
```

### `PrivateSet`[​](#privateset "Direct link to privateset") 

A `PrivateSet` makes all Routes inside that Set require authentication. When a user isn\'t authenticated and attempts to visit one of the Routes in the `PrivateSet`, they\'ll be redirected to the Route passed as the `PrivateSet`\'s `unauthenticated` prop. The originally-requested Route\'s path is added to the query string as a `redirectTo` param. This lets you send the user to the page they originally requested once they\'re logged-in.

Here\'s an example of how you\'d use a `PrivateSet`:

Routes.jsx

``` 
<Router useAuth=>
  <Route path="/" page= name="home" />
  <PrivateSet unauthenticated="home">
    <Route path="/admin" page= name="admin" />
  </PrivateSet>
</Router>
```

For more fine-grained control, you can specify `roles` (which takes a string for a single role or an array of roles), and the router will check to see that the current user is authorized before giving them access to the Route. If they\'re not, they will be redirected to the page specified in the `unauthenticated` prop, such as a \"forbidden\" page. Read more about Role-based Access Control in Redwood [here](/docs/how-to/role-based-access-control-rbac).

To protect private routes for access by a single role:

Routes.jsx

``` 
<Router useAuth=>
  <PrivateSet unauthenticated="forbidden" roles="admin">
    <Route path="/admin/users" page= name="users" />
  </PrivateSet>

  <Route path="/forbidden" page= name="forbidden" />
</Router>
```

To protect private routes for access by multiple roles:

Routes.jsx

``` 
<Router useAuth=>
  <PrivateSet unauthenticated="forbidden" roles=>
    <Route path="/admin/posts//edit" page= name="editPost" />
  </PrivateSet>

  <Route path="/forbidden" page= name="forbidden" />
</Router>
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Note about roles

A route is permitted when authenticated and user has **any** of the provided roles such as `"admin"` or `["admin", "editor", "publisher"]`.

Redwood uses the `useAuth` hook under the hood to determine if the user is authenticated. Read more about authentication in Redwood [here](/docs/tutorial/chapter4/authentication).

## Link and named route functions[​](#link-and-named-route-functions "Direct link to Link and named route functions") 

When it comes to routing, matching URLs to Pages is only half the equation. The other half is generating links to your pages. The router makes this really simple without having to hardcode URL paths. In a Page component, you can do this (only relevant bits are shown in code samples from now on):

SomePage.jsx

``` 
import  from '@redwoodjs/router'

// Given the route in the last section, this produces: <a href="/">
const SomePage = () => <Link to= />
```

You use a `Link` to generate a link to one of your routes and can access URL generators for any of your routes from the `routes` object. We call the functions on the `routes` object *named route functions* and they are named after whatever you specify in the `name` prop of the `Route`.

Named route functions simply return a string, so you can still pass in hardcoded strings to the `to` prop of the `Link` component, but using the proper named route function is easier and safer. Plus, if you ever decide to change the `path` of a route, you don\'t need to change any of the `Link`s to it (as long as you keep the `name` the same)!

## Active links[​](#active-links "Direct link to Active links") 

`NavLink` is a special version of `Link` that will switch to the `activeClassName` classes for the rendered element when it matches the current URL.

MainMenu.jsx

``` 
import  from '@redwoodjs/router'

const MainMenu = () =>
  <ul>
    <li>
      <!--
        Normally renders as `<a className="link homeLink" ...>`, but when the
        URL matches "/" it'll switch to render
        `<a className="activeLink homeLink" ...>`
      -->
      <NavLink
        className="link homeLink"
        activeClassName="activeLink homeLink"
        to=>
        Home
      </NavLink>
    </li>
    <li>
      <!--
        Normally renders as `<a className="link" ...>`, but when the URL
        matches "/?tab=tutorial" (params order insensitive) it'll switch to
        render `<a className="activeLink" ...>`
      -->
      <NavLink
        className="link"
        activeClassName="activeLink"
        to=)}>
          Home > Tutorial
      </NavLink>
    </li>
  </ul>
```

The `activeMatchParams` prop can be used to control how query params are matched:

``` 
import  from '@redwoodjs/router'

// Will render <a href="/?tab=tutorial&page=2" className="activeLink"> when on
// any Home tutorial page
const MainMenu = () => (
  <li>
    <NavLink
      className="link"
      activeClassName="activeLink"
      activeMatchParams=]}
      to=)}
    >
      Home > Tutorial
    </NavLink>
  </li>
)
```

> Note `activeMatchParams` is an array of `string` *(key only)* or `Record<string, any>` *(key and value)*

More granular match; needs to be on the tutorial tab (`tab=tutorial`) and have the `page` key specified:

``` 
// Match /?tab=tutorial&page=*
activeMatchParams=, 'page' ]}
```

### useMatch[​](#usematch "Direct link to useMatch") 

You can use `useMatch` to create your own component with active styles.

> `NavLink` uses it internally!

``` 
import  from '@redwoodjs/router'

const CustomLink = () =>  to= isActive= />
}

const MainMenu = () =>  />
}
```

`useMatch` accepts `searchParams` in the `options` for matching granularity which is exactly the same as `activeMatchParams` of `NavLink`

``` 
import  from '@redwoodjs/router'

const CustomLink = () => , 'page'] })

  return <SomeStyledComponent as= to= isActive= />
}
```

Passing in `routeParams` you can make it match only on specific route parameter values.

``` 
const match = useMatch('/product//', ,
})
```

The above example will match /product/shirts/213, but not /product/pants/213 (whereas not specifying `routeParams` at all would match both).

To get the path you need to pass to `useMatch` you can use [`useRoutePaths`](#useroutepaths) or [`useRoutePath`](#useroutepath)

Here\'s an example:

``` 
<Route path="//" page= name="animal" />

const animalRoutePath = useRoutePath('animal')
// => '//'

const matchOnlyDog = useMatch(animalRoutePath, })
const matchFullyDynamic = useMatch(animalRoutePath)
```

In the above example, if the current page url was `https://example.org/dog/fido` then both `matchOnlyDog` and `matchFullyDynamic` would have `match: true`.

If the current page instead was `https://example.org/cat/garfield` then only `matchFullyDynamic` would match

See below for more info on route parameters.

## Route parameters[​](#route-parameters "Direct link to Route parameters") 

To match variable data in a path, you can use route parameters, which are specified by a parameter name surrounded by curly braces:

Routes.jsx

``` 
<Route path="/user/" page= name="user" />
```

This route will match URLs like `/user/7` or `/user/mojombo`. You can have as many route parameters as you like:

Routes.jsx

``` 
<Route path="/blog////" page= name="post" />
```

By default, route parameters will match up to the next slash or end-of-string. Once extracted, the route parameters are sent as props to the Page component. In the 2nd example above, you can receive them like so:

PostPage.jsx

``` 
const PostPage = () => 
```

## Named route functions with parameters[​](#named-route-functions-with-parameters "Direct link to Named route functions with parameters") 

If a route has route parameters, then its named route function will take an object of those same parameters as an argument:

SomePage.jsx

``` 
<Link to=)}>...</Link>
```

All parameters will be converted to strings before being inserted into the generated URL. If you don\'t like the default JavaScript behavior of how this conversion happens, make sure to convert to a string before passing it into the named route function.

If you specify parameters to the named route function that do not correspond to parameters defined on the route, they will be appended to the end of the generated URL as search params in `key=val` format:

SomePage.jsx

``` 
<Link to=)}>...</Link>
// => "/users?sort=desc&filter=all"
```

## Route parameter types[​](#route-parameter-types "Direct link to Route parameter types") 

Route parameters are extracted as strings by default, but they will often represent typed data. The router offers a convenient way to auto-convert certain types right in the `path` specification:

Routes.jsx

``` 
<Route path="/user/" page= name="user" />
```

By adding `:Int` onto the route parameter, you are telling the router to only match `/\d+/` and then use `Number()` to convert the parameter into a number. Now, instead of a string being sent to the Page, a number will be sent! This means you could have both a route that matches numeric user IDs **and** a route that matches string IDs:

Routes.jsx

``` 
<Route path="/user/" page= name="userInt" />
<Route path="/user/" page= name="userString" />
```

Now, if a request for `/user/mojombo` comes in, it will fail to match the first route, but will succeed in matching the second.

## Core route parameter types[​](#core-route-parameter-types "Direct link to Core route parameter types") 

We call built-in parameter types *core parameter types*. All core parameter types begin with a capital letter. Here are the types:

-   `Int` - Matches and converts an integer.
-   `Float` - Matches and converts a Float.
-   `Boolean` - Matches and converts Boolean (true or false only)

> Note on TypeScript support Redwood will automatically generate types for your named routes, but you do have to run `yarn redwood dev` or `yarn redwood build` at least once for your `Routes.ts` to be parsed

### Glob Type[​](#glob-type "Direct link to Glob Type") 

There is one more core type that is a bit different: the glob type. Instead of matching to the next `/` or the end of the string, it will greedily match as much as possible (including `/` characters) and capture the match as a string.

Routes.jsx

``` 
<Route path="/file/" page= name="file" />
```

In this example, we want to take everything after `/file/` and have it sent to the Page as `filePath`. So for the path `/file/api/src/lib/auth.js`, `filePath` would contain `api/src/lib/auth.js`.

You can use multiple globs in your paths:

Routes.jsx

``` 
<Route path="/from//to/" page= name="dateRange" />
```

This will match a path like `/from/2021/11/03/to/2021/11/17`. Note that for this to work, there must be some static string between the globs so the router can determine where the boundaries of the matches should be.

## User route parameter types[​](#user-route-parameter-types "Direct link to User route parameter types") 

The router goes even further, allowing you to define your own route parameter types. Your custom types must begin with a lowercase letter. You can specify them like so:

Routes.jsx

``` 
const userRouteParamTypes = ,
}

<Router paramTypes=>
  <Route path="/post/" page= name= />
</Router>
```

Here we\'ve created a custom `slug` route parameter type. It is defined by `match` and `parse`. Both are optional; the default `match` regexp is `/[^/]+/` and the default `parse` function is `(param) => param`.

In the route we\'ve specified a route parameter of `` which will invoke our custom route parameter type and if we have a request for `/post/redwood-router`, the resulting `name` prop delivered to `PostPage` will be `['redwood', 'router']`.

## Trailing slashes[​](#trailing-slashes "Direct link to Trailing slashes") 

The router by default removes all trailing slashes before attempting to match the route you are trying to navigate to.

For example, if you attempt to navigate to `/about` and you enter `/about/`, the router will remove the trailing `/` and will match `path="/about"`

There are 3 values that can be used with the `trailingSlashes` prop

1.  **never** (default): strips trailing slashes before matching (\"/about/\" -\> \"/about\")
2.  **always**: always adds trailing slashes before matching (\"/about\" -\> \"/about/\")
3.  **preserve** -\> paths without a slash won\'t match paths with a slash (\"/about\" -\> \"/about\", \"/about/\" -\> \"/about/\")

If you need to match trailing slashes exactly, use the `preserve` value. In the following example, `/about/` will *not* match `/about` and you will be sent to the `NotFoundPage`

``` 
<Router trailingSlashes=>
  <Route path="/" page= name="home" />
  <Route path="/about" page= name="about" />
  <Route notfound page= />
</Router>
```

## useParams[​](#useparams "Direct link to useParams") 

Sometimes it\'s convenient to receive route parameters as the props to the Page, but in the case where a deeply nested component needs access to the route parameters, it quickly becomes tedious to pass those props through every intervening component. The router solves this with the `useParams` hook:

SomeDeeplyNestedComponent.jsx

``` 
import  from '@redwoodjs/router'

const SomeDeeplyNestedComponent = () =>  = useParams()
  ...
}
```

In the above example, we\'ve pulled in the `id` route parameter without needing to have it passed in to us from anywhere.

## useLocation[​](#uselocation "Direct link to useLocation") 

If you\'d like to get access to the current URL, `useLocation` returns a read-only location object representing it. The location object has three properties, [pathname](https://developer.mozilla.org/en-US/docs/Web/API/Location/pathname), [search](https://developer.mozilla.org/en-US/docs/Web/API/Location/search), and [hash](https://developer.mozilla.org/en-US/docs/Web/API/Location/hash), that update when the URL changes. This makes it easy to fire off navigation side effects or use the URL as if it were state:

``` 
import  from '@redwoodjs/router'

const App = () =>  = useLocation()

  // log the URL when the pathname changes
  React.useEffect(() => , [pathname])

  // initiate a query state with the search val
  const [query, setQuery] = React.useState(search)

  // conditionally render based on hash
  if (hash === '#ping') 

  return <>...</>
}
```

## useRoutePaths[​](#useroutepaths "Direct link to useRoutePaths") 

`useRoutePaths()` is a React hook you can use to get a map of all routes mapped to their literal paths, as they\'re defined in your routes file.

Example usage:

``` 
const routePaths = useRoutePaths()

return <pre><code></code></pre>
```

Example output:

``` 
/edit",
  "contact": "/contacts/",
  "contacts": "/contacts",
}
```

## useRoutePath[​](#useroutepath "Direct link to useRoutePath") 

Use this hook when you only want the path for a single route. By default it will give you the path for the current route

``` 
// returns "/about" if you're currently on https://example.org/about
const aboutPath = useRoutePath()
```

You can also pass in the name of a route and get the path for that route

``` 
// returns "/about"
const aboutPath = useRoutePath('about')
```

Note that the above is the same as

``` 
const routePaths = useRoutePaths()
// returns "/about"
const aboutPath = routePaths.about
```

## useRouteName[​](#useroutename "Direct link to useRouteName") 

Use the `useRouteName()` hook to get the name of the current route (the page the user is currently visiting). The name can then also be used with `routes` if you need to dynamically get the url to the current page:

``` 
const routeName = useRouteName()
const routeUrl = routeName ? routes[routeName]() : undefined
```

## Navigation[​](#navigation "Direct link to Navigation") 

### navigate[​](#navigate "Direct link to navigate") 

If you\'d like to programmatically navigate to a different page, you can simply use the `navigate` function:

SomePage.jsx

``` 
import  from '@redwoodjs/router'

const SomePage = () => 
  ...
}
```

The browser keeps track of the browsing history in a stack. By default when you navigate to a new page a new item is pushed to the history stack. But sometimes you want to replace the top item on the stack instead of appending to the stack. This is how you do that in Redwood: `navigate(routes.home(), )`. As you can see you need to pass an options object as the second parameter to `navigate` with the option `replace` set to `true`.

By default `navigate` will scroll to the top after navigating to a new route (except for hash param changes), we can prevent this behavior by setting the `scroll` option to false: `navigate(routes.home(), )`

### back[​](#back "Direct link to back") 

Going back is as easy as using the `back()` function that\'s exported from the router.

SomePage.jsx

``` 
import  from '@redwoodjs/router'

const SomePage = () => 
  ...
}
```

## Blocking[​](#blocking "Direct link to Blocking") 

### useBlocker[​](#useblocker "Direct link to useBlocker") 

The `useBlocker` hook allows you to prevent navigation away from a page under certain conditions. This is useful for scenarios such as preventing a user from accidentally navigating away from a form with unsaved changes.

``` 
import  from '@redwoodjs/router'
import  from '@redwoodjs/forms'

const SomeForm = () => )

  return (
    <Form formMethods= onSubmit= error=>
      >
            Confirm
          </button>
          <button type="button" onClick=>
            Abort
          </button>
        </div>
      )}
      ...
    </Form>
  )
}
```

## Redirect[​](#redirect "Direct link to Redirect") 

If you want to declaratively redirect to a different page, use the `<Redirect>` component.

In the example below, SomePage will redirect to the home page.

SomePage.jsx

``` 
import  from '@redwoodjs/router'

const SomePage = () => <Redirect to= />
```

In addition to the `to` prop, `<Redirect />` also takes an `options` prop. This is the same as [`navigate()`](#navigate)\'s second argument: `navigate(_, )`. We can use it to *replace* the top item of the browser history stack (instead of pushing a new one). This is how you use it to have this effect: `<Redirect to= options=}/>`.

By default redirect will scroll to the top after navigating to a new route (except for hash param changes), we can prevent this behavior by setting the `scroll` option to false: `<Redirect to= options=}/>`

## Code-splitting[​](#code-splitting "Direct link to Code-splitting") 

By default, the router will code-split on every Page, creating a separate lazy-loaded bundle for each. When navigating from page to page, the router will wait until the new Page module is loaded before re-rendering, thus preventing the \"white-flash\" effect.

## Not code splitting[​](#not-code-splitting "Direct link to Not code splitting") 

If you\'d like to override the default lazy-loading behavior and include certain Pages in the main bundle, you can simply add the import statement to the `Routes.js` file:

Routes.jsx

``` 
import HomePage from 'src/pages/HomePage'
```

Redwood will detect your explicit import and refrain from splitting that page into a separate bundle. Be careful with this feature, as you can easily bloat the size of your main bundle to the point where your initial page load time becomes unacceptable.

## Page loaders & PageLoadingContext[​](#page-loaders--pageloadingcontext "Direct link to Page loaders & PageLoadingContext") 

### Loader while page chunks load[​](#loader-while-page-chunks-load "Direct link to Loader while page chunks load") 

Because lazily-loaded pages can take a non-negligible amount of time to load (depending on bundle size and network connection), you may want to show a loading indicator to signal to the user that something is happening after they click a link.

In order to show a loader as your page chunks are loading, you simply add the `whileLoadingPage` prop to your route, `Set` or `PrivateSet` component.

Routes.jsx

``` 
import SkeletonLoader from 'src/components/SkeletonLoader'
<Router>
  <Set whileLoadingPage=>
    <Route path="/contact" page= name="contact" />
    <Route path="/about" page= name="about" />
  </Set>
</Router>
```

After adding this to your app you will probably not see it when navigating between pages. This is because having a loading indicator is nice, but can get annoying when it shows up every single time you navigate to a new page. In fact, this behavior makes it feel like your pages take even longer to load than they actually do! The router takes this into account and, by default, will only show the loader when it takes more than 1000 milliseconds for the page to load. You can change this to whatever you like with the `pageLoadingDelay` prop on `Router`:

Routes.jsx

``` 
<Router pageLoadingDelay=>...</Router>
```

Now the loader will show up after 500ms of load time. To see your loading indicator, you can set this value to 0 or, even better, [change the network speed](https://developers.google.com/web/tools/chrome-devtools/network#throttle) in developer tools to \"Slow 3G\" or another agonizingly slow connection speed.

#### Using PageLoadingContext[​](#using-pageloadingcontext "Direct link to Using PageLoadingContext") 

An alternative way to implement whileLoadingPage is to use `usePageLoadingContext`:

> **VIDEO:** If you\'d prefer to watch a video, there\'s one accompanying this section: [https://www.youtube.com/watch?v=BVkyXjUQADs&feature=youtu.be](https://www.youtube.com/watch?v=BVkyXjUQADs&feature=youtu.be)

SomeLayout.jsx

``` 
import  from '@redwoodjs/router'

const SomeLayout = (props) =>  = usePageLoadingContext()
  return (
    <div>
      
      <main></main>
    </div>
  )
}
```

When the lazy-loaded page is loading, `PageLoadingContext.Consumer` will pass `` to the render function, or false otherwise. You can use this context wherever you like in your application!

### Loader while auth details are being retrieved[​](#loader-while-auth-details-are-being-retrieved "Direct link to Loader while auth details are being retrieved") 

Let\'s say you have a dashboard area on your Redwood app, which can only be accessed after logging in. When Redwood Router renders your private page, it will first fetch the user\'s details, and only render the page if it determines the user is indeed logged in.

In order to display a loader while auth details are being retrieved you can add the `whileLoadingAuth` prop to your `PrivateSet` component:

Routes.jsx

``` 
<Router useAuth=>
  <PrivateSet
    wrap=
    unauthenticated="login"
    whileLoadingAuth= //<-- auth loader
    whileLoadingPage= // <-- page chunk loader
    prerender
  >
    <Route path="/dashboard" page= name="dashboard" />

    
  </PrivateSet>
</Router>
```

## `FatalErrorPage`[​](#fatalerrorpage "Direct link to fatalerrorpage") 

Every Redwood project ships with a default `FatalErrorPage` located in `web/src/pages/FatalErrorPage`. This page gets rendered when an error makes its way all the way to the top of your app without being handled by a catch block or a React error boundary.

Note that this page behaves differently in development than in production.

### In Development[​](#in-development "Direct link to In Development") 

In development, the `FatalErrorPage` provides helpful debugging information about the error and any GraphQL request that\'s involved.

For example, if there\'s a missing component that\'s causing an error, this\'s what you\'ll see:

![fatal_error_message](/assets/images/fatal_error_message-4c6bbb7bbac712368d56bc6d2329bed4.png)

Or if the variable passed as a prop to a component can\'t be found:

![fatal_error_message_query](/assets/images/fatal_error_message_query-ecedc696d9c583fe98481b10559cae89.png)

And if the page has a Cell, you\'ll see the Cell\'s request which may have contributed to the error - but will depend on how your Suspense boundary is setup:

![cell_error_request](/assets/images/cell_req_error-f36f97b12c0294c1e5b7af90b596fa40.png)

### In Production[​](#in-production "Direct link to In Production") 

By default, the `FatalErrorPage` in production is barebones:

![fatal_something_went_wrong](/assets/images/fatal_something_went_wrong-add6362d7ce71548636429f00c2df4fd.png)

### Customizing the `FatalErrorPage`[​](#customizing-the-fatalerrorpage "Direct link to customizing-the-fatalerrorpage") 

You can customize the production `FatalErrorPage`, but it\'s important to keep things simple to avoid the possibility that it\'ll cause its own error. If it does, the router still renders a generic error page, but your users will appreciate something a bit more thoughtful:

![fatal_something_went_wrong_custom](/assets/images/fatal_something_went_wrong_custom-09e47a85a68da972a177063bd3ba0d06.png)

web/src/pages/FatalErrorPage/FatalErrorPage.jsx

``` 
import  from '@redwoodjs/router'

// ...

export default RedwoodDevFatalErrorPage ||
  (() => (
    <div className="bg-white min-h-full px-4 py-16 sm:px-6 sm:py-24 md:grid md:place-items-center lg:px-8">
      <div className="max-w-max mx-auto">
        <main className="sm:flex">
          <p className="text-4xl font-extrabold text-blue-600 sm:text-5xl">
            🤦‍♂️ Oops.
          </p>
          <div className="sm:ml-6">
            <div className="sm:border-l sm:border-gray-200 sm:pl-6">
              <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight sm:text-5xl">
                Something went wrong
              </h1>
              <p className="mt-1 text-base text-gray-500">
                Sorry about that. Please contact support for help.
              </p>
            </div>
            <div className="mt-10 flex space-x-3 sm:border-l sm:border-transparent sm:pl-6">
              <Link
                to=
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-blue-600 hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                Home
              </Link>
              <Link
                to=
                className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-blue-700 bg-blue-100 hover:bg-blue-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500"
              >
                Contact Support
              </Link>
            </div>
          </div>
        </main>
      </div>
    </div>
  ))
```

Note that if you\'re copy-pasting this example, it uses [Tailwind CSS](https://tailwindcss.com), so you\'ll have to set that up first. See the [setup ui](/docs/cli-commands#setup-ui) CLI command to add it to your project.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]Can I customize the development one?

As it\'s part of the RedwoodJS framework, you can\'t *change* the dev fatal error page, but you can always build your own that takes the same props. If there\'s a feature you want to add to the built-in version, let us know on the [forums](https://community.redwoodjs.com/).

## `NotFoundPage`[​](#notfoundpage "Direct link to notfoundpage") 

Every Redwood project ships with a default `NotFoundPage` located in `web/src/pages/NotFoundPage`.

But just because it\'s called `NotFoundPage` doesn\'t mean the router knows that. The only way the router knows which page is the `NotFoundPage` is via the `notfound` prop, which tells the router what to render when no routes match:

web/src/Routes.jsx

``` 
import  from '@redwoodjs/router'

const Routes = () => (
  <Router>
    <Route notfound page= />
  </Router>
)

export default Routes
```

### Customizing the `NotFoundPage`[​](#customizing-the-notfoundpage "Direct link to customizing-the-notfoundpage") 

By default, the `NotFoundPage` is a basic HTML page with internal styles:

web/src/pages/NotFoundPage/NotFoundPage.jsx

``` 
export default () => (
  <main>
    // ... some custom css
    <section>
      <h1>
        <span>404 Page Not Found</span>
      </h1>
    </section>
  </main>
)
```

You\'re free to customize it however you like. You can change the markup and even use CSS or UI libraries to style it. Here\'s an example using [Tailwind CSS](https://tailwindcss.com). (See the [setup ui](/docs/cli-commands#setup-ui) CLI command to add it to your project.)

![custom_not_found](/assets/images/custom_not_found_page-30b2593d3cde8816fcc1d95cc5229dce.png)

web/src/pages/NotFoundPage/NotFoundPage.jsx

``` 
import  from '@redwoodjs/router'

export default () => (
  <div className="bg-white min-h-full px-4 py-16 sm:px-6 sm:py-24 md:grid md:place-items-center lg:px-8">
    <div className="max-w-max mx-auto">
      <main className="sm:flex">
        <p className="text-4xl font-extrabold text-red-600 sm:text-5xl">404</p>
        <div className="sm:ml-6">
          <div className="sm:border-l sm:border-gray-200 sm:pl-6">
            <h1 className="text-4xl font-extrabold text-gray-900 tracking-tight sm:text-5xl">
              Page not found
            </h1>
            <p className="mt-1 text-base text-gray-500">
              Check the URL in the address bar and please try again.
            </p>
          </div>
          <div className="mt-10 flex space-x-3 sm:border-l sm:border-transparent sm:pl-6">
            <Link
              to=
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Home
            </Link>
            <Link
              to=
              className="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-red-700 bg-red-100 hover:bg-red-200 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500"
            >
              Get Help
            </Link>
          </div>
        </div>
      </main>
    </div>
  </div>
)
```

While the `notfound` route can\'t be nested in a `Set` like other routes, you can still wrap it in Layouts by importing them into the page:

web/src/pages/NotFoundPage/NotFoundPage.jsx

``` 
import MainLayout from 'src/layouts/MainLayout/MainLayout'

export default () => (
  <MainLayout>
    <main>
      <section>
        <h1>
          <span>404 Page Not Found</span>
        </h1>
      </section>
    </main>
  </MainLayout>
)
```

This means that the `NotFoundPage` can use Redwood features like Cells or auth to construct navigation options or detailed header and footer content to help your users find their way back to the main application.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/router.md)