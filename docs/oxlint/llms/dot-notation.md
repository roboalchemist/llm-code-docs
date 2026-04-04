# Source: https://oxc.rs/docs/guide/usage/linter/rules/typescript/dot-notation.md

---
url: /docs/guide/usage/linter/rules/typescript/dot-notation.md
---

### What it does

Enforce dot notation whenever property access can be written safely as `obj.prop`.

### Why is this bad?

Dot notation is generally more readable and concise than bracket notation for static
property names.

### Examples

Examples of **incorrect** code for this rule:

```ts
obj["name"];
foo["bar"];
```

Examples of **correct** code for this rule:

```ts
obj.name;
foo.bar;

obj[key];
obj["not-an-identifier"];
```

## Configuration

This rule accepts a configuration object with the following properties:

### allowIndexSignaturePropertyAccess

type: `boolean`

default: `false`

Allow bracket notation for properties covered by an index signature.

### allowKeywords

type: `boolean`

default: `true`

Allow bracket notation for ES3 keyword property names (for example `obj["class"]`).

### allowPattern

type: `string`

default: `""`

Regex pattern for property names that are allowed to use bracket notation.

### allowPrivateClassPropertyAccess

type: `boolean`

default: `false`

Allow bracket notation for private class members.

### allowProtectedClassPropertyAccess

type: `boolean`

default: `false`

Allow bracket notation for protected class members.

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "rules": {
    "typescript/dot-notation": "error"
  }
}
```

```bash [CLI]
oxlint --type-aware --deny typescript/dot-notation
```

:::

## References

* Rule Source
* Rule Source (tsgolint)
