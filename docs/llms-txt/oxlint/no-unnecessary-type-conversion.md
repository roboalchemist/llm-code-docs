# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/no-unnecessary-type-conversion.md

---
url: /docs/guide/usage/linter/rules/typescript/no-unnecessary-type-conversion.md
---

### What it does

Disallow unnecessary type conversion expressions.

### Why is this bad?

Type conversions that do not change a value's type or runtime behavior
add noise and can obscure intent.

### Examples

Examples of **incorrect** code for this rule:

```ts
const value = String("asdf");
```

Examples of **correct** code for this rule:

```ts
const value = "asdf";
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/no-unnecessary-type-conversion": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/no-unnecessary-type-conversion
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
