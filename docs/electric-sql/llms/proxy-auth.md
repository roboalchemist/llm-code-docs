# Source: https://electric-sql.com/demos/proxy-auth.md

---
url: /demos/proxy-auth.md
description: Example showing how to authorize access to Electric using a proxy.
---

# {{ $frontmatter.title }}

{{ $frontmatter.description }}

## Proxy auth with Electric

This example demonstrates authorizing access to the Electric HTTP API using a proxy. It implements the [proxy-auth](/docs/guides/auth#proxy-auth) pattern described in the [Auth](/docs/guides/auth) guide.

The main proxy code is in [`./app/shape-proxy/route.ts`](https://github.com/electric-sql/electric/blob/main/examples/proxy-auth/app/shape-proxy/route.ts):

<<< @../../examples/proxy-auth/app/shape-proxy/route.ts{typescript}
