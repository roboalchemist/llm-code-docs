# Source: https://oxc.rs/docs/guide/usage/linter/rules/unicorn/prefer-string-starts-ends-with.md

# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/prefer-string-starts-ends-with.md

---
url: /docs/guide/usage/linter/rules/typescript/prefer-string-starts-ends-with.md
---

### What it does

Prefer `startsWith` and `endsWith` over manual string boundary checks.

### Why is this bad?

Boundary checks written with `slice`, `indexOf`, regex anchors, or manual indexing are
harder to read and maintain than `startsWith`/`endsWith`.

### Examples

Examples of **incorrect** code for this rule:

```ts
value.slice(0, 3) === "foo";
value.slice(-3) === "bar";
```

Examples of **correct** code for this rule:

```ts
value.startsWith("foo");
value.endsWith("bar");
```

## Configuration

This rule accepts a configuration object with the following properties:

### allowSingleElementEquality

type: `"always" | "never"`

default: `null`

Whether equality checks against the first/last character are allowed.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/prefer-string-starts-ends-with": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/prefer-string-starts-ends-with
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
