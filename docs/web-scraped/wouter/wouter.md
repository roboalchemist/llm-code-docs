# Source: https://npm.im/wouter

Title: wouter

URL Source: https://npm.im/wouter

Markdown Content:
[![Image 1: Wouter — a super-tiny React router (logo by Katya Simacheva)](https://raw.githubusercontent.com/molefrog/wouter/HEAD/assets/logo.svg)](https://github.com/molefrog/wouter/blob/HEAD/assets/logo.svg)

[![Image 2: npm](https://camo.githubusercontent.com/41abd10de7d0b19be5751e54838833330c84b5c99ded253f46064b2acd13cfab/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f776f757465722e7376673f636f6c6f723d626c61636b266c6162656c436f6c6f723d383838)](https://npmjs.org/package/wouter)[![Image 3: CI](https://camo.githubusercontent.com/b004e1dbe9d5141b718207a2fc8a41c8df7af1fba60cd28fc19eaad125ab2031/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f6d6f6c6566726f672f776f757465722f73697a652e796d6c3f636f6c6f723d626c61636b266c6162656c436f6c6f723d383838266c6162656c3d322e354b422b6c696d6974)](https://travis-ci.org/molefrog/wouter)[![Image 4: Coverage](https://camo.githubusercontent.com/08ff0e1b82cbe5fd2a85584f48159106b77e36f49dd124bdf32d5a8d17adffb1/68747470733a2f2f696d672e736869656c64732e696f2f636f766572616c6c732f6769746875622f6d6f6c6566726f672f776f757465722f76332e7376673f636f6c6f723d626c61636b266c6162656c436f6c6f723d383838)](https://coveralls.io/github/molefrog/wouter?branch=v3)[![Image 5: Coverage](https://camo.githubusercontent.com/11352ccdf1411bf7f92f4faac64d3ba7be953ef9c3d51f726b0b2d555e150cd0/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f646d2f776f757465722e7376673f636f6c6f723d626c61636b266c6162656c436f6c6f723d383838)](https://www.npmjs.com/package/wouter)[![Image 6: Edit in StackBlitz IDE](https://camo.githubusercontent.com/cb1ee91c0d71e8b543c4fa625ea946b076f4aa2319d06e3214a08d9cc1972ba6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f537461636b426c69747a2d4e657725323050522d626c61636b3f6c6162656c436f6c6f723d383838)](https://pr.new/molefrog/wouter)

**wouter** is a tiny router for modern React and Preact apps that relies on Hooks. 

 A router you wanted so bad in your project!

[![Image 7: by Katya Simacheva](https://raw.githubusercontent.com/molefrog/wouter/HEAD/assets/wouter.svg)](https://github.com/molefrog/wouter/blob/HEAD/assets/wouter.svg)

*   Minimum dependencies, only **2.1 KB** gzipped vs 18.7KB [React Router](https://github.com/ReactTraining/react-router).
*   Supports both **React** and **[Preact](https://preactjs.com/)**! Read _["Preact support" section](https://npm.im/wouter#preact-support)_ for more details.
*   No top-level `<Router />` component, it is **fully optional**.
*   Mimics [React Router](https://github.com/ReactTraining/react-router)'s best practices by providing familiar **[`Route`](https://npm.im/wouter#route-pathpattern-)**, **[`Link`](https://npm.im/wouter#link-hrefpath-)**, **[`Switch`](https://npm.im/wouter#switch-)** and **[`Redirect`](https://npm.im/wouter#redirect-topath-)** components.
*   Has hook-based API for more granular control over routing (like animations): **[`useLocation`](https://npm.im/wouter#uselocation-working-with-the-history)**, **[`useRoute`](https://npm.im/wouter#useroute-route-matching-and-parameters)** and **[`useRouter`](https://npm.im/wouter#userouter-accessing-the-router-object)**.

> ... I love Wouter. It’s tiny, fully embraces hooks, and has an intuitive and barebones API. I can accomplish everything I could with react-router with Wouter, and it just feels **more minimalist while not being inconvenient.**
> 
> 
> [**Matt Miller**, _An exhaustive React ecosystem for 2020_](https://medium.com/@mmiller42/an-exhaustive-react-guide-for-2020-7859f0bddc56)

Wouter provides a simple API that many developers and library authors appreciate. Some notable projects that use wouter: **[Ultra](https://ultrajs.dev/)**, **[React-three-fiber](https://github.com/react-spring/react-three-fiber)**, **[Sunmao UI](https://sunmao-ui.com/)**, **[Million](https://million.dev/)** and many more.

*   [Getting Started](https://npm.im/wouter#getting-started)

    *   [Browser Support](https://npm.im/wouter#browser-support)

*   [Wouter API](https://npm.im/wouter#wouter-api)

    *   [The list of methods available](https://npm.im/wouter#the-list-of-methods-available)

*   [Hooks API](https://npm.im/wouter#hooks-api)

    *   [`useRoute`: route matching and parameters](https://npm.im/wouter#useroute-route-matching-and-parameters)
    *   [`useLocation`: working with the history](https://npm.im/wouter#uselocation-working-with-the-history)
        *   [Additional navigation parameters](https://npm.im/wouter#additional-navigation-parameters)
        *   [Customizing the location hook](https://npm.im/wouter#customizing-the-location-hook)

    *   [`useParams`: extracting matched parameters](https://npm.im/wouter#useparams-extracting-matched-parameters)
    *   [`useSearch`: query strings](https://npm.im/wouter#usesearch-query-strings)
    *   [`useSearchParams`: search parameters](https://npm.im/wouter#usesearchparams-search-parameters)
    *   [`useRouter`: accessing the router object](https://npm.im/wouter#userouter-accessing-the-router-object)

*   [Component API](https://npm.im/wouter#component-api)

    *   [`<Route path={pattern} />`](https://npm.im/wouter#route-pathpattern-)
        *   [Route nesting](https://npm.im/wouter#route-nesting)

    *   [`<Link href={path} />`](https://npm.im/wouter#link-hrefpath-)
    *   [`<Switch />`](https://npm.im/wouter#switch-)
    *   [`<Redirect to={path} />`](https://npm.im/wouter#redirect-topath-)
    *   [`<Router hook={hook} parser={fn} base={basepath} />`](https://npm.im/wouter#router-hookhook-parserfn-basebasepath-hrefsfn-)

*   [FAQ and Code Recipes](https://npm.im/wouter#faq-and-code-recipes)

    *   [I deploy my app to the subfolder. Can I specify a base path?](https://npm.im/wouter#i-deploy-my-app-to-the-subfolder-can-i-specify-a-base-path)
    *   [How do I make a default route?](https://npm.im/wouter#how-do-i-make-a-default-route)
    *   [How do I make a link active for the current route?](https://npm.im/wouter#how-do-i-make-a-link-active-for-the-current-route)
    *   [Are strict routes supported?](https://npm.im/wouter#are-strict-routes-supported)
    *   [Are relative routes and links supported?](https://npm.im/wouter#are-relative-routes-and-links-supported)
    *   [Can I initiate navigation from outside a component?](https://npm.im/wouter#can-i-initiate-navigation-from-outside-a-component)
    *   [Can I use _wouter_ in my TypeScript project?](https://npm.im/wouter#can-i-use-wouter-in-my-typescript-project)
    *   [How can add animated route transitions?](https://npm.im/wouter#how-can-add-animated-route-transitions)
    *   [How do I add view transitions to my app?](https://npm.im/wouter#how-do-i-add-view-transitions-to-my-app)
    *   [Preact support?](https://npm.im/wouter#preact-support)
    *   [Server-side Rendering support (SSR)?](https://npm.im/wouter#server-side-rendering-support-ssr)
    *   [How do I configure the router to render a specific route in tests?](https://npm.im/wouter#how-do-i-configure-the-router-to-render-a-specific-route-in-tests)
    *   [1KB is too much, I can't afford it!](https://npm.im/wouter#1kb-is-too-much-i-cant-afford-it)

*   [Acknowledgements](https://npm.im/wouter#acknowledgements)

First, add wouter to your project.

npm i wouter

Or, if you're using Preact the use the following command [`npm i wouter-preact`](https://npm.im/wouter#preact-support).

Check out this simple demo app below. It doesn't cover hooks and other features such as nested routing, but it's a good starting point for those who are migrating from React Router.

import { Link, Route, Switch } from "wouter";

const App = () => (
  <>
    <Link href="/users/1">Profile</Link>

    <Route path="/about">About Us</Route>

    {/* 
 Routes below are matched exclusively -
 the first matched route gets rendered
 */}
    <Switch>
      <Route path="/inbox" component={InboxPage} />

      <Route path="/users/:name">
        {(params) => <>Hello, {params.name}!</>}
      </Route>

      {/* Default route in a switch */}
      <Route>404: No such page!</Route>
    </Switch>
  </>
);

This library is designed for **ES2020+** compatibility. If you need to support older browsers, make sure that you transpile `node_modules`. Additionally, the minimum supported TypeScript version is 4.1 in order to support route parameter inference.

Wouter comes with three kinds of APIs: low-level **standalone location hooks**, hooks for **routing and pattern matching** and more traditional **component-based API** similar to React Router's one.

You are free to choose whatever works for you: use location hooks when you want to keep your app as small as possible and don't need pattern matching; use routing hooks when you want to build custom routing components; or if you're building a traditional app with pages and navigation — components might come in handy.

Check out also [FAQ and Code Recipes](https://npm.im/wouter#faq-and-code-recipes) for more advanced things like active links, default routes, server-side rendering etc.

**Location Hooks**

These can be used separately from the main module and have an interface similar to `useState`. These hooks are standalone and don't include built-in support for nesting, base path, or route matching. However, when passed to `<Router>`, they work seamlessly with all Router features including nesting and base paths.

*   **[`import { useBrowserLocation } from "wouter/use-browser-location"`](https://github.com/molefrog/wouter/blob/v3/packages/wouter/src/use-browser-location.js)** — allows to manipulate current location in the browser's address bar, a tiny wrapper around the History API.
*   **[`import { useHashLocation } from "wouter/use-hash-location"`](https://github.com/molefrog/wouter/blob/v3/packages/wouter/src/use-hash-location.js)** — similarly, gets location from the hash part of the address, i.e. the string after a `#`.
*   **[`import { memoryLocation } from "wouter/memory-location"`](https://npm.im/wouter#uselocation-working-with-the-history)** — an in-memory location hook with history support, external navigation and immutable mode for testing. **Note** the module name because it is a high-order hook. See how memory location can be used in [testing](https://npm.im/wouter#how-do-i-configure-the-router-to-render-a-specific-route-in-tests).

**Routing Hooks**

Import from `wouter` module.

*   **[`useRoute`](https://npm.im/wouter#useroute-the-power-of-hooks)** — shows whether or not current page matches the pattern provided.
*   **[`useLocation`](https://npm.im/wouter#uselocation-working-with-the-history)** — allows to manipulate current router's location, by default subscribes to browser location. **Note:** this isn't the same as `useBrowserLocation`, read below.
*   **[`useParams`](https://npm.im/wouter#useparams-extracting-matched-parameters)** — returns an object with parameters matched from the closest route.
*   **[`useSearch`](https://npm.im/wouter#usesearch-query-strings)** — returns a search string – everything that goes after the `?`.
*   **[`useRouter`](https://npm.im/wouter#userouter-accessing-the-router-object)** — returns a global router object that holds the configuration. Only use it if you want to customize the routing.

**Components**

Import from `wouter` module.

*   **[`<Route />`](https://npm.im/wouter#route-pathpattern-)** — conditionally renders a component based on a pattern.
*   **[`<Link />`](https://npm.im/wouter#link-hrefpath-)** — wraps `<a>`, allows to perform a navigation.
*   **[`<Switch />`](https://npm.im/wouter#switch-)** — exclusive routing, only renders the first matched route.
*   **[`<Redirect />`](https://npm.im/wouter#redirect-topath-)** — when rendered, performs an immediate navigation.
*   **[`<Router />`](https://npm.im/wouter#router-hookhook-matchermatchfn-basebasepath-)** — an optional top-level component for advanced routing configuration.

Checks if the current location matches the pattern provided and returns an object with parameters. This is powered by a wonderful [`regexparam`](https://github.com/lukeed/regexparam) library, so all its pattern syntax is fully supported.

You can use `useRoute` to perform manual routing or implement custom logic, such as route transitions, etc.

import { useRoute } from "wouter";

const Users = () => {
  // `match` is a boolean
  const [match, params] = useRoute("/users/:name");

  if (match) {
    return <>Hello, {params.name}!</>;
  } else {
    return null;
  }
};

A quick cheatsheet of what types of segments are supported:

useRoute("/app/:page");
useRoute("/app/:page/:section");

// optional parameter, matches "/en/home" and "/home"
useRoute("/:locale?/home");

// suffixes
useRoute("/movies/:title.(mp4|mov)");

// wildcards, matches "/app", "/app-1", "/app/home"
useRoute("/app*");

// optional wildcards, matches "/orders", "/orders/"
// and "/orders/completed/list"
useRoute("/orders/*?");

// regex for matching complex patterns,
// matches "/hello:123"
useRoute(/^[/]([a-z]+):([0-9]+)[/]?$/);
// and with named capture groups
useRoute(/^[/](?<word>[a-z]+):(?<num>[0-9]+)[/]?$/);

The second item in the pair `params` is an object with parameters or null if there was no match. For wildcard segments the parameter name is `"*"`:

// wildcards, matches "/app", "/app-1", "/app/home"
const [match, params] = useRoute("/app*");

if (match) {
  // "/home" for "/app/home"
  const page = params["*"];
}

To get the current path and navigate between pages, call the `useLocation` hook. Similarly to `useState`, it returns a value and a setter: the component will re-render when the location changes and by calling `navigate` you can update this value and perform navigation.

By default, it uses `useBrowserLocation` under the hood, though you can configure this in a top-level `Router` component (for example, if you decide at some point to switch to a hash-based routing). `useLocation` will also return scoped path when used within nested routes or with base path setting.

import { useLocation } from "wouter";

const CurrentLocation = () => {
  const [location, navigate] = useLocation();

  return (
    <div>
      {`The current page is: ${location}`}
      <a onClick={() => navigate("/somewhere")}>Click to update</a>
    </div>
  );
};

All the components internally call the `useLocation` hook.

The setter method of `useLocation` can also accept an optional object with parameters to control how the navigation update will happen.

When browser location is used (default), `useLocation` hook accepts `replace` flag to tell the hook to modify the current history entry instead of adding a new one. It is the same as calling `replaceState`.

const [location, navigate] = useLocation();

navigate("/jobs"); // `pushState` is used
navigate("/home", { replace: true }); // `replaceState` is used

Additionally, you can provide a `state` option to update `history.state` while navigating:

navigate("/home", { state: { modal: "promo" } });

history.state; // { modal: "promo" }

By default, **wouter** uses `useLocation` hook that reacts to `pushState` and `replaceState` navigation via `useBrowserLocation`.

To customize this, wrap your app in a `Router` component:

import { Router, Route } from "wouter";
import { useHashLocation } from "wouter/use-hash-location";

const App = () => (
  <Router hook={useHashLocation}>
    <Route path="/about" component={About} />
    ...
  </Router>
);

Because these hooks have return values similar to `useState`, it is easy and fun to build your own location hooks: `useCrossTabLocation`, `useLocalStorage`, `useMicroFrontendLocation` and whatever routing logic you want to support in the app. Give it a try!

This hook allows you to access the parameters exposed through [matching dynamic segments](https://npm.im/wouter#matching-dynamic-segments). Internally, we simply wrap your components in a context provider allowing you to access this data anywhere within the `Route` component.

This allows you to avoid "prop drilling" when dealing with deeply nested components within the route. **Note:**`useParams` will only extract parameters from the closest parent route.

import { Route, useParams } from "wouter";

const User = () => {
  const params = useParams();

  params.id; // "1"

  // alternatively, use the index to access the prop
  params[0]; // "1"
};

<Route path="/user/:id" component={User}> />

It is the same for regex paths. Capture groups can be accessed by their index, or if there is a named capture group, that can be used instead.

import { Route, useParams } from "wouter";

const User = () => {
  const params = useParams();

  params.id; // "1"
  params[0]; // "1"
};

<Route path={/^[/]u s e r[/](?<id>[0-9]+)[/]?$/} component={User}> />

Use this hook to get the current search (query) string value. It will cause your component to re-render only when the string itself and not the full location updates. The search string returned **does not** contain a `?` character.

import { useSearch } from "wouter";

// returns "tab=settings&id=1"
const searchString = useSearch();

For the SSR, use `ssrSearch` prop passed to the router.

<Router ssrSearch={request.search}>{/* SSR! */}</Router>

Refer to [Server-Side Rendering](https://npm.im/wouter#server-side-rendering-support-ssr) for more info on rendering and hydration.

Returns a `URLSearchParams` object and a setter function to update search parameters. The setter accepts either a value (object, URLSearchParams, string[][], etc.) or a **callback function** that receives the current params and must return the new params.

import { useSearchParams } from 'wouter';

const [searchParams, setSearchParams] = useSearchParams();

// extract a specific search parameter
const id = searchParams.get('id');

// modify a specific search parameter
setSearchParams((prev) => {
  prev.set('tab', 'settings');
  return prev;
});

// override all search parameters
setSearchParams({
  id: 1234,
  tab: 'settings',
});

// by default, setSearchParams() will push a new history entry
// to avoid this, set `replace` option to `true`
setSearchParams(
  (prev) => {
    prev.set('order', 'desc');
    return prev;
  },
  {
    replace: true,
  },
);

// you can also pass a history state in options
setSearchParams(
  (prev) => {
    prev.set('foo', 'bar');
    return prev;
  },
  {
    state: 'hello',
  },
);

If you're building advanced integration, for example custom location hook, you might want to get access to the global router object. Router is a simple object that holds routing options that you configure in the `Router` component.

import { useRouter } from "wouter";

const Custom = () => {
  const router = useRouter();

  router.hook; // `useBrowserLocation` by default
  router.base; // "/app"
};

const App = () => (
  <Router base="/app">
    <Custom />
  </Router>
);

`Route` represents a piece of the app that is rendered conditionally based on a pattern `path`. Pattern has the same syntax as the argument you pass to [`useRoute`](https://npm.im/wouter#useroute-route-matching-and-parameters).

The library provides multiple ways to declare a route's body:

import { Route } from "wouter";

// simple form
<Route path="/home"><Home /></Route>

// render-prop style
<Route path="/users/:id">
  {params => <UserPage id={params.id} />}
</Route>

// the `params` prop will be passed down to <Orders />
<Route path="/orders/:status" component={Orders} />

A route with no path is considered to always match, and it is the same as `<Route path="*" />`. When developing your app, use this trick to peek at the route's content without navigation.

-<Route path="/some/page">
+<Route>
  {/* Strip out the `path` to make this visible */}
</Route>

Nesting is a core feature of wouter and can be enabled on a route via the `nest` prop. When this prop is present, the route matches everything that starts with a given pattern and it creates a nested routing context. All child routes will receive location relative to that pattern.

Let's take a look at this example:

<Route path="/app" nest>
  <Route path="/users/:id" nest>
    <Route path="/orders" />
  </Route>
</Route>

1.   This first route will be active for all paths that start with `/app`, this is equivalent to having a base path in your app.

2.   The second one uses dynamic pattern to match paths like `/app/user/1`, `/app/user/1/anything` and so on.

3.   Finally, the inner-most route will only work for paths that look like `/app/users/1/orders`. The match is strict, since that route does not have a `nest` prop and it works as usual.

If you call `useLocation()` inside the last route, it will return `/orders` and not `/app/users/1/orders`. This creates a nice isolation and it makes it easier to make changes to parent route without worrying that the rest of the app will stop working. If you need to navigate to a top-level page however, you can use a prefix `~` to refer to an absolute path:

<Route path="/payments" nest>
  <Route path="/all">
    <Link to="~/home">Back to Home</Link>
  </Route>
</Route>

**Note:** The `nest` prop does not alter the regex passed into regex paths. Instead, the `nest` prop will only determine if nested routes will match against the rest of path or the same path. To make a strict path regex, use a regex pattern like `/^[/](your pattern)[/]?$/` (this matches an optional end slash and the end of the string). To make a nestable regex, use a regex pattern like `/^[/](your pattern)(?=$|[/])/` (this matches either the end of the string or a slash for future segments).

Link component renders an `<a />` element that, when clicked, performs a navigation.

import { Link } from "wouter"

<Link href="/">Home</Link>

// `to` is an alias for `href`
<Link to="/">Home</Link>

// all standard `a` props are proxied
<Link href="/" className="link" aria-label="Go to homepage">Home</Link>

// all location hook options are supported
<Link href="/" replace state={{ animate: true }} />

Link will always wrap its children in an `<a />` tag, unless `asChild` prop is provided. Use this when you need to have a custom component that renders an `<a />` under the hood.

// use this instead
<Link to="/" asChild>
  <UIKitLink />
</Link>

// Remember, `UIKitLink` must implement an `onClick` handler
// in order for navigation to work!

When you pass a function as a `className` prop, it will be called with a boolean value indicating whether the link is active for the current route. You can use this to style active links (e.g. for links in navigation menu)

<Link className={(active) => (active ? "active" : "")}>Nav</Link>

Read more about [active links here](https://npm.im/wouter#how-do-i-make-a-link-active-for-the-current-route).

There are cases when you want to have an exclusive routing: to make sure that only one route is rendered at the time, even if the routes have patterns that overlap. That's what `Switch` does: it only renders **the first matching route**.

import { Route, Switch } from "wouter";

<Switch>
  <Route path="/orders/all" component={AllOrders} />
  <Route path="/orders/:status" component={Orders} />

  {/* 
 in wouter, any Route with empty path is considered always active. 
 This can be used to achieve "default" route behaviour within Switch. 
 Note: the order matters! See examples below.
 */}
  <Route>This is rendered when nothing above has matched</Route>
</Switch>;

When no route in switch matches, the last empty `Route` will be used as a fallback. See [**FAQ and Code Recipes** section](https://npm.im/wouter#how-do-i-make-a-default-route) to read about default routes.

When mounted performs a redirect to a `path` provided. Uses `useLocation` hook internally to trigger the navigation inside of a `useEffect` block.

`Redirect` can also accept props for [customizing how navigation will be performed](https://npm.im/wouter#additional-navigation-parameters), for example for setting history state when navigating. These options are specific to the currently used location hook.

<Redirect to="/" />

// arbitrary state object
<Redirect to="/" state={{ modal: true }} />

// use `replaceState`
<Redirect to="/" replace />

If you need more advanced logic for navigation, for example, to trigger the redirect inside of an event handler, consider using [`useLocation` hook instead](https://npm.im/wouter#uselocation-working-with-the-history):

import { useLocation } from "wouter";

const [location, setLocation] = useLocation();

fetchOrders().then((orders) => {
  setOrders(orders);
  setLocation("/app/orders");
});

Unlike _React Router_, routes in wouter **don't have to be wrapped in a top-level component**. An internal router object will be constructed on demand, so you can start writing your app without polluting it with a cascade of top-level providers. There are cases however, when the routing behaviour needs to be customized.

These cases include hash-based routing, basepath support, custom matcher function etc.

import { useHashLocation } from "wouter/use-hash-location";

<Router hook={useHashLocation} base="/app">
  {/* Your app goes here */}
</Router>;

A router is a simple object that holds the routing configuration options. You can always obtain this object using a [`useRouter` hook](https://npm.im/wouter#userouter-accessing-the-router-object). The list of currently available options:

*   **`hook: () => [location: string, setLocation: fn]`** — is a React Hook function that subscribes to location changes. It returns a pair of current `location` string e.g. `/app/users` and a `setLocation` function for navigation. You can use this hook from any component of your app by calling [`useLocation()` hook](https://npm.im/wouter#uselocation-working-with-the-history). See [Customizing the location hook](https://npm.im/wouter#customizing-the-location-hook).

*   **`searchHook: () => [search: string, setSearch: fn]`** — similar to `hook`, but for obtaining the [current search string](https://npm.im/wouter#usesearch-query-strings).

*   **`base: string`** — an optional setting that allows to specify a base path, such as `/app`. All application routes will be relative to that path. To navigate out to an absolute path, prefix your path with an `~`. [See the FAQ](https://npm.im/wouter#are-relative-routes-and-links-supported).

*   **`parser: (path: string, loose?: boolean) => { pattern, keys }`** — a pattern parsing function. Produces a RegExp for matching the current location against the user-defined patterns like `/app/users/:id`. Has the same interface as the [`parse`](https://github.com/lukeed/regexparam?tab=readme-ov-file#regexparamparseinput-regexp) function from `regexparam`. See [this example](https://npm.im/wouter#are-strict-routes-supported) that demonstrates custom parser feature.

*   **`ssrPath: string`** and **`ssrSearch: string`** use these when [rendering your app on the server](https://npm.im/wouter#server-side-rendering-support-ssr).

*   `hrefs: (href: boolean) => string` — a function for transforming `href` attribute of an `<a />` element rendered by `Link`. It is used to support hash-based routing. By default, `href` attribute is the same as the `href` or `to` prop of a `Link`. A location hook can also define a `hook.hrefs` property, in this case the `href` will be inferred.

*   **`aroundNav: (navigate, to, options) => void`** — a handler that wraps all navigation calls. Use this to intercept navigation and perform custom logic before and after the navigation occurs. You can modify navigation parameters, add side effects, or prevent navigation entirely. This is particularly useful for implementing [view transitions](https://npm.im/wouter#how-do-i-add-view-transitions-to-my-app). By default, it simply calls `navigate(to, options)`.

const aroundNav = (navigate, to, options) => {
  // do something before navigation
  navigate(to, options); // perform navigation
  // do something after navigation
}; 

You can! Wrap your app with `<Router base="/app" />` component and that should do the trick:

import { Router, Route, Link } from "wouter";

const App = () => (
  <Router base="/app">
    {/* the link's href attribute will be "/app/users" */}
    <Link href="/users">Users</Link>

    <Route path="/users">The current path is /app/users!</Route>
  </Router>
);

Calling `useLocation()` within a route in an app with base path will return a path scoped to the base. Meaning that when base is `"/app"` and pathname is `"/app/users"` the returned string is `"/users"`. Accordingly, calling `navigate` will automatically append the base to the path argument for you.

When you have multiple nested routers, base paths are inherited and stack up.

<Router base="/app">
  <Router base="/cms">
    <Route path="/users">Path is /app/cms/users!</Route>
  </Router>
</Router>

One of the common patterns in application routing is having a default route that will be shown as a fallback, in case no other route matches (for example, if you need to render 404 message). In **wouter** this can easily be done as a combination of `<Switch />` component and a default route:

import { Switch, Route } from "wouter";

<Switch>
  <Route path="/about">...</Route>
  <Route>404, Not Found!</Route>
</Switch>;

_Note:_ the order of switch children matters, default route should always come last.

If you want to have access to the matched segment of the path you can use wildcard parameters:

<Switch>
  <Route path="/users">...</Route>

  {/* will match anything that starts with /users/, e.g. /users/foo, /users/1/edit etc. */}
  <Route path="/users/*">...</Route>

  {/* will match everything else */}
  <Route path="*">
    {(params) => `404, Sorry the page ${params["*"]} does not exist!`}
  </Route>
</Switch>

**[▶ Demo Sandbox](https://codesandbox.io/s/wouter-v3-ts-8q532r)**

Instead of a regular `className` string, provide a function to use custom class when this link matches the current route. Note that it will always perform an exact match (i.e. `/users` will not be active for `/users/1`).

<Link className={(active) => (active ? "active" : "")}>Nav link</Link>

If you need to control other props, such as `aria-current` or `style`, you can write your own `<Link />` wrapper and detect if the path is active by using the `useRoute` hook.

const [isActive] = useRoute(props.href);

return (
  <Link {...props} asChild>
    <a style={isActive ? { color: "red" } : {}}>{props.children}</a>
  </Link>
);

**[▶ Demo Sandbox](https://codesandbox.io/s/wouter-v3-ts-8q532r?file=/src/ActiveLink.tsx)**

If a trailing slash is important for your app's routing, you could specify a custom parser. Parser is a method that takes a pattern string and returns a RegExp and an array of parsed key. It uses the signature of a [`parse`](https://github.com/lukeed/regexparam?tab=readme-ov-file#regexparamparseinput-regexp) function from `regexparam`.

Let's write a custom parser based on a popular [`path-to-regexp`](https://github.com/pillarjs/path-to-regexp) package that does support strict routes option.

import { pathToRegexp } from "path-to-regexp";

/**
 * Custom parser based on `pathToRegexp` with strict route option
 */
const strictParser = (path, loose) => {
  const keys = [];
  const pattern = pathToRegexp(path, keys, { strict: true, end: !loose });

  return {
    pattern,
    // `pathToRegexp` returns some metadata about the keys,
    // we want to strip it to just an array of keys
    keys: keys.map((k) => k.name),
  };
};

const App = () => (
  <Router parser={strictParser}>
    <Route path="/foo">...</Route>
    <Route path="/foo/">...</Route>
  </Router>
);

**[▶ Demo Sandbox](https://codesandbox.io/p/sandbox/wouter-v3-strict-routes-w3xdtz)**

Yes! Any route with `nest` prop present creates a nesting context. Keep in mind, that the location inside a nested route will be scoped.

const App = () => (
  <Router base="/app">
    <Route path="/dashboard" nest>
      {/* the href is "/app/dashboard/users" */}
      <Link to="/users" />

      <Route path="/users">
        {/* Here `useLocation()` returns "/users"! */}
      </Route>
    </Route>
  </Router>
);

**[▶ Demo Sandbox](https://codesandbox.io/p/sandbox/wouter-v3-nested-routes-l8p23s)**

Yes, the `navigate` function is exposed from the `"wouter/use-browser-location"` module:

import { navigate } from "wouter/use-browser-location";

navigate("/", { replace: true });

It's the same function that is used internally.

Yes! Although the project isn't written in TypeScript, the type definition files are bundled with the package.

Let's take look at how wouter routes can be animated with [`framer-motion`](https://github.com/molefrog/wouter/blob/HEAD/framer.com/motion). Animating enter transitions is easy, but exit transitions require a bit more work. We'll use the `AnimatePresence` component that will keep the page in the DOM until the exit animation is complete.

Unfortunately, `AnimatePresence` only animates its **direct children**, so this won't work:

import { motion, AnimatePresence } from "framer-motion";

export const MyComponent = () => (
  <AnimatePresence>
    {/* This will not work! `motion.div` is not a direct child */}
    <Route path="/">
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
      />
    </Route>
  </AnimatePresence>
);

The workaround is to match this route manually with `useRoute`:

export const MyComponent = ({ isVisible }) => {
  const [isMatch] = useRoute("/");

  return (
    <AnimatePresence>
      {isMatch && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
        />
      )}
    </AnimatePresence>
  );
};

More complex examples involve using `useRoutes` hook (similar to how React Router does it), but wouter does not ship it out-of-the-box. Please refer to [this issue](https://github.com/molefrog/wouter/issues/414#issuecomment-1954192679) for the workaround.

Wouter works seamlessly with the [View Transitions API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transitions_API), but you'll need to manually activate it. This is because view transitions require synchronous DOM rendering and must be wrapped in `flushSync` from `react-dom`. Following wouter's philosophy of staying lightweight and avoiding unnecessary dependencies, view transitions aren't built-in. However, there's a simple escape hatch to enable them: the `aroundNav` prop.

import { flushSync } from "react-dom";
import { Router, type AroundNavHandler } from "wouter";

const aroundNav: AroundNavHandler = (navigate, to, options) => {
  // Check if View Transitions API is supported
  if (!document.startViewTransition) {
    navigate(to, options);
    return;
  }

  document.startViewTransition(() => {
    flushSync(() => {
      navigate(to, options);
    });
  });
};

const App = () => (
  <Router aroundNav={aroundNav}>
    {/* Your routes here */}
  </Router>
);

You can also enable transitions selectively using the `transition` prop, which will be available in the `options` parameter:

// Enable transition for a specific link
<Link to="/about" transition>About</Link>

// Or programmatically
const [location, navigate] = useLocation();
navigate("/about", { transition: true });

// Then check for it in your handler
const aroundNav: AroundNavHandler = (navigate, to, options) => {
  if (!document.startViewTransition) {
    navigate(to, options);
    return;
  }

  if (options?.transition) {
    document.startViewTransition(() => {
      flushSync(() => {
        navigate(to, options);
      });
    });
  } else {
    navigate(to, options);
  }
};

Preact exports are available through a separate package named `wouter-preact` (or within the `wouter/preact` namespace, however this method isn't recommended as it requires React as a peer dependency):

- import { useRoute, Route, Switch } from "wouter";
+ import { useRoute, Route, Switch } from "wouter-preact";

You might need to ensure you have the latest version of [Preact X](https://github.com/preactjs/preact/releases/tag/10.0.0-alpha.0) with support for hooks.

**[▶ Demo Sandbox](https://codesandbox.io/s/wouter-preact-0lr3n)**

In order to render your app on the server, you'll need to wrap your app with top-level Router and specify `ssrPath` prop (usually, derived from current request). Optionally, `Router` accepts `ssrSearch` parameter if need to have access to a search string on a server.

import { renderToString } from "react-dom/server";
import { Router } from "wouter";

const handleRequest = (req, res) => {
  // top-level Router is mandatory in SSR mode
  // pass an optional context object to handle redirects on the server
  const ssrContext = {};
  const prerendered = renderToString(
    <Router ssrPath={req.path} ssrSearch={req.search} ssrContext={ssrContext}>
      <App />
    </Router>
  );

  if (ssrContext.redirectTo) {
    // encountered redirect
    res.redirect(ssrContext.redirectTo);
  } else {
    // respond with prerendered html
  }
};

Tip: wouter can pre-fill `ssrSearch`, if `ssrPath` contains the `?` character. So these are equivalent:

<Router ssrPath="/goods?sort=asc" />;

// is the same as
<Router ssrPath="/goods" ssrSearch="sort=asc" />;

On the client, the static markup must be hydrated in order for your app to become interactive. Note that to avoid having hydration warnings, the JSX rendered on the client must match the one used by the server, so the `Router` component must be present.

import { hydrateRoot } from "react-dom/client";

const root = hydrateRoot(
  domNode,
  // during hydration, `ssrPath` is set to `location.pathname`,
  // `ssrSearch` set to `location.search` accordingly
  // so there is no need to explicitly specify them
  <Router>
    <App />
  </Router>
);

**[▶ Demo](https://github.com/molefrog/wultra)**

Testing with wouter is no different from testing regular React apps. You often need a way to provide a fixture for the current location to render a specific route. This can be easily done by swapping the normal location hook with `memoryLocation`. It is an initializer function that returns a hook that you can then specify in a top-level `Router`.

import { render } from "@testing-library/react";
import { memoryLocation } from "wouter/memory-location";

it("renders a user page", () => {
  // `static` option makes it immutable
  // even if you call `navigate` somewhere in the app location won't change
  const { hook, searchHook } = memoryLocation({ path: "/user/2", static: true });

  const { container } = render(
    <Router hook={hook} searchHook={searchHook}>
      <Route path="/user/:id">{(params) => <>User ID: {params.id}</>}</Route>
    </Router>
  );

  expect(container.innerHTML).toBe("User ID: 2");
});

**Note:** When you pass a `hook` prop to `Router`, it will automatically inherit the `searchHook` from the hook if available (via `hook.searchHook`). This means you don't need to explicitly pass both `hook` and `searchHook` when using `memoryLocation` - just passing `hook` is enough for `useSearch()` to work correctly with query parameters.

it("works with query parameters", () => {
  const { hook } = memoryLocation({ path: "/products?sort=price&order=asc" });

  const { result } = renderHook(() => useSearch(), {
    wrapper: ({ children }) => <Router hook={hook}>{children}</Router>,
  });

  expect(result.current).toBe("sort=price&order=asc");
});

The hook can be configured to record navigation history. Additionally, it comes with a `navigate` function for external navigation.

it("performs a redirect", () => {
  const { hook, history, navigate } = memoryLocation({
    path: "/",
    // will store navigation history in `history`
    record: true,
  });

  const { container } = render(
    <Router hook={hook}>
      <Switch>
        <Route path="/">Index</Route>
        <Route path="/orders">Orders</Route>

        <Route>
          <Redirect to="/orders" />
        </Route>
      </Switch>
    </Router>
  );

  expect(history).toStrictEqual(["/"]);

  navigate("/unknown/route");

  expect(container.innerHTML).toBe("Orders");
  expect(history).toStrictEqual(["/", "/unknown/route", "/orders"]);
});

We've got some great news for you! If you're a minimalist bundle-size nomad and you need a damn simple routing in your app, you can just use bare location hooks. For example, `useBrowserLocation` hook which is only **650 bytes gzipped** and manually match the current location with it:

import { useBrowserLocation } from "wouter/use-browser-location";

const UsersRoute = () => {
  const [location] = useBrowserLocation();

  if (location !== "/users") return null;

  // render the route
};

Wouter's motto is **"Minimalist-friendly"**.

**Architecture principles:**

*   All code is written in JavaScript for full control over size optimization
*   TypeScript definitions are maintained separately in `types/` directories
*   `wouter-preact` reuses the same source except for `react-deps.js` (Preact-specific hooks)
*   Type definitions are duplicated between packages (not ideal, but works for now)

**Development:** Tests run directly from source files (no build required). Run `npm run test` for interactive mode or `npm run test -- --run` for a single run. Use `npm run build` to build the distributable package before publishing.

Wouter illustrations and logos were made by [Katya Simacheva](https://simachevakatya.com/) and [Katya Vakulenko](https://katyavakulenko.com/). Thank you to **[@jeetiss](https://github.com/jeetiss)** and all the amazing [contributors](https://github.com/molefrog/wouter/graphs/contributors) for helping with the development.
