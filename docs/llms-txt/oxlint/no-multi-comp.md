# Source: https://oxc.rs/docs/guide/usage/linter/rules/react/no-multi-comp.md

---
url: /docs/guide/usage/linter/rules/react/no-multi-comp.md
---

### What it does

Prevents multiple React components from being defined in the same file.

### Why is this bad?

Declaring multiple components in a single file can make it harder to navigate
and maintain the codebase. Each component should ideally be in its own file
for better organization and reusability.

### Examples

Examples of **incorrect** code for this rule:

```jsx
function Foo({ name }) {
  return <div>Hello {name}</div>;
}

function Bar({ name }) {
  return <div>Hello again {name}</div>;
}
```

Examples of **correct** code for this rule:

```jsx
function Foo({ name }) {
  return <div>Hello {name}</div>;
}
```

## Configuration

### ignoreStateless

type: `boolean`

default: `false`

When `true`, the rule will ignore stateless components and will allow you to have multiple
stateless components in the same file. Or one stateful component and one-or-more stateless
components in the same file.

Stateless basically just means function components, including those created via
`memo` and `forwardRef`.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["react"],
  "rules": {
    "react/no-multi-comp": "error"
  }
}
```

```bash [CLI]
oxlint --deny react/no-multi-comp --react-plugin
```

:::

## References

* Rule Source
