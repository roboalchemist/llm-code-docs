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
  - /docs/getting-started
related:
  - /docs/data-fetching
  - /docs/conditional-fetching
---

# Arguments



By default, `key` will be passed to `fetcher` as the argument. So the following 3 expressions are equivalent:

```js
useSWR('/api/user', () => fetcher('/api/user'))
useSWR('/api/user', url => fetcher(url))
useSWR('/api/user', fetcher)
```

## Multiple Arguments

Sometimes it's useful to pass multiple arguments to the `fetcher` function. For example, an authorized fetch request:

```js
const { data: user, error, isLoading } = useSWR(
  ['/api/user', token],
  ([url, token]) => fetchWithToken(url, token)
)
```

The `key` will be passed to `fetcher` function, and the return value of `fetcher` is the `data`.

## Passing Objects

<Callout emoji="⚠️">
  In older versions (< 2.0.0), SWR compared arguments shallowly, which could cause unnecessary re-renders. This has been fixed since v2.0.0.
</Callout>

When using objects as arguments, you must normalize them so that they're always in the same format. This will help SWR to cache results properly:

```js
// Avoid
useSWR(['/api/user', { id: user.id }], ([url, config]) => fetchWithConfig(url, config))

// Good
useSWR(['/api/user', user.id], (url, id) => fetchWithConfig(url, { id }))
```

---
title: Data Fetching
type: reference
summary: Guide to writing fetcher functions for SWR.
prerequisites:
  - /docs/getting-started
related:
  - /docs/arguments
  - /docs/error-handling
---

# Data Fetching



SWR is agnostic to how you fetch data. You can use anything you want, as long as the `fetcher` returns a Promise. Here are some examples:

```js
// Using native fetch
const fetcher = url => fetch(url).then(r => r.json())

const { data } = useSWR('/api/data', fetcher)
```

```js
// Using axios
import axios from 'axios'

const fetcher = url => axios.get(url).then(r => r.data)

const { data } = useSWR('/api/data', fetcher)
```

```js
// Using GraphQL
const fetcher = query => fetch('https://api.example.com/graphql', {
  method: 'POST',
  headers: { 'Content-type': 'application/json' },
  body: JSON.stringify({ query })
}).then(res => res.json())
```

### With TypeScript

You can type the `fetcher` function and its arguments:

```ts
import type { ReactNode } from 'react'
import useSWR, { SWRConfiguration } from 'swr'

interface User {
  name: string
  email: string
}

const fetcher = (url: string) => fetch(url).then(r => r.json() as Promise<User>)

const { data } = useSWR<User>('/api/user', fetcher)
// `data` is `User | undefined`
```

---
title: Error Handling
type: reference
summary: Handling errors in SWR data fetching.
prerequisites:
  - /docs/getting-started
related:
  - /docs/data-fetching
  - /docs/mutation
---

# Error Handling

The `error` object will be defined if the fetcher throws an error (or returns a promise that rejects).

```js
const { data, error } = useSWR('/api/user', fetcher)
```

## Status Code and Error Object

Sometimes we want the `error` object to contain the status code as well. You can create a custom `fetcher` that does this:

```js
const fetcher = async (url) => {
  const res = await fetch(url)

  // If the status code is not in the range 200-299,
  // we still try to parse and throw it.
  if (!res.ok) {
    const error = new Error('An error occurred while fetching the resource.')
    error.status = res.status
    throw error
  }

  return res.json()
}

const { data, error } = useSWR('/api/user', fetcher)
```

## Error Retry

By default, SWR will use the `onErrorRetry` handler to retry on errors. You can override this behavior:

```js
const { data, error } = useSWR(
  '/api/user',
  fetcher,
  {
    onErrorRetry: (error, key, config, revalidate, revalidateOps) => {
      // Never retry on 404.
      if (error.status === 404) {
        return
      }

      // Never retry for a specific key.
      if (key === '/api/user/secret') {
        return
      }

      // Only retry up to 10 times.
      if (revalidateOps.retryCount >= 10) {
        return
      }

      // Retry after 5 seconds.
      setTimeout(() => revalidate(revalidateOps), 5000)
    }
  }
)
```

---
title: Revalidation
type: reference
summary: How SWR revalidates data.
prerequisites:
  - /docs/getting-started
related:
  - /docs/global-configuration
  - /docs/mutation
---

# Revalidation

## Manual Revalidation

You can manually trigger revalidation by calling the `mutate(undefined, { revalidate: true })`:

```js
const { data, mutate } = useSWR('/api/user', fetcher)

// manually trigger a revalidation
mutate()
```

## Revalidate on Focus

When you refocus a web page, SWR will automatically revalidate the data. This is useful to sync your latest data immediately when your user returns to the application.

You can disable this behavior with `revalidateOnFocus: false`:

```js
useSWR('/api/data', fetcher, {
  revalidateOnFocus: false
})
```

## Revalidate on Reconnect

SWR will automatically revalidate when your browser regains a network connection. This is useful when a user's device goes offline and then comes back online.

You can disable this behavior with `revalidateOnReconnect: false`:

```js
useSWR('/api/data', fetcher, {
  revalidateOnReconnect: false
})
```

## Revalidate on Mount

By default, SWR does not revalidate on mount (when the component is first mounted). You can enable this behavior with `revalidateOnMount: true`:

```js
useSWR('/api/data', fetcher, {
  revalidateOnMount: true
})
```

## Disable Automatic Revalidations

You can disable all automatic revalidations by setting `revalidateIfStale` to `false`:

```js
useSWR('/api/data', fetcher, {
  revalidateIfStale: false,
  revalidateOnFocus: false,
  revalidateOnReconnect: false
})
```

## Polling

To enable polling, you can set `refreshInterval` to a number in milliseconds:

```js
useSWR('/api/data', fetcher, {
  refreshInterval: 1000
})
```

You can also pass a function to `refreshInterval` to compute the interval dynamically:

```js
useSWR('/api/data', fetcher, {
  refreshInterval: (latestData) => {
    // Increase interval if there's an error
    if (latestData?.error) return 5000
    return 1000
  }
})
```

## Refresh When Hidden

By default, SWR will not revalidate when the window is hidden. You can enable this behavior with `refreshWhenHidden: true`:

```js
useSWR('/api/data', fetcher, {
  refreshWhenHidden: true
})
```

## Refresh When Offline

By default, SWR will not revalidate when the browser is offline. You can enable this behavior with `refreshWhenOffline: true`:

```js
useSWR('/api/data', fetcher, {
  refreshWhenOffline: true
})
```

---
title: Mutation
type: reference
summary: Mutate and update cached data in SWR.
prerequisites:
  - /docs/getting-started
related:
  - /docs/revalidation
  - /docs/global-configuration
---

# Mutation

## Mutate

The `mutate` function allows you to update the cache data without triggering a revalidation. It's useful for optimistically updating the UI.

```js
const { data, mutate } = useSWR('/api/user', fetcher)

// Update the data
mutate({ ...data, name: 'New Name' })
```

## Mutate with Options

You can pass options to `mutate` to control how it behaves:

```js
const { mutate } = useSWR('/api/user', fetcher)

// Revalidate after mutation
mutate(newData, { revalidate: true })

// Populate only
mutate(newData, { populateCache: false })

// Trigger callbacks
mutate(newData, { rollbackOnError: true })
```

### Revalidate

Set `revalidate: true` to revalidate the data after mutation:

```js
mutate(newData, { revalidate: true })
```

### Rollback on Error

Set `rollbackOnError: true` to rollback on error:

```js
mutate(newData, { rollbackOnError: true })
```

This will revert the cache to the previous value if the revalidation fails.

### Populate Cache

Set `populateCache: false` to skip populating the cache:

```js
mutate(newData, { populateCache: false })
```

## Global Mutate

You can also use `mutate` from `swr` to mutate any cache by key:

```js
import { mutate } from 'swr'

// Mutate a specific key
mutate('/api/user')

// Mutate by a pattern
mutate(key => key.startsWith('/api/'))
```

## Mutate Multiple Keys

You can mutate multiple keys by using a filter function:

```js
import { mutate } from 'swr'

mutate(
  key => typeof key === 'string' && key.startsWith('/api/user'),
  undefined,
  { revalidate: true }
)
```

---
title: Conditional Fetching
type: reference
summary: Conditionally enable or disable SWR fetching.
prerequisites:
  - /docs/getting-started
related:
  - /docs/arguments
  - /docs/data-fetching
---

# Conditional Fetching

## Conditional Request

Use `null` or return the key from a function as a dependency to conditionally enable or disable a request:

```js
// conditionally fetch
const { data } = useSWR(shouldFetch ? '/api/data' : null, fetcher)
```

When the condition changes, SWR will re-evaluate the key and re-fetch accordingly.

```js
function User() {
  const [id, setId] = useState(null)

  // The fetching will not start until `id` changes
  const { data: user } = useSWR(id ? `/api/user/${id}` : null, fetcher)

  return (
    <>
      <input
        type="number"
        value={id}
        onChange={(e) => setId(e.target.value)}
      />
      {user && <h1>{user.name}</h1>}
    </>
  )
}
```

### Dependent Fetching

Sometimes you want to fetch data that depends on other data. SWR makes it easy to do conditional fetching:

```js
function MyComponent() {
  const { data: user } = useSWR('/api/user')
  // Pass null as key to skip fetching
  const { data: settings } = useSWR(user ? `/api/user/${user.id}/settings` : null, fetcher)

  return (
    <>
      {!user ? 'loading user...' : (
        <>
          <h1>{user.name}</h1>
          {!settings ? 'loading settings...' : <div>{settings}</div>}
        </>
      )}
    </>
  )
}
```

---
title: Suspense
type: reference
summary: Using React Suspense with SWR.
prerequisites:
  - /docs/getting-started
related:
  - /docs/global-configuration
  - /docs/error-boundaries
---

# Suspense

You can enable Suspense mode by setting the `suspense: true` option:

```js
import { Suspense } from 'react'
import useSWR from 'swr'

function Profile() {
  const { data } = useSWR('/api/user', fetcher, { suspense: true })
  return <h1>{data.name}</h1>
}

export default function App() {
  return (
    <Suspense fallback={<div>loading...</div>}>
      <Profile />
    </Suspense>
  )
}
```

In Suspense mode, `data` is always defined. If the request is still loading, `useSWR` will throw a Promise, and the Suspense boundary will catch it.

```js
const { data, error } = useSWR('/api/user', fetcher, { suspense: true })
```

## Error Boundaries with Suspense

When using Suspense with SWR, errors thrown by the fetcher will be caught by an error boundary:

```js
import { Suspense } from 'react'
import useSWR from 'swr'

class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props)
    this.state = { hasError: false }
  }

  static getDerivedStateFromError(error) {
    return { hasError: true }
  }

  render() {
    if (this.state.hasError) {
      return <div>An error occurred</div>
    }

    return this.props.children
  }
}

function Profile() {
  const { data } = useSWR('/api/user', fetcher, { suspense: true })
  return <h1>{data.name}</h1>
}

export default function App() {
  return (
    <ErrorBoundary>
      <Suspense fallback={<div>loading...</div>}>
        <Profile />
      </Suspense>
    </ErrorBoundary>
  )
}
```

---
title: Middleware
type: reference
summary: SWR middleware for custom behavior.
prerequisites:
  - /docs/getting-started
related:
  - /docs/advanced/understanding
---

# Middleware

Middleware is an experimental feature. Use at your own risk.

Middleware allow you to inject custom logic into SWR's hook. You can access the hook's life cycle and manipulate the returned state.

## Creating Middleware

A middleware is a function that takes `useSWRNext` and returns a new hook:

```js
function myMiddleware(useSWRNext) {
  return (key, fetcher, config) => {
    // Before hook runs...

    // Handle the next hook
    const swr = useSWRNext(key, fetcher, config)

    // After hook runs...
    return swr
  }
}
```

You can apply middleware by passing it in the `use` option:

```js
useSWR(key, fetcher, { use: [myMiddleware] })
```

## Examples

### Logging

```js
function logMiddleware(useSWRNext) {
  return (key, fetcher, config) => {
    const swr = useSWRNext(key, fetcher, config)

    useEffect(() => {
      if (swr.data) console.log(key, swr.data)
    }, [swr.data])

    return swr
  }
}
```

### Request Retrying

```js
function retryMiddleware(useSWRNext) {
  return (key, fetcher, config) => {
    const swr = useSWRNext(key, fetcher, config)

    return useMemo(
      () => ({
        ...swr,
        mutate: async (...args) => {
          for (let i = 0; i < 3; i++) {
            try {
              return await swr.mutate(...args)
            } catch {
              // retry
            }
          }
        }
      }),
      [swr]
    )
  }
}
```

## Global Configuration

You can also apply middleware globally using `SWRConfig`:

```js
import { SWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig
      value={{
        use: [myMiddleware]
      }}
    >
      <Component />
    </SWRConfig>
  )
}
```

---
title: Global Configuration
type: reference
summary: Configure SWR globally across your application.
prerequisites:
  - /docs/getting-started
related:
  - /docs/api
  - /docs/advanced/understanding
---

# Global Configuration

The `SWRConfig` context can provide global configuration for all SWR hooks. When a configuration item is not found in the hook options, the global configuration will be used.

## SWRConfig Provider

Wrap your component tree with `SWRConfig` to provide global configuration:

```js
import { SWRConfig } from 'swr'

function App() {
  return (
    <SWRConfig
      value={{
        dedupingInterval: 0,
        focusThrottleInterval: 0,
      }}
    >
      <MyComponent />
    </SWRConfig>
  )
}
```

All options listed in the [API](/docs/api) can be used as global configuration values.

## Multiple Providers

You can nest multiple `SWRConfig` providers:

```js
<SWRConfig value={{ dedupingInterval: 0 }}>
  <SWRConfig value={{ focusThrottleInterval: 0 }}>
    <Component />
  </SWRConfig>
</SWRConfig>
```

## Merging Configurations

Configurations are merged shallowly, so you can mix global and local options:

```js
const globalConfig = {
  dedupingInterval: 0,
  focusThrottleInterval: 0,
}

const localConfig = {
  revalidateOnFocus: false,
}

useSWR('/api/data', fetcher, {
  ...globalConfig,
  ...localConfig,
})
```

---
title: TypeScript
type: reference
summary: TypeScript support in SWR.
prerequisites:
  - /docs/getting-started
related:
  - /docs/api
---

# TypeScript

## Basic Usage

SWR is very TypeScript-friendly. You can type your data by passing a generic to `useSWR`:

```ts
const { data, error } = useSWR<string>('/api/hello', fetcher)
// `data` is `string | undefined`
```

## Typing the Fetcher

You can type the fetcher function to ensure it returns the correct type:

```ts
import type { Fetcher } from 'swr'

const fetcher: Fetcher<string, string> = url => fetch(url).then(r => r.json())

const { data } = useSWR<string>(url, fetcher)
```

## Typing Multiple Arguments

When you pass multiple arguments to your fetcher, you can type them:

```ts
const fetcher = ([url, token]: [string, string]) => 
  fetch(url, { headers: { Authorization: `Bearer ${token}` } })
    .then(r => r.json())

const { data } = useSWR<Data>(
  ['/api/user', token],
  fetcher
)
```

## Error Type

You can also type the error object:

```ts
interface Error {
  status: number
  message: string
}

const { data, error } = useSWR<Data, Error>('/api/user', fetcher)
```

---
title: Advanced - Understanding
type: reference
summary: Advanced concepts in SWR.
prerequisites:
  - /docs/getting-started
related:
  - /docs/advanced/performance
---

# Advanced - Understanding

## Return Previous Data for Better UX

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

## Dependency Collection for performance

SWR only triggers re-rendering when the states used in the component have been updated. If you only use `data` in the component, SWR ignores the updates of other properties like `isValidating`, and `isLoading`. This reduces rendering counts a lot. More information can be found [here](/docs/advanced/performance#dependency-collection).
