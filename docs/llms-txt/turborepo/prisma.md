# Source: https://turborepo.dev/guides/tools/prisma.md

---
title: Prisma
description: Learn how to use Prisma in a Turborepo.
product: turborepo
type: integration
summary: Integrate Prisma as a shared database package in your Turborepo monorepo.
related:

- /docs/guides/tools/docker
- /docs/guides/tools/typescript

---

# Prisma

[Prisma](https://www.prisma.io/) unlocks a new level of developer experience when working with databases thanks to its intuitive data model, automated migrations, type-safety & auto-completion.

[Their official guide](https://www.prisma.io/docs/guides/turborepo) describes how to integrate Prisma into a Turborepo, including:

- Prisma client initialization
- Packaging the client as an [Internal Package](/docs/core-concepts/internal-packages)
- Performing migrations
- Working on your applications locally
- Deploying

Example [#example]

To get started with our community-supported Prisma example, run:

```bash title="Terminal"
npx create-turbo@latest -e with-prisma
```

---

[View full sitemap](/sitemap.md)
