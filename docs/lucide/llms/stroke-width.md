# Source: https://www.lucide.dev/guide/angular/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/react-native/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/preact/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/astro/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/solid/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/svelte/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/vue/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/react/basics/stroke-width.md

# Source: https://www.lucide.dev/guide/lucide/basics/stroke-width.md

---
url: /guide/lucide/basics/stroke-width.md
description: >-
  Learn how to customize the stroke width of Lucide icons in your Vanilla
  JavaScript applications using the strokeWidth and absoluteStrokeWidth
  attributes.
---

# Stroke width

All icons are designed with SVG elements using strokes.
These have a default stroke width of `2px`.

The `strokeWidth` can be adjusted to create a different look of the icons.

## Adjusting stroke width with `strokeWidth` prop

::: sandpack {template=vanilla showTabs=false editorHeight=250 editorWidthPercentage=70 dependencies="lucide"}

```html /index.html [active]
<!DOCTYPE html>
<html>
  <body>
    <i data-lucide="folder-lock" stroke-width="1"></i>

    <script src="index.js"></script>
  </body>
</html>
```

```js /index.js
import "./styles.css";

import { createIcons, FolderLock } from 'lucide/dist/cjs/lucide';

createIcons({
  icons: {
    FolderLock,
  }
});

```

:::
