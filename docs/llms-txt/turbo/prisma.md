# Source: https://turbo.build/guides/tools/prisma.md

# Prisma

<CopyPrompt
  title="Set up Prisma in a Turborepo"
  prompt={
  "Set up Prisma in this Turborepo.\n1) Create a database package\n2) Configure the Prisma client\n3) Set up scripts for migrations and generation\n\nWalk me through each step."
}
/>

[Prisma](https://www.prisma.io/) unlocks a new level of developer experience when working with databases thanks to its intuitive data model, automated migrations, type-safety & auto-completion.

[Their official guide](https://www.prisma.io/docs/guides/turborepo) describes how to integrate Prisma into a Turborepo, including:

* Prisma client initialization
* Packaging the client as an [Internal Package](/docs/core-concepts/internal-packages)
* Performing migrations
* Working on your applications locally
* Deploying

## Example

To get started with our community-supported Prisma example, run:

```bash title="Terminal"
npx create-turbo@latest -e with-prisma
```

---

[View full sitemap](/sitemap.md)