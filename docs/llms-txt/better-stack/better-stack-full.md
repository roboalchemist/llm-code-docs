# Better Stack Documentation

Source: https://www.better-stack.ai/docs/llms-full.txt

---

# API Reference (/api-reference)

## Backend (`@btst/stack/api`)

### stack

<AutoTypeTable path="../packages/stack/src/api/index.ts" name="stack" />

### BackendPlugin

<AutoTypeTable path="../packages/stack/src/types.ts" name="BackendPlugin" />

### BackendLibConfig

<AutoTypeTable path="../packages/stack/src/types.ts" name="BackendLibConfig" />

### BackendLib

<AutoTypeTable path="../packages/stack/src/types.ts" name="BackendLib" />

### toNodeHandler

Re-exported from `better-call/node`. Converts a BTST handler to a Node.js compatible request handler.

## Client (`@btst/stack/client`)

### createStackClient

<AutoTypeTable path="../packages/stack/src/client/index.ts" name="createStackClient" />

### ClientPlugin

<AutoTypeTable path="../packages/stack/src/types.ts" name="ClientPlugin" />

### ClientLib

<AutoTypeTable path="../packages/stack/src/types.ts" name="ClientLib" />

### ClientLibConfig

<AutoTypeTable path="../packages/stack/src/types.ts" name="ClientLibConfig" />

### SitemapEntry

<AutoTypeTable path="../packages/stack/src/types.ts" name="SitemapEntry" />

### Sitemap

An array of `SitemapEntry` objects.

```ts
type Sitemap = Array<SitemapEntry>;
```

### sitemapEntryToXmlString

<AutoTypeTable path="../packages/stack/src/client/sitemap-utils.ts" name="sitemapEntryToXmlString" />

### metaElementsToObject

<AutoTypeTable path="../packages/stack/src/client/meta-utils.ts" name="metaElementsToObject" />

### normalizePath

<AutoTypeTable path="../packages/stack/src/client/path-utils.ts" name="normalizePath" />

## Client Components (`@btst/stack/client/components`)

### RouteWithComponents

<AutoTypeTable path="../packages/stack/src/client/components/compose.tsx" name="RouteWithComponents" />

### RouteRenderer

<AutoTypeTable path="../packages/stack/src/client/components/compose.tsx" name="RouteRenderer" />

### ComposedRoute

<AutoTypeTable path="../packages/stack/src/client/components/compose.tsx" name="ComposedRoute" />

### FallbackProps

<AutoTypeTable path="../packages/stack/src/client/components/error-boundary.tsx" name="FallbackProps" />

### ErrorBoundary

<AutoTypeTable path="../packages/stack/src/client/components/error-boundary.tsx" name="ErrorBoundary" />

## Context (`@btst/stack/context`)

### StackProvider

<AutoTypeTable path="../packages/stack/src/context/provider.tsx" name="StackProvider" />

### useStack

<AutoTypeTable path="../packages/stack/src/context/provider.tsx" name="useStack" />

### usePluginOverrides

<AutoTypeTable path="../packages/stack/src/context/provider.tsx" name="usePluginOverrides" />

### useBasePath

<AutoTypeTable path="../packages/stack/src/context/provider.tsx" name="useBasePath" />


# Breaking Changes (/breaking-changes)

import { Callout } from "fumadocs-ui/components/callout";
import { Steps, Step } from "fumadocs-ui/components/steps";

This page documents breaking changes between major versions and provides migration guides.

***

## v1 → v2: Rebranding to BTST

BTST v2 introduces a rebranding from "Better Stack" to "BTST". This guide covers all the changes you need to make to upgrade your project.

<Callout type="info">
  This is a breaking change that requires updates to imports, function names, and file references. The functionality remains the same.
</Callout>

### Summary of Changes

| v1 (Better Stack)           | v2 (BTST)           |
| --------------------------- | ------------------- |
| `betterStack()`             | `stack()`           |
| `betterStackClient()`       | `stackClient()`     |
| `BetterStackProvider`       | `StackProvider`     |
| `useBetterStack`            | `useStack`          |
| `BetterStackAttribution`    | `StackAttribution`  |
| `better-stack.ts`           | `stack.ts`          |
| `better-stack-client.tsx`   | `stack-client.tsx`  |
| `"Powered by Better Stack"` | `"Powered by BTST"` |

### Migration Steps

<Steps>
  <Step>
    #### Update Package

    Update your `@btst/stack` package to v2:

    ```bash
    npm install @btst/stack@latest
    # or
    pnpm add @btst/stack@latest
    ```
  </Step>

  <Step>
    #### Rename Backend Setup Function

    Update your backend configuration file (commonly `lib/better-stack.ts` → `lib/stack.ts`):

    ```diff
    - import { betterStack } from "@btst/stack";
    + import { stack } from "@btst/stack";

    - export const { api, clientConfig, generateSitemap } = betterStack({
    + export const { api, clientConfig, generateSitemap } = stack({
        // ... your configuration
      });
    ```
  </Step>

  <Step>
    #### Rename Client Setup Function

    Update your client configuration file (commonly `lib/better-stack-client.tsx` → `lib/stack-client.tsx`):

    ```diff
    - import { betterStackClient } from "@btst/stack/client";
    + import { stackClient } from "@btst/stack/client";

    - export const { PluginPages, routes, loaders, metas } = betterStackClient({
    + export const { PluginPages, routes, loaders, metas } = stackClient({
        // ... your configuration
      });
    ```
  </Step>

  <Step>
    #### Update Provider Component

    If you're using the provider component directly:

    ```diff
    - import { BetterStackProvider } from "@btst/stack/client";
    + import { StackProvider } from "@btst/stack/client";

    function App() {
      return (
    -   <BetterStackProvider overrides={overrides}>
    +   <StackProvider overrides={overrides}>
          {children}
    -   </BetterStackProvider>
    +   </StackProvider>
      );
    }
    ```
  </Step>

  <Step>
    #### Update Hook Imports

    If you're using the context hook directly:

    ```diff
    - import { useBetterStack } from "@btst/stack/client";
    + import { useStack } from "@btst/stack/client";

    function MyComponent() {
    -   const context = useBetterStack();
    +   const context = useStack();
        // ...
    }
    ```
  </Step>

  <Step>
    #### Update Attribution Component

    If you're using the attribution component:

    ```diff
    - import { BetterStackAttribution } from "@workspace/ui/components/better-stack-attribution";
    + import { StackAttribution } from "@workspace/ui/components/stack-attribution";

    - <BetterStackAttribution />
    + <StackAttribution />
    ```
  </Step>

  <Step>
    #### Update File Imports

    Update any imports that reference the old filenames:

    ```diff
    - import { api } from "@/lib/better-stack";
    + import { api } from "@/lib/stack";

    - import { PluginPages } from "@/lib/better-stack-client";
    + import { PluginPages } from "@/lib/stack-client";
    ```
  </Step>

  <Step>
    #### Rename Files (Optional but Recommended)

    For consistency, rename your configuration files:

    ```bash
    # Backend config
    mv lib/better-stack.ts lib/stack.ts

    # Client config  
    mv lib/better-stack-client.tsx lib/stack-client.tsx

    # Auth config (if applicable)
    mv lib/better-stack-auth.ts lib/stack-auth.ts
    ```
  </Step>
</Steps>

### Find and Replace

You can use these find-and-replace patterns to quickly update your codebase:

| Find                               | Replace                     |
| ---------------------------------- | --------------------------- |
| `betterStack(`                     | `stack(`                    |
| `betterStackClient(`               | `stackClient(`              |
| `BetterStackProvider`              | `StackProvider`             |
| `useBetterStack`                   | `useStack`                  |
| `BetterStackAttribution`           | `StackAttribution`          |
| `better-stack-attribution`         | `stack-attribution`         |
| `from "@/lib/better-stack"`        | `from "@/lib/stack"`        |
| `from "@/lib/better-stack-client"` | `from "@/lib/stack-client"` |
| `from "./better-stack"`            | `from "./stack"`            |
| `from "./better-stack-client"`     | `from "./stack-client"`     |

### TypeScript Types

The following types have been renamed:

```diff
- import type { BetterStackContext } from "@btst/stack";
+ import type { StackContext } from "@btst/stack";
```

### Localization Strings

If you've customized localization, update any references:

```diff
- "Powered by Better Stack"
+ "Powered by BTST"
```

### No Functional Changes

<Callout type="info">
  All plugin functionality, APIs, database schemas, and component behavior remain unchanged. This is purely a naming/branding update.
</Callout>

The following are **unchanged**:

* All plugin configurations and options
* Database schemas and adapters
* API endpoints and routes
* Component props and behavior
* Hook return values and options
* SSR, meta tags, and sitemap generation

***

## Need Help?

If you encounter any issues during migration, please [open an issue](https://github.com/better-stack-ai/better-stack/issues) on GitHub.


# CLI (/cli)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";

The BTST CLI (`@btst/cli`) helps you generate database schemas and migrations from your plugin `dbSchema` exports.

## About Better DB

BTST uses [Better DB (`@btst/db`)](https://github.com/better-stack-ai/better-auth/tree/main/packages/btst) as its database abstraction layer—a specialized fork of [better-auth](https://www.better-auth.com)'s database layer optimized for BTST's plugin architecture.

The CLI works with the `dbSchema` exported from your BTST configuration, which is built using Better DB's schema definition API. All plugin schemas are automatically merged into a unified schema that the CLI can process.

Install the CLI as a dev dependency:

<Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
  <Tab value="npm">
    ```bash
    npm install -D @btst/cli
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpm add -D @btst/cli
    ```
  </Tab>

  <Tab value="yarn">
    ```bash
    yarn add -D @btst/cli
    ```
  </Tab>
</Tabs>

## Parameters

| Parameter        | Command                             | Required                             | Values                                    | Description                                                     |
| ---------------- | ----------------------------------- | ------------------------------------ | ----------------------------------------- | --------------------------------------------------------------- |
| `--config`       | `generate`, `migrate`               | Yes                                  | File path (e.g., `db.ts`, `lib/stack.ts`) | Path to your BTST configuration file that exports `dbSchema`    |
| `--orm`          | `generate`                          | Yes                                  | `prisma`, `drizzle`, `kysely`             | The ORM to generate schema for                                  |
| `--output`       | `generate`, `migrate`               | Yes (generate), Yes (migrate)        | File path                                 | Output file path for generated schema or migration SQL          |
| `--database-url` | `generate` (kysely only), `migrate` | Yes (kysely generate), Yes (migrate) | Database connection string                | Database URL (can also use `DATABASE_URL` environment variable) |

## Generate

Generate database schemas for your ORM from your BTST `dbSchema`:

<Tabs items={["prisma", "drizzle", "kysely"]}>
  <Tab value="prisma">
    ```bash
    npx @btst/cli generate --config=lib/stack.ts --orm=prisma --output=schema.prisma
    ```
  </Tab>

  <Tab value="drizzle">
    ```bash
    npx @btst/cli generate --config=lib/stack.ts --orm=drizzle --output=src/db/schema.ts
    ```
  </Tab>

  <Tab value="kysely">
    Kysely requires a database connection for introspection:

    **Using DATABASE\_URL environment variable:**

    ```bash
    DATABASE_URL=sqlite:./dev.db npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql
    ```

    **Or using --database-url flag:**

    ```bash
    npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql --database-url=sqlite:./dev.db
    ```

    ```bash
    npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql --database-url=postgres://user:pass@localhost:5432/db
    ```
  </Tab>
</Tabs>

## Migrate

Migrate your database schema directly (Kysely only). For Prisma and Drizzle, use their native migration tools.

**Using DATABASE\_URL environment variable:**

```bash
DATABASE_URL=sqlite:./dev.db npx @btst/cli migrate --config=lib/stack.ts
```

**Or using --database-url flag:**

```bash
npx @btst/cli migrate --config=lib/stack.ts --database-url=sqlite:./dev.db
```

```bash
npx @btst/cli migrate --config=lib/stack.ts --database-url=postgres://user:pass@localhost:5432/db
```

### Generate SQL to File

Instead of running migrations directly, generate SQL to a file:

```bash
npx @btst/cli migrate --config=lib/stack.ts --output=migrations.sql --database-url=sqlite:./dev.db
```

## Gotchas

Because the CLI executes your config file to extract the `dbSchema`, there are a few limitations to be aware of:

* **Path aliases don't work**: Path aliases (like `@/` or `~/`) configured in your TypeScript config won't work for any imports used in your `stack.ts` file or any files it imports. Use relative paths instead.

* **Environment variables**: If your config file or its imports have conditional checks for available environment variables (e.g., checking if `process.env.SOME_VAR` exists), you should also pass those environment variables when running CLI commands:

```bash
SOME_VAR=value npx @btst/cli generate --config=lib/stack.ts --orm=prisma --output=schema.prisma
```


# How It Works (/how-it-works)



Here's a high-level overview of how BTST works:

<img alt="Architecture Overview" src={__img0} placeholder="blur" />

## Server Side

The server handles database operations, API endpoints, data prefetching, routing, and server-side rendering.

**`stack`** manages the backend layer:

* **API Router**: Routes incoming requests to the appropriate plugin handlers. Returns a handler function that you mount at your API path.
* **DB Adapter**: Translates BTST's database operations to your ORM (Prisma, Drizzle, Kysely, MongoDB). Plugins define schemas that get merged and passed to the adapter.

**`stackClient`** manages the rendering layer:

* **Data Fetching**: Plugins can prefetch data server-side into React Query cache before rendering, enabling instant page loads with hydrated state.
* **Page Router**: Matches URLs to plugin routes and returns the appropriate page component, loader, and metadata.
* **SSR**: Server-side renders pages with prefetched data, then hydrates on the client.

## Client Side

After server-side rendering, the client takes over for interactivity.

**React Hydration**

Server-rendered HTML is hydrated with client-side React. The React Query cache—prefetched during SSR—transfers seamlessly, so components render instantly without loading states or refetching.

**SPA Navigation (If using in an SPA)**

After the initial page load, `stackClient`'s router handles client-side navigation. Clicking links doesn't trigger full page reloads—React Query fetches data in the background while the UI updates immediately.

**State Management**

First party plugins use React Query under the hood for all data operations:

* **Queries**: Hooks like `usePosts()`, `usePost(slug)`, and `useTags()` (examples from the blog plugin) fetch and cache data with automatic background refetching
* **Mutations**: Hooks like `useCreatePost()`, `useUpdatePost()`, and `useDeletePost()` (examples from the blog plugin) handle writes with automatic cache invalidation
* **Suspense**: Suspense variants (`useSuspensePosts`, `useSuspensePost`) integrate with React Suspense boundaries for streaming SSR and other advanced features

Note: 3rd party plugins may use a different state management library.

**Context & Overrides**

The `StackProvider` wraps your pages and injects framework-specific components via React Context. Plugin components access these overrides through `usePluginOverrides()`, allowing them to use your framework's `Link`, `Image`, and navigation without tight coupling and to avoid breaking the client/server boundary in frameworks like Next.js.

## Plugins

Plugins are the building blocks of BTST. Each feature (like Blog) ships as **two separate plugins**—one for the backend, one for the client—that you register independently:

```ts
// Backend: lib/stack.ts
import { stack } from "@btst/stack"
import { blogBackendPlugin } from "@btst/stack/plugins/blog/api"

const { handler } = stack({
  plugins: {
    blog: blogBackendPlugin({ /* config */ })
  },
  // ...
})

// Client: lib/stack-client.tsx
import { createStackClient } from "@btst/stack/client"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"

const stackClient = createStackClient({
  plugins: {
    blog: blogClientPlugin({ /* config */ })
  }
})
```

**Backend plugins** (registered in `stack`):

* Define database schemas (tables, columns, relations)
* Register API route handlers for CRUD operations
* Provide hooks for authorization and custom logic

**Client plugins** (registered in `stackClient`):

* Define page routes and components
* Provide loaders for server-side data prefetching
* Export components, hooks, and utilities for state management
* Generate SEO metadata and sitemaps

This separation keeps server-only code (database schemas, API handlers) out of your client bundle, and allows each plugin to be configured independently for its context.

## Overrides

Framework-specific components injected into plugins at runtime:

* **Link**: Use Next.js `Link`, React Router `Link`, or TanStack `Link` for optimized navigation
* **Image**: Use Next.js `Image` for automatic optimization
* **navigate**: Programmatic navigation function for your framework
* **apiBaseURL/apiBasePath**: Configure where your API is mounted


# Introduction (/)

import { Card, Cards } from "fumadocs-ui/components/card";
import { Rocket, BookOpenCheck, Server, Layers, Router, Zap, Terminal } from "lucide-react";

## 👋 Welcome to BTST

**@btst - BTST** is a composable full-stack plugin system for modern React frameworks.

Instead of building routes, APIs, databases, SSR, and forms from scratch, BTST gives you **complete full-stack features as plugins** that work with any modern React framework.

### Key Features

* **🔄 Framework Agnostic** - Works with Next.js, React Router, TanStack Router, Remix
* **📦 Full-Stack** - Routes, APIs, database schemas, components, hooks, SSR, metatags, sitemaps
* **🎯 Composable** - Mix and match features like LEGO blocks
* **🚀 Zero Boilerplate** - Configure and it works

### Available Plugins

**Blog** - Content management, editor, drafts, publishing, tags, SEO and more

More plugins coming soon (AI assistant, scheduling, feedback, newsletters, comments).
Or build your own plugins for any horizontal feature.

<Cards>
  <Card title="Installation" href="/installation" icon={<Zap size={20} />} description="Install and configure." />

  <Card title="Plugins" href="/plugins" icon={<Layers size={20} />} description="Available plugins and features." />

  <Card title="CLI" href="/cli" icon={<Terminal size={20} />} description="Generate database schemas and migrations." />

  <Card title="Plugin Development" href="/plugins/development" icon={<BookOpenCheck size={20} />} description="Build your own plugins." />
</Cards>

***

## LLMs.txt

BTST provides an LLMs.txt file that helps AI models understand how to use the library. You can find it at [/docs/llms.txt](/llms.txt).


# Installation (/installation)

import { Steps, Step } from "fumadocs-ui/components/steps";
import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";

## Prerequisites

In order to use BTST, your application must meet the following requirements:

* **[shadcn/ui](https://ui.shadcn.com/)** installed with CSS variables enabled - Plugins use shadcn/ui components. To verify CSS variables are enabled, check that your `components.json` has `"cssVariables": true` or your Tailwind config uses CSS variables for colors.
* **[Sonner](https://ui.shadcn.com/docs/components/sonner)** `<Toaster />` component configured for toast notifications
* **[TailwindCSS](https://tailwindcss.com) v4** set up and configured correctly - Plugins use Tailwind classes and utilities
* **[@tanstack/react-query](https://tanstack.com/query)** installed - Required for server-side prefetching and client-side data fetching/state management

<Steps>
  <Step>
    ### Install the Package

    Let's start by adding BTST to your project:

    <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
      <Tab value="npm">
        ```bash
        npm install @btst/stack @tanstack/react-query
        ```
      </Tab>

      <Tab value="pnpm">
        ```bash
        pnpm add @btst/stack @tanstack/react-query
        ```
      </Tab>

      <Tab value="yarn">
        ```bash
        yarn add @btst/stack @tanstack/react-query
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      BTST plugins require `@tanstack/react-query` for server-side prefetching and client-side data fetching and state management.
    </Callout>
  </Step>

  <Step>
    ### Install Database Adapter

    BTST requires a database adapter to work with your database. Choose one based on your setup:

    <Tabs groupId="adapter-type" items={["prisma", "drizzle", "kysely", "mongodb", "memory"]} persist>
      <Tab value="prisma">
        For Prisma ORM:

        <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
          <Tab value="npm">
            ```bash
            npm install @btst/adapter-prisma
            ```
          </Tab>

          <Tab value="pnpm">
            ```bash
            pnpm add @btst/adapter-prisma
            ```
          </Tab>

          <Tab value="yarn">
            ```bash
            yarn add @btst/adapter-prisma
            ```
          </Tab>
        </Tabs>
      </Tab>

      <Tab value="drizzle">
        For Drizzle ORM:

        <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
          <Tab value="npm">
            ```bash
            npm install @btst/adapter-drizzle
            ```
          </Tab>

          <Tab value="pnpm">
            ```bash
            pnpm add @btst/adapter-drizzle
            ```
          </Tab>

          <Tab value="yarn">
            ```bash
            yarn add @btst/adapter-drizzle
            ```
          </Tab>
        </Tabs>
      </Tab>

      <Tab value="kysely">
        For Kysely query builder:

        <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
          <Tab value="npm">
            ```bash
            npm install @btst/adapter-kysely
            ```
          </Tab>

          <Tab value="pnpm">
            ```bash
            pnpm add @btst/adapter-kysely
            ```
          </Tab>

          <Tab value="yarn">
            ```bash
            yarn add @btst/adapter-kysely
            ```
          </Tab>
        </Tabs>
      </Tab>

      <Tab value="mongodb">
        For MongoDB:

        <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
          <Tab value="npm">
            ```bash
            npm install @btst/adapter-mongodb
            ```
          </Tab>

          <Tab value="pnpm">
            ```bash
            pnpm add @btst/adapter-mongodb
            ```
          </Tab>

          <Tab value="yarn">
            ```bash
            yarn add @btst/adapter-mongodb
            ```
          </Tab>
        </Tabs>
      </Tab>

      <Tab value="memory">
        For development and testing, use the in-memory adapter:

        <Tabs groupId="installation" items={['npm', 'pnpm', 'yarn']} persist>
          <Tab value="npm">
            ```bash
            npm install @btst/adapter-memory
            ```
          </Tab>

          <Tab value="pnpm">
            ```bash
            pnpm add @btst/adapter-memory
            ```
          </Tab>

          <Tab value="yarn">
            ```bash
            yarn add @btst/adapter-memory
            ```
          </Tab>
        </Tabs>
      </Tab>
    </Tabs>
  </Step>

  <Step>
    ### Create Backend Instance

    Create a file named `stack.ts` in your `lib/` folder to configure the backend API:

    <Tabs groupId="adapter-type" items={["prisma", "drizzle", "kysely", "mongodb", "memory"]} persist>
      <Tab value="prisma">
        ```ts title="lib/stack.ts"
        import { stack } from "@btst/stack"
        import { createPrismaAdapter } from "@btst/adapter-prisma"
        import { PrismaClient } from "@prisma/client"

        const prisma = new PrismaClient()

        const { handler, dbSchema } = stack({
          basePath: "/api/data",
          plugins: {
            // Add your backend plugins here
          },
          adapter: (db) => createPrismaAdapter(prisma, db, { 
            provider: "postgresql" // or "mysql", "sqlite", "cockroachdb", "mongodb"
          })
        })

        export { handler, dbSchema }
        ```
      </Tab>

      <Tab value="drizzle">
        ```ts title="lib/stack.ts"
        import { stack } from "@btst/stack"
        import { createDrizzleAdapter } from "@btst/adapter-drizzle"
        import { drizzle } from "drizzle-orm/postgres-js" // or "drizzle-orm/mysql2", "drizzle-orm/better-sqlite3", etc.
        import postgres from "postgres"

        const client = postgres(process.env.DATABASE_URL!)
        const drizzleDb = drizzle(client)

        const { handler, dbSchema } = stack({
          basePath: "/api/data",
          plugins: {
            // Add your backend plugins here
          },
          adapter: (db) => createDrizzleAdapter(drizzleDb, db, {})
        })

        export { handler, dbSchema }
        ```
      </Tab>

      <Tab value="kysely">
        ```ts title="lib/stack.ts"
        import { stack } from "@btst/stack"
        import { createKyselyAdapter } from "@btst/adapter-kysely"
        import { Kysely, PostgresDialect } from "kysely"
        import { Pool } from "pg"

        const kyselyDb = new Kysely({
          dialect: new PostgresDialect({
            pool: new Pool({ connectionString: process.env.DATABASE_URL })
          })
        })

        const { handler, dbSchema } = stack({
          basePath: "/api/data",
          plugins: {
            // Add your backend plugins here
          },
          adapter: (db) => createKyselyAdapter(kyselyDb, db, {})
        })

        export { handler, dbSchema }
        ```
      </Tab>

      <Tab value="mongodb">
        ```ts title="lib/stack.ts"
        import { stack } from "@btst/stack"
        import { createMongodbAdapter } from "@btst/adapter-mongodb"
        import { MongoClient } from "mongodb"

        const client = new MongoClient(process.env.MONGODB_URI!)
        const mongoDb = client.db()

        const { handler, dbSchema } = stack({
          basePath: "/api/data",
          plugins: {
            // Add your backend plugins here
            // blog: blogBackendPlugin()
          },
          adapter: (db) => createMongodbAdapter(mongoDb, db, {})
        })

        export { handler, dbSchema }
        ```
      </Tab>

      <Tab value="memory">
        ```ts title="lib/stack.ts"
        // IMPORTANT: Memory adapter is used for development and testing only
        import { stack } from "@btst/stack"
        import { createMemoryAdapter } from "@btst/adapter-memory"

        const { handler, dbSchema } = stack({
          basePath: "/api/data",
          plugins: {
            // Add your backend plugins here
          },
          adapter: (db) => createMemoryAdapter(db)({})
        })

        export { handler, dbSchema }
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      **What happens here:**

      * `stack()` collects all plugin database schemas and merges them into a unified `dbSchema`
      * The `basePath` determines where your API is mounted (e.g., `/api/data/*`)
      * The `adapter` function receives this merged schema (`db`) and returns an adapter that translates BTST's database operations to your ORM
      * The `handler` is a request handler function `(request: Request) => Promise<Response>` that processes all API calls
    </Callout>

    **Now you can generate database schema** using the CLI (not needed for mongodb):

    <Tabs items={["prisma", "drizzle", "kysely"]}>
      <Tab value="prisma">
        ```bash
        npx @btst/cli generate --config=lib/stack.ts --orm=prisma --output=schema.prisma
        ```
      </Tab>

      <Tab value="drizzle">
        ```bash
        npx @btst/cli generate --config=lib/stack.ts --orm=drizzle --output=src/db/schema.ts
        ```
      </Tab>

      <Tab value="kysely">
        Kysely requires a database connection for introspection:

        **Using DATABASE\_URL environment variable:**

        ```bash
        DATABASE_URL=sqlite:./dev.db npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql
        ```

        **Or using --database-url flag:**

        ```bash
        npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql --database-url=sqlite:./dev.db
        ```

        ```bash
        npx @btst/cli generate --config=lib/stack.ts --orm=kysely --output=migrations/schema.sql --database-url=postgres://user:pass@localhost:5432/db
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      See the [CLI documentation](/cli) to learn more about generating database schemas and migrations.
    </Callout>
  </Step>

  <Step>
    ### Create API Route

    Create a catch-all API route to handle BTST requests. The route will handle requests for the path `/api/data/*`. If you use a different path make sure to update the `basePath` in the `stack` config to match your chosen path.

    <Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack", "nodejs"]} persist>
      <Tab value="next-js">
        ```ts title="app/api/data/[[...all]]/route.ts"
        import { handler } from "@/lib/stack"

        export const GET = handler
        export const POST = handler
        export const PUT = handler
        export const DELETE = handler
        ```
      </Tab>

      <Tab value="react-router">
        ```ts title="app/routes/api/data/route.ts"
        import { handler } from "~/lib/stack"
        import type { LoaderFunctionArgs, ActionFunctionArgs } from "@remix-run/node"

        export async function loader({ request }: LoaderFunctionArgs) {
          return handler(request)
        }

        export async function action({ request }: ActionFunctionArgs) {
          return handler(request)
        }
        ```
      </Tab>

      <Tab value="tanstack">
        ```ts title="src/routes/api/data/$.ts"
        import { createFileRoute } from '@tanstack/react-router'
        import { handler } from '@/lib/stack'

        export const Route = createFileRoute('/api/data/$')({
          server: {
            handlers: {
              GET: async ({ request }) => {
                return handler(request)
              },
              POST: async ({ request }) => {
                return handler(request)
              },
              PUT: async ({ request }) => {
                return handler(request)
              },
              DELETE: async ({ request }) => {
                return handler(request)
              },
            },
          },
        })
        ```
      </Tab>

      <Tab value="nodejs">
        For standalone Node.js servers (Express, Fastify, etc.), use `toNodeHandler` to convert the Web API handler to a Node.js-compatible handler:

        ```ts title="server.ts"
        import express from "express"
        import { handler } from "./lib/stack"
        import { toNodeHandler } from "@btst/stack/api"

        const app = express()

        // Convert Web API handler to Node.js handler
        const nodeHandler = toNodeHandler(handler)

        // Mount at your basePath
        app.use("/api/data", nodeHandler)

        app.listen(3000, () => {
          console.log("Server running on http://localhost:3000")
        })
        ```

        **Alternative: Using with Express middleware**

        ```ts title="server.ts"
        import express from "express"
        import { handler } from "./lib/stack"
        import { toNodeHandler } from "@btst/stack/api"

        const app = express()
        app.use(express.json()) // Parse JSON bodies

        // Convert and mount BTST handler
        app.all("/api/data/*", toNodeHandler(handler))

        app.listen(3000)
        ```
      </Tab>
    </Tabs>
  </Step>

  <Step>
    ### Import Plugin Styles

    Plugins use [TailwindCSS v4](https://tailwindcss.com), so you should add the following `@import` to your global css file to ensure proper styling:

    ```css title="app/globals.css"
    @import "@btst/stack/plugins/blog/css";
    ```

    <Callout type="info">
      Each plugin may require its own CSS import. The import path follows the pattern `@btst/stack/plugins/{plugin-name}/css`. Check the plugin documentation for specific requirements.
    </Callout>
  </Step>

  <Step>
    ### Create Client Instance

    Create a client instance that routes requests to plugin pages, prefetches their data on the server, and renders them with instant hydration on the client:

    ```ts title="lib/stack-client.tsx"
    import { createStackClient } from "@btst/stack/client"
    import { QueryClient } from "@tanstack/react-query"

    export const getStackClient = (queryClient: QueryClient) => {
      return createStackClient({
        plugins: {
          // Add your client plugins here
        }
      })
    }
    ```

    <Callout type="info">
      **Why a function?** `getStackClient` takes a `QueryClient` because different contexts use different instances:

      * **Server (SSR)**: Each request gets its own QueryClient (or cached per-request)
      * **Client**: A singleton QueryClient is shared across navigations
      * **Additional options**: You can pass additional options to the `createStackClient` function, such as `headers` for SSR authentication if plugins expose lifecycle hooks.

      This pattern allows you to pass the appropriate QueryClient and other options for each context.
    </Callout>
  </Step>

  <Step>
    ### Set Up Query Client Provider

    If you don't already have a query client utility, create one to ensure proper SSR hydration:

    ```ts title="lib/query-client.ts"
    import { QueryClient, isServer } from "@tanstack/react-query"
    import { cache } from "react"

    function makeQueryClient() {
      return new QueryClient({
        defaultOptions: {
          queries: {
            staleTime: isServer ? 60 * 1000 : 0,
            refetchOnMount: false,
            refetchOnWindowFocus: false,
            retry: false
          },
          dehydrate: {
            // Include both successful and error states to avoid refetching on the client
            // This prevents loading states when there's an error in prefetched data
            shouldDehydrateQuery: (query) => {
                return true
            }
          }
        }
      })
    }

    let browserQueryClient: QueryClient | undefined = undefined

    export function getOrCreateQueryClient() {
        if (isServer) {
            // Server: always make a new query client
            return makeQueryClient();
        } else {
            // Browser: make a new query client if we don't already have one
            // This is very important, so we don't re-make a new client if React
            // suspends during the initial render. This may not be needed if we
            // have a suspense boundary BELOW the creation of the query client
            if (!browserQueryClient) browserQueryClient = makeQueryClient();
            return browserQueryClient;
        }
    }
    ```

    Then configure `QueryClientProvider` in your your app:

    <Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
      <Tab value="next-js">
        ```tsx title="app/layout.tsx"
        import { QueryClientProvider } from "@tanstack/react-query"
        import { getOrCreateQueryClient } from "@/lib/query-client"

        export default function RootLayout({ children }) {
          const queryClient = getOrCreateQueryClient()
          
          return (
            <html>
              <body>
                <QueryClientProvider client={queryClient}>
                  {children}
                </QueryClientProvider>
              </body>
            </html>
          )
        }
        ```
      </Tab>

      <Tab value="react-router">
        ```tsx title="app/root.tsx"
        import { QueryClientProvider } from "@tanstack/react-query"
        import { getOrCreateQueryClient } from "~/lib/query-client"
        import { Outlet } from "react-router"

        export default function App() {
          const queryClient = getOrCreateQueryClient()
          
          return (
            <QueryClientProvider client={queryClient}>
              <Outlet />
            </QueryClientProvider>
          )
        }
        ```
      </Tab>

      <Tab value="tanstack">
        ```tsx title="src/router.tsx"
        import { createRouter } from '@tanstack/react-router'
        import { routeTree } from './routeTree.gen'
        import { QueryClient } from '@tanstack/react-query'
        import { setupRouterSsrQueryIntegration } from '@tanstack/react-router-ssr-query'
        import { getOrCreateQueryClient } from '@/lib/query-client'

        export interface MyRouterContext {
          queryClient: QueryClient
        }

        export function getRouter() {
          const queryClient = getOrCreateQueryClient()
          
          const router = createRouter({
            routeTree,
            scrollRestoration: true,
            defaultPreload: false,
            context: {
              queryClient,
            },
            notFoundMode: "root",
          })

          setupRouterSsrQueryIntegration({
            router,
            queryClient,
          })

          return router
        }

        declare module '@tanstack/react-router' {
          interface Register {
            router: ReturnType<typeof getRouter>
          }
        }
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      The `getOrCreateQueryClient()` utility ensures:

      * **Server**: Each request gets its own QueryClient
      * **Client**: A singleton QueryClient prevents recreation during React Suspense
      * **Hydration**: Server-prefetched data seamlessly transfers to the client

      **Note**: QueryClient might have to be configured differently in your framework of choice. See [Example Projects](#example-projects) or [TanStack Query docs](https://tanstack.com/query/latest/docs/framework/react/overview) for more details.
    </Callout>
  </Step>

  <Step>
    ### Set Up Layout Provider

    Wrap your BTST pages with the `StackProvider` to enable framework-specific overrides:

    <Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
      <Tab value="next-js">
        ```tsx title="app/pages/[[...all]]/layout.tsx"
        import { StackProvider } from "@btst/stack/context"
        import type { ExamplePluginOverrides } from "@btst/stack/plugins/example/client"
        import Link from "next/link"
        import Image from "next/image"
        import { useRouter } from "next/navigation"

        // Define the shape of all plugin overrides for type safety
        type PluginOverrides = {
          example: ExamplePluginOverrides
          // Add other plugins here
        }

        export default function Layout({ children }) {
          const router = useRouter()
          
          return (
            <StackProvider<PluginOverrides>
              basePath="/pages"
              overrides={{
                example: {
                  Link: (props) => <Link {...props} />,
                  Image: (props) => <Image {...props} />,
                  navigate: (path) => router.push(path),
                  // Add other plugin overrides here
                }
                // Add other plugins here
              }}
            >
              {children}
            </StackProvider>
          )
        }
        ```
      </Tab>

      <Tab value="react-router">
        ```tsx title="app/routes/pages/_layout.tsx"
        import { Outlet, Link, useNavigate } from "react-router"
        import { StackProvider } from "@btst/stack/context"
        import type { ExamplePluginOverrides } from "@btst/stack/plugins/example/client"

        // Define the shape of all plugin overrides
        type PluginOverrides = {
          example: ExamplePluginOverrides
          // Add other plugins here
        }

        export default function Layout() {
          const navigate = useNavigate()
          
          return (
            <StackProvider<PluginOverrides>
              basePath="/pages"
              overrides={{
                example: {
                  navigate: (href) => navigate(href),
                  Link: ({ href, children, className, ...props }) => (
                    <Link to={href || ""} className={className} {...props}>
                      {children}
                    </Link>
                  )
                  // Add other plugin overrides here
                }
                // Add other plugins here
              }}
            >
              <Outlet />
            </StackProvider>
          )
        }
        ```
      </Tab>

      <Tab value="tanstack">
        ```tsx title="src/routes/pages/route.tsx"
        import { StackProvider } from "@btst/stack/context"
        import { QueryClientProvider } from "@tanstack/react-query"
        import type { ExamplePluginOverrides } from "@btst/stack/plugins/example/client"
        import { Link, useRouter, Outlet, createFileRoute } from "@tanstack/react-router"

        // Define the shape of all plugin overrides
        type PluginOverrides = {
          example: ExamplePluginOverrides
          // Add other plugins here
        }

        export const Route = createFileRoute('/pages')({
          component: Layout
        })

        function Layout() {
          const router = useRouter()
          const context = Route.useRouteContext()

          return (
            <QueryClientProvider client={context.queryClient}>
              <StackProvider<PluginOverrides>
                basePath="/pages"
                overrides={{
                  example: {
                    navigate: (href) => router.navigate({ href }),
                    Link: ({ href, children, className, ...props }) => (
                      <Link to={href} className={className} {...props}>
                        {children}
                      </Link>
                    )
                    // Add other plugin overrides here
                  }
                  // Add other plugins here
                }}
              >
                <Outlet />
              </StackProvider>
            </QueryClientProvider>
          )
        }
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      **Understanding Overrides:**

      * **Purpose**: Injects framework-specific components via React Context. Plugin components access these overrides through `usePluginOverrides()` hook, allowing them to use your framework's `Link`, `Image`, and navigation without tight coupling and to avoid breaking the client/server boundary in frameworks like Next.js.
      * **Type Safety**: Each plugin exports its override type (e.g., `ExamplePluginOverrides`)
    </Callout>
  </Step>

  <Step>
    ### Set Up Page Handler

    Create a catch-all route to handle BTST pages defined in your plugins. This enables server-side rendering, metadata generation and automatic route handling.

    <Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
      <Tab value="next-js">
        ```tsx title="app/pages/[[...all]]/page.tsx"
        import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
        import { notFound } from "next/navigation"
        import { getOrCreateQueryClient } from "@/lib/query-client"
        import { getStackClient } from "@/lib/stack-client"
        import { metaElementsToObject, normalizePath } from "@btst/stack/client"
        import { Metadata } from "next"

        export default async function Page({ params }: { params: Promise<{ all: string[] }> }) {
          const pathParams = await params
          const path = normalizePath(pathParams?.all)
          
          const queryClient = getOrCreateQueryClient()
          const stackClient = getStackClient(queryClient)
          const route = stackClient.router.getRoute(path)
          
          // Prefetch data server-side if the route has a loader
          if (route?.loader) await route.loader()
          
          // Serialize React Query cache for client hydration
          const dehydratedState = dehydrate(queryClient)
          
          return (
            <HydrationBoundary state={dehydratedState}>
              {route && route.PageComponent ? <route.PageComponent /> : notFound()}
            </HydrationBoundary>
          )
        }

        export async function generateMetadata({ params }: { params: Promise<{ all: string[] }> }) {
          const pathParams = await params
          const path = normalizePath(pathParams?.all)
          
          const queryClient = getOrCreateQueryClient()
          const stackClient = getStackClient(queryClient)
          const route = stackClient.router.getRoute(path)
          
          if (!route) return notFound()
          if (route?.loader) await route.loader()
          
          // Convert plugin meta elements to Next.js Metadata format
          return route.meta ? metaElementsToObject(route.meta()) satisfies Metadata : { title: "No meta" }
        }
        ```
      </Tab>

      <Tab value="react-router">
        ```tsx title="app/routes/pages/index.tsx"
        import type { Route } from "./+types/index"
        import { useLoaderData } from "react-router"
        import { dehydrate, HydrationBoundary, QueryClient, useQueryClient } from "@tanstack/react-query"
        import { getStackClient } from "~/lib/stack-client"
        import { normalizePath } from "@btst/stack/client"

        export async function loader({ params }: Route.LoaderArgs) {
          const path = normalizePath(params["*"])
          
          // Create QueryClient for this request with consistent config
          const queryClient = new QueryClient({
            defaultOptions: { queries: { staleTime: 1000 * 60 * 5, refetchOnMount: false, retry: false } }
          })
          const stackClient = getStackClient(queryClient)
          const route = stackClient.router.getRoute(path)
          
          if (route?.loader) await route.loader()
          
          // Include errors so client doesn't refetch on error
          const dehydratedState = dehydrate(queryClient)
          
          return { path, dehydratedState, meta: route?.meta?.() }
        }

        export function meta({ loaderData }: Route.MetaArgs) {
          return loaderData.meta
        }

        export default function PagesIndex() {
          const { path, dehydratedState } = useLoaderData<typeof loader>()
          const queryClient = useQueryClient()
          const route = getStackClient(queryClient).router.getRoute(path)
          const Page = route && route.PageComponent ? <route.PageComponent /> : <div>Route not found</div>
          
          return dehydratedState ? (
            <HydrationBoundary state={dehydratedState}>{Page}</HydrationBoundary>
          ) : Page
        }
        ```
      </Tab>

      <Tab value="tanstack">
        ```tsx title="src/routes/pages/$.tsx"
        import { createFileRoute, notFound } from "@tanstack/react-router"
        import { getStackClient } from "@/lib/stack-client"
        import { normalizePath } from "@btst/stack/client"

        export const Route = createFileRoute("/pages/$")({
          ssr: true,
          component: Page,
          loader: async ({ params, context }) => {
            const routePath = normalizePath(params._splat)
            const stackClient = getStackClient(context.queryClient)
            const route = stackClient.router.getRoute(routePath)
            
            if (!route) throw notFound()
            if (route?.loader) await route.loader()
            
            return { meta: await route?.meta?.() }
          },
          head: ({ loaderData }) => {
            return loaderData?.meta && Array.isArray(loaderData.meta) 
              ? { meta: loaderData.meta } 
              : { meta: [{ title: "No Meta" }], title: "No Meta" }
          },
          notFoundComponent: () => <p>This page doesn't exist!</p>
        })

        function Page() {
          const context = Route.useRouteContext()
          const { _splat } = Route.useParams()
          const routePath = normalizePath(_splat)
          const route = getStackClient(context.queryClient).router.getRoute(routePath)
          
          return route && route.PageComponent ? <route.PageComponent /> : <div>Route not found</div>
        }
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      **How it works:**

      `stackClient.router.getRoute(path)` matches the URL to a plugin route and returns a route object:

      ```typescript
      route = {
        PageComponent: React.ComponentType,     // The page to render
        loader?: () => Promise<void>,           // Prefetches React Query data
        meta?: () => MetadataElements,          // Returns SEO metadata
        ErrorComponent?: React.ComponentType,   // Standalone error components
        LoadingComponent?: React.ComponentType  // Standalone loading components
      }
      ```

      **Key steps:**

      * **Server-side data loading**: Call `route.loader()` before rendering to prefetch data into React Query cache
      * **Hydration**: Use `dehydrate()` to serialize prefetched data for the client (not required with TanStack Start)
      * **Error handling**: Configure your query client with `shouldDehydrateQuery` to include failed queries in dehydration, preventing client-side refetching on errors
      * **Metadata generation**: Use `route.meta()` with framework-specific meta functions for SEO
      * **404 handling**: Return `notFound()` or your framework's equivalent function when routes don't exist
    </Callout>
  </Step>

  <Step>
    ### Set Up Sitemap Generation (Optional)

    Create a sitemap route to enable automatic sitemap generation for SEO. The library automatically collects URLs from all registered plugins.

    **How it works**: Each plugin can export a `sitemap()` function that returns URLs with metadata (lastModified, changeFrequency, priority). The `generateSitemap()` method aggregates and deduplicates entries from all plugins.

    <Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
      <Tab value="next-js">
        ```ts title="app/sitemap.ts"
        import type { MetadataRoute } from "next"
        import { QueryClient } from "@tanstack/react-query"
        import { getStackClient } from "@/lib/stack-client"

        export const dynamic = "force-dynamic"

        export default async function sitemap(): Promise<MetadataRoute.Sitemap> {
          const queryClient = new QueryClient()
          const stackClient = getStackClient(queryClient)
          return stackClient.generateSitemap()
        }
        ```
      </Tab>

      <Tab value="react-router">
        ```ts title="app/routes/sitemap.xml.ts"
        import type { Route } from "./+types/sitemap.xml"
        import { QueryClient } from "@tanstack/react-query"
        import { getStackClient } from "~/lib/stack-client"
        import { sitemapEntryToXmlString } from "@btst/stack/client"

        export async function loader({}: Route.LoaderArgs) {
          const queryClient = new QueryClient()
          const stackClient = getStackClient(queryClient)
          const entries = await stackClient.generateSitemap()
          const xml = sitemapEntryToXmlString(entries)

          return new Response(xml, {
            headers: {
              "Content-Type": "application/xml; charset=utf-8",
              "Cache-Control": "public, max-age=0, s-maxage=3600, stale-while-revalidate=86400",
            },
          })
        }
        ```
      </Tab>

      <Tab value="tanstack">
        ```ts title="src/routes/sitemap[.]xml.ts"
        // Note: [.] syntax in TanStack Router creates a route for "sitemap.xml"
        import { createFileRoute } from "@tanstack/react-router"
        import { QueryClient } from "@tanstack/react-query"
        import { getStackClient } from "@/lib/stack-client"
        import { sitemapEntryToXmlString } from "@btst/stack/client"

        export const Route = createFileRoute("/sitemap.xml")({
          server: {
            handlers: {
              GET: async () => {
                const queryClient = new QueryClient()
                const stackClient = getStackClient(queryClient)
                const entries = await stackClient.generateSitemap()
                const xml = sitemapEntryToXmlString(entries)

                return new Response(xml, {
                  headers: {
                    "Content-Type": "application/xml; charset=utf-8",
                    "Cache-Control": "public, max-age=0, s-maxage=3600, stale-while-revalidate=86400",
                  },
                })
              },
            },
          },
        })
        ```
      </Tab>
    </Tabs>

    <Callout type="info">
      The `generateSitemap()` method automatically collects URLs from all registered plugins. Each plugin can contribute its own routes to the sitemap with appropriate metadata like priority and change frequency. This step is optional but recommended for SEO.
    </Callout>
  </Step>

  <Step>
    ### 🎉 That's it!

    Your setup is complete! Here's what you've configured:

    * ✅ Backend API handler that processes all plugin requests
    * ✅ Database adapter that connects plugins to your database
    * ✅ Client-side router with SSR support
    * ✅ React Query integration for data fetching
    * ✅ Framework-specific overrides

    **Next steps:**

    1. **Add plugins** to both backend and client configurations:
       * Backend: `plugins: { blog: blogBackendPlugin() }`
       * Client: `plugins: { blog: blogClientPlugin() }`

    2. **Visit your pages** at `/pages/*` to see plugin routes in action

    **Available plugins:**

    * `@btst/stack/plugins/blog` - Full-featured blog with markdown editor, SEO, and RSS. Learn more about the blog plugin [here](/plugins/blog).
    * More plugins coming soon!

    Each plugin provides everything you need: routes, API endpoints, database schemas, React components, and hooks - all working together seamlessly.

    ## Example Projects

    See complete working examples for each framework:

    * **[Next.js Example](https://github.com/better-stack-ai/better-stack/tree/main/examples/nextjs)** - Full Next.js App Router setup with blog and todo plugins
    * **[React Router Example](https://github.com/better-stack-ai/better-stack/tree/main/examples/react-router)** - React Router v7 setup with SSR support
    * **[TanStack Start Example](https://github.com/better-stack-ai/better-stack/tree/main/examples/tanstack)** - TanStack Router setup with file-based routing

    Each example includes complete configuration, plugin setup, and demonstrates framework-specific patterns.
  </Step>
</Steps>


# Shadcn Registry (/shadcn-registry)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import { Card, Cards } from "fumadocs-ui/components/card";
import { BookOpen, Bot, Database, FileText, Layout, Columns3 } from "lucide-react";

Every BTST plugin ships its page components as a [shadcn v4 registry](https://ui.shadcn.com/docs/registry) block. This lets you **eject the entire view layer** into your own codebase and customize it freely — while all data-fetching, API logic, hooks, and routing stay untouched inside `@btst/stack`.

## How it works

The registry approach separates two concerns:

| Layer                                | Where it lives after ejection                                        |
| ------------------------------------ | -------------------------------------------------------------------- |
| **View** (page components, styles)   | Your repo at `src/components/btst/{plugin}/client/`                  |
| **Data** (hooks, API calls, routing) | `@btst/stack/plugins/{plugin}/client/hooks` (npm package, unchanged) |

Installing a registry block copies React component source files into your project. You own those files and can edit them however you like. The hooks they import remain in the npm package, so you always get data-layer bug fixes and new features via a normal `npm update`.

## Install a plugin's UI

Pick the plugin you want to customize:

<Cards>
  <Card title="Blog" href="/plugins/blog#shadcn-registry" icon={<BookOpen size={20} />} description="Posts list, post detail, editor, drafts, tag pages" />

  <Card title="AI Chat" href="/plugins/ai-chat#shadcn-registry" icon={<Bot size={20} />} description="Chat home, conversation pages" />

  <Card title="CMS" href="/plugins/cms#shadcn-registry" icon={<Database size={20} />} description="Dashboard, content list, editor pages" />

  <Card title="Form Builder" href="/plugins/form-builder#shadcn-registry" icon={<FileText size={20} />} description="Form list, editor, submissions pages" />

  <Card title="UI Builder" href="/plugins/ui-builder#shadcn-registry" icon={<Layout size={20} />} description="Page list, page builder editor" />

  <Card title="Kanban" href="/plugins/kanban#shadcn-registry" icon={<Columns3 size={20} />} description="Boards list, board detail page" />
</Cards>

Or install a single plugin's UI directly:

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    # Blog
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json

    # AI Chat
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json

    # CMS
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json

    # Form Builder
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json

    # UI Builder
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json

    # Kanban
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    # Blog
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json

    # AI Chat
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json

    # CMS
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json

    # Form Builder
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json

    # UI Builder
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json

    # Kanban
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    # Blog
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json

    # AI Chat
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json

    # CMS
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json

    # Form Builder
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json

    # UI Builder
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json

    # Kanban
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>
</Tabs>

## Wire up ejected components

After the install, import your ejected components and pass them to the client plugin via `pageComponents`. Any key you omit falls back to the built-in default, so you only need to override the pages you actually want to change.

### Blog

```tsx title="lib/stack-client.tsx"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"
import { HomePageComponent } from "@/components/btst/blog/client/components/pages/home-page"
import { PostPageComponent } from "@/components/btst/blog/client/components/pages/post-page"

blogClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  siteBaseURL: "...",
  siteBasePath: "/pages",
  queryClient,
  pageComponents: {
    posts: HomePageComponent,    // published posts list
    post: PostPageComponent,     // single post detail
    // drafts | newPost | editPost | tag — omit to keep defaults
  },
})
```

### AI Chat

```tsx title="lib/stack-client.tsx"
import { aiChatClientPlugin } from "@btst/stack/plugins/ai-chat/client"
import { ChatPageComponent } from "@/components/btst/ai-chat/client/components/pages/chat-page"
import { ChatConversationPageComponent } from "@/components/btst/ai-chat/client/components/pages/chat-conversation-page"

aiChatClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    chat: ChatPageComponent,                         // chat home page
    chatConversation: ChatConversationPageComponent, // conversation page (authenticated mode)
  },
})
```

### CMS

```tsx title="lib/stack-client.tsx"
import { cmsClientPlugin } from "@btst/stack/plugins/cms/client"
import { DashboardPageComponent } from "@/components/btst/cms/client/components/pages/dashboard-page"
import { ContentListPageComponent } from "@/components/btst/cms/client/components/pages/content-list-page"

cmsClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    dashboard: DashboardPageComponent,      // CMS dashboard
    contentList: ContentListPageComponent,  // content list per type
    // newContent | editContent — omit to keep defaults
  },
})
```

### Form Builder

```tsx title="lib/stack-client.tsx"
import { formBuilderClientPlugin } from "@btst/stack/plugins/form-builder/client"
import { FormListPageComponent } from "@/components/btst/form-builder/client/components/pages/form-list-page"
import { EditFormPageComponent } from "@/components/btst/form-builder/client/components/pages/edit-form-page"

formBuilderClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    formList: FormListPageComponent, // form list page
    editForm: EditFormPageComponent, // form editor
    // newForm | submissions — omit to keep defaults
  },
})
```

### UI Builder

```tsx title="lib/stack-client.tsx"
import { uiBuilderClientPlugin } from "@btst/stack/plugins/ui-builder/client"
import { PageListPageComponent } from "@/components/btst/ui-builder/client/components/pages/page-list-page"
import { EditPagePageComponent } from "@/components/btst/ui-builder/client/components/pages/edit-page-page"

uiBuilderClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    pageList: PageListPageComponent, // page list
    editPage: EditPagePageComponent, // page builder editor
    // newPage — omit to keep default
  },
})
```

### Kanban

```tsx title="lib/stack-client.tsx"
import { kanbanClientPlugin } from "@btst/stack/plugins/kanban/client"
import { BoardsPageComponent } from "@/components/btst/kanban/client/components/pages/boards-page"
import { BoardPageComponent } from "@/components/btst/kanban/client/components/pages/board-page"

kanbanClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    boards: BoardsPageComponent, // boards list
    board: BoardPageComponent,   // board detail
    // newBoard — omit to keep default
  },
})
```

## Available `pageComponents` keys

| Plugin       | Key                | Props                              | Description           |
| ------------ | ------------------ | ---------------------------------- | --------------------- |
| Blog         | `posts`            | —                                  | Published posts list  |
| Blog         | `drafts`           | —                                  | Drafts list           |
| Blog         | `newPost`          | —                                  | New post editor       |
| Blog         | `post`             | `{ slug: string }`                 | Single post detail    |
| Blog         | `editPost`         | `{ slug: string }`                 | Edit post editor      |
| Blog         | `tag`              | `{ tagSlug: string }`              | Tag + tagged posts    |
| AI Chat      | `chat`             | —                                  | Chat home page        |
| AI Chat      | `chatConversation` | `{ conversationId: string }`       | Conversation detail   |
| CMS          | `dashboard`        | —                                  | CMS dashboard         |
| CMS          | `contentList`      | `{ typeSlug: string }`             | Content list per type |
| CMS          | `newContent`       | `{ typeSlug: string }`             | New content editor    |
| CMS          | `editContent`      | `{ typeSlug: string; id: string }` | Edit content editor   |
| Form Builder | `formList`         | —                                  | Form list             |
| Form Builder | `newForm`          | —                                  | New form editor       |
| Form Builder | `editForm`         | `{ id: string }`                   | Form editor           |
| Form Builder | `submissions`      | `{ formId: string }`               | Form submissions      |
| UI Builder   | `pageList`         | —                                  | Page list             |
| UI Builder   | `newPage`          | —                                  | New page builder      |
| UI Builder   | `editPage`         | `{ id: string }`                   | Page builder editor   |
| Kanban       | `boards`           | —                                  | Boards list           |
| Kanban       | `newBoard`         | —                                  | New board             |
| Kanban       | `board`            | `{ boardId: string }`              | Board detail          |

## What the registry installs

<Callout type="info">
  **Hooks are never included.** Components import hooks from `@btst/stack/plugins/{plugin}/client/hooks`. Only the view layer is ejected.
</Callout>

The shadcn CLI reads the registry JSON, resolves all dependencies, and copies source files into your project. The directory structure is preserved exactly, so all relative imports between components remain valid with no manual path-fixing required.

Standard shadcn components (Button, Dialog, etc.) referenced by the ejected files are listed as `registryDependencies` — the CLI installs them automatically.

## Rebuilding the registry

The registry JSON files are generated from source. If you are working in the monorepo and have changed plugin components, regenerate them before committing:

```bash
pnpm --filter @btst/stack build-registry
```


# Standalone Components (/standalone-components)

import { Callout } from "fumadocs-ui/components/callout";
import { Tabs, Tab } from "fumadocs-ui/components/tabs";

BTST ships a set of UI components that can be used **without setting up any plugin**. Each is available as its own import path from `@btst/stack`, so you only bundle what you use.

| Import path                                | CSS export                            | What you get                            |
| ------------------------------------------ | ------------------------------------- | --------------------------------------- |
| `@btst/stack/components/auto-form`         | —                                     | `AutoForm`, `AutoFormSubmit`            |
| `@btst/stack/components/stepped-auto-form` | —                                     | `SteppedAutoForm`                       |
| `@btst/stack/components/form-builder`      | —                                     | `FormBuilder` and schema helpers        |
| `@btst/stack/components/markdown`          | `@btst/stack/components/markdown/css` | `MarkdownContent`, `MarkdownEditor`     |
| `@btst/stack/components/multi-select`      | —                                     | `MultipleSelector`                      |
| `@btst/stack/components/search-select`     | —                                     | `SearchSelect`                          |
| `@btst/stack/components/empty`             | —                                     | `Empty`, `EmptyHeader`, `EmptyTitle`, … |

***

## AutoForm

Generate forms automatically from Zod schemas. [Learn more →](https://github.com/better-stack-ai/form-builder)

```ts
import { AutoForm, AutoFormSubmit } from "@btst/stack/components/auto-form"
import type { FieldConfig, Dependency } from "@btst/stack/components/auto-form"
```

```tsx
<AutoForm
  formSchema={z.object({
    name: z.string().min(1),
    email: z.string().email(),
  })}
  onSubmit={(values) => console.log(values)}
>
  <AutoFormSubmit>Submit</AutoFormSubmit>
</AutoForm>
```

### Stepped AutoForm

Multi-step wizard variant. [Learn more →](https://github.com/better-stack-ai/form-builder)

```ts
import { SteppedAutoForm } from "@btst/stack/components/stepped-auto-form"
import type { SteppedAutoFormProps, StepperComponentProps } from "@btst/stack/components/stepped-auto-form"
```

***

## FormBuilder

A JSON-schema-driven form editor — lets users visually create form definitions that can be stored and later rendered. [Learn more →](https://github.com/better-stack-ai/form-builder)

```ts
import {
  FormBuilder,
  defaultComponents,
  objectFieldDefinition,
  arrayFieldDefinition,
  defineComponent,
  baseMetaSchema,
  baseMetaSchemaWithPlaceholder,
} from "@btst/stack/components/form-builder"
import type {
  FormBuilderComponentDefinition,
  FormBuilderField,
  JSONSchema,
  JSONSchemaProperty,
} from "@btst/stack/components/form-builder"
```

```tsx
<FormBuilder
  schema={currentSchema}
  onChange={(schema) => setSchema(schema)}
  components={defaultComponents}
/>
```

<Callout type="info">
  The full **Form Builder plugin** (`@btst/stack/plugins/form-builder`) layers data persistence, API routes, and submissions on top of this component. Use the standalone import when you want to manage your own storage.
</Callout>

***

## Markdown

### MarkdownContent

Renders Markdown/MDX to HTML with syntax highlighting:

```ts
import { MarkdownContent } from "@btst/stack/components/markdown"
import type { MarkdownContentProps } from "@btst/stack/components/markdown"
```

```tsx
<MarkdownContent content="# Hello\n\nSome **bold** text." />
```

Import the stylesheet in your root CSS (or layout):

```css
@import "@btst/stack/components/markdown/css";
```

### MarkdownEditor

A rich Markdown editor powered by Milkdown/Crepe with optional image upload:

```ts
import { MarkdownEditor } from "@btst/stack/components/markdown"
import type { MarkdownEditorProps } from "@btst/stack/components/markdown"
```

```tsx
<MarkdownEditor
  value={content}
  onChange={(markdown) => setContent(markdown)}
  placeholder="Write something..."
  uploadImage={async (file) => {
    const url = await uploadToStorage(file)
    return url
  }}
/>
```

#### MarkdownEditor Props

| Prop          | Type                              | Default                | Description                                      |
| ------------- | --------------------------------- | ---------------------- | ------------------------------------------------ |
| `value`       | `string`                          | `""`                   | Current Markdown content                         |
| `onChange`    | `(markdown: string) => void`      | —                      | Called on every change                           |
| `className`   | `string`                          | —                      | Additional CSS classes                           |
| `placeholder` | `string`                          | `"Write something..."` | Placeholder when empty                           |
| `uploadImage` | `(file: File) => Promise<string>` | —                      | Enables image upload; must return the public URL |

The stylesheet also covers the Markdown editor. Import once from `@btst/stack/components/markdown/css`.

***

## MultipleSelector

A multi-select combobox with search, async options, and tag-style values:

```ts
import { MultipleSelector } from "@btst/stack/components/multi-select"
import type { Option, MultipleSelectorRef } from "@btst/stack/components/multi-select"
```

```tsx
const options: Option[] = [
  { value: "react", label: "React" },
  { value: "vue", label: "Vue" },
  { value: "svelte", label: "Svelte" },
]

<MultipleSelector
  options={options}
  value={selected}
  onChange={setSelected}
  placeholder="Select frameworks..."
/>
```

***

## SearchSelect

A searchable single-value select powered by Radix + cmdk:

```ts
import { SearchSelect } from "@btst/stack/components/search-select"
```

```tsx
<SearchSelect
  options={[
    { value: "us", label: "United States" },
    { value: "gb", label: "United Kingdom" },
  ]}
  value={country}
  onValueChange={setCountry}
  placeholder="Select a country..."
/>
```

***

## Empty

Composable empty-state UI components:

```ts
import {
  Empty,
  EmptyHeader,
  EmptyTitle,
  EmptyDescription,
  EmptyContent,
  EmptyMedia,
} from "@btst/stack/components/empty"
```

```tsx
<Empty>
  <EmptyMedia>
    <InboxIcon className="size-12 text-muted-foreground" />
  </EmptyMedia>
  <EmptyHeader>
    <EmptyTitle>No results</EmptyTitle>
    <EmptyDescription>Try adjusting your search or filters.</EmptyDescription>
  </EmptyHeader>
  <EmptyContent>
    <Button>Clear filters</Button>
  </EmptyContent>
</Empty>
```


# Database Adapters (/databases/adapters)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";

BTST uses a flexible adapter system that allows you to connect to any database through your preferred ORM. The adapter acts as a bridge between BTST's unified data layer and your database of choice.

## Package Overview

BTST consists of separate npm packages under the `@btst` namespace:

* **`@btst/stack`** - Core package (install this first)
* **`@btst/adapter-*`** - Database adapters (install one based on your ORM)
* **`@btst/cli`** - CLI tools for schema generation (dev dependency)
* **`@btst/db`** - Internal database abstraction layer (installed as a dependency of other packages)

See the [Installation guide](/installation) for setup instructions.

## Available Adapters

BTST provides official adapters for popular ORMs:

* **Prisma** - `@btst/adapter-prisma` - Supports PostgreSQL, MySQL, SQLite, CockroachDB, and MongoDB
* **Drizzle** - `@btst/adapter-drizzle` - Supports PostgreSQL, MySQL, SQLite, and more
* **Kysely** - `@btst/adapter-kysely` - Supports PostgreSQL, MySQL, SQLite, and more
* **MongoDB** - `@btst/adapter-mongodb` - Native MongoDB driver support
* **Memory** - `@btst/adapter-memory` - In-memory adapter for development and testing

## Installation

Adapters are separate packages that must be installed alongside `@btst/stack`:

```bash
# Install core package
npm install @btst/stack

# Install your chosen adapter
npm install @btst/adapter-prisma
```

See the [Installation guide](/installation#install-database-adapter) for detailed adapter setup instructions.

## Usage

When you configure BTST, the `stack()` function collects all plugin database schemas and merges them into a unified schema. The adapter function receives this merged schema and returns an adapter that translates BTST's database operations to your ORM.

<Tabs groupId="adapter-type" items={["prisma", "drizzle", "kysely", "mongodb", "memory"]} persist>
  <Tab value="prisma">
    ```ts title="lib/stack.ts"
    import { stack } from "@btst/stack"
    import { createPrismaAdapter } from "@btst/adapter-prisma"
    import { PrismaClient } from "@prisma/client"

    const prisma = new PrismaClient()

    const { handler, dbSchema } = stack({
      basePath: "/api/data",
      plugins: {
        // Your plugins here
      },
      // The adapter receives the merged db schema from all plugins
      adapter: (db) => createPrismaAdapter(prisma, db, { 
        provider: "postgresql" // or "mysql", "sqlite", "cockroachdb", "mongodb"
      })
    })

    export { handler, dbSchema }
    ```
  </Tab>

  <Tab value="drizzle">
    ```ts title="lib/stack.ts"
    import { stack } from "@btst/stack"
    import { createDrizzleAdapter } from "@btst/adapter-drizzle"
    import { drizzle } from "drizzle-orm/postgres-js" // or "drizzle-orm/mysql2", "drizzle-orm/better-sqlite3", etc.
    import postgres from "postgres"

    const client = postgres(process.env.DATABASE_URL!)
    const drizzleDb = drizzle(client)

    const { handler, dbSchema } = stack({
      basePath: "/api/data",
      plugins: {
        // Your plugins here
      },
      adapter: (db) => createDrizzleAdapter(drizzleDb, db, {})
    })

    export { handler, dbSchema }
    ```
  </Tab>

  <Tab value="kysely">
    ```ts title="lib/stack.ts"
    import { stack } from "@btst/stack"
    import { createKyselyAdapter } from "@btst/adapter-kysely"
    import { Kysely, PostgresDialect } from "kysely"
    import { Pool } from "pg"

    const kyselyDb = new Kysely({
      dialect: new PostgresDialect({
        pool: new Pool({ connectionString: process.env.DATABASE_URL })
      })
    })

    const { handler, dbSchema } = stack({
      basePath: "/api/data",
      plugins: {
        // Your plugins here
      },
      adapter: (db) => createKyselyAdapter(kyselyDb, db, {})
    })

    export { handler, dbSchema }
    ```
  </Tab>

  <Tab value="mongodb">
    ```ts title="lib/stack.ts"
    import { stack } from "@btst/stack"
    import { createMongodbAdapter } from "@btst/adapter-mongodb"
    import { MongoClient } from "mongodb"

    const client = new MongoClient(process.env.MONGODB_URI!)
    const mongoDb = client.db()

    const { handler, dbSchema } = stack({
      basePath: "/api/data",
      plugins: {
        // Your plugins here
      },
      adapter: (db) => createMongodbAdapter(mongoDb, db, {})
    })

    export { handler, dbSchema }
    ```
  </Tab>

  <Tab value="memory">
    ```ts title="lib/stack.ts"
    // IMPORTANT: Memory adapter is used for development and testing only
    import { stack } from "@btst/stack"
    import { createMemoryAdapter } from "@btst/adapter-memory"

    const { handler, dbSchema } = stack({
      basePath: "/api/data",
      plugins: {
        // Your plugins here
      },
      adapter: (db) => createMemoryAdapter(db)({})
    })

    export { handler, dbSchema }
    ```
  </Tab>
</Tabs>

The `adapter` function receives the merged database schema (`db`) containing all tables and relationships from your plugins, and returns an adapter instance that implements the common adapter interface.

<Callout type="info">
  To learn more about generating database schemas and running migrations, see the [CLI documentation](/cli).
</Callout>

### How the Adapter Function Works

The adapter pattern follows this flow:

1. `stack()` merges all plugin schemas into a unified `db` object
2. Your `adapter` function receives this `db` object
3. The adapter creator function (e.g., `createPrismaAdapter`, `createDrizzleAdapter`) returns an adapter instance
4. This adapter instance implements the common interface (create, update, findOne, etc.)

The adapter function signature allows the adapter to be configured with both BTST's schema and any ORM-specific options.

## Database Schema Generation

After configuring your adapter, you'll need to generate database schemas and migrations. BTST provides a CLI tool to help with this process.

See the [CLI documentation](/cli) for detailed information on generating schemas for Prisma, Drizzle, and Kysely, as well as running migrations.

## How Data Layer Works

BTST's data layer is built on [Better DB](https://github.com/better-stack-ai/better-auth/tree/main/packages/btst), a fork of better-auth's database layer. Better DB is a type-safe database abstraction layer that provides:

* **Unified Schema Definition**: Plugins define their database schemas using Better DB's schema definition API
* **Schema Composition**: All plugin schemas are automatically merged into a single unified schema
* **Type-Safe Operations**: Full TypeScript support for all database operations
* **Adapter Abstraction**: Works with any database through adapters

### How Adapters Work

Adapters implement a common interface that provides methods for:

* `create` - Insert new records
* `update` - Update existing records
* `updateMany` - Bulk update operations
* `delete` - Delete records
* `deleteMany` - Bulk delete operations
* `findOne` - Find a single record (supports `join` option)
* `findMany` - Query multiple records (supports `join` option)
* `count` - Count records matching criteria

Each adapter translates these operations to the appropriate ORM calls (Prisma, Drizzle, Kysely, MongoDB, etc.).

## Relational Queries with Join

Adapters support a `join` option for `findOne` and `findMany` operations, allowing you to fetch related records in a single query.

### Defining Foreign Key Relationships

To use joins, you must define foreign key relationships in your schema using the `references` property:

```ts title="db/schema.ts"
import { createDbPlugin } from "@btst/db";

export const mySchema = createDbPlugin("myPlugin", {
  post: {
    modelName: "post",
    fields: {
      title: { type: "string", required: true },
      // ... other fields
    },
  },
  tag: {
    modelName: "tag",
    fields: {
      name: { type: "string", required: true },
      // ... other fields
    },
  },
  postTag: {
    modelName: "postTag",
    fields: {
      postId: {
        type: "string",
        required: true,
        references: {
          model: "post",
          field: "id",
          onDelete: "cascade", // Optional: automatically delete when parent is deleted
        },
      },
      tagId: {
        type: "string",
        required: true,
        references: {
          model: "tag",
          field: "id",
          onDelete: "cascade",
        },
      },
    },
  },
});
```

### Using the Join Option

Once relationships are defined, you can use the `join` option to fetch related records:

```ts
// Fetch posts with their related postTag records
const posts = await adapter.findMany<Post & { postTag?: PostTag[] }>({
  model: "post",
  where: [{ field: "published", value: true }],
  join: {
    postTag: true, // Join the postTag model
  },
});

// Each post will have a `postTag` array with related records
posts.forEach(post => {
  console.log(post.title, post.postTag);
});
```

### Join Option Configuration

The `join` option accepts an object where keys are model names and values configure the join:

```ts
type JoinOption = {
  [model: string]: boolean | {
    limit?: number; // Limit the number of joined records
  };
};
```

Examples:

```ts
// Simple join - fetch all related records
join: { postTag: true }

// Limited join - fetch only first 5 related records
join: { postTag: { limit: 5 } }
```

### Cascade Delete

When you define `onDelete: "cascade"` on a foreign key reference, deleting the parent record will automatically delete all related child records:

```ts
// With cascade delete defined, this single operation
// also deletes all related postTag records automatically
await adapter.delete({
  model: "post",
  where: [{ field: "id", value: postId }],
});
```

Available `onDelete` options:

* `"cascade"` - Delete child records when parent is deleted
* `"set null"` - Set the foreign key to null when parent is deleted
* `"restrict"` - Prevent deletion if child records exist
* `"no action"` - No automatic action (database default)
* `"set default"` - Set the foreign key to its default value

## Using Other Better Auth Compatible Adapters

Better DB is a fork of better-auth's database layer, which means existing [better-auth adapters](https://www.better-auth.com/docs/concepts/database) can work with BTST with a small wrapper modification. The wrapper is necessary because BTST's plugin system merges schemas differently than better-auth plugins.

This allows you to leverage the wide ecosystem of better-auth adapters. The wrapper function needs to inject the Better DB schema into the better-auth adapter's plugin system so it can find your models. Here's an example of how `@btst/adapter-prisma` wraps better-auth's Prisma adapter:

```ts title="lib/adapters/prisma.ts"

export * from "better-auth/adapters/prisma";

import type { Adapter, DatabaseDefinition } from "@btst/db";
import { prismaAdapter, type PrismaConfig } from "better-auth/adapters/prisma";
import type { BetterAuthOptions } from "better-auth/types";

/**
 * Helper function to create a Prisma adapter with Better DB schema
 *
 * This handles passing the Better DB schema to the prismaAdapter
 * by injecting it as a plugin so Better Auth can find your models.
 */
export function createPrismaAdapter(
	prisma: any,
	db: DatabaseDefinition,
	config: PrismaConfig,
	options: BetterAuthOptions = {},
): (options: BetterAuthOptions) => Adapter {
	return (adapterOptions: BetterAuthOptions = {}) => {
		const mergedOptions = {
			...options,
			...adapterOptions,
			plugins: [
				...(options.plugins || []),
				...(adapterOptions.plugins || []),
				{
					id: "better-db-schema",
					schema: db.getSchema(),
				},
			],
		};
		return prismaAdapter(prisma, config)(mergedOptions);
	};
}
```

You can apply the same pattern to wrap other better-auth compatible adapters that are currently not exported by better-db.

## Better DB Package

Better DB is a fork of [better-auth](https://www.better-auth.com)'s database layer. For more information about the underlying data layer, see the [Better DB package](https://github.com/better-stack-ai/better-auth/tree/main/packages/btst) on GitHub. This package provides the core database abstraction that powers BTST's adapter system.


# AI Chat Demo (/demos/ai-chat)

A standalone Next.js demo showcasing the `ai-chat` plugin in **public mode** (no user accounts needed).

**What's included:**

* Streaming AI chat interface
* Suggested prompts pre-configured for exploring BTST
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

<Callout>
  To enable AI responses in StackBlitz, add your `OPENAI_API_KEY` to the `.env.local` file (copy from `.env.local.example`).
</Callout>

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/ai-chat?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/ai-chat?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/ai-chat?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fchat" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST AI Chat Demo" />


# Blog Demo (/demos/blog)

A standalone Next.js demo showcasing the `blog` plugin. Three sample posts are seeded automatically on startup.

**What's included:**

* Blog list page with search and tag filtering
* Individual post pages with Markdown rendering
* New post / edit post pages with the Markdown editor
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/blog?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/blog?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/blog?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fblog" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST Blog Demo" />


# CMS Demo (/demos/cms)

A standalone Next.js demo showcasing the `cms` plugin. An `Article` content type and 3 sample articles are seeded on startup.

**What's included:**

* CMS dashboard with content type list
* Content item list and editor with AutoForm
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/cms?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/cms?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/cms?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fcms" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST CMS Demo" />


# Form Builder Demo (/demos/form-builder)

A standalone Next.js demo showcasing the `form-builder` plugin. Two sample forms ("Contact Us" and "Feedback") are seeded on startup.

**What's included:**

* Form list page
* Visual form builder with drag-and-drop field ordering
* Public submission view for each form
* Submission history per form
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/form-builder?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/form-builder?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/form-builder?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fforms" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST Form Builder Demo" />


# Demos (/demos)

Each demo is a standalone Next.js project that showcases a BTST plugin with:

* **Seeded data** so you can explore immediately without any setup
* **API Docs** generated by the OpenAPI plugin (`/api/data/reference`)
* **Route Docs** generated by the Route Docs plugin (`/pages/route-docs`)
* **In-memory adapter** — all data is ephemeral and resets on server restart

| Demo                                     | Plugin                             | Start path            |
| ---------------------------------------- | ---------------------------------- | --------------------- |
| [Blog](/docs/demos/blog)                 | `@btst/stack/plugins/blog`         | `/pages/blog`         |
| [AI Chat](/docs/demos/ai-chat)           | `@btst/stack/plugins/ai-chat`      | `/pages/chat`         |
| [CMS](/docs/demos/cms)                   | `@btst/stack/plugins/cms`          | `/pages/cms`          |
| [Form Builder](/docs/demos/form-builder) | `@btst/stack/plugins/form-builder` | `/pages/form-builder` |
| [Kanban](/docs/demos/kanban)             | `@btst/stack/plugins/kanban`       | `/pages/kanban`       |
| [UI Builder](/docs/demos/ui-builder)     | `@btst/stack/plugins/ui-builder`   | `/pages/ui-builder`   |

### Running locally

Each demo is in the `demos/` folder of the monorepo:

```bash
cd demos/blog
pnpm install
pnpm dev
```


# Kanban Demo (/demos/kanban)

A standalone Next.js demo showcasing the `kanban` plugin. One demo board with 4 columns and 7 tasks is seeded on startup.

**What's included:**

* Boards list page
* Drag-and-drop Kanban board with task cards
* Task creation, editing, and priority management
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/kanban?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/kanban?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/kanban?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fkanban" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST Kanban Demo" />


# UI Builder Demo (/demos/ui-builder)

A standalone Next.js demo showcasing the `ui-builder` plugin backed by the `cms` plugin. A sample "Welcome" page is seeded with a hero and features layout.

**What's included:**

* Page list view
* Drag-and-drop page builder with component inspector
* Live preview of the rendered page
* API Docs at `/api/data/reference` (OpenAPI Scalar)
* Route Docs at `/pages/route-docs`

[Open in CodeSandbox →](https://codesandbox.io/p/devbox/github/better-stack-ai/better-stack/tree/main/demos/ui-builder?file=%2Flib%2Fstack.ts)
[Open in StackBlitz →](https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/ui-builder?startScript=dev\&file=lib%2Fstack.ts)

<iframe src="https://stackblitz.com/github/better-stack-ai/better-stack/tree/main/demos/ui-builder?startScript=dev&embed=1&file=lib%2Fstack.ts&view=preview&initialPath=%2Fpages%2Fui-builder" style={{width:"100%", height:"600px", border:"0", borderRadius:"4px"}} title="BTST UI Builder Demo" />


# AI Chat Plugin (/plugins/ai-chat)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import chatDemo from "../../../assets/chat-demo.png";
import chatDemo1 from "../../../assets/chat-demo-1.png";

<div className="grid grid-cols-1 lg:grid-cols-2 gap-2 my-2">
  <a href={chatDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={chatDemo} alt="AI Chat Plugin Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={chatDemo1.src} target="_blank" rel="noopener noreferrer">
    <Image src={chatDemo1} alt="AI Chat Plugin Demo - Conversation" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

[View interactive demo →](/demos/ai-chat)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

Follow these steps to add the AI Chat plugin to your BTST setup.

### 1. Add Plugin to Backend API

Import and register the AI Chat backend plugin in your `stack.ts` file:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { aiChatBackendPlugin } from "@btst/stack/plugins/ai-chat/api"
import { openai } from "@ai-sdk/openai"
// ... your adapter imports

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    aiChat: aiChatBackendPlugin({
      model: openai("gpt-4o"), // Or any LanguageModel from AI SDK
      mode: "authenticated", // "authenticated" (default) or "public"
      // Extract userId from request headers to scope conversations per user
      getUserId: async (ctx) => {
        const token = ctx.headers?.get("authorization")
        if (!token) return null // Deny access if no auth
        const user = await verifyToken(token) // Your auth logic
        return user?.id ?? null
      },
      systemPrompt: "You are a helpful assistant.", // Optional
      tools: {}, // Optional: AI SDK v5 tools
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

export { handler, dbSchema }
```

The `aiChatBackendPlugin()` accepts optional hooks for customizing behavior (authorization, logging, etc.).

<Callout type="info">
  **Model Configuration:** You can use any model from the AI SDK, including OpenAI, Anthropic, Google, and more. Make sure to install the corresponding provider package (e.g., `@ai-sdk/openai`) and set up your API keys in environment variables.
</Callout>

### 2. Add Plugin to Client

Register the AI Chat client plugin in your `stack-client.tsx` file:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { aiChatClientPlugin } from "@btst/stack/plugins/ai-chat/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () => 
  typeof window !== 'undefined' 
    ? (process.env.NEXT_PUBLIC_BASE_URL || window.location.origin)
    : (process.env.BASE_URL || "http://localhost:3000")

export const getStackClient = (queryClient: QueryClient, options?: { headers?: Headers }) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      aiChat: aiChatClientPlugin({
        // Required configuration
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient: queryClient,
        headers: options?.headers,
        // Mode should match backend config
        mode: "authenticated", // "authenticated" (default) or "public"
        // Optional: SEO configuration
        seo: {
          siteName: "My Chat App",
          description: "AI-powered chat assistant",
        },
      })
    }
  })
}
```

**Required configuration:**

* `apiBaseURL`: Base URL for API calls during SSR data prefetching (use environment variables for flexibility)
* `apiBasePath`: Path where your API is mounted (e.g., `/api/data`)
* `siteBaseURL`: Base URL of your site
* `siteBasePath`: Path where your pages are mounted (e.g., `/pages`)
* `queryClient`: React Query client instance

<Callout type="info">
  **Why configure API paths here?** This configuration is used by **server-side loaders** that prefetch data before your pages render. These loaders run outside of React Context, so they need direct configuration. You'll also provide `apiBaseURL` and `apiBasePath` again in the Provider overrides (Section 4) for **client-side components** that run during actual rendering.
</Callout>

### 3. Import Plugin CSS

Add the AI Chat plugin CSS to your global stylesheet:

```css title="app/globals.css"
@import "@btst/stack/plugins/ai-chat/css";
```

This includes all necessary styles for the chat components and markdown rendering.

### 4. Add Context Overrides

Configure framework-specific overrides in your `StackProvider`:

<Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
  <Tab value="next-js">
    ```tsx title="app/pages/layout.tsx"
    "use client"
    import { useState } from "react"
    import { StackProvider } from "@btst/stack/context"
    import { QueryClientProvider } from "@tanstack/react-query"
    import type { AiChatPluginOverrides } from "@btst/stack/plugins/ai-chat/client"
    import Link from "next/link"
    import Image from "next/image"
    import { useRouter } from "next/navigation"
    import { getOrCreateQueryClient } from "@/lib/query-client"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (process.env.NEXT_PUBLIC_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      "ai-chat": AiChatPluginOverrides
    }

    export default function Layout({ children }) {
      const router = useRouter()
      const [queryClient] = useState(() => getOrCreateQueryClient())
      const baseURL = getBaseURL()
      
      return (
        <QueryClientProvider client={queryClient}>
          <StackProvider<PluginOverrides>
            basePath="/pages"
            overrides={{
              "ai-chat": {
                mode: "authenticated", // Should match backend config
                apiBaseURL: baseURL,
                apiBasePath: "/api/data",
                navigate: (path) => router.push(path),
                refresh: () => router.refresh(),
                uploadFile: async (file) => {
                  // Implement your file upload logic
                  return "https://example.com/uploads/file.pdf"
                },
                Link: ({ href, ...props }) => <Link href={href || "#"} {...props} />,
                Image: (props) => <Image {...props} />,
              }
            }}
          >
            {children}
          </StackProvider>
        </QueryClientProvider>
      )
    }
    ```
  </Tab>

  <Tab value="react-router">
    ```tsx title="app/routes/pages/_layout.tsx"
    import { useState } from "react"
    import { Outlet, Link, useNavigate } from "react-router"
    import { StackProvider } from "@btst/stack/context"
    import { QueryClientProvider, QueryClient } from "@tanstack/react-query"
    import type { AiChatPluginOverrides } from "@btst/stack/plugins/ai-chat/client"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:5173")

    type PluginOverrides = {
      "ai-chat": AiChatPluginOverrides
    }

    export default function Layout() {
      const navigate = useNavigate()
      const [queryClient] = useState(() => new QueryClient())
      const baseURL = getBaseURL()
      
      return (
        <QueryClientProvider client={queryClient}>
          <StackProvider<PluginOverrides>
            basePath="/pages"
            overrides={{
              "ai-chat": {
                mode: "authenticated",
                apiBaseURL: baseURL,
                apiBasePath: "/api/data",
                navigate: (href) => navigate(href),
                uploadFile: async (file) => {
                  return "https://example.com/uploads/file.pdf"
                },
                Link: ({ href, children, className, ...props }) => (
                  <Link to={href || ""} className={className} {...props}>
                    {children}
                  </Link>
                ),
              }
            }}
          >
            <Outlet />
          </StackProvider>
        </QueryClientProvider>
      )
    }
    ```
  </Tab>

  <Tab value="tanstack">
    ```tsx title="src/routes/pages/route.tsx"
    import { useState } from "react"
    import { StackProvider } from "@btst/stack/context"
    import { QueryClientProvider, QueryClient } from "@tanstack/react-query"
    import type { AiChatPluginOverrides } from "@btst/stack/plugins/ai-chat/client"
    import { Link, useRouter, Outlet } from "@tanstack/react-router"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      "ai-chat": AiChatPluginOverrides
    }

    function Layout() {
      const router = useRouter()
      const [queryClient] = useState(() => new QueryClient())
      const baseURL = getBaseURL()

      return (
        <QueryClientProvider client={queryClient}>
          <StackProvider<PluginOverrides>
            basePath="/pages"
            overrides={{
              "ai-chat": {
                mode: "authenticated",
                apiBaseURL: baseURL,
                apiBasePath: "/api/data",
                navigate: (href) => router.navigate({ href }),
                uploadFile: async (file) => {
                  return "https://example.com/uploads/file.pdf"
                },
                Link: ({ href, children, className, ...props }) => (
                  <Link to={href} className={className} {...props}>
                    {children}
                  </Link>
                ),
              }
            }}
          >
            <Outlet />
          </StackProvider>
        </QueryClientProvider>
      )
    }
    ```
  </Tab>
</Tabs>

**Required overrides:**

* `apiBaseURL`: Base URL for API calls (used by client-side components during rendering)
* `apiBasePath`: Path where your API is mounted
* `navigate`: Function for programmatic navigation

**Optional overrides:**

* `mode`: Plugin mode (`"authenticated"` or `"public"`)
* `uploadFile`: Function to upload files and return their URL
* `allowedFileTypes`: Array of allowed file type categories (default: all types)
* `chatSuggestions`: Array of suggested prompts shown in empty chat state
* `Link`: Custom Link component (defaults to `<a>` tag)
* `Image`: Custom Image component (useful for Next.js Image optimization)
* `refresh`: Function to refresh server-side cache (useful for Next.js)
* `localization`: Custom localization strings
* `headers`: Headers to pass with API requests

<Callout type="warn">
  **Why provide API paths again?** You already configured these in Section 2, but that configuration is only available to **server-side loaders**. The overrides here provide the same values to **client-side components** (like hooks, forms, and UI) via React Context. These two contexts serve different phases: loaders prefetch data server-side before rendering, while components use data during actual rendering (both SSR and CSR).
</Callout>

### 5. Generate Database Schema

After adding the plugin, generate your database schema using the CLI:

```bash
npx @btst/cli generate --orm prisma --config lib/stack.ts --output prisma/schema.prisma
```

This will create the necessary database tables for conversations and messages. Run migrations as needed for your ORM.

For more details on the CLI and all available options, see the [CLI documentation](/cli).

## Congratulations, You're Done! 🎉

Your AI Chat plugin is now fully configured and ready to use! Here's a quick reference of what's available:

### Plugin Modes

The AI Chat plugin supports two distinct modes:

**Authenticated Mode (Default)**

* Conversation persistence in database
* User-scoped data via `getUserId`
* Full UI with sidebar and conversation history
* Routes: `/chat` (new/list) and `/chat/:id` (existing conversation)

**Public Mode**

* No persistence (stateless)
* Simple UI without sidebar
* Ideal for public-facing chatbots
* Single route: `/chat`

### API Endpoints

The AI Chat plugin provides the following API endpoints (mounted at your configured `apiBasePath`):

* **POST** `/chat` - Send a message and receive streaming response
* **GET** `/conversations` - List all conversations (authenticated mode only)
* **GET** `/conversations/:id` - Get a conversation with messages
* **POST** `/conversations` - Create a new conversation
* **PUT** `/conversations/:id` - Update (rename) a conversation
* **DELETE** `/conversations/:id` - Delete a conversation

### Page Routes

The AI Chat plugin automatically creates the following pages (mounted at your configured `siteBasePath`):

**Authenticated mode:**

* `/chat` - Start a new conversation (with sidebar showing history)
* `/chat/:id` - Resume an existing conversation

**Public mode:**

* `/chat` - Simple chat interface without history

### Features

* **Full-page Layout**: Responsive chat interface with collapsible sidebar
* **Conversation Sidebar**: View, rename, and delete past conversations
* **Streaming Responses**: Real-time streaming of AI responses using AI SDK v5
* **Markdown Support**: Full markdown rendering with code highlighting
* **File Uploads**: Attach images, PDFs, and text files to messages
* **Tools Support**: Use AI SDK v5 tools for function calling
* **Customizable Models**: Use any LanguageModel from the AI SDK
* **Authorization Hooks**: Add custom authentication and authorization logic
* **Localization**: Customize all UI strings

### Page Component Overrides

You can replace any built-in page with your own React component using the optional `pageComponents` field in `aiChatClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
aiChatClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the chat home page
    chat: MyCustomChatPage,
    // Replace the conversation page (authenticated mode only)
    // receives conversationId as a prop
    chatConversation: ({ conversationId }) => (
      <MyCustomConversationPage conversationId={conversationId} />
    ),
  },
})
```

### Adding Authorization

To add authorization rules and customize behavior, you can use the lifecycle hooks defined in the API Reference section below. These hooks allow you to control access to API endpoints, add logging, and customize the plugin's behavior to fit your application's needs.

## API Reference

### Backend (`@btst/stack/plugins/ai-chat/api`)

#### aiChatBackendPlugin

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/api/plugin.ts" name="aiChatBackendPlugin" />

#### AiChatBackendConfig

The backend plugin accepts a configuration object with the model, mode, and optional hooks:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/api/plugin.ts" name="AiChatBackendConfig" />

#### AiChatBackendHooks

Customize backend behavior with optional lifecycle hooks. All hooks are optional and allow you to add authorization, logging, and custom behavior:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/api/plugin.ts" name="AiChatBackendHooks" />

**Example usage:**

```ts title="lib/stack.ts"
import { aiChatBackendPlugin, type AiChatBackendHooks } from "@btst/stack/plugins/ai-chat/api"

const chatHooks: AiChatBackendHooks = {
  // Authorization hooks — throw to deny access
  onBeforeChat(messages, context) {
    const authHeader = context.headers?.get("authorization")
    if (!authHeader) throw new Error("Unauthorized")
  },
  async onBeforeListConversations(context) {
    if (!await isAuthenticated(context.headers as Headers))
      throw new Error("Unauthorized")
  },
  async onBeforeDeleteConversation(conversationId, context) {
    if (!await isAuthenticated(context.headers as Headers))
      throw new Error("Unauthorized")
  },
  // Lifecycle hooks
  onConversationCreated(conversation, context) {
    console.log("Conversation created:", conversation.id)
  },
  onAfterChat(conversationId, messages, context) {
    console.log("Chat completed:", conversationId, "messages:", messages.length)
  },
  // Error hooks
  onChatError(error, context) {
    console.error("Chat error:", error.message)
  },
}

const { handler, dbSchema } = stack({
  plugins: {
    aiChat: aiChatBackendPlugin({
      model: openai("gpt-4o"),
      hooks: chatHooks
    })
  },
  // ...
})
```

#### ChatApiContext

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/api/plugin.ts" name="ChatApiContext" />

### Client (`@btst/stack/plugins/ai-chat/client`)

#### aiChatClientPlugin

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/plugin.tsx" name="aiChatClientPlugin" />

#### AiChatClientConfig

The client plugin accepts a configuration object with required fields and optional SEO settings:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/plugin.tsx" name="AiChatClientConfig" />

**Example usage:**

```tsx title="lib/stack-client.tsx"
aiChat: aiChatClientPlugin({
  // Required configuration
  apiBaseURL: baseURL,
  apiBasePath: "/api/data",
  siteBaseURL: baseURL,
  siteBasePath: "/pages",
  queryClient: queryClient,
  headers: options?.headers,
  // Mode configuration
  mode: "authenticated",
  // Optional SEO configuration
  seo: {
    siteName: "My AI Assistant",
    description: "Chat with our AI assistant",
    locale: "en_US",
    defaultImage: `${baseURL}/og-image.png`,
  },
})
```

#### AiChatClientHooks

Customize client-side behavior with lifecycle hooks. These hooks are called during data fetching (both SSR and CSR):

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/plugin.tsx" name="AiChatClientHooks" />

**Example usage:**

```tsx title="lib/stack-client.tsx"
aiChat: aiChatClientPlugin({
  // ... rest of the config
  headers: options?.headers,
  hooks: {
    beforeLoadConversations: async (context) => {
      // Check if user is authenticated before loading
      if (!await isAuthenticated(context.headers))
        throw new Error("Unauthorized")
    },
    afterLoadConversation: async (conversation, id, context) => {
      // Log access for analytics
      console.log("User accessed conversation:", id)
    },
    onLoadError(error, context) {
      // Handle error - redirect to login
      redirect("/auth/sign-in")
    },
  }
})
```

#### LoaderContext

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/plugin.tsx" name="LoaderContext" />

#### RouteContext

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/plugin.tsx" name="RouteContext" />

#### AiChatPluginOverrides

Configure framework-specific overrides and route lifecycle hooks. All lifecycle hooks are optional:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/overrides.ts" name="AiChatPluginOverrides" />

**Example usage:**

```tsx
overrides={{
  "ai-chat": {
    // Required overrides
    apiBaseURL: baseURL,
    apiBasePath: "/api/data",
    navigate: (path) => router.push(path),
    // Optional overrides
    mode: "authenticated",
    uploadFile: async (file) => {
      const formData = new FormData()
      formData.append("file", file)
      const res = await fetch("/api/upload", { method: "POST", body: formData })
      const { url } = await res.json()
      return url
    },
    allowedFileTypes: ["image", "pdf", "text"], // Restrict allowed types
    // Suggested prompts shown in empty chat state
    chatSuggestions: [
      "What can you help me with?",
      "Tell me about your features",
      "How do I get started?",
    ],
    // Custom tool UI renderers (see "Custom Tool UI Renderers" section)
    toolRenderers: {
      getWeather: WeatherCard,
      searchDocs: SearchResultsRenderer,
    },
    // Optional lifecycle hooks
    onBeforeChatPageRendered: (context) => {
      // Check if user can view chat. Useful for SPA.
      // Throw to deny: throw new Error("Unauthorized")
    },
    onBeforeConversationPageRendered: (id, context) => {
      // Check if user can view this specific conversation.
      // Throw to deny: throw new Error("Unauthorized")
    },
  }
}}
```

### ChatLayout Component

The `ChatLayout` component provides a ready-to-use chat interface. It can be used directly for custom integrations or public mode with persistence:

```tsx
import { ChatLayout, type ChatLayoutProps, type UIMessage } from "@btst/stack/plugins/ai-chat/client"
```

#### ChatLayoutProps

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/components/chat-layout.tsx" name="ChatLayoutProps" />

#### Widget layout — built-in trigger (default)

The default widget mode manages its own open/close state and renders a floating trigger button. Drop it anywhere in your layout and it just works:

```tsx
<ChatLayout
  apiBaseURL={baseURL}
  apiBasePath="/api/data"
  layout="widget"
  widgetHeight="520px"
/>
```

#### Widget layout — externally controlled (no trigger)

Use `defaultOpen` and `showTrigger={false}` when your own UI handles opening and closing — for example, a Next.js [intercepting route](https://nextjs.org/docs/app/building-your-application/routing/intercepting-routes) modal or a custom dialog. The chat panel is immediately visible and the built-in trigger button is not rendered:

```tsx
{/* Rendered inside a modal/dialog that you control */}
<ChatLayout
  apiBaseURL={baseURL}
  apiBasePath="/api/data"
  layout="widget"
  widgetHeight="500px"
  defaultOpen={true}
  showTrigger={false}
/>
```

**Next.js parallel-routes + intercepting-routes pattern** — a common way to display the widget as a modal overlay while keeping a floating button on every page:

```
app/
  @chatWidget/
    default.tsx          ← floating button (Link to /chat)
    loading.tsx          ← loading overlay
    (.)chat/
      page.tsx           ← intercepting route: renders modal with ChatLayout
  chat/
    page.tsx             ← full-page fallback (hard nav / refresh)
  layout.tsx             ← passes chatWidget slot into the body
```

```tsx title="app/@chatWidget/default.tsx"
"use client";
import Link from "next/link";
import { BotIcon } from "lucide-react";

export default function ChatWidgetButton() {
  return (
    <Link href="/chat" className="fixed bottom-6 right-6 z-50 ...">
      <BotIcon className="size-8" />
    </Link>
  );
}
```

```tsx title="app/@chatWidget/(.)chat/page.tsx"
"use client";
import { useRouter } from "next/navigation";
import { StackProvider } from "@btst/stack/context";
import { ChatLayout } from "@btst/stack/plugins/ai-chat/client";

const getBaseURL = () =>
  typeof window !== "undefined"
    ? (process.env.NEXT_PUBLIC_BASE_URL || window.location.origin)
    : (process.env.BASE_URL || "http://localhost:3000");

export default function ChatModal() {
  const router = useRouter();
  const baseURL = getBaseURL();
  return (
    {/* Backdrop */}
    <div className="fixed inset-0 z-50 bg-black/50" onClick={() => router.back()}>
      {/* Modal card */}
      <div className="..." onClick={(e) => e.stopPropagation()}>
        <StackProvider ...>
          {/* Panel is pre-opened; no trigger button rendered */}
          <ChatLayout
            apiBaseURL={baseURL}
            apiBasePath="/api/data"
            layout="widget"
            defaultOpen={true}
            showTrigger={false}
          />
        </StackProvider>
      </div>
    </div>
  );
}
```

**Example usage with localStorage persistence:**

```tsx
<ChatLayout
  apiBaseURL={baseURL}
  apiBasePath="/api/data"
  layout="widget"
  widgetHeight="500px"
  initialMessages={savedMessages}
  onMessagesChange={(messages) => localStorage.setItem("chat", JSON.stringify(messages))}
/>
```

## React Data Hooks and Types

You can import the hooks from `"@btst/stack/plugins/ai-chat/client/hooks"` to use in your components.

```tsx
import {
  useConversations,
  useConversation,
  useSuspenseConversations,
  useSuspenseConversation,
  useCreateConversation,
  useRenameConversation,
  useDeleteConversation,
} from "@btst/stack/plugins/ai-chat/client/hooks"
```

### UseConversationsOptions

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/hooks/chat-hooks.tsx" name="UseConversationsOptions" />

### UseConversationsResult

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/hooks/chat-hooks.tsx" name="UseConversationsResult" />

### UseConversationOptions

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/hooks/chat-hooks.tsx" name="UseConversationOptions" />

### UseConversationResult

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/hooks/chat-hooks.tsx" name="UseConversationResult" />

**Example usage:**

```tsx
import {
  useConversations,
  useConversation,
  useCreateConversation,
  useRenameConversation,
  useDeleteConversation,
} from "@btst/stack/plugins/ai-chat/client/hooks"

function ConversationsList() {
  // List all conversations
  const { conversations, isLoading, error, refetch } = useConversations()

  // Get single conversation with messages
  const { conversation } = useConversation(selectedId)

  // Mutations
  const createMutation = useCreateConversation()
  const renameMutation = useRenameConversation()
  const deleteMutation = useDeleteConversation()

  const handleCreate = async () => {
    const newConv = await createMutation.mutateAsync({ title: "New Chat" })
    // Navigate to new conversation
  }

  const handleRename = async (id: string, newTitle: string) => {
    await renameMutation.mutateAsync({ id, title: newTitle })
  }

  const handleDelete = async (id: string) => {
    await deleteMutation.mutateAsync({ id })
  }

  // ... render conversations
}
```

## Model & Tools Configuration

### Using Different Models

```ts title="lib/stack.ts"
import { openai } from "@ai-sdk/openai"
import { anthropic } from "@ai-sdk/anthropic"
import { google } from "@ai-sdk/google"

// Use OpenAI
aiChat: aiChatBackendPlugin({
  model: openai("gpt-4o"),
})

// Or use Anthropic
aiChat: aiChatBackendPlugin({
  model: anthropic("claude-3-5-sonnet-20241022"),
})

// Or use Google
aiChat: aiChatBackendPlugin({
  model: google("gemini-1.5-pro"),
})
```

### Adding Tools

Use AI SDK v5 tools for function calling:

```ts title="lib/stack.ts"
import { tool } from "ai"
import { z } from "zod"

const weatherTool = tool({
  description: "Get the current weather in a location",
  inputSchema: z.object({
    location: z.string().describe("The city and state"),
  }),
  execute: async ({ location }) => {
    // Your implementation
    return { temperature: 72, condition: "sunny" }
  },
})

aiChat: aiChatBackendPlugin({
  model: openai("gpt-4o"),
  tools: {
    getWeather: weatherTool,
  },
})
```

### Custom Tool UI Renderers

By default, tool calls are displayed using a collapsible accordion that shows the tool name, status, input, and output. You can customize this UI by providing custom renderers for specific tools via the `toolRenderers` override.

#### Default Tool UI

The default `ToolCallDisplay` component shows:

* Tool name with status indicator (loading spinner, checkmark, or error icon)
* Collapsible accordion to inspect tool call details
* Input arguments passed to the tool
* Output returned by the tool (when complete)
* Error message (if tool execution failed)

#### Custom Tool Renderers

Provide custom UI components for specific tools using the `toolRenderers` override. Each key should match the tool name from your backend configuration:

```tsx title="app/pages/layout.tsx"
import type { AiChatPluginOverrides, ToolCallProps } from "@btst/stack/plugins/ai-chat/client"

// Custom weather card component
function WeatherCard({ input, output, isLoading }: ToolCallProps<{ location: string }, { temperature: number; condition: string }>) {
  if (isLoading) {
    return (
      <div className="p-4 border rounded-lg animate-pulse">
        <div className="h-4 w-24 bg-muted rounded" />
      </div>
    )
  }
  
  if (!output) return null
  
  return (
    <div className="p-4 border rounded-lg bg-gradient-to-r from-blue-50 to-blue-100">
      <h4 className="font-medium">{input?.location}</h4>
      <p className="text-2xl font-bold">{output.temperature}°F</p>
      <p className="text-muted-foreground">{output.condition}</p>
    </div>
  )
}

// In your layout
<StackProvider<PluginOverrides>
  basePath="/pages"
  overrides={{
    "ai-chat": {
      apiBaseURL: baseURL,
      apiBasePath: "/api/data",
      navigate: (path) => router.push(path),
      // Custom tool renderers
      toolRenderers: {
        getWeather: WeatherCard,
        searchDocs: ({ input, output, isLoading }) => (
          <SearchResultsCard query={input?.query} results={output} loading={isLoading} />
        ),
      },
    }
  }}
>
  {children}
</StackProvider>
```

#### ToolCallProps

Each custom renderer receives these props:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/overrides.ts" name="ToolCallProps" />

#### ToolCallState

The possible states of a tool call:

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/overrides.ts" name="ToolCallState" />

#### Using the Default ToolCallDisplay

You can also import and use the default `ToolCallDisplay` component in your custom renderers as a fallback:

```tsx
import { ToolCallDisplay, type ToolCallProps } from "@btst/stack/plugins/ai-chat/client"

function MyCustomToolRenderer(props: ToolCallProps) {
  // Custom rendering for specific states
  if (props.state === "output-available" && props.output) {
    return <MyCustomOutput data={props.output} />
  }
  
  // Fall back to default display for other states
  return <ToolCallDisplay {...props} />
}
```

## Public Mode Configuration

For public chatbots without user authentication:

### Backend Setup

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { aiChatBackendPlugin } from "@btst/stack/plugins/ai-chat/api"
import { openai } from "@ai-sdk/openai"

// Example rate limiter (implement your own)
const rateLimiter = new Map<string, number>()

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    aiChat: aiChatBackendPlugin({
      model: openai("gpt-4o"),
      mode: "public", // Stateless mode - no persistence
      systemPrompt: "You are a helpful customer support bot.",
      hooks: {
        onBeforeChat: async (messages, ctx) => {
          // Implement rate limiting
          const ip = ctx.headers?.get("x-forwarded-for") || "unknown"
          const requests = rateLimiter.get(ip) || 0
          if (requests > 10) {
            throw new Error("Rate limit exceeded")
          }
          rateLimiter.set(ip, requests + 1)
        },
      },
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})
```

### Client Setup

```tsx title="lib/stack-client.tsx"
aiChat: aiChatClientPlugin({
  apiBaseURL: baseURL,
  apiBasePath: "/api/data",
  siteBaseURL: baseURL,
  siteBasePath: "/pages",
  queryClient: queryClient,
  mode: "public", // Must match backend
})
```

### Context Overrides

```tsx
overrides={{
  "ai-chat": {
    mode: "public",
    apiBaseURL: baseURL,
    apiBasePath: "/api/data",
    navigate: (path) => router.push(path),
    // No uploadFile needed in public mode typically
  }
}}
```

<Callout type="info">
  In public mode, the sidebar is hidden, conversation history is not saved to the database, and only the `/chat` route is available.
</Callout>

### Local Storage Persistence

By default, public mode is completely stateless - messages are lost on page refresh. However, you can persist conversations to localStorage (or any storage mechanism) using the `initialMessages` and `onMessagesChange` props on `ChatLayout`:

```tsx title="components/public-chat.tsx"
"use client";

import { ChatLayout, type UIMessage } from "@btst/stack/plugins/ai-chat/client";
import { useLocalStorage } from "@/hooks/useLocalStorage"; // Your hook

const baseURL = typeof window !== "undefined" ? window.location.origin : "http://localhost:3000";

export default function PublicChat() {
  const [messages, setMessages] = useLocalStorage<UIMessage[]>(
    "public-chat-messages",
    []
  );

  return (
    <ChatLayout
      apiBaseURL={baseURL}
      apiBasePath="/api/data"
      layout="widget"
      initialMessages={messages}
      onMessagesChange={setMessages}
    />
  );
}
```

<Callout type="warn">
  **SSR Hydration:** When using localStorage with SSR frameworks, ensure you handle hydration correctly to avoid mismatches. The `initialMessages` prop is applied on mount, so it works well with client-side storage hooks that return an empty array during SSR.
</Callout>

**Key points:**

* `initialMessages` - Pre-populates the chat with saved messages on mount
* `onMessagesChange` - Called whenever messages change (only fires in public mode)
* `UIMessage` type is re-exported from `@btst/stack/plugins/ai-chat/client` for convenience

This pattern enables:

* **localStorage** - Simple browser-based persistence
* **sessionStorage** - Per-tab conversation history
* **IndexedDB** - Larger storage for long conversations
* **External state management** - Redux, Zustand, etc.

## Localization

Customize UI strings by providing a `localization` override:

```tsx
overrides={{
  "ai-chat": {
    // ... other overrides
    localization: {
      CHAT_PLACEHOLDER: "Ask me anything...",
      CHAT_EMPTY_STATE: "How can I help you today?",
      SIDEBAR_NEW_CHAT: "Start new conversation",
      CONVERSATION_DELETE_CONFIRM_TITLE: "Delete this chat?",
      // See AiChatLocalization type for all available strings
    }
  }
}}
```

#### AiChatLocalization

<AutoTypeTable path="../packages/stack/src/plugins/ai-chat/client/localization/index.ts" name="AiChatLocalization" />

## Server-side Data Access

The AI Chat plugin exposes standalone getter functions for server-side use cases, giving you direct access to conversation history without going through HTTP.

### Two patterns

**Pattern 1 — via `stack().api`**

```ts title="app/lib/stack.ts"
import { myStack } from "./stack";

// List all conversations (optionally scoped to a user)
const all        = await myStack.api["ai-chat"].getAllConversations();
const userConvs  = await myStack.api["ai-chat"].getAllConversations("user-123");

// Get a conversation with its full message history
const conv       = await myStack.api["ai-chat"].getConversationById("conv-456");
if (conv) {
  console.log(conv.messages); // Message[]
}
```

**Pattern 2 — direct import**

```ts
import {
  getAllConversations,
  getConversationById,
} from "@btst/stack/plugins/ai-chat/api";

const conv = await getConversationById(myAdapter, conversationId);
```

### Available getters

| Function                                | Description                                              |
| --------------------------------------- | -------------------------------------------------------- |
| `getAllConversations(adapter, userId?)` | Returns all conversations, optionally filtered by userId |
| `getConversationById(adapter, id)`      | Returns a conversation with messages, or `null`          |

## Route-Aware AI Context

The AI chat plugin supports **route-aware context** — pages register contextual data and client-side tool handlers that the chat widget reads automatically. This enables:

* The AI to summarize content from the current page
* The AI to fill in forms or update editors on the user's behalf
* Dynamic suggestion chips that change based on which page is open

### Setup

**Step 1 — Add `PageAIContextProvider` to your root layout** (above all `StackProvider` instances):

```tsx title="app/layout.tsx"
import { PageAIContextProvider } from "@btst/stack/plugins/ai-chat/client/context"

export default function RootLayout({ children }) {
  return (
    <html>
      <body>
        <PageAIContextProvider>
          {/* Everything else, including StackProvider and your chat modal */}
          {children}
        </PageAIContextProvider>
      </body>
    </html>
  )
}
```

<Callout type="info">
  Place `PageAIContextProvider` above any `StackProvider` so it spans both the main app tree and any chat modals rendered as Next.js parallel/intercept routes. Both trees need to be descendants of the same context instance for context to flow between them.
</Callout>

**Step 2 — Enable page tools in your backend config**:

```ts title="lib/stack.ts"
aiChatBackendPlugin({
  model: openai("gpt-4o"),
  enablePageTools: true, // activates built-in fillBlogForm, updatePageLayers tools
})
```

### Registering Page Context

Call `useRegisterPageAIContext` in any page component to publish context to the chat. The registration is cleaned up automatically when the component unmounts.

```tsx
import { useRegisterPageAIContext } from "@btst/stack/plugins/ai-chat/client/context"

// Blog post page — provides content for summarization
function BlogPostPage({ post }) {
  useRegisterPageAIContext(post ? {
    routeName: "blog-post",
    pageDescription: `Blog post: "${post.title}"\n\n${post.content.slice(0, 16000)}`,
    suggestions: ["Summarize this post", "What are the key takeaways?"],
  } : null)

  // ...
}
```

Pass `null` to conditionally disable context (e.g. while data is loading).

### Client-Side Tools

Pages can expose **client-side tool handlers** — functions the AI can call to mutate page state. Built-in tools (`fillBlogForm`, `updatePageLayers`) are already wired up in the blog and UI builder plugins. For custom pages:

**1. Register a tool handler on the page:**

```tsx
import { useRegisterPageAIContext } from "@btst/stack/plugins/ai-chat/client/context"

function ProductPage({ product, cart }) {
  useRegisterPageAIContext({
    routeName: "product-detail",
    pageDescription: `Product: ${product.name}. Price: $${product.price}.`,
    suggestions: ["Tell me about this product", "Add to cart"],
    clientTools: {
      addToCart: async ({ quantity }) => {
        cart.add(product.id, quantity)
        return { success: true, message: `Added ${quantity} to cart` }
      }
    }
  })
}
```

**2. Register the tool schema server-side** (so the LLM knows the parameter shapes):

```ts title="lib/stack.ts"
import { tool } from "ai"
import { z } from "zod"

aiChatBackendPlugin({
  model: openai("gpt-4o"),
  enablePageTools: true,
  clientToolSchemas: {
    addToCart: tool({
      description: "Add the current product to the shopping cart",
      inputSchema: z.object({ quantity: z.number().int().min(1) }),
      // No execute — this is handled client-side
    }),
  }
})
```

When the AI calls `addToCart`, the return value from the client handler is sent back to the model as the tool result, allowing the conversation to continue.

### Built-In Page Tools

| Tool               | Registered by        | Description                                                |
| ------------------ | -------------------- | ---------------------------------------------------------- |
| `fillBlogForm`     | Blog new/edit pages  | Fills title, content, excerpt, and tags in the post editor |
| `updatePageLayers` | UI builder edit page | Replaces the component layer tree in the page builder      |

### API Reference

#### `PageAIContextProvider`

```tsx
import { PageAIContextProvider } from "@btst/stack/plugins/ai-chat/client/context"

<PageAIContextProvider>
  {children}
</PageAIContextProvider>
```

#### `useRegisterPageAIContext(config)`

```ts
import { useRegisterPageAIContext } from "@btst/stack/plugins/ai-chat/client/context"

useRegisterPageAIContext({
  routeName: string,           // shown as badge in chat header
  pageDescription: string,     // injected into system prompt (max 8,000 chars)
  suggestions?: string[],      // quick-action chips in chat empty state
  clientTools?: {              // handlers the AI can invoke
    [toolName: string]: (args: any) => Promise<{ success: boolean; message?: string }>
  }
})
```

#### `AiChatBackendConfig` — new options

| Option                         | Type                                          | Default | Description                                              |
| ------------------------------ | --------------------------------------------- | ------- | -------------------------------------------------------- |
| `enablePageTools`              | `boolean`                                     | `false` | Activate page tool support                               |
| `clientToolSchemas`            | `Record<string, Tool>`                        | —       | Custom tool schemas for non-BTST pages                   |
| `hooks.onBeforeToolsActivated` | `(toolNames, routeName, context) => string[]` | —       | Filter active tools per request; throw to abort with 403 |

### Tool Authorization Hook

`onBeforeToolsActivated` runs server-side after the structural `routeName` allowlist check. Use it to add user-level authorization — for example, restricting which tools are available based on the authenticated user's role or subscription tier.

```ts title="lib/stack.ts"
import type { AiChatBackendHooks } from "@btst/stack/plugins/ai-chat/api"

aiChatBackendPlugin({
  enablePageTools: true,
  hooks: {
    onBeforeToolsActivated: async (toolNames, routeName, context) => {
      const role = await getUserRole(context.headers);
      // Viewers cannot use any interactive tools
      if (role === "viewer") return [];
      // Non-editors cannot fill the blog form
      if (role !== "editor") return toolNames.filter(t => t !== "fillBlogForm");
      return toolNames;
    },
  },
})
```

| Parameter   | Type                  | Description                                     |
| ----------- | --------------------- | ----------------------------------------------- |
| `toolNames` | `string[]`            | Tools that passed the routeName allowlist check |
| `routeName` | `string \| undefined` | Claimed route name from the request             |
| `context`   | `ChatApiContext`      | Full request context (headers, body, etc.)      |

Return a subset of `toolNames` to allow, or `[]` to suppress all page tools. Throw an `Error` to abort the entire chat request — the endpoint catches it and returns a **403** response.

<Callout type="info">
  This hook runs **after** the structural `routeName` allowlist check (which validates that each built-in tool is only requested from its intended page). `onBeforeToolsActivated` is the right place to add user-specific logic — the two layers are complementary.
</Callout>

## Shadcn Registry

The AI Chat plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/ai-chat/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ai-chat.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/ai-chat/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { aiChatClientPlugin } from "@btst/stack/plugins/ai-chat/client"
// Import your ejected (and customized) page components
import { ChatPageComponent } from "@/components/btst/ai-chat/client/components/pages/chat-page"
import { ChatConversationPageComponent } from "@/components/btst/ai-chat/client/components/pages/chat-conversation-page"

aiChatClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    chat: ChatPageComponent,                          // replaces the chat home page
    chatConversation: ChatConversationPageComponent,  // replaces the conversation page
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.


# Better Auth UI Plugin (Beta) (/plugins/better-auth-ui)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import { Github, BookOpen, GitFork } from "lucide-react";
import Image from "next/image";

import betterAuthUiDemo from "../../../assets/better-auth-ui-demo.webp";

<div className="my-4">
  <a href={betterAuthUiDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={betterAuthUiDemo} alt="Better Auth UI Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

The Better Auth UI plugin provides beautiful, plug-and-play authentication UI components built with [shadcn/ui](https://ui.shadcn.com/) for [better-auth](https://www.better-auth.com/). This is a fork of the popular [better-auth-ui](https://github.com/better-auth-ui/better-auth-ui) library, adapted for seamless integration with BTST.

<div className="flex gap-4 my-4">
  <a href="https://github.com/better-stack-ai/better-auth-ui" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors">
    <Github className="w-5 h-5" />

    @btst/better-auth-ui
  </a>

  <a href="https://github.com/better-auth-ui/better-auth-ui" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors">
    <GitFork className="w-5 h-5" />

    Original Repo
  </a>

  <a href="https://better-auth-ui.com/" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors">
    <BookOpen className="w-5 h-5" />

    Documentation
  </a>
</div>

## Features

* **Sign In / Sign Up** – Complete authentication flows with email, password, social login, and magic links
* **Account Management** – User profile settings, security settings, API keys, and team/organization memberships
* **Two-Factor Authentication** – TOTP and OTP support for enhanced security
* **Social Login** – GitHub, Google, Discord, and more OAuth providers
* **Passkeys** – WebAuthn/Passkey authentication support
* **Organizations** – Team and organization management with invitations and roles
* **Email OTP / Magic Link** – Passwordless authentication options
* **Email Verification** – Enforce email verification before access
* **Generic OAuth** – Bring your own OAuth provider
* **Fully Customizable** – Built with TailwindCSS and shadcn/ui; per-page `className`, `classNames`, and `localization` overrides

## Installation

<Callout type="info">
  Before starting, ensure you have:

  * A Next.js project with `@btst/stack` already set up (see [Installation](/installation))
  * `better-auth` configured (server-side auth)
  * A `better-auth` client (`lib/auth-client.ts`) set up
  * A database adapter (e.g., Drizzle with `@btst/adapter-drizzle`)
</Callout>

### 1. Install the Package

```bash
pnpm add @btst/better-auth-ui
```

Or with npm/yarn:

```bash
npm install @btst/better-auth-ui
# or
yarn add @btst/better-auth-ui
```

### 2. Configure the Stack Client

Import and register the auth plugins in your `stack-client.tsx` file:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import {
  authClientPlugin,
  accountClientPlugin,
  organizationClientPlugin,
} from "@btst/better-auth-ui/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () =>
  typeof window !== "undefined"
    ? window.location.origin
    : process.env.BASE_URL || "http://localhost:3000"

export function getStackClient(queryClient: QueryClient) {
  const baseURL = getBaseURL()

  return createStackClient({
    plugins: {
      // Auth plugin — sign-in, sign-up, forgot-password, magic-link, etc.
      auth: authClientPlugin({
        siteBaseURL: baseURL,
        siteBasePath: "/p",   // prefix used in your catch-all route
      }),

      // Account plugin — settings, security, API keys, teams, organizations
      account: accountClientPlugin({
        siteBaseURL: baseURL,
        siteBasePath: "/p",
      }),

      // Organization plugin — org settings, members, teams
      organization: organizationClientPlugin({
        siteBaseURL: baseURL,
        siteBasePath: "/p",
      }),

      // ... other BTST plugins (blog, cms, etc.)
    },
  })
}
```

### 3. Configure the StackProvider (Client-Side Layout)

Configure the plugin overrides in your catch-all layout file. The `auth` overrides are shared across all three plugins using `...authConfig`.

<Tabs groupId="frameworks" items={["next-js"]} persist>
  <Tab value="next-js">
    ```tsx title="app/p/[[...all]]/layout.tsx"
    "use client"

    import { StackProvider } from "@btst/stack/context"
    import type {
      AuthPluginOverrides,
      AccountPluginOverrides,
      OrganizationPluginOverrides,
    } from "@btst/better-auth-ui/client"
    import { authClient } from "@/lib/auth-client"
    import Link from "next/link"
    import { useRouter } from "next/navigation"
    import type { ReactNode } from "react"

    type PluginOverrides = {
      auth: AuthPluginOverrides
      account: AccountPluginOverrides
      organization: OrganizationPluginOverrides
    }

    export default function PagesLayout({ children }: { children: ReactNode }) {
      const router = useRouter()

      // Shared auth configuration — spread into each plugin override
      const authConfig = {
        authClient,
        navigate: router.push,
        replace: router.replace,
        onSessionChange: () => router.refresh(),
        Link,
      }

      return (
        <StackProvider<PluginOverrides>
          basePath="/p"
          overrides={{
            auth: {
              ...authConfig,
              basePath: "/p/auth",              // auth routes prefix
              redirectTo: "/p/account/settings", // redirect after login
              // social: { providers: ["github", "google"] },
              // magicLink: true,
              // emailOTP: true,
              // passkey: true,
              // twoFactor: ["otp", "totp"],
              // emailVerification: true,
              // credentials: { forgotPassword: true },
            },
            account: {
              ...authConfig,
              basePath: "/p/account",           // account routes prefix
              account: {
                fields: ["image", "name"],       // editable profile fields
              },
              // deleteUser: true,
              // teams: true,
              // apiKey: true,
              // avatar: {
              //   upload: async (file) => myUploader(file),
              //   size: 128,
              //   extension: "png",
              // },
            },
            organization: {
              ...authConfig,
              basePath: "/p/org",
              organization: {
                basePath: "/p/org",
                // logo: true,
                // customRoles: [{ role: "editor", label: "Editor" }],
                // apiKey: true,
                // pathMode: "slug",
              },
              // teams: true,
            },
          }}
        >
          {children}
        </StackProvider>
      )
    }
    ```
  </Tab>
</Tabs>

### 4. Import Required CSS

Add the better-auth-ui styles to your global stylesheet:

```css title="app/globals.css"
@import "@btst/better-auth-ui/css";
```

## Available Routes

Once configured, the following routes become available under your configured `basePath`.

### Auth Routes (`/p/auth/...`)

| Route                        | Description                        |
| ---------------------------- | ---------------------------------- |
| `/p/auth/sign-in`            | Sign in page                       |
| `/p/auth/sign-up`            | Sign up page                       |
| `/p/auth/forgot-password`    | Password reset request             |
| `/p/auth/reset-password`     | Password reset form                |
| `/p/auth/magic-link`         | Magic link landing page            |
| `/p/auth/email-otp`          | Email OTP landing page             |
| `/p/auth/two-factor`         | Two-factor verification            |
| `/p/auth/recover-account`    | Backup code recovery               |
| `/p/auth/callback`           | OAuth callback handler             |
| `/p/auth/sign-out`           | Sign out page                      |
| `/p/auth/accept-invitation`  | Organization invitation acceptance |
| `/p/auth/email-verification` | Email verification page            |

### Account Routes (`/p/account/...`)

| Route                      | Description                             |
| -------------------------- | --------------------------------------- |
| `/p/account/settings`      | Profile & account settings              |
| `/p/account/security`      | Password, 2FA, passkeys, sessions       |
| `/p/account/api-keys`      | API key management (`apiKey: true`)     |
| `/p/account/organizations` | User's organization memberships         |
| `/p/account/teams`         | User's team memberships (`teams: true`) |

### Organization Routes (`/p/org/...`)

| Route             | Description                            |
| ----------------- | -------------------------------------- |
| `/p/org/settings` | Organization name, logo, danger zone   |
| `/p/org/members`  | Member management, invitations, roles  |
| `/p/org/api-keys` | Organization API keys (`apiKey: true`) |
| `/p/org/teams`    | Team management (`teams: true`)        |

<Callout type="info">
  Routes are prefixed with your configured `basePath`. The examples above use `/p` as the base path.
  The exact sub-paths come from the view paths constants in the library and match the route keys above.
</Callout>

## Configuration Options

### Auth Plugin (`AuthPluginOverrides`)

| Option              | Type                                  | Default         | Description                                |
| ------------------- | ------------------------------------- | --------------- | ------------------------------------------ |
| `authClient`        | `AnyAuthClient`                       | Required        | Better Auth client                         |
| `basePath`          | `string`                              | `"/auth"`       | Base path for auth routes                  |
| `baseURL`           | `string`                              | —               | Front-end base URL for OAuth callbacks     |
| `redirectTo`        | `string`                              | `"/"`           | Redirect URL after login                   |
| `credentials`       | `boolean \| CredentialsOptions`       | `true`          | Email/password login                       |
| `signUp`            | `boolean \| SignUpOptions`            | `true`          | Sign-up flow                               |
| `social`            | `SocialOptions`                       | —               | Social provider config                     |
| `genericOAuth`      | `GenericOAuthOptions`                 | —               | Custom OAuth providers                     |
| `magicLink`         | `boolean`                             | `false`         | Passwordless magic link                    |
| `emailOTP`          | `boolean`                             | `false`         | Passwordless email OTP                     |
| `passkey`           | `boolean`                             | `false`         | WebAuthn passkeys                          |
| `oneTap`            | `boolean`                             | `false`         | Google One Tap                             |
| `twoFactor`         | `("otp" \| "totp")[]`                 | —               | Two-factor authentication                  |
| `multiSession`      | `boolean`                             | `false`         | Multiple session support                   |
| `emailVerification` | `boolean`                             | —               | Require email verification                 |
| `changeEmail`       | `boolean`                             | `true`          | Allow email changes                        |
| `nameRequired`      | `boolean`                             | `true`          | Name field required on sign-up             |
| `apiKey`            | `boolean \| { prefix?, metadata? }`   | —               | API key plugin support                     |
| `gravatar`          | `boolean \| GravatarOptions`          | —               | Gravatar avatars                           |
| `avatar`            | `boolean \| AvatarOptions`            | —               | Avatar upload                              |
| `additionalFields`  | `AdditionalFields`                    | —               | Extra user fields                          |
| `captcha`           | `CaptchaOptions`                      | —               | CAPTCHA integration                        |
| `localization`      | `AuthLocalization`                    | —               | Override all UI strings                    |
| `viewPaths`         | `Partial<AuthViewPaths>`              | —               | Custom route sub-paths                     |
| `freshAge`          | `number`                              | `86400`         | Session freshness in seconds               |
| `persistClient`     | `boolean`                             | `false`         | Force session refresh on callback          |
| `optimistic`        | `boolean`                             | `false`         | Optimistic user updates                    |
| `hooks`             | `Partial<AuthHooks>`                  | —               | Custom data fetching hooks                 |
| `mutators`          | `Partial<AuthMutators>`               | —               | Custom mutation handlers                   |
| `Link`              | `Link`                                | `<a>`           | Custom link component                      |
| `navigate`          | `(href: string) => void`              | `location.href` | Navigation function                        |
| `replace`           | `(href: string) => void`              | `navigate`      | Replace navigation                         |
| `toast`             | `RenderToast`                         | Sonner          | Custom toast renderer                      |
| `onSessionChange`   | `() => void`                          | —               | Session change callback                    |
| `onRouteError`      | `(name, error, ctx) => void`          | —               | Route error callback                       |
| `pageProps`         | See [Per-Page Props](#per-page-props) | —               | Per-page className/classNames/localization |

### Account Plugin (`AccountPluginOverrides`)

Extends `Partial<AuthPluginOverrides>` with:

| Option       | Type                                  | Default                         | Description                                |
| ------------ | ------------------------------------- | ------------------------------- | ------------------------------------------ |
| `account`    | `boolean \| Partial<AccountOptions>`  | `{ fields: ["image", "name"] }` | Account view config                        |
| `deleteUser` | `boolean \| DeleteUserOptions`        | —                               | Account deletion                           |
| `teams`      | `boolean \| TeamOptions`              | —                               | Teams support                              |
| `pageProps`  | See [Per-Page Props](#per-page-props) | —                               | Per-page className/classNames/localization |

### Organization Plugin (`OrganizationPluginOverrides`)

Extends `Partial<AuthPluginOverrides>` with:

| Option         | Type                                  | Default | Description                                |
| -------------- | ------------------------------------- | ------- | ------------------------------------------ |
| `organization` | `boolean \| OrganizationOptions`      | —       | Organization config                        |
| `teams`        | `boolean \| TeamOptions`              | —       | Teams within organizations                 |
| `pageProps`    | See [Per-Page Props](#per-page-props) | —       | Per-page className/classNames/localization |

**`OrganizationOptions`:**

| Option         | Type                                          | Default           | Description                                        |
| -------------- | --------------------------------------------- | ----------------- | -------------------------------------------------- |
| `basePath`     | `string`                                      | `"/organization"` | Base path for org routes                           |
| `logo`         | `boolean \| Partial<OrganizationLogoOptions>` | —                 | Logo upload                                        |
| `customRoles`  | `{ role: string; label: string }[]`           | `[]`              | Extra roles beyond owner/admin/member              |
| `apiKey`       | `boolean`                                     | `false`           | API keys for organizations                         |
| `pathMode`     | `"default" \| "slug"`                         | `"default"`       | Route mode                                         |
| `slug`         | `string`                                      | —                 | Active organization slug (when `pathMode: "slug"`) |
| `personalPath` | `string`                                      | —                 | Redirect path when Personal Account is selected    |
| `viewPaths`    | `Partial<OrganizationViewPaths>`              | —                 | Custom route sub-paths                             |

## Per-Page Props

You can customize each page individually with `className`, `classNames`, `localization`, and other view-specific props — without replacing the entire component.

These are set via `pageProps` in the relevant plugin override:

```tsx
overrides={{
  auth: {
    ...authConfig,
    basePath: "/p/auth",
    pageProps: {
      signIn: {
        className: "my-wrapper",
        classNames: {
          title: "text-3xl font-bold",
          description: "text-muted-foreground",
          footer: "border-t pt-4",
        },
        localization: { SIGN_IN: "Log in" },  // only override what you need
        socialLayout: "grid",
        redirectTo: "/dashboard",
      },
      signUp: {
        cardHeader: <MyCustomHeader />,     // replace the card header entirely
        callbackURL: "/welcome",
      },
      callback: {
        redirectTo: "/onboarding",          // override the post-OAuth redirect
      },
      signOut: {
        redirectTo: "/p/auth/sign-in",
      },
    },
  },
  account: {
    ...authConfig,
    basePath: "/p/account",
    account: { fields: ["image", "name"] },
    pageProps: {
      accountSettings: {
        className: "max-w-2xl mx-auto",
        hideNav: true,
      },
      accountSecurity: {
        localization: { SECURITY: "Privacy & Security" },
      },
    },
  },
  organization: {
    ...authConfig,
    basePath: "/p/org",
    organization: { basePath: "/p/org" },
    pageProps: {
      organizationSettings: {
        className: "p-8",
        classNames: { sidebar: { base: "w-64" } },
      },
    },
  },
}}
```

### `AuthPageProps` (auth pages)

| Prop            | Type                                             | Description                             |
| --------------- | ------------------------------------------------ | --------------------------------------- |
| `className`     | `string`                                         | Wrapper class                           |
| `classNames`    | `AuthViewClassNames`                             | Fine-grained class overrides            |
| `localization`  | `Partial<AuthLocalization>`                      | Override specific strings               |
| `socialLayout`  | `"auto" \| "horizontal" \| "grid" \| "vertical"` | Social provider button layout           |
| `callbackURL`   | `string`                                         | URL sent to OAuth providers as callback |
| `redirectTo`    | `string`                                         | Override the post-auth redirect         |
| `cardHeader`    | `ReactNode`                                      | Replace the card header                 |
| `cardFooter`    | `ReactNode`                                      | Replace the card footer                 |
| `otpSeparators` | `0 \| 1 \| 2`                                    | OTP input separator count               |

> `callback` and `signOut` only accept `{ redirectTo }`. `acceptInvitation` only accepts `{ className }`.

### `AccountPageProps` (account pages)

| Prop           | Type                                          | Description                        |
| -------------- | --------------------------------------------- | ---------------------------------- |
| `className`    | `string`                                      | Wrapper class                      |
| `classNames`   | `{ base?, cards?, drawer?, sidebar?, card? }` | Fine-grained class overrides       |
| `localization` | `Partial<AuthLocalization>`                   | Override specific strings          |
| `hideNav`      | `boolean`                                     | Hide the sidebar/drawer navigation |
| `showTeams`    | `boolean`                                     | Show teams tab on the page         |

### `OrganizationPageProps` (organization pages)

| Prop           | Type                                          | Description                           |
| -------------- | --------------------------------------------- | ------------------------------------- |
| `className`    | `string`                                      | Wrapper class                         |
| `classNames`   | `{ base?, cards?, drawer?, sidebar?, card? }` | Fine-grained class overrides          |
| `localization` | `Partial<AuthLocalization>`                   | Override specific strings             |
| `hideNav`      | `boolean`                                     | Hide the sidebar/drawer navigation    |
| `slug`         | `string`                                      | Override the active organization slug |

## Common Recipes

### Social Login

```tsx
auth: {
  ...authConfig,
  social: {
    providers: ["github", "google", "discord"],
  },
}
```

### Passwordless (Magic Link + Email OTP)

```tsx
auth: {
  ...authConfig,
  magicLink: true,
  emailOTP: true,
}
```

### Two-Factor Authentication

```tsx
auth: {
  ...authConfig,
  twoFactor: ["otp", "totp"],
}
```

### Passkeys

```tsx
auth: {
  ...authConfig,
  passkey: true,
}
```

### Avatar Upload

```tsx
account: {
  ...authConfig,
  avatar: {
    upload: async (file) => {
      const result = await myStorage.upload(file)
      return result.url
    },
    size: 128,
    extension: "png",
  },
}
```

### Account Deletion

```tsx
account: {
  ...authConfig,
  deleteUser: true,
  // or with a confirmation requirement:
  // deleteUser: { requirePassword: true },
}
```

### Organizations with Logo Upload

```tsx
organization: {
  ...authConfig,
  basePath: "/p/org",
  organization: {
    basePath: "/p/org",
    logo: {
      upload: async (file) => {
        const result = await myStorage.upload(file)
        return result.url
      },
      size: 256,
      extension: "png",
    },
    customRoles: [
      { role: "editor", label: "Editor" },
      { role: "viewer", label: "Viewer" },
    ],
    apiKey: true,
  },
  teams: true,
}
```

### API Keys

Enable API key management in account settings:

```tsx
auth: {
  ...authConfig,
  apiKey: {
    prefix: "sk",           // key prefix shown in the UI
    metadata: {},           // default metadata attached to new keys
  },
}
```

## Learn More

For comprehensive documentation on all configuration options, customization, and advanced features, visit:

* **[Better Auth UI Documentation](https://better-auth-ui.com/)** – Official documentation with demos and guides
* **[GitHub Repository (Fork)](https://github.com/better-stack-ai/better-auth-ui)** – Source code for the BTST fork
* **[Original Repository](https://github.com/better-auth-ui/better-auth-ui)** – Upstream repository
* **[better-auth Documentation](https://www.better-auth.com/)** – Documentation for the underlying auth library


# Blog Plugin (/plugins/blog)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import blogDemo from "../../../assets/blog-demo.png";
import blogDemo1 from "../../../assets/blog-demo-1.png";
import blogDemo2 from "../../../assets/blog-demo-2.png";
import blogDemo3 from "../../../assets/blog-demo-3.png";

<div className="grid grid-cols-1 lg:grid-cols-2 gap-2 my-2">
  <a href={blogDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={blogDemo} alt="Blog Plugin Demo - Home" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={blogDemo1.src} target="_blank" rel="noopener noreferrer">
    <Image src={blogDemo1} alt="Blog Plugin Demo - Post" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={blogDemo2.src} target="_blank" rel="noopener noreferrer">
    <Image src={blogDemo2} alt="Blog Plugin Demo - Editor" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={blogDemo3.src} target="_blank" rel="noopener noreferrer">
    <Image src={blogDemo3} alt="Blog Plugin Demo - Drafts" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

[View interactive demo →](/demos/blog)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

Follow these steps to add the Blog plugin to your BTST setup.

### 1. Add Plugin to Backend API

Import and register the blog backend plugin in your `stack.ts` file:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { blogBackendPlugin } from "@btst/stack/plugins/blog/api"
// ... your adapter imports

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    blog: blogBackendPlugin()
  },
  adapter: (db) => createPrismaAdapter(prisma, db, { 
    provider: "postgresql" 
  })
})

export { handler, dbSchema }
```

The `blogBackendPlugin()` accepts optional hooks for customizing behavior (authorization, logging, etc.).

### 2. Add Plugin to Client

Register the blog client plugin in your `stack-client.tsx` file:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () => 
   (process.env.BASE_URL || "http://localhost:3000")

export const getStackClient = (queryClient: QueryClient) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      blog: blogClientPlugin({
        // Required configuration
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient: queryClient,
        // Optional: SEO configuration
        seo: {
          siteName: "My Blog",
          author: "Your Name",
          twitterHandle: "@yourhandle",
          locale: "en_US",
          defaultImage: `${baseURL}/og-image.png`,
        },
      })
    }
  })
}
```

**Required configuration:**

* `apiBaseURL`: Base URL for API calls during SSR data prefetching (use environment variables for flexibility)
* `apiBasePath`: Path where your API is mounted (e.g., `/api/data`)
* `siteBaseURL`: Base URL of your site
* `siteBasePath`: Path where your pages are mounted (e.g., `/pages`)
* `queryClient`: React Query client instance

<Callout type="info">
  **Why configure API paths here?** This configuration is used by **server-side loaders** that prefetch data before your pages render. These loaders run outside of React Context, so they need direct configuration. You'll also provide `apiBaseURL` and `apiBasePath` again in the Provider overrides (Section 4) for **client-side components** that run during actual rendering.
</Callout>

### 3. Import Plugin CSS

Add the blog plugin CSS to your global stylesheet:

```css title="app/globals.css"
@import "@btst/stack/plugins/blog/css";
```

This includes all necessary styles for the blog components, markdown rendering, and editor.

### 4. Add Context Overrides

Configure framework-specific overrides in your `StackProvider`:

<Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
  <Tab value="next-js">
    ```tsx title="app/pages/[[...all]]/layout.tsx"
    import { StackProvider } from "@btst/stack/context"
    import type { BlogPluginOverrides } from "@btst/stack/plugins/blog/client"
    import Link from "next/link"
    import Image from "next/image"
    import { useRouter } from "next/navigation"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (process.env.NEXT_PUBLIC_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      blog: BlogPluginOverrides
    }

    export default function Layout({ children }) {
      const router = useRouter()
      const baseURL = getBaseURL()
      
      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            blog: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (path) => router.push(path),
              refresh: () => router.refresh(),
              uploadImage: async (file) => {
                // Implement your image upload logic
                // Return the URL of the uploaded image
                return "https://example.com/uploads/image.jpg"
              },
              Link: (props) => <Link {...props} />,
              Image: (props) => <Image {...props} />,
            }
          }}
        >
          {children}
        </StackProvider>
      )
    }
    ```
  </Tab>

  <Tab value="react-router">
    ```tsx title="app/routes/pages/_layout.tsx"
    import { Outlet, Link, useNavigate } from "react-router"
    import { StackProvider } from "@btst/stack/context"
    import type { BlogPluginOverrides } from "@btst/stack/plugins/blog/client"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:5173")

    type PluginOverrides = {
      blog: BlogPluginOverrides
    }

    export default function Layout() {
      const navigate = useNavigate()
      const baseURL = getBaseURL()
      
      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            blog: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (href) => navigate(href),
              uploadImage: async (file) => {
                // Implement your image upload logic
                return "https://example.com/uploads/image.jpg"
              },
              Link: ({ href, children, className, ...props }) => (
                <Link to={href || ""} className={className} {...props}>
                  {children}
                </Link>
              ),
            }
          }}
        >
          <Outlet />
        </StackProvider>
      )
    }
    ```
  </Tab>

  <Tab value="tanstack">
    ```tsx title="src/routes/pages/route.tsx"
    import { StackProvider } from "@btst/stack/context"
    import type { BlogPluginOverrides } from "@btst/stack/plugins/blog/client"
    import { Link, useRouter, Outlet } from "@tanstack/react-router"

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      blog: BlogPluginOverrides
    }

    function Layout() {
      const router = useRouter()
      const baseURL = getBaseURL()

      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            blog: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (href) => router.navigate({ href }),
              uploadImage: async (file) => {
                // Implement your image upload logic
                return "https://example.com/uploads/image.jpg"
              },
              Link: ({ href, children, className, ...props }) => (
                <Link to={href} className={className} {...props}>
                  {children}
                </Link>
              ),
            }
          }}
        >
          <Outlet />
        </StackProvider>
      )
    }
    ```
  </Tab>
</Tabs>

**Required overrides:**

* `apiBaseURL`: Base URL for API calls (used by client-side components during rendering)
* `apiBasePath`: Path where your API is mounted
* `navigate`: Function for programmatic navigation
* `uploadImage`: Function to upload images and return their URL

**Optional overrides:**

* `Link`: Custom Link component (defaults to `<a>` tag)
* `Image`: Custom Image component (useful for Next.js Image optimization)
* `refresh`: Function to refresh server-side cache (useful for Next.js)
* `localization`: Custom localization strings
* `showAttribution`: Whether to show BTST attribution

<Callout type="warn">
  **Why provide API paths again?** You already configured these in Section 2, but that configuration is only available to **server-side loaders**. The overrides here provide the same values to **client-side components** (like hooks, forms, and UI) via React Context. These two contexts serve different phases: loaders prefetch data server-side before rendering, while components use data during actual rendering (both SSR and CSR).
</Callout>

### 5. Generate Database Schema

After adding the plugin, generate your database schema using the CLI:

```bash
npx @btst/cli generate --orm prisma --config lib/stack.ts  --output prisma/schema.prisma
```

This will create the necessary database tables for posts and tags. Run migrations as needed for your ORM.

For more details on the CLI and all available options, see the [CLI documentation](/cli).

## Congratulations, You're Done! 🎉

Your blog plugin is now fully configured and ready to use! Here's a quick reference of what's available:

### API Endpoints

The blog plugin provides the following API endpoints (mounted at your configured `apiBasePath`):

* **GET** `/posts` - List posts with optional filtering (published status, tag, search query)
* **POST** `/posts` - Create a new post
* **PUT** `/posts/:id` - Update an existing post
* **DELETE** `/posts/:id` - Delete a post
* **GET** `/posts/next-previous` - Get previous and next posts relative to a date
* **GET** `/tags` - List all tags

### Page Routes

The blog plugin automatically creates the following pages (mounted at your configured `siteBasePath`):

* `/blog` - Blog homepage with published posts
* `/blog/drafts` - Draft posts page
* `/blog/new` - Create new post page
* `/blog/:slug` - Individual post page
* `/blog/:slug/edit` - Edit post page
* `/blog/tag/:tagSlug` - Posts filtered by tag

### Page Component Overrides

You can replace any built-in page with your own React component using the optional `pageComponents` field in `blogClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
blogClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the published posts list page
    posts: MyCustomPostsPage,
    // Replace the single post page — receives the slug as a prop
    post: ({ slug }) => <MyCustomPostPage slug={slug} />,
    // Replace the edit post page — receives the slug as a prop
    editPost: ({ slug }) => <MyCustomEditPage slug={slug} />,
    // Replace the tag page — receives tagSlug as a prop
    tag: ({ tagSlug }) => <MyCustomTagPage tagSlug={tagSlug} />,
    // Replace the drafts list page
    drafts: MyCustomDraftsPage,
    // Replace the new post page
    newPost: MyCustomNewPostPage,
  },
})
```

### Adding Authorization

To add authorization rules and customize behavior, you can use the lifecycle hooks defined in the API Reference section below. These hooks allow you to control access to API endpoints, add logging, and customize the plugin's behavior to fit your application's needs.

## API Reference

### Backend (`@btst/stack/plugins/blog/api`)

#### blogBackendPlugin

<AutoTypeTable path="../packages/stack/src/plugins/blog/api/plugin.ts" name="blogBackendPlugin" />

#### BlogBackendHooks

Customize backend behavior with optional lifecycle hooks. All hooks are optional and allow you to add authorization, logging, and custom behavior:

<AutoTypeTable path="../packages/stack/src/plugins/blog/api/plugin.ts" name="BlogBackendHooks" />

**Example usage:**

```ts title="lib/stack.ts"
import { blogBackendPlugin, type BlogBackendHooks } from "@btst/stack/plugins/blog/api"

const blogHooks: BlogBackendHooks = {
  // Authorization hooks — throw to deny access
  async onBeforeListPosts(filter, context) {
    if (filter.published === false) {
      if (!await isBlogAdmin(context.headers as Headers))
        throw new Error("Admin access required to view drafts")
    }
  },
  async onBeforeCreatePost(data, context) {
    if (!await isBlogAdmin(context.headers as Headers))
      throw new Error("Admin access required to create posts")
  },
  async onBeforeUpdatePost(postId, data, context) {
    if (!await isBlogAdmin(context.headers as Headers))
      throw new Error("Admin access required to update posts")
  },
  async onBeforeDeletePost(postId, context) {
    if (!await isBlogAdmin(context.headers as Headers))
      throw new Error("Admin access required to delete posts")
  },
  // ... other hooks
}

const { handler, dbSchema } = stack({
  plugins: {
    blog: blogBackendPlugin(blogHooks)
  },
  // ...
})
```

#### BlogApiContext

<AutoTypeTable path="../packages/stack/src/plugins/blog/api/plugin.ts" name="BlogApiContext" />

### Client (`@btst/stack/plugins/blog/client`)

#### blogClientPlugin

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/plugin.tsx" name="blogClientPlugin" />

#### BlogClientConfig

The client plugin accepts a configuration object with required fields and optional SEO settings:

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/plugin.tsx" name="BlogClientConfig" />

**Example usage:**

```tsx title="lib/stack-client.tsx"
blog: blogClientPlugin({
  // Required configuration
  apiBaseURL: baseURL,
  apiBasePath: "/api/data",
  siteBaseURL: baseURL,
  siteBasePath: "/pages",
  queryClient: queryClient,
  // Optional SEO configuration
  seo: {
    siteName: "My Awesome Blog",
    author: "John Doe",
    twitterHandle: "@johndoe",
    locale: "en_US",
    defaultImage: `${baseURL}/og-image.png`,
  },
})
```

#### BlogClientHooks

Customize client-side behavior with lifecycle hooks. These hooks are called during data fetching (both SSR and CSR):

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/plugin.tsx" name="BlogClientHooks" />

**Example usage:**

```tsx title="lib/stack-client.tsx"
blog: blogClientPlugin({
  // ... rest of the config
  headers: options?.headers,
  hooks: {
    beforeLoadPosts: async (filter, context) => {
      // only allow loading draft posts for admin
      if (!filter.published) {
        if (!await isAdmin(context.headers))
          throw new Error("Admin access required to view drafts")
      }
    },
    afterLoadPost: async (post, slug, context) => {
      // only allow loading draft post for admin
      const isEditRoute = context.path?.includes('/edit');
      if (post?.published === false || isEditRoute) {
        if (!await isAdmin(context.headers))
          throw new Error("Admin access required")
      }
    },
    onLoadError(error, context) {
      //handle error during prefetching
      redirect("/auth/sign-in")
    },
    // ... other hooks
  }
})
```

#### RouteContext

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/plugin.tsx" name="RouteContext" />

#### LoaderContext

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/plugin.tsx" name="LoaderContext" />

#### BlogPluginOverrides

Configure framework-specific overrides and route lifecycle hooks. All lifecycle hooks are optional:

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/overrides.ts" name="BlogPluginOverrides" />

**Example usage:**

```tsx
overrides={{
  blog: {
    // Required overrides
    apiBaseURL: baseURL,
    apiBasePath: "/api/data",
    navigate: (path) => router.push(path),
    uploadImage: async (file) => {
      // Implement your image upload logic
      return "https://example.com/uploads/image.jpg"
    },
    // Optional lifecycle hooks
    onBeforePostsPageRendered: (context) => {
      // Check if user can view posts list. Helpful for SPA; not needed for SSR (check auth in the loader instead).
      // Throw to deny: throw new Error("Unauthorized")
    },
    // ... other hooks
  }
}}
```

## React Data Hooks and Types

You can import the hooks from `"@btst/stack/plugins/blog/client/hooks"` to use in your components.

#### UsePostsOptions

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UsePostsOptions" />

#### UsePostsResult

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UsePostsResult" />

#### UsePostResult

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UsePostResult" />

#### UsePostSearchOptions

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UsePostSearchOptions" />

#### UsePostSearchResult

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UsePostSearchResult" />

#### UseNextPreviousPostsOptions

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UseNextPreviousPostsOptions" />

#### UseNextPreviousPostsResult

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UseNextPreviousPostsResult" />

#### UseRecentPostsOptions

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UseRecentPostsOptions" />

#### UseRecentPostsResult

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="UseRecentPostsResult" />

#### PostCreateInput

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="PostCreateInput" />

#### PostUpdateInput

<AutoTypeTable path="../packages/stack/src/plugins/blog/client/hooks/blog-hooks.tsx" name="PostUpdateInput" />

## Server-side Data Access

The blog plugin exposes standalone getter functions for server-side and SSG use cases. These bypass the HTTP layer entirely and query the database directly.

### Two patterns

**Pattern 1 — via `stack().api` (recommended for runtime server code)**

After calling `stack()`, the returned object includes a fully-typed `api` namespace. Getters are pre-bound to the adapter:

```ts title="app/lib/stack.ts"
import { myStack } from "./stack"; // your stack() instance

// In a Server Component, generateStaticParams, etc.
const result = await myStack.api.blog.getAllPosts({ published: true });
// result.items  — Post[]
// result.total  — total count before pagination
// result.limit  — applied limit
// result.offset — applied offset

const post = await myStack.api.blog.getPostBySlug("hello-world");
const tags = await myStack.api.blog.getAllTags();
```

**Pattern 2 — direct import (SSG, build-time, or custom adapter)**

Import getters directly and pass any `Adapter`:

```ts
import { getAllPosts, getPostBySlug, getAllTags } from "@btst/stack/plugins/blog/api";

// e.g. in Next.js generateStaticParams
export async function generateStaticParams() {
  const { items } = await getAllPosts(myAdapter, { published: true });
  return items.map((p) => ({ slug: p.slug }));
}
```

### Available getters

| Function                        | Returns          | Description                                     |
| ------------------------------- | ---------------- | ----------------------------------------------- |
| `getAllPosts(adapter, params?)` | `PostListResult` | Paginated posts matching optional filter params |
| `getPostBySlug(adapter, slug)`  | `Post \| null`   | Single post by slug, or `null` if not found     |
| `getAllTags(adapter)`           | `Tag[]`          | All tags, sorted alphabetically                 |

### `PostListParams`

<AutoTypeTable path="../packages/stack/src/plugins/blog/api/getters.ts" name="PostListParams" />

### `PostListResult`

<AutoTypeTable path="../packages/stack/src/plugins/blog/api/getters.ts" name="PostListResult" />

## Static Site Generation (SSG)

`route.loader()` makes HTTP requests to `apiBaseURL`, which silently fails during `next build` because no dev server is running. Use `prefetchForRoute()` instead — it reads directly from the database and pre-populates the React Query cache before rendering.

### `prefetchForRoute(routeKey, queryClient, params?)`

| Route key    | Params required       | Data prefetched      |
| ------------ | --------------------- | -------------------- |
| `"posts"`    | —                     | Published posts list |
| `"drafts"`   | —                     | Draft posts list     |
| `"post"`     | `{ slug: string }`    | Single post detail   |
| `"tag"`      | `{ tagSlug: string }` | Tag + tagged posts   |
| `"newPost"`  | —                     | *(nothing)*          |
| `"editPost"` | `{ slug: string }`    | Post to edit         |

### Next.js example

```tsx title="app/pages/blog/page.tsx"
import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
import { getOrCreateQueryClient } from "@/lib/query-client"
import { getStackClient } from "@/lib/stack-client"
import { myStack } from "@/lib/stack"
import { metaElementsToObject, normalizePath } from "@btst/stack/client"
import type { Metadata } from "next"

// Opt into SSG — Next.js generates this page at build time
export async function generateStaticParams() {
  return [{}]
}

// export const revalidate = 3600 // uncomment for ISR (1 hour)

export async function generateMetadata(): Promise<Metadata> {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["blog"]))
  if (!route) return { title: "Blog" }
  await myStack.api.blog.prefetchForRoute("posts", queryClient)
  return metaElementsToObject(route.meta?.() ?? []) satisfies Metadata
}

export default async function BlogListPage() {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["blog"]))
  if (!route) return null
  // Reads directly from DB — works at build time, no HTTP server required
  await myStack.api.blog.prefetchForRoute("posts", queryClient)
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

For individual post pages, also generate the static params list:

```tsx title="app/pages/blog/[slug]/page.tsx"
export async function generateStaticParams() {
  const { items } = await myStack.api.blog.getAllPosts({ published: true, limit: 1000 })
  return items.map((p) => ({ slug: p.slug }))
}

export default async function BlogPostPage({ params }: { params: { slug: string } }) {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["blog", params.slug]))
  if (!route) return null
  await myStack.api.blog.prefetchForRoute("post", queryClient, { slug: params.slug })
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

### ISR cache invalidation

If you use [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration), the static page cache must be purged whenever content changes. Wire up `revalidatePath` (or `revalidateTag`) inside the backend lifecycle hooks so Next.js regenerates the page on the next request:

```ts title="lib/stack.ts"
import { revalidatePath } from "next/cache"
import type { BlogBackendHooks } from "@btst/stack/plugins/blog"

const blogHooks: BlogBackendHooks = {
  onPostCreated: async (post) => {
    revalidatePath("/blog")
    revalidatePath(`/blog/${post.slug}`)
  },
  onPostUpdated: async (post) => {
    revalidatePath("/blog")
    revalidatePath(`/blog/${post.slug}`)
  },
  onPostDeleted: async (postId) => {
    revalidatePath("/blog")
  },
}
```

<Callout type="info">
  `revalidatePath` / `revalidateTag` are Next.js APIs — import them from `"next/cache"`. They are no-ops outside of a Next.js runtime, so this pattern is safe to use in the `lib/stack.ts` shared file without breaking other frameworks.
</Callout>

### Query key consistency

`prefetchForRoute` uses the same query key shapes as `createBlogQueryKeys` (the HTTP client). The shared constants live in `@btst/stack/plugins/blog/api` as `BLOG_QUERY_KEYS` and `postsListDiscriminator`, so the two paths can never drift silently.

## Shadcn Registry

The Blog plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/blog/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-blog.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/blog/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"
// Import your ejected (and customized) page components
import { HomePageComponent } from "@/components/btst/blog/client/components/pages/home-page"
import { PostPageComponent } from "@/components/btst/blog/client/components/pages/post-page"

blogClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  siteBaseURL: "...",
  siteBasePath: "/pages",
  queryClient,
  pageComponents: {
    posts: HomePageComponent,       // replaces the published posts list page
    post: PostPageComponent,        // replaces the single post page
    // drafts, newPost, editPost, tag — omit to keep built-in defaults
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.


# CMS Plugin (/plugins/cms)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";

import Image from "next/image";

The CMS plugin provides a headless content management system where developers define content types as Zod schemas in code. This "agency workflow" approach means:

* **Developers** define the content model (schemas, validation rules, field descriptions)
* **Clients** manage content items through a friendly admin UI
* **TypeScript** provides end-to-end type safety when schema shapes change

import cmsDemo from "../../../assets/cms-demo.png";
import cmsDemo1 from "../../../assets/cms-demo-1.png";
import cmsDemo2 from "../../../assets/cms-demo-2.png";

<div className="grid grid-cols-1 lg:grid-cols-2 gap-2 my-2">
  <a href={cmsDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={cmsDemo} alt="CMS Plugin Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={cmsDemo1.src} target="_blank" rel="noopener noreferrer">
    <Image src={cmsDemo1} alt="CMS Plugin Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={cmsDemo2.src} target="_blank" rel="noopener noreferrer">
    <Image src={cmsDemo2} alt="CMS Plugin Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

[View interactive demo →](/demos/cms)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

### 1. Define Content Types

Create your content types as Zod schemas in a shared file. This allows you to use the schemas on both server (for validation) and client (for type-safe hooks). Use `.meta()` to add descriptions and placeholders that appear in the admin UI:

```ts title="lib/cms-schemas.ts"
import { z } from "zod";

// ========== Product Schema ==========
// Use .meta({ fieldType: "..." }) to customize how fields render in the admin UI
export const ProductSchema = z.object({
  name: z.string().min(1).meta({ 
    description: "Product display name",
    placeholder: "Enter product name..." 
  }),
  description: z.string().meta({ 
    description: "Full product description",
    placeholder: "Describe this product...",
    fieldType: "textarea", // Renders as a textarea
  }),
  price: z.coerce.number().min(0).meta({ placeholder: "0.00" }),
  featured: z.boolean().default(false).meta({ 
    description: "Show on homepage featured section",
    fieldType: "switch", // Renders as a toggle switch
  }),
  category: z.enum(["Electronics", "Clothing", "Home", "Sports"]),
  image: z.string().optional().meta({
    description: "Product image",
    fieldType: "file", // Renders as file upload (uses uploadImage override)
  }),
});

// ========== Testimonial Schema ==========
export const TestimonialSchema = z.object({
  author: z.string().min(1).meta({ placeholder: "Customer name" }),
  company: z.string().optional().meta({ placeholder: "Company (optional)" }),
  quote: z.string().meta({ 
    description: "Customer testimonial text",
    placeholder: "What did they say?",
    fieldType: "textarea",
  }),
  rating: z.coerce.number().min(1).max(5).meta({ 
    description: "Rating out of 5 stars" 
  }),
});

// ========== Type Exports for Client Hooks ==========

/** Inferred type for Product data */
export type ProductData = z.infer<typeof ProductSchema>;

/** Inferred type for Testimonial data */
export type TestimonialData = z.infer<typeof TestimonialSchema>;

/**
 * Type map for all CMS content types.
 * Use this with CMS hooks for type-safe parsedData.
 */
export type CMSTypes = {
  product: ProductData;
  testimonial: TestimonialData;
};
```

### 2. Add Plugin to Backend API

Register the CMS backend plugin with your content types:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { cmsBackendPlugin } from "@btst/stack/plugins/cms/api"
import { ProductSchema, TestimonialSchema } from "./cms-schemas"

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    cms: cmsBackendPlugin({
      contentTypes: [
        { 
          name: "Product", 
          slug: "product", 
          description: "Products for the store",
          schema: ProductSchema,
          // Field types are defined in the schema via .meta({ fieldType: "..." })
        },
        { 
          name: "Testimonial", 
          slug: "testimonial", 
          description: "Customer testimonials",
          schema: TestimonialSchema,
        },
      ],
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

export { handler, dbSchema }
```

### 3. Add Plugin to Client

Register the CMS client plugin:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { cmsClientPlugin } from "@btst/stack/plugins/cms/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () => 
  process.env.BASE_URL || "http://localhost:3000"

export const getStackClient = (queryClient: QueryClient, options?: { headers?: Headers }) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      cms: cmsClientPlugin({
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient: queryClient,
        headers: options?.headers,
      })
    }
  })
}
```

### 4. Configure Provider Overrides

Add CMS overrides to your layout:

```tsx title="app/pages/layout.tsx"
import type { CMSPluginOverrides } from "@btst/stack/plugins/cms/client"

type PluginOverrides = {
  cms: CMSPluginOverrides,
}

<StackProvider<PluginOverrides>
  basePath="/pages"
  overrides={{
    cms: {
      apiBaseURL: baseURL,
      apiBasePath: "/api/data",
      navigate: (path) => router.push(path),
      refresh: () => router.refresh(),
      uploadImage: async (file) => {
        // Your image upload logic
        return "https://example.com/image.png"
      },
      Link: ({ href, ...props }) => <Link href={href || "#"} {...props} />,
    }
  }}
>
  {children}
</StackProvider>
```

### 5. Import CSS

Add the CMS styles to your global CSS:

```css title="app/globals.css"
@import "@btst/stack/plugins/cms/css";
```

## Supported Field Types

The CMS uses [AutoForm](https://github.com/vantezzen/autoform) to automatically render forms from Zod schemas. Use `.meta({ fieldType: "..." })` on any field to customize its rendering:

| Zod Type            | Default Handler | With `fieldType` Override |
| ------------------- | --------------- | ------------------------- |
| `z.string()`        | Input (text)    | `"textarea"`, `"file"`    |
| `z.coerce.number()` | Number input    | -                         |
| `z.boolean()`       | Checkbox        | `"switch"`                |
| `z.coerce.date()`   | Date picker     | -                         |
| `z.enum([...])`     | Select dropdown | `"radio"`                 |

### Adding UI Customization

Use `.meta()` to customize how fields appear and render. All field configuration is done directly in the Zod schema:

```ts
const ProductSchema = z.object({
  name: z.string().min(1).meta({ 
    description: "Product display name",  // Shows as help text
    placeholder: "Enter name..."          // Input placeholder
  }),
  bio: z.string().meta({
    description: "About this product",
    fieldType: "textarea",  // Renders as a multi-line textarea
  }),
  featured: z.boolean().default(false).meta({
    fieldType: "switch",  // Renders as a toggle switch instead of checkbox
  }),
  category: z.enum(["A", "B", "C"]).meta({
    fieldType: "radio",  // Renders as radio buttons instead of select
  }),
});
```

### Image Upload Fields

To add an image upload field to your content type:

1. Add an optional string field with `fieldType: "file"` in your schema:

```ts
const ProductSchema = z.object({
  name: z.string().min(1),
  image: z.string().optional().meta({ 
    description: "Product image URL",
    fieldType: "file",  // Renders as file upload
  }),
  // ...other fields
});
```

2. Provide `uploadImage` in your StackProvider overrides:

```ts
// In your StackProvider overrides
cms: {
  uploadImage: async (file: File) => {
    // Upload to S3, Cloudinary, etc. and return the URL
    const formData = new FormData();
    formData.append("file", file);
    const res = await fetch("/api/upload", { method: "POST", body: formData });
    const { url } = await res.json();
    return url;
  },
  // ...other overrides
}
```

The built-in file component will use your `uploadImage` function to upload files and store the returned URL.

## Admin Routes

The CMS plugin provides these admin routes:

| Route                | Description                                        |
| -------------------- | -------------------------------------------------- |
| `/cms`               | Dashboard - Grid of content types with item counts |
| `/cms/:typeSlug`     | Content list - Paginated table of items            |
| `/cms/:typeSlug/new` | Create new item                                    |
| `/cms/:typeSlug/:id` | Edit existing item                                 |

<Callout type="warn">
  Admin routes are automatically set to `noindex` for SEO. Don't include them in your public sitemap.
</Callout>

### Page Component Overrides

You can replace any built-in admin page with your own React component using the optional `pageComponents` field in `cmsClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
cmsClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the CMS dashboard page
    dashboard: MyCustomDashboard,
    // Replace the content list page — receives typeSlug as a prop
    contentList: ({ typeSlug }) => <MyCustomContentList typeSlug={typeSlug} />,
    // Replace the new content page — receives typeSlug as a prop
    newContent: ({ typeSlug }) => <MyCustomNewContent typeSlug={typeSlug} />,
    // Replace the edit content page — receives typeSlug and id as props
    editContent: ({ typeSlug, id }) => (
      <MyCustomEditContent typeSlug={typeSlug} id={id} />
    ),
  },
})
```

## Client Hooks

Fetch content data in your frontend pages using the provided hooks. All hooks support **optional type generics** for full type safety on `parsedData`.

### Available Hooks

#### Query Hooks

| Hook                                              | Description                                | Returns                                                                         |
| ------------------------------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------- |
| `useContentTypes()`                               | List all content types                     | `{ contentTypes, isLoading, error, refetch }`                                   |
| `useContentType(slug)`                            | Get single content type by slug            | `{ contentType, isLoading, error, refetch }`                                    |
| `useContent(typeSlug, options?)`                  | List paginated items with infinite loading | `{ items, total, hasMore, loadMore, isLoadingMore, isLoading, error, refetch }` |
| `useContentItem(typeSlug, id)`                    | Get item by ID                             | `{ item, isLoading, error, refetch }`                                           |
| `useContentItemBySlug(typeSlug, slug)`            | Get item by slug                           | `{ item, isLoading, error, refetch }`                                           |
| `useContentItemPopulated(typeSlug, id)`           | Get item with relations populated          | `{ item, isLoading, error, refetch }`                                           |
| `useContentByRelation(typeSlug, field, targetId)` | Filter items by relation                   | `{ items, total, hasMore, loadMore, isLoadingMore, isLoading, error, refetch }` |

#### Suspense Hooks

All query hooks have suspense variants for use with React Suspense:

| Hook                                                      | Description                        | Returns                                                       |
| --------------------------------------------------------- | ---------------------------------- | ------------------------------------------------------------- |
| `useSuspenseContentTypes()`                               | List all content types (suspense)  | `{ contentTypes, refetch }`                                   |
| `useSuspenseContent(typeSlug, options?)`                  | List paginated items (suspense)    | `{ items, total, hasMore, loadMore, isLoadingMore, refetch }` |
| `useSuspenseContentItem(typeSlug, id)`                    | Get item by ID (suspense)          | `{ item, refetch }`                                           |
| `useSuspenseContentItemPopulated(typeSlug, id)`           | Get item with relations (suspense) | `{ item, refetch }`                                           |
| `useSuspenseContentByRelation(typeSlug, field, targetId)` | Filter by relation (suspense)      | `{ items, total, hasMore, loadMore, isLoadingMore, refetch }` |

#### Mutation Hooks

| Hook                         | Description     | Returns              |
| ---------------------------- | --------------- | -------------------- |
| `useCreateContent(typeSlug)` | Create mutation | React Query mutation |
| `useUpdateContent(typeSlug)` | Update mutation | React Query mutation |
| `useDeleteContent(typeSlug)` | Delete mutation | React Query mutation |

### Basic Usage (Without Type Safety)

```tsx
import { 
  useContentTypes,
  useContent,
  useContentItem,
  useContentItemBySlug 
} from "@btst/stack/plugins/cms/client/hooks"

// List all content types
function ContentTypesGrid() {
  const { contentTypes, isLoading } = useContentTypes()
  // ...
}

// List paginated content items
function ProductList() {
  const { items, total, hasMore } = useContent("product", { limit: 20 })
  // items[0].parsedData is Record<string, unknown>
}
```

### Type-Safe Usage (Recommended)

Import your `CMSTypes` type map and pass it to the hooks for full type inference on `parsedData`:

```tsx
import { useContent, useContentItem, useContentItemBySlug } from "@btst/stack/plugins/cms/client/hooks"
import type { CMSTypes } from "@/lib/cms-schemas"

// List products with type-safe parsedData
function ProductList() {
  const { items, total, hasMore } = useContent<CMSTypes, "product">("product", { 
    limit: 20 
  })
  
  return (
    <ul>
      {items.map((item) => (
        <li key={item.id}>
          {/* All fields are fully typed! */}
          <h3>{item.parsedData.name}</h3>
          <p>${item.parsedData.price}</p>
          <span>{item.parsedData.category}</span>
          {item.parsedData.featured && <Badge>Featured</Badge>}
        </li>
      ))}
    </ul>
  )
}

// Get single item by ID with type safety
function ProductDetail({ id }: { id: string }) {
  const { item, isLoading } = useContentItem<CMSTypes, "product">("product", id)
  
  if (isLoading || !item) return <Skeleton />
  
  return (
    <div>
      <h1>{item.parsedData.name}</h1>
      <p>{item.parsedData.description}</p>
    </div>
  )
}

// Get single item by slug with type safety
function ProductPage({ slug }: { slug: string }) {
  const { item } = useContentItemBySlug<CMSTypes, "product">("product", slug)
  // item.parsedData.price is typed as number
}
```

<Callout type="info">
  The type generics are optional for backward compatibility. Without them, `parsedData` defaults to `Record<string, unknown>`.
</Callout>

### Mutations

Mutation hooks also support type generics for type-safe input data:

```tsx
import { 
  useCreateContent,
  useUpdateContent,
  useDeleteContent 
} from "@btst/stack/plugins/cms/client/hooks"
import type { ProductData } from "@/lib/cms-schemas"

function CreateProductForm() {
  // Type-safe mutation - TypeScript enforces correct data shape
  const createProduct = useCreateContent<ProductData>("product")
  
  const handleSubmit = async () => {
    await createProduct.mutateAsync({
      slug: "my-product",
      data: { 
        name: "New Product", 
        description: "A great product",
        price: 29.99,
        featured: false,
        category: "Electronics", // TypeScript autocompletes enum values!
      }
    })
  }
}

function UpdateProductForm({ id }: { id: string }) {
  const updateProduct = useUpdateContent<ProductData>("product")
  
  const handleUpdate = async () => {
    await updateProduct.mutateAsync({
      id,
      data: { data: { name: "Updated Name", price: 39.99 } }
    })
  }
}
```

## Backend Hooks

Customize CMS behavior with backend hooks:

```ts
cmsBackendPlugin({
  contentTypes: [...],
  hooks: {
    onBeforeCreate: async (data, context) => {
      console.log("Creating item in", context.typeSlug)
      // Return modified data to allow, throw to deny
      return data
    },
    onAfterCreate: async (item, context) => {
      console.log("Created:", item.slug)
      // Trigger webhooks, notifications, etc.
    },
    onBeforeUpdate: async (id, data, context) => {
      // Return modified data to allow, throw to deny
      return data
    },
    onAfterUpdate: async (item, context) => {
      // ...
    },
    onBeforeDelete: async (id, context) => {
      // Throw to deny: throw new Error("Cannot delete published content")
    },
    onAfterDelete: async (id, context) => {
      // ...
    },
    onError: async (error, operation, context) => {
      console.error(`CMS ${operation} error:`, error.message)
    },
  },
})
```

## Type Safety

The CMS plugin provides **end-to-end type safety** from schema definition to frontend rendering:

### 1. Schema Definition → Backend Validation

Zod schemas defined in `cms-schemas.ts` are used by the backend to validate all content operations:

```ts
// lib/cms-schemas.ts
export const ProductSchema = z.object({
  name: z.string().min(1),
  price: z.coerce.number().min(0),
});
```

### 2. Type Map → Client Hooks

Export inferred types and a type map for client-side type safety:

```ts
// lib/cms-schemas.ts
export type ProductData = z.infer<typeof ProductSchema>;
export type CMSTypes = { product: ProductData };
```

### 3. Type-Safe Data Access

Use the type map with hooks to get fully typed `parsedData`:

```tsx
import { useContent } from "@btst/stack/plugins/cms/client/hooks"
import type { CMSTypes } from "@/lib/cms-schemas"

function ProductList() {
  const { items } = useContent<CMSTypes, "product">("product")
  
  // ✅ TypeScript knows all field types
  items[0].parsedData.name   // string
  items[0].parsedData.price  // number
  
  // ❌ TypeScript error: Property 'invalid' does not exist
  items[0].parsedData.invalid
}
```

### 4. Schema Changes Trigger Compile Errors

When you update a schema, TypeScript shows errors everywhere the types are used:

```ts
// Adding a new required field to ProductSchema...
const ProductSchema = z.object({
  name: z.string(),
  price: z.number(),
  sku: z.string(), // New field
});

// ...triggers TypeScript errors in components
<span>{item.parsedData.sku}</span> // ✅ Now works
createProduct.mutate({ 
  slug: "x", 
  data: { name: "X", price: 10 } // ❌ Error: missing 'sku'
})
```

This ensures developers catch schema changes at compile time rather than in production.

## API Endpoints

The CMS plugin exposes these REST endpoints:

| Endpoint                           | Method | Description                                     |
| ---------------------------------- | ------ | ----------------------------------------------- |
| `/content-types`                   | GET    | List all content types with item counts         |
| `/content-types/:slug`             | GET    | Get single content type by slug                 |
| `/content/:typeSlug`               | GET    | List items (query: `slug`, `limit`, `offset`)   |
| `/content/:typeSlug`               | POST   | Create item                                     |
| `/content/:typeSlug/:id`           | GET    | Get single item                                 |
| `/content/:typeSlug/:id`           | PUT    | Update item                                     |
| `/content/:typeSlug/:id`           | DELETE | Delete item                                     |
| `/content/:typeSlug/:id/populated` | GET    | Get item with relations populated               |
| `/content/:typeSlug/populated`     | GET    | List items with relations populated             |
| `/content/:typeSlug/by-relation`   | GET    | Filter by relation (query: `field`, `targetId`) |

## Authorization & Lifecycle Hooks

The CMS plugin provides two levels of hooks for authorization:

### Client Hooks (SSR Authorization)

Use `hooks` in the client plugin config for **async authorization** during SSR. These run in loaders before pages render, supporting async session checks and redirects:

```tsx title="lib/stack-client.tsx"
import { redirect } from "next/navigation" // or your framework's redirect

cms: cmsClientPlugin({
  apiBaseURL: baseURL,
  apiBasePath: "/api/data",
  siteBaseURL: baseURL,
  siteBasePath: "/pages",
  queryClient: queryClient,
  headers: options?.headers,
  hooks: {
    beforeLoadDashboard: async (context) => {
      const session = await getSession(context.headers)
      return session?.user?.isAdmin === true
    },
    beforeLoadContentList: async (typeSlug, context) => {
      const session = await getSession(context.headers)
      return session?.user?.isAdmin === true
    },
    beforeLoadContentEditor: async (typeSlug, id, context) => {
      const session = await getSession(context.headers)
      return session?.user?.isAdmin === true
    },
    onLoadError: (error, context) => {
      // Redirect to login on authorization failure
      redirect("/auth/sign-in")
    },
  },
})
```

<Callout type="info">
  **Use client hooks for SSR.** These hooks run during server-side data loading and support async operations like session checks. The `onLoadError` hook is called when any `beforeLoad*` hook returns `false`, allowing you to redirect unauthorized users.
</Callout>

### Override Hooks (Client-Side)

Use lifecycle hooks in `StackProvider` overrides for **synchronous** client-side checks (SPA navigation):

```tsx title="app/pages/layout.tsx"
cms: {
  // ...required overrides
  onBeforeDashboardRendered: (context) => {
    // Sync check - runs during component render
    if (user?.isAdmin !== true) throw new Error("Admin access required")
  },
  onBeforeListRendered: (typeSlug, context) => {
    // Throw to deny: throw new Error("Unauthorized")
  },
  onBeforeEditorRendered: (typeSlug, id, context) => {
    // id is null for new items
    // Throw to deny: throw new Error("Unauthorized")
  },
  onRouteRender: (routeName, context) => {
    // Track page views
  },
  onRouteError: (routeName, error, context) => {
    // Log errors
  },
}
```

<Callout type="warn">
  **Override hooks are synchronous.** They run during component render and cannot await async operations. For SSR authorization with session checks, use the client hooks above.
</Callout>

## Custom Field Components

You can provide custom field components via the `fieldComponents` override. This allows you to:

* **Override built-in types** (like "file") with custom implementations
* **Add custom field types** for specialized inputs (rich text editors, color pickers, etc.)

### Using fieldComponents Override

The `fieldComponents` property maps field type names to React components:

```tsx
import type { CMSPluginOverrides, AutoFormInputComponentProps } from "@btst/stack/plugins/cms/client"

// Define a custom component
function MyColorPicker({ field, label, isRequired, fieldConfigItem }: AutoFormInputComponentProps) {
  return (
    <div className="space-y-2">
      <label className="text-sm font-medium">
        {label}
        {isRequired && <span className="text-destructive"> *</span>}
      </label>
      <input
        type="color"
        value={field.value || "#000000"}
        onChange={(e) => field.onChange(e.target.value)}
        className="h-10 w-full cursor-pointer"
      />
      {fieldConfigItem?.description && (
        <p className="text-sm text-muted-foreground">{String(fieldConfigItem.description)}</p>
      )}
    </div>
  )
}

// In your StackProvider overrides:
cms: {
  fieldComponents: {
    // Override the built-in "file" type
    file: ({ field, label, isRequired }) => (
      <MyCustomFileUpload
        value={field.value}
        onChange={field.onChange}
        label={label}
        required={isRequired}
      />
    ),
    // Add a custom "color" type
    color: MyColorPicker,
    // Add a custom "richText" type
    richText: ({ field, label }) => (
      <MyRichTextEditor value={field.value} onChange={field.onChange} label={label} />
    ),
  },
  // ...other overrides
}
```

### Registering Custom Field Types

To use a custom field type, add it to your Zod schema with `.meta({ fieldType: "..." })`:

```ts
// In your schema definition
const ProductSchema = z.object({
  name: z.string().min(1),
  primaryColor: z.string().optional().meta({
    description: "Brand color",
    fieldType: "color",     // Uses custom "color" component from fieldComponents
  }),
  longDescription: z.string().optional().meta({
    description: "Rich text content",
    fieldType: "richText",  // Uses custom "richText" component from fieldComponents
  }),
});
```

### AutoFormInputComponentProps

Custom components receive these props:

| Prop              | Type                    | Description                                                  |
| ----------------- | ----------------------- | ------------------------------------------------------------ |
| `field`           | `ControllerRenderProps` | React Hook Form field controller with `value` and `onChange` |
| `label`           | `string`                | The field label (derived from schema key)                    |
| `isRequired`      | `boolean`               | Whether the field is required                                |
| `fieldConfigItem` | `FieldConfigItem`       | Field config including `description`, `inputProps`, etc.     |
| `fieldProps`      | `object`                | Additional props from `inputProps` in fieldConfig            |
| `zodItem`         | `ZodAny`                | The Zod schema for this field                                |

### Using the Built-in CMSFileUpload

The plugin exports `CMSFileUpload` for consumers who want to use or extend the default file upload:

```tsx
import { CMSFileUpload } from "@btst/stack/plugins/cms/client"

// In your fieldComponents override
cms: {
  fieldComponents: {
    // Use the built-in component with your upload function
    file: (props) => (
      <CMSFileUpload {...props} uploadImage={myUploadFn} />
    ),
    // Or create a wrapper with custom styling
    customImage: (props) => (
      <div className="my-custom-wrapper">
        <CMSFileUpload {...props} uploadImage={myUploadFn} />
      </div>
    ),
  },
}
```

<Callout type="info">
  When a custom component is provided for a field type via `fieldComponents`, it takes precedence over the built-in component. This allows you to completely customize how any field type is rendered.
</Callout>

## Data Relationships

The CMS plugin supports relationships between content types, enabling you to build directories, blogs with tags, or any relational data structure. Relationships are defined in your Zod schemas using `.meta({ fieldType: "relation", relation: {...} })`.

### Defining Relationships

Add a relation field to your schema:

```ts title="lib/cms-schemas.ts"
import { z } from "zod";

// Category schema (the target of the relation)
export const CategorySchema = z.object({
  name: z.string().min(1).meta({
    description: "Category name",
    placeholder: "Enter category name...",
  }),
  description: z.string().optional().meta({
    description: "Optional category description",
    fieldType: "textarea",
  }),
  color: z.string().optional().meta({
    description: "Category color (hex code)",
    placeholder: "#3b82f6",
  }),
});

// Resource schema with a manyToMany relation to categories
export const ResourceSchema = z.object({
  name: z.string().min(1).meta({
    description: "Resource name",
    placeholder: "Enter resource name...",
  }),
  description: z.string().meta({
    description: "Full resource description",
    fieldType: "textarea",
  }),
  website: z.string().url().optional().meta({
    description: "Website URL",
    placeholder: "https://example.com",
  }),
  // Relation field - manyToMany with categories
  categoryIds: z
    .array(z.object({ id: z.string() }))
    .default([])
    .meta({
      fieldType: "relation",
      relation: {
        type: "manyToMany",
        targetType: "category",    // Slug of the target content type
        displayField: "name",      // Field to display in the selector
        creatable: true,           // Allow creating new categories inline
      },
    }),
});

export type CategoryData = z.infer<typeof CategorySchema>;
export type ResourceData = z.infer<typeof ResourceSchema>;

export type CMSTypes = {
  category: CategoryData;
  resource: ResourceData;
};
```

### Relationship Types

| Type         | Description                      | Schema Format                             | Use Case                                 |
| ------------ | -------------------------------- | ----------------------------------------- | ---------------------------------------- |
| `belongsTo`  | Single reference to another item | `z.object({ id: z.string() }).optional()` | Comment → Resource (one-to-many inverse) |
| `hasMany`    | Multiple references              | `z.array(z.object({ id: z.string() }))`   | Author → Posts                           |
| `manyToMany` | Many-to-many via junction table  | `z.array(z.object({ id: z.string() }))`   | Resource ↔ Categories                    |

<Callout type="info">
  **belongsTo vs manyToMany**: Use `belongsTo` when an item references a single parent (e.g., a Comment belongs to one Resource). Use `manyToMany` when items can have multiple relationships (e.g., a Resource can have many Categories).
</Callout>

#### belongsTo Example (One-to-Many)

For one-to-many relationships, the "many" side uses `belongsTo` to reference the "one" side:

```ts title="lib/cms-schemas.ts"
// Resource Schema - the "one" side
export const ResourceSchema = z.object({
  name: z.string().min(1),
  description: z.string(),
  // ... other fields
});

// Comment Schema - the "many" side (belongs to Resource)
export const CommentSchema = z.object({
  author: z.string().min(1).meta({
    description: "Comment author name",
    placeholder: "Your name...",
  }),
  content: z.string().min(1).meta({
    description: "Comment content",
    placeholder: "Write your comment...",
    fieldType: "textarea",
  }),
  // belongsTo relation - links to a single Resource
  // Unlike manyToMany (array), belongsTo stores a single { id: string }
  resourceId: z.object({ id: z.string() }).optional().meta({
    fieldType: "relation",
    relation: {
      type: "belongsTo",
      targetType: "resource",
      displayField: "name",
    },
  }),
});
```

The admin UI renders `belongsTo` fields as a single-select dropdown instead of a multi-select.

### RelationConfig Properties

| Property       | Type                                       | Description                                                        |
| -------------- | ------------------------------------------ | ------------------------------------------------------------------ |
| `type`         | `"belongsTo" \| "hasMany" \| "manyToMany"` | The relationship type                                              |
| `targetType`   | `string`                                   | Slug of the target content type                                    |
| `displayField` | `string`                                   | Field to show in the selector (e.g., "name", "title")              |
| `creatable`    | `boolean`                                  | Allow creating new related items inline (optional, default: false) |

### Relation Hooks

Use these hooks to fetch content with populated relations:

```tsx
import { 
  useContentItemPopulated,
  useContentByRelation 
} from "@btst/stack/plugins/cms/client/hooks"
import type { CMSTypes } from "@/lib/cms-schemas"

// Get a single resource with its related categories populated
function ResourceDetail({ id }: { id: string }) {
  const { item, isLoading } = useContentItemPopulated<CMSTypes, "resource">(
    "resource", 
    id
  )

  if (isLoading || !item) return <Skeleton />

  return (
    <div>
      <h1>{item.parsedData.name}</h1>
      <p>{item.parsedData.description}</p>
      
      {/* Related categories are populated in _relations */}
      <div className="flex gap-2">
        {item._relations?.categoryIds?.map((category) => (
          <span key={category.id} className="badge">
            {category.parsedData.name}
          </span>
        ))}
      </div>
    </div>
  )
}

// Get resources filtered by a specific category
function CategoryResources({ categoryId }: { categoryId: string }) {
  const { items, isLoading } = useContentByRelation<CMSTypes, "resource">(
    "resource",
    "categoryIds",  // Field name containing the relation
    categoryId      // ID of the related category
  )

  return (
    <ul>
      {items.map((resource) => (
        <li key={resource.id}>{resource.parsedData.name}</li>
      ))}
    </ul>
  )
}
```

### Inline Creation

When `creatable: true` is set in the relation config, users can create new related items directly from the relation selector. A modal form will appear allowing them to create a new item (e.g., a new category) without leaving the current form.

```ts
categoryIds: z
  .array(z.object({ id: z.string() }))
  .default([])
  .meta({
    fieldType: "relation",
    relation: {
      type: "manyToMany",
      targetType: "category",
      displayField: "name",
      creatable: true,  // Shows "Create new..." option in selector
    },
  }),
```

### Inverse Relations Panel

When editing content in the CMS admin, an **Inverse Relations Panel** automatically appears below the form. This panel shows all items that reference the current item via `belongsTo` relations.

For example, when editing a Resource, the panel displays all Comments that belong to that Resource:

```
┌─────────────────────────────────────────────┐
│ 📝 Comments (3)                         [▼] │
├─────────────────────────────────────────────┤
│ • "Great resource!" by John     [Edit] [🗑] │
│ • "Very helpful" by Jane        [Edit] [🗑] │
│ • "Thanks!" by Bob              [Edit] [🗑] │
│                                             │
│ [+ Add Comment]                             │
└─────────────────────────────────────────────┘
```

The panel:

* Auto-discovers content types with `belongsTo` relations pointing to the current type
* Shows a count and list of related items with edit/delete links
* Provides an "Add" button to create new related items with the relation pre-filled

### Relation API Endpoints

| Endpoint                                             | Method | Description                                                           |
| ---------------------------------------------------- | ------ | --------------------------------------------------------------------- |
| `/content/:typeSlug/:id/populated`                   | GET    | Get item with relations populated                                     |
| `/content/:typeSlug/populated`                       | GET    | List items with relations populated                                   |
| `/content/:typeSlug/by-relation`                     | GET    | Filter by relation (query: `field`, `targetId`)                       |
| `/content-types/:slug/inverse-relations`             | GET    | Get content types that reference this type (query: `itemId` optional) |
| `/content-types/:slug/inverse-relations/:sourceType` | GET    | Get items referencing this item (query: `itemId`, `fieldName`)        |

**Example API calls:**

```bash
# Get resource with populated categories
curl /api/data/content/resource/abc123/populated

# Get all resources linked to a specific category
curl /api/data/content/resource/by-relation?field=categoryIds&targetId=cat456

# Get inverse relations for a resource (what types reference it)
curl /api/data/content-types/resource/inverse-relations?itemId=abc123

# Get all comments for a specific resource
curl /api/data/content-types/resource/inverse-relations/comment?itemId=abc123&fieldName=resourceId
```

### Creating Items with Relations via API

When creating content items via API, pass relation values based on the relation type:

#### manyToMany / hasMany Relations (Array)

```ts
// Link to existing categories (array format)
await fetch("/api/data/content/resource", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    slug: "my-resource",
    data: {
      name: "My Resource",
      description: "A great resource",
      categoryIds: [
        { id: "existing-category-id-1" },
        { id: "existing-category-id-2" },
      ],
    },
  }),
});

// Create new categories inline using _new flag
await fetch("/api/data/content/resource", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    slug: "my-resource",
    data: {
      name: "My Resource",
      description: "A great resource",
      categoryIds: [
        { id: "existing-category-id" },
        { _new: true, data: { name: "New Category", color: "#10b981" } },
      ],
    },
  }),
});
```

#### belongsTo Relations (Single Object)

```ts
// Create comment linked to a resource (single object format)
await fetch("/api/data/content/comment", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    slug: "my-comment",
    data: {
      author: "John Doe",
      content: "Great resource!",
      resourceId: { id: "existing-resource-id" },  // Single object, not array
    },
  }),
});
```

### Building a Directory

Here's a complete example of building a resource directory with categories:

```tsx title="app/directory/page.tsx"
"use client"
import { useContent } from "@btst/stack/plugins/cms/client/hooks"
import type { CMSTypes } from "@/lib/cms-schemas"

export default function DirectoryPage() {
  const { items: resources } = useContent<CMSTypes, "resource">("resource")
  const { items: categories } = useContent<CMSTypes, "category">("category")
  const [search, setSearch] = useState("")

  const filteredResources = resources.filter((r) =>
    r.parsedData.name.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <div className="flex gap-8">
      {/* Sidebar with categories */}
      <aside className="w-64">
        <h3>Categories</h3>
        <ul>
          {categories.map((cat) => (
            <li key={cat.id}>
              <Link href={`/directory/category/${cat.id}`}>
                {cat.parsedData.name}
              </Link>
            </li>
          ))}
        </ul>
      </aside>

      {/* Main content */}
      <main className="flex-1">
        <input
          type="text"
          placeholder="Search resources..."
          value={search}
          onChange={(e) => setSearch(e.target.value)}
        />
        
        <div className="grid grid-cols-3 gap-4">
          {filteredResources.map((resource) => (
            <Link key={resource.id} href={`/directory/${resource.id}`}>
              <h3>{resource.parsedData.name}</h3>
              <p>{resource.parsedData.description}</p>
            </Link>
          ))}
        </div>
      </main>
    </div>
  )
}
```

## API Reference

### Backend (`@btst/stack/plugins/cms/api`)

#### CMSBackendConfig

<AutoTypeTable path="../packages/stack/src/plugins/cms/types.ts" name="CMSBackendConfig" />

#### CMSBackendHooks

<AutoTypeTable path="../packages/stack/src/plugins/cms/types.ts" name="CMSBackendHooks" />

#### CMSHookContext

<AutoTypeTable path="../packages/stack/src/plugins/cms/types.ts" name="CMSHookContext" />

### Client (`@btst/stack/plugins/cms/client`)

#### cmsClientPlugin

<AutoTypeTable path="../packages/stack/src/plugins/cms/client/plugin.tsx" name="cmsClientPlugin" />

#### CMSClientConfig

<AutoTypeTable path="../packages/stack/src/plugins/cms/client/plugin.tsx" name="CMSClientConfig" />

#### CMSClientHooks

Customize client-side behavior with lifecycle hooks. These hooks run during SSR data loading and support async authorization:

<AutoTypeTable path="../packages/stack/src/plugins/cms/client/plugin.tsx" name="CMSClientHooks" />

**Example usage:**

```tsx title="lib/stack-client.tsx"
cms: cmsClientPlugin({
  // ... rest of the config
  headers: options?.headers,
  hooks: {
    beforeLoadDashboard: async (context) => {
      const session = await getSession(context.headers)
      return session?.user?.isAdmin === true
    },
    beforeLoadContentList: async (typeSlug, context) => {
      // Check per-content-type permissions
      return isAdmin(context.headers)
    },
    beforeLoadContentEditor: async (typeSlug, id, context) => {
      return isAdmin(context.headers)
    },
    onLoadError(error, context) {
      // Redirect on auth failure
      redirect("/auth/sign-in")
    },
  }
})
```

#### LoaderContext

<AutoTypeTable path="../packages/stack/src/plugins/cms/client/plugin.tsx" name="LoaderContext" />

#### CMSPluginOverrides

Configure framework-specific overrides and route lifecycle hooks:

<AutoTypeTable path="../packages/stack/src/plugins/cms/client/overrides.ts" name="CMSPluginOverrides" />

### Schema Converter Utilities (`@btst/stack/plugins/cms/client`)

The CMS plugin re-exports schema converter utilities for converting between Zod schemas and JSON Schema. These are useful when working with content types programmatically:

#### zodToFormSchema

Convert a Zod schema to JSON Schema with proper handling for dates, steps metadata, and date constraints:

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="zodToFormSchema" />

**Example:**

```ts
import { zodToFormSchema } from "@btst/stack/plugins/cms/client"

const jsonSchema = zodToFormSchema(ProductSchema, {
  steps: [
    { id: "basic", title: "Basic Info" },
    { id: "details", title: "Details" }
  ],
  stepGroupMap: {
    name: 0,
    price: 0,
    description: 1
  }
})
```

#### formSchemaToZod

Convert JSON Schema back to a Zod schema with proper handling for date fields, constraints, and steps metadata:

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="formSchemaToZod" />

**Example:**

```ts
import { formSchemaToZod } from "@btst/stack/plugins/cms/client"

// Convert JSON Schema from database to Zod for validation
const zodSchema = formSchemaToZod(jsonSchema)
const result = zodSchema.safeParse(data)
```

#### Utility Functions

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="hasSteps" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="getSteps" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="getStepGroupMap" />

#### Types

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="FormStep" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="FormSchemaMetadata" />

## Server-side Data Access

The CMS plugin exposes standalone getter functions for server-side and SSG use cases.

### Two patterns

**Pattern 1 — via `stack().api`**

```ts title="app/lib/stack.ts"
import { myStack } from "./stack";

const types  = await myStack.api.cms.getAllContentTypes();
const items  = await myStack.api.cms.getAllContentItems("posts", { limit: 10 });
const item   = await myStack.api.cms.getContentItemBySlug("posts", "my-first-post");
```

**Pattern 2 — direct import**

```ts
import {
  getAllContentTypes,
  getAllContentItems,
  getContentItemBySlug,
} from "@btst/stack/plugins/cms/api";

export async function generateStaticParams() {
  const result = await getAllContentItems(myAdapter, "posts", { limit: 100 });
  return result.items.map((item) => ({ slug: item.slug }));
}
```

### Available getters

| Function                                         | Description                                          |
| ------------------------------------------------ | ---------------------------------------------------- |
| `getAllContentTypes(adapter)`                    | Returns all registered content types, sorted by name |
| `getAllContentItems(adapter, typeSlug, params?)` | Returns paginated items for a content type           |
| `getContentItemBySlug(adapter, typeSlug, slug)`  | Returns a single item by slug, or `null`             |

### Server-side mutation — `createContentItem`

In addition to read-only getters, the CMS plugin exposes a **mutation function** for creating content items directly from server-side code.

<Callout type="warn">
  **`createContentItem` bypasses authorization hooks and Zod schema validation.** Hooks such as `onBeforeCreate` and `onAfterCreate` are **not** called, and the data payload is stored as-is without running the content type's schema validation. The caller is responsible for providing valid, relation-free data and for any access-control checks. For relation fields or schema validation, use the HTTP endpoint instead.
</Callout>

**Via `myStack.api.cms`:**

```ts
await myStack.api.cms.createContentItem("client-profile", {
  slug: `intake-${Date.now()}`,
  data: {
    clientName: "Sarah Chen",
    age: 34,
    riskTolerance: "moderate",
    recommendation: "Rebalance windfall 80% equity, 20% cash.",
    amlFlag: false,
    confidenceScore: 94,
  },
})
```

**Direct import:**

```ts
import { createCMSContentItem } from "@btst/stack/plugins/cms/api"

await createCMSContentItem(myStack.adapter, "client-profile", {
  slug: `intake-${Date.now()}`,
  data: { clientName: "Sarah Chen", age: 34, amlFlag: false },
})
```

Throws if:

* The content type slug is not found (run `ensureSynced` first if calling outside a plugin request)
* A content item with the same slug already exists in that content type

## Static Site Generation (SSG)

`route.loader()` makes HTTP requests to `apiBaseURL`, which silently fails during `next build` because no dev server is running. Use `prefetchForRoute()` instead — it reads directly from the database and pre-populates the React Query cache before rendering.

### `prefetchForRoute(routeKey, queryClient, params?)`

| Route key       | Params required                    | Data prefetched                      |
| --------------- | ---------------------------------- | ------------------------------------ |
| `"dashboard"`   | —                                  | All content types (with item counts) |
| `"contentList"` | `{ typeSlug: string }`             | Content types + first page of items  |
| `"newContent"`  | —                                  | All content types                    |
| `"editContent"` | `{ typeSlug: string; id: string }` | Content types + specific item        |

<Callout type="info">
  `prefetchForRoute` calls `ensureSynced(adapter)` internally before any DB query. This function is idempotent — concurrent calls during `generateStaticParams` + `generateMetadata` + `page` all share the same Promise and the schema sync runs exactly once.
</Callout>

### Next.js example

```tsx title="app/pages/cms/[typeSlug]/page.tsx"
import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
import { getOrCreateQueryClient } from "@/lib/query-client"
import { getStackClient } from "@/lib/stack-client"
import { myStack } from "@/lib/stack"
import { metaElementsToObject, normalizePath } from "@btst/stack/client"
import type { Metadata } from "next"

// Generate one static page per content type slug
export async function generateStaticParams() {
  const types = await myStack.api.cms.getAllContentTypes()
  return types.map((t) => ({ typeSlug: t.slug }))
}

export async function generateMetadata(
  { params }: { params: { typeSlug: string } }
): Promise<Metadata> {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["cms", params.typeSlug]))
  if (!route) return { title: "Content" }
  await myStack.api.cms.prefetchForRoute("contentList", queryClient, { typeSlug: params.typeSlug })
  return metaElementsToObject(route.meta?.() ?? []) satisfies Metadata
}

export default async function ContentListPage({ params }: { params: { typeSlug: string } }) {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["cms", params.typeSlug]))
  if (!route) return null
  await myStack.api.cms.prefetchForRoute("contentList", queryClient, { typeSlug: params.typeSlug })
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

### ISR cache invalidation

If you use [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration), call `revalidatePath` inside the backend lifecycle hooks so Next.js regenerates the page on the next request:

```ts title="lib/stack.ts"
import { revalidatePath } from "next/cache"
import { cmsBackendPlugin } from "@btst/stack/plugins/cms/api"

cmsBackendPlugin({
  contentTypes: { ... },
  hooks: {
    onAfterCreate: async (item, context) => {
      revalidatePath(`/cms/${context.typeSlug}`, "page")
    },
    onAfterUpdate: async (item, context) => {
      revalidatePath(`/cms/${context.typeSlug}`, "page")
    },
    onAfterDelete: async (id, context) => {
      revalidatePath(`/cms/${context.typeSlug}`, "page")
    },
  },
})
```

### Query key consistency

`prefetchForRoute` uses the same query key shapes as `createCMSQueryKeys` (the HTTP client). The shared constants live in `@btst/stack/plugins/cms/api` as `CMS_QUERY_KEYS` and `contentListDiscriminator`, so the two paths can never drift silently.

## Shadcn Registry

The CMS plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/cms/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-cms.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/cms/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { cmsClientPlugin } from "@btst/stack/plugins/cms/client"
// Import your ejected (and customized) page components
import { DashboardPageComponent } from "@/components/btst/cms/client/components/pages/dashboard-page"
import { ContentListPageComponent } from "@/components/btst/cms/client/components/pages/content-list-page"

cmsClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    dashboard: DashboardPageComponent,          // replaces the CMS dashboard page
    contentList: ContentListPageComponent,      // replaces the content list page
    // newContent, editContent — omit to keep built-in defaults
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.


# Plugin Development (/plugins/development)

Learn how to create custom plugins for BTST. Plugins extend your application with new features, routes, and API endpoints while maintaining full type safety across backend and frontend.

## Overview

A BTST plugin consists of two parts:

* **Backend Plugin** - Defines database schema and API endpoints
* **Client Plugin** - Provides routes, React components, and hooks

You can create plugins **inside your project** (like the [Todo example](#in-project-plugin-example)) or as a **standalone package** to publish on npm using the [Plugin Starter repository](https://github.com/better-stack-ai/plugin-starter).

## Core Concepts

### Plugin Architecture

```
your-plugin/
├── api/
│   ├── backend.ts          # Backend plugin (defineBackendPlugin)
│   ├── getters.ts          # Pure DB read functions — no HTTP context
│   ├── mutations.ts        # Server-side write functions — no hooks, no HTTP context
│   ├── query-key-defs.ts   # Shared query key shapes (prevents SSG/SSR drift)
│   └── serializers.ts      # Convert Date fields to strings for the query cache
├── client/
│   ├── client.tsx      # Client plugin with routes
│   ├── hooks.tsx       # React Query hooks
│   ├── components.tsx  # Page components
│   └── overrides.ts    # Framework adapter types
├── schema.ts           # Database schema definition
└── types.ts            # Shared TypeScript types
```

### Key Imports

**Backend Plugin APIs:**

```typescript
import { 
  defineBackendPlugin,  // Create a backend plugin
  createEndpoint,       // Define an API endpoint
  createDbPlugin,       // Define database schema
  type Adapter          // Database adapter type
} from "@btst/stack/plugins/api"
```

**Client Plugin APIs:**

```typescript
import { 
  defineClientPlugin,   // Create a client plugin
  createRoute,          // Define a route
  createApiClient,      // Type-safe API client
  isConnectionError     // Detect build-time "no server" fetch failures
} from "@btst/stack/plugins/client"
```

***

## Database Schema

Define your database models using `createDbPlugin`. Each model specifies fields with their types, constraints, and defaults.

```typescript
import { createDbPlugin } from "@btst/stack/plugins/api"

export const todosSchema = createDbPlugin("todos", {
  todo: {
    modelName: "todo",
    fields: {
      title: {
        type: "string",
        required: true
      },
      completed: {
        type: "boolean",
        defaultValue: false
      },
      createdAt: {
        type: "date",
        defaultValue: () => new Date()
      }
    }
  }
})
```

**Field Types:**

* `string` - Text values
* `boolean` - True/false values
* `number` - Numeric values
* `date` - Date/time values

**Field Options:**

* `required` - Field must have a value
* `defaultValue` - Default value (can be a function)
* `unique` - Value must be unique across all records

### Complex Schema Example (Blog Plugin)

For plugins with relationships, define multiple models:

```typescript
export const blogSchema = createDbPlugin("blog", {
  post: {
    modelName: "post",
    fields: {
      title: { type: "string", required: true },
      content: { type: "string", required: true },
      slug: { type: "string", required: true, unique: true },
      published: { type: "boolean", defaultValue: false },
      publishedAt: { type: "date", required: false },
      createdAt: { type: "date", defaultValue: () => new Date() },
      updatedAt: { type: "date", defaultValue: () => new Date() },
    }
  },
  tag: {
    modelName: "tag",
    fields: {
      name: { type: "string", required: true, unique: true },
      slug: { type: "string", required: true, unique: true },
      createdAt: { type: "date", defaultValue: () => new Date() },
    }
  },
  postTag: {
    modelName: "postTag",
    fields: {
      postId: { type: "string", required: true },
      tagId: { type: "string", required: true },
    }
  }
})
```

***

## Backend Plugin

The backend plugin defines your API endpoints using the database adapter.

### Basic Structure

```typescript
import { type Adapter, defineBackendPlugin, createEndpoint } from "@btst/stack/plugins/api"
import { z } from "zod"
import { todosSchema as dbSchema } from "../schema"
import type { Todo } from "../types"

// Request validation schemas
const createTodoSchema = z.object({
  title: z.string().min(1, "Title is required"),
  completed: z.boolean().optional().default(false)
})

export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,
  
  routes: (adapter: Adapter) => {
    // Define endpoints here
    return { /* endpoints */ } as const
  }
})

// Export the router type for client-side type safety
export type TodosApiRouter = ReturnType<typeof todosBackendPlugin.routes>
```

### Creating Endpoints

Use `createEndpoint` to define type-safe API routes:

```typescript
routes: (adapter: Adapter) => {
  // GET /todos - List all todos
  const listTodos = createEndpoint(
    "/todos",
    { method: "GET" },
    async () => {
      const todos = await adapter.findMany<Todo>({
        model: "todo",
        sortBy: { field: "createdAt", direction: "desc" }
      })
      return todos || []
    }
  )

  // POST /todos - Create a todo
  const createTodo = createEndpoint(
    "/todos",
    { method: "POST", body: createTodoSchema },
    async (ctx) => {
      const { title, completed } = ctx.body
      return await adapter.create<Todo>({
        model: "todo",
        data: { title, completed: completed ?? false, createdAt: new Date() }
      })
    }
  )

  // PUT /todos/:id - Update a todo
  const updateTodo = createEndpoint(
    "/todos/:id",
    { method: "PUT", body: updateTodoSchema },
    async (ctx) => {
      const updated = await adapter.update({
        model: "todo",
        where: [{ field: "id", value: ctx.params.id }],
        update: ctx.body
      })
      if (!updated) throw new Error("Todo not found")
      return updated
    }
  )

  // DELETE /todos/:id - Delete a todo
  const deleteTodo = createEndpoint(
    "/todos/:id",
    { method: "DELETE" },
    async (ctx) => {
      await adapter.delete({
        model: "todo",
        where: [{ field: "id", value: ctx.params.id }]
      })
      return { success: true }
    }
  )

  return { listTodos, createTodo, updateTodo, deleteTodo } as const
}
```

### Adapter Operations

The adapter provides these database operations:

| Method                                                     | Description                     |
| ---------------------------------------------------------- | ------------------------------- |
| `findMany<T>({ model, where?, sortBy?, limit?, offset? })` | Query multiple records          |
| `create<T>({ model, data })`                               | Create a new record             |
| `update<T>({ model, where, update })`                      | Update matching records         |
| `delete<T>({ model, where })`                              | Delete matching records         |
| `transaction(async (tx) => { ... })`                       | Run operations in a transaction |

### Backend Hooks (Authorization & Lifecycle)

For more control, plugins can accept hooks for authorization and lifecycle events:

```typescript
export interface BlogBackendHooks {
  // Authorization hooks - throw an error to deny access
  onBeforeCreatePost?: (data, context) => Promise<void> | void
  onBeforeUpdatePost?: (postId, data, context) => Promise<void> | void
  onBeforeDeletePost?: (postId, context) => Promise<void> | void
  onBeforeListPosts?: (filter, context) => Promise<void> | void

  // Lifecycle hooks - called after operations
  onPostCreated?: (post, context) => Promise<void> | void
  onPostUpdated?: (post, context) => Promise<void> | void
  onPostDeleted?: (postId, context) => Promise<void> | void
  onPostsRead?: (posts, filter, context) => Promise<void> | void

  // Error hooks
  onCreatePostError?: (error, context) => Promise<void> | void
  onUpdatePostError?: (error, context) => Promise<void> | void
  onDeletePostError?: (error, context) => Promise<void> | void
  onListPostsError?: (error, context) => Promise<void> | void
}

export const blogBackendPlugin = (hooks?: BlogBackendHooks) =>
  defineBackendPlugin({
    name: "blog",
    dbPlugin: dbSchema,
    routes: (adapter: Adapter) => {
      const createPost = createEndpoint("/posts", { method: "POST", body: createPostSchema },
        async (ctx) => {
          // Authorization check — throw to deny, return to allow
          if (hooks?.onBeforeCreatePost) {
            try {
              await hooks.onBeforeCreatePost(ctx.body, { headers: ctx.headers })
            } catch (e) {
              throw ctx.error(403, { message: e instanceof Error ? e.message : "Unauthorized" })
            }
          }
          
          const post = await adapter.create({ model: "post", data: ctx.body })
          
          // Lifecycle callback
          if (hooks?.onPostCreated) {
            await hooks.onPostCreated(post, { headers: ctx.headers })
          }
          
          return post
        }
      )
      // ... more endpoints
    }
  })
```

### Server-side API (Getter Functions)

Plugins can expose a typed `api` surface that lets server code — Server Components, `generateStaticParams`, cron jobs, scripts — query the database directly, **without going through HTTP**.

<Callout type="warn">
  **Getter functions bypass authorization hooks.** Plugin hooks such as `onBeforeListPosts` or `onBeforeListForms` are **not** called when you invoke getters via `myStack.api.*`. These functions are pure database calls — the caller is fully responsible for performing any access-control checks before invoking them. Do not call getters from user-facing request handlers without adding your own authorization logic first.
</Callout>

Add an `api` factory to `defineBackendPlugin`. The factory receives the shared adapter and returns an object of async functions:

```typescript
export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,

  // Expose server-side getters bound to the adapter
  api: (adapter) => ({
    listTodos: () =>
      adapter.findMany<Todo>({ model: "todo", sortBy: { field: "createdAt", direction: "desc" } }),

    getTodoById: (id: string) =>
      adapter.findOne<Todo>({ model: "todo", where: [{ field: "id", value: id, operator: "eq" }] }),
  }),

  routes: (adapter: Adapter) => {
    // ... existing HTTP endpoints
  },
})
```

After calling `stack()`, the returned object exposes the combined `api` namespace — one key per plugin — plus the raw `adapter`:

```typescript
import { stack } from "@btst/stack"
import { todosBackendPlugin } from "./plugins/todo/api/backend"

export const myStack = stack({
  basePath: "/api/data",
  plugins: { todos: todosBackendPlugin },
  adapter: (db) => createMemoryAdapter(db)({}),
})

// Fully typed — no HTTP roundtrip
const todos = await myStack.api.todos.listTodos()
const todo  = await myStack.api.todos.getTodoById("abc-123")

// Or use the raw adapter directly
const raw = await myStack.adapter.findMany<Todo>({ model: "todo" })
```

**When to use this pattern:**

| Use case                         | Approach                                     |
| -------------------------------- | -------------------------------------------- |
| Server Component / RSC           | `myStack.api.todos.listTodos()`              |
| `generateStaticParams` (Next.js) | Import getters directly and pass any adapter |
| Cron job / script                | `myStack.api.*` or direct getter import      |
| HTTP route handler               | HTTP endpoint via `routes` as normal         |

**Tip — direct getter imports for SSG/build-time:**

If you need access to data before your `stack()` instance is available (e.g. at build time with a separate adapter), export the getter functions independently and pass an adapter yourself:

```typescript
// api/getters.ts
import type { Adapter } from "@btst/stack/plugins/api"
import type { Todo } from "../types"

export async function listTodos(adapter: Adapter) {
  return adapter.findMany<Todo>({ model: "todo" })
}

// api/backend.ts
import { listTodos } from "./getters"

export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,
  api: (adapter) => ({
    listTodos: () => listTodos(adapter),
  }),
  routes: (adapter) => { /* ... */ },
})

// In api/index.ts — re-export for consumers
export { listTodos } from "./getters"
```

### Server-side Mutations (`mutations.ts`)

Plugins can also expose **write operations** that bypass the HTTP layer — useful inside AI tool `execute` callbacks, cron jobs, admin scripts, or any server-side code that needs to create or update records without going through an HTTP endpoint.

Keep mutations in a **separate `api/mutations.ts`** file, distinct from the read-only `getters.ts`. Both are re-exported from `api/index.ts` and exposed on the `api` factory.

<Callout type="warn">
  **Mutation functions bypass authorization hooks.** Plugin hooks such as `onBeforeCreateTask` are **not** called when you use these functions directly. The caller is responsible for any access-control checks before invoking mutations. Never call them from user-facing request handlers without adding your own authorization logic first.
</Callout>

```typescript
// api/mutations.ts — write operations, no hooks, no HTTP context
import type { Adapter } from "@btst/stack/plugins/api"
import type { Todo } from "../types"

export interface CreateTodoInput {
  title: string
  description?: string
}

/**
 * Create a todo directly in the database.
 *
 * @remarks Authorization hooks are NOT called. The caller is responsible for
 * access-control checks.
 */
export async function createTodo(
  adapter: Adapter,
  input: CreateTodoInput,
): Promise<Todo> {
  return adapter.create<Todo>({
    model: "todo",
    data: {
      title: input.title,
      description: input.description,
      completed: false,
      createdAt: new Date(),
      updatedAt: new Date(),
    },
  })
}
```

Wire mutations into the `api` factory alongside the read methods:

```typescript
// api/backend.ts
import { listTodos } from "./getters"
import { createTodo, type CreateTodoInput } from "./mutations"

export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,
  api: (adapter) => ({
    // Reads
    listTodos: () => listTodos(adapter),
    // Mutations
    createTodo: (input: CreateTodoInput) => createTodo(adapter, input),
  }),
  routes: (adapter) => { /* HTTP endpoints */ },
})

// api/index.ts — re-export both
export { listTodos } from "./getters"
export { createTodo, type CreateTodoInput } from "./mutations"
```

**Common use case — inside an AI tool `execute` function:**

Because AI tool `execute` functions run at request time (after module initialization), the adapter can safely be captured via a module-level variable set immediately after `stack()` returns:

```typescript title="lib/stack.ts"
import { createTodo } from "./plugins/todo/api/mutations"

// eslint-disable-next-line @typescript-eslint/no-explicit-any
let _adapter: any

const myTool = tool({
  description: "Create a new task",
  inputSchema: z.object({ title: z.string() }),
  execute: async ({ title }) => {
    await createTodo(_adapter, { title })
    return { success: true }
  },
})

export const myStack = stack({
  plugins: {
    todos: todosBackendPlugin,
    aiChat: aiChatBackendPlugin({ tools: { myTool } }),
  },
  adapter: (db) => createMemoryAdapter(db)({}),
})

// Adapter is now available — execute() only fires during HTTP requests,
// which occur after module initialization is complete.
_adapter = myStack.adapter
```

***

## Client Plugin

The client plugin defines routes with React components, SSR data loaders, and SEO meta generators.

### Basic Structure

```typescript
import { createApiClient, defineClientPlugin, createRoute } from "@btst/stack/plugins/client"
import type { QueryClient } from "@tanstack/react-query"
import type { TodosApiRouter } from "../api/backend"
import { lazy } from "react"

export interface TodosClientConfig {
  queryClient: QueryClient
  apiBaseURL: string
  apiBasePath: string
  siteBaseURL: string
  siteBasePath: string
}

export const todosClientPlugin = (config: TodosClientConfig) =>
  defineClientPlugin({
    name: "todos",
    
    routes: () => ({
      todos: createRoute("/todos", () => {
        const TodosListPage = lazy(() =>
          import("./components").then((m) => ({ default: m.TodosListPage }))
        )
        
        return {
          PageComponent: TodosListPage,
          loader: todosLoader(config),
          meta: createTodosMeta(config, "/todos"),
        }
      }),
    }),
    
    sitemap: async () => [
      { 
        url: `${config.siteBaseURL}${config.siteBasePath}/todos`, 
        lastModified: new Date(), 
        priority: 0.7 
      },
    ],
  })
```

### SSR Data Loaders

Loaders prefetch data during server-side rendering. Always add an `isConnectionError` check in the `catch` block so developers get an actionable warning if they call `route.loader()` during `next build` when no HTTP server is running (instead of a silent empty page):

```typescript
import { createApiClient, isConnectionError } from "@btst/stack/plugins/client"

function todosLoader(config: TodosClientConfig) {
  return async () => {
    // Only run on server
    if (typeof window === "undefined") {
      const { queryClient, apiBasePath, apiBaseURL } = config
      
      try {
        await queryClient.prefetchQuery({
          queryKey: ["todos"],
          queryFn: async () => {
            const client = createApiClient<TodosApiRouter>({
              baseURL: apiBaseURL,
              basePath: apiBasePath,
            })
            const response = await client("/todos", { method: "GET" })
            return response.data
          },
        })
      } catch (error) {
        if (isConnectionError(error)) {
          console.warn(
            "[your-plugin] route.loader() failed — no server running at build time. " +
            "Use myStack.api.todos.prefetchForRoute() for SSG data prefetching."
          )
        }
        // Don't re-throw — let Error Boundaries handle it during render
      }
    }
  }
}
```

### SEO Meta Generators

Meta generators create SEO tags based on loaded data:

```typescript
function createTodosMeta(config: TodosClientConfig, path: string) {
  return () => {
    const { queryClient, siteBaseURL, siteBasePath } = config
    const todos = queryClient.getQueryData<Todo[]>(["todos"]) ?? []
    const fullUrl = `${siteBaseURL}${siteBasePath}${path}`
    
    return [
      { name: "title", content: `${todos.length} Todos` },
      { name: "description", content: `Track ${todos.length} todos.` },
      { property: "og:title", content: `${todos.length} Todos` },
      { property: "og:url", content: fullUrl },
      { name: "twitter:card", content: "summary" },
    ]
  }
}
```

### Static Site Generation (SSG)

`route.loader()` makes HTTP requests that **fail silently** during `next build` because no HTTP server is running. Plugins that support SSG must expose a `prefetchForRoute` method on the `api` factory so consumers can seed the query cache directly from the database at build time.

#### 1. Shared query key constants (`api/query-key-defs.ts`)

Create a file that both `query-keys.ts` (the HTTP client path) and `prefetchForRoute` (the DB path) import from. This prevents the two paths drifting out of sync silently:

```typescript
// api/query-key-defs.ts
export function todosListDiscriminator(params?: { limit?: number }) {
  return { limit: params?.limit ?? 20 }
}

export const TODO_QUERY_KEYS = {
  list: (params?: { limit?: number }) =>
    ["todos", "list", todosListDiscriminator(params)] as const,
  detail: (id: string) => ["todos", "detail", id] as const,
}
```

Import `todosListDiscriminator` in `query-keys.ts` so both paths use the identical key shape.

#### 2. Serializers (`api/serializers.ts`)

DB getters return `Date` objects; the HTTP path returns ISO strings. Always serialize before calling `setQueryData`:

```typescript
// api/serializers.ts
import type { Todo } from "../types"

export function serializeTodo(todo: Todo) {
  return {
    ...todo,
    createdAt: todo.createdAt.toISOString(),
  }
}
```

#### 3. `RouteKey` type and `prefetchForRoute` overloads (`api/backend.ts`)

Use typed function overloads so TypeScript enforces the correct `params` per route:

```typescript
import type { QueryClient } from "@tanstack/react-query"
import { TODO_QUERY_KEYS } from "./query-key-defs"
import { serializeTodo } from "./serializers"
import { listTodos, getTodoById } from "./getters"

export type TodosRouteKey = "list" | "detail" | "new"

interface TodosPrefetchForRoute {
  (key: "list" | "new", qc: QueryClient): Promise<void>
  (key: "detail", qc: QueryClient, params: { id: string }): Promise<void>
}

function createTodosPrefetchForRoute(adapter: Adapter): TodosPrefetchForRoute {
  return async function prefetchForRoute(
    key: TodosRouteKey,
    qc: QueryClient,
    params?: Record<string, string>,
  ): Promise<void> {
    switch (key) {
      case "list": {
        const todos = await listTodos(adapter)
        // Lists backed by useInfiniteQuery need the { pages, pageParams } shape
        qc.setQueryData(TODO_QUERY_KEYS.list(), {
          pages: [todos.map(serializeTodo)],
          pageParams: [0],
        })
        break
      }
      case "detail": {
        const todo = await getTodoById(adapter, params!.id)
        if (todo) qc.setQueryData(TODO_QUERY_KEYS.detail(params!.id), serializeTodo(todo))
        break
      }
      case "new":
        break // no data needed
    }
  } as TodosPrefetchForRoute
}

export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,
  api: (adapter) => ({
    listTodos: () => listTodos(adapter),
    getTodoById: (id: string) => getTodoById(adapter, id),
    prefetchForRoute: createTodosPrefetchForRoute(adapter), // ← SSG entry point
  }),
  routes: (adapter) => { /* ... HTTP endpoints */ },
})
```

#### 4. SSG `page.tsx` (consumer side, Next.js App Router)

The consumer creates a dedicated static page outside `[[...all]]/` that calls `prefetchForRoute` instead of `route.loader()`:

```tsx
// app/pages/todos/page.tsx
import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
import { notFound } from "next/navigation"
import { getOrCreateQueryClient } from "@/lib/query-client"
import { getStackClient } from "@/lib/stack-client"
import { myStack } from "@/lib/stack"
import { metaElementsToObject, normalizePath } from "@btst/stack/client"
import type { Metadata } from "next"

export async function generateStaticParams() { return [{}] }
// export const revalidate = 3600  // uncomment for ISR

export async function generateMetadata(): Promise<Metadata> {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["todos"]))
  if (!route) return { title: "Todos" }
  await myStack.api.todos.prefetchForRoute("list", queryClient)
  return metaElementsToObject(route.meta?.() ?? []) satisfies Metadata
}

export default async function TodosPage() {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["todos"]))
  if (!route) notFound()
  // Direct DB read — no HTTP server required at build time
  await myStack.api.todos.prefetchForRoute("list", queryClient)
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

<Callout type="info">
  The shared `StackProvider` layout must live at `app/pages/layout.tsx` (not inside `[[...all]]/layout.tsx`) so it applies to both the catch-all routes and these specific SSG pages.
</Callout>

#### 5. ISR cache invalidation

If you enable [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration) (`export const revalidate = 3600`), the cached page must be purged whenever the underlying data changes. Wire up `revalidatePath` (or `revalidateTag`) inside the backend plugin hooks:

```ts title="lib/stack.ts"
import { revalidatePath } from "next/cache"

const myPlugin = myBackendPlugin({
  hooks: {
    onAfterCreate: async (item) => {
      revalidatePath("/todos")
    },
    onAfterUpdate: async (item) => {
      revalidatePath("/todos")
    },
    onAfterDelete: async (id) => {
      revalidatePath("/todos")
    },
  },
})
```

<Callout type="info">
  `revalidatePath` / `revalidateTag` are Next.js APIs imported from `"next/cache"`. They are no-ops outside of a Next.js runtime, so it is safe to call them from a shared `lib/stack.ts` without breaking non-Next.js frameworks.
</Callout>

***

### Client Hooks

Type-safe React Query hooks using `createApiClient`:

```typescript
"use client"
import { createApiClient } from "@btst/stack/plugins/client"
import { useMutation, useQueryClient, useSuspenseQuery } from "@tanstack/react-query"
import type { TodosApiRouter } from "../api/backend"

export function useTodos() {
  const client = createApiClient<TodosApiRouter>({ baseURL: "/api/data" })

  return useSuspenseQuery({
    queryKey: ["todos"],
    queryFn: async () => {
      const response = await client("/todos", { method: "GET" })
      return response.data
    }
  })
}

export function useCreateTodo() {
  const client = createApiClient<TodosApiRouter>({ baseURL: "/api/data" })
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (data: { title: string }) => {
      // Note: @post prefix for POST requests
      const response = await client("@post/todos", {
        method: "POST",
        body: data
      })
      return response.data
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] })
    }
  })
}

export function useToggleTodo() {
  const client = createApiClient<TodosApiRouter>({ baseURL: "/api/data" })
  const queryClient = useQueryClient()

  return useMutation({
    mutationFn: async (data: { id: string; completed: boolean }) => {
      // Note: @put prefix and params for route parameters
      const response = await client("@put/todos/:id", {
        method: "PUT",
        params: { id: data.id },
        body: { completed: data.completed }
      })
      return response.data
    },
    // Optimistic updates
    onMutate: async (variables) => {
      await queryClient.cancelQueries({ queryKey: ["todos"] })
      const previousTodos = queryClient.getQueryData<Todo[]>(["todos"])
      
      queryClient.setQueryData<Todo[]>(["todos"], (old) =>
        old?.map((todo) =>
          todo.id === variables.id
            ? { ...todo, completed: variables.completed }
            : todo
        )
      )
      
      return { previousTodos }
    },
    onError: (_error, _variables, context) => {
      if (context?.previousTodos) {
        queryClient.setQueryData(["todos"], context.previousTodos)
      }
    },
    onSettled: () => {
      queryClient.invalidateQueries({ queryKey: ["todos"] })
    }
  })
}
```

### Framework Overrides

Define types for framework-specific components (Link, navigation):

```typescript
import type { ComponentType, ReactNode } from "react"

export interface TodosPluginOverrides {
  Link: ComponentType<{
    href: string
    children: ReactNode
    className?: string
  }>
  navigate?: (path: string) => void | Promise<void>
}
```

Use them in components:

```typescript
import { usePluginOverrides, useBasePath } from "@btst/stack/context"
import type { TodosPluginOverrides } from "./overrides"

function TodosList() {
  const { Link } = usePluginOverrides<TodosPluginOverrides>("todos")
  const basePath = useBasePath()
  
  return (
    <Link href={`${basePath}/todos/add`}>
      Add Todo
    </Link>
  )
}
```

### ComposedRoute

For production-ready page components, use `ComposedRoute` to wrap your pages with Suspense boundaries, error boundaries, and 404 handling:

```typescript
import { ComposedRoute } from "@btst/stack/client/components"
```

**Props:**

| Prop                | Type                                       | Description                                        |
| ------------------- | ------------------------------------------ | -------------------------------------------------- |
| `path`              | `string`                                   | Current route path (used for error boundary reset) |
| `PageComponent`     | `React.ComponentType`                      | The page component to render                       |
| `LoadingComponent`  | `React.ComponentType`                      | Component shown during Suspense                    |
| `ErrorComponent`    | `React.ComponentType<FallbackProps>`       | Error boundary fallback                            |
| `NotFoundComponent` | `React.ComponentType<{ message: string }>` | 404 fallback                                       |
| `props`             | `any`                                      | Props passed to PageComponent                      |
| `onError`           | `(error: Error, info: ErrorInfo) => void`  | Error callback                                     |

**Example from Blog Plugin:**

```typescript
"use client"
import { lazy } from "react"
import { ComposedRoute } from "@btst/stack/client/components"
import { usePluginOverrides } from "@btst/stack/context"
import type { BlogPluginOverrides } from "../../overrides"

// Lazy load the page content
const HomePage = lazy(() =>
  import("./home-page.internal").then((m) => ({ default: m.HomePage }))
)

// Loading skeleton component
function PostsLoading() {
  return <div className="animate-pulse">Loading posts...</div>
}

// Error fallback component
function DefaultError({ error, resetErrorBoundary }) {
  return (
    <div>
      <p>Something went wrong: {error.message}</p>
      <button onClick={resetErrorBoundary}>Try again</button>
    </div>
  )
}

// 404 component
function NotFoundPage({ message }) {
  return <div>Page not found: {message}</div>
}

// Exported page component with all boundaries
export function HomePageComponent({ published = true }) {
  const { onRouteError } = usePluginOverrides<BlogPluginOverrides>("blog")
  
  return (
    <ComposedRoute
      path={published ? "/blog" : "/blog/drafts"}
      PageComponent={HomePage}
      LoadingComponent={PostsLoading}
      ErrorComponent={DefaultError}
      NotFoundComponent={NotFoundPage}
      props={{ published }}
      onError={(error) => {
        onRouteError?.("posts", error, {
          path: published ? "/blog" : "/blog/drafts",
          isSSR: typeof window === "undefined",
        })
      }}
    />
  )
}
```

This pattern ensures:

* **Loading states** - Shows a skeleton while lazy components load
* **Error recovery** - Catches errors and provides reset functionality
* **404 handling** - Graceful fallback for missing routes
* **Error reporting** - Hooks into your error tracking via `onError`

***

## Plugin Registration

### Backend Registration

Register plugins in your BTST configuration:

```typescript
import { stack } from "@btst/stack"
import { createMemoryAdapter } from "@btst/adapter-memory"
import { todosBackendPlugin } from "./plugins/todo/api/backend"
import { blogBackendPlugin } from "@btst/stack/plugins/blog/api"

// Export the full stack instance so myStack.api.* is accessible anywhere
export const myStack = stack({
  basePath: "/api/data",
  plugins: {
    todos: todosBackendPlugin,
    blog: blogBackendPlugin({
      onBeforeCreatePost: async (data, context) => {
        // Throw to deny, return to allow
        // if (!session) throw new Error("Authentication required")
      },
      onPostCreated: async (post) => {
        console.log("Post created:", post.id)
      }
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

// Named re-exports for the HTTP route handler and DB schema
export const { handler, dbSchema } = myStack

// myStack also exposes:
//   myStack.adapter  — raw database adapter
//   myStack.api      — typed server-side getters per plugin
//
// Usage in a Server Component or generateStaticParams:
//   const todos = await myStack.api.todos.listTodos()
//   const todo  = await myStack.api.todos.getTodoById("abc-123")
//   const posts = await myStack.api.blog.getAllPosts({ published: true })
```

### Client Registration

Register client plugins with your stack client:

```typescript
import { createStackClient } from "@btst/stack/client"
import { todosClientPlugin } from "./plugins/todo/client/client"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"
import { QueryClient } from "@tanstack/react-query"

export const getStackClient = (queryClient: QueryClient) => {
  const baseURL = typeof window !== 'undefined' 
    ? window.location.origin 
    : "http://localhost:3000"
    
  return createStackClient({
    plugins: {
      todos: todosClientPlugin({
        queryClient,
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
      }),
      blog: blogClientPlugin({
        queryClient,
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        seo: {
          siteName: "My Blog",
          author: "Your Name",
          twitterHandle: "@handle",
        },
        hooks: {
          beforeLoadPosts: async (filter, context) => {
            console.log(`Loading ${filter.published ? 'published' : 'drafts'}`)
            // Throw to cancel loading: throw new Error("Not authorised")
          }
        }
      })
    }
  })
}
```

***

## In-Project Plugin Example

Whether you're building a plugin inside your project or as a standalone npm package, the code and patterns are identical. The only difference is packaging—standalone plugins are built and published to npm, while in-project plugins are imported directly.

Here's a complete example based on the [Todo Plugin](https://github.com/better-stack-ai/better-stack/tree/main/examples/nextjs/lib/plugins/todo):

**File: `lib/plugins/todo/schema.ts`**

```typescript
import { createDbPlugin } from "@btst/stack/plugins/api"

export const todosSchema = createDbPlugin("todos", {
  todo: {
    modelName: "todo",
    fields: {
      title: { type: "string", required: true },
      completed: { type: "boolean", defaultValue: false },
      createdAt: { type: "date", defaultValue: () => new Date() }
    }
  }
})
```

**File: `lib/plugins/todo/types.ts`**

```typescript
export type Todo = {
  id: string
  title: string
  completed: boolean
  createdAt: Date
}
```

**File: `lib/plugins/todo/api/getters.ts`**

```typescript
import type { Adapter } from "@btst/stack/plugins/api"
import type { Todo } from "../types"

/** Retrieve all todos, sorted newest-first. Safe for server-side and SSG use. */
export async function listTodos(adapter: Adapter): Promise<Todo[]> {
  return adapter.findMany<Todo>({
    model: "todo",
    sortBy: { field: "createdAt", direction: "desc" },
  }) as Promise<Todo[]>
}

/** Retrieve a single todo by ID. Returns null if not found. */
export async function getTodoById(
  adapter: Adapter,
  id: string,
): Promise<Todo | null> {
  return adapter.findOne<Todo>({
    model: "todo",
    where: [{ field: "id", value: id, operator: "eq" }],
  })
}
```

**File: `lib/plugins/todo/api/backend.ts`**

```typescript
import { type Adapter, defineBackendPlugin, createEndpoint } from "@btst/stack/plugins/api"
import { z } from "zod"
import { todosSchema as dbSchema } from "../schema"
import type { Todo } from "../types"
import { listTodos, getTodoById } from "./getters"

const createTodoSchema = z.object({
  title: z.string().min(1),
  completed: z.boolean().optional().default(false)
})

const updateTodoSchema = z.object({
  title: z.string().min(1).optional(),
  completed: z.boolean().optional()
})

export const todosBackendPlugin = defineBackendPlugin({
  name: "todos",
  dbPlugin: dbSchema,

  // Server-side getters — available as myStack.api.todos.*
  api: (adapter) => ({
    listTodos: () => listTodos(adapter),
    getTodoById: (id: string) => getTodoById(adapter, id),
  }),

  routes: (adapter: Adapter) => {
    const listTodos = createEndpoint("/todos", { method: "GET" },
      async () => adapter.findMany<Todo>({ model: "todo" }) || []
    )
    
    const createTodo = createEndpoint("/todos", { method: "POST", body: createTodoSchema },
      async (ctx) => adapter.create<Todo>({
        model: "todo",
        data: { ...ctx.body, createdAt: new Date() }
      })
    )

    const updateTodo = createEndpoint("/todos/:id", { method: "PUT", body: updateTodoSchema },
      async (ctx) => {
        const updated = await adapter.update({
          model: "todo",
          where: [{ field: "id", value: ctx.params.id }],
          update: ctx.body
        })
        if (!updated) throw new Error("Todo not found")
        return updated
      }
    )

    const deleteTodo = createEndpoint("/todos/:id", { method: "DELETE" },
      async (ctx) => {
        await adapter.delete({ model: "todo", where: [{ field: "id", value: ctx.params.id }] })
        return { success: true }
      }
    )
    
    return { listTodos, createTodo, updateTodo, deleteTodo } as const
  }
})

export type TodosApiRouter = ReturnType<typeof todosBackendPlugin.routes>
```

**File: `lib/plugins/todo/client/client.tsx`**

```typescript
import { createApiClient, defineClientPlugin, createRoute } from "@btst/stack/plugins/client"
import type { QueryClient } from "@tanstack/react-query"
import type { TodosApiRouter } from "../api/backend"
import { lazy } from "react"
import type { Todo } from "../types"

export interface TodosClientConfig {
  queryClient: QueryClient
  apiBaseURL: string
  apiBasePath: string
  siteBaseURL: string
  siteBasePath: string
  context?: Record<string, unknown>
}

// SSR loader - prefetch data on the server
function todosLoader(config: TodosClientConfig) {
  return async () => {
    if (typeof window === "undefined") {
      const { queryClient, apiBasePath, apiBaseURL } = config
      
      await queryClient.prefetchQuery({
        queryKey: ["todos"],
        queryFn: async () => {
          const client = createApiClient<TodosApiRouter>({
            baseURL: apiBaseURL,
            basePath: apiBasePath,
          })
          const response = await client("/todos", { method: "GET" })
          return response.data
        },
      })
    }
  }
}

// Meta generator - create SEO tags from loaded data
function createTodosMeta(config: TodosClientConfig, path: string) {
  return () => {
    const { queryClient, siteBaseURL, siteBasePath } = config
    const todos = queryClient.getQueryData<Todo[]>(["todos"]) ?? []
    const fullUrl = `${siteBaseURL}${siteBasePath}${path}`
    
    return [
      { name: "title", content: `${todos.length} Todos` },
      { name: "description", content: `Track ${todos.length} todos.` },
      { property: "og:title", content: `${todos.length} Todos` },
      { property: "og:url", content: fullUrl },
      { name: "twitter:card", content: "summary" },
    ]
  }
}

export const todosClientPlugin = (config: TodosClientConfig) =>
  defineClientPlugin({
    name: "todos",

    routes: () => ({
      todos: createRoute("/todos", () => {
        const TodosListPage = lazy(() =>
          import("./components").then((m) => ({ default: m.TodosListPage }))
        )
        
        return {
          PageComponent: TodosListPage,
          loader: todosLoader(config),
          meta: createTodosMeta(config, "/todos"),
        }
      }),
      addTodo: createRoute("/todos/add", () => {
        const AddTodoPage = lazy(() =>
          import("./components").then((m) => ({ default: m.AddTodoPage }))
        )
        
        return {
          PageComponent: AddTodoPage,
          meta: createTodosMeta(config, "/todos/add"),
        }
      }),
    }),
    
    sitemap: async () => [
      { url: `${config.siteBaseURL}${config.siteBasePath}/todos`, lastModified: new Date(), priority: 0.7 },
      { url: `${config.siteBaseURL}${config.siteBasePath}/todos/add`, lastModified: new Date(), priority: 0.6 },
    ],
  })
```

**File: `lib/plugins/todo/client/hooks.tsx`**

```typescript
"use client"
import { createApiClient } from "@btst/stack/plugins/client"
import { useSuspenseQuery, useMutation, useQueryClient } from "@tanstack/react-query"
import type { TodosApiRouter } from "../api/backend"

export function useTodos() {
  const client = createApiClient<TodosApiRouter>({ baseURL: "/api/data" })
  return useSuspenseQuery({
    queryKey: ["todos"],
    queryFn: async () => (await client("/todos", { method: "GET" })).data
  })
}

export function useCreateTodo() {
  const client = createApiClient<TodosApiRouter>({ baseURL: "/api/data" })
  const queryClient = useQueryClient()
  return useMutation({
    mutationFn: async (title: string) => 
      (await client("@post/todos", { method: "POST", body: { title } })).data,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ["todos"] })
  })
}
```

***

## AI Chat Plugin Integration

Plugins can participate in the **route-aware AI context** system. When a user opens the chat widget while viewing one of your plugin's pages, it can automatically:

* Inject a description of the current page into the AI's system prompt
* Expose action chips (quick suggestions) relevant to the page
* Provide **client-side tool handlers** the AI can call to mutate page state (fill forms, update editors, etc.)

### Step 1 — Register context from the page component

Call `useRegisterPageAIContext` inside your `.internal.tsx` page component. The registration is automatically cleaned up on unmount.

```tsx
import { useRegisterPageAIContext } from "@btst/stack/plugins/ai-chat/client/context"
import { useRef, useCallback } from "react"
import type { UseFormReturn } from "react-hook-form"

export function MyPluginEditPage() {
  // Capture the form instance via an onFormReady callback from your form component
  const formRef = useRef<UseFormReturn<any> | null>(null)
  const handleFormReady = useCallback((form: UseFormReturn<any>) => {
    formRef.current = form
  }, [])

  useRegisterPageAIContext({
    // Short identifier shown as a badge in the chat widget header
    routeName: "my-plugin-edit",

    // Injected into the AI system prompt (capped at 8,000 characters)
    pageDescription: "User is editing a My Plugin item. When asked to fill in the form, call the fillMyPluginForm tool.",

    // Quick-action chips shown in the chat empty state (merged with static suggestions)
    suggestions: ["Fill in the form for me", "Suggest a title"],

    // Handlers the AI can invoke — keyed by tool name
    clientTools: {
      fillMyPluginForm: async ({ title, description }) => {
        const form = formRef.current
        if (!form) return { success: false, message: "Form not ready" }
        if (title !== undefined) form.setValue("title", title, { shouldValidate: true })
        if (description !== undefined) form.setValue("description", description)
        return { success: true, message: "Form filled" }
      },
    },
  })

  return <MyPluginForm onFormReady={handleFormReady} />
}
```

Pass `null` to conditionally disable the context while data is loading:

```tsx
useRegisterPageAIContext(item ? {
  routeName: "my-plugin-detail",
  pageDescription: `Viewing: "${item.title}"\n\n${item.content?.slice(0, 16000)}`,
  suggestions: ["Summarize this", "What are the key points?"],
} : null)
```

### Step 2 — Register the tool schema server-side

Client-side tool handlers need a matching server-side schema so the LLM knows what parameters to send.

**For first-party BTST plugins**, add the schema to `BUILT_IN_PAGE_TOOL_SCHEMAS` in `src/plugins/ai-chat/api/page-tools.ts`:

```ts
// packages/stack/src/plugins/ai-chat/api/page-tools.ts
import { tool } from "ai"
import { z } from "zod"

export const BUILT_IN_PAGE_TOOL_SCHEMAS: Record<string, Tool> = {
  // ...existing built-in tools (fillBlogForm, updatePageLayers)

  fillMyPluginForm: tool({
    description: "Fill in the my-plugin form fields. Call this when the user asks to populate or draft the form.",
    inputSchema: z.object({
      title: z.string().optional().describe("The item title"),
      description: z.string().optional().describe("A short description"),
    }),
    // No execute — this is handled entirely client-side via onToolCall in ChatInterface
  }),
}
```

**For consumer (third-party) plugins**, instruct users to pass `clientToolSchemas` in `aiChatBackendPlugin`:

```ts
// Consumer's lib/stack.ts
aiChatBackendPlugin({
  model: openai("gpt-4o"),
  enablePageTools: true,
  clientToolSchemas: {
    fillMyPluginForm: tool({
      description: "Fill in the my-plugin form fields",
      parameters: z.object({ title: z.string().optional() }),
    }),
  },
})
```

### Step 3 — Ensure PageAIContextProvider is in the root layout

The `PageAIContextProvider` must be present **above all `StackProvider` instances** in every example app's root layout. It is already wired up in the BTST example apps — you only need to ensure your plugin's pages call `useRegisterPageAIContext` correctly.

<Callout type="info">
  `useRegisterPageAIContext` silently no-ops when `PageAIContextProvider` is absent from the tree. If context doesn't appear in the chat widget, check that the provider wraps the root layout.
</Callout>

### Read-only context (no tools)

If your page only displays content the AI should be able to read but not mutate, omit `clientTools`:

```tsx
// Blog post detail page — AI can summarize but not write
useRegisterPageAIContext(post ? {
  routeName: "blog-post",
  pageDescription: `Blog post: "${post.title}"\n\n${post.content?.slice(0, 16000)}`,
  suggestions: ["Summarize this post", "What are the key takeaways?"],
} : null)
```

### Reference implementations inside BTST

| Plugin             | File                                                                | Tools exposed      |
| ------------------ | ------------------------------------------------------------------- | ------------------ |
| Blog (new post)    | `blog/client/components/pages/new-post-page.internal.tsx`           | `fillBlogForm`     |
| Blog (edit post)   | `blog/client/components/pages/edit-post-page.internal.tsx`          | `fillBlogForm`     |
| Blog (post detail) | `blog/client/components/pages/post-page.internal.tsx`               | none (read-only)   |
| UI Builder         | `ui-builder/client/components/pages/page-builder-page.internal.tsx` | `updatePageLayers` |

***

## Reference Implementations

### Simple Plugin: Todo

A basic CRUD plugin demonstrating core concepts:

**Source Code:** [Todo Plugin](https://github.com/better-stack-ai/better-stack/tree/main/examples/nextjs/lib/plugins/todo)

Features:

* Basic CRUD operations
* Database schema
* API endpoints (list, create, update, delete)
* Server-side getter functions (`getters.ts`)
* `stack().api.todos.*` surface for direct server-side access
* Client components and hooks

### Full-Featured Plugin: Blog

A production-ready plugin with advanced features:

**Source Code:** [Blog Plugin](https://github.com/better-stack-ai/better-stack/tree/main/packages/stack/src/plugins/blog)

Features:

* Multiple related models (posts, tags, postTags)
* Complex queries with pagination, filtering, search
* SSR data loading with React Query
* **SSG support** via `prefetchForRoute` — seeds the query cache at build time without HTTP
* `api/query-key-defs.ts` — shared key constants used by both `query-keys.ts` and `prefetchForRoute`
* `api/serializers.ts` — `Date` → ISO string conversion for consistent cache hydration
* SEO meta generation
* Sitemap generation
* Authorization and lifecycle hooks
* Optimistic updates
* Rich text editing

***

## Publishing Plugins

To create a standalone plugin package for npm, use the **Plugin Starter** repository:

**🚀 [Plugin Starter Repository](https://github.com/better-stack-ai/plugin-starter)**

The starter provides:

* Complete monorepo setup with build tooling
* Example plugin you can modify
* Next.js example app for testing
* E2E testing with Playwright
* GitHub Actions for automated publishing

Clone it, modify the plugin package, and publish to npm under your own account.


# Form Builder Plugin (/plugins/form-builder)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import formBuilderDemo from "../../../assets/form-builder-demo.png";
import formBuilderDemo1 from "../../../assets/form-builder-demo-1.png";
import formBuilderDemo2 from "../../../assets/form-builder-demo-2.png";
import formBuilderDemo3 from "../../../assets/form-builder-demo-3.png";

<div className="grid grid-cols-1 lg:grid-cols-2 gap-2 my-2">
  <a href={formBuilderDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={formBuilderDemo} alt="Form Builder Plugin Demo - Forms List" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={formBuilderDemo1.src} target="_blank" rel="noopener noreferrer">
    <Image src={formBuilderDemo1} alt="Form Builder Plugin Demo - Builder" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={formBuilderDemo2.src} target="_blank" rel="noopener noreferrer">
    <Image src={formBuilderDemo2} alt="Form Builder Plugin Demo - Preview" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>

  <a href={formBuilderDemo3.src} target="_blank" rel="noopener noreferrer">
    <Image src={formBuilderDemo3} alt="Form Builder Plugin Demo - Submissions" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

The Form Builder plugin provides a visual drag-and-drop form creation interface where administrators can create forms that are serialized and stored as JSON Schema. This is distinct from the CMS plugin - while CMS uses developer-defined Zod schemas, Form Builder allows non-technical administrators to create forms dynamically.

**Key Features:**

* **Visual Form Builder** - Drag-and-drop interface for creating forms with various field types
* **JSON Schema Storage** - Forms are serialized to JSON Schema for database persistence
* **Public Form Rendering** - Render forms by slug on the frontend with automatic validation
* **Submission Tracking** - Store and view form submissions with IP address and user agent logging
* **Backend Hooks** - Lifecycle hooks for authentication, rate limiting, and integrations

[View interactive demo →](/demos/form-builder)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

### 1. Add Plugin to Backend API

Register the Form Builder backend plugin:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { formBuilderBackendPlugin } from "@btst/stack/plugins/form-builder/api"

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    formBuilder: formBuilderBackendPlugin({
      hooks: {
        // Authentication - check if user can access admin pages
        onBeforeListForms: async (ctx) => {
          const session = await getSession(ctx.headers)
          if (session?.user?.isAdmin !== true)
            throw new Error("Admin access required")
        },
        onBeforeFormCreated: async (data, ctx) => {
          const session = await getSession(ctx.headers)
          if (!session?.user?.isAdmin)
            throw new Error("Admin access required")
          return data
        },
        // Rate limiting for public submissions
        onBeforeSubmission: async (formSlug, data, ctx) => {
          // Check rate limit by IP
          const isAllowed = await checkRateLimit(ctx.ipAddress, formSlug)
          if (!isAllowed) throw new Error("Rate limit exceeded")
          return data
        },
        // Post-submission actions
        onAfterSubmission: async (submission, form, ctx) => {
          // Send notification email
          await sendEmail({
            to: "admin@example.com",
            subject: `New submission: ${form.name}`,
            body: JSON.stringify(JSON.parse(submission.data), null, 2),
          })
          // CRM integration
          await updateCRM(submission.data)
        },
      },
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

export { handler, dbSchema }
```

### 2. Add Plugin to Client

Register the Form Builder client plugin:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { formBuilderClientPlugin } from "@btst/stack/plugins/form-builder/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () => 
  process.env.BASE_URL || "http://localhost:3000"

export const getStackClient = (queryClient: QueryClient, options?: { headers?: Headers }) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      "form-builder": formBuilderClientPlugin({
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient: queryClient,
        headers: options?.headers,
        hooks: {
          beforeLoadFormList: async (context) => {
            const session = await getSession(context.headers)
            return session?.user?.isAdmin === true
          },
          beforeLoadFormBuilder: async (formId, context) => {
            const session = await getSession(context.headers)
            return session?.user?.isAdmin === true
          },
          beforeLoadSubmissions: async (formId, context) => {
            const session = await getSession(context.headers)
            return session?.user?.isAdmin === true
          },
          onLoadError: (error, context) => {
            redirect("/auth/sign-in")
          },
        },
      })
    }
  })
}
```

### 3. Configure Provider Overrides

Add Form Builder overrides to your layout:

```tsx title="app/pages/layout.tsx"
import type { FormBuilderPluginOverrides } from "@btst/stack/plugins/form-builder/client"

type PluginOverrides = {
  "form-builder": FormBuilderPluginOverrides,
}

<StackProvider<PluginOverrides>
  basePath="/pages"
  overrides={{
    "form-builder": {
      apiBaseURL: baseURL,
      apiBasePath: "/api/data",
      navigate: (path) => router.push(path),
      refresh: () => router.refresh(),
      Link: ({ href, ...props }) => <Link href={href || "#"} {...props} />,
      // Optional file upload for file fields
      uploadFile: async (file) => {
        // Your file upload logic
        return "https://example.com/file.pdf"
      },
      // Lifecycle hooks
      onRouteRender: async (routeName, context) => {
        console.log(`Form Builder route:`, routeName)
      },
      onRouteError: async (routeName, error, context) => {
        console.error(`Form Builder error:`, routeName, error.message)
      },
    }
  }}
>
  {children}
</StackProvider>
```

### 4. Import CSS

Add the Form Builder styles to your global CSS:

```css title="app/globals.css"
@import "@btst/stack/plugins/form-builder/css";
```

## Admin Routes

The Form Builder plugin provides these admin routes:

| Route                    | Description                                      |
| ------------------------ | ------------------------------------------------ |
| `/forms`                 | List all forms with create, edit, delete actions |
| `/forms/new`             | Create a new form with the visual form builder   |
| `/forms/:id/edit`        | Edit an existing form                            |
| `/forms/:id/submissions` | View submissions for a form                      |

<Callout type="warn">
  Admin routes are automatically set to `noindex` for SEO. Don't include them in your public sitemap.
</Callout>

### Page Component Overrides

You can replace any built-in admin page with your own React component using the optional `pageComponents` field in `formBuilderClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
formBuilderClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the form list page
    formList: MyCustomFormList,
    // Replace the new form page
    newForm: MyCustomNewForm,
    // Replace the form editor page — receives id as a prop
    editForm: ({ id }) => <MyCustomFormEditor id={id} />,
    // Replace the form submissions page — receives formId as a prop
    submissions: ({ formId }) => <MyCustomSubmissions formId={formId} />,
  },
})
```

## Form Builder UI

The form builder provides a drag-and-drop interface with:

* **Component Palette** - Available field types to drag onto the canvas
* **Canvas** - Where you build your form by arranging fields
* **Preview Tab** - Live preview of how the form will look
* **JSON Schema Tab** - View the generated JSON Schema

### Available Field Types

| Field Type  | Description                 | JSON Schema Properties                            |
| ----------- | --------------------------- | ------------------------------------------------- |
| Text Input  | Single-line text field      | `type: "string"`                                  |
| Email       | Email input with validation | `type: "string", format: "email"`                 |
| Password    | Password input              | `type: "string", fieldType: "password"`           |
| Number      | Numeric input               | `type: "number"` with `minimum`/`maximum`         |
| Text Area   | Multi-line text field       | `type: "string", fieldType: "textarea"`           |
| Select      | Dropdown selection          | `type: "string", enum: [...]`                     |
| Checkbox    | Boolean checkbox            | `type: "boolean"`                                 |
| Switch      | Toggle switch               | `type: "boolean", fieldType: "switch"`            |
| Radio Group | Radio button group          | `type: "string", enum: [...], fieldType: "radio"` |
| Date Picker | Date selection              | `type: "string", format: "date-time"`             |
| Phone       | Phone number input          | `type: "string", fieldType: "phone"`              |
| URL         | Website URL input           | `type: "string", format: "uri"`                   |

### Field Properties

Each field can be configured with:

| Property      | Description                                              |
| ------------- | -------------------------------------------------------- |
| Label         | Display label for the field                              |
| Field Name    | The property key in the JSON Schema                      |
| Description   | Help text shown below the field                          |
| Placeholder   | Placeholder text in the input                            |
| Required      | Whether the field is required                            |
| Min/Max       | Minimum and maximum values (numbers) or length (strings) |
| Options       | For select, radio, and checkbox groups                   |
| Default Value | Pre-filled value for the field                           |

## Public Form Rendering

The `FormRenderer` component allows you to render forms on public pages by their slug:

```tsx title="app/form-demo/[slug]/page.tsx"
"use client"

import { FormRenderer } from "@btst/stack/plugins/form-builder/client/components"

export default function FormDemoPage({ params }: { params: { slug: string } }) {
  return (
    <div className="max-w-2xl mx-auto p-6">
      <FormRenderer
        slug={params.slug}
        onSuccess={(submission) => {
          console.log("Form submitted:", submission)
          // submission.form contains successMessage and redirectUrl
        }}
        onError={(error) => {
          console.error("Submission error:", error)
        }}
        // Optional: Custom loading/error states
        LoadingComponent={() => <div>Loading form...</div>}
        ErrorComponent={({ error }) => (
          <div>Form not found: {error.message}</div>
        )}
        // Optional: Custom submit button text
        submitButtonText="Send Message"
        // Optional: Custom success message (overrides form's successMessage)
        successMessage="Thanks for your submission!"
        className="space-y-6"
      />
    </div>
  )
}
```

### FormRenderer Props

| Prop               | Type                              | Description                                                             |
| ------------------ | --------------------------------- | ----------------------------------------------------------------------- |
| `slug`             | `string`                          | Form slug to fetch and render                                           |
| `onSuccess`        | `(submission) => void`            | Callback after successful submission (submission.form has success info) |
| `onError`          | `(error) => void`                 | Callback when submission fails                                          |
| `LoadingComponent` | `ComponentType`                   | Custom loading state                                                    |
| `ErrorComponent`   | `ComponentType<{ error: Error }>` | Custom error state                                                      |
| `submitButtonText` | `string`                          | Custom submit button text                                               |
| `successMessage`   | `string`                          | Override the form's success message                                     |
| `fieldComponents`  | `Record<string, ComponentType>`   | Custom field components                                                 |
| `className`        | `string`                          | Additional CSS classes                                                  |

<Callout type="info">
  The `FormRenderer` uses `SteppedAutoForm` internally, which automatically handles both single-step and multi-step forms based on the JSON Schema structure.
</Callout>

## Client Hooks

Access form data in your frontend using the provided hooks:

### Available Hooks

| Hook                          | Description                  | Returns                                       |
| ----------------------------- | ---------------------------- | --------------------------------------------- |
| `useFormsAdmin()`             | List all forms (admin)       | `{ forms, total, isLoading, error, refetch }` |
| `useFormBySlug(slug)`         | Get form by slug (public)    | `{ form, isLoading, error }`                  |
| `useSuspenseFormById(id)`     | Get form by ID with Suspense | `{ form, refetch }`                           |
| `useCreateForm()`             | Create mutation              | React Query mutation                          |
| `useUpdateForm()`             | Update mutation              | React Query mutation                          |
| `useDeleteForm()`             | Delete mutation              | React Query mutation                          |
| `useSubmitForm(slug)`         | Submit form data             | React Query mutation                          |
| `useSubmissions(formId)`      | List submissions for a form  | `{ submissions, total, isLoading }`           |
| `useDeleteSubmission(formId)` | Delete submission            | React Query mutation                          |

### Usage Examples

```tsx
import { 
  useFormBySlug,
  useSubmitForm,
  useFormsAdmin 
} from "@btst/stack/plugins/form-builder/client/hooks"

// Public: Fetch form by slug
function ContactPage() {
  const { form, isLoading } = useFormBySlug("contact-form")
  const submitForm = useSubmitForm("contact-form")

  if (isLoading || !form) return <Loading />

  return (
    <AutoForm
      schema={JSON.parse(form.schema)}
      onSubmit={async (data) => {
        await submitForm.mutateAsync({ data })
      }}
    />
  )
}

// Admin: List all forms
function FormsAdmin() {
  const { forms, total, isLoading } = useFormsAdmin()
  
  return (
    <ul>
      {forms.map(form => (
        <li key={form.id}>{form.name} - {form.status}</li>
      ))}
    </ul>
  )
}
```

## Backend Hooks

Customize Form Builder behavior with backend lifecycle hooks:

### FormBuilderBackendHooks

```ts
formBuilderBackendPlugin({
  hooks: {
    // Form CRUD authorization
    onBeforeListForms: async (ctx) => {
      // Throw to deny, return void to allow
      if (!await isAdmin(ctx.headers))
        throw new Error("Admin access required")
    },
    onBeforeFormCreated: async (data, ctx) => {
      // Return modified data to allow, throw to deny
      return data
    },
    onBeforeFormUpdated: async (formId, data, ctx) => {
      // Return modified data to allow, throw to deny
      return data
    },
    onBeforeFormDeleted: async (formId, ctx) => {
      // Throw to deny: throw new Error("Cannot delete this form")
    },
    
    // Form lifecycle
    onAfterFormCreated: async (form, ctx) => {
      console.log("Form created:", form.name)
    },
    onAfterFormUpdated: async (form, ctx) => {
      console.log("Form updated:", form.name)
    },
    onAfterFormDeleted: async (formId, ctx) => {
      console.log("Form deleted:", formId)
    },
    
    // Submission authorization and processing
    onBeforeSubmission: async (formSlug, data, ctx) => {
      // Access IP and user agent for rate limiting
      console.log("Submission from:", ctx.ipAddress, ctx.userAgent)
      
      // Rate limiting example
      const allowed = await checkRateLimit(ctx.ipAddress, formSlug)
      if (!allowed) throw new Error("Rate limit exceeded")
      
      // Spam filtering
      if (containsSpam(data)) throw new Error("Submission rejected")
      
      return data
    },
    onAfterSubmission: async (submission, form, ctx) => {
      // Send email notifications
      await sendEmail({
        to: "admin@example.com",
        subject: `New ${form.name} submission`,
        body: formatSubmission(submission.data),
      })
      
      // CRM integration
      await pushToCRM(submission, form)
      
      // Webhook
      await triggerWebhook(form.webhookUrl, submission)
    },
    
    // Submissions list authorization
    onBeforeListSubmissions: async (formId, ctx) => {
      return isAdmin(ctx.headers)
    },
    onBeforeDeleteSubmission: async (submissionId, ctx) => {
      return isAdmin(ctx.headers)
    },
    
    // Error handling
    onFormError: async (error, operation, ctx) => {
      console.error(`Form ${operation} error:`, error.message)
    },
    onSubmissionError: async (error, formSlug, ctx) => {
      console.error(`Submission to ${formSlug} error:`, error.message)
    },
  },
})
```

### Hook Context

All hooks receive a context object with:

| Property    | Type                  | Description                        |
| ----------- | --------------------- | ---------------------------------- |
| `headers`   | `Headers`             | Request headers for auth           |
| `userId`    | `string \| undefined` | Authenticated user ID if available |
| `ipAddress` | `string \| undefined` | Client IP address                  |
| `userAgent` | `string \| undefined` | Client user agent                  |

## Client Hooks (SSR Authorization)

Use `hooks` in the client plugin config for **async authorization** during SSR:

```tsx title="lib/stack-client.tsx"
import { redirect } from "next/navigation"

"form-builder": formBuilderClientPlugin({
  // ... config
  hooks: {
    beforeLoadFormList: async (context) => {
      const session = await getSession(context.headers)
      if (session?.user?.isAdmin !== true)
        throw new Error("Admin access required")
    },
    beforeLoadFormBuilder: async (formId, context) => {
      // formId is undefined for new forms
      const session = await getSession(context.headers)
      if (session?.user?.isAdmin !== true)
        throw new Error("Admin access required")
    },
    beforeLoadSubmissions: async (formId, context) => {
      const session = await getSession(context.headers)
      if (session?.user?.isAdmin !== true)
        throw new Error("Admin access required")
    },
    afterLoadFormList: async (forms, context) => {
      console.log("Loaded", forms?.length, "forms")
    },
    onLoadError: (error, context) => {
      // Redirect on authorization failure
      redirect("/auth/sign-in")
    },
  },
})
```

<Callout type="info">
  **Use client hooks for SSR.** These hooks run during server-side data loading and support async operations like session checks. The `onLoadError` hook is called when any `beforeLoad*` hook returns `false`, allowing you to redirect unauthorized users.
</Callout>

## API Endpoints

The Form Builder plugin exposes these REST endpoints:

| Endpoint                              | Method | Description                                         |
| ------------------------------------- | ------ | --------------------------------------------------- |
| `/form-builder/forms`                 | GET    | List all forms (query: `limit`, `offset`, `status`) |
| `/form-builder/forms`                 | POST   | Create a new form                                   |
| `/form-builder/forms/:slug`           | GET    | Get form by slug                                    |
| `/form-builder/forms/:id`             | PUT    | Update a form                                       |
| `/form-builder/forms/:id`             | DELETE | Delete a form                                       |
| `/form-builder/forms/:slug/submit`    | POST   | Submit form data                                    |
| `/form-builder/forms/:id/submissions` | GET    | List submissions for a form                         |
| `/form-builder/submissions/:id`       | DELETE | Delete a submission                                 |

## Form Schema Structure

Forms are stored with this schema:

```ts
interface Form {
  id: string
  name: string          // Display name
  slug: string          // URL-friendly identifier
  schema: string        // JSON Schema as string
  successMessage?: string  // Message shown after submission
  redirectUrl?: string     // URL to redirect after submission
  status: "draft" | "published"
  createdAt: Date
  updatedAt: Date
}

interface FormSubmission {
  id: string
  formId: string        // Reference to form
  data: string          // Submitted data as JSON string
  ipAddress?: string    // Client IP
  userAgent?: string    // Client user agent
  createdAt: Date
}
```

## Multi-Step Forms

The Form Builder supports multi-step forms through JSON Schema's `allOf` structure:

```json
{
  "type": "object",
  "allOf": [
    {
      "title": "Step 1: Personal Info",
      "properties": {
        "name": { "type": "string", "label": "Full Name" },
        "email": { "type": "string", "format": "email" }
      }
    },
    {
      "title": "Step 2: Details",
      "properties": {
        "company": { "type": "string" },
        "message": { "type": "string", "fieldType": "textarea" }
      }
    }
  ]
}
```

The `SteppedAutoForm` component automatically renders this as a multi-step wizard with navigation.

## Custom Field Components

Provide custom field components via the `fieldComponents` prop on `FormRenderer`:

```tsx
import type { AutoFormInputComponentProps } from "@btst/stack/plugins/form-builder/client"

function CustomRating({ field, label }: AutoFormInputComponentProps) {
  return (
    <div>
      <label>{label}</label>
      <StarRating 
        value={field.value} 
        onChange={field.onChange} 
      />
    </div>
  )
}

<FormRenderer
  slug="feedback"
  fieldComponents={{
    rating: CustomRating,
    richText: MyRichTextEditor,
  }}
/>
```

## API Reference

### Backend (`@btst/stack/plugins/form-builder/api`)

#### formBuilderBackendPlugin

Creates the backend plugin with optional hooks configuration.

#### FormBuilderBackendHooks

| Hook                       | Parameters              | Return          | Description                      |
| -------------------------- | ----------------------- | --------------- | -------------------------------- |
| `onBeforeListForms`        | `ctx`                   | `boolean`       | Authorization for listing forms  |
| `onBeforeFormCreated`      | `data, ctx`             | `data \| false` | Validate/transform before create |
| `onAfterFormCreated`       | `form, ctx`             | `void`          | Post-create lifecycle            |
| `onBeforeFormUpdated`      | `id, data, ctx`         | `data \| false` | Validate/transform before update |
| `onAfterFormUpdated`       | `form, ctx`             | `void`          | Post-update lifecycle            |
| `onBeforeFormDeleted`      | `id, ctx`               | `boolean`       | Authorization for delete         |
| `onAfterFormDeleted`       | `id, ctx`               | `void`          | Post-delete lifecycle            |
| `onBeforeSubmission`       | `slug, data, ctx`       | `data \| false` | Validate/rate limit submissions  |
| `onAfterSubmission`        | `submission, form, ctx` | `void`          | Post-submission actions          |
| `onBeforeListSubmissions`  | `formId, ctx`           | `boolean`       | Authorization for listing        |
| `onBeforeDeleteSubmission` | `id, ctx`               | `boolean`       | Authorization for delete         |
| `onFormError`              | `error, operation, ctx` | `void`          | Handle form operation errors     |
| `onSubmissionError`        | `error, slug, ctx`      | `void`          | Handle submission errors         |

### Client (`@btst/stack/plugins/form-builder/client`)

#### formBuilderClientPlugin

Creates the client plugin with routes and SSR loaders.

#### FormBuilderPluginOverrides

| Property          | Type                              | Required | Description               |
| ----------------- | --------------------------------- | -------- | ------------------------- |
| `apiBaseURL`      | `string`                          | Yes      | Base URL for API requests |
| `apiBasePath`     | `string`                          | Yes      | API path prefix           |
| `navigate`        | `(path: string) => void`          | Yes      | Navigation function       |
| `Link`            | `ComponentType`                   | No       | Link component            |
| `refresh`         | `() => void`                      | No       | Refresh function          |
| `uploadFile`      | `(file: File) => Promise<string>` | No       | File upload handler       |
| `fieldComponents` | `Record<string, ComponentType>`   | No       | Custom field components   |
| `localization`    | `FormBuilderLocalization`         | No       | Custom labels             |
| `showAttribution` | `boolean`                         | No       | Show BTST attribution     |
| `onRouteRender`   | `(route, context) => void`        | No       | Lifecycle hook            |
| `onRouteError`    | `(route, error, context) => void` | No       | Error hook                |

#### FormBuilderClientHooks

| Hook                    | Parameters             | Return                  | Description                              |
| ----------------------- | ---------------------- | ----------------------- | ---------------------------------------- |
| `beforeLoadFormList`    | `context`              | `void \| Promise<void>` | SSR auth for forms list — throw to deny  |
| `afterLoadFormList`     | `forms, context`       | `void`                  | Post-load hook                           |
| `beforeLoadFormBuilder` | `formId, context`      | `void \| Promise<void>` | SSR auth for builder — throw to deny     |
| `afterLoadFormBuilder`  | `form, context`        | `void`                  | Post-load hook                           |
| `beforeLoadSubmissions` | `formId, context`      | `void \| Promise<void>` | SSR auth for submissions — throw to deny |
| `afterLoadSubmissions`  | `submissions, context` | `void`                  | Post-load hook                           |
| `onLoadError`           | `error, context`       | `void`                  | Handle auth failures                     |

### Schema Converter Utilities (`@btst/stack/plugins/form-builder/client`)

The Form Builder plugin re-exports schema converter utilities for converting between Zod schemas and JSON Schema. These are useful when working with form schemas programmatically:

#### zodToFormSchema

Convert a Zod schema to JSON Schema with proper handling for dates, steps metadata, and date constraints:

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="zodToFormSchema" />

**Example:**

```ts
import { zodToFormSchema } from "@btst/stack/plugins/form-builder/client"

const jsonSchema = zodToFormSchema(ContactFormSchema, {
  steps: [
    { id: "personal", title: "Personal Information" },
    { id: "message", title: "Your Message" }
  ],
  stepGroupMap: {
    name: 0,
    email: 0,
    message: 1
  }
})
```

#### formSchemaToZod

Convert JSON Schema back to a Zod schema with proper handling for date fields, constraints, and steps metadata. This is used internally by `FormRenderer` to validate form submissions:

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="formSchemaToZod" />

**Example:**

```ts
import { formSchemaToZod } from "@btst/stack/plugins/form-builder/client"

// Convert JSON Schema from database to Zod for validation
const zodSchema = formSchemaToZod(jsonSchema)
const result = zodSchema.safeParse(submissionData)
```

#### Utility Functions

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="hasSteps" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="getSteps" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="getStepGroupMap" />

#### Types

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="FormStep" />

<AutoTypeTable path="../packages/ui/src/lib/schema-converter.ts" name="FormSchemaMetadata" />

## Server-side Data Access

The Form Builder plugin exposes standalone getter functions for server-side use cases.

### Two patterns

**Pattern 1 — via `stack().api`**

```ts title="app/lib/stack.ts"
import { myStack } from "./stack";

const forms       = await myStack.api["form-builder"].getAllForms({ status: "active" });
const form        = await myStack.api["form-builder"].getFormBySlug("contact");
const submissions = await myStack.api["form-builder"].getFormSubmissions(form!.id);
```

**Pattern 2 — direct import**

```ts
import {
  getAllForms,
  getFormBySlug,
  getFormSubmissions,
} from "@btst/stack/plugins/form-builder/api";

const form = await getFormBySlug(myAdapter, "contact");
if (form) {
  const result = await getFormSubmissions(myAdapter, form.id, { limit: 50 });
  console.log(result.total, "submissions");
}
```

### Available getters

| Function                                       | Description                                         |
| ---------------------------------------------- | --------------------------------------------------- |
| `getAllForms(adapter, params?)`                | Returns paginated forms with optional status filter |
| `getFormBySlug(adapter, slug)`                 | Returns a single form by slug, or `null`            |
| `getFormSubmissions(adapter, formId, params?)` | Returns paginated submissions for a form            |

## Static Site Generation (SSG)

`route.loader()` makes HTTP requests to `apiBaseURL`, which silently fails during `next build` because no dev server is running. Use `prefetchForRoute()` instead — it reads directly from the database and pre-populates the React Query cache before rendering.

### `prefetchForRoute(routeKey, queryClient, params?)`

| Route key       | Params required      | Data prefetched                      |
| --------------- | -------------------- | ------------------------------------ |
| `"formList"`    | —                    | First page of forms                  |
| `"newForm"`     | —                    | *(nothing)*                          |
| `"editForm"`    | `{ id: string }`     | Single form by ID                    |
| `"submissions"` | `{ formId: string }` | First page of submissions for a form |

### Next.js example

```tsx title="app/pages/forms/page.tsx"
import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
import { getOrCreateQueryClient } from "@/lib/query-client"
import { getStackClient } from "@/lib/stack-client"
import { myStack } from "@/lib/stack"
import { metaElementsToObject, normalizePath } from "@btst/stack/client"
import type { Metadata } from "next"

export async function generateStaticParams() {
  return [{}]
}

// export const revalidate = 3600 // uncomment for ISR

export async function generateMetadata(): Promise<Metadata> {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["forms"]))
  if (!route) return { title: "Forms" }
  await myStack.api.formBuilder.prefetchForRoute("formList", queryClient)
  return metaElementsToObject(route.meta?.() ?? []) satisfies Metadata
}

export default async function FormsListPage() {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["forms"]))
  if (!route) return null
  // Reads directly from DB — works at build time, no HTTP server required
  await myStack.api.formBuilder.prefetchForRoute("formList", queryClient)
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

### ISR cache invalidation

If you use [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration), call `revalidatePath` inside the backend lifecycle hooks so Next.js regenerates the page on the next request:

```ts title="lib/stack.ts"
import { revalidatePath } from "next/cache"
import type { FormBuilderBackendHooks } from "@btst/stack/plugins/form-builder"

const formHooks: FormBuilderBackendHooks = {
  onAfterFormCreated: async (form) => {
    revalidatePath("/forms", "page")
  },
  onAfterFormUpdated: async (form) => {
    revalidatePath("/forms", "page")
  },
}
```

### Query key consistency

`prefetchForRoute` uses the same query key shapes as `createFormBuilderQueryKeys` (the HTTP client). The shared constants live in `@btst/stack/plugins/form-builder/api` as `FORM_QUERY_KEYS`, `formsListDiscriminator`, and `submissionsListDiscriminator`, so the two paths can never drift silently.

## Shadcn Registry

The Form Builder plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/form-builder/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-form-builder.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/form-builder/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { formBuilderClientPlugin } from "@btst/stack/plugins/form-builder/client"
// Import your ejected (and customized) page components
import { FormListPageComponent } from "@/components/btst/form-builder/client/components/pages/form-list-page"
import { EditFormPageComponent } from "@/components/btst/form-builder/client/components/pages/edit-form-page"

formBuilderClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    formList: FormListPageComponent,   // replaces the form list page
    editForm: EditFormPageComponent,   // replaces the form editor page
    // newForm, submissions — omit to keep built-in defaults
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.


# Plugins (/plugins)

import { Card, Cards } from "fumadocs-ui/components/card";
import { BookOpen, Database, Hammer, Bot, Shield, FileText, FileCode, Route, Layout, Columns3 } from "lucide-react";

BTST provides a collection of full-stack plugins that you can easily integrate into your React application. Each plugin includes routes, APIs, database schemas, components, and hooks—everything you need to add complete features to your app.

With more plugins coming soon, you can add complete features to your app in minutes.

<Cards>
  <Card title="Blog Plugin" href="/plugins/blog" icon={<BookOpen size={20} />} description="Content management, editor, drafts, publishing, SEO, RSS feeds." />

  <Card title="AI Chat Plugin" href="/plugins/ai-chat" icon={<Bot size={20} />} description="AI-powered chat with conversation history, streaming, and customizable models." />

  <Card title="CMS Plugin" href="/plugins/cms" icon={<Database size={20} />} description="Headless CMS with custom content types, Zod schemas, and auto-generated forms." />

  <Card title="Form Builder Plugin" href="/plugins/form-builder" icon={<FileText size={20} />} description="Dynamic form builder with drag-and-drop editor, submissions, and validation." />

  <Card title="UI Builder Plugin" href="/plugins/ui-builder" icon={<Layout size={20} />} description="Visual drag-and-drop page builder with component registry and public rendering." />

  <Card title="Kanban Plugin" href="/plugins/kanban" icon={<Columns3 size={20} />} description="Project management with boards, columns, tasks, drag-and-drop, and priority levels." />

  <Card title="OpenAPI Plugin" href="/plugins/open-api" icon={<FileCode size={20} />} description="Auto-generated API documentation with interactive Scalar UI." />

  <Card title="Route Docs Plugin" href="/plugins/route-docs" icon={<Route size={20} />} description="Auto-generated client route documentation with interactive navigation." />

  <Card title="Better Auth UI Plugin" href="/plugins/better-auth-ui" icon={<Shield size={20} />} description="Beautiful shadcn/ui authentication components for better-auth." />

  <Card title="Building Plugins" href="/plugins/development" icon={<Hammer size={20} />} description="Learn how to build your own plugins for BTST." />
</Cards>


# Kanban Plugin (/plugins/kanban)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import kanbanDemo from "../../../assets/kanban-demo.png";

<div className="grid grid-cols-1 gap-2 my-2">
  <a href={kanbanDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={kanbanDemo} alt="Kanban Plugin Demo - Board View" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

## Overview

The Kanban plugin provides a full-featured project management system with:

* **Boards** - Organize different projects or workflows
* **Columns** - Define workflow stages (e.g., To Do, In Progress, Done)
* **Tasks** - Track individual work items with priorities
* **Assignees** - Assign users to tasks with avatar display
* **Drag-and-Drop** - Reorder tasks and columns with smooth animations
* **Priority Levels** - LOW, MEDIUM, HIGH, URGENT with visual badges
* **Organization Support** - Optional scoping by user or organization

[View interactive demo →](/demos/kanban)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

Follow these steps to add the Kanban plugin to your BTST setup.

### 1. Add Plugin to Backend API

Import and register the kanban backend plugin in your `stack.ts` file:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { kanbanBackendPlugin } from "@btst/stack/plugins/kanban/api"
// ... your adapter imports

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    kanban: kanbanBackendPlugin()
  },
  adapter: (db) => createPrismaAdapter(prisma, db, { 
    provider: "postgresql" 
  })
})

export { handler, dbSchema }
```

The `kanbanBackendPlugin()` accepts optional hooks for customizing behavior (authorization, logging, etc.).

### 2. Add Plugin to Client

Register the kanban client plugin in your `stack-client.tsx` file:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { kanbanClientPlugin } from "@btst/stack/plugins/kanban/client"
import { QueryClient } from "@tanstack/react-query"

const getBaseURL = () => 
   (process.env.BASE_URL || "http://localhost:3000")

export const getStackClient = (queryClient: QueryClient) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      kanban: kanbanClientPlugin({
        // Required configuration
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient: queryClient,
        // Optional: SEO configuration
        seo: {
          siteName: "My Kanban App",
          description: "Manage your projects with kanban boards",
        },
      })
    }
  })
}
```

**Required configuration:**

* `apiBaseURL`: Base URL for API calls during SSR data prefetching
* `apiBasePath`: Path where your API is mounted (e.g., `/api/data`)
* `siteBaseURL`: Base URL of your site
* `siteBasePath`: Path where your pages are mounted (e.g., `/pages`)
* `queryClient`: React Query client instance

### 3. Import Plugin CSS

Add the kanban plugin CSS to your global stylesheet:

```css title="app/globals.css"
@import "@btst/stack/plugins/kanban/css";
```

This includes all necessary styles for the kanban board components and drag-and-drop functionality.

### 4. Add Context Overrides

Configure framework-specific overrides in your `StackProvider`:

<Tabs groupId="frameworks" items={["next-js", "react-router", "tanstack"]} persist>
  <Tab value="next-js">
    ```tsx title="app/pages/[[...all]]/layout.tsx"
    import { StackProvider } from "@btst/stack/context"
    import type { KanbanPluginOverrides } from "@btst/stack/plugins/kanban/client"
    import Link from "next/link"
    import { useRouter } from "next/navigation"
    import { resolveUser, searchUsers } from "@/lib/users" // Your user resolver

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (process.env.NEXT_PUBLIC_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      kanban: KanbanPluginOverrides
    }

    export default function Layout({ children }) {
      const router = useRouter()
      const baseURL = getBaseURL()
      
      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            kanban: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (path) => router.push(path),
              refresh: () => router.refresh(),
              Link: (props) => <Link {...props} />,
              // Required: User resolution for assignees
              resolveUser,
              searchUsers,
            }
          }}
        >
          {children}
        </StackProvider>
      )
    }
    ```
  </Tab>

  <Tab value="react-router">
    ```tsx title="app/routes/pages/_layout.tsx"
    import { Outlet, Link, useNavigate } from "react-router"
    import { StackProvider } from "@btst/stack/context"
    import type { KanbanPluginOverrides } from "@btst/stack/plugins/kanban/client"
    import { resolveUser, searchUsers } from "../lib/users" // Your user resolver

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:5173")

    type PluginOverrides = {
      kanban: KanbanPluginOverrides
    }

    export default function Layout() {
      const navigate = useNavigate()
      const baseURL = getBaseURL()
      
      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            kanban: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (href) => navigate(href),
              Link: ({ href, children, className, ...props }) => (
                <Link to={href || ""} className={className} {...props}>
                  {children}
                </Link>
              ),
              // Required: User resolution for assignees
              resolveUser,
              searchUsers,
            }
          }}
        >
          <Outlet />
        </StackProvider>
      )
    }
    ```
  </Tab>

  <Tab value="tanstack">
    ```tsx title="src/routes/pages/route.tsx"
    import { StackProvider } from "@btst/stack/context"
    import type { KanbanPluginOverrides } from "@btst/stack/plugins/kanban/client"
    import { Link, useRouter, Outlet } from "@tanstack/react-router"
    import { resolveUser, searchUsers } from "../../lib/users" // Your user resolver

    const getBaseURL = () => 
      typeof window !== 'undefined' 
        ? (import.meta.env.VITE_BASE_URL || window.location.origin)
        : (process.env.BASE_URL || "http://localhost:3000")

    type PluginOverrides = {
      kanban: KanbanPluginOverrides
    }

    function Layout() {
      const router = useRouter()
      const baseURL = getBaseURL()

      return (
        <StackProvider<PluginOverrides>
          basePath="/pages"
          overrides={{
            kanban: {
              apiBaseURL: baseURL,
              apiBasePath: "/api/data",
              navigate: (href) => router.navigate({ href }),
              Link: ({ href, children, className, ...props }) => (
                <Link to={href} className={className} {...props}>
                  {children}
                </Link>
              ),
              // Required: User resolution for assignees
              resolveUser,
              searchUsers,
            }
          }}
        >
          <Outlet />
        </StackProvider>
      )
    }
    ```
  </Tab>
</Tabs>

**Required overrides:**

* `apiBaseURL`: Base URL for API calls
* `apiBasePath`: Path where your API is mounted
* `navigate`: Function for programmatic navigation
* `resolveUser`: Function to resolve user info from ID (for assignee display)
* `searchUsers`: Function to search/list users (for assignee picker)

**Optional overrides:**

* `Link`: Custom Link component (defaults to `<a>` tag)
* `refresh`: Function to refresh server-side cache
* `localization`: Custom localization strings

### 5. Generate Database Schema

After adding the plugin, generate your database schema using the CLI:

```bash
npx @btst/cli generate --orm prisma --config lib/stack.ts  --output prisma/schema.prisma
```

This will create the necessary database tables for boards, columns, and tasks. Run migrations as needed for your ORM.

## Congratulations, You're Done!

Your kanban plugin is now fully configured and ready to use! Here's a quick reference of what's available:

### API Endpoints

The kanban plugin provides the following API endpoints (mounted at your configured `apiBasePath`):

**Boards:**

* **GET** `/boards` - List boards with optional filtering
* **GET** `/boards/:id` - Get a single board with columns and tasks
* **POST** `/boards` - Create a new board (with default columns)
* **PUT** `/boards/:id` - Update a board
* **DELETE** `/boards/:id` - Delete a board

**Columns:**

* **POST** `/columns` - Create a new column
* **PUT** `/columns/:id` - Update a column
* **DELETE** `/columns/:id` - Delete a column
* **POST** `/columns/reorder` - Reorder columns within a board

**Tasks:**

* **POST** `/tasks` - Create a new task
* **PUT** `/tasks/:id` - Update a task
* **DELETE** `/tasks/:id` - Delete a task
* **POST** `/tasks/move` - Move a task to a different column
* **POST** `/tasks/reorder` - Reorder tasks within a column

### Page Routes

The kanban plugin automatically creates the following pages (mounted at your configured `siteBasePath`):

* `/kanban` - Boards list page
* `/kanban/new` - Create new board page
* `/kanban/:boardId` - Board detail page with kanban view

### Page Component Overrides

You can replace any built-in page with your own React component using the optional `pageComponents` field in `kanbanClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
kanbanClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the boards list page
    boards: MyCustomBoardsPage,
    // Replace the board detail page — receives boardId as a prop
    board: ({ boardId }) => <MyCustomBoardPage boardId={boardId} />,
    // Replace the new board page
    newBoard: MyCustomNewBoardPage,
  },
})
```

### Priority Levels

Tasks support four priority levels, each with a visual badge:

| Priority | Badge Color | Use Case                                     |
| -------- | ----------- | -------------------------------------------- |
| LOW      | Gray        | Nice-to-have tasks                           |
| MEDIUM   | Yellow      | Standard priority (default)                  |
| HIGH     | Orange      | Important tasks                              |
| URGENT   | Red         | Critical tasks requiring immediate attention |

## Task Assignees

The kanban plugin supports assigning users to tasks. Since the plugin is authentication-agnostic, you provide resolver functions to integrate with your auth system.

### KanbanUser Type

The plugin uses a simple `KanbanUser` interface for user information:

```ts
interface KanbanUser {
  id: string;       // Unique user identifier
  name: string;     // Display name
  avatarUrl?: string; // Optional avatar image URL
  email?: string;   // Optional email address
}
```

### Required Resolver Functions

You must provide two resolver functions in your overrides:

```tsx title="Context Overrides"
overrides={{
  kanban: {
    // ... other overrides
    
    // Resolve user info from an ID (for displaying assignee on task cards)
    resolveUser: (userId: string) => {
      // Return KanbanUser or null if not found
    },
    
    // Search/list users (for the assignee picker dropdown)
    searchUsers: (query: string, boardId?: string) => {
      // Return array of KanbanUser matching the query
      // Return all users if query is empty
    },
  }
}}
```

### Integration Examples

<Tabs groupId="auth" items={["clerk", "nextauth", "mock"]} persist>
  <Tab value="clerk">
    ```tsx title="Clerk Integration"
    import { clerkClient } from "@clerk/nextjs/server"

    const overrides = {
      kanban: {
        // ... other overrides
        resolveUser: async (userId) => {
          const user = await clerkClient.users.getUser(userId)
          return {
            id: user.id,
            name: user.fullName || user.username || "Unknown",
            avatarUrl: user.imageUrl,
            email: user.emailAddresses[0]?.emailAddress,
          }
        },
        searchUsers: async (query) => {
          const users = await clerkClient.users.getUserList({ query, limit: 10 })
          return users.map(user => ({
            id: user.id,
            name: user.fullName || user.username || "Unknown",
            avatarUrl: user.imageUrl,
            email: user.emailAddresses[0]?.emailAddress,
          }))
        },
      }
    }
    ```
  </Tab>

  <Tab value="nextauth">
    ```tsx title="NextAuth/Prisma Integration"
    import { prisma } from "@/lib/prisma"

    const overrides = {
      kanban: {
        // ... other overrides
        resolveUser: async (userId) => {
          const user = await prisma.user.findUnique({ 
            where: { id: userId } 
          })
          return user ? {
            id: user.id,
            name: user.name || "Unknown",
            avatarUrl: user.image || undefined,
            email: user.email || undefined,
          } : null
        },
        searchUsers: async (query) => {
          const users = await prisma.user.findMany({
            where: query ? {
              OR: [
                { name: { contains: query, mode: "insensitive" } },
                { email: { contains: query, mode: "insensitive" } },
              ]
            } : undefined,
            take: 10,
          })
          return users.map(user => ({
            id: user.id,
            name: user.name || "Unknown",
            avatarUrl: user.image || undefined,
            email: user.email || undefined,
          }))
        },
      }
    }
    ```
  </Tab>

  <Tab value="mock">
    ```tsx title="Mock Users (for development)"
    import type { KanbanUser } from "@btst/stack/plugins/kanban/client"

    const MOCK_USERS: KanbanUser[] = [
      { id: "user-1", name: "Alice Johnson", avatarUrl: "https://api.dicebear.com/7.x/avataaars/svg?seed=alice" },
      { id: "user-2", name: "Bob Smith", avatarUrl: "https://api.dicebear.com/7.x/avataaars/svg?seed=bob" },
      { id: "user-3", name: "Carol Williams", avatarUrl: "https://api.dicebear.com/7.x/avataaars/svg?seed=carol" },
    ]

    const overrides = {
      kanban: {
        // ... other overrides
        resolveUser: (userId) => MOCK_USERS.find(u => u.id === userId) ?? null,
        searchUsers: (query) => {
          if (!query) return MOCK_USERS
          const lower = query.toLowerCase()
          return MOCK_USERS.filter(u => u.name.toLowerCase().includes(lower))
        },
      }
    }
    ```
  </Tab>
</Tabs>

### Assignee Display

When a task has an assignee:

* **Task Card**: Shows the user's avatar and name
* **Task Form**: Displays a searchable dropdown to select/change assignee

When no assignee is set, the task card shows "Unassigned" with a placeholder icon.

## API Reference

### Backend (`@btst/stack/plugins/kanban/api`)

#### kanbanBackendPlugin

Creates the kanban backend plugin with optional hooks for authorization and customization.

```ts
import { kanbanBackendPlugin } from "@btst/stack/plugins/kanban/api"

const { handler, dbSchema } = stack({
  plugins: {
    kanban: kanbanBackendPlugin(hooks)
  },
  // ...
})
```

#### KanbanBackendHooks

Customize backend behavior with optional lifecycle hooks. All hooks are optional and allow you to add authorization, logging, and custom behavior:

```ts title="lib/stack.ts"
import { kanbanBackendPlugin, type KanbanBackendHooks } from "@btst/stack/plugins/kanban/api"

const kanbanHooks: KanbanBackendHooks = {
  // Board hooks — throw to deny access
  onBeforeListBoards: async (filter, context) => {
    if (!await isAuthenticated(context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeCreateBoard: async (data, context) => {
    if (!await isAuthenticated(context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeUpdateBoard: async (boardId, data, context) => {
    if (!await isBoardOwner(boardId, context.headers))
      throw new Error("You do not own this board")
  },
  onBeforeDeleteBoard: async (boardId, context) => {
    if (!await isBoardOwner(boardId, context.headers))
      throw new Error("You do not own this board")
  },
  
  // Column hooks
  onBeforeCreateColumn: async (data, context) => {
    if (!await canEditBoard(data.boardId, context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeUpdateColumn: async (columnId, data, context) => {
    if (!await canEditColumn(columnId, context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeDeleteColumn: async (columnId, context) => {
    if (!await canEditColumn(columnId, context.headers))
      throw new Error("Unauthorized")
  },
  
  // Task hooks
  onBeforeCreateTask: async (data, context) => {
    if (!await canEditColumn(data.columnId, context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeUpdateTask: async (taskId, data, context) => {
    if (!await canEditTask(taskId, context.headers))
      throw new Error("Unauthorized")
  },
  onBeforeDeleteTask: async (taskId, context) => {
    if (!await canEditTask(taskId, context.headers))
      throw new Error("Unauthorized")
  },
  
  // Lifecycle hooks
  onBoardCreated: async (board, context) => {
    console.log("Board created:", board.name)
  },
  onTaskCreated: async (task, context) => {
    console.log("Task created:", task.title)
  },
}

const { handler, dbSchema } = stack({
  plugins: {
    kanban: kanbanBackendPlugin(kanbanHooks)
  },
  // ...
})
```

**Available hooks:**

| Hook                   | Description                                          |
| ---------------------- | ---------------------------------------------------- |
| `onBeforeListBoards`   | Called before listing boards. Throw to deny.         |
| `onBeforeCreateBoard`  | Called before creating a board. Throw to deny.       |
| `onBeforeReadBoard`    | Called before reading a single board. Throw to deny. |
| `onBeforeUpdateBoard`  | Called before updating a board. Throw to deny.       |
| `onBeforeDeleteBoard`  | Called before deleting a board. Throw to deny.       |
| `onBeforeCreateColumn` | Called before creating a column. Throw to deny.      |
| `onBeforeUpdateColumn` | Called before updating a column. Throw to deny.      |
| `onBeforeDeleteColumn` | Called before deleting a column. Throw to deny.      |
| `onBeforeCreateTask`   | Called before creating a task. Throw to deny.        |
| `onBeforeUpdateTask`   | Called before updating a task. Throw to deny.        |
| `onBeforeDeleteTask`   | Called before deleting a task. Throw to deny.        |
| `onBoardsRead`         | Called after boards are listed successfully.         |
| `onBoardCreated`       | Called after a board is created.                     |
| `onBoardUpdated`       | Called after a board is updated.                     |
| `onBoardDeleted`       | Called after a board is deleted.                     |
| `onColumnCreated`      | Called after a column is created.                    |
| `onColumnUpdated`      | Called after a column is updated.                    |
| `onColumnDeleted`      | Called after a column is deleted.                    |
| `onTaskCreated`        | Called after a task is created.                      |
| `onTaskUpdated`        | Called after a task is updated.                      |
| `onTaskDeleted`        | Called after a task is deleted.                      |

### Client (`@btst/stack/plugins/kanban/client`)

#### kanbanClientPlugin

Creates the kanban client plugin with routes, loaders, and meta generators.

```tsx title="lib/stack-client.tsx"
kanban: kanbanClientPlugin({
  // Required configuration
  apiBaseURL: baseURL,
  apiBasePath: "/api/data",
  siteBaseURL: baseURL,
  siteBasePath: "/pages",
  queryClient: queryClient,
  // Optional SEO configuration
  seo: {
    siteName: "My Kanban App",
    description: "Project management",
  },
  // Optional hooks
  hooks: {
    beforeLoadBoards: async (context) => {
      if (!await isAuthenticated(context.headers))
        throw new Error("Unauthorized")
    },
    beforeLoadBoard: async (boardId, context) => {
      if (!await canViewBoard(boardId, context.headers))
        throw new Error("Unauthorized")
    },
  },
})
```

#### KanbanClientHooks

Customize client-side behavior with lifecycle hooks:

| Hook                 | Description                                                |
| -------------------- | ---------------------------------------------------------- |
| `beforeLoadBoards`   | Called before loading boards list. Throw to cancel.        |
| `afterLoadBoards`    | Called after boards are loaded.                            |
| `beforeLoadBoard`    | Called before loading a single board. Throw to cancel.     |
| `afterLoadBoard`     | Called after a board is loaded.                            |
| `beforeLoadNewBoard` | Called before loading the new board page. Throw to cancel. |
| `afterLoadNewBoard`  | Called after the new board page is loaded.                 |
| `onLoadError`        | Called when a loading error occurs.                        |

#### KanbanPluginOverrides

Configure framework-specific overrides and route lifecycle hooks:

```tsx
overrides={{
  kanban: {
    // Required overrides
    apiBaseURL: baseURL,
    apiBasePath: "/api/data",
    navigate: (path) => router.push(path),
    
    // Required: User resolution for assignees
    resolveUser: (userId) => findUserById(userId),
    searchUsers: (query) => searchAllUsers(query),
    
    // Optional overrides
    Link: (props) => <Link {...props} />,
    refresh: () => router.refresh(),
    
    // Optional lifecycle hooks
    onRouteRender: async (routeName, context) => {
      console.log("Rendering route:", routeName)
    },
    onBeforeBoardsPageRendered: (context) => {
      return isAuthenticated()
    },
    onBeforeBoardPageRendered: (boardId, context) => {
      return canViewBoard(boardId)
    },
    onBeforeNewBoardPageRendered: (context) => {
      return canCreateBoard()
    },
  }
}}
```

**Required overrides:**

| Override      | Type                                                | Description                          |
| ------------- | --------------------------------------------------- | ------------------------------------ |
| `apiBaseURL`  | `string`                                            | Base URL for API calls               |
| `apiBasePath` | `string`                                            | Path where your API is mounted       |
| `navigate`    | `(path: string) => void`                            | Function for programmatic navigation |
| `resolveUser` | `(userId: string) => KanbanUser \| null`            | Resolve user info from ID            |
| `searchUsers` | `(query: string, boardId?: string) => KanbanUser[]` | Search/list users for picker         |

## React Hooks

Import hooks from `@btst/stack/plugins/kanban/client/hooks` to use in your components:

```tsx
import { 
  useBoards,
  useBoard,
  useBoardMutations,
  useColumnMutations,
  useTaskMutations,
  useResolveUser,
  useSearchUsers,
} from "@btst/stack/plugins/kanban/client/hooks"

// List all boards
const { data: boards, isLoading, error } = useBoards()

// Get a single board with columns and tasks
const { data: board, isLoading, error } = useBoard(boardId)

// Board mutations
const { createBoard, updateBoard, deleteBoard, isCreating, isUpdating, isDeleting } = useBoardMutations()

// Column mutations
const { createColumn, updateColumn, deleteColumn } = useColumnMutations()

// Task mutations (includes assigneeId support)
const { createTask, updateTask, deleteTask, moveTask } = useTaskMutations()

// Resolve user info (with caching)
const { data: user, isLoading } = useResolveUser(assigneeId)

// Search users for picker
const { data: users, isLoading } = useSearchUsers(searchQuery, boardId)
```

## Types

The plugin exports TypeScript types for all data structures:

```ts
// API types
import type { 
  Board, 
  Column, 
  Task, 
  Priority,
  BoardWithColumns,
  ColumnWithTasks,
  SerializedBoard,
  SerializedColumn,
  SerializedTask,
} from "@btst/stack/plugins/kanban/api"

// Client types (for user resolution)
import type { 
  KanbanUser,
  KanbanPluginOverrides,
} from "@btst/stack/plugins/kanban/client"
```

## Server-side Data Access

The Kanban plugin exposes standalone getter functions for server-side and SSG use cases.

### Two patterns

**Pattern 1 — via `stack().api`**

```ts title="app/lib/stack.ts"
import { myStack } from "./stack";

// List all boards (with columns and tasks)
const result = await myStack.api.kanban.getAllBoards({ ownerId: "user-123" });
// result.items  — BoardWithColumns[]
// result.total  — total count before pagination
// result.limit  — applied limit
// result.offset — applied offset

// Get a single board with full column/task tree
const board = await myStack.api.kanban.getBoardById("board-456");
if (board) {
  board.columns.forEach((col) => {
    console.log(col.title, col.tasks.length, "tasks");
  });
}
```

**Pattern 2 — direct import**

```ts
import {
  getAllBoards,
  getBoardById,
} from "@btst/stack/plugins/kanban/api";

// In Next.js generateStaticParams
export async function generateStaticParams() {
  const { items } = await getAllBoards(myAdapter);
  return items.map((b) => ({ slug: b.slug }));
}
```

### Available getters

| Function                         | Returns                    | Description                                                                           |
| -------------------------------- | -------------------------- | ------------------------------------------------------------------------------------- |
| `getAllBoards(adapter, params?)` | `BoardListResult`          | Paginated boards with columns and tasks; supports slug/ownerId/organizationId filters |
| `getBoardById(adapter, id)`      | `BoardWithColumns \| null` | Single board with full column/task tree, or `null`                                    |

### `BoardListResult`

<AutoTypeTable path="../packages/stack/src/plugins/kanban/api/getters.ts" name="BoardListResult" />

## Static Site Generation (SSG)

`route.loader()` makes HTTP requests to `apiBaseURL`, which silently fails during `next build` because no dev server is running. Use `prefetchForRoute()` instead — it reads directly from the database and pre-populates the React Query cache before rendering.

### `prefetchForRoute(routeKey, queryClient, params?)`

| Route key    | Params required       | Data prefetched                     |
| ------------ | --------------------- | ----------------------------------- |
| `"boards"`   | —                     | First page of boards                |
| `"newBoard"` | —                     | *(nothing)*                         |
| `"board"`    | `{ boardId: string }` | Single board with columns and tasks |

### Next.js example

```tsx title="app/pages/kanban/page.tsx"
import { dehydrate, HydrationBoundary } from "@tanstack/react-query"
import { getOrCreateQueryClient } from "@/lib/query-client"
import { getStackClient } from "@/lib/stack-client"
import { myStack } from "@/lib/stack"
import { metaElementsToObject, normalizePath } from "@btst/stack/client"
import type { Metadata } from "next"

export async function generateStaticParams() {
  return [{}]
}

// export const revalidate = 3600 // uncomment for ISR

export async function generateMetadata(): Promise<Metadata> {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["kanban"]))
  if (!route) return { title: "Kanban Boards" }
  await myStack.api.kanban.prefetchForRoute("boards", queryClient)
  return metaElementsToObject(route.meta?.() ?? []) satisfies Metadata
}

export default async function KanbanBoardsPage() {
  const queryClient = getOrCreateQueryClient()
  const stackClient = getStackClient(queryClient)
  const route = stackClient.router.getRoute(normalizePath(["kanban"]))
  if (!route) return null
  // Reads directly from DB — works at build time, no HTTP server required
  await myStack.api.kanban.prefetchForRoute("boards", queryClient)
  return (
    <HydrationBoundary state={dehydrate(queryClient)}>
      <route.PageComponent />
    </HydrationBoundary>
  )
}
```

### ISR cache invalidation

If you use [Incremental Static Regeneration](https://nextjs.org/docs/app/building-your-application/data-fetching/incremental-static-regeneration), call `revalidatePath` inside the backend lifecycle hooks so Next.js regenerates the page on the next request:

```ts title="lib/stack.ts"
import { revalidatePath } from "next/cache"
import type { KanbanBackendHooks } from "@btst/stack/plugins/kanban/api"

const kanbanHooks: KanbanBackendHooks = {
  onBoardCreated: async (board) => {
    revalidatePath("/kanban")
  },
  onBoardUpdated: async (board) => {
    revalidatePath("/kanban")
  },
  onBoardDeleted: async (boardId) => {
    revalidatePath("/kanban")
  },
}
```

### Query key consistency

`prefetchForRoute` uses the same query key shapes as `createKanbanQueryKeys` (the HTTP client). The shared constants live in `@btst/stack/plugins/kanban/api` as `KANBAN_QUERY_KEYS` and `boardsListDiscriminator`, so the two paths can never drift silently.

## Server-side Mutations

In addition to the read-only getters, the Kanban plugin exposes **mutation functions** for creating boards, columns, and tasks directly from server-side code — no HTTP roundtrip required. These live in `api/mutations.ts` and are re-exported from `@btst/stack/plugins/kanban/api`.

<Callout type="warn">
  **Mutation functions bypass authorization hooks.** Hooks such as `onBeforeCreateBoard` and `onBeforeCreateTask` are **not** called when you use these functions. They are pure database writes — the caller is responsible for any access-control checks before invoking them. Never call mutations from user-facing request handlers without adding your own authorization logic first.
</Callout>

### Available mutations

| Function                                                | Description                                                 |
| ------------------------------------------------------- | ----------------------------------------------------------- |
| `createKanbanTask(adapter, input)`                      | Create a task in a column; auto-computes insertion order    |
| `findOrCreateKanbanBoard(adapter, slug, name, columns)` | Find a board by slug or create it with custom column titles |
| `getKanbanColumnsByBoardId(adapter, boardId)`           | List columns for a board sorted by order                    |

### `createKanbanTask`

```ts
import { createKanbanTask } from "@btst/stack/plugins/kanban/api"

await createKanbanTask(myStack.adapter, {
  title: "Review Q1 financials",
  columnId: "col-abc",
  description: "See attached report",
  priority: "HIGH",         // "LOW" | "MEDIUM" | "HIGH" | "URGENT"
})
```

### `findOrCreateKanbanBoard`

Creates a board with custom column titles on first call; returns the existing board on subsequent calls. Safe to call concurrently — uses find-before-create.

```ts
import { findOrCreateKanbanBoard, getKanbanColumnsByBoardId } from "@btst/stack/plugins/kanban/api"

const board = await findOrCreateKanbanBoard(
  myStack.adapter,
  "advisor-review-queue",           // slug (URL-safe, unique)
  "Advisor Review Queue",           // display name (used only on creation)
  ["New Intakes", "Under Review", "Escalated"], // column titles (used only on creation)
)

const columns = await getKanbanColumnsByBoardId(myStack.adapter, board.id)
const target = columns.find((c) => c.title === "New Intakes")
```

### Via `myStack.api.kanban`

All three functions are also available pre-bound to the stack adapter:

```ts
const board = await myStack.api.kanban.findOrCreateBoard(
  "advisor-review-queue",
  "Advisor Review Queue",
  ["New Intakes", "Under Review", "Escalated"],
)
const columns = await myStack.api.kanban.getColumnsByBoardId(board.id)
await myStack.api.kanban.createTask({
  title: "Sarah Chen — Ready for Review",
  columnId: columns[0]!.id,
  priority: "MEDIUM",
})
```

### Inside an AI tool `execute` function

The primary use case for mutations is populating Kanban boards from server-side AI tool callbacks:

```ts title="lib/stack.ts"
import { tool } from "ai"
import { z } from "zod"
import { createKanbanTask, findOrCreateKanbanBoard, getKanbanColumnsByBoardId } from "@btst/stack/plugins/kanban/api"

// Adapter captured after stack() returns — safe for tool execute closures
let adapter: any

const myTool = tool({
  description: "Create a review card",
  inputSchema: z.object({ title: z.string(), urgent: z.boolean() }),
  execute: async ({ title, urgent }) => {
    const board = await findOrCreateKanbanBoard(adapter, "review", "Review Queue", ["To Do", "Urgent"])
    const columns = await getKanbanColumnsByBoardId(adapter, board.id)
    const col = urgent ? columns.find((c) => c.title === "Urgent") : columns[0]
    await createKanbanTask(adapter, { title, columnId: col!.id, priority: urgent ? "URGENT" : "MEDIUM" })
    return { success: true }
  },
})

export const myStack = stack({ plugins: { aiChat: aiChatBackendPlugin({ tools: { myTool } }), kanban: kanbanBackendPlugin() } })
adapter = myStack.adapter
```

## Shadcn Registry

The Kanban plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/kanban/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-kanban.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/kanban/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { kanbanClientPlugin } from "@btst/stack/plugins/kanban/client"
// Import your ejected (and customized) page components
import { BoardsPageComponent } from "@/components/btst/kanban/client/components/pages/boards-page"
import { BoardPageComponent } from "@/components/btst/kanban/client/components/pages/board-page"

kanbanClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    boards: BoardsPageComponent,   // replaces the boards list page
    board: BoardPageComponent,     // replaces the board detail page
    // newBoard — omit to keep built-in default
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.


# OpenAPI Plugin (/plugins/open-api)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import openApiDemo from "../../../assets/openapi-demo.png";

<div className="my-2">
  <a href={openApiDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={openApiDemo} alt="OpenAPI Plugin Demo - Interactive Scalar UI" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

The OpenAPI plugin automatically generates OpenAPI 3.1 documentation for all your BTST plugins. It provides both a JSON schema endpoint and an interactive API reference UI powered by [Scalar](https://scalar.com/).

## Features

* **Automatic Schema Generation** - Traverses all registered plugins and extracts endpoint metadata
* **OpenAPI 3.1 Compliant** - Generates valid OpenAPI 3.1 schemas from Zod definitions
* **Interactive UI** - Beautiful API reference page powered by Scalar
* **Multiple Themes** - Choose from 10+ Scalar themes to match your brand
* **Zero Configuration** - Works out of the box with sensible defaults

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

### Add Plugin to Backend API

Import and register the OpenAPI backend plugin in your `stack.ts` file:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { blogBackendPlugin } from "@btst/stack/plugins/blog/api"
import { openApiBackendPlugin } from "@btst/stack/plugins/open-api/api"
// ... your adapter imports

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    blog: blogBackendPlugin(),
    // Add OpenAPI plugin - it will document all other plugins
    openApi: openApiBackendPlugin({
      title: "My API",
      description: "API documentation for my application",
      theme: "kepler",
    }),
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

export { handler, dbSchema }
```

<Callout type="warn">
  The OpenAPI plugin is backend-only. There is no client plugin required.
</Callout>

## Endpoints

Once configured, the plugin exposes two endpoints:

| Endpoint                        | Description                         |
| ------------------------------- | ----------------------------------- |
| `GET /api/data/open-api/schema` | Returns the OpenAPI 3.1 JSON schema |
| `GET /api/data/reference`       | Interactive Scalar API reference UI |

Replace `/api/data` with your configured `basePath`.

## Configuration Options

```ts
openApiBackendPlugin({
  // Custom title for the API documentation
  title: "My API",
  
  // Description shown in the API reference
  description: "API documentation for my application",
  
  // API version string
  version: "1.0.0",
  
  // Scalar theme (see themes section below)
  theme: "kepler",
  
  // Custom path for the reference page (default: "/reference")
  path: "/docs",
  
  // Disable the HTML reference page (only serve JSON schema)
  disableDefaultReference: false,
  
  // CSP nonce for inline scripts (for strict Content Security Policy)
  nonce: "your-nonce-value",
})
```

## Available Themes

The plugin supports all Scalar themes:

| Theme        | Description                 |
| ------------ | --------------------------- |
| `default`    | Clean, minimal design       |
| `alternate`  | Alternative styling         |
| `moon`       | Dark mode optimized         |
| `purple`     | Purple accent colors        |
| `solarized`  | Solarized color scheme      |
| `bluePlanet` | Blue-focused theme          |
| `saturn`     | Saturn-inspired colors      |
| `kepler`     | Modern space theme          |
| `mars`       | Red/orange accent theme     |
| `deepSpace`  | Deep dark theme             |
| `laserwave`  | Synthwave-inspired          |
| `none`       | No styling (bring your own) |

## How It Works

The OpenAPI plugin introspects all registered plugins at startup:

1. **Context Injection** - BTST passes a context object containing all plugins to each plugin's `routes()` function
2. **Endpoint Traversal** - The OpenAPI plugin iterates over all other plugins and their endpoints
3. **Schema Extraction** - Zod schemas from `query`, `body`, and `params` are converted to OpenAPI schema objects
4. **Path Transformation** - Express-style paths (`:param`) are converted to OpenAPI format (`{param}`)
5. **Tag Generation** - Each plugin becomes a tag in the OpenAPI spec for easy navigation

## Generated Schema Structure

The plugin generates a complete OpenAPI 3.1 schema including:

```json
{
  "openapi": "3.1.0",
  "info": {
    "title": "My API",
    "description": "API documentation",
    "version": "1.0.0"
  },
  "servers": [
    { "url": "/api/data", "description": "API Server" }
  ],
  "tags": [
    { "name": "Blog", "description": "Blog plugin endpoints" },
    { "name": "Cms", "description": "Cms plugin endpoints" }
  ],
  "paths": {
    "/posts": {
      "get": {
        "tags": ["Blog"],
        "operationId": "blog_listPosts",
        "parameters": [...],
        "responses": {...}
      }
    }
  },
  "components": {
    "securitySchemes": {
      "bearerAuth": { "type": "http", "scheme": "bearer" },
      "cookieAuth": { "type": "apiKey", "in": "cookie", "name": "session" }
    }
  }
}
```

## Using the JSON Schema

You can fetch the raw OpenAPI schema for use with other tools:

```bash
# Fetch the OpenAPI schema
curl http://localhost:3000/api/data/open-api/schema

# Save to a file
curl http://localhost:3000/api/data/open-api/schema > openapi.json
```

The schema can be used with:

* **Code generators** (OpenAPI Generator, openapi-typescript)
* **API testing tools** (Postman, Insomnia)
* **Documentation platforms** (Redoc, Swagger UI)
* **Mock servers** (Prism, Mock Service Worker)

## Programmatic Access

You can also use the schema generator directly:

```ts
import { generateOpenAPISchema } from "@btst/stack/plugins/open-api/api"

// Generate schema from context
const schema = generateOpenAPISchema(context, {
  title: "My API",
  description: "Custom description",
  version: "2.0.0",
})
```

## Security Considerations

<Callout type="warn">
  The OpenAPI documentation exposes your API structure. Consider these security measures:
</Callout>

1. **Restrict Access** - Use middleware to restrict access to the reference page in production
2. **Disable in Production** - Set `disableDefaultReference: true` and only serve the JSON to authorized users
3. **Use CSP Nonces** - If you have strict Content Security Policy, provide a `nonce` option

```ts
// Example: Disable reference UI in production
openApiBackendPlugin({
  disableDefaultReference: process.env.NODE_ENV === "production",
})
```

## Troubleshooting

### Schema shows empty or incomplete endpoints

Ensure plugins are registered **before** the OpenAPI plugin in your plugins object. The OpenAPI plugin introspects all other plugins at initialization time.

### Reference page shows blank

Check your browser console for CSP (Content Security Policy) errors. If you have strict CSP, you may need to:

1. Provide a `nonce` option
2. Allow `cdn.jsdelivr.net` in your script-src directive

### Types not showing correctly

The plugin converts Zod schemas to OpenAPI schemas. Complex nested types, unions, and intersections should work, but some edge cases may show as `{ type: "object" }`. Consider adding explicit `metadata.openapi` to your endpoints for better documentation.


# Route Docs Plugin (/plugins/route-docs)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import Image from "next/image";

import routeDocsDemo from "../../../assets/route-docs-demo.png";

<div className="my-2">
  <a href={routeDocsDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={routeDocsDemo} alt="Route Docs Plugin Demo - Interactive route documentation" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" placeholder="blur" />
  </a>
</div>

The Route Docs plugin automatically generates documentation for all your client-side routes. It provides an interactive reference page that displays route paths, parameters, sitemap entries, and navigation tools.

## Features

* **Automatic Route Discovery** - Traverses all registered client plugins and extracts route metadata
* **Interactive Navigation** - Click any route to scroll to its details, or use the sidebar
* **Parameter Documentation** - Shows path and query parameters with types and descriptions
* **Sitemap Integration** - Displays sitemap entries for each route
* **Live Route Testing** - Fill in parameters and navigate directly to routes
* **Responsive Design** - Mobile-friendly with collapsible sidebar

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first.
</Callout>

### Add Plugin to Client

Import and register the Route Docs client plugin in your client configuration:

```tsx title="lib/stack-client.tsx"
import { stackClient } from "@btst/stack/client"
import { blogClientPlugin } from "@btst/stack/plugins/blog/client"
import { routeDocsClientPlugin } from "@btst/stack/plugins/route-docs/client"

const { ClientProvider, routes, ...client } = stackClient({
  basePath: "/pages",
  apiBasePath: "/api/data",
  queryClient: queryClient,
  plugins: {
    blog: blogClientPlugin({ queryClient }),
    // Add Route Docs plugin - it will document all other client plugins
    routeDocs: routeDocsClientPlugin({
      queryClient: queryClient,
      siteBasePath: "/pages",
      title: "Client Route Documentation",
      description: "Documentation for all client routes in this application",
    }),
  },
})

export { ClientProvider, routes, client }
```

<Callout type="warn">
  The Route Docs plugin is client-only. There is no backend plugin required.
</Callout>

## Accessing the Documentation

Once configured, navigate to your route docs page:

| Route               | Description                          |
| ------------------- | ------------------------------------ |
| `/pages/route-docs` | Interactive route documentation page |

Replace `/pages` with your configured `siteBasePath`.

## Configuration Options

```tsx
routeDocsClientPlugin({
  // React Query client for data fetching
  queryClient: queryClient,
  
  // Custom title for the documentation page
  title: "Client Route Documentation",
  
  // Description shown on the page
  description: "Documentation for all client routes",
  
  // Base path for generating URLs (default: "/pages")
  siteBasePath: "/pages",
  
  // Custom route path (default: "/route-docs")
  basePath: "/docs/routes",
})
```

## Page Layout

The documentation page includes several sections:

### All Routes Table

An overview table showing all routes at a glance with:

* Route path with highlighted parameters
* Plugin name
* Parameter count
* Sitemap entry count
* Quick actions (visit or scroll to details)

### Route Details

For each route, detailed documentation includes:

1. **Route Path** - The route pattern with parameters highlighted
2. **Navigate to Route** - Interactive form to fill in parameters and visit the route
3. **Path Parameters** - Table of path parameters with name, type, required status
4. **Query Parameters** - Table of query parameters with defaults and descriptions
5. **Sitemap Entries** - URLs that match this route pattern

## How It Works

The Route Docs plugin introspects all registered client plugins:

1. **Context Access** - BTST passes a context object containing all plugins
2. **Route Traversal** - The plugin iterates over all client plugins and their routes
3. **Metadata Extraction** - Route metadata including path, parameters, and meta tags are collected
4. **Sitemap Collection** - Each plugin's sitemap entries are gathered and matched to routes
5. **Schema Generation** - A complete documentation schema is generated and cached

## Security Considerations

<Callout type="warn">
  The Route Docs page exposes your application's route structure. Consider these measures:
</Callout>

1. **Development Only** - Consider only enabling in development environments
2. **Access Control** - Add authentication middleware to protect the route
3. **Sensitive Routes** - Be aware that all registered routes will be documented

```tsx
// Example: Only enable in development
const plugins = {
  blog: blogClientPlugin({ queryClient }),
  ...(process.env.NODE_ENV === "development" && {
    routeDocs: routeDocsClientPlugin({ queryClient }),
  }),
}
```


# UI Builder Plugin (/plugins/ui-builder)

import { Tabs, Tab } from "fumadocs-ui/components/tabs";
import { Callout } from "fumadocs-ui/components/callout";
import { BookOpen } from "lucide-react";
import Image from "next/image";

import uiBuilderDemo from "../../../assets/ui-builder-demo-1.gif";

<div className="my-4">
  <a href={uiBuilderDemo.src} target="_blank" rel="noopener noreferrer">
    <Image src={uiBuilderDemo} alt="UI Builder Plugin Demo" className="rounded-lg border shadow-sm w-full h-auto hover:opacity-90 transition-opacity cursor-pointer" unoptimized />
  </a>
</div>

The UI Builder plugin provides a visual drag-and-drop page creation interface where administrators can create pages using pre-defined components. Pages are stored as JSON layers in the CMS and can be rendered on public routes.

<div className="flex gap-4 my-4">
  <a href="https://www.uibuilder.app/" target="_blank" rel="noopener noreferrer" className="inline-flex items-center gap-2 text-sm text-muted-foreground hover:text-foreground transition-colors">
    <BookOpen className="w-5 h-5" />

    Full Documentation
  </a>
</div>

<Callout type="info">
  For comprehensive documentation including interactive demos, block templates, and advanced customization options, visit [uibuilder.app](https://www.uibuilder.app/).
</Callout>

**Key Features:**

* **Visual Page Builder** - Drag-and-drop interface for creating pages with components
* **Component Registry** - Pre-built shadcn/ui components + custom component support
* **Variables** - Define page variables for dynamic content
* **CMS Integration** - Leverages the CMS plugin for data persistence
* **Public Page Rendering** - Render pages by slug with the `PageRenderer` component
* **SSR Authorization** - Lifecycle hooks for protecting admin pages

[View interactive demo →](/demos/ui-builder)

## Installation

<Callout type="info">
  Ensure you followed the general [framework installation guide](/installation) first. The UI Builder requires the CMS plugin to be configured.
</Callout>

### 1. Add Content Type to CMS Backend

The UI Builder stores pages as CMS content items. Add the pre-configured content type to your CMS:

```ts title="lib/stack.ts"
import { stack } from "@btst/stack"
import { cmsBackendPlugin } from "@btst/stack/plugins/cms/api"
import { UI_BUILDER_CONTENT_TYPE } from "@btst/stack/plugins/ui-builder"

const { handler, dbSchema } = stack({
  basePath: "/api/data",
  plugins: {
    cms: cmsBackendPlugin({
      contentTypes: [
        UI_BUILDER_CONTENT_TYPE,
        // ... other content types
      ],
      hooks: {
        // Optional: Add authorization for CMS operations
        onBeforeListContent: async (typeSlug, ctx) => {
          if (typeSlug === "ui-builder-page") {
            const session = await getSession(ctx.headers)
            if (session?.user?.isAdmin !== true)
              throw new Error("Admin access required")
          }
        },
      },
    })
  },
  adapter: (db) => createMemoryAdapter(db)({})
})

export { handler, dbSchema }
```

### 2. Add Plugin to Client

Register the UI Builder client plugin:

```tsx title="lib/stack-client.tsx"
import { createStackClient } from "@btst/stack/client"
import { cmsClientPlugin } from "@btst/stack/plugins/cms/client"
import { uiBuilderClientPlugin, defaultComponentRegistry } from "@btst/stack/plugins/ui-builder/client"
import { QueryClient } from "@tanstack/react-query"
import { redirect } from "next/navigation"

const getBaseURL = () => 
  process.env.BASE_URL || "http://localhost:3000"

export const getStackClient = (queryClient: QueryClient, options?: { headers?: Headers }) => {
  const baseURL = getBaseURL()
  return createStackClient({
    plugins: {
      // CMS plugin is required
      "cms": cmsClientPlugin({
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient,
        headers: options?.headers,
      }),
      // UI Builder plugin
      "ui-builder": uiBuilderClientPlugin({
        apiBaseURL: baseURL,
        apiBasePath: "/api/data",
        siteBaseURL: baseURL,
        siteBasePath: "/pages",
        queryClient,
        componentRegistry: defaultComponentRegistry,
        headers: options?.headers,
        hooks: {
          // SSR authorization hooks
          beforeLoadPageList: async (context) => {
            const session = await getSession(context.headers)
            return session?.user?.isAdmin === true
          },
          beforeLoadPageBuilder: async (pageId, context) => {
            const session = await getSession(context.headers)
            return session?.user?.isAdmin === true
          },
          onLoadError: (error, context) => {
            redirect("/auth/sign-in")
          },
        },
      })
    }
  })
}
```

### 3. Configure Provider Overrides

Add UI Builder overrides to your layout:

```tsx title="app/pages/layout.tsx"
import type { UIBuilderPluginOverrides } from "@btst/stack/plugins/ui-builder/client"
import type { CMSPluginOverrides } from "@btst/stack/plugins/cms/client"

type PluginOverrides = {
  "cms": CMSPluginOverrides,
  "ui-builder": UIBuilderPluginOverrides,
}

<StackProvider<PluginOverrides>
  basePath="/pages"
  overrides={{
    "cms": {
      apiBaseURL: baseURL,
      apiBasePath: "/api/data",
      navigate: (path) => router.push(path),
      refresh: () => router.refresh(),
      Link: ({ href, ...props }) => <Link href={href || "#"} {...props} />,
    },
    "ui-builder": {
      apiBaseURL: baseURL,
      apiBasePath: "/api/data",
      navigate: (path) => router.push(path),
      refresh: () => router.refresh(),
      Link: ({ href, ...props }) => <Link href={href || "#"} {...props} />,
      componentRegistry: defaultComponentRegistry,
    }
  }}
>
  {children}
</StackProvider>
```

### 4. Install Required Dependencies

The UI Builder uses the Tailwind Typography plugin for the Markdown component. Install it as a dependency:

```bash
npm install @tailwindcss/typography
# or
pnpm add @tailwindcss/typography
```

### 5. Import CSS

**This step is critical for the UI Builder to work correctly.**

The UI Builder uses a large number of Tailwind utility classes for dynamic component styling. Add the CSS import to ensure Tailwind v4 scans all required classes:

```css title="app/globals.css"
@import "@btst/stack/plugins/ui-builder/css";
```

<Callout type="warn">
  Without this CSS import, many styling options in the UI Builder will not work because Tailwind won't include the dynamic classes.
</Callout>

## Admin Routes

The UI Builder plugin provides these admin routes:

| Route                  | Description                                      |
| ---------------------- | ------------------------------------------------ |
| `/ui-builder`          | List all pages with create, edit, delete actions |
| `/ui-builder/new`      | Create a new page with the visual builder        |
| `/ui-builder/:id/edit` | Edit an existing page                            |

<Callout type="warn">
  Admin routes are automatically set to `noindex` for SEO. Don't include them in your public sitemap.
</Callout>

### Page Component Overrides

You can replace any built-in admin page with your own React component using the optional `pageComponents` field in `uiBuilderClientPlugin(config)`. The built-in component is used as the fallback whenever an override is not provided, so this is fully backward-compatible.

```tsx
uiBuilderClientPlugin({
  // ... other config
  pageComponents: {
    // Replace the page list page
    pageList: MyCustomPageList,
    // Replace the new page builder page
    newPage: MyCustomNewPage,
    // Replace the edit page builder page — receives id as a prop
    editPage: ({ id }) => <MyCustomPageBuilder id={id} />,
  },
})
```

## Component Registry

The UI Builder uses a component registry to define available components. A default registry is provided with common components:

### Default Components

**Primitives:**

* `div`, `span`, `p`, `h1`-`h6` - HTML elements
* `a` - Anchor links
* `img` - Images
* `iframe` - Embedded content

**Layout Components:**

* `Flexbox` - Flexible box layout
* `Grid` - CSS Grid layout

**Content Components:**

* `Markdown` - Rich text with Markdown support
* `Icon` - Lucide icons
* `CodePanel` - Syntax-highlighted code blocks

**shadcn/ui Components:**

* `Button` - Interactive buttons
* `Badge` - Status badges
* `Card`, `CardHeader`, `CardTitle`, `CardContent`, `CardFooter` - Card layouts
* `Accordion`, `AccordionItem`, `AccordionTrigger`, `AccordionContent` - Collapsible sections
* `Separator` - Visual separators
* `Carousel`, `CarouselItem` - Image/content carousels

### Custom Component Registry

Extend or replace the default registry with your own components:

```tsx
import { 
  createComponentRegistry, 
  defaultComponentRegistry,
  primitiveComponentDefinitions,
} from "@btst/stack/plugins/ui-builder/client"
import { z } from "zod"

// Extend the default registry
const customRegistry = createComponentRegistry({
  ...defaultComponentRegistry,
  
  // Add a custom component
  HeroSection: {
    component: HeroSection,
    schema: z.object({
      title: z.string().default("Welcome"),
      subtitle: z.string().optional(),
      backgroundImage: z.string().optional(),
      ctaText: z.string().default("Get Started"),
      ctaLink: z.string().default("#"),
    }),
    from: "@/components/hero-section",
  },
  
  // Add a pricing card
  PricingCard: {
    component: PricingCard,
    schema: z.object({
      plan: z.string(),
      price: z.string(),
      features: z.array(z.string()).default([]),
      highlighted: z.boolean().default(false),
    }),
    from: "@/components/pricing-card",
  },
})

// Use in client plugin
uiBuilderClientPlugin({
  // ...
  componentRegistry: customRegistry,
})
```

### Registry Entry Properties

Each component in the registry has these properties:

| Property                  | Type                                  | Required | Description                                            |
| ------------------------- | ------------------------------------- | -------- | ------------------------------------------------------ |
| `component`               | `ComponentType`                       | No       | The React component (optional for primitives)          |
| `schema`                  | `ZodSchema`                           | Yes      | Zod schema defining props                              |
| `from`                    | `string`                              | No       | Import path for code generation                        |
| `isFromDefaultExport`     | `boolean`                             | No       | Whether component is default export                    |
| `defaultChildren`         | `ComponentLayer[] \| string`          | No       | Default children when added                            |
| `defaultVariableBindings` | `DefaultVariableBinding[]`            | No       | Auto-bind props to variables                           |
| `fieldOverrides`          | `Record<string, FieldConfigFunction>` | No       | Custom form field renderers                            |
| `childOf`                 | `string[]`                            | No       | Restrict which parent types can contain this component |

### Parent-Child Restrictions

Use the `childOf` property to restrict where a component can be placed:

```tsx
const registry = createComponentRegistry({
  ...defaultComponentRegistry,
  
  // TabsTrigger can only be added inside TabsList
  TabsTrigger: {
    component: TabsTrigger,
    schema: z.object({
      value: z.string(),
      children: z.any(),
    }),
    childOf: ["TabsList"], // Can only be a child of TabsList
  },
  
  // CarouselItem can only be inside Carousel
  CarouselItem: {
    component: CarouselItem,
    schema: z.object({
      children: z.any(),
    }),
    childOf: ["Carousel"],
  },
})
```

### Minimal Registry

Create a minimal registry with only the components you need:

```tsx
const minimalRegistry = createComponentRegistry({
  div: primitiveComponentDefinitions.div,
  span: primitiveComponentDefinitions.span,
  Flexbox: complexComponentDefinitions.Flexbox,
  Button: complexComponentDefinitions.Button,
})
```

## Block Registry

Blocks are pre-built component compositions that users can insert as templates. They appear in the "Blocks" tab of the add component popover.

### Defining Blocks

Create a block registry with reusable templates:

```tsx
import type { BlockRegistry, ComponentLayer } from "@btst/stack/components/ui-builder"

const myBlocks: BlockRegistry = {
  "hero-01": {
    name: "hero-01",
    category: "hero",
    description: "Hero section with title, subtitle, and CTA button",
    thumbnail: "/blocks/hero-01.png", // Optional preview image
    template: {
      id: "hero-root",
      type: "Flexbox",
      name: "Hero Section",
      props: {
        className: "min-h-[60vh] items-center justify-center bg-gradient-to-b from-primary/10 to-background",
        direction: "column",
        gap: 4,
      },
      children: [
        {
          id: "hero-title",
          type: "h1",
          name: "Title",
          props: { className: "text-5xl font-bold text-center" },
          children: "Welcome to Our Platform",
        },
        {
          id: "hero-subtitle",
          type: "p",
          name: "Subtitle",
          props: { className: "text-xl text-muted-foreground text-center max-w-2xl" },
          children: "Build amazing experiences with our powerful tools",
        },
        {
          id: "hero-cta",
          type: "Button",
          name: "CTA Button",
          props: { variant: "default", size: "lg" },
          children: [
            { id: "cta-text", type: "span", name: "Button Text", props: {}, children: "Get Started" }
          ],
        },
      ],
    },
  },
  "pricing-01": {
    name: "pricing-01",
    category: "pricing",
    description: "Simple pricing card",
    template: {
      id: "pricing-root",
      type: "Card",
      name: "Pricing Card",
      props: { className: "w-full max-w-sm" },
      children: [
        {
          id: "pricing-header",
          type: "CardHeader",
          name: "Header",
          props: {},
          children: [
            { id: "plan-name", type: "CardTitle", name: "Plan", props: {}, children: [
              { id: "plan-text", type: "span", name: "Plan Text", props: {}, children: "Pro" }
            ]},
            { id: "plan-desc", type: "CardDescription", name: "Description", props: {}, children: [
              { id: "desc-text", type: "span", name: "Description Text", props: {}, children: "For professionals" }
            ]},
          ],
        },
        {
          id: "pricing-content",
          type: "CardContent",
          name: "Content",
          props: {},
          children: [
            { id: "price", type: "p", name: "Price", props: { className: "text-4xl font-bold" }, children: "$29/mo" },
          ],
        },
      ],
    },
  },
}
```

### Using Blocks in UIBuilder

Pass the block registry to the UIBuilder component:

```tsx
import { UIBuilder, defaultComponentRegistry } from "@btst/stack/components/ui-builder"

function PageEditor() {
  return (
    <UIBuilder
      componentRegistry={defaultComponentRegistry}
      blocks={myBlocks}
      initialLayers={[]}
      onChange={(layers) => console.log("Layers changed:", layers)}
    />
  )
}
```

### BlockDefinition Properties

| Property             | Type             | Required | Description                                              |
| -------------------- | ---------------- | -------- | -------------------------------------------------------- |
| `name`               | `string`         | Yes      | Unique block identifier, e.g., "hero-01"                 |
| `category`           | `string`         | Yes      | Category for grouping, e.g., "hero", "pricing", "footer" |
| `description`        | `string`         | No       | Human-readable description shown in UI                   |
| `template`           | `ComponentLayer` | Yes      | The component tree to insert                             |
| `thumbnail`          | `string`         | No       | Preview image URL                                        |
| `requiredComponents` | `string[]`       | No       | List of required component types                         |

<Callout type="info">
  Blocks appear in a separate "Blocks" tab in the add component popover, organized by category. Users can insert entire pre-built sections with a single click.
</Callout>

## Public Page Rendering

The UI Builder provides multiple ways to render pages on public routes, depending on your needs:

| Component             | Use Case                                          | Server Component Compatible |
| --------------------- | ------------------------------------------------- | --------------------------- |
| `PageRenderer`        | Client-side rendering with built-in data fetching | No (requires "use client")  |
| `LayerRenderer`       | Render pre-fetched layer data on the client       | No (requires "use client")  |
| `ServerLayerRenderer` | SSR/RSC rendering of layer data                   | Yes                         |

### PageRenderer (Client Component)

The `PageRenderer` component fetches and renders UI Builder pages by slug:

```tsx title="app/preview/[slug]/page.tsx"
"use client"

import { PageRenderer } from "@btst/stack/plugins/ui-builder/client"

export default function PreviewPage({ params }: { params: { slug: string } }) {
  return (
    <PageRenderer
      slug={params.slug}
      className="min-h-screen"
    />
  )
}
```

#### PageRenderer Props

| Prop                | Type                       | Description                           |
| ------------------- | -------------------------- | ------------------------------------- |
| `slug`              | `string`                   | Page slug to fetch and render         |
| `componentRegistry` | `ComponentRegistry`        | Custom registry (defaults to default) |
| `variableValues`    | `Record<string, any>`      | Runtime variable values               |
| `LoadingComponent`  | `ComponentType`            | Custom loading state                  |
| `ErrorComponent`    | `ComponentType<{ error }>` | Custom error state                    |
| `NotFoundComponent` | `ComponentType`            | Custom 404 state                      |
| `className`         | `string`                   | Additional CSS classes                |

### LayerRenderer (Client Component)

The `LayerRenderer` component renders pre-fetched ComponentLayer data. Use this when you've already fetched the page data and want more control:

```tsx title="app/pages/[slug]/page.tsx"
"use client"

import { LayerRenderer, defaultComponentRegistry } from "@btst/stack/components/ui-builder"

export default function DynamicPage({ page, variables }: { 
  page: ComponentLayer, 
  variables: Variable[] 
}) {
  return (
    <LayerRenderer
      page={page}
      componentRegistry={defaultComponentRegistry}
      variables={variables}
      variableValues={{
        userName: "John Doe",
      }}
      className="min-h-screen"
    />
  )
}
```

#### LayerRenderer Props

| Prop                | Type                        | Required | Description                          |
| ------------------- | --------------------------- | -------- | ------------------------------------ |
| `page`              | `ComponentLayer`            | Yes      | The root ComponentLayer to render    |
| `componentRegistry` | `ComponentRegistry`         | Yes      | Component definitions registry       |
| `variables`         | `Variable[]`                | No       | Variable definitions from the page   |
| `variableValues`    | `Record<string, PropValue>` | No       | Runtime values for variables         |
| `editorConfig`      | `EditorConfig`              | No       | Editor configuration (for admin use) |
| `className`         | `string`                    | No       | Additional CSS classes               |

### ServerLayerRenderer (Server Component)

The `ServerLayerRenderer` is an SSR-friendly renderer that works in React Server Components (RSC), Static Site Generation (SSG), and Server-Side Rendering (SSR):

```tsx title="app/pages/[slug]/page.tsx"
// No "use client" needed - this is a Server Component
import { ServerLayerRenderer, defaultComponentRegistry } from "@btst/stack/components/ui-builder"

export default async function StaticPage({ params }: { params: { slug: string } }) {
  // Fetch page data on the server
  const page = await fetchPageFromDatabase(params.slug)
  
  if (!page) {
    return <NotFound />
  }
  
  const layers = JSON.parse(page.parsedData.layers)
  const variables = JSON.parse(page.parsedData.variables)
  
  return (
    <ServerLayerRenderer
      page={layers[0]}
      componentRegistry={defaultComponentRegistry}
      variables={variables}
      variableValues={{
        // Pass any runtime values
        currentYear: new Date().getFullYear(),
      }}
      className="min-h-screen"
    />
  )
}
```

#### ServerLayerRenderer Props

| Prop                | Type                        | Required | Description                        |
| ------------------- | --------------------------- | -------- | ---------------------------------- |
| `page`              | `ComponentLayer`            | Yes      | The root ComponentLayer to render  |
| `componentRegistry` | `ComponentRegistry`         | Yes      | Component definitions registry     |
| `variables`         | `Variable[]`                | No       | Variable definitions from the page |
| `variableValues`    | `Record<string, PropValue>` | No       | Runtime values for variables       |
| `className`         | `string`                    | No       | Additional CSS classes             |

<Callout type="info">
  **When to use ServerLayerRenderer:**

  * Static pages that can be rendered at build time (SSG)
  * SEO-critical pages that need server-side rendering
  * Pages where you want to avoid client-side JavaScript for the initial render
  * When using React Server Components in Next.js App Router

  **When to use LayerRenderer:**

  * Pages with interactive editor features
  * When you need client-side state management
  * Pages that require client-side data fetching
</Callout>

### With Variable Values

Pass runtime values to page variables:

```tsx
import { PageRenderer } from "@btst/stack/plugins/ui-builder/client"

export default function UserPage({ params }: { params: { slug: string } }) {
  const user = useCurrentUser()
  
  return (
    <PageRenderer
      slug={params.slug}
      variableValues={{
        userName: user?.name ?? "Guest",
        userEmail: user?.email,
        isLoggedIn: !!user,
      }}
    />
  )
}
```

### SSR with Suspense

For server-side rendering with streaming:

````tsx
import { Suspense } from "react"
import { SuspensePageRenderer } from "@btst/stack/plugins/ui-builder/client"

export default function Page({ params }: { params: { slug: string } }) {
  return (
    <Suspense fallback={<PageSkeleton />}>
      <SuspensePageRenderer slug={params.slug} />
    </Suspense>
  )
}

## Client Hooks

Access UI Builder data with React Query hooks:

### Available Hooks

| Hook | Description | Returns |
|------|-------------|---------|
| `useUIBuilderPages()` | List all pages | `{ pages, total, isLoading, loadMore, hasMore }` |
| `useSuspenseUIBuilderPages()` | Suspense variant | `{ pages, total, loadMore, hasMore }` |
| `useUIBuilderPage(id)` | Get page by ID | `{ page, isLoading, error }` |
| `useUIBuilderPageBySlug(slug)` | Get page by slug | `{ page, layers, variables, isLoading }` |
| `useCreateUIBuilderPage()` | Create mutation | React Query mutation |
| `useUpdateUIBuilderPage()` | Update mutation | React Query mutation |
| `useDeleteUIBuilderPage()` | Delete mutation | React Query mutation |

### Usage Examples

```tsx
import { 
  useUIBuilderPageBySlug,
  useCreateUIBuilderPage,
  useUIBuilderPages 
} from "@btst/stack/plugins/ui-builder/client"

// Public: Fetch page by slug
function DynamicPage({ slug }: { slug: string }) {
  const { page, layers, variables, isLoading } = useUIBuilderPageBySlug(slug)
  
  if (isLoading || !page) return <Loading />
  
  return (
    <LayerRenderer
      page={layers[0]}
      componentRegistry={defaultComponentRegistry}
      variables={variables}
    />
  )
}

// Admin: Create new page
function CreatePage() {
  const createPage = useCreateUIBuilderPage()
  
  const handleCreate = async () => {
    await createPage.mutateAsync({
      slug: "my-new-page",
      layers: [
        {
          id: "root",
          type: "div",
          name: "Page Root",
          props: { className: "min-h-screen p-8" },
          children: [],
        }
      ],
      status: "draft",
    })
  }
  
  return <Button onClick={handleCreate}>Create Page</Button>
}
````

## SSR Authorization Hooks

Use hooks in the client plugin config for async authorization during SSR:

```tsx title="lib/stack-client.tsx"
import { redirect } from "next/navigation"

"ui-builder": uiBuilderClientPlugin({
  // ... config
  hooks: {
    beforeLoadPageList: async (context) => {
      // context.headers contains request headers
      const session = await getSession(context.headers)
      if (session?.user?.isAdmin !== true)
        throw new Error("Admin access required")
    },
    beforeLoadPageBuilder: async (pageId, context) => {
      // pageId is undefined for new pages
      const session = await getSession(context.headers)
      if (session?.user?.isAdmin !== true)
        throw new Error("Admin access required")
    },
    afterLoadPageList: async (context) => {
      console.log("Page list loaded")
    },
    afterLoadPageBuilder: async (pageId, context) => {
      console.log("Page builder loaded for:", pageId)
    },
    onLoadError: (error, context) => {
      // Redirect on authorization failure
      redirect("/auth/sign-in")
    },
  },
})
```

### UIBuilderClientHooks

| Hook                    | Parameters        | Return                  | Description                            |
| ----------------------- | ----------------- | ----------------------- | -------------------------------------- |
| `beforeLoadPageList`    | `context`         | `void \| Promise<void>` | SSR auth for page list — throw to deny |
| `afterLoadPageList`     | `context`         | `void`                  | Post-load lifecycle                    |
| `beforeLoadPageBuilder` | `pageId, context` | `void \| Promise<void>` | SSR auth for builder — throw to deny   |
| `afterLoadPageBuilder`  | `pageId, context` | `void`                  | Post-load lifecycle                    |
| `onLoadError`           | `error, context`  | `void`                  | Handle auth failures                   |

### LoaderContext

All hooks receive a context object:

| Property      | Type                     | Description               |
| ------------- | ------------------------ | ------------------------- |
| `path`        | `string`                 | Current route path        |
| `params`      | `Record<string, string>` | Route parameters          |
| `isSSR`       | `boolean`                | Whether running on server |
| `apiBaseURL`  | `string`                 | API base URL              |
| `apiBasePath` | `string`                 | API path prefix           |
| `headers`     | `Headers \| undefined`   | Request headers           |

## Page Data Structure

UI Builder pages are stored with this structure:

```ts
interface UIBuilderPage {
  id: string
  slug: string              // URL-friendly identifier
  parsedData: {
    layers: string          // JSON-serialized ComponentLayer[]
    variables: string       // JSON-serialized Variable[]
    status: "published" | "draft" | "archived"
  }
  createdAt: string
  updatedAt: string
}

interface ComponentLayer {
  id: string
  type: string              // Component type from registry
  name?: string             // Display name in layers panel
  props: Record<string, any>
  children: ComponentLayer[] | string | VariableReference
}

interface Variable {
  id: string
  name: string
  type: "string" | "number" | "boolean" | "function"
  defaultValue: any
}

// Variable reference for dynamic content
interface VariableReference {
  __variableRef: string     // Variable ID
}
```

### Variable References

You can bind component children to variables for dynamic content:

```ts
const layer: ComponentLayer = {
  id: "greeting",
  type: "h1",
  name: "Greeting",
  props: { className: "text-2xl font-bold" },
  // Children bound to a variable
  children: { __variableRef: "userName" }
}

const variables: Variable[] = [
  { id: "userName", name: "User Name", type: "string", defaultValue: "Guest" }
]
```

When rendering, pass runtime values to override defaults:

```tsx
<PageRenderer
  slug="welcome"
  variableValues={{ userName: "John Doe" }}
/>
```

## API Reference

### Backend (`@btst/stack/plugins/ui-builder`)

#### UI\_BUILDER\_CONTENT\_TYPE

Pre-configured content type for UI Builder pages. Add to your CMS config:

```ts
import { UI_BUILDER_CONTENT_TYPE } from "@btst/stack/plugins/ui-builder"

cms: cmsBackendPlugin({
  contentTypes: [UI_BUILDER_CONTENT_TYPE]
})
```

### Client (`@btst/stack/plugins/ui-builder/client`)

#### uiBuilderClientPlugin

Creates the client plugin with routes and SSR loaders.

#### UIBuilderPluginOverrides

| Property            | Type                     | Required | Description               |
| ------------------- | ------------------------ | -------- | ------------------------- |
| `apiBaseURL`        | `string`                 | Yes      | Base URL for API requests |
| `apiBasePath`       | `string`                 | Yes      | API path prefix           |
| `navigate`          | `(path: string) => void` | Yes      | Navigation function       |
| `Link`              | `ComponentType`          | No       | Link component            |
| `refresh`           | `() => void`             | No       | Refresh function          |
| `componentRegistry` | `ComponentRegistry`      | No       | Custom component registry |
| `showAttribution`   | `boolean`                | No       | Show BTST attribution     |

#### defaultComponentRegistry

The default component registry with primitives and shadcn/ui components.

#### createComponentRegistry

Helper function to create a type-safe component registry:

```ts
const registry = createComponentRegistry({
  ...defaultComponentRegistry,
  CustomComponent: { component: CustomComponent, schema: customSchema },
})
```

#### UIBuilder

The main visual editor component. Import from `@btst/stack/components/ui-builder`:

```tsx
import { UIBuilder } from "@btst/stack/components/ui-builder"

<UIBuilder
  componentRegistry={myRegistry}
  blocks={myBlocks}
  functionRegistry={myFunctionRegistry}
  initialLayers={initialLayers}
  initialVariables={initialVariables}
  onChange={(layers) => saveLayers(layers)}
  onVariablesChange={(variables) => saveVariables(variables)}
  allowPagesCreation={true}
  allowPagesDeletion={true}
  allowVariableEditing={true}
  persistLayerStore={false}
  showExport={true}
  navLeftChildren={<Logo />}
  navRightChildren={<SaveButton />}
/>
```

##### UIBuilder Props

| Prop                   | Type                                 | Required | Default | Description                                       |
| ---------------------- | ------------------------------------ | -------- | ------- | ------------------------------------------------- |
| `componentRegistry`    | `ComponentRegistry`                  | Yes      | -       | Registry of available components                  |
| `blocks`               | `BlockRegistry`                      | No       | -       | Pre-built block templates for the Blocks tab      |
| `functionRegistry`     | `FunctionRegistry`                   | No       | -       | Bindable event handlers (onClick, onSubmit, etc.) |
| `initialLayers`        | `ComponentLayer[]`                   | No       | -       | Initial layer tree to load                        |
| `initialVariables`     | `Variable[]`                         | No       | -       | Initial variables to load                         |
| `onChange`             | `(layers: ComponentLayer[]) => void` | No       | -       | Callback when layers change                       |
| `onVariablesChange`    | `(variables: Variable[]) => void`    | No       | -       | Callback when variables change                    |
| `persistLayerStore`    | `boolean`                            | No       | `true`  | Persist layers to localStorage                    |
| `allowVariableEditing` | `boolean`                            | No       | `true`  | Show variables panel                              |
| `allowPagesCreation`   | `boolean`                            | No       | `true`  | Allow creating new pages                          |
| `allowPagesDeletion`   | `boolean`                            | No       | `true`  | Allow deleting pages                              |
| `showExport`           | `boolean`                            | No       | `true`  | Show export button in navbar                      |
| `navLeftChildren`      | `ReactNode`                          | No       | -       | Content for left side of navbar                   |
| `navRightChildren`     | `ReactNode`                          | No       | -       | Content for right side of navbar                  |
| `panelConfig`          | `PanelConfig`                        | No       | -       | Custom panel configuration                        |

#### PageRenderer

Component to render UI Builder pages on public routes (client component):

```tsx
<PageRenderer
  slug="homepage"
  componentRegistry={customRegistry}
  variableValues={{ userName: "John" }}
/>
```

#### LayerRenderer

Component to render pre-fetched ComponentLayer data (client component):

```tsx
import { LayerRenderer } from "@btst/stack/components/ui-builder"

<LayerRenderer
  page={rootLayer}
  componentRegistry={customRegistry}
  variables={variables}
  variableValues={{ userName: "John" }}
/>
```

#### ServerLayerRenderer

SSR-friendly renderer for React Server Components:

```tsx
import { ServerLayerRenderer } from "@btst/stack/components/ui-builder"

// In a Server Component (no "use client" needed)
<ServerLayerRenderer
  page={rootLayer}
  componentRegistry={customRegistry}
  variables={variables}
  variableValues={{ currentYear: 2024 }}
/>
```

### Types (`@btst/stack/components/ui-builder`)

#### BlockDefinition

Pre-built component compositions for templates:

```ts
interface BlockDefinition {
  name: string           // Unique block name, e.g., "login-01"
  category: string       // Block category, e.g., "login", "sidebar"
  description?: string   // Human-readable description
  template: ComponentLayer  // ComponentLayer tree to insert
  thumbnail?: string     // Optional preview image URL
  requiredComponents?: string[]  // Required shadcn components
}
```

#### BlockRegistry

A record of block name to block definition:

```ts
type BlockRegistry = Record<string, BlockDefinition>
```

#### FunctionDefinition

Defines a callable function that can be bound to component event handlers via the function registry:

```ts
interface FunctionDefinition {
  name: string                // Human-readable name
  schema: ZodTuple | ZodObject | ZodSchema  // Parameter schema
  fn: (...args: any[]) => any // The actual function
  description?: string        // Description shown in UI
  typeSignature?: string      // TS type signature for code generation
}
```

#### FunctionRegistry

A record of function ID to function definition:

```ts
type FunctionRegistry = Record<string, FunctionDefinition>
```

Variables with `type: "function"` reference a key in the `FunctionRegistry`. At runtime, the function is resolved and bound to the component prop (e.g. `onClick`, `onSubmit`).

```tsx
import { z } from "zod"

const functionRegistry: FunctionRegistry = {
  handleSubmit: {
    name: "Handle Submit",
    description: "Process form submission",
    schema: z.tuple([z.custom<React.FormEvent<HTMLFormElement>>()]),
    fn: (e) => { e.preventDefault(); console.log("submitted") },
    typeSignature: "(e: React.FormEvent<HTMLFormElement>) => void",
  },
}

<UIBuilder
  componentRegistry={myRegistry}
  functionRegistry={functionRegistry}
  // ...
/>
```

#### ComponentLayer

The structure representing a component in the UI Builder tree:

```ts
interface ComponentLayer {
  id: string
  type: string                          // Component type from registry
  name?: string                         // Display name in layers panel
  props: Record<string, PropValue>
  children: ComponentLayer[] | string | VariableReference
}
```

#### Variable

Variable definition for dynamic content:

```ts
interface Variable {
  id: string
  name: string
  type: "string" | "number" | "boolean" | "function"
  defaultValue: any
}
```

#### VariableReference

Reference to a variable for dynamic binding:

```ts
interface VariableReference {
  __variableRef: string  // Variable ID
}
```

## Shadcn Registry

The UI Builder plugin UI layer is distributed as a [shadcn registry](https://ui.shadcn.com/docs/registry) block. Use the registry to **eject and fully customize** the page components while keeping all data-fetching and API logic from `@btst/stack`.

<Callout type="info">
  The registry installs only the view layer. Hooks and data-fetching continue to come from `@btst/stack/plugins/ui-builder/client/hooks`.
</Callout>

<Tabs items={["npx", "pnpm", "bunx"]}>
  <Tab value="npx">
    ```bash
    npx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json
    ```
  </Tab>

  <Tab value="pnpm">
    ```bash
    pnpx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json
    ```
  </Tab>

  <Tab value="bunx">
    ```bash
    bunx shadcn@latest add https://github.com/better-stack-ai/better-stack/blob/main/packages/stack/registry/btst-ui-builder.json
    ```
  </Tab>
</Tabs>

This copies the page components into `src/components/btst/ui-builder/client/` in your project. All relative imports remain valid and you can edit the files freely — the plugin's data layer stays intact.

### Using ejected components

After installing, wire your custom components into the plugin via the `pageComponents` option in your client plugin config:

```tsx title="lib/stack-client.tsx"
import { uiBuilderClientPlugin } from "@btst/stack/plugins/ui-builder/client"
// Import your ejected (and customized) page components
import { PageListPageComponent } from "@/components/btst/ui-builder/client/components/pages/page-list-page"
import { EditPagePageComponent } from "@/components/btst/ui-builder/client/components/pages/edit-page-page"

uiBuilderClientPlugin({
  apiBaseURL: "...",
  apiBasePath: "/api/data",
  queryClient,
  pageComponents: {
    pageList: PageListPageComponent,   // replaces the page list page
    editPage: EditPagePageComponent,   // replaces the page builder editor
    // newPage — omit to keep built-in default
  },
})
```

Any key you omit falls back to the built-in default, so you can override just the pages you want to change.
