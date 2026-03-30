# Source: https://oxc.rs/docs/guide/usage/linter/rules/eslint/no-unmodified-loop-condition.md

---
url: /docs/guide/usage/linter/rules/eslint/no-unmodified-loop-condition.md
---

### What it does

Disallow references in loop conditions that are never modified within the loop.

### Why is this bad?

A loop condition that depends on values that never change within the loop body
can cause infinite loops or logic bugs.

### Examples

Examples of **incorrect** code for this rule:

```js
let done = false;
while (!done) {
  work();
}
```

Examples of **correct** code for this rule:

```js
let done = false;
while (!done) {
  done = checkDone();
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "no-unmodified-loop-condition": "error"
  }
}
```

```bash [CLI]
oxlint --deny no-unmodified-loop-condition
```

:::

## References

* Rule Source
