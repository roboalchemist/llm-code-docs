# UnoCSS Documentation
# Source: https://raw.githubusercontent.com/unocss/unocss/main/docs/config/preflights.md
# Path: docs/config/preflights.md

---
title: Preflights
description: You can inject raw CSS as preflights from the configuration. The resolved theme is available to customize the CSS.
---

# Preflights

You can inject raw CSS as preflights from the configuration. The resolved `theme` is available to customize the CSS.

<!--eslint-skip-->

```ts
preflights: [
  {
    getCSS: ({ theme }) => `
      * {
        color: ${theme.colors.gray?.[700] ?? '#333'};
        padding: 0;
        margin: 0;
      }
    `,
  },
]
```
