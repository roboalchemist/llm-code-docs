# Source: https://jotai.org/docs/basics/showcase

<div>

# [![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyODkuMTkgOTkuNzciIGNsYXNzPSJ0ZXh0LWJsYWNrIGRhcms6dGV4dC13aGl0ZSB3LVs0cmVtXSI+PHRpdGxlPkpvdGFpPC90aXRsZT48cGF0aCBkPSJNNDIuMzYsNS4zMkg2MS44MlY3MC4yM2EyOS40NiwyOS40NiwwLDAsMS00LDE1LjYxQTI3LjE5LDI3LjE5LDAsMCwxLDQ2LjY0LDk2LjA3YTM2LjI2LDM2LjI2LDAsMCwxLTE2LjU5LDMuNjEsMzcuNTYsMzcuNTYsMCwwLDEtMTUuMjUtM0EyNC4zLDI0LjMsMCwwLDEsNCw4Ny41OVEwLDgxLjUsMCw3Mi4yM0gxOS41OWMuMDYsMy42OSwxLjEzLDYuNTcsMy4yMSw4LjYxYTExLjIxLDExLjIxLDAsMCwwLDguMjUsMy4wN3ExMS4yMiwwLDExLjMxLTEzLjY4WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTEwNSw5OS43N3EtMTAuNTksMC0xOC4yOS00LjUyQTMwLjU0LDMwLjU0LDAsMCwxLDc0LjgyLDgyLjYxYTQwLjUyLDQwLjUyLDAsMCwxLTQuMTgtMTguODQsNDAuNzUsNDAuNzUsMCwwLDEsNC4xOC0xOC45M0EzMC42LDMwLjYsMCwwLDEsODYuNzEsMzIuMiwzNS41MiwzNS41MiwwLDAsMSwxMDUsMjcuNjhhMzUuNTgsMzUuNTgsMCwwLDEsMTguMyw0LjUyLDMwLjU3LDMwLjU3LDAsMCwxLDExLjg4LDEyLjY0LDQwLjc2LDQwLjc2LDAsMCwxLDQuMTksMTguOTMsNDAuNTIsNDAuNTIsMCwwLDEtNC4xOSwxOC44NEEzMC41MSwzMC41MSwwLDAsMSwxMjMuMyw5NS4yNVExMTUuNTksOTkuNzgsMTA1LDk5Ljc3Wk0xMjcuMTQsNS4zMnYxMC41SDgyLjg3VjUuMzJabS0yMiw3OS40NWExMiwxMiwwLDAsMCwxMC44OS02cTMuNy02LDMuNy0xNS4xM1QxMTYsNDguNDhhMTIsMTIsMCwwLDAtMTAuODktNiwxMi4xNSwxMi4xNSwwLDAsMC0xMSw2cS0zLjczLDYtMy43MywxNS4xNnQzLjczLDE1LjEzQTEyLjE2LDEyLjE2LDAsMCwwLDEwNS4wOSw4NC43N1oiIGZpbGw9ImN1cnJlbnRDb2xvciI+PC9wYXRoPjxwYXRoIGQ9Ik0xODYuMywyOC41OVY0My4xNEgxNzMuMTZWNzdxMCw0LDEuODIsNS40YTcuNSw3LjUsMCwwLDAsNC43MywxLjQxLDE0LjcyLDE0LjcyLDAsMCwwLDIuNzItLjI1bDIuMDktLjM4LDMsMTQuNDFjLTEsLjMtMi4zMy42Ni00LjA5LDEuMDZhMzQuMTMsMzQuMTMsMCwwLDEtNi40MS43NXEtMTAuNTUuNDctMTYuOTMtNC41NlQxNTMuOCw3OS41VjQzLjE0aC05LjU1VjI4LjU5aDkuNTVWMTEuODZoMTkuMzZWMjguNTlaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48cGF0aCBkPSJNMjE2LDk5LjczcS0xMCwwLTE2LjU5LTUuMjN0LTYuNTktMTUuNTlxMC03LjgxLDMuNjgtMTIuMjdhMjEuMTksMjEuMTksMCwwLDEsOS42Ni02LjUzQTU0Ljc4LDU0Ljc4LDAsMCwxLDIxOSw1Ny40MWE5OC41Nyw5OC41NywwLDAsMCwxMy0xLjkxcTMuOTItMSwzLjkxLTQuMzZ2LS4yOGE4LjQyLDguNDIsMCwwLDAtMi43LTYuNjhxLTIuNzItMi4zNS03LjY2LTIuMzZhMTMuNzcsMTMuNzcsMCwwLDAtOC4zMiwyLjI3LDEwLjcsMTAuNywwLDAsMC00LjA5LDUuNzdsLTE3LjkxLTEuNDVhMjMuODgsMjMuODgsMCwwLDEsOS45My0xNS4xNHE3Ljk0LTUuNTgsMjAuNDgtNS41OWE0Mi4yNCw0Mi4yNCwwLDAsMSwxNC41NCwyLjQ2LDI0LjE5LDI0LjE5LDAsMCwxLDEwLjk0LDcuNjZxNC4xNiw1LjIxLDQuMTYsMTMuNTJWOTguNDFIMjM2LjkyVjg4LjczaC0uNTRhMjAuMTgsMjAuMTgsMCwwLDEtNy42Miw3LjkzUTIyMy42OSw5OS43MywyMTYsOTkuNzNabTUuNTQtMTMuMzdBMTUsMTUsMCwwLDAsMjMyLDgyLjY2YTExLjk0LDExLjk0LDAsMCwwLDQuMDktOS4yVjY2LjA1YTExLjM4LDExLjM4LDAsMCwxLTMuNTIsMS4zNmMtMS42LjM5LTMuMjkuNzMtNS4xLDFzLTMuNDEuNTQtNC44NC43NWExOS4xOSwxOS4xOSwwLDAsMC04LjIsMi44Nyw3LjA2LDcuMDYsMCwwLDAtMy4xMSw2LjIyLDYuOTQsNi45NCwwLDAsMCwyLjg4LDZBMTIuNDMsMTIuNDMsMCwwLDAsMjIxLjUxLDg2LjM2WiIgZmlsbD0iY3VycmVudENvbG9yIj48L3BhdGg+PHBhdGggZD0iTTI3OC42OSwxOS41OWExMC40MSwxMC40MSwwLDAsMS03LjM3LTIuODksOS4xNCw5LjE0LDAsMCwxLTMuMDktNi45Myw5LjEsOS4xLDAsMCwxLDMuMDktNi45MSwxMSwxMSwwLDAsMSwxNC43OCwwLDkuMSw5LjEsMCwwLDEsMy4wOSw2LjkxLDkuMTQsOS4xNCwwLDAsMS0zLjA5LDYuOTNBMTAuNDUsMTAuNDUsMCwwLDEsMjc4LjY5LDE5LjU5Wk0yNjksOTguNDFWMjguNTloMTkuMzZWOTguNDFaIiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)[Jotai]

状態

Primitive and flexible state management for React

</div>

# Showcase 

-   Text Length example [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://githubbox.com/pmndrs/jotai/tree/main/examples/text_length)

    Count the length and show the uppercase of any text.

-   Hacker News example [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://githubbox.com/pmndrs/jotai/tree/main/examples/hacker_news)

    Demonstrate a news article with Jotai, hit next to see more articles.

-   Todos example [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://githubbox.com/pmndrs/jotai/tree/main/examples/todos)

    Record your todo list by typing them into this app, check them off if you have completed the task, and switch between `Completed` and `Incompleted` to see the status of your task.

-   Todos example with atomFamily and localStorage [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://githubbox.com/pmndrs/jotai/tree/main/examples/todos_with_atomFamily)

    Implement a todo list using atomFamily and localStorage. You can store your todo list to localStorage by clicking `Save to localStorage`, then remove your todo list and try restoring them by clicking `Load from localStorage`.

-   Clock with Next.js [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://codesandbox.io/s/nextjs-with-jotai-5ylrj)

    An UTC time electronic clock implementation using Next.js and Jotai.

-   Tic Tac Toe game [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://codesandbox.io/s/jotai-tic-tac-6cg3h)

    A game of tic tac toe implemented with Jotai.

-   React Three Fiber demo [![Open in CodeSandbox](https://img.shields.io/badge/Open%20in-CodeSandbox-blue?style=flat-square&logo=codesandbox)](https://codesandbox.io/s/jotai-r3f-fri9d)

    A simple demo to use Jotai with react-three-fiber

[library by [Daishi Kato]](https://twitter.com/dai_shi "Daishi Kato")[art by [Jessie Waters]](https://jessiewaters.com "Jessie Waters")[](https://candycode.com/ "candycode, an alternative graphic design and web development agency based in San Diego")

[site by]![candycode alternative graphic design web development agency San Diego](https://storage.googleapis.com/candycode/candycode.svg)