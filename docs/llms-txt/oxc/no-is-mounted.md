# Source: https://oxc.rs/docs/guide/usage/linter/rules/react/no-is-mounted.md

---
url: /docs/guide/usage/linter/rules/react/no-is-mounted.md
---

### What it does

This rule prevents using `isMounted` in class components.

### Why is this bad?

`isMounted` is an anti-pattern, and is not available
when using classes or function components.

### Examples

Examples of **incorrect** code for this rule:

```jsx
class Hello extends React.Component {
  someMethod() {
    if (!this.isMounted()) {
      return;
    }
  }
  render() {
    return <div onClick={this.someMethod.bind(this)}>Hello</div>;
  }
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["react"],
  "rules": {
    "react/no-is-mounted": "error"
  }
}
```

```bash [CLI]
oxlint --deny react/no-is-mounted --react-plugin
```

:::

## References

* Rule Source
