# Source: https://jotai.org/docs/guides/debugging

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Debugging 

In basic apps, `console.log` can be our best friend for debugging atoms, but when applications get bigger and we have more atoms to use, logging would not be a good way of debugging atoms. Jotai provides two ways of debugging atoms, **React Dev Tools** and **Redux Dev tools**. For reading values and simple debugging, React Dev Tools might suit you, but for more complicated tasks like Time-travelling and setting values, Redux Dev Tools would be a better option.

## [Debug labels](#debug-labels)

It is worth mentioning that we have a concept called **Debug labels** in Jotai which may help us with debugging. By default each Jotai state has the label like `1:<no debugLabel>` with number being internal `key` assigned to each atom automatically. But you can add labels to atoms to help you distinguish them more easily with `debugLabel`.

    const countAtom = atom(0)// countAtom's debugLabel by default is 'atom1'if (process.env.NODE_ENV !== 'production') 

Jotai provides both a Babel and a SWC plugin, that adds a debugLabel automatically to every atom, which makes things easier for us. For more info, check out [jotai/babel](https://github.com/pmndrs/jotai/blob/main/docs/tools/babel.mdx#plugin-debug-label) and [\@swc-jotai/debug-label](https://github.com/pmndrs/jotai/blob/main/docs/tools/swc.mdx)

## [Using React Dev Tools](#using-react-dev-tools)

You can use [React Dev Tools](https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi) to inspect Jotai state. To achieve that [useDebugValue](https://react.dev/reference/react/useDebugValue) is used inside custom hooks. Keep in mind that it only works in dev mode (such as `NODE_ENV === 'development'`).

### [useAtom](#useatom)

`useAtom` calls `useDebugValue` for atom values, so if you select the component that consumes Jotai atoms in React Dev Tools, you would see \"Atom\" hooks for each atom that is used in the component along with the value it has right now.

### [useAtomsDebugValue](#useatomsdebugvalue)

`useAtomsDebugValue` catches all atoms in a component tree under Provider (or an entire tree for Provider-less mode), and `useDebugValue` for all atoms values. If you navigate to the component that has `useAtomsDebugValue` in the React Dev Tools, we can see a custom hook \"AtomsDebugValue\" which allows you to see all atom values and their dependents.

One use case is to put the hook just under the `Provider` component:

    const DebugAtoms = () => 
    const Root = () => (  <Provider>    <DebugAtoms />    <App />  </Provider>)

## [Using Redux DevTools](#using-redux-devtools)

You can also use [Redux DevTools](https://chrome.google.com/webstore/detail/redux-devtools/lmhkpmbekcpmknklioeibfkpmmfibljd) to inspect atoms, with many features like Time-travelling and value dispatching.

### [](#useatomdevtools)[useAtomDevtools](https://jotai.org/docs/api/devtools#use-atom-devtools)

> `useAtomDevtools` is a React hook that manages ReduxDevTools extension for a particular atom.

If you have a specific atom in mind that you may want to debug, `useAtomDevtools` can be a good option.

    const countAtom = atom(0)// setting countAtom.debugLabel is recommended if we have more atoms
    function Counter() 

Now if we try `setCount`, we can see that the Redux Dev Tools logs those changes immediately.

![](https://lh3.googleusercontent.com/pw/AP1GczMgeYQOyCAc69gJIAcRBtKO9BOUEE3SQB5Bl-7IScJfChWGnVb3B0OmlhrjK8caQVnj-HtyN1cpv1l1K9kE4pxwapUwu_2OB-dO_G18ZUC1NbDJFiXYRW9jX8OeDBJeWg1Qx9_IdkfoaoIin90A8gSE=w828-h268-s-no-gm) ![]()

#### [Time travel](#time-travel)

Sometimes we need to switch to a specific value of our atoms\' state, with Time travelling this is possible. You can hover on each action you see in the devtools and see the **Jump** option there, with clicking it you\'d be able to switch to that specific value.

#### [Pause](#pause)

If we don\'t record changes on atoms, we can stop watching those using the **Pausing** feature.

![](https://lh3.googleusercontent.com/pw/AP1GczP8hTBFtwlx0BJGGbbcXgfhMNG2Vz_uozdVnrTJHwMb1gKx55TP59WgvsMwgIyExwscgYZSpYDmxCJXjk_pKy6wP-K-0p287lkRXdTZEf074xUZr8fnIpkwg-zN14VXZ2STet1sVgTTawm49mc8Oygb=w395-h87-s-no-gm)

#### [Dispatch](#dispatch)

It\'s possible to set values on atoms with the **Dispatch** feature. You can do that by clicking on the **Show Dispatcher** button. ![](https://lh3.googleusercontent.com/pw/AP1GczMNn6aXTA7K8ZFzUj17I40cm0o7joOG6E76Q6UVnXYJ3TO7ItRI6Jr1EIxogfY9P2xkiQfyYqB7_aU--R_vdSyNXAtTfPuxxLymApRoZov0-6ZHS7mmxxxD4Ku1JnqTRyPyZaQHyQPkq8j4CciQaISV=w832-h149-s-no-gm) This would set the `countAtoms`\'s value to `5`.

> We should note that the value will be parsed by JSON.parse, so pass supported values.

### [](#useatomsdevtools)[useAtomsDevtools](../tools/devtools)

> `useAtomsDevtools` is a catch-all version of `useAtomDevtools` where it shows all atoms in the store instead of showing a specific one.

We\'d recommend this hook if you want to keep track of all of your atoms in one place. It means every action on every atom that is placed in the bottom of this hook (in the React tree) will be caught by the Redux Dev Tools.

Every feature of `useAtomDevtools` is supported in this hook, but there\'s an extra feature, which includes giving more information about atoms dependents like:

    ,  "dependents": }

## [Frozen Atoms](#frozen-atoms)

To find bugs where you accidentally tried to mutate objects stored in atoms you could use `freezeAtom` or `freezeAtomCreator`from `jotai/utils` bundle. Which returns atoms value that is deeply freezed with `Object.freeze`.

### [freezeAtom](#freezeatom)

    freezeAtom(anAtom): AtomType

`freezeAtom` takes an existing atom and make it \"frozen\". It returns the same atom. The atom value will be deeply frozen by `Object.freeze`. It is useful to find bugs where you unintentionally tried to change objects (states) which can lead to unexpected behavior. You may use `freezeAtom` with all atoms to prevent this situation.

#### [Parameters](#parameters)

**anAtom** (required): An atom you wish to freeze.

#### [Examples](#examples)

    import  from 'jotai'import  from 'jotai/utils'
    const objAtom = freezeAtom(atom())

### [freezeAtomCreator](#freezeatomcreator)

If you need, you can define a factory for `freezeAtom`.

    import  from 'jotai/utils'
    export function freezeAtomCreator<  CreateAtom extends (...args: unknown[]) => Atom<unknown>,>(createAtom: CreateAtom): CreateAtom 

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)