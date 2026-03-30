# Source: https://www.lucide.dev/guide/angular/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/react-native/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/preact/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/astro/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/solid/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/svelte/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/vue/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/react/advanced/with-lucide-lab.md

# Source: https://www.lucide.dev/guide/lucide/advanced/with-lucide-lab.md

---
url: /guide/lucide/advanced/with-lucide-lab.md
description: >-
  Learn how to use Lucide Lab or custom icons in your Vanilla JavaScript
  applications.
---

# With Lucide Lab or custom icons

[Lucide Lab](https://github.com/lucide-icons/lucide-lab) is a collection of icons that are not part of the Lucide main library.

They can be used by adding the `@lucide/lab` package to your project.
All props like regular lucide icons can be passed to adjust the icon appearance.

## Using Lucide Lab icons

This creates a single icon based on the iconNode passed and renders a Lucide icon component.

::: sandpack {template=vanilla editorHeight=295 editorWidthPercentage=60 dependencies="lucide,@lucide/lab"}

```html /index.html [active]
<!DOCTYPE html>
<html>
  <body>
    <i data-lucide="avocado"></i>

    <script src="index.js"></script>
  </body>
</html>
```

```js /index.js
import "./styles.css";

import { createIcons, Smile } from 'lucide/dist/cjs/lucide';
import { avocado as Avocado } from '@lucide/lab';

createIcons({
  icons: {
    Avocado,
  }
});

```

:::
