# Source: https://oxc.rs/docs/guide/usage/linter/rules/unicorn/relative-url-style.md

---
url: /docs/guide/usage/linter/rules/unicorn/relative-url-style.md
---

### What it does

Enforce consistent relative URL style.

### Why is this bad?

When using a relative URL in `new URL()`, the URL should either never or always use the `./` prefix consistently.

### Examples

Examples of **incorrect** code for this rule with the default `"never"` option:

```js
new URL("./foo", base);
```

Examples of **correct** code for this rule with the default `"never"` option:

```js
new URL("foo", base);
```

Examples of **incorrect** code for this rule with the `"always"` option:

```js
new URL("foo", base);
```

Examples of **correct** code for this rule with the `"always"` option:

```js
new URL("./foo", base);
```

## Configuration

This rule accepts one of the following string values:

### `"never"`

Never use a `./` prefix.

### `"always"`

Always add a `./` prefix to the relative URL when possible.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "unicorn/relative-url-style": "error"
  }
}
```

```bash [CLI]
oxlint --deny unicorn/relative-url-style
```

:::

## References

* Rule Source
