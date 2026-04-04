# Source: https://docs.turso.tech/sdk/ts/guides/nextjs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.turso.tech/llms.txt
> Use this file to discover all available pages before exploring further.

# Next.js + Turso

> Set up Turso in your Next.js project in minutes.

<img src="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=70fd7aa0941f6871ae5e4a2eb3292cce" alt="Next.js banner" data-og-width="1133" width="1133" data-og-height="595" height="595" data-path="images/guides/nextjs-banner.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=280&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3ec3bc230f1a419c2fe1e76226f1c53e 280w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=560&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3aea7655fd4bd73d0184f940cf81ea73 560w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=840&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=27acb905210e1ffbb4af5741a6a786b1 840w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=1100&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=f47b1f24678b02ea31781bdfa12656fb 1100w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=1650&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=3bee8f44381437fa9c6a5e09b4832a5c 1650w, https://mintcdn.com/turso/7mjM7fXIfeZ8ZwNC/images/guides/nextjs-banner.png?w=2500&fit=max&auto=format&n=7mjM7fXIfeZ8ZwNC&q=85&s=9a6aa8d84b587b5a3887c2b1760bc23b 2500w" />

## Prerequisites

Before you start, make sure you:

* [Install the Turso CLI](/cli/installation)
* [Sign up or login to Turso](/cli/authentication#signup)
* Have a Next.js app — [learn more](https://nextjs.org/docs/getting-started/installation)

<Steps>
  <Step title="Install the libSQL SDK">
    <Snippet file="install-libsql-client-ts.mdx" />
  </Step>

  <Step title="Configure database credentials">
    <Snippet file="retrieve-database-credentials.mdx" />
  </Step>

  <Step title="Configure libSQL client">
    <Snippet file="configure-libsql-client-ts.mdx" />
  </Step>

  <Step title="Execute SQL">
    <CodeGroup>
      ```tsx App Router theme={null}
      import { turso } from "@/lib/turso";

      export default async function Page() {
        const { rows } = await turso.execute("SELECT * FROM table_name");

        return (
          <ul>
            {rows.map((row) => (
              <li key={row.id}>{row.id}</li>
            ))}
          </ul>
        );
      }
      ```

      ```ts Pages Directory theme={null}
      import type { InferGetServerSidePropsType, GetServerSideProps } from "next";

      import { turso } from "@/lib/turso";

      export const getServerSideProps = (async () => {
        const { rows } = await turso.execute("SELECT * FROM table_name");

        return {
          props: {
            rows,
          },
        };
      }) satisfies GetServerSideProps<{ rows: any[] }>;

      export default function Page({
        rows,
      }: InferGetServerSidePropsType<typeof getServerSideProps>) {
        return (
          <ul>
            {rows.map((row) => (
              <li key={row.id}>{row.id}</li>
            ))}
          </ul>
        );
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Examples

<CardGroup cols={2}>
  <Card title="Full Stack App" icon="github" href="https://github.com/tursodatabase/nextjs-turso-starter">
    Build with Next.js, Turso, and Drizzle ORM.
  </Card>
</CardGroup>
