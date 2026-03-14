# Source: https://oxc.rs/docs/guide/usage/linter/rules/react/jsx-no-constructed-context-values.md

---
url: /docs/guide/usage/linter/rules/react/jsx-no-constructed-context-values.md
---

### What it does

Disallows JSX context provider values from taking values that will cause needless rerenders.

### Why is this bad?

React Context and all its child nodes and Consumers are rerendered whenever the value prop
changes. Because each JavaScript object carries its own identity, things like object
expressions (`{foo: 'bar'}`) or function expressions get a new identity on every render.
This makes the context think it has gotten a new object and can cause needless rerenders
and unintended consequences.

This can be a large performance hit because not only will it cause the context providers
and consumers to rerender with all the elements in its subtree, the processing for the
tree scan React does to render the provider and find consumers is also wasted.

### Examples

Examples of **incorrect** code for this rule:

```jsx
return <SomeContext.Provider value={{ foo: "bar" }}>...</SomeContext.Provider>;
```

```jsx
function Component() {
  function foo() {}
  return <MyContext.Provider value={foo} />;
}
```

Examples of **correct** code for this rule:

```jsx
const foo = useMemo(() => ({ foo: "bar" }), []);
return <SomeContext.Provider value={foo}>...</SomeContext.Provider>;
```

```jsx
const MyContext = createContext();
const Component = () => <MyContext.Provider value="Some string" />;
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["react"],
  "rules": {
    "react/jsx-no-constructed-context-values": "error"
  }
}
```

```bash [CLI]
oxlint --deny react/jsx-no-constructed-context-values --react-plugin
```

:::

## References

* Rule Source
