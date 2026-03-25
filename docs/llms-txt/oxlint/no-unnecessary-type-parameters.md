# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/no-unnecessary-type-parameters.md

---
url: /docs/guide/usage/linter/rules/typescript/no-unnecessary-type-parameters.md
---

### What it does

Disallow type parameters that are declared but not meaningfully used.

### Why is this bad?

Unnecessary type parameters make signatures noisier and harder to understand, and they
often hide opportunities to simplify APIs.

### Examples

Examples of **incorrect** code for this rule:

```ts
function parseYAML<T>(input: string): T {
  return input as any as T;
}
```

Examples of **correct** code for this rule:

```ts
function parseYAML(input: string): unknown {
  return input;
}

function identity<T>(value: T): T {
  return value;
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/no-unnecessary-type-parameters": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/no-unnecessary-type-parameters
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
