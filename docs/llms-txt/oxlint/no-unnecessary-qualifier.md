# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/no-unnecessary-qualifier.md

---
url: /docs/guide/usage/linter/rules/typescript/no-unnecessary-qualifier.md
---

### What it does

Disallow namespace qualifiers when the referenced name is already in scope.

### Why is this bad?

Redundant qualifiers add noise and make type references harder to read.

### Examples

Examples of **incorrect** code for this rule:

```ts
namespace A {
  export type B = number;
  const value: A.B = 1;
}
```

Examples of **correct** code for this rule:

```ts
namespace A {
  export type B = number;
  const value: B = 1;
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/no-unnecessary-qualifier": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/no-unnecessary-qualifier
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
