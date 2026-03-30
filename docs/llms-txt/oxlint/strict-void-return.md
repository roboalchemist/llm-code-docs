# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/strict-void-return.md

---
url: /docs/guide/usage/linter/rules/typescript/strict-void-return.md
---

### What it does

Disallow returning non-void values where a `void` return is expected.

### Why is this bad?

Returning values from `void` contexts can hide logic errors and make callback APIs
behave unexpectedly.

### Examples

Examples of **incorrect** code for this rule:

```ts
declare function run(cb: () => void): void;

run(() => "value");
run(async () => 123);
```

Examples of **correct** code for this rule:

```ts
declare function run(cb: () => void): void;

run(() => {
  doWork();
});

run(() => undefined);
```

## Configuration

This rule accepts a configuration object with the following properties:

### allowReturnAny

type: `boolean`

default: `false`

Allow callbacks that return `any` in places that expect a `void` callback.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/strict-void-return": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/strict-void-return
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
