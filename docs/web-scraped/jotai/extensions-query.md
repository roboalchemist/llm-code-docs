# Source: https://jotai.org/docs/extensions/query

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Query 

[TanStack Query](https://tanstack.com/query/) provides a set of functions for managing async state (typically external data).

From the [Overview docs](https://tanstack.com/query/v5/docs/framework/react/overview):

> React Query is often described as the missing data-fetching library for React, but in more technical terms, it makes **fetching, caching, synchronizing and updating server state** in your React applications a breeze.

[jotai-tanstack-query](https://github.com/jotai-labs/jotai-tanstack-query) is a Jotai extension library for TanStack Query. It provides a wonderful interface with all of the TanStack Query features, providing you the ability to use those features in combination with your existing Jotai state.

### [Support](#support)

jotai-tanstack-query currently supports TanStack Query v5.

### [Install](#install)

In addition to `jotai`, you have to install `jotai-tanstack-query` and `@tanstack/query-core` to use the extension.

    npm install jotai-tanstack-query @tanstack/query-core

### [Incremental Adoption](#incremental-adoption)

You can incrementally adopt `jotai-tanstack-query` in your app. It\'s not an all or nothing solution. You just have to ensure you are using the same QueryClient instance. [QueryClient Setup](#referencing-the-same-instance-of-query-client-in-your-project).

    // existing useQueryHookconst  = useQuery()
    // jotai-tanstack-queryconst todosAtom = atomWithQuery(() => ())
    const [] = useAtom(todosAtom)

### [Exported functions](#exported-functions)

-   `atomWithQuery` for [useQuery](https://tanstack.com/query/v5/docs/react/reference/useQuery)
-   `atomWithInfiniteQuery` for [useInfiniteQuery](https://tanstack.com/query/v5/docs/react/reference/useInfiniteQuery)
-   `atomWithMutation` for [useMutation](https://tanstack.com/query/v5/docs/react/reference/useMutation)
-   `atomWithSuspenseQuery` for [useSuspenseQuery](https://tanstack.com/query/v5/docs/react/reference/useSuspenseQuery)
-   `atomWithSuspenseInfiniteQuery` for [useSuspenseInfiniteQuery](https://tanstack.com/query/v5/docs/react/reference/useSuspenseInfiniteQuery)
-   `atomWithMutationState` for [useMutationState](https://tanstack.com/query/v5/docs/react/reference/useMutationState)

All functions follow the same signature.

    const dataAtom = atomWithSomething(getOptions, getQueryClient)

The first `getOptions` parameter is a function that returns an input to the observer. The second optional `getQueryClient` parameter is a function that return [QueryClient](https://tanstack.com/query/v5/docs/reference/QueryClient).

### [atomWithQuery usage](#atomwithquery-usage)

`atomWithQuery` creates a new atom that implements a standard [`Query`](https://tanstack.com/query/v5/docs/react/guides/queries) from TanStack Query.

    import  from 'jotai'import  from 'jotai-tanstack-query'
    const idAtom = atom(1)const userAtom = atomWithQuery((get) => () => `)    return res.json()  },}))
    const UserData = () => ] = useAtom(userAtom)
      if (isPending) return <div>Loading...</div>  if (isError) return <div>Error</div>
      return <div></div>}

### [atomWithInfiniteQuery usage](#atomwithinfinitequery-usage)

`atomWithInfiniteQuery` is very similar to `atomWithQuery`, however it is for an `InfiniteQuery`, which is used for data that is meant to be paginated. You can [read more about Infinite Queries here](https://tanstack.com/query/v5/docs/framework/react/guides/infinite-queries).

> Rendering lists that can additively \"load more\" data onto an existing set of data or \"infinite scroll\" is also a very common UI pattern. React Query supports a useful version of useQuery called useInfiniteQuery for querying these types of lists.

A notable difference between a standard query atom is the additional option `getNextPageParam` and `getPreviousPageParam`, which is what you\'ll use to instruct the query on how to fetch any additional pages.

    import  from 'jotai'import  from 'jotai-tanstack-query'
    const postsAtom = atomWithInfiniteQuery(() => () => `)    return res.json()  },  getNextPageParam: (lastPage, allPages, lastPageParam) => lastPageParam + 1,  initialPageParam: 1,}))
    const Posts = () => ] =    useAtom(postsAtom)
      if (isPending) return <div>Loading...</div>  if (isError) return <div>Error</div>
      return (    <>      >          ></div>          ))}        </div>      ))}      <button onClick=>Next</button>    </>  )}

### [atomWithMutation usage](#atomwithmutation-usage)

`atomWithMutation` creates a new atom that implements a standard [`Mutation`](https://tanstack.com/query/v5/docs/framework/react/guides/mutations) from TanStack Query.

> Unlike queries, mutations are typically used to create/update/delete data or perform server side-effects.

    const postAtom = atomWithMutation(() => (: ) => ),      headers: ,    })    const data = await res.json()    return data  },}))
    const Posts = () => ] = useAtom(postAtom)  return (    <div>      <button onClick=)}>Click me</button>      <pre></pre>    </div>  )}

### [atomWithMutationState usage](#atomwithmutationstate-usage)

`atomWithMutationState` creates a new atom that gives you access to all mutations in the [`MutationCache`](https://tanstack.com/query/v5/docs/react/reference/useMutationState).

    const mutationStateAtom = atomWithMutationState((get) => (,}))

### [Suspense](#suspense)

jotai-tanstack-query can also be used with React\'s Suspense.

### [atomWithSuspenseQuery usage](#atomwithsuspensequery-usage)

    import  from 'jotai'import  from 'jotai-tanstack-query'
    const idAtom = atom(1)const userAtom = atomWithSuspenseQuery((get) => () => `)    return res.json()  },}))
    const UserData = () => ] = useAtom(userAtom)
      return <div></div>}

### [atomWithSuspenseInfiniteQuery usage](#atomwithsuspenseinfinitequery-usage)

    import  from 'jotai'import  from 'jotai-tanstack-query'
    const postsAtom = atomWithSuspenseInfiniteQuery(() => () => `)    return res.json()  },  getNextPageParam: (lastPage, allPages, lastPageParam) => lastPageParam + 1,  initialPageParam: 1,}))
    const Posts = () => ] =    useAtom(postsAtom)
      return (    <>      >          ></div>          ))}        </div>      ))}      <button onClick=>Next</button>    </>  )}

### [Referencing the same instance of Query Client in your project](#referencing-the-same-instance-of-query-client-in-your-project)

Perhaps you have some custom hooks in your project that utilises the `useQueryClient()` hook to obtain the `QueryClient` object and call its methods.

To ensure that you reference the same `QueryClient` object, be sure to wrap the root of your project in a `<Provider>` and initialise `queryClientAtom` with the same `queryClient` value you provided to `QueryClientProvider`.

Without this step, `useQueryAtom` will reference a separate `QueryClient` from any hooks that utilise the `useQueryClient()` hook to get the queryClient.

Alternatively, you can specify your `queryClient` with `getQueryClient` parameter.

#### [Example](#example)

In the example below, we have a mutation hook, `useTodoMutation` and a query `todosAtom`.

We included an initialisation step in our root `<App>` node.

Although they reference methods same query key (`'todos'`), the `onSuccess` invalidation in `useTodoMutation` will not trigger **if the `Provider` initialisation step was not done.**

This will result in `todosAtom` showing stale data as it was not prompted to refetch.

⚠️ Note: When using **Typescript**, it is recommended to use a Map when passing the queryClient value to useHydrateAtoms. You can find a working example in the [Initializing State on Render docs](https://jotai.org/docs/guides/initialize-atom-on-render#using-typescript)

    import  from 'jotai/react'import  from 'jotai/react/utils'import  from '@tanstack/react-query'import  from 'jotai-tanstack-query'
    const queryClient = new QueryClient()
    const HydrateAtoms = () => 
    export const App = () => >      <Provider>                <HydrateAtoms>          <App />        </HydrateAtoms>      </Provider>    </QueryClientProvider>  )}
    export const todosAtom = atomWithQuery((get) => })
    export const useTodoMutation = () => )    },    ,      onError,    }  )}

### [SSR support](#ssr-support)

All atoms can be used within the context of a server side rendered app, such as a next.js app or Gatsby app. You can [use both options](https://tanstack.com/query/v5/docs/framework/react/guides/ssr) that React Query supports for use within SSR apps, [hydration](https://tanstack.com/query/v5/docs/react/guides/ssr#using-the-hydration-apis) or [`initialData`](https://tanstack.com/query/v5/docs/react/guides/ssr#get-started-fast-with-initialdata).

### [Error handling](#error-handling)

Fetch error will be thrown and can be caught with ErrorBoundary. Refetching may recover from a temporary error.

See [a working example](https://codesandbox.io/s/4gfp6z) to learn more.

### [Devtools](#devtools)

In order to use the Devtools, you need to install it additionally.

    npm install @tanstack/react-query-devtools

All you have to do is put the `<ReactQueryDevtools />` within `<QueryClientProvider />`.

    import  from '@tanstack/react-query'import  from '@tanstack/react-query-devtools'import  from 'jotai-tanstack-query'
    const queryClient = new QueryClient(,  },})
    const HydrateAtoms = () => 
    export const App = () => >      <Provider>        <HydrateAtoms>          <App />        </HydrateAtoms>      </Provider>      <ReactQueryDevtools />    </QueryClientProvider>  )}

## [Migrate to v0.8.0](#migrate-to-v0-8-0) 

### [Change in atom signature](#change-in-atom-signature)

All atom signatures have changed to be more consistent with TanStack Query. v0.8.0 returns only a single atom, instead of a tuple of atoms, and hence the name change from `atomsWithSomething` to`atomWithSomething`.

    - const [dataAtom, statusAtom] = atomsWithSomething(getOptions, getQueryClient)+ const dataAtom = atomWithSomething(getOptions, getQueryClient)

### [Simplified Return Structure](#simplified-return-structure)

In the previous version of `jotai-tanstack-query`, the query atoms `atomsWithQuery` and `atomsWithInfiniteQuery` returned a tuple of atoms: `[dataAtom, statusAtom]`. This design separated the data and its status into two different atoms.

#### [atomWithQuery and atomWithInfiniteQuery](#atomwithquery-and-atomwithinfinitequery)

-   `dataAtom` was used to access the actual data (`TData`).
-   `statusAtom` provided the status object (`QueryObserverResult<TData, TError>`), which included additional attributes like `isPending`, `isError`, etc.

In v0.8.0, they have been replaced by `atomWithQuery` and `atomWithInfiniteQuery` to return only a single `dataAtom`. This `dataAtom` now directly provides the `QueryObserverResult<TData, TError>`, aligning it closely with the behavior of Tanstack Query\'s bindings.

To migrate to the new version, replace the separate `dataAtom` and `statusAtom` usage with the unified `dataAtom` that now contains both data and status information.

    - const [dataAtom, statusAtom] = atomsWithQuery(/* ... */);- const [data] = useAtom(dataAtom);- const [status] = useAtom(statusAtom);
    + const dataAtom = atomWithQuery(/* ... */);+ const [] = useAtom(dataAtom);

#### [atomWithMutation](#atomwithmutation)

Similar to `atomsWithQuery` and `atomsWithInfiniteQuery`, `atomWithMutation` also returns a single atom instead of a tuple of atoms. The return type of the atom value is `MutationObserverResult<TData, TError, TVariables, TContext>`.

    - const [, postAtom] = atomsWithMutation(/* ... */);- const [post, mutate] = useAtom(postAtom); // Accessing mutation status from post; and mutate() to execute the mutation
    + const postAtom = atomWithMutation(/* ... */);+ const [] = useAtom(postAtom); // Accessing mutation result and mutate method from the same atom

### [Examples](#examples)

#### [Basic demo](#basic-demo)

#### [Devtools demo](#devtools-demo)

#### [Hackernews](#hackernews)

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)