# Source: https://ast-grep.github.io/catalog/tsx.md

---
url: /catalog/tsx.md
---
# TSX

This page curates a list of example ast-grep rules to check and to rewrite TypeScript with JSX syntax.

:::danger TSX and TypeScript are different.
TSX differs from TypeScript because it is an extension of the latter that supports JSX elements.
They need distinct parsers because of [conflicting syntax](https://www.typescriptlang.org/docs/handbook/jsx.html#the-as-operator).

In order to reduce rule duplication, you can use the [`languageGlobs`](/reference/sgconfig.html#languageglobs) option to force ast-grep to use parse `.ts` files as TSX.
:::

## Unnecessary `useState` Type&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiUGF0Y2giLCJsYW5nIjoidHlwZXNjcmlwdCIsInF1ZXJ5IjoidXNlU3RhdGU8c3RyaW5nPigkQSkiLCJyZXdyaXRlIjoidXNlU3RhdGUoJEEpIiwiY29uZmlnIjoiIyBZQU1MIFJ1bGUgaXMgbW9yZSBwb3dlcmZ1bCFcbiMgaHR0cHM6Ly9hc3QtZ3JlcC5naXRodWIuaW8vZ3VpZGUvcnVsZS1jb25maWcuaHRtbCNydWxlXG5ydWxlOlxuICBhbnk6XG4gICAgLSBwYXR0ZXJuOiBjb25zb2xlLmxvZygkQSlcbiAgICAtIHBhdHRlcm46IGNvbnNvbGUuZGVidWcoJEEpXG5maXg6XG4gIGxvZ2dlci5sb2coJEEpIiwic291cmNlIjoiZnVuY3Rpb24gQ29tcG9uZW50KCkge1xuICBjb25zdCBbbmFtZSwgc2V0TmFtZV0gPSB1c2VTdGF0ZTxzdHJpbmc+KCdSZWFjdCcpXG59In0=)

### Description

React's [`useState`](https://react.dev/reference/react/useState) is a Hook that lets you add a state variable to your component. The type annotation of `useState`'s generic type argument, for example `useState<number>(123)`, is unnecessary if TypeScript can infer the type of the state variable from the initial value.

We can usually skip annotating if the generic type argument is a single primitive type like `number`, `string` or `boolean`.

### Pattern

::: code-group

```bash [number]
ast-grep -p 'useState<number>($A)' -r 'useState($A)' -l tsx
```

```bash [string]
ast-grep -p 'useState<string>($A)' -r 'useState($A)'
```

```bash [boolean]
ast-grep -p 'useState<boolean>($A)' -r 'useState($A)'
```

:::

### Example

```ts {2}
function Component() {
  const [name, setName] = useState<string>('React')
}
```

### Diff

```ts
function Component() {
  const [name, setName] = useState<string>('React') // [!code --]
  const [name, setName] = useState('React') // [!code ++]
}
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim)

## Avoid `&&` short circuit in JSX&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InRzeCIsInF1ZXJ5IjoiY29uc29sZS5sb2coJE1BVENIKSIsInJld3JpdGUiOiJsb2dnZXIubG9nKCRNQVRDSCkiLCJjb25maWciOiJpZDogZG8td2hhdC1icm9vb29vb2tseW4tc2FpZFxubGFuZ3VhZ2U6IFRzeFxuc2V2ZXJpdHk6IGVycm9yXG5ydWxlOlxuICBraW5kOiBqc3hfZXhwcmVzc2lvblxuICBoYXM6XG4gICAgcGF0dGVybjogJEEgJiYgJEJcbiAgbm90OlxuICAgIGluc2lkZTpcbiAgICAgIGtpbmQ6IGpzeF9hdHRyaWJ1dGVcbmZpeDogXCJ7JEEgPyAkQiA6IG51bGx9XCIiLCJzb3VyY2UiOiI8ZGl2PntcbiAgbnVtICYmIDxkaXYvPlxufTwvZGl2PiJ9)

### Description

In [React](https://react.dev/learn/conditional-rendering), you can conditionally render JSX using JavaScript syntax like `if` statements, `&&`, and `? :` operators.
However, you should almost never put numbers on the left side of `&&`. This is because React will render the number `0`, instead of the JSX element on the right side. A concrete example will be conditionally rendering a list when the list is not empty.

This rule will find and fix any short-circuit rendering in JSX and rewrite it to a ternary operator.

### YAML

```yaml
id: do-what-brooooooklyn-said
language: Tsx
rule:
  kind: jsx_expression
  has:
    pattern: $A && $B
  not:
    inside:
      kind: jsx_attribute
fix: "{$A ? $B : null}"
```

### Example

```tsx {1}
<div>{ list.length && list.map(i => <p/>) }</div>
```

### Diff

```tsx
<div>{ list.length && list.map(i => <p/>) }</div> // [!code --]
<div>{ list.length ?  list.map(i => <p/>) : null }</div> // [!code ++]
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim), inspired by [@Brooooook\_lyn](https://twitter.com/Brooooook_lyn/status/1666637274757595141)

## Rewrite MobX Component Style&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6ImNvbnNvbGUubG9nKCRNQVRDSCkiLCJyZXdyaXRlIjoibG9nZ2VyLmxvZygkTUFUQ0gpIiwiY29uZmlnIjoicnVsZTpcbiAgcGF0dGVybjogZXhwb3J0IGNvbnN0ICRDT01QID0gb2JzZXJ2ZXIoJEZVTkMpXG5maXg6IHwtXG4gIGNvbnN0IEJhc2UkQ09NUCA9ICRGVU5DXG4gIGV4cG9ydCBjb25zdCAkQ09NUCA9IG9ic2VydmVyKEJhc2UkQ09NUCkiLCJzb3VyY2UiOiJleHBvcnQgY29uc3QgRXhhbXBsZSA9IG9ic2VydmVyKCgpID0+IHtcbiAgcmV0dXJuIDxkaXY+SGVsbG8gV29ybGQ8L2Rpdj5cbn0pIn0=)

### Description

React and MobX are libraries that help us build user interfaces with JavaScript.

[React hooks](https://react.dev/reference/react) allow us to use state and lifecycle methods in functional components. But we need follow some hook rules, or React may break. [MobX](https://mobx.js.org/react-integration.html) has an `observer` function that makes a component update when data changes.

When we use the `observer` function like this:

```JavaScript
export const Example = observer(() => {…})
```

ESLint, the tool that checks hooks, thinks that `Example` is not a React component, but just a regular function. So it does not check the hooks inside it, and we may miss some wrong usages.

To fix this, we need to change our component style to this:

```JavaScript
const BaseExample = () => {…}
const Example = observer(BaseExample)
```

Now ESLint can see that `BaseExample` is a React component, and it can check the hooks inside it.

### YAML

```yaml
id: rewrite-mobx-component
language: typescript
rule:
  pattern: export const $COMP = observer($FUNC)
fix: |-
  const Base$COMP = $FUNC
  export const $COMP = observer(Base$COMP)
```

### Example

```js {1-3}
export const Example = observer(() => {
  return <div>Hello World</div>
})
```

### Diff

```js
export const Example = observer(() => { // [!code --]
  return <div>Hello World</div>         // [!code --]
})                                      // [!code --]
const BaseExample = () => {             // [!code ++]
  return <div>Hello World</div>         // [!code ++]
}                                       // [!code ++]
export const Example = observer(BaseExample) // [!code ++]
```

### Contributed by

[Bryan Lee](https://twitter.com/meetliby/status/1698601672568901723)

## Avoid Unnecessary React Hook

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6ImphdmFzY3JpcHQiLCJxdWVyeSI6IiIsInJld3JpdGUiOiIiLCJzdHJpY3RuZXNzIjoic21hcnQiLCJzZWxlY3RvciI6IiIsImNvbmZpZyI6InV0aWxzOlxuICBob29rX2NhbGw6XG4gICAgaGFzOlxuICAgICAga2luZDogY2FsbF9leHByZXNzaW9uXG4gICAgICByZWdleDogXnVzZVxuICAgICAgc3RvcEJ5OiBlbmRcbnJ1bGU6XG4gIGFueTpcbiAgLSBwYXR0ZXJuOiBmdW5jdGlvbiAkRlVOQygkJCQpIHsgJCQkIH1cbiAgLSBwYXR0ZXJuOiBsZXQgJEZVTkMgPSAoJCQkKSA9PiAkJCQgXG4gIC0gcGF0dGVybjogY29uc3QgJEZVTkMgPSAoJCQkKSA9PiAkJCRcbiAgaGFzOlxuICAgIHBhdHRlcm46ICRCT0RZXG4gICAga2luZDogc3RhdGVtZW50X2Jsb2NrXG4gICAgc3RvcEJ5OiBlbmQgXG5jb25zdHJhaW50czpcbiAgRlVOQzoge3JlZ2V4OiBedXNlIH1cbiAgQk9EWTogeyBub3Q6IHsgbWF0Y2hlczogaG9va19jYWxsIH0gfSBcbiIsInNvdXJjZSI6ImZ1bmN0aW9uIHVzZUlBbU5vdEhvb2tBY3R1YWxseShhcmdzKSB7XG4gICAgY29uc29sZS5sb2coJ0NhbGxlZCBpbiBSZWFjdCBidXQgSSBkb250IG5lZWQgdG8gYmUgYSBob29rJylcbiAgICByZXR1cm4gYXJncy5sZW5ndGhcbn1cbmNvbnN0IHVzZUlBbU5vdEhvb2tUb28gPSAoLi4uYXJncykgPT4ge1xuICAgIGNvbnNvbGUubG9nKCdDYWxsZWQgaW4gUmVhY3QgYnV0IEkgZG9udCBuZWVkIHRvIGJlIGEgaG9vaycpXG4gICAgcmV0dXJuIGFyZ3MubGVuZ3RoXG59XG5cbmZ1bmN0aW9uIHVzZUhvb2soKSB7XG4gICAgdXNlRWZmZWN0KCgpID0+IHtcbiAgICAgIGNvbnNvbGUubG9nKCdSZWFsIGhvb2snKSAgIFxuICAgIH0pXG59In0=)

### Description

React hook is a powerful feature in React that allows you to use state and other React features in a functional component.

However, you should avoid using hooks when you don't need them. If the code does not contain using any other React hooks,
it can be rewritten to a plain function. This can help to separate your application logic from the React-specific UI logic.

### YAML

```yaml
id: unnecessary-react-hook
language: Tsx
utils:
  hook_call:
    has:
      kind: call_expression
      regex: ^use
      stopBy: end
rule:
  any:
  - pattern: function $FUNC($$$) { $$$ }
  - pattern: let $FUNC = ($$$) => $$$
  - pattern: const $FUNC = ($$$) => $$$
  has:
    pattern: $BODY
    kind: statement_block
    stopBy: end
constraints:
  FUNC: {regex: ^use }
  BODY: { not: { matches: hook_call } }
```

### Example

```tsx {1-8}
function useIAmNotHookActually(args) {
    console.log('Called in React but I dont need to be a hook')
    return args.length
}
const useIAmNotHookToo = (...args) => {
    console.log('Called in React but I dont need to be a hook')
    return args.length
}

function useTrueHook() {
    useEffect(() => {
      console.log('Real hook')
    })
}
```

### Contributed by

[Herrington Darkholme](https://twitter.com/hd_nvim)

## Reverse React Compiler™&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InRzeCIsInF1ZXJ5IjoiIiwicmV3cml0ZSI6IiIsInN0cmljdG5lc3MiOiJyZWxheGVkIiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogcmV3cml0ZS1jYWNoZSBcbmxhbmd1YWdlOiB0c3hcbnJ1bGU6XG4gIGFueTpcbiAgLSBwYXR0ZXJuOiB1c2VDYWxsYmFjaygkRk4sICQkJClcbiAgLSBwYXR0ZXJuOiBtZW1vKCRGTiwgJCQkKVxuZml4OiAkRk5cblxuLS0tXG5cbmlkOiByZXdyaXRlLXVzZS1tZW1vXG5sYW5ndWFnZTogdHN4XG5ydWxlOiB7IHBhdHRlcm46ICd1c2VNZW1vKCRGTiwgJCQkKScgfVxuZml4OiAoJEZOKSgpIiwic291cmNlIjoiY29uc3QgQ29tcG9uZW50ID0gKCkgPT4ge1xuICBjb25zdCBbY291bnQsIHNldENvdW50XSA9IHVzZVN0YXRlKDApXG4gIGNvbnN0IGluY3JlbWVudCA9IHVzZUNhbGxiYWNrKCgpID0+IHtcbiAgICBzZXRDb3VudCgocHJldkNvdW50KSA9PiBwcmV2Q291bnQgKyAxKVxuICB9LCBbXSlcbiAgY29uc3QgZXhwZW5zaXZlQ2FsY3VsYXRpb24gPSB1c2VNZW1vKCgpID0+IHtcbiAgICAvLyBtb2NrIEV4cGVuc2l2ZSBjYWxjdWxhdGlvblxuICAgIHJldHVybiBjb3VudCAqIDJcbiAgfSwgW2NvdW50XSlcblxuICByZXR1cm4gKFxuICAgIDw+XG4gICAgICA8cD5FeHBlbnNpdmUgUmVzdWx0OiB7ZXhwZW5zaXZlQ2FsY3VsYXRpb259PC9wPlxuICAgICAgPGJ1dHRvbiBvbkNsaWNrPXtpbmNyZW1lbnR9Pntjb3VudH08L2J1dHRvbj5cbiAgICA8Lz5cbiAgKVxufSJ9)

### Description

React Compiler is a build-time only tool that automatically optimizes your React app, working with plain JavaScript and understanding the Rules of React without requiring a rewrite. It optimizes apps by automatically memoizing code, similar to `useMemo`, `useCallback`, and `React.memo`, reducing unnecessary recomputation due to incorrect or forgotten memoization.

Reverse React Compiler™ is a [parody tweet](https://x.com/aidenybai/status/1881397529369034997) that works in the opposite direction. It takes React code and removes memoization,  guaranteed to make your code slower. ([not](https://x.com/kentcdodds/status/1881404373646880997) [necessarily](https://dev.to/prathamisonline/are-you-over-using-usememo-and-usecallback-hooks-in-react-5lp))

It is originally written in Babel and this is an [ast-grep version](https://x.com/hd_nvim/status/1881402678493970620) of it.

:::details The Original Babel Implementation
For comparison purposes only. Note the original code [does not correctly rewrite](https://x.com/hd_nvim/status/1881404893136896415) `useMemo`.

```js
const ReverseReactCompiler = ({ types: t }) => ({
  visitor: {
    CallExpression(path) {
      const callee = path.node.callee;
      if (
        t.isIdentifier(callee, { name: "useMemo" }) ||
        t.isIdentifier(callee, { name: "useCallback" }) ||
        t.isIdentifier(callee, { name: "memo" })
      ) {
        path.replaceWith(args[0]);
      }
    },
  },
});
```

:::

### YAML

```yaml
id: rewrite-cache
language: tsx
rule:
  any:
  - pattern: useCallback($FN, $$$)
  - pattern: memo($FN, $$$)
fix: $FN
---
id: rewrite-use-memo
language: tsx
rule: { pattern: 'useMemo($FN, $$$)' }
fix: ($FN)()   # need IIFE to wrap memo function
```

### Example

```tsx {3-5,6-9}
const Component = () => {
  const [count, setCount] = useState(0)
  const increment = useCallback(() => {
    setCount((prevCount) => prevCount + 1)
  }, [])
  const expensiveCalculation = useMemo(() => {
    // mock Expensive calculation
    return count * 2
  }, [count])

  return (
    <>
      <p>Expensive Result: {expensiveCalculation}</p>
      <button onClick={increment}>{count}</button>
    </>
  )
}
```

### Diff

```tsx
const Component = () => {
  const [count, setCount] = useState(0)
  const increment = useCallback(() => {     // [!code --]
    setCount((prevCount) => prevCount + 1)  // [!code --]
  }, [])                                 // [!code --]
  const increment = () => {         // [!code ++]
    setCount((prevCount) => prevCount + 1) // [!code ++]
  } // [!code ++]
  const expensiveCalculation = useMemo(() => { // [!code --]
    // mock Expensive calculation             // [!code --]
    return count * 2                        // [!code --]
  }, [count])                             // [!code --]
  const expensiveCalculation = (() => { // [!code ++]
    // mock Expensive calculation      // [!code ++]
    return count * 2                 // [!code ++]
  })()                            // [!code ++]
  return (
    <>
      <p>Expensive Result: {expensiveCalculation}</p>
      <button onClick={increment}>{count}</button>
    </>
  )
}
```

### Contributed by

Inspired by [Aiden Bai](https://twitter.com/aidenybai)

## Avoid nested links

* [Playground Link](https://ast-grep.github.io/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InRzeCIsInF1ZXJ5IjoiaWYgKCRBKSB7ICQkJEIgfSIsInJld3JpdGUiOiJpZiAoISgkQSkpIHtcbiAgICByZXR1cm47XG59XG4kJCRCIiwic3RyaWN0bmVzcyI6InNtYXJ0Iiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogbm8tbmVzdGVkLWxpbmtzXG5sYW5ndWFnZTogdHN4XG5zZXZlcml0eTogZXJyb3JcbnJ1bGU6XG4gIHBhdHRlcm46IDxhICQkJD4kJCRBPC9hPlxuICBoYXM6XG4gICAgcGF0dGVybjogPGEgJCQkPiQkJDwvYT5cbiAgICBzdG9wQnk6IGVuZCIsInNvdXJjZSI6ImZ1bmN0aW9uIENvbXBvbmVudCgpIHtcbiAgcmV0dXJuIDxhIGhyZWY9Jy9kZXN0aW5hdGlvbic+XG4gICAgPGEgaHJlZj0nL2Fub3RoZXJkZXN0aW5hdGlvbic+TmVzdGVkIGxpbmshPC9hPlxuICA8L2E+O1xufVxuZnVuY3Rpb24gT2theUNvbXBvbmVudCgpIHtcbiAgcmV0dXJuIDxhIGhyZWY9Jy9kZXN0aW5hdGlvbic+XG4gICAgSSBhbSBqdXN0IGEgbGluay5cbiAgPC9hPjtcbn0ifQ==)

### Description

React will produce a warning message if you nest a link element inside of another link element. This rule will catch this mistake!

### YAML

```yaml
id: no-nested-links
language: tsx
severity: error
rule:
  pattern: <a $$$>$$$A</a>
  has:
    pattern: <a $$$>$$$</a>
    stopBy: end
```

### Example

```tsx {1-5}
function Component() {
  return <a href='/destination'>
    <a href='/anotherdestination'>Nested link!</a>
  </a>;
}
function OkayComponent() {
  return <a href='/destination'>
    I am just a link.
  </a>;
}
```

### Contributed by

[Tom MacWright](https://macwright.com/)

## Rename SVG Attribute&#x20;

* [Playground Link](/playground.html#eyJtb2RlIjoiQ29uZmlnIiwibGFuZyI6InRzeCIsInF1ZXJ5IjoiIiwicmV3cml0ZSI6IiIsInN0cmljdG5lc3MiOiJyZWxheGVkIiwic2VsZWN0b3IiOiIiLCJjb25maWciOiJpZDogcmV3cml0ZS1zdmctYXR0cmlidXRlXG5sYW5ndWFnZTogdHN4XG5ydWxlOlxuICBwYXR0ZXJuOiAkUFJPUFxuICByZWdleDogKFthLXpdKyktKFthLXpdKVxuICBraW5kOiBwcm9wZXJ0eV9pZGVudGlmaWVyXG4gIGluc2lkZTpcbiAgICBraW5kOiBqc3hfYXR0cmlidXRlXG50cmFuc2Zvcm06XG4gIE5FV19QUk9QOlxuICAgIGNvbnZlcnQ6XG4gICAgICBzb3VyY2U6ICRQUk9QXG4gICAgICB0b0Nhc2U6IGNhbWVsQ2FzZVxuZml4OiAkTkVXX1BST1AiLCJzb3VyY2UiOiJjb25zdCBlbGVtZW50ID0gKFxuICA8c3ZnIHdpZHRoPVwiMTAwXCIgaGVpZ2h0PVwiMTAwXCIgdmlld0JveD1cIjAgMCAxMDAgMTAwXCI+XG4gICAgPHBhdGggZD1cIk0xMCAyMCBMMzAgNDBcIiBzdHJva2UtbGluZWNhcD1cInJvdW5kXCIgZmlsbC1vcGFjaXR5PVwiMC41XCIgLz5cbiAgPC9zdmc+XG4pIn0=)

### Description

[SVG](https://en.wikipedia.org/wiki/SVG)(Scalable Vector Graphics)s' hyphenated names are not compatible with JSX syntax in React. JSX requires [camelCase naming](https://react.dev/learn/writing-markup-with-jsx#3-camelcase-salls-most-of-the-things) for attributes.
For example, an SVG attribute like `stroke-linecap` needs to be renamed to `strokeLinecap` to work correctly in React.

### YAML

```yaml
id: rewrite-svg-attribute
language: tsx
rule:
  pattern: $PROP            # capture in metavar
  regex: ([a-z]+)-([a-z])   # hyphenated name
  kind: property_identifier
  inside:
    kind: jsx_attribute     # in JSX attribute
transform:
  NEW_PROP:                 # new property name
    convert:                # use ast-grep's convert
      source: $PROP
      toCase: camelCase     # to camelCase naming
fix: $NEW_PROP
```

### Example

```tsx {3}
const element = (
  <svg width="100" height="100" viewBox="0 0 100 100">
    <path d="M10 20 L30 40" stroke-linecap="round" fill-opacity="0.5" />
  </svg>
)
```

### Diff

```ts
const element = (
  <svg width="100" height="100" viewBox="0 0 100 100">
    <path d="M10 20 L30 40" stroke-linecap="round" fill-opacity="0.5" /> // [!code --]
    <path d="M10 20 L30 40" strokeLinecap="round" fillOpacity="0.5" />   // [!code ++]
  </svg>
)
```

### Contributed by

Inspired by [SVG Renamer](https://admondtamang.medium.com/introducing-svg-renamer-your-solution-for-react-svg-attributes-26503382d5a8)
