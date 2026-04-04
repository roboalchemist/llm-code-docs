# Source: https://www.zuplo.com/docs/dev-portal/zudoku/components/mermaid.md

# Source: https://www.zuplo.com/docs/dev-portal/zudoku/guides/mermaid.md

# Mermaid Diagrams

Dev Portal supports rendering [Mermaid diagrams](https://mermaid.js.org/) in two ways:

| Approach                        | Pros                                                                  | Cons                                                        |
| ------------------------------- | --------------------------------------------------------------------- | ----------------------------------------------------------- |
| **Build-Time** (rehype-mermaid) | • Faster page loads<br/>• No client-side JS needed<br/>• SEO friendly | • Requires playwright<br/>• Slower builds<br/>• Static only |
| **Client-Side** (`<Mermaid />`) | • Fast builds<br/>• Can be dynamic<br/>• No build dependencies        | • Requires client-side JS<br/>• Slight render delay         |

## Client-Side Rendering

For the [`<Mermaid />` component](/dev-portal/zudoku/components/mermaid), install the peer dependency:

```bash
npm install mermaid
```

Then use in your MDX files (no import needed):

```tsx
<Mermaid
  chart={`graph TD;
    A-->B;
    A-->C;`}
/>
```

Outside of MDX, import from `zudoku/mermaid`:

```tsx
import { Mermaid } from "zudoku/mermaid";
```

See the [Mermaid component documentation](/dev-portal/zudoku/components/mermaid) for full details.

## Build-Time Rendering

<Stepper>

1. Install dependencies:

   ```bash
   npm install rehype-mermaid
   npm install -D playwright
   npx playwright install
   ```

1. Add to `zudoku.build.ts`:

   ```tsx title="zudoku.build.ts"
   import rehypeMermaid from "rehype-mermaid";

   export default {
     rehypePlugins: (plugins) => [[rehypeMermaid, { strategy: "inline-svg" }], ...plugins],
   };
   ```

1. Use in markdown with code blocks:

   ````mdx
   ```mermaid
   graph TD;
       A-->B;
   ```
   ````

</Stepper>
