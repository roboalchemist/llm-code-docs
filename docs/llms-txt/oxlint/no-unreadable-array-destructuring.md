# Source: https://oxc.rs/docs/guide/usage/linter/rules/unicorn/no-unreadable-array-destructuring.md

---
url: /docs/guide/usage/linter/rules/unicorn/no-unreadable-array-destructuring.md
---

### What it does

Disallows destructuring values from an array in ways that are difficult to read.

### Why is this bad?

Destructuring can be very useful, but it can also make some code harder to read.
This rule prevents ignoring consecutive values (e.g. `let [,,foo] = array`)
when destructuring from an array.

### Examples

Examples of **incorrect** code for this rule:

```javascript
const [, , foo] = parts;
const [, , ...rest] = parts;
```

Examples of **correct** code for this rule:

```javascript
const [foo] = parts;
const foo = parts[3];
const rest = parts.slice(2);

// One is fine
const [, foo] = parts;
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "unicorn/no-unreadable-array-destructuring": "error"
  }
}
```

```bash [CLI]
oxlint --deny unicorn/no-unreadable-array-destructuring
```

:::

## References

* Rule Source
