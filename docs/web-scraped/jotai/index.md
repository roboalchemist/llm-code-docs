# Source: https://jotai.org/docs/

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Documentation 

Welcome to the Jotai v2 documentation! Jotai\'s atomic approach to global React state management scales from a simple `useState` replacement to an enterprise application with complex requirements.

## [Features](#features)

-   Minimal core API (2kb)
-   Many utilities and extensions
-   TypeScript oriented
-   Works with Next.js, Waku, Remix, and React Native

## [Core](#core)

Jotai has a very minimal API, exposing only a few exports from the main `jotai` bundle. They are split into four categories below.

[](/docs/core/atom "atom")

<div>

atom

</div>

[](/docs/core/use-atom "useAtom")

<div>

useAtom

</div>

[](/docs/core/store "Store")

<div>

Store

</div>

[](/docs/core/provider "Provider")

<div>

Provider

</div>

## [Utilities](#utilities)

Jotai also includes a `jotai/utils` bundle with a variety of extra utility functions. One example is `atomWithStorage`, which includes localStorage persistence and cross browser tab synchronization.

[](/docs/utilities/storage "Storage")

<div>

Storage

</div>

[](/docs/utilities/ssr "SSR")

<div>

SSR

</div>

[](/docs/utilities/async "Async")

<div>

Async

</div>

[](/docs/utilities/lazy "Lazy")

<div>

Lazy

</div>

[](/docs/utilities/resettable "Resettable")

<div>

Resettable

</div>

[](/docs/utilities/family "Family")

<div>

Family

</div>

## [Extensions](#extensions)

Jotai has many officially maintained extensions including `atomWithQuery` for React Query and `atomWithMachine` for XState, among many others.

[](/docs/extensions/trpc "tRPC")

<div>

tRPC

</div>

[](/docs/extensions/query "Query")

<div>

Query

</div>

[](/docs/extensions/effect "Effect")

<div>

Effect

</div>

[](/docs/extensions/urql "URQL")

<div>

URQL

</div>

[](/docs/extensions/immer "Immer")

<div>

Immer

</div>

[](/docs/extensions/xstate "XState")

<div>

XState

</div>

[](/docs/extensions/location "Location")

<div>

Location

</div>

[](/docs/extensions/cache "Cache")

<div>

Cache

</div>

[](/docs/extensions/scope "Scope")

<div>

Scope

</div>

[](/docs/extensions/optics "Optics")

<div>

Optics

</div>

## [Third-party](#third-party)

Beyond the official extensions, there are many third-party community packages as well.

[](/docs/third-party/history "History")

<div>

History

</div>

[](/docs/third-party/derive "Derive")

<div>

Derive

</div>

[](/docs/third-party/bunja "Bunja")

<div>

Bunja

</div>

## [Tools](#tools)

Use SWC and Babel compiler plugins for React Fast Refresh support and debugging labels. This creates the best developer experience when using a React framework such as Next.js or Waku.

[](/docs/tools/swc "SWC")

<div>

SWC

</div>

[](/docs/tools/babel "Babel")

<div>

Babel

</div>

[](/docs/tools/devtools "Devtools")

<div>

Devtools

</div>

## [Basics](#basics)

Learn the basic concepts of the library, discover how it compares with others, and see usage examples.

[](/docs/basics/concepts "Concepts")

<div>

Concepts

</div>

[](/docs/basics/comparison "Comparison")

<div>

Comparison

</div>

[](/docs/basics/showcase "Showcase")

<div>

Showcase

</div>

[](/docs/basics/functional-programming-and-jotai "Functional programming and Jotai")

<div>

Functional programming and Jotai

</div>

## [Guides](#guides)

Guides can help with use common cases such as TypeScript, React frameworks, and basic patterns.

[](/docs/guides/migrating-to-v2-api "v2 API migration")

<div>

v2 API migration

</div>

[](/docs/guides/typescript "TypeScript")

<div>

TypeScript

</div>

[](/docs/guides/nextjs "Next.js")

<div>

Next.js

</div>

[](/docs/guides/waku "Waku")

<div>

Waku

</div>

[](/docs/guides/remix "Remix")

<div>

Remix

</div>

[](/docs/guides/react-native "React Native")

<div>

React Native

</div>

[](/docs/guides/debugging "Debugging")

<div>

Debugging

</div>

[](/docs/guides/performance "Performance")

<div>

Performance

</div>

[](/docs/guides/testing "Testing")

<div>

Testing

</div>

[](/docs/guides/core-internals "Core internals")

<div>

Core internals

</div>

[](/docs/guides/composing-atoms "Composing atoms")

<div>

Composing atoms

</div>

[](/docs/guides/atoms-in-atom "Atoms in atom")

<div>

Atoms in atom

</div>

[](/docs/guides/initialize-atom-on-render "Initializing state on render")

<div>

Initializing state on render

</div>

[](/docs/guides/persistence "Persistence")

<div>

Persistence

</div>

## [Recipes](#recipes)

Recipes can help with more advanced patterns.

[](/docs/recipes/large-objects "Large objects")

<div>

Large objects

</div>

[](/docs/recipes/custom-useatom-hooks "Custom useAtom hooks")

<div>

Custom useAtom hooks

</div>

[](/docs/recipes/use-atom-effect "useAtomEffect")

<div>

useAtomEffect

</div>

[](/docs/recipes/atom-with-toggle "atomWithToggle")

atomWithToggle

[](/docs/recipes/atom-with-compare "atomWithCompare")

atomWithCompare

[](/docs/recipes/atom-with-toggle-and-storage "atomWithToggleAndStorage")

atomWithToggleAndStorage

[](/docs/recipes/atom-with-refresh "atomWithRefresh")

atomWithRefresh

[](/docs/recipes/atom-with-refresh-and-default "atomWithRefreshAndDefault")

atomWithRefreshAndDefault

[](/docs/recipes/atom-with-listeners "atomWithListeners")

atomWithListeners

[](/docs/recipes/atom-with-broadcast "atomWithBroadcast")

atomWithBroadcast

[](/docs/recipes/atom-with-debounce "atomWithDebounce")

atomWithDebounce

[](/docs/recipes/use-reducer-atom "useReducerAtom")

<div>

useReducerAtom

</div>

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)