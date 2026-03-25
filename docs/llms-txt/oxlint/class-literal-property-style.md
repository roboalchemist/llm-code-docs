# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/class-literal-property-style.md

---
url: /docs/guide/usage/linter/rules/typescript/class-literal-property-style.md
---

### What it does

Enforces a consistent style for exposing literal values on classes.

### Why is this bad?

Mixing readonly fields and trivial literal getters for the same kind of value
makes class APIs inconsistent and harder to scan.

### Examples

Examples of **incorrect** code for this rule (default `"fields"`):

```ts
class C {
  get name() {
    return "oxc";
  }
}
```

Examples of **correct** code for this rule:

```ts
class C {
  readonly name = "oxc";
}
```

## Configuration

This rule accepts one of the following string values:

type: `"fields" | "getters"`

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/class-literal-property-style": "error"
  }
}
```

```bash [CLI]
oxlint --deny typescript/class-literal-property-style
```

:::

## References

* Rule Source
