# Source: https://oxc.rs/docs/guide/usage/linter/rules/jsx_a11y/no-redundant-roles.md

---
url: /docs/guide/usage/linter/rules/jsx_a11y/no-redundant-roles.md
---

### What it does

Enforces that code does not include a redundant `role` property, in the
case that it's identical to the implicit `role` property of the
element type.

### Why is this bad?

Redundant roles can lead to confusion and verbosity in the codebase.

### Examples

This rule applies for the following elements and their implicit roles:

* `<nav>`: `navigation`
* `<button>`: `button`
* `<body>`: `document`

Examples of **incorrect** code for this rule:

```jsx
<nav role="navigation"></nav>
<button role="button"></button>
<body role="document"></body>
```

Examples of **correct** code for this rule:

```jsx
<nav></nav>
<button></button>
<body></body>
```

## How to use

To **enable** this rule using the config file or in the CLI, you can use:

::: code-group

```json [Config (.oxlintrc.json)]
{
  "plugins": ["jsx-a11y"],
  "rules": {
    "jsx-a11y/no-redundant-roles": "error"
  }
}
```

```bash [CLI]
oxlint --deny jsx-a11y/no-redundant-roles --jsx-a11y-plugin
```

:::

## References

* Rule Source
