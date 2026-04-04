# Source: https://jotai.org/docs/basics/comparison

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Comparison 

Jotai was born to solve extra re-render issues in React. An extra re-render is when the render process produces the same UI result, where users won\'t see any differences.

To tackle this issue with React context (useContext + useState), one would require many contexts and face some issues.

-   Provider hell: It\'s likely that your root component has many context providers, which is technically okay, and sometimes desirable to provide context in different subtree.
-   Dynamic addition/deletion: Adding a new context at runtime is not very nice, because you need to add a new provider and its children will be re-mounted.

Traditionally, a top-down solution to this is to use a selector function. The [use-context-selector](https://github.com/dai-shi/use-context-selector) library is one example. The issue with this approach is the selector function needs to return referentially equal values to prevent re-renders, and this often requires a memoization technique.

Jotai takes a bottom-up approach with the atomic model, inspired by [Recoil](https://recoiljs.org/). One can build state combining atoms, and optimize renders based on atom dependency. This avoids the need for memoization.

Jotai has two principles.

-   Primitive: Its basic API is simple, like `useState`.
-   Flexible: Atoms can derive another atom and form a graph. Atoms can also be updated by another arbitrary atom. It allows abstracting complex state models.

### [How is Jotai different from useContext of React?](#how-is-jotai-different-from-usecontext-of-react)

Jotai\'s core API is minimalistic and makes it easy to build utilities based upon it.

#### [Analogy](#analogy)

You can view Jotai as a drop-in replacement to `useContext`. Except Jotai is aiming for simplicity, minimalistic API and can do much more than `useContext` & `useState`.

#### [Usage difference](#usage-difference)

We can see how we used to share data to children, compared to how we do it with Jotai. But let\'s use a real-world example where we have multiple `Context` in our app.

    // 1. useState local stateconst Component = () => 
    // 2. Lift local state up and share it via contextconst StateContext = createContext()const Parent = () => >          </StateContext.Provider>  )}const Component = () => 
    // 3. Have multiple states and contextsconst State1Context = createContext()const State2Context = createContext()const Parent = () => (  <State1Context.Provider value=>    <State2Context.Provider value=>          </State2Context.Provider>  </State1Context.Provider>)const Component1 = () => const Component2 = () => 

Now let\'s see how Jotai simplify it for us. You can just use atoms instead of multiple `Context`.

    import  from 'jotai'const atom1 = atom(0)const atom2 = atom(0)// Optional: you can use Provider's just like useContext,// ...but if you only need one,// ...you can just omit it and Jotai will use a default one (called Provider-less mode).const Parent = () => </Provider>}const Component1 = () => const Component2 = () => 

### [How is Jotai different from Zustand?](#how-is-jotai-different-from-zustand)

#### [Name](#name)

Jotai means \"state\" in Japanese. Zustand means \"state\" in German.

#### [Analogy](#analogy) 

Jotai is like Recoil. Zustand is like Redux.

#### [Where state resides](#where-state-resides)

To hold states, Both have stores that can exist either at module level or at context level. Jotai is designed to be context first, and module second. Zustand is designed to be module first, and context second.

#### [How to structure state](#how-to-structure-state)

Jotai state consists of atoms (i.e. bottom-up). Zustand state is one object (i.e. top-down).

#### [Technical difference](#technical-difference)

The major difference is the state model. Zustand is a single store (although you could create multiple separate stores), while Jotai consists of primitive atoms and allows composing them together. In this sense, it\'s the matter of programming mental model.

#### [When to use which](#when-to-use-which)

-   If you need a replacement for useState+useContext, Jotai fits well.
-   If you want a simple module state, Zustand fits well.
-   If code splitting is important, Jotai should perform well.
-   If you prefer Redux devtools, Zustand is good to go.
-   If you want to make use of Suspense, Jotai is the one.

### [How is Jotai different from Recoil?](#how-is-jotai-different-from-recoil)

(Disclaimer: the author is not very familiar with Recoil, this may be biased and inaccurate.)

#### [Developer](#developer)

-   Jotai is developed with collective work by a few developers in Poimandres (formerly react-spring) org.
-   Recoil is developed by a team at Facebook.

#### [Basis](#basis)

-   Jotai is focusing on primitive APIs for easy learning, and it\'s unopinionated. (The same philosophy with Zustand)
-   Recoil is all-in-one, and it has various cache strategies.

#### [Technical difference](#technical-difference) 

-   Jotai depends on atom object referential identities.
-   Recoil depends on atom string keys.

#### [When to use which](#when-to-use-which) 

-   If you want to learn something new, either should work.
-   If you like Zustand, Jotai would also be pleasant.
-   If you need React Context alternatives, Jotai comes with enough features.
-   If you need to read and write atoms outside React, Jotai provides store API.
-   If you would try to create a new library, Jotai might give good primitives.
-   Otherwise, both are pretty similar about the general goals and basic techniques, so please try both and share your feedback with us.

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)