# Source: https://electric-sql.com/demos/nextjs.md

---
url: /demos/nextjs.md
description: Example of an Electric app using Next.js.
---

# {{ $frontmatter.title }}

{{ $frontmatter.description }}

## Next.js example app

This is an example using Electric with [Next.js](/docs/integrations/next).

The entrypoint for the Electric-specific code is in [`./app/page.tsx`](https://github.com/electric-sql/electric/blob/main/examples/nextjs/app/page.tsx):

<<< @../../examples/nextjs/app/page.tsx{tsx}
