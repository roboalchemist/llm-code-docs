---
title: API
type: reference
summary: Complete API reference for SWR hooks and utilities.
prerequisites:
  - /docs/getting-started
related:
  - /docs/global-configuration
  - /docs/typescript
---

# API

```js
const { data, error, isLoading, isValidating, mutate } = useSWR(key, fetcher, options)
```

## Parameters

* `key`: a unique key string for the request (or a function / array / null) [(details)](/docs/arguments), [(advanced usage)](/docs/conditional-fetching)
* `fetcher`: (*optional*) a Promise-returning function to fetch your data [(details)](/docs/data-fetching)
* `options`: (*optional*) an object of options for this SWR hook

## Return Values

* `data`: data for the given key resolved by `fetcher` (or undefined if not loaded)
* `error`: error thrown by `fetcher` (or undefined)
* `isLoading`: if there's an ongoing request and no "loaded data". Fallback data and previous data are not considered "loaded data"
* `isValidating`: if there's a request or revalidation loading
* `mutate(data?, options?)`: function to mutate the cached data [(details)](/docs/mutation)

More information can be found [here](/docs/advanced/understanding).

## Options

* `suspense = false`: enable React Suspense mode [(details)](/docs/suspense)
* `fetcher(args)`: the fetcher function
* `revalidateIfStale = true`: automatically revalidate even if there is stale data [(details)](/docs/revalidation#disable-automatic-revalidations)
* `revalidateOnMount`: enable or disable automatic revalidation when component is mounted [(details)](/docs/revalidation#revalidate-on-mount)
* `revalidateOnFocus = true`: automatically revalidate when window gets focused [(details)](/docs/revalidation)
* `revalidateOnReconnect = true`: automatically revalidate when the browser regains a network connection (via `navigator.onLine`) [(details)](/docs/revalidation)
* `refreshInterval` [(details)](/docs/revalidation):
  * Disabled by default: `refreshInterval = 0`
  * If set to a number, polling interval in milliseconds
  * If set to a function, the function will receive the latest data and should return the interval in milliseconds
* `refreshWhenHidden = false`: polling when the window is invisible (if `refreshInterval` is enabled)
* `refreshWhenOffline = false`: polling when the browser is offline (determined by `navigator.onLine`)
* `shouldRetryOnError = true`: retry when fetcher has an error
* `dedupingInterval = 2000`: dedupe requests with the same key in this time span in milliseconds
* `focusThrottleInterval = 5000`: only revalidate once during a time span in milliseconds
* `loadingTimeout = 3000`: timeout to trigger the onLoadingSlow event in milliseconds
* `errorRetryInterval = 5000`: error retry interval in milliseconds
* `errorRetryCount`: max error retry count
* `fallback`: a key-value object of multiple fallback data [(example)](/docs/with-nextjs)
* `fallbackData`: initial data to be returned (note: This is per-hook)
* `strictServerPrefetchWarning = false`: show a warning message in the console when a key has no pre-filled data provided [(details)](/docs/with-nextjs#prefetch-data-in-server-components)
* `keepPreviousData = false`: return the previous key's data until the new data has been loaded [(details)](/docs/advanced/understanding#return-previous-data-for-better-ux)
* `onLoadingSlow(key, config)`: callback function when a request takes too long to load (see `loadingTimeout`)
* `onSuccess(data, key, config)`: callback function when a request finishes successfully
* `onError(err, key, config)`: callback function when a request returns an error
* `onErrorRetry(err, key, config, revalidate, revalidateOps)`: handler for error retry
* `onDiscarded(key)`: callback function when a request is ignored due to race conditions
* `compare(a, b)`: comparison function used to detect when returned data has changed, to avoid spurious rerenders. By default, [stable-hash](https://github.com/shuding/stable-hash) is used.
* `isPaused()`: function to detect whether pause revalidations, will ignore fetched data and errors when it returns `true`. Returns `false` by default.
* `use`: array of middleware functions [(details)](/docs/middleware)

<Callout emoji="💡">
  When under a slow network (2G, {'<='} 70Kbps), <code>errorRetryInterval</code> will be 10s, and{' '}
  <code>loadingTimeout</code> will be 5s by default.
</Callout>

You can also use [global configuration](/docs/global-configuration) to provide default options.

---
title: Arguments
type: reference
summary: Pass arguments to SWR fetcher functions.
prerequisites:

* /docs/getting-started
related:
* /docs/data-fetching
* /docs/conditional-fetching

---

# Arguments

By default, `key` will be passed to `fetcher` as the argument. So the following 3 expressions are equivalent:

```js
useSWR('/api/user', () => fetcher('/api/user'))
useSWR('/api/user', url => fetcher(url))
useSWR('/api/user', fetcher)
```

## Multiple Arguments

In some scenarios, it's useful to pass multiple arguments (can be any value or object) to the `fetcher` function.
For example an authorized fetch request:

```js
useSWR('/api/user', url => fetchWithToken(url, token))
```

This is **incorrect**. Because the identifier (also the cache key) of the data is `'/api/user'`,
even if `token` changes, SWR will still use the same key and return the wrong data.

Instead, you can use an **array** as the `key` parameter, which contains multiple arguments of `fetcher`:

```js
const { data: user } = useSWR(['/api/user', token], ([url, token]) => fetchWithToken(url, token))
```

The `fetcher` function accepts the `key` parameter as is, and the cache key will also be associated with the entire `key` argument. In the above example, `url` and `token` are both tied to the cache key.

<Callout emoji="⚠️">
  In the previous versions (\< 2.0.0), The `fetcher` function will receive the spreaded arguments from original `key` when the `key` argument is array type. E.g., key `[url, token]` will become 2 arguments `(url, token)` for `fetcher` function.
</Callout>

## Passing Objects

<Callout>
  Since SWR 1.1.0, object-like keys will be serialized under the hood automatically.
</Callout>

Say you have another function that fetches data with a user scope: `fetchWithUser(api, user)`. You can do the following:

```js
const { data: user } = useSWR(['/api/user', token], fetchWithToken)

// ...and then pass it as an argument to another useSWR hook
const { data: orders } = useSWR(user ? ['/api/orders', user] : null, fetchWithUser)
```

You can directly pass an object as the key, and `fetcher` will receive that object too:

```js
const { data: orders } = useSWR({ url: '/api/orders', args: user }, fetcher)
```

<Callout emoji="⚠️">
  In older versions (\< 1.1.0), SWR **shallowly** compares the arguments on every render, and triggers revalidation if any of them has changed.
</Callout>

---
title: Conditional Fetching
type: guide
summary: Conditionally fetch data based on dependencies or user state.
prerequisites:

* /docs/data-fetching
related:
* /docs/data-fetching
* /docs/arguments

---

# Conditional Fetching

## Conditional

Use `null` or pass a function as `key` to conditionally fetch data. If the function throws or returns a falsy value, SWR will not start the request.

```js
// conditionally fetch
const { data } = useSWR(shouldFetch ? '/api/data' : null, fetcher)

// ...or return a falsy value
const { data } = useSWR(() => shouldFetch ? '/api/data' : null, fetcher)

// ...or throw an error when user.id is not defined
const { data } = useSWR(() => '/api/data?uid=' + user.id, fetcher)
```

## Dependent

SWR also allows you to fetch data that depends on other data. It ensures the maximum possible parallelism (avoiding waterfalls), as well as serial fetching when a piece of dynamic data is required for the next data fetch to happen.

```js
function MyProjects () {
  const { data: user } = useSWR('/api/user')
  const { data: projects } = useSWR(() => '/api/projects?uid=' + user.id)
  // When passing a function, SWR will use the return
  // value as `key`. If the function throws or returns
  // falsy, SWR will know that some dependencies are not
  // ready. In this case `user.id` throws when `user`
  // isn't loaded.

  if (!projects) return 'loading...'
  return 'You have ' + projects.length + ' projects'
}
```

---
title: Data Fetching
type: guide
summary: Fetch data with SWR using custom fetcher functions.
prerequisites:

* /docs/getting-started
related:
* /docs/error-handling
* /docs/arguments

---

# Data Fetching

```js
const { data, error } = useSWR(key, fetcher)
```

This is the very fundamental API of SWR. The `fetcher` here is an async function that **accepts the `key`** of SWR, and returns the data.

The returned value will be passed as `data`, and if it throws, it will be caught as `error`.

<Callout emoji="💡">
  Note that <code>fetcher</code> can be omitted from the parameters if it's{' '}
  <Link href="/docs/global-configuration">provided globally</Link>.
</Callout>

## Fetch

You can use any library to handle data fetching, for example a `fetch` polyfill [developit/unfetch](https://github.com/developit/unfetch):

```js
import fetch from 'unfetch'

const fetcher = url => fetch(url).then(r => r.json())

function App () {
  const { data, error } = useSWR('/api/data', fetcher)
  // ...
}
```

<Callout emoji="💡">
  If you are using <strong>Next.js</strong>, you don't need to import this polyfill:<br />
  <a target="_blank" rel="noopener" href="https://nextjs.org/blog/next-9-1-7#new-built-in-polyfills-fetch-url-and-objectassign">New Built-In Polyfills: fetch(), URL, and Object.assign</a>
</Callout>

## Axios

```js
import axios from 'axios'

const fetcher = url => axios.get(url).then(res => res.data)

function App () {
  const { data, error } = useSWR('/api/data', fetcher)
  // ...
}
```

## GraphQL

Or using GraphQL with libs like [graphql-request](https://github.com/prisma-labs/graphql-request):

```js
import { request } from 'graphql-request'

const fetcher = query => request('/api/graphql', query)

function App () {
  const { data, error } = useSWR(
    `{
      Movie(title: "Inception") {
        releaseDate
        actors {
          name
        }
      }
    }`,
    fetcher
  )
  // ...
}
```

*If you want to pass variables to a GraphQL query, check out [Multiple Arguments](/docs/arguments).*

---
title: Error Handling
type: guide
summary: Handle errors when fetching data with SWR.
prerequisites:

* /docs/getting-started
related:
* /docs/data-fetching
* /docs/revalidation

---

# Error Handling

If an error is thrown inside [`fetcher`](/docs/data-fetching), it will be returned as `error` by the hook.

```js
const fetcher = url => fetch(url).then(r => r.json())

// ...
const { data, error } = useSWR('/api/user', fetcher)
```

The `error` object will be defined if the fetch promise is rejected.

## Status Code and Error Object

Sometimes we want an API to return an error object alongside the status code.
Both of them are useful for the client.

We can customize our `fetcher` to return more information. If the status code is not `2xx`,
we consider it an error even if it can be parsed as JSON:

```js
const fetcher = async url => {
  const res = await fetch(url)

  // If the status code is not in the range 200-299,
  // we still try to parse and throw it.
  if (!res.ok) {
    const error = new Error('An error occurred while fetching the data.')
    // Attach extra info to the error object.
    error.info = await res.json()
    error.status = res.status
    throw error
  }

  return res.json()
}

// ...
const { data, error } = useSWR('/api/user', fetcher)
// error.info === {
//   message: "You are not authorized to access this resource.",
//   documentation_url: "..."
// }
// error.status === 403
```

<Callout emoji="💡">
  Note that <code>data</code> and <code>error</code> can exist at the same time. So the UI can display the existing data,
  while knowing the upcoming request has failed.
</Callout>

[Here](/examples/error-handling) we have an example.

## Error Retry

SWR uses the [exponential backoff algorithm](https://en.wikipedia.org/wiki/Exponential_backoff) to retry the request on error.
The algorithm allows the app to recover from errors quickly, but not waste resources retrying too often.

You can also override this behavior via the [onErrorRetry](/docs/api#options) option:

```js
useSWR('/api/user', fetcher, {
  onErrorRetry: (error, key, config, revalidate, { retryCount }) => {
    // Never retry on 404.
    if (error.status === 404) return

    // Never retry for a specific key.
    if (key === '/api/user') return

    // Only retry up to 10 times.
    if (retryCount >= 10) return

    // Retry after 5 seconds.
    setTimeout(() => revalidate({ retryCount }), 5000)
  }
})
```

This callback gives you the flexibility to retry based on various conditions. You can also disable it by setting `shouldRetryOnError: false`.

It's also possible to provide it via the [Global Configuration](/docs/global-configuration) context.

## Global Error Report

You can always get the `error` object inside the component reactively.
But in case you want to handle the error globally, to notify the UI to show a [toast](https://vercel.com/design/toast) or a [snackbar](https://material.io/components/snackbars), or report it somewhere such as [Sentry](https://sentry.io),
there's an [`onError`](/docs/api#options) event:

```jsx
<SWRConfig value={{
  onError: (error, key) => {
    if (error.status !== 403 && error.status !== 404) {
      // We can send the error to Sentry,
      // or show a notification UI.
    }
  }
}}>
  <MyApp />
</SWRConfig>
```

---
title: Getting Started
type: guide
summary: Install and set up SWR for data fetching in React applications.
related:

* /docs/data-fetching
* /docs/api

---

# Getting Started

## Installation

Inside your React project directory, run the following:

<CodeBlockTabs defaultValue="npm">
  <CodeBlockTabsList>
    <CodeBlockTabsTrigger value="npm">
      npm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="pnpm">
      pnpm
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="yarn">
      yarn
    </CodeBlockTabsTrigger>

    <CodeBlockTabsTrigger value="bun">
      bun
    </CodeBlockTabsTrigger>
  </CodeBlockTabsList>

  <CodeBlockTab value="npm">
    ```bash
    npm i swr
    ```
  </CodeBlockTab>

  <CodeBlockTab value="pnpm">
    ```bash
    pnpm add swr
    ```
  </CodeBlockTab>

  <CodeBlockTab value="yarn">
    ```bash
    yarn add swr
    ```
  </CodeBlockTab>

  <CodeBlockTab value="bun">
    ```bash
    bun add swr
    ```
  </CodeBlockTab>
</CodeBlockTabs>

## Quick Start

For normal RESTful APIs with JSON data, first you need to create a `fetcher` function, which is just a wrapper of the native `fetch`:

```jsx
const fetcher = (...args) => fetch(...args).then(res => res.json())
```

<Callout emoji="💡">
  If you want to use GraphQL API or libs like Axios, you can create your own fetcher function.
  Check <Link href="/docs/data-fetching">here</Link> for more examples.
</Callout>

Then you can import `useSWR` and start using it inside any function components:

```jsx
import useSWR from 'swr'

function Profile ({ userId }) {
  const { data, error, isLoading } = useSWR(`/api/user/${userId}`, fetcher)

  if (error) return <div>failed to load</div>
  if (isLoading) return <div>loading...</div>

  // render data
  return <div>hello {data.name}!</div>
}
```

Normally, there're 3 possible states of a request: "loading", "ready", or "error". You can use the value of `data`, `error` and `isLoading` to
determine the current state of the request, and return the corresponding UI.

## Make It Reusable

When building a web app, you might need to reuse the data in many places of the UI. It is incredibly easy to create reusable data hooks
on top of SWR:

```jsx
function useUser (id) {
  const { data, error, isLoading } = useSWR(`/api/user/${id}`, fetcher)

  return {
    user: data,
    isLoading,
    isError: error
  }
}
```

And use it in your components:

```jsx
function Avatar ({ userId }) {
  const { user, isLoading, isError } = useUser(userId)

  if (isLoading) return <Spinner />
  if (isError) return <Error />
  return <img src={user.avatar} />
}
```

By adopting this pattern, you can forget about **fetching** data in the imperative way: start the request, update the loading state, and return the final result.
Instead, your code is more declarative: you just need to specify what data is used by the component.

## Example

In a real-world example, our website shows a navbar and the content, both depend on `user`:

<div className="mt-8">
  <Welcome />
</div>

Traditionally, we fetch data once using `useEffect` in the top level component, and pass it to child components via props (notice that we don't handle error state for now):

```jsx {7-11,17,18,27}
// page component

function Page ({ userId }) {
  const [user, setUser] = useState(null)

  // fetch data
  useEffect(() => {
    fetch(`/api/user/${userId}`)
      .then(res => res.json())
      .then(data => setUser(data))
  }, [userId])

  // global loading state
  if (!user) return <Spinner/>

  return <div>
    <Navbar user={user} />
    <Content user={user} />
  </div>
}

// child components

function Navbar ({ user }) {
  return <div>
    ...
    <Avatar user={user} />
  </div>
}

function Content ({ user }) {
  return <h1>Welcome back, {user.name}</h1>
}

function Avatar ({ user }) {
  return <img src={user.avatar} alt={user.name} />
}
```

Usually, we need to keep all the data fetching in the top level component and add props to every component deep down the tree.
The code will become harder to maintain if we add more data dependency to the page.

Although we can avoid passing props using [Context](https://react.dev/learn/passing-data-deeply-with-context), there's still the dynamic content problem:
components inside the page content can be dynamic, and the top level component might not know what data will be needed by its child components.

SWR solves the problem perfectly. With the `useUser` hook we just created, the code can be refactored to:

```jsx {20,26}
// page component

function Page ({ userId }) {
  return <div>
    <Navbar userId={userId} />
    <Content userId={userId} />
  </div>
}

// child components

function Navbar ({ userId }) {
  return <div>
    ...
    <Avatar userId={userId} />
  </div>
}

function Content ({ userId }) {
  const { user, isLoading } = useUser(userId)
  if (isLoading) return <Spinner />
  return <h1>Welcome back, {user.name}</h1>
}

function Avatar ({ userId }) {
  const { user, isLoading } = useUser(userId)
  if (isLoading) return <Spinner />
  return <img src={user.avatar} alt={user.name} />
}
```

Data is now **bound** to the components which need the data, and all components are **independent** to each other.
All the parent components don't need to know anything about the data or passing data around. They just render.
The code is much simpler and easier to maintain now.

The most beautiful thing is that there will be only **1 request** sent to the API, because they use the same SWR key and
the request is **deduped**, **cached** and **shared** automatically.

Also, the application now has the ability to refetch the data on [user focus or network reconnect](/docs/revalidation)!
That means, when the user's laptop wakes from sleep or they switch between browser tabs, the data will be refreshed automatically.

---
title: Global Configuration
type: reference
summary: Configure default options for all SWR hooks.
prerequisites:

* /docs/getting-started
related:
* /docs/api
* /docs/middleware

---

# Global Configuration

The context `SWRConfig` can provide global configurations ([options](/docs/api)) for all SWR hooks.

```jsx
<SWRConfig value={options}>
  <Component/>
</SWRConfig>
```

In this example, all SWR hooks will use the same fetcher provided to load JSON data, and refresh every 3 seconds by default:

```jsx
import useSWR, { SWRConfig } from 'swr'

function Dashboard () {
  const { data: events } = useSWR('/api/events')
  const { data: projects } = useSWR('/api/projects')
  const { data: user } = useSWR('/api/user', { refreshInterval: 0 }) // override

  // ...
}

function App () {
  return (
    <SWRConfig 
      value={{
        refreshInterval: 3000,
        fetcher: (resource, init) => fetch(resource, init).then(res => res.json())
      }}
    >
      <Dashboard />
    </SWRConfig>
  )
}
```

## Nesting Configurations

`SWRConfig` merges the configuration from the parent context. It can receive either an object or a functional configuration. The functional one receives the parent configuration as argument and returns a new configuration that you can customize yourself.

### Object Configuration Example

```jsx
import { SWRConfig, useSWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig
      value={{
        dedupingInterval: 100,
        refreshInterval: 100,
        fallback: { a: 1, b: 1 },
      }}
    >
      <SWRConfig
        value={{
          dedupingInterval: 200, // will override the parent value since the value is primitive
          fallback: { a: 2, c: 2 }, // will merge with the parent value since the value is a mergeable object
        }}
      >
        <Page />
      </SWRConfig>
    </SWRConfig>
  )
}

function Page() {
  const config = useSWRConfig()
  // {
  //   dedupingInterval: 200,
  //   refreshInterval: 100,
  //   fallback: { a: 2,  b: 1, c: 2 },
  // }
}
```

### Functional Configuration Example

```jsx
import { SWRConfig, useSWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig
      value={{
        dedupingInterval: 100,
        refreshInterval: 100,
        fallback: { a: 1, b: 1 },
      }}
    >
      <SWRConfig
        value={parent => ({
          dedupingInterval: parent.dedupingInterval * 5,
          fallback: { a: 2, c: 2 },
        })}
      >
        <Page />
      </SWRConfig>
    </SWRConfig>
  )
}

function Page() {
  const config = useSWRConfig()
  // {
  //   dedupingInterval: 500,
  //   fallback: { a: 2, c: 2 },
  // }
}
```

## Extra APIs

### Cache Provider

Besides all the [options](/docs/api) listed, `SWRConfig` also accepts an optional `provider` function. Please refer to the [Cache](/docs/advanced/cache) section for more details.

```jsx
<SWRConfig value={{ provider: () => new Map() }}>
  <Dashboard />
</SWRConfig>
```

### Access To Global Configurations

You can use the `useSWRConfig` hook to get the global configurations, as well as [`mutate`](/docs/mutation) and [`cache`](/docs/advanced/cache):

```jsx
import { useSWRConfig } from 'swr'

function Component () {
  const { refreshInterval, mutate, cache, ...restConfig } = useSWRConfig()

  // ...
}
```

Nested configurations will be extended. If no `<SWRConfig>` is used, it will return the default ones.

---
title: Middleware
type: conceptual
summary: Extend SWR with custom middleware.
prerequisites:

* /docs/getting-started
related:
* /docs/global-configuration

---

# Middleware

<Callout>
  Upgrade to the latest version (≥ 1.0.0) to use this feature.
</Callout>

The middleware feature is a new addition in SWR 1.0 that enables you to execute logic before and after SWR hooks.

## Usage

Middleware receive the SWR hook and can execute logic before and after running it. If there are multiple middleware, each middleware wraps the next middleware. The last middleware in the list will receive the original SWR hook `useSWR`.

### API

*Notes: The function name shouldn't be capitalized (e.g. `myMiddleware` instead of `MyMiddleware`) or React lint rules will throw `Rules of Hook` error*

[TypeScript](https://swr.vercel.app/docs/typescript#middleware-types)

```jsx
function myMiddleware (useSWRNext) {
  return (key, fetcher, config) => {
    // Before hook runs...

    // Handle the next middleware, or the `useSWR` hook if this is the last one.
    const swr = useSWRNext(key, fetcher, config)

    // After hook runs...
    return swr
  }
}
```

You can pass an array of middleware as an option to `SWRConfig` or `useSWR`:

```jsx
<SWRConfig value={{ use: [myMiddleware] }}>

// or...

useSWR(key, fetcher, { use: [myMiddleware] })
```

### Extend

Middleware will be extended like regular options. For example:

```jsx
function Bar () {
  useSWR(key, fetcher, { use: [c] })
  // ...
}

function Foo() {
  return (
    <SWRConfig value={{ use: [a] }}>
      <SWRConfig value={{ use: [b] }}>
        <Bar/>
      </SWRConfig>
    </SWRConfig>
  )
}
```

is equivalent to:

```js
useSWR(key, fetcher, { use: [a, b, c] })
```

### Multiple Middleware

Each middleware wraps the next middleware, and the last one just wraps the SWR hook. For example:

```jsx
useSWR(key, fetcher, { use: [a, b, c] })
```

The order of middleware executions will be `a → b → c`, as shown below:

```plaintext
enter a
  enter b
    enter c
      useSWR()
    exit  c
  exit  b
exit  a
```

## Examples

### Request Logger

Let's build a simple request logger middleware as an example. It prints out all the fetcher requests sent from this SWR hook. You can also use this middleware for all SWR hooks by adding it to `SWRConfig`.

```jsx
function logger(useSWRNext) {
  return (key, fetcher, config) => {
    // Add logger to the original fetcher.
    const extendedFetcher = (...args) => {
      console.log('SWR Request:', key)
      return fetcher(...args)
    }

    // Execute the hook with the new fetcher.
    return useSWRNext(key, extendedFetcher, config)
  }
}

// ... inside your component
useSWR(key, fetcher, { use: [logger] })
```

Every time the request is fired, it outputs the SWR key to the console:

```plaintext
SWR Request: /api/user1
SWR Request: /api/user2
```

### Keep Previous Result

Sometimes you want the data returned by `useSWR` to be "laggy". Even if the key changes,
you still want it to return the previous result until the new data has loaded.

This can be built as a laggy middleware together with `useRef`. In this example, we are also going to
extend the returned object of the `useSWR` hook:

```jsx
import { useRef, useEffect, useCallback } from 'react'

// This is a SWR middleware for keeping the data even if key changes.
function laggy(useSWRNext) {
  return (key, fetcher, config) => {
    // Use a ref to store previous returned data.
    const laggyDataRef = useRef()

    // Actual SWR hook.
    const swr = useSWRNext(key, fetcher, config)

    useEffect(() => {
      // Update ref if data is not undefined.
      if (swr.data !== undefined) {
        laggyDataRef.current = swr.data
      }
    }, [swr.data])

    // Expose a method to clear the laggy data, if any.
    const resetLaggy = useCallback(() => {
      laggyDataRef.current = undefined
    }, [])

    // Fallback to previous data if the current data is undefined.
    const dataOrLaggyData = swr.data === undefined ? laggyDataRef.current : swr.data

    // Is it showing previous data?
    const isLagging = swr.data === undefined && laggyDataRef.current !== undefined

    // Also add a `isLagging` field to SWR.
    return Object.assign({}, swr, {
      data: dataOrLaggyData,
      isLagging,
      resetLaggy,
    })
  }
}
```

When you need a SWR hook to be laggy, you can then use this middleware:

```js
const { data, isLagging, resetLaggy } = useSWR(key, fetcher, { use: [laggy] })
```

### Serialize Object Keys

<Callout>
  Since SWR 1.1.0, object-like keys will be serialized under the hood automatically.
</Callout>

<Callout emoji="⚠️">
  In older versions (\< 1.1.0), SWR **shallowly** compares the arguments on every render, and triggers revalidation if any of them has changed.
  If you are passing serializable objects as the key. You can serialize object keys to ensure its stability, a simple middleware can help:
</Callout>

```jsx
function serialize(useSWRNext) {
  return (key, fetcher, config) => {
    // Serialize the key.
    const serializedKey = Array.isArray(key) ? JSON.stringify(key) : key

    // Pass the serialized key, and unserialize it in fetcher.
    return useSWRNext(serializedKey, (k) => fetcher(...JSON.parse(k)), config)
  }
}

// ...
useSWR(['/api/user', { id: '73' }], fetcher, { use: [serialize] })

// ... or enable it globally with
<SWRConfig value={{ use: [serialize] }}>
```

You don’t need to worry that object might change between renders. It’s always serialized to the same string, and the fetcher will still receive those object arguments.

<Callout>
  Furthermore, you can use libs like [fast-json-stable-stringify](https://github.com/epoberezkin/fast-json-stable-stringify) instead of `JSON.stringify` — faster and stabler.
</Callout>

---
title: Mutation & Revalidation
type: guide
summary: Mutate cached data and trigger revalidation.
prerequisites:

* /docs/data-fetching
related:
* /docs/data-fetching
* /docs/revalidation

---

# Mutation & Revalidation

SWR provides the [`mutate`](/docs/mutation#mutate) and [`useSWRMutation`](/docs/mutation#useswrmutation) APIs for mutating remote data and related cache.

## `mutate`

There're 2 ways to use the `mutate` API to mutate the data, the global mutate API which can mutate any key and the bound mutate API which only can mutate the data of corresponding SWR hook.

#### Global Mutate

The recommended way to get the global mutator is to use the [`useSWRConfig`](/docs/global-configuration#access-to-global-configurations) hook:

```js
import { useSWRConfig } from "swr"

function App() {
  const { mutate } = useSWRConfig()
  mutate(key, data, options)
}
```

You can also import it globally:

```js
import { mutate } from "swr"

function App() {
  mutate(key, data, options)
}
```

<Callout emoji="⚠️">
  Using global mutator only with the `key` parameter will ***not update the cache or trigger revalidation*** unless there is a mounted SWR hook using the same key.
</Callout>

#### Bound Mutate

Bound mutate is the short path to mutate the current key with data. Which `key` is bounded to the `key` passing to `useSWR`, and receive the `data` as the first argument.

It is functionally equivalent to the global `mutate` function in the previous section but does not require the `key` parameter:

```jsx
import useSWR from 'swr'

function Profile () {
  const { data, mutate } = useSWR('/api/user', fetcher)

  return (
    <div>
      <h1>My name is {data.name}.</h1>
      <button onClick={async () => {
        const newName = data.name.toUpperCase()
        // send a request to the API to update the data
        await requestUpdateUsername(newName)
        // update the local data immediately and revalidate (refetch)
        // NOTE: key is not required when using useSWR's mutate as it's pre-bound
        mutate({ ...data, name: newName })
      }}>Uppercase my name!</button>
    </div>
  )
}
```

#### Revalidation

When you call `mutate(key)` (or just `mutate()` with the bound mutate API) without any data, it will trigger a revalidation (mark the data as expired and trigger a refetch)
for the resource. This example shows how to automatically refetch the login info (e.g. inside `<Profile/>`)
when the user clicks the “Logout” button:

```jsx {14}
import useSWR, { useSWRConfig } from 'swr'

function App () {
  const { mutate } = useSWRConfig()

  return (
    <div>
      <Profile />
      <button onClick={() => {
        // set the cookie as expired
        document.cookie = 'token=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;'

        // tell all SWRs with this key to revalidate
        mutate('/api/user')
      }}>
        Logout
      </button>
    </div>
  )
}
```

<Callout>
  It broadcasts to SWR hooks under the same [cache provider](/docs/advanced/cache) scope. If no cache provider exists, it will broadcast to all SWR hooks.
</Callout>

### API

#### Parameters

* `key`: same as `useSWR`'s `key`, but a function behaves as [a filter function](/docs/mutation#mutate-multiple-items)
* `data`: data to update the client cache, or an async function for the remote mutation
* `options`: accepts the following options
  * `optimisticData`: data to immediately update the client cache, or a function that receives current data and returns the new client cache data, usually used in optimistic UI.
  * `revalidate = true`: should the cache revalidate once the asynchronous update resolves. If set to a function, the function receives `data` and `key`.
  * `populateCache = true`: should the result of the remote mutation be written to the cache, or a function that receives new result and current result as arguments and returns the mutation result.
  * `rollbackOnError = true`: should the cache rollback if the remote mutation errors, or a function that receives the error thrown from fetcher as arguments and returns a boolean whether should rollback or not.
  * `throwOnError = true`: should the mutate call throw the error when fails.

#### Return Values

`mutate` returns the results the `data` parameter has been resolved. The function passed to `mutate` will return an updated data which is used to update the corresponding cache value. If there is an error thrown while executing the function, the error will be thrown so it can be handled appropriately.

```jsx
try {
  const user = await mutate('/api/user', updateUser(newUser))
} catch (error) {
  // Handle an error while updating the user here
}
```

## `useSWRMutation`

SWR also provides `useSWRMutation` as a hook for remote mutations. The remote mutations are only triggered manually, instead of automatically like `useSWR`.

Also, this hook doesn’t share states with other `useSWRMutation` hooks.

```tsx
import useSWRMutation from 'swr/mutation'

// Fetcher implementation.
// The extra argument will be passed via the `arg` property of the 2nd parameter.
// In the example below, `arg` will be `'my_token'`
async function updateUser(url, { arg }: { arg: string }) {
  await fetch(url, {
    method: 'POST',
    headers: {
      Authorization: `Bearer ${arg}`
    }
  })
}

function Profile() {
  // A useSWR + mutate like API, but it will not start the request automatically.
  const { trigger } = useSWRMutation('/api/user', updateUser, options)

  return <button onClick={() => {
    // Trigger `updateUser` with a specific argument.
    trigger('my_token')
  }}>Update User</button>
}
```

### API

#### Parameters

* `key`: same as [`mutate`](/docs/mutation#mutate)'s `key`
* `fetcher(key, { arg })`: an async function for remote mutation
* `options`: an optional object with the following properties:
  * `optimisticData`: same as `mutate`'s `optimisticData`
  * `revalidate = true`: same as `mutate`'s `revalidate`
  * `populateCache = false`: same as `mutate`'s `populateCache`, but the default is `false`
  * `rollbackOnError = true`: same as `mutate`'s `rollbackOnError`
  * `throwOnError = true`: same as `mutate`'s `throwOnError`
  * `onSuccess(data, key, config)`:　 callback function when a remote mutation has been finished successfully
  * `onError(err, key, config)`: callback function when a remote mutation has returned an error

#### Return Values

* `data`: data for the given key returned from `fetcher`
* `error`: error thrown by `fetcher` (or undefined)
* `trigger(arg, options)`: a function to trigger a remote mutation
* `reset`: a function to reset the state (`data`, `error`, `isMutating`)
* `isMutating`: if there's an ongoing remote mutation

### Basic Usage

```tsx
import useSWRMutation from 'swr/mutation'

async function sendRequest(url, { arg }: { arg: { username: string }}) {
  return fetch(url, {
    method: 'POST',
    body: JSON.stringify(arg)
  }).then(res => res.json())
}

function App() {
  const { trigger, isMutating } = useSWRMutation('/api/user', sendRequest, /* options */)

  return (
    <button
      disabled={isMutating}
      onClick={async () => {
        try {
          const result = await trigger({ username: 'johndoe' }, /* options */)
        } catch (e) {
          // error handling
        }
      }}
    >
      Create User
    </button>
  )
}
```

If you want to use the mutation results in rendering, you can get them from the return values of `useSWRMutation`.

```jsx
const { trigger, data, error } = useSWRMutation('/api/user', sendRequest)
```

`useSWRMutation` shares a cache store with `useSWR`, so it can detect and avoid race conditions between `useSWR`. It also supports `mutate`'s functionalities like optimistic updates and rollback on errors. You can pass these options `useSWRMutation` and its `trigger` function.

```jsx
const { trigger } = useSWRMutation('/api/user', updateUser, {
  optimisticData: current => ({ ...current, name: newName })
})

// or

trigger(newName, {
  optimisticData: current => ({ ...current, name: newName })
})
```

### Defer loading data until needed

You can also use `useSWRMutation` for loading data. `useSWRMutation` won't start requesting until `trigger` is called, so you can defer loading data when you actually need it.

```jsx
import { useState } from 'react'
import useSWRMutation from 'swr/mutation'

const fetcher = url => fetch(url).then(res => res.json())

const Page = () => {
  const [show, setShow] = useState(false)
  // data is undefined until trigger is called
  const { data: user, trigger } = useSWRMutation('/api/user', fetcher);

  return (
    <div>
      <button onClick={() => {
        trigger();
        setShow(true);
      }}>Show User</button>
      {show && user ? <div>{user.name}</div> : null}
    </div>
  );
}
```

## Optimistic Updates

In many cases, applying local mutations to data is a good way to make changes
feel faster — no need to wait for the remote source of data.

With the `optimisticData` option, you can update your local data manually, while
waiting for the remote mutation to finish. Composing `rollbackOnError` you can also
control when to rollback the data.

```jsx
import useSWR, { useSWRConfig } from 'swr'

function Profile () {
  const { mutate } = useSWRConfig()
  const { data } = useSWR('/api/user', fetcher)

  return (
    <div>
      <h1>My name is {data.name}.</h1>
      <button onClick={async () => {
        const newName = data.name.toUpperCase()
        const user = { ...data, name: newName }
        const options = {
          optimisticData: user,
          rollbackOnError(error) {
            // If it's timeout abort error, don't rollback
            return error.name !== 'AbortError'
          },
        }

        // updates the local data immediately
        // send a request to update the data
        // triggers a revalidation (refetch) to make sure our local data is correct
        mutate('/api/user', updateFn(user), options);
      }}>Uppercase my name!</button>
    </div>
  )
}
```

> The **`updateFn`** should be a promise or asynchronous function to handle the remote mutation, it should return updated data.

You can also pass a function to `optimisticData` to make it depending on the current data:

```jsx
import useSWR, { useSWRConfig } from 'swr'

function Profile () {
  const { mutate } = useSWRConfig()
  const { data } = useSWR('/api/user', fetcher)

  return (
    <div>
      <h1>My name is {data.name}.</h1>
      <button onClick={async () => {
        const newName = data.name.toUpperCase()
        mutate('/api/user', updateUserName(newName), {
          optimisticData: user => ({ ...user, name: newName }),
          rollbackOnError: true
        });
      }}>Uppercase my name!</button>
    </div>
  )
}
```

You can also create the same thing with `useSWRMutation` and `trigger`:

```jsx
import useSWRMutation from 'swr/mutation'

function Profile () {
  const { trigger } = useSWRMutation('/api/user', updateUserName)

  return (
    <div>
      <h1>My name is {data.name}.</h1>
      <button onClick={async () => {
        const newName = data.name.toUpperCase()

        trigger(newName, {
          optimisticData: user => ({ ...user, name: newName }),
          rollbackOnError: true
        })
      }}>Uppercase my name!</button>
    </div>
  )
}
```

## Rollback on Errors

When you have `optimisticData` set, it’s possible that the optimistic data gets
displayed to the user, but the remote mutation fails. In this case, you can leverage
`rollbackOnError` to revert the local cache to the previous state, to make sure
the user is seeing the correct data.

## Update Cache After Mutation

Sometimes, the remote mutation request directly returns the updated data, so there is no need to do an extra fetch to load it.
You can enable the `populateCache` option to update the cache for `useSWR` with the response of the mutation:

```jsx
const updateTodo = () => fetch('/api/todos/1', {
  method: 'PATCH',
  body: JSON.stringify({ completed: true })
})

mutate('/api/todos', updateTodo, {
  populateCache: (updatedTodo, todos) => {
    // filter the list, and return it with the updated item
    const filteredTodos = todos.filter(todo => todo.id !== '1')
    return [...filteredTodos, updatedTodo]
  },
  // Since the API already gives us the updated information,
  // we don't need to revalidate here.
  revalidate: false
})
```

Or with the `useSWRMutation` hook:

```jsx
useSWRMutation('/api/todos', updateTodo, {
  populateCache: (updatedTodo, todos) => {
    // filter the list, and return it with the updated item
    const filteredTodos = todos.filter(todo => todo.id !== '1')
    return [...filteredTodos, updatedTodo]
  },
  // Since the API already gives us the updated information,
  // we don't need to revalidate here.
  revalidate: false
})
```

When combined with `optimisticData` and `rollbackOnError`, you’ll get a perfect optimistic UI experience.

## Avoid Race Conditions

Both `mutate` and `useSWRMutation` can avoid race conditions between `useSWR`. For example,

```tsx
function Profile() {
  const { data } = useSWR('/api/user', getUser, { revalidateInterval: 3000 })
  const { trigger } = useSWRMutation('/api/user', updateUser)

  return <>
    {data ? data.username : null}
    <button onClick={() => trigger()}>Update User</button>
  </>
}
```

The normal `useSWR` hook might refresh its data any time due to focus, polling, or other conditions. This way the displayed username
can be as fresh as possible. However, since we have a mutation there that can happen at the nearly same time of a refetch of `useSWR`, there
could be a race condition that `getUser` request starts earlier, but takes longer than `updateUser`.

Luckily, `useSWRMutation` handles this for you automatically. After the mutation, it will tell `useSWR` to ditch the ongoing request and revalidate,
so the stale data will never be displayed.

## Mutate Based on Current Data

Sometimes, you want to update a part of your data based on the current data.

With `mutate`, you can pass an async function which will receive the current cached value, if any, and returns an updated document.

```jsx
mutate('/api/todos', async todos => {
  // let's update the todo with ID `1` to be completed,
  // this API returns the updated data
  const updatedTodo = await fetch('/api/todos/1', {
    method: 'PATCH',
    body: JSON.stringify({ completed: true })
  })

  // filter the list, and return it with the updated item
  const filteredTodos = todos.filter(todo => todo.id !== '1')
  return [...filteredTodos, updatedTodo]
// Since the API already gives us the updated information,
// we don't need to revalidate here.
}, { revalidate: false })
```

## Mutate Multiple Items

The global `mutate` API accepts a filter function, which accepts `key` as the argument and returns which keys to revalidate. The filter function is applied to all the existing cache keys:

```jsx
import { mutate } from 'swr'
// Or from the hook if you customized the cache provider:
// { mutate } = useSWRConfig()

mutate(
  key => typeof key === 'string' && key.startsWith('/api/item?id='),
  undefined,
  { revalidate: true }
)
```

This also works with any key type like an array. The mutation matches all keys, of which the first element is `'item'`.

```jsx
useSWR(['item', 123], ...)
useSWR(['item', 124], ...)
useSWR(['item', 125], ...)

mutate(
  key => Array.isArray(key) && key[0] === 'item',
  undefined,
  { revalidate: false }
)
```

The filter function is applied to all existing cache keys, so you should not assume the shape of keys when using multiple shapes of keys.

```jsx
// ✅ matching array key
mutate((key) => key[0].startsWith('/api'), data)
// ✅ matching string key
mutate((key) => typeof key === 'string' && key.startsWith('/api'), data)

// ❌ ERROR: mutate uncertain keys (array or string)
mutate((key: any) => /\/api/.test(key.toString()))
```

You can use the filter function to clear all cache data, which is useful when logging out:

```js
const clearCache = () => mutate(
  () => true,
  undefined,
  { revalidate: false }
)

// ...clear cache on logout
clearCache()
```

---
title: Pagination
type: guide
summary: Implement pagination and infinite loading patterns with SWR.
prerequisites:

* /docs/data-fetching
related:
* /docs/data-fetching
* /docs/mutation

---

# Pagination

<Callout emoji="✅">
  Please update to the latest version (≥ 0.3.0) to use this API. The previous <code>useSWRPages</code> API is now deprecated.
</Callout>

SWR provides a dedicated API `useSWRInfinite` to support common UI patterns such as **pagination** and **infinite loading**.

## When to Use `useSWR`

### Pagination

First of all, we might **NOT** need `useSWRInfinite` but can use just `useSWR` if we are building something like this:

<div className="mt-8">
  <Pagination />
</div>

...which is a typical pagination UI. Let's see how it can be easily implemented with
`useSWR`:

```jsx {5}
function App () {
  const [pageIndex, setPageIndex] = useState(0);

  // The API URL includes the page index, which is a React state.
  const { data } = useSWR(`/api/data?page=${pageIndex}`, fetcher);

  // ... handle loading and error states

  return <div>
    {data.map(item => <div key={item.id}>{item.name}</div>)}
    <button onClick={() => setPageIndex(pageIndex - 1)}>Previous</button>
    <button onClick={() => setPageIndex(pageIndex + 1)}>Next</button>
  </div>
}
```

Furthermore, we can create an abstraction for this "page component":

```jsx {13}
function Page ({ index }) {
  const { data } = useSWR(`/api/data?page=${index}`, fetcher);

  // ... handle loading and error states

  return data.map(item => <div key={item.id}>{item.name}</div>)
}

function App () {
  const [pageIndex, setPageIndex] = useState(0);

  return <div>
    <Page index={pageIndex}/>
    <button onClick={() => setPageIndex(pageIndex - 1)}>Previous</button>
    <button onClick={() => setPageIndex(pageIndex + 1)}>Next</button>
  </div>
}
```

Because of SWR's cache, we get the benefit to preload the next page. We render the next page inside
a hidden div, so SWR will trigger the data fetching of the next page. When the user navigates to the next page, the data is already there:

```jsx {6}
function App () {
  const [pageIndex, setPageIndex] = useState(0);

  return <div>
    <Page index={pageIndex}/>
    <div style={{ display: 'none' }}><Page index={pageIndex + 1}/></div>
    <button onClick={() => setPageIndex(pageIndex - 1)}>Previous</button>
    <button onClick={() => setPageIndex(pageIndex + 1)}>Next</button>
  </div>
}
```

With just 1 line of code, we get a much better UX. The `useSWR` hook is so powerful,
that most scenarios are covered by it.

### Infinite Loading

Sometimes we want to build an **infinite loading** UI, with a "Load More" button that appends data
to the list (or done automatically when you scroll):

<div className="mt-8">
  <Infinite />
</div>

To implement this, we need to make **dynamic number of requests** on this page. React Hooks have [a couple of rules](https://react.dev/reference/rules/rules-of-hooks),
so we **CANNOT** do something like this:

```jsx {5,6,7,8,9}
function App () {
  const [cnt, setCnt] = useState(1)

  const list = []
  for (let i = 0; i < cnt; i++) {
    // 🚨 This is wrong! Commonly, you can't use hooks inside a loop.
    const { data } = useSWR(`/api/data?page=${i}`)
    list.push(data)
  }

  return <div>
    {list.map((data, i) =>
      <div key={i}>{
        data.map(item => <div key={item.id}>{item.name}</div>)
      }</div>)}
    <button onClick={() => setCnt(cnt + 1)}>Load More</button>
  </div>
}
```

Instead, we can use the `<Page />` abstraction that we created to achieve it:

```jsx {5,6,7}
function App () {
  const [cnt, setCnt] = useState(1)

  const pages = []
  for (let i = 0; i < cnt; i++) {
    pages.push(<Page index={i} key={i} />)
  }

  return <div>
    {pages}
    <button onClick={() => setCnt(cnt + 1)}>Load More</button>
  </div>
}
```

### Advanced Cases

However, in some advanced use cases, the solution above doesn't work.

For example, we are still implementing the same "Load More" UI, but also need to display a number
about how many items are there in total. We can't use the `<Page />` solution anymore because
the top level UI (`<App />`) needs the data inside each page:

```jsx {10}
function App () {
  const [cnt, setCnt] = useState(1)

  const pages = []
  for (let i = 0; i < cnt; i++) {
    pages.push(<Page index={i} key={i} />)
  }

  return <div>
    <p>??? items</p>
    {pages}
    <button onClick={() => setCnt(cnt + 1)}>Load More</button>
  </div>
}
```

Also, if the pagination API is **cursor based**, that solution doesn't work either. Because each page
needs the data from the previous page, they're not isolated.

That's how this new `useSWRInfinite` Hook can help.

## useSWRInfinite

`useSWRInfinite` gives us the ability to trigger a number of requests with one Hook. This is how it looks:

```jsx
import useSWRInfinite from 'swr/infinite'

// ...
const { data, error, isLoading, isValidating, mutate, size, setSize } = useSWRInfinite(
  getKey, fetcher?, options?
)
```

Similar to `useSWR`, this new Hook accepts a function that returns the request key, a fetcher function, and options.
It returns all the values that `useSWR` returns, including 2 extra values: the page size and a page size setter, like a React state.

In infinite loading, one *page* is one request, and our goal is to fetch multiple pages and render them.

<Callout emoji="⚠️">
  If you are using SWR 0.x versions, `useSWRInfinite` needs to be imported from `swr`:<br />
  `import { useSWRInfinite } from 'swr'`
</Callout>

### API

#### Parameters

* `getKey`: a function that accepts the index and the previous page data, returns the key of a page
* `fetcher`: same as `useSWR`'s [fetcher function](/docs/data-fetching)
* `options`: accepts all the options that `useSWR` supports, with 4 extra options:
  * `initialSize = 1`: number of pages should be loaded initially
  * `revalidateAll = false`: always try to revalidate all pages
  * `revalidateFirstPage = true`: always try to revalidate the first page
  * `persistSize = false`: don't reset the page size to 1 (or `initialSize` if set) when the first page's key changes
  * `parallel = false`: fetches multiple pages in parallel

<Callout>
  Note that the `initialSize` option is not allowed to change in the lifecycle.
</Callout>

#### Return Values

* `data`: an array of fetch response values of each page
* `error`: same as `useSWR`'s `error`
* `isLoading`: same as `useSWR`'s `isLoading`
* `isValidating`: same as `useSWR`'s `isValidating`
* `mutate`: same as `useSWR`'s bound mutate function but manipulates the data array
* `size`: the number of pages that *will* be fetched and returned
* `setSize`: set the number of pages that need to be fetched

### Example 1: Index Based Paginated API

For normal index based APIs:

```plaintext
GET /users?page=0&limit=10
[
  { name: 'Alice', ... },
  { name: 'Bob', ... },
  { name: 'Cathy', ... },
  ...
]
```

```jsx {4,5,6,7,10}
// A function to get the SWR key of each page,
// its return value will be accepted by `fetcher`.
// If `null` is returned, the request of that page won't start.
const getKey = (pageIndex, previousPageData) => {
  if (previousPageData && !previousPageData.length) return null // reached the end
  return `/users?page=${pageIndex}&limit=10`                    // SWR key
}

function App () {
  const { data, size, setSize } = useSWRInfinite(getKey, fetcher)
  if (!data) return 'loading'

  // We can now calculate the number of all users
  let totalUsers = 0
  for (let i = 0; i < data.length; i++) {
    totalUsers += data[i].length
  }

  return <div>
    <p>{totalUsers} users listed</p>
    {data.map((users, index) => {
      // `data` is an array of each page's API response.
      return users.map(user => <div key={user.id}>{user.name}</div>)
    })}
    <button onClick={() => setSize(size + 1)}>Load More</button>
  </div>
}
```

The `getKey` function is the major difference between `useSWRInfinite` and `useSWR`.
It accepts the index of the current page, as well as the data from the previous page.
So both index based and cursor based pagination API can be supported nicely.

Also `data` is no longer just one API response. It's an array of multiple API responses:

```js
// `data` will look like this
[
  [
    { name: 'Alice', ... },
    { name: 'Bob', ... },
    { name: 'Cathy', ... },
    ...
  ],
  [
    { name: 'John', ... },
    { name: 'Paul', ... },
    { name: 'George', ... },
    ...
  ],
  ...
]
```

### Example 2: Cursor or Offset Based Paginated API

Let's say the API now requires a cursor and returns the next cursor alongside with the data:

```plaintext
GET /users?cursor=123&limit=10
{
  data: [
    { name: 'Alice' },
    { name: 'Bob' },
    { name: 'Cathy' },
    ...
  ],
  nextCursor: 456
}
```

We can change our `getKey` function to:

```jsx
const getKey = (pageIndex, previousPageData) => {
  // reached the end
  if (previousPageData && !previousPageData.data) return null

  // first page, we don't have `previousPageData`
  if (pageIndex === 0) return `/users?limit=10`

  // add the cursor to the API endpoint
  return `/users?cursor=${previousPageData.nextCursor}&limit=10`
}
```

### Parallel Fetching Mode

<Callout emoji="✅">
  Please update to the latest version (≥ 2.1.0) to use this API.
</Callout>

The default behavior of useSWRInfinite is to fetch data for each page in sequence, as key creation is based on the previously fetched data. However, fetching data sequentially for a large number of pages may not be optimal, particularly if the pages are not interdependent. By specifying `parallel` option to `true` will let you fetch pages independently in parallel, which can significantly speed up the loading process.

```jsx
// parallel = false (default)
// page1 ===> page2 ===> page3 ===> done
//
// parallel = true
// page1 ==> done
// page2 =====> done
// page3 ===> done
//
// previousPageData is always `null`
const getKey = (pageIndex, previousPageData) => {
  return `/users?page=${pageIndex}&limit=10`
}

function App () {
  const { data } = useSWRInfinite(getKey, fetcher, { parallel: true })
}
```

<Callout emoji="⚠️">
  The `previousPageData` argument of the `getKey` function becomes `null` when you enable the `parallel` option.
</Callout>

### Revalidate Specific Pages

<Callout emoji="✅">
  Please update to the latest version (≥ 2.2.5) to use this API.
</Callout>

The default behavior of the mutation of `useSWRInfinite` is to revalidate all pages that have been loaded. But you might want to revalidate only the specific pages that have been changed. You can revalidate only specific pages by passing a function to the `revalidate` option.

The `revalidate` function is called for each page.

```jsx
function App() {
  const { data, mutate, size } = useSWRInfinite(
    (index) => [`/api/?page=${index + 1}`, index + 1],
    fetcher
  );

  mutate(data, {
    // only revalidate the last page
    revalidate: (pageData, [url, page]) => page === size
  });
}
```

### Global Mutate with `useSWRInfinite`

`useSWRInfinite` stores all page data into the cache with a special cache key along with each page data, so you have to use `unstable_serialize` in `swr/infinite` to revalidate the data with the global mutate.

```jsx
import { useSWRConfig } from "swr"
import { unstable_serialize } from "swr/infinite"

function App() {
    const { mutate } = useSWRConfig()
    mutate(unstable_serialize(getKey))
}
```

<Callout emoji="⚠️">
  As the name implies, `unstable_serialize` is not a stable API, so we might change it in the future.
</Callout>

### Advanced Features

[Here is an example](/examples/infinite-loading) showing how you can implement the following features with `useSWRInfinite`:

* loading states
* show a special UI if it's empty
* disable the "Load More" button if reached the end
* changeable data source
* refresh the entire list

---
title: Prefetching Data
type: guide
summary: Prefetch data to improve perceived performance.
prerequisites:

* /docs/data-fetching
related:
* /docs/data-fetching
* /docs/advanced/performance

---

# Prefetching Data

## Top-Level Page Data

There’re many ways to prefetch the data for SWR. For top level requests, [`rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Preloading_content) is highly recommended:

```html
<link rel="preload" href="/api/data" as="fetch" crossorigin="anonymous">
```

Just put it inside your HTML `<head>`. It’s easy, fast and native.

It will prefetch the data when the HTML loads, even before JavaScript starts to download. All your incoming fetch requests with the same URL will reuse the result (including SWR, of course).

## Programmatically Prefetch

SWR provides the `preload` API to prefetch the resources programmatically and store the results in the cache. `preload` accepts `key` and `fetcher` as the arguments.

You can call `preload` even outside of React.

```jsx
import { useState } from 'react'
import useSWR, { preload } from 'swr'

const fetcher = (url) => fetch(url).then((res) => res.json())

// Preload the resource before rendering the User component below,
// this prevents potential waterfalls in your application.
// You can also start preloading when hovering the button or link, too.
preload('/api/user', fetcher)

function User() {
  const { data } = useSWR('/api/user', fetcher)
  ...
}

export default function App() {
  const [show, setShow] = useState(false)
  return (
    <div>
      <button onClick={() => setShow(true)}>Show User</button>
      {show ? <User /> : null}
    </div>
  )
}
```

Within React rendering tree, `preload` is also available to use in event handlers or effects.

```jsx
function App({ userId }) {
  const [show, setShow] = useState(false)

  // preload in effects
  useEffect(() => {
    preload('/api/user?id=' + userId, fetcher)
  }, [userId])

  return (
    <div>
      <button
        onClick={() => setShow(true)}
        {/* preload in event callbacks */}
        onHover={() => preload('/api/user?id=' + userId, fetcher)}
      >
        Show User
      </button>
      {show ? <User /> : null}
    </div>
  )
}
```

Together with techniques like [page prefetching](https://nextjs.org/docs/api-reference/next/router#routerprefetch) in Next.js, you will be able to load both next page and data instantly.

In Suspense mode, you should utilize `preload` to avoid waterfall problems.

```jsx
import useSWR, { preload } from 'swr'

// should call before rendering
preload('/api/user', fetcher);
preload('/api/movies', fetcher);

const Page = () => {
  // The below useSWR hooks will suspend the rendering, but the requests to `/api/user` and `/api/movies` have started by `preload` already,
  // so the waterfall problem doesn't happen.
  const { data: user } = useSWR('/api/user', fetcher, { suspense: true });
  const { data: movies } = useSWR('/api/movies', fetcher, { suspense: true });
  return (
    <div>
      <User user={user} />
      <Movies movies={movies} />
    </div>
  );
}
```

## Pre-fill Data

If you want to pre-fill existing data into the SWR cache, you can use the `fallbackData` option. For example:

```jsx
useSWR('/api/data', fetcher, { fallbackData: prefetchedData })
```

If SWR hasn't fetched the data yet, this hook will return `prefetchedData` as a fallback.

You can also configure this for all SWR hooks and multiple keys with `<SWRConfig>` and the `fallback` option. Check [Next.js SSG and SSR](/docs/with-nextjs) for more details.

## Pre-fetch in React Server Components (RSC)

When using Next.js App Router with React Server Components, you can prefetch data on the server and pass it to client components via `SWRConfig`. This approach allows you to leverage server-side data fetching while maintaining the benefits of SWR's client-side caching and revalidation.

For detailed information and examples, see the [Usage with Next.js](/docs/with-nextjs#prefetch-data-in-server-components) documentation.

---
title: Automatic Revalidation
type: conceptual
summary: Automatically revalidate stale data with focus, interval, and reconnect strategies.
prerequisites:

* /docs/getting-started
related:
* /docs/mutation
* /docs/conditional-fetching

---

# Automatic Revalidation

<Callout>
  If you want to manually revalidate the data, check <Link href="/docs/mutation">mutation</Link>.
</Callout>

## Revalidate on Focus

When you re-focus a page or switch between tabs, SWR automatically revalidates data.

This can be useful to immediately synchronize to the latest state. This is helpful for refreshing data in scenarios like stale mobile tabs, or laptops that **went to sleep**.

<Bleed>
  <Video src="https://raw.githubusercontent.com/vercel/swr-site/master/.github/videos/focus-revalidate.mp4" caption="Video: using focus revalidation to automatically sync login state between pages." ratio={307/768} className="mx-8 2xl:mx-24" />
</Bleed>

This feature is enabled by default. You can disable it via the [`revalidateOnFocus`](/docs/api) option.

## Revalidate on Interval

In many cases, data changes because of multiple devices, multiple users, multiple tabs. How can we over time update the data on screen?

SWR will give you the option to automatically refetch data. It’s **smart** which means refetching will only happen if the component associated with the hook is **on screen**.

<Bleed>
  <Video src="https://raw.githubusercontent.com/vercel/swr-site/master/.github/videos/refetch-interval.mp4" caption="Video: when a user makes a change, both sessions will eventually render the same data." ratio={307/768} className="mx-8 2xl:mx-24" />
</Bleed>

You can enable it by setting a [`refreshInterval`](/docs/api) value:

```js
useSWR('/api/todos', fetcher, { refreshInterval: 1000 })
```

There're also options such as `refreshWhenHidden` and `refreshWhenOffline`. Both are disabled by default so SWR won't fetch when the webpage is not on screen, or there's no network connection.

## Revalidate on Reconnect

It's useful to also revalidate when the user is back online. This scenario happens a lot when the user unlocks their computer, but the internet is not yet connected at the same moment.

To make sure the data is always up-to-date, SWR automatically revalidates when network recovers.

This feature is enabled by default. You can disable it via the [`revalidateOnReconnect`](/docs/api) option.

## Disable Automatic Revalidations

If the resource is **immutable**, that will never change if we revalidate again, we can disable all kinds of automatic revalidations for it.

Since version 1.0, SWR provides a helper hook `useSWRImmutable` to mark the resource as immutable:

```js
import useSWRImmutable from 'swr/immutable'

// ...
useSWRImmutable(key, fetcher, options)
```

It has the same API interface as the normal `useSWR` hook. You can also do the same thing by disabling the following revalidation options:

```js
useSWR(key, fetcher, {
  revalidateIfStale: false,
  revalidateOnFocus: false,
  revalidateOnReconnect: false
})

// equivalent to
useSWRImmutable(key, fetcher)
```

The `revalidateIfStale` controls if SWR should revalidate when it mounts and there is stale data.

These 2 hooks above do the **exact same** thing. Once the data is cached, they will never request it again.

## Revalidate on Mount

It's useful to force override SWR revalidation on mounting. By default, the value of `revalidateOnMount` is set to undefined.

A SWR hook mounts as:

* First it checks if `revalidateOnMount` is defined. It starts request if it's true, stop if it's false.

`revalidateIfStale` useful to control the mount behaviour. By default `revalidateIfStale` is set to true.

If `revalidateIfStale` is set to true it only refetches if there's any cache data else it will not refetch.

---
title: Subscription
type: guide
summary: Subscribe to real-time data sources with SWR.
prerequisites:

* /docs/getting-started
related:
* /docs/data-fetching

---

# Subscription

<Callout emoji="✅">
  Please update to the latest version (≥ 2.1.0) to use this API.
</Callout>

## `useSWRSubscription`

`useSWRSubscription` is a React hook that allows subscribing to real-time data sources with SWR.

```tsx
useSWRSubscription<Data, Error>(key: Key, subscribe: (key: Key, options: { next: (error?: Error | null, data: Data) => void }) => () => void): { data?: Data, error?: Error }
```

### API

This hook subscribes to a real-time data source using the subscribe function provided, and returns the latest data received and any errors encountered. The hook automatically updates the returned data as new events are received.

#### Parameters

* `key`: A unique key that identifies the data being subscribed to, same key as `useSWR` key.
* `subscribe`: A function that subscribes to the real-time data source. It receives the following arguments:
  * `key`: same key as above
  * `options`: an object with the following properties:
    * `next`: A function that accepts an error and data, and updates the state with the latest data received from the real-time data source.

For instance

```tsx
function subscribe(key, { next }) {
  const sub = remote.subscribe(key, (err, data) => next(err, data))
  return () => sub.close()
}
```

You could also pass a updater function as `data` to `next`, which will receive the previous data as the first argument and return the new data.

```tsx
function subscribe(key, { next }) {
  const sub = remote.subscribe(key, (err, data) => next(err, prev => prev.concat(data)))
  return () => sub.close()
}
```

#### Return Values

* `state`: An object with the following properties:
  * `data`: The latest data received from the real-time data source.
  * `error`: An Error object if an error occurred while subscribing to the real-time data source, otherwise undefined.

When new data is received, the `error` will be reset to `undefined`.

### Usage

Using `useSWRSubscription` to subscribe to a Firestore data source:

```tsx
import useSWRSubscription from 'swr/subscription'

function Post({ id }) {
  const { data } = useSWRSubscription(['views', id], ([_, postId], { next }) => {
    const ref = firebase.database().ref('views/' + postId)
    ref.on('value',
      snapshot => next(null, snapshot.data()),
      err => next(err)
    )
    return () => ref.off()
  })

  return <span>Your post has {data} views!</span>
}
```

Using `useSWRSubscription` to subscribe to a WebSocket data source:

```tsx
import useSWRSubscription from 'swr/subscription'

function App() {
  const { data, error } = useSWRSubscription('ws://...', (key, { next }) => {
    const socket = new WebSocket(key)
    socket.addEventListener('message', (event) => next(null, event.data))
    socket.addEventListener('error', (event) => next(event.error))
    return () => socket.close()
  })
  if (error) return <div>failed to load</div>
  if (!data) return <div>loading...</div>
  return <div>hello {data}!</div>
}
```

You could also check TypeScript examples of `useSWRSubscription` at [this page](/docs/typescript#useswrsubscription)

### Deduplication

`useSWRSubscription` deduplicates the subscription requests with the same key.
If there are multiple components using the same key, they will share the same subscription.
When the last component using the key unmounts, the subscription will be closed.

This means that if you have multiple components using the same key, they will all receive the same data.
And there's only one subscription to the real-time data source per key.

---
title: Suspense
type: guide
summary: Use SWR with React Suspense for declarative data fetching.
prerequisites:

* /docs/getting-started
related:
* /docs/data-fetching

---

# Suspense

You can enable the `suspense` option to use SWR with React [Suspense](https://react.dev/reference/react/Suspense):

```jsx
import { Suspense } from 'react'
import useSWR from 'swr'

function Profile () {
  const { data } = useSWR('/api/user', fetcher, { suspense: true })
  return <div>hello, {data.name}</div>
}

function App () {
  return (
    <Suspense fallback={<div>loading...</div>}>
      <Profile/>
    </Suspense>
  )
}
```

<Callout>
  Note that the `suspense` option is not allowed to change in the lifecycle.
</Callout>

In Suspense mode, `data` is always the fetch response (so you don't need to check if it's `undefined`).
But if an error occurred, you need to use an [error boundary](https://reactjs.org/docs/concurrent-mode-suspense.html#handling-errors) to catch it:

```jsx
<ErrorBoundary fallback={<h2>Could not fetch posts.</h2>}>
  <Suspense fallback={<h1>Loading posts...</h1>}>
    <Profile />
  </Suspense>
</ErrorBoundary>
```

<Callout>
  Suspense mode suspends rendering until the data is ready, which means it causes waterfall problems easily. To avoid that, you should prefetch resources before rendering. [More information](/docs/prefetching)
</Callout>

***

### Note: With Conditional Fetching

Normally, when you enabled `suspense` it's guaranteed that `data` will always be ready on render:

```jsx
function Profile () {
  const { data } = useSWR('/api/user', fetcher, { suspense: true })

  // `data` will never be `undefined`
  // ...
}
```

However, when using it together with conditional fetching or dependent fetching, `data` will be `undefined` if the request is **paused**:

```jsx
function Profile () {
  const { data } = useSWR(isReady ? '/api/user' : null, fetcher, { suspense: true })

  // `data` will be `undefined` if `isReady` is false
  // ...
}
```

If you want to read more technical details about this restriction, check [the discussion here](https://github.com/vercel/swr/pull/357#issuecomment-627089889).

### Server-Side Rendering

When using suspense mode on the server-side (including pre-rendering in Next.js), it's **required** to provide the initial data via [fallbackData or fallback](/docs/with-nextjs#pre-rendering-with-default-data). This means that you can't use `Suspense` to fetch data on the server side, but either doing fully client-side data fetching, or fetch the data via the framework level data fetching method(such as getStaticProps in Next.js). More discussions can be found [here](https://github.com/vercel/swr/issues/1906).

---
title: TypeScript
type: reference
summary: Use SWR with TypeScript for type-safe data fetching.
prerequisites:

* /docs/getting-started
related:
* /docs/api

---

# TypeScript

SWR is friendly for apps written in TypeScript, with type safety out of the box.

## Basic Usage

By default, SWR will also infer the argument types of `fetcher` from `key`, so you can have the preferred types automatically.

### useSWR

```typescript
// `key` is inferred to be `string`
useSWR('/api/user', key => {})
useSWR(() => '/api/user', key => {})

// `key` will be inferred as { a: string; b: { c: string; d: number } }
useSWR({ a: '1', b: { c: '3', d: 2 } }, key => {})
useSWR(() => ({ a: '1', b: { c: '3', d: 2 } }), key => {})

// `arg0` will be inferred as string.  `arg1` will be inferred as number
useSWR(['user', 8], ([arg0, arg1]) => {})
useSWR(() => ['user', 8], ([arg0, arg1]) => {})
```

You can also explicitly specify the types for `key` and `fetcher`'s arguments.

```typescript
import useSWR, { Fetcher } from 'swr'

const uid = '<user_id>'
const fetcher: Fetcher<User, string> = (id) => getUserById(id)

const { data } = useSWR(uid, fetcher)
// `data` will be `User | undefined`.
```

By default, [the error thrown](/docs/error-handling) inside the `fetcher` function has type `any`. The type can also be explicitly specified.

```typescript
const { data, error } = useSWR<User, Error>(uid, fetcher);
// `data` will be `User | undefined`.
// `error` will be `Error | undefined`.
```

### useSWRInfinite

Same for `swr/infinite`, you can either rely on the automatic type inference or explicitly specify the types by yourself.

```typescript
import { SWRInfiniteKeyLoader } from 'swr/infinite'

const getKey: SWRInfiniteKeyLoader = (index, previousPageData) => {
  // ...
}

const { data } = useSWRInfinite(getKey, fetcher)
```

### useSWRSubscription

* Inline subscribe function and manually specify the type of `next` using `SWRSubscriptionOptions`.

```tsx
import useSWRSubscription from 'swr/subscription'
import type { SWRSubscriptionOptions } from 'swr/subscription'

const { data, error } = useSWRSubscription('key', 
  (key, { next }: SWRSubscriptionOptions<number, Error>) => {
  //^ key will be inferred as `string`
  //....
  })
  return {
    data,
    //^ data will be inferred as `number | undefined`
    error
    //^ error will be inferred as `Error | undefined`
  }
}
```

* declare subscribe function using `SWRSubscription`

```tsx
import useSWRSubscription from 'swr/subscription'
import type { SWRSubscription } from 'swr/subscription'

/** 
 * The first generic is Key
 * The second generic is Data
 * The Third generic is Error
 */
const sub: SWRSubscription<string, number, Error> = (key, { next }) => {                         
  //......
}
const { data, error } = useSWRSubscription('key', sub)
```

## Generics

Specifying the type of `data` is easy. By default, it will use the return type of `fetcher` (with `undefined` for the non-ready state) as the `data` type, but you can also pass it as a parameter:

```typescript
// 🔹 A. Use a typed fetcher:
// `getUser` is `(endpoint: string) => User`.
const { data } = useSWR('/api/user', getUser)

// 🔹 B. Specify the data type:
// `fetcher` is generally returning `any`.
const { data } = useSWR<User>('/api/user', fetcher)
```

If you want to add types for other options of SWR, you can also import those types directly:

```typescript
import useSWR from 'swr'
import type { SWRConfiguration } from 'swr'

const config: SWRConfiguration = {
  fallbackData: "fallback",
  revalidateOnMount: false
  // ...
}

const { data } = useSWR<string[]>('/api/data', fetcher, config)
```

## Middleware Types

There're some extra type definitions you can import to help adding types to your custom middleware.

```typescript
import useSWR, { Middleware, SWRHook } from 'swr'

const swrMiddleware: Middleware = (useSWRNext: SWRHook) => (key, fetcher, config) => {
  // ...
  return useSWRNext(key, fetcher, config)
}
```

---
title: Usage with Next.js
type: integration
summary: Integrate SWR with Next.js for server-side rendering and static generation.
prerequisites:

* /docs/getting-started
related:
* /docs/prefetching
* /docs/advanced/cache

---

# Usage with Next.js

## App Router

### Server Components

<Callout type="default" emoji="✅">
  In Next.js App Router, all components are React Server Components (RSC) by default. **You can import SWRConfig and the key serialization APIs from SWR in RSC.**
</Callout>

```tsx filename="app/page.tsx" copy
import { unstable_serialize } from 'swr' // ✅ Available in server components
import { unstable_serialize as infinite_unstable_serialize } from 'swr/infinite' // ✅ Available in server components

import { SWRConfig } from 'swr' // ✅ Available in server components
```

<Callout type="error">
  You could not import hook APIs from SWR since they are not available in RSC.
</Callout>

```tsx filename="app/page.tsx" highlight={1}
import useSWR from 'swr' // ❌ This is not available in server components
import useSWRInfinite from 'swr/infinite' // ❌ This is not available in server components
import usesSWRMutation from 'swr/mutation' // ❌ This is not available in server components
```

### Client Components

You can mark your components with `'use client'` directive or import SWR from client components, both ways will allow you to use the SWR client data fetching hooks.

```tsx filename="app/page.tsx" highlight={1} copy
'use client'

import useSWR from 'swr'

export default function Page() {
  const { data } = useSWR('/api/user', fetcher)
  return <h1>{data.name}</h1>
}
```

### Prefetch Data in Server Components

Similar to the [pre-rendering with default data](#pre-rendering-with-default-data) pattern, with React Server Components (RSC) you can go even further.

You can **initiate** the data prefetching on the server side and pass the **promise** to client component tree via the `<SWRConfig>` provider's `fallback` option:

```tsx filename="app/layout.tsx" copy
import { SWRConfig } from 'swr'

export default async function Layout({ children }: { children: React.ReactNode }) {
  // Initiate the data fetching on the server side.
  const userPromise = fetchUserFromAPI()
  const postsPromise = fetchPostsFromAPI()

  return (
    <SWRConfig
      value={{
        fallback: {
          // Pass the promises to client components.
          '/api/user': userPromise,
          '/api/posts': postsPromise,
        },
      }}
    >
      {children}
    </SWRConfig>
  )
}
```

<Callout emoji="💡">
  The two data fetching function calls `fetchUserFromAPI()` and `fetchPostsFromAPI()` will be executed in parallel on the server side because we don't await them immediately.
</Callout>

In React Server Components, you can pass promises across the `"use client"` boundary, and SWR will resolve them automatically during Server-Side Rendering:

```tsx filename="app/page.tsx" copy
'use client'

import useSWR from 'swr'

export default function Page() {
  // SWR will resolve the promise passed from server components.
  // Both `user` and `posts` are ready during SSR and client hydration.
  const { data: user } = useSWR('/api/user', fetcher)
  const { data: posts } = useSWR('/api/posts', fetcher)

  return (
    <div>
      <h1>{user.name}'s Posts</h1>
      <ul>
        {posts.map(post => (
          <li key={post.id}>{post.title}</li>
        ))}
      </ul>
    </div>
  )
}
```

Then, on the client-side SWR will take over and keep the behavior as usual.

By passing promises from Server Components to Client Components, the data fetching can be initiated as early as possible on the server side. And only the UI boundaries (closest `Suspense` boundary or Next.js layout) that actually consume the data will be blocked during streaming SSR.

<Callout type="default">
  To incrementally adopt this prefetch pattern in your application, you can enable the `strictServerPrefetchWarning` option. This will show a warning message in the console when a key has no pre-filled data provided, helping you identify which data fetching calls could benefit from server-side prefetching.
</Callout>

## Client Side Data Fetching

If your page contains frequently updating data, and you don’t need to pre-render the data, SWR is a perfect fit and no special setup is needed: just import `useSWR` and use the hook inside any components that use the data.

Here’s how it works:

* First, immediately show the page without data. You can show loading states for missing data.
* Then, fetch the data on the client side and display it when ready.

This approach works well for user dashboard pages, for example. Because a dashboard is a private, user-specific page, SEO is not relevant and the page doesn’t need to be pre-rendered. The data is frequently updated, which requires request-time data fetching.

## Pre-rendering with Default Data

If the page must be pre-rendered, Next.js supports [2 forms of pre-rendering](https://nextjs.org/docs/basic-features/data-fetching):
**Static Generation (SSG)** and **Server-side Rendering (SSR)**.

Together with SWR, you can pre-render the page for SEO, and also have features such as caching, revalidation, focus tracking, refetching on interval on the client side.

You can use the `fallback` option of [`SWRConfig`](/docs/global-configuration) to pass the pre-fetched data as the initial value of all SWR hooks.

For example with `getStaticProps`:

```jsx
 export async function getStaticProps () {
  // `getStaticProps` is executed on the server side.
  const article = await getArticleFromAPI()
  return {
    props: {
      fallback: {
        '/api/article': article
      }
    }
  }
}

function Article() {
  // `data` will always be available as it's in `fallback`.
  const { data } = useSWR('/api/article', fetcher)
  return <h1>{data.title}</h1>
}

export default function Page({ fallback }) {
  // SWR hooks inside the `SWRConfig` boundary will use those values.
  return (
    <SWRConfig value={{ fallback }}>
      <Article />
    </SWRConfig>
  )
}
```

The page is still pre-rendered. It's SEO friendly, fast to response, but also fully powered by SWR on the client side. The data can be dynamic and self-updated over time.

<Callout emoji="💡">
  The `Article` component will render the pre-generated data first, and after the page is hydrated, it will fetch the latest data again to keep it fresh.
</Callout>

### Complex Keys

`useSWR` can be used with keys that are `array` and `function` types. Utilizing pre-fetched data with these kinds of keys requires serializing the `fallback` keys with `unstable_serialize`.

```jsx
import useSWR, { unstable_serialize } from 'swr'

export async function getStaticProps () {
  const article = await getArticleFromAPI(1)
  return {
    props: {
      fallback: {
        // unstable_serialize() array style key
        [unstable_serialize(['api', 'article', 1])]: article,
      }
    }
  }
}

function Article() {
  // using an array style key.
  const { data } = useSWR(['api', 'article', 1], fetcher)
  return <h1>{data.title}</h1>
}

export default function Page({ fallback }) {
  return (
    <SWRConfig value={{ fallback }}>
      <Article />
    </SWRConfig>
  )
}
```

---
title: Cache
type: conceptual
summary: Customize the cache provider and implement advanced caching strategies.
prerequisites:

* /docs/global-configuration
related:
* /docs/global-configuration

---

# Cache

<Callout>
  Upgrade to the latest version (≥ 1.0.0) to use this feature.
</Callout>

<Callout emoji="⚠️">
  In most cases, you shouldn't directly *write* to the cache, which might cause undefined behaviors of SWR. If you need to manually mutate a key, please consider using the SWR APIs.<br />
  See also: [Mutation](/docs/mutation), [Reset Cache Between Test Cases](#reset-cache-between-test-cases).
</Callout>

By default, SWR uses a global cache to store and share data across all components. But you can also customize this behavior with the `provider` option of `SWRConfig`.

Cache providers are intended to enable SWR with more customized storages.

## Cache Provider

A cache provider is Map-like object which matches the following TypeScript definition (which can be imported from `swr`):

```typescript
interface Cache<Data> {
  get(key: string): Data | undefined
  set(key: string, value: Data): void
  delete(key: string): void
  keys(): IterableIterator<string>
}
```

For example, a [JavaScript Map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Map) instance can be directly used as the cache provider for SWR.

## Create Cache Provider

The `provider` option of `SWRConfig` receives a function that returns a [cache provider](#cache-provider). The provider will then be used by all SWR hooks inside that `SWRConfig` boundary. For example:

```jsx
import useSWR, { SWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig value={{ provider: () => new Map() }}>
      <Page/>
    </SWRConfig>
  )
}
```

All SWR hooks inside `<Page/>` will read and write from that Map instance. You can also use other cache provider implementations as well for your specific use case.

<Callout>
  In the example above, when the `<App/>` component is re-mounted, the provider will also be re-created. Cache providers should be put higher in the component tree, or outside of render.
</Callout>

<div className="my-8">
  <Cache />
</div>

When nested, SWR hooks will use the upper-level cache provider. If there is no upper-level cache provider, it fallbacks to the default cache provider, which is an empty `Map`.

<Callout emoji="⚠️">
  If a cache provider is used, the global `mutate` will **not** work for SWR hooks under that `<SWRConfig>` boundary. Please use [this](#access-current-cache-provider) instead.
</Callout>

## Access Current Cache Provider

When inside a React component, you need to use the [`useSWRConfig`](/docs/global-configuration#access-to-global-configurations) hook to get access to the current cache provider as well as other configurations including `mutate`:

```jsx
import { useSWRConfig } from 'swr'

function Avatar() {
  const { cache, mutate, ...extraConfig } = useSWRConfig()
  // ...
}
```

If it's not under any `<SWRConfig>`, it will return the default configurations.

## Experimental: Extend Cache Provider

<Callout emoji="🧪">
  This is an experimental feature, the behavior might change in future upgrades.
</Callout>

When multiple `<SWRConfig>` components are nested, cache provider can be extended.

The first argument for the `provider` function is the cache provider of the upper-level `<SWRConfig>` (or the default cache if there's no parent `<SWRConfig>`), you can use it to extend the cache provider:

```jsx
<SWRConfig value={{ provider: (cache) => newCache }}>
  ...
</SWRConfig>
```

## Examples

### LocalStorage Based Persistent Cache

You might want to sync your cache to `localStorage`. Here's an example implementation:

```jsx
function localStorageProvider() {
  // When initializing, we restore the data from `localStorage` into a map.
  const map = new Map(JSON.parse(localStorage.getItem('app-cache') || '[]'))

  // Before unloading the app, we write back all the data into `localStorage`.
  window.addEventListener('beforeunload', () => {
    const appCache = JSON.stringify(Array.from(map.entries()))
    localStorage.setItem('app-cache', appCache)
  })

  // We still use the map for write & read for performance.
  return map
}
```

Then use it as a provider:

```jsx
<SWRConfig value={{ provider: localStorageProvider }}>
  <App/>
</SWRConfig>
```

<Callout>
  As an improvement, you can also use the memory cache as a buffer, and write to `localStorage` periodically. You can also implement a similar layered cache with IndexedDB or WebSQL.
</Callout>

### Reset Cache Between Test Cases

When testing your application, you might want to reset the SWR cache between test cases. You can simply wrap your application with an empty cache provider. Here's an example with Jest:

```jsx
describe('test suite', async () => {
  it('test case', async () => {
    render(
      <SWRConfig value={{ provider: () => new Map() }}>
        <App/>
      </SWRConfig>
    )
  })
})
```

### Modify the Cache Data

<Callout emoji="🚨" type="error">
  You should not write to the cache directly, it might cause undefined behavior.
</Callout>

You can use [`mutate`](/docs/mutation) to modify the cache. For example, you can clear all cache data like the following.

```jsx
const { mutate } = useSWRConfig()

mutate(
  key => true, // which cache keys are updated
  undefined, // update cache data to `undefined`
  { revalidate: false } // do not revalidate
)
```

More information can be found [here](/docs/arguments#multiple-arguments).

---
title: DevTools
type: guide
summary: Debug SWR with developer tools.
prerequisites:

* /docs/getting-started
related:
* /docs/advanced/cache

---

# DevTools

<Callout>
  SWRDevTools is not an official project of Vercel.
</Callout>

[SWRDevTools](https://swr-devtools.vercel.app/) is a developer tool for SWR, which helps to debug your SWR cache and fetchers.

You can install SWR DevTools from the extension pages and use it with zero settings!

* Chrome: [https://chrome.google.com/webstore/detail/swr-devtools/liidbicegefhheghhjbomajjaehnjned](https://chrome.google.com/webstore/detail/swr-devtools/liidbicegefhheghhjbomajjaehnjned)
* Firefox: [https://addons.mozilla.org/en-US/firefox/addon/swr-devtools/](https://addons.mozilla.org/en-US/firefox/addon/swr-devtools/)

After installing it, the SWR devtool panel will appear on browsers' developer tools.

Checkout more information on the [website](https://swr-devtools.vercel.app/) and the [repository](https://github.com/koba04/swr-devtools)

---
title: Performance
type: conceptual
summary: Optimize performance with deduplication, deep comparison, and dependency tracking.
prerequisites:

* /docs/getting-started
related:
* /docs/data-fetching
* /docs/advanced/cache

---

# Performance

SWR provides critical functionality in all kinds of web apps, so **performance** is a top priority.

SWR’s built-in **caching** and **[deduplication](#deduplication)** skips unnecessary network requests, but
the performance of the `useSWR` hook itself still matters. In a complex app, there could be hundreds of `useSWR` calls in a single page render.

SWR ensures that your app has:

* *no unnecessary requests*
* *no unnecessary re-renders*
* *no unnecessary code imported*

without any code changes from you.

## Deduplication

It’s very common to reuse SWR hooks in your app. For example, an app that renders the current user’s avatar 5 times:

```jsx
function useUser () {
  return useSWR('/api/user', fetcher)
}

function Avatar () {
  const { data, error } = useUser()

  if (error) return <Error />
  if (!data) return <Spinner />

  return <img src={data.avatar_url} />
}

function App () {
  return <>
    <Avatar />
    <Avatar />
    <Avatar />
    <Avatar />
    <Avatar />
  </>
}
```

Each `<Avatar>` component has a `useSWR` hook inside. Since they have the same SWR key and are rendered almost at the same time, **only 1 network request will be made**.

You can reuse your data hooks (like `useUser` in the example above) everywhere, without worrying about performance or duplicated requests.

There is also a [`dedupingInterval` option](/docs/api) for overriding the default deduplication interval.

## Deep Comparison

SWR **deep compares** data changes by default. If the `data` value isn’t changed, a re-render will not be triggered.

You can also customize the comparison function via the [`compare` option](/docs/api) if you want to change the behavior.
For example, some API responses return a server timestamp that you might want to exclude from the data diff.

## Dependency Collection

`useSWR` returns 4 **stateful** values: `data`, `error`, `isLoading` and `isValidating`, each one can be updated independently.
For example, if we print those values within a full data-fetching lifecycle, it will be something like this:

```jsx
function App () {
  const { data, error, isLoading, isValidating } = useSWR('/api', fetcher)
  console.log(data, error, isLoading, isValidating)
  return null
}
```

In the worst case (the first request failed, then the retry was successful), you will see 4 lines of logs:

```js
// console.log(data, error, isLoading, isValidating)
undefined undefined true true  // => start fetching
undefined Error false false    // => end fetching, got an error
undefined Error true true      // => start retrying
Data undefined false false     // => end retrying, get the data
```

The state changes make sense. But that also means our component **rendered 4 times**.

If we change our component to only use `data`:

```jsx
function App () {
  const { data } = useSWR('/api', fetcher)
  console.log(data)
  return null
}
```

The magic happens — there are only **2 re-renders** now:

```js
// console.log(data)
undefined // => hydration / initial render
Data      // => end retrying, get the data
```

The exact same process has happened internally, there was an error from the first request, then we got the data from the retry.
However, **SWR only updates the states that are used by the component**, which is only `data` now.

If you are not always using all these 3 states, you are already benefitting from this feature.
At [Vercel](https://vercel.com), this optimization results in \~60% fewer re-renders.

## Tree Shaking

The SWR package is [tree-shakeable](https://webpack.js.org/guides/tree-shaking) and side-effect free.
That means if you are only importing the core `useSWR` API, unused APIs like `useSWRInfinite` won't be bundled in your application.

---
title: React Native
type: integration
summary: Use SWR with React Native applications.
prerequisites:

* /docs/getting-started
related:
* /docs/getting-started

---

# React Native

<Callout>
  Upgrade to the latest version (≥ 1.0.0) to experience this customization.
</Callout>

Unlike React running inside the browsers, React Native has a very different user experience. For example there is no “tab focus”, switching from the background to the app is considered as a “focus” instead.
To customize these behaviors, you can replace the default browser `focus` and `online` events listeners with React Native’s app state detection and other native ported API, and configure SWR to use them.

## Example

### Global Setup

You can wrap your app under `SWRConfig` and preconfig all configurations there

```jsx
<SWRConfig
  value={{
    /* ... */
  }}
>
  <App>
</SWRConfig>
```

### Customize `focus` and `reconnect` Events

There're few configurations you need to take care of such as `isOnline`, `isVisible`, `initFocus` and `initReconnect`.

`isOnline` and `isVisible` are functions that return a boolean, to determine if the application is "active". By default, SWR will bail out a revalidation if these conditions are not met.

When using `initFocus` and `initReconnect`, it's required to also set up a [custom cache provider](/docs/advanced/cache). You can use an empty `Map()` or any storage you prefer.

```jsx
<SWRConfig
  value={{
    provider: () => new Map(),
    isOnline() {
      /* Customize the network state detector */
      return true
    },
    isVisible() {
      /* Customize the visibility state detector */
      return true
    },
    initFocus(callback) {
      /* Register the listener with your state provider */
    },
    initReconnect(callback) {
      /* Register the listener with your state provider */
    }
  }}
>
  <App />
</SWRConfig>
```

Let's take `initFocus` as example:

```jsx
import { AppState } from 'react-native'

// ...

<SWRConfig
  value={{
    provider: () => new Map(),
    isVisible: () => { return true },
    initFocus(callback) {
      let appState = AppState.currentState

      const onAppStateChange = (nextAppState) => {
        /* If it's resuming from background or inactive mode to active one */
        if (appState.match(/inactive|background/) && nextAppState === 'active') {
          callback()
        }
        appState = nextAppState
      }

      // Subscribe to the app state change events
      const subscription = AppState.addEventListener('change', onAppStateChange)

      return () => {
        subscription.remove()
      }
    }
  }}
>
  <App>
</SWRConfig>
```

For `initReconnect`, it requires some 3rd party libraries such as [NetInfo](https://github.com/react-native-netinfo/react-native-netinfo) to subscribe to the network status. The implementation will be similar to the example above: receiving a `callback` function and trigger it when the network recovers from offline, so SWR can start a revalidation to keep your data up-to-date.

---
title: Understanding SWR
type: conceptual
summary: Understand how SWR works internally.
prerequisites:

* /docs/getting-started
related:
* /docs/advanced/cache
* /docs/advanced/performance

---

# Understanding SWR

## State Machine

`useSWR` returns `data`, `error`, `isLoading`, and `isValidating` depending on the state of the `fetcher` function. This diagrams describe how SWR returns values in some scenarios.

### Fetch and Revalidate

This pattern is to fetch data and revalidate it later.

<img alt="A pattern for fetch and revalidate" src={__img0} />

### Key Change

This pattern is to fetch data and change the key and revalidate it later.

<img alt="A pattern for key change" src={__img1} />

### Key Change + Previous Data

This pattern is to fetch data and change the key and revalidate it later with the `keepPreviousData` option.

<img alt="A pattern for key change + previous data" src={__img2} />

### Fallback

This pattern is to fetch data and revalidate it later with fallback data.

<img alt="A pattern for fallback" src={__img3} />

### Key Change + Fallback

This pattern is to fetch data and change the key and revalidate it later with fallback data.

<img alt="A pattern for key change + fallback" src={__img4} />

### Key Change + Previous Data + Fallback

This pattern is to fetch data and change the key and revalidate it later with the `keepPreviousData` option and fallback data.

<img alt="A pattern for key change + previous data + fallback" src={__img5} />

## Combining with isLoading and isValidating for better UX

Comparing to the existing `isValidating` value, `isLoading` is a new property that can help you for the more general loading cases for UX.

* `isValidating` becomes `true` whenever there is an ongoing request **whether the data is loaded or not**
* `isLoading` becomes `true` when there is an ongoing request and **data is not loaded yet**.

Simply saying you can use `isValidating` for indicating everytime there is an ongoing revalidation, and `isLoading` for indicating that SWR is revalidating but there is no data yet to display.

<Callout emoji="📝">
  Fallback data and previous data are not considered "loaded data," so when you use fallback data or enable the keepPreviousData option, you might have data to display.
</Callout>

```jsx
function Stock() {
  const { data, isLoading, isValidating } = useSWR(STOCK_API, fetcher, {
    refreshInterval: 3000
  });

  // If it's still loading the initial data, there is nothing to display.
  // We return a skeleton here.
  if (isLoading) return <div className="skeleton" />;

  // Otherwise, display the data and a spinner that indicates a background
  // revalidation.
  return (
    <>
      <div>${data}</div>
      {isValidating ? <div className="spinner" /> : null}
    </>
  );
}
```

<img alt="An example of using the isLoading state" src={__img6} />

You can find the code example [here](https://codesandbox.io/s/swr-isloading-jtopow)

## Return previous data for better UX

When doing data fetching based on continuous user actions, e.g. real-time search when typing, keeping the previous fetched data can improve the UX a lot. `keepPreviousData` is an option to enable that behavior. Here's a simple search UI:

```jsx
function Search() {
  const [search, setSearch] = React.useState('');

  const { data, isLoading } = useSWR(`/search?q=${search}`, fetcher, {
    keepPreviousData: true
  });

  return (
    <div>
      <input
        type="text"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        placeholder="Search..."
      />

      <div className={isLoading ? "loading" : ""}>
        {data?.products.map(item => <Product key={item.id} name={item.name} />)
      </div>
    </div>
  );
}
```

With `keepPreviousData` enabled, you will still get the previous data even if you change the SWR key and the data for the new key starts loading again.

<Video src="https://user-images.githubusercontent.com/3676859/163695903-a3eb1259-180e-41e0-821e-21c320201194.mp4" caption="Keep previous search results when keepPreviousData has been enabled" ratio={640/730} />

You can find the full code for this example here: [https://codesandbox.io/s/swr-keeppreviousdata-fsjz3m](https://codesandbox.io/s/swr-keeppreviousdata-fsjz3m).

## Dependency Collection for performance

SWR only triggers re-rendering when the states used in the component have been updated. If you only use `data` in the component, SWR ignores the updates of other properties like `isValidating`, and `isLoading`. This reduces rendering counts a lot. More information can be found [here](/docs/advanced/performance#dependency-collection).
