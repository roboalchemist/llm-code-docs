# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/prefer-regexp-exec.md

---
url: /docs/guide/usage/linter/rules/typescript/prefer-regexp-exec.md
---

### What it does

Prefer `RegExp#exec()` over `String#match()` when extracting a regex match.

### Why is this bad?

`exec()` is more explicit about matching with a regular expression and avoids the
overloaded behavior of `String#match()`.

### Examples

Examples of **incorrect** code for this rule:

```ts
const text = "value";
text.match(/v/);
```

Examples of **correct** code for this rule:

```ts
const text = "value";
/v/.exec(text);
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/prefer-regexp-exec": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/prefer-regexp-exec
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
