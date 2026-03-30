# Source: https://developers.webflow.com/devlink/usage/styling-and-theming-overrides.mdx

***

title: Styling and Theming
slug: devlink/usage/styling-and-theming-overrides
description: >-
How to override DevLink component styles using CSS Modules, global CSS
imports, and advanced configuration.
------------------------------------

DevLink exports your Webflow styles as CSS, giving you full control over how components look in your React application. You can maintain design consistency while adding custom theming, responsive behavior, and component variants.

<Warning title="Never edit the generated files">
  Never edit the auto-generated React files or CSS Modules inside your `/devlink` folder. They will be overwritten on the next sync. Always extend or override styles externally.
</Warning>

## Global CSS setup

DevLink generates a `global.css` file containing base styles, responsive breakpoints, and CSS variables from your Webflow project. Import it once at your app's root to apply Webflow's design system globally:

```tsx title="app/layout.tsx"
import "@/devlink/global.css";
```

## Override with CSS modules

The safest way to customize DevLink components is by attaching your own CSS Module classes via the `className` prop. This approach preserves Webflow's original styles while adding your customizations:

<CodeBlocks>
  ```tsx title="CustomStyles.module.css"
  .fancyButton {
    border-radius: 8px;
    padding: 1rem 2rem;
  }
  ```

  ```tsx title="Page.tsx"
  import overrides from "./CustomStyles.module.css";
  import { Button } from "@/devlink";

  export function Page() {
    return <Button className={overrides.fancyButton}>Click me</Button>;
  }
  ```
</CodeBlocks>

## Reuse Webflow classes and variables

DevLink exports your Webflow project's class names and CSS variables, enabling you to build custom components that match your design system. This approach is ideal for components with dynamic data or complex interactions that you wouldn't build in Webflow:

**Custom-built React component:**

<CodeBlocks>
  ```tsx title="ProductCard.tsx"
  import "./ProductCard.module.css";

  interface ProductCardProps {
    product: {
      id: string;
      name: string;
      price: number;
      image: string;
    };
    onAddToCart: (productId: string) => void;
  }

  export function ProductCard({ product, onAddToCart }: ProductCardProps) {
    return (
      <div className="webflow-card">
        <img
          src={product.image}
          alt={product.name}
          className="webflow-card-image"
        />
        <div className="webflow-card-content">
          <h3 className="webflow-heading-small">{product.name}</h3>
          <p className="webflow-text-large">${product.price}</p>
          <button
            className="webflow-button-primary"
            onClick={() => onAddToCart(product.id)}
          >
            Add to Cart
          </button>
        </div>
      </div>
    );
  }
  ```

  ```css title="ProductCard.module.css"
  .webflow-card {
    background-color: var(--color-neutral-100);
    border-radius: var(--border-radius-medium);
    padding: var(--spacing-medium);
  }

  .webflow-card-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: var(--border-radius-small);
  }

  .webflow-card-content {
    margin-top: var(--spacing-small);
  }

  ```
</CodeBlocks>

Additionally, you can reuse component classes from your Webflow project in your custom-built React components, by importing the CSS module into your custom component styles.

## Custom Identifiers

DevLink automatically transforms **custom IDs** into safe, namespaced selectors using CSS Modules, preventing style conflicts when components are used in larger React apps.

Custom IDs are transformed into the following format:

```
<ComponentName>_<custom-id>__<unique-identifier>

```

For example, a custom ID of `featured-section` on a **Grid** element within a `Hero` component may become: `Hero_featured-section__abc123`

Use attribute selectors with wildcards to style elements reliably:

<CodeBlocks>
  ```css title="CustomStyles.module.css"
  /* Target elements with custom IDs */
  [id*="ProductGrid_featured-section__"] {
    background-color: var(--color-accent);
    padding: var(--spacing-large);
  }

  /* Target elements with custom attributes */
  [data-category="electronics"] {
    border: 2px solid var(--color-primary);
  }

  [data-product-count] {
    position: relative;
  }
  ```

  ```tsx title="ProductGrid.tsx"
  import { Grid } from "@/devlink/Grid";
  import styles from "./CustomStyles.module.css";

  export function ProductGrid({ products, category }: ProductGridProps) {
    return (
      <Grid
        id="featured-section" // Custom ID for styling hooks
        data-category={category} // Custom attribute for conditional styling
        data-product-count={products.length}
        className={styles.productGrid}
      >
        {/* Grid content */}
      </Grid>
    );
  }
  ```
</CodeBlocks>

### Avoid dynamic IDs

Some Webflow elements (like Grid or Quick Stack) rely on fixed IDs for CSS. If you replace them dynamically in React, the exported CSS will no longer apply. Instead, use custom attributes to keep Webflow’s styling intact while allowing you to attach your own identifier.

<Warning title="Don't do this">
  ```jsx
  // ❌ This breaks Webflow’s generated CSS
  <Grid id={sectionId} />
  ```
</Warning>

<Tip title="Use custom attributes instead">
  ```jsx dashboard.jsx
  // ✅ Use custom attributes instead
  <Grid
    data-section-id={sectionId}
  />
  ```
</Tip>

## CSS-in-JS integration

If your project uses styled-components or emotion, you can wrap DevLink components with styled overrides. This approach works well for component variants and theme-based styling:

```tsx title="Dashboard.tsx"
import styled from "styled-components";
import { Button } from "@/devlink";

const DangerButton = styled(Button)`
  background-color: red;
  border-radius: 4px;
  color: white;
`;

<DangerButton>Delete</DangerButton>
```

## Tailwind CSS integration

### Prevent style conflicts

To avoid conflicts between DevLink's global styles and Tailwind's reset, enable `skipTagSelectors` in your DevLink configuration:

<CodeBlocks>
  ```json title="webflow.json"
  {
    "devlink": {
      "skipTagSelectors": true
    }
  }
  ```

  ```javascript title=".webflowrc.js"
  module.exports = {
    skipTagSelectors: true
  }
  ```
</CodeBlocks>

### Control style priority

To give DevLink styles higher priority over Tailwind's reset, add a custom layer to your CSS:

```css title="src/globals.css"
@layer base, components, utilities, devlink;
```
