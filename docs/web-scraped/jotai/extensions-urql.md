# Source: https://jotai.org/docs/extensions/urql

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# URQL 

[urql](https://formidable.com/open-source/urql/) offers a toolkit for GraphQL querying, caching, and state management.

From the [Overview docs](https://formidable.com/open-source/urql/docs/):

> urql is a highly customizable and versatile GraphQL client with which you add on features like normalized caching as you grow. It\'s built to be both easy to use for newcomers to GraphQL, and extensible, to grow to support dynamic single-app applications and highly customized GraphQL infrastructure. In short, urql prioritizes usability and adaptability.

[jotai-urql](https://github.com/jotaijs/jotai-urql) is a Jotai extension library for URQL. It offers a cohesive interface that incorporates all of URQL\'s GraphQL features, allowing you to leverage these functionalities alongside your existing Jotai state.

### [Install](#install)

You have to install `jotai-urql`, `@urql/core` and `wonka` to use the extension.

    npm install jotai-urql @urql/core wonka

### [Exported functions](#exported-functions)

-   `atomWithQuery` for [client.query](https://formidable.com/open-source/urql/docs/api/core/#clientquery)
-   `atomWithMutation` for [client.mutation](https://formidable.com/open-source/urql/docs/api/core/#clientmutation)
-   `atomWithSubscription` for [client.subscription](https://formidable.com/open-source/urql/docs/api/core/#clientsubscription)

### [Basic usage](#basic-usage)

#### [Query:](#query)

    import  from 'jotai'
    const countQueryAtom = atomWithQuery<>(',  getClient: () => client, // This option is optional if `useRehydrateAtom([[clientAtom, client]])` is used globally})
    const Counter = () => 
      // You have to use optional chaining here, as data may be undefined at this point (only in case of error)  return <></>}

#### [Mutation:](#mutation)

    import  from 'jotai'
    const incrementMutationAtom = atomWithMutation<>(',})
    const Counter = () =>       >        Increment      </button>      <div></div>    </div>  )}

### [Simplified type of options passed to functions](#simplified-type-of-options-passed-to-functions)

    type AtomWithQueryOptions<  Data = unknown,  Variables extends AnyVariables = AnyVariables,> = 
    type AtomWithMutationOptions<  Data = unknown,  Variables extends AnyVariables = AnyVariables,> = 
    // Subscription type is the same as AtomWithQueryOptions

### [Disable suspense](#disable-suspense)

Usage of `import  from "jotai/utils"` is preferred instead as proven more stable. However is you still want that here is how you do it:

    import  from 'jotai-urql'
    export const App = () => 

### [Useful helper hook](#useful-helper-hook)

Here is the helper hook, to cover one rare corner case, and make use of these bindings similar to `@tanstack/react-query` default behavior where errors are treated as errors (in case of Promise reject) and are handled mostly in the nearby ErrorBoundaries. Only valid for suspended version.

#### [useQueryAtomData](#usequeryatomdata)

Neatly returns `data` after the resolution + handles all the error throwing/reexecute cases/corner cases. Note that Type is overridden so `data` it never `undefined` nor `null` (unless that\'s expected return type of the query itself)

    import type  from '@urql/core'import  from 'jotai'import type  from 'jotai-urql'
    export const useQueryAtomData = <  Data = unknown,  Variables extends AnyVariables = AnyVariables,>(  queryAtom: AtomWithQuery<Data, Variables>,) => ),    )  }
      if (opResult.error) 
      if (!opResult.data)   return [opResult.data, dispatch, opResult] as [    Exclude<typeof opResult.data, undefined>,    typeof dispatch,    typeof opResult,  ]}
    // Suspense tree while promise is resolving (not going to be needed in next versions of React)function use(promise: Promise<any> | any)   if (promise.status === 'rejected')  else if (promise.status === 'pending')  else ,      (reason: any) => ,    )    throw promise  }}

#### [Basic demo](#basic-demo)

### [Referencing the same instance of the client for both atoms and urql provider](#referencing-the-same-instance-of-the-client-for-both-atoms-and-urql-provider)

To ensure that you reference the same urqlClient object, be sure to wrap the root of your project in a `<Provider>` and initialise clientAtom with the same urqlClient value you provided to UrqlProvider.

Without this step, you may end up specifying client each time when you use `atomWithQuery`. Now you can just ignore the optional `getClient` parameter, and it will use the client from the context.

    import  from 'react'import  from 'jotai/react'import  from 'jotai/react/utils'import  from 'jotai-urql'
    import  from 'urql'
    const urqlClient = createClient( }  },})
    const HydrateAtoms = () => 
    export default function MyApp() >      <Provider>        <HydrateAtoms>          <Suspense fallback="Loading...">            <Component  />          </Suspense>        </HydrateAtoms>      </Provider>    </UrqlProvider>  )}

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)