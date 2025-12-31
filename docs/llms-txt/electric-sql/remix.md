# Source: https://electric-sql.com/demos/remix.md

---
url: /demos/remix.md
description: Example of an Electric app using Remix.
---

# {{ $frontmatter.title }}

{{ $frontmatter.description }}

## Remix example app

This is an example using Electric with [Remix](https://remix.run/).

The entrypoint for the Electric-specific code is in [`./app/routes/_index.tsx`](https://github.com/electric-sql/electric/blob/main/examples/remix/app/routes/_index.tsx):

<<< @../../examples/remix/app/routes/\_index.tsx{tsx}
