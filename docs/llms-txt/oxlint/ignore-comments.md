# Source: https://oxc.rs/docs/guide/usage/linter/ignore-comments.md

# Source: https://oxc.rs/docs/guide/usage/formatter/ignore-comments.md

---
url: /docs/guide/usage/formatter/ignore-comments.md
---
# Inline ignore comments

For JS/TS files, use `oxfmt-ignore` to skip formatting the next statement:

```js
// oxfmt-ignore
const a    = 42;

/* oxfmt-ignore */
const x = () => { return 2; };

<>
  {/* oxfmt-ignore */}
  <span   ugly   format=""   />
</>;
```

For JS-in-Vue, use `oxfmt-ignore` inside the `<script>` tag:

```vue
<script>
// oxfmt-ignore
const a    = 42;
</script>
```

Trailing ignore comments are also supported:

```js
const a    = 42; // oxfmt-ignore
```

For other files and non-JS parts of Vue files (e.g., `<template>`, `<style>`), use `prettier-ignore` comment. See also Prettier's [ignore documentation](https://prettier.io/docs/ignore#html).

Currently, TOML files do not support ignore comments.

## Prettier compatibility

* `prettier-ignore` comment is also supported
