# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/consistent-return.md

---
url: /docs/guide/usage/linter/rules/typescript/consistent-return.md
---

### What it does

Enforce consistent return behavior in functions.

### Why is this bad?

Mixing value-returning and non-value-returning code paths makes control flow harder to
reason about and frequently indicates a bug.

### Examples

Examples of **incorrect** code for this rule:

```ts
function maybe(flag: boolean): number {
  if (flag) {
    return 1;
  }
  return;
}
```

Examples of **correct** code for this rule:

```ts
function maybe(flag: boolean): number {
  if (flag) {
    return 1;
  }
  return 0;
}
```

## Configuration

This rule accepts a configuration object with the following properties:

### treatUndefinedAsUnspecified

type: `boolean`

default: `false`

Treat explicit `return undefined` as equivalent to an unspecified return.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/consistent-return": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/consistent-return
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
