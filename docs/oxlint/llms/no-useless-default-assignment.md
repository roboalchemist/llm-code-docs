# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/no-useless-default-assignment.md

---
url: /docs/guide/usage/linter/rules/typescript/no-useless-default-assignment.md
---

### What it does

Disallow default assignments that can never be used.

### Why is this bad?

A default assignment is redundant when the value can never be `undefined`.
This adds runtime logic and noise without changing behavior.

### Examples

Examples of **incorrect** code for this rule:

```ts
[1, 2, 3].map((a = 0) => a + 1);
```

Examples of **correct** code for this rule:

```ts
[1, 2, 3].map((a) => a + 1);
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/no-useless-default-assignment": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/no-useless-default-assignment
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
