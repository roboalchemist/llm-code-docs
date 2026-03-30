# Source: https://oxc.rs/docs/guide/usage/linter/rules/jest/no-unneeded-async-expect-function.md

---
url: /docs/guide/usage/linter/rules/jest/no-unneeded-async-expect-function.md
---

### What it does

Disallows unnecessary async function wrapper for expected promises.

### Why is this bad?

When the only statement inside an async wrapper is `await someCall()`,
the call should be passed directly to `expect` instead. This makes the
test code more concise and easier to read.

### Examples

Examples of **incorrect** code for this rule:

```js
await expect(async () => {
  await doSomethingAsync();
}).rejects.toThrow();

await expect(async () => await doSomethingAsync()).rejects.toThrow();
```

Examples of **correct** code for this rule:

```js
await expect(doSomethingAsync()).rejects.toThrow();
```

This rule is compatible with [eslint-plugin-vitest](https://github.com/vitest-dev/eslint-plugin-vitest/blob/main/docs/rules/no-unneeded-async-expect-function.md),
to use it, add the following configuration to your `.oxlintrc.json`:

```json
{
  "rules": {
    "vitest/no-unneeded-async-expect-function": "error"
  }
}
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["jest"],
  "rules": {
    "jest/no-unneeded-async-expect-function": "error"
  }
}
```

```bash [CLI]
oxlint --deny jest/no-unneeded-async-expect-function --jest-plugin
```

:::

## References

* Rule Source
