# Source: https://redocly.com/docs/realm/customization/react-components/wrap-components.md

# Customize theme components

To customize an existing theme component, you can override the component by mirroring the original import path.
Overriding a component ensures that the updated version is used consistently across the entire site.
This approach is especially useful for applying design updates or behavior changes across the entire documentation without modifying each usage manually.

Since components are imported directly from the theme, your replacement must follow the same file structure.

For example, if the component is imported like this:


```tsx
import Admonition from '@redocly/theme/components/Admonition/Admonition';
```

Place your custom component in the following structure:


```treeview
@theme/
âââ components/
    âââ Admonition/
        âââ Admonition.tsx
```

If the file structure matches the import path, the theme automatically uses your version of the component instead of the default one.

## Example


```tsx Admonition.tsx
import React from 'react';

import { Admonition as Original } from '@redocly/theme/components/Admonition/Admonition';

export const Admonition = (props) => {
  return <Original {...props} className="my-admonition" />;
};
```

Now, every time the `Admonition` component is used â whether on pages or in other components â the customized version renders automatically.

## Resources

- **[Components usage tutorial](/docs/realm/customization/react-components/use-in-react-page)** - Learn to use your customized components in React pages with practical examples and implementation patterns
- **[List of customizable components](/docs/realm/customization/react-components/list)** - Browse all available built-in React components that you can wrap, customize, and extend
- **[Customizable icons list](/docs/realm/customization/react-components/list/icons)** - Explore available icon components that you can customize and extend with your own styling and functionality