# Source: https://oxc.rs/docs/guide/usage/linter/rules/react/prefer-es6-class.md

---
url: /docs/guide/usage/linter/rules/react/prefer-es6-class.md
---

### What it does

React offers you two ways to create traditional components: using the
`create-react-class` package or the newer ES2015 class system.

Note that function components are preferred over class components in modern React,
and it is *especially* discouraged to use `createReactClass` in modern React.

### Why is this bad?

This rule enforces a consistent React class style.

### Examples

Examples of **incorrect** code for this rule by default:

```jsx
var Hello = createReactClass({
  render: function () {
    return <div>Hello {this.props.name}</div>;
  },
});
```

## Configuration

This rule accepts one of the following string values:

### `"always"`

Always prefer ES2015 class-style components.

### `"never"`

Do not allow ES2015 class-style, prefer `createReactClass`.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["react"],
  "rules": {
    "react/prefer-es6-class": "error"
  }
}
```

```bash [CLI]
oxlint --deny react/prefer-es6-class --react-plugin
```

:::

## References

* Rule Source
