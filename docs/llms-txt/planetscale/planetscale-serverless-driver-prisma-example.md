# Source: https://planetscale.com/docs/vitess/tutorials/planetscale-serverless-driver-prisma-example.md

# Using the PlanetScale serverless driver with Prisma

> This document outlines how you can use the [PlanetScale serverless driver](/docs/vitess/tutorials/planetscale-serverless-driver) along with Prisma in your application.

## Set up

To get started:

<Steps>
  <Step>
    Install the Prisma driver adapter for PlanetScale (`@prisma/adapter-planetscale`), PlanetScale serverless driver (`@planetscale/database`), and `undici` packages:

    ```shell  theme={null}
    npm install @prisma/adapter-planetscale @planetscale/database undici
    ```

    <Note>
      When using an older version of Node.js, you can provide a custom fetch function implementation. We recommend the `undici` package on which Node's built-in fetch is based. Node.js version 18 includes a built-in global `fetch` function.
    </Note>
  </Step>

  <Step>
    Enable the `driverAdapters` Preview feature flag:

    ```javascript  theme={null}
    // schema.prisma
    generator client {
      provider        = "prisma-client-js"
      previewFeatures = ["driverAdapters"]
    }

    datasource db {
      provider     = "mysql"
      url          = env("DATABASE_URL")
      relationMode = "prisma"
    }
    ```

    <Note>
      Ensure you update the host value in your connection string to `aws.connect.psdb.cloud`. You can learn more about this [here](/docs/vitess/tutorials/planetscale-serverless-driver#add-and-use-the-planetscale-serverless-driver-for-javascript-to-your-project).
    </Note>
  </Step>

  <Step>
    Generate Prisma Client:

    ```shell  theme={null}
    npx prisma generate
    ```
  </Step>

  <Step>
    Update your Prisma Client instance to use the PlanetScale serverless driver:

    ```javascript expandable theme={null}
    import { Client } from '@planetscale/database'
    import { PrismaPlanetScale } from '@prisma/adapter-planetscale'
    import { PrismaClient } from '@prisma/client'
    import dotenv from 'dotenv'
    import { fetch as undiciFetch } from 'undici'

    dotenv.config()
    const connectionString = `${process.env.DATABASE_URL}`

    const client = new Client({ url: connectionString, fetch: undiciFetch })
    const adapter = new PrismaPlanetScale(client)
    const prisma = new PrismaClient({ adapter })

    async function main() {
      const posts = await prisma.post.findMany()
      console.log(posts)
    }
    ```
  </Step>
</Steps>

You can then use Prisma Client as you usually would with auto-completion and full type-safety.

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt