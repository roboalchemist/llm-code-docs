# Source: https://oxc.rs/docs/guide/usage/linter/rules/vitest/prefer-expect-type-of.md

---
url: /docs/guide/usage/linter/rules/vitest/prefer-expect-type-of.md
---

### What it does

Enforce using `expectTypeOf` instead of `expect(typeof ...)`

### Why is this bad?

Vitest provide a more expressive type-safe way to test type than using `expect(typeof ...)`

### Examples

Examples of **incorrect** code for this rule:

```js
test('type checking', () => {
  expect(typeof 'hello').toBe('string')
  expect(typeof 42).toBe('number')
  expect(typeof true).toBe('boolean')
  expect(typeof {}).toBe('object')
  expect(typeof () => {}).toBe('function')
  expect(typeof Symbol()).toBe('symbol')
  expect(typeof 123n).toBe('bigint')
  expect(typeof undefined).toBe('undefined')
})
```

Examples of **correct** code for this rule:

```js
test("type checking", () => {
  expectTypeOf("hello").toBeString();
  expectTypeOf(42).toBeNumber();
  expectTypeOf(true).toBeBoolean();
  expectTypeOf({}).toBeObject();
  expectTypeOf(() => {}).toBeFunction();
  expectTypeOf(Symbol()).toBeSymbol();
  expectTypeOf(123n).toBeBigInt();
  expectTypeOf(undefined).toBeUndefined();
});
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["vitest"],
  "rules": {
    "vitest/prefer-expect-type-of": "error"
  }
}
```

```bash [CLI]
oxlint --deny vitest/prefer-expect-type-of --vitest-plugin
```

:::

## References

* Rule Source
