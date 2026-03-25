# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/prefer-find.md

---
url: /docs/guide/usage/linter/rules/typescript/prefer-find.md
---

### What it does

Prefer `.find(...)` over `.filter(...)[0]` for retrieving a single element.

### Why is this bad?

`.filter(...)[0]` builds an intermediate array and is less clear about intent.
`.find(...)` directly expresses that only the first matching element is needed.

### Examples

Examples of **incorrect** code for this rule:

```ts
const first = list.filter((item) => item.active)[0];
```

Examples of **correct** code for this rule:

```ts
const first = list.find((item) => item.active);
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/prefer-find": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/prefer-find
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
