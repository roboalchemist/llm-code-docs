# Source: https://jotai.org/docs/tools/devtools

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Devtools 

### [Install](#install)

Install `jotai-devtools` to your project to get started.

    npm install jotai-devtools

### [Notes](#notes)

-   `<DevTools/>` is optimized to be tree-shakable for production builds, and **only works in a non-production environment**
-   Hooks are dev-only, and are designed to work in a non-production environment
-   Feedback welcome, please file issues or ask questions on the [Jotai DevTools GitHub Repo](https://github.com/jotaijs/jotai-devtools/discussions)

### [Quick links](#quick-links)

-   [UI Devtools](#ui-devtools)
-   Hooks
    -   [useAtomsDebugValue](#useatomsdebugvalue)
    -   [useAtomDevtools](#useatomdevtools)
    -   [useAtomsDevtools](#useatomsdevtools)
    -   [useAtomsSnapshot](#useatomssnapshot)
    -   [useGotoAtomsSnapshot](#usegotoatomssnapshot)
-   Migration guides
    -   [Migrate from `@emotion/react`](https://github.com/jotaijs/jotai-devtools?tab=readme-ov-file#migrate-%C6%92rom-emotionreact-to-native-css)

### [UI DevTools](#ui-devtools)

Enhance your development experience with the UI based Jotai DevTool.

#### [Babel plugin setup - (*Optional but highly recommended*)](#babel-plugin-setup-optional-but-highly-recommended) 

Use Jotai babel plugins for optimal debugging experience. Find the complete guide on the [babel](../tools/babel) page and/or [swc](../tools/swc) page.

Example:

    

Example for Vite + React project:

    // vite.config.ts
    export default defineConfig(,    }),  ],})

### [Next JS setup](#next-js-setup)

*You may skip this section if you\'re not using [Next.js](https://nextjs.org).*

Enable `transpilePackages` for the UI CSS and components to be transpiled correctly.

    // next.config.tsconst nextConfig = module.exports = nextConfig

### [Available props](#available-props)

    type DevToolsProps = }

### [Usage](#usage)

#### [Provider-less](#provider-less)

    import  from 'jotai-devtools'import 'jotai-devtools/styles.css'
    const App = () =>     </>  )}

#### [With Provider](#with-provider)

    import  from 'jotai'import  from 'jotai-devtools'import 'jotai-devtools/styles.css'
    const customStore = createStore()
    const App = () => >      <DevTools store= />          </Provider>  )}

### [Preview](#preview)

## [useAtomsDebugValue](#useatomsdebugvalue)

`useAtomsDebugValue` is a React hook that will show all atom values in React Devtools.

    function useAtomsDebugValue(options?: ): void

Internally, it uses `useDebugValue` which is only effective in DEV mode. It will catch all atoms that are accessible from the place the hook is located.

### [Example](#example)

    import  from 'jotai-devtools/utils'
    const textAtom = atom('hello')textAtom.debugLabel = 'textAtom'
    const lenAtom = atom((get) => get(textAtom).length)lenAtom.debugLabel = 'lenAtom'
    const TextBox = () =>  onChange= />()    </span>  )}
    const DebugAtoms = () => 
    const App = () => (  <Provider>    <DebugAtoms />    <TextBox />  </Provider>)

## [useAtomDevtools](#useatomdevtools)

`useAtomDevtools` is a React hook that manages ReduxDevTools extension for a particular atom.

    function useAtomDevtools<Value>(  anAtom: WritableAtom<Value, Value>,  options?: ,): void

The `useAtomDevtools` hook accepts a generic type parameter (mirroring the type stored in the atom). Additionally, the hook accepts two invocation parameters, `anAtom` and `name`. `anAtom` is the atom that will be attached to the devtools instance. `name` is an optional parameter that defines the debug label for the devtools instance. If `name` is undefined, `atom.debugLabel` will be used instead.

### [Example](#example) 

    import  from 'jotai-devtools/utils'
    // The interface for the type stored in the atom.export interface Task 
    // The atom to debug.export const tasksAtom = atom<Task[]>([])
    // If the useAtomDevtools name parameter is undefined, this value will be used instead.tasksAtom.debugLabel = 'Tasks'
    export const useTasksDevtools = () => 

## [useAtomsDevtools](#useatomsdevtools)

⚠️ Note: This hook is experimental (feedbacks are welcome) and only works in a `process.env.NODE_ENV !== 'production'` environment.

`useAtomsDevtools` is a catch-all version of `useAtomDevtools` where it shows all atoms in the store instead of showing a specific one.

    function useAtomsDevtools(  name: string,  options?: ,): void

It takes a `name` parameter that is needed for naming the Redux devtools instance and a `store` parameter.

As a limitation for this API, we need to put `useAtomsDevtools` in a component where the consumed atoms should be in a lower place of the React tree than that component (`AtomsDevtools` in the below example). `AtomsDevtools` component can be considered as a best practice for our apps.

### [Example](#example) 

    const countAtom = atom(0);const doubleCountAtom = atom((get) => get(countAtom) * 2);
    function Counter() 
    const AtomsDevtools = () => 
    export default function App()  

## [useAtomsSnapshot](#useatomssnapshot)

⚠️ Note: This hook only works in a `process.env.NODE_ENV !== 'production'` environment. And it returns a static empty value in production.

`useAtomsSnapshot` takes a snapshot of the currently mounted atoms and their state.

    function useAtomsSnapshot(options?: ): AtomsSnapshot

It accepts a `store` parameter and will return an `AtomsSnapshot`, which is basically a `Map<AnyAtom, unknown>`. You can use the `Map` API to iterate over atoms and their state. This hook is primarily meant for debugging and devtools use cases.

Be careful using this hook because it will cause the component to re-render for all state changes.

### [Example](#example) 

    import  from 'jotai'import  from 'jotai-devtools/utils'
    const RegisteredAtoms = () => </p>      <div>        `}>: $`}</p>        ))}      </div>    </div>  )}
    const App = () => (  <Provider>    <RegisteredAtoms />  </Provider>)

## [useGotoAtomsSnapshot](#usegotoatomssnapshot)

⚠️ Note: This hook only works in a `process.env.NODE_ENV !== 'production'` environment. And it works like an empty function in the production environment.

`useGotoAtomsSnapshot` will update the current Jotai state to match the passed snapshot.

    function useGotoAtomsSnapshot(options?: ): (values: Iterable<readonly [AnyAtom, unknown]>) => void

This hook returns a callback, which takes a `snapshot` from the `useAtomsSnapshot` hook and will update the Jotai state. It accepts a `store` parameter. This hook is primarily meant for debugging and devtools use cases.

### [Example](#example) 

    import  from 'jotai'import  from 'jotai-devtools/utils'
    const petAtom = atom('cat')const colorAtom = atom('blue')
    const UpdateSnapshot = () => }    >      Go to snapshot    </button>  )}

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)