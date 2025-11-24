# Source: https://trigger.dev/docs/guides/frameworks/sequin.md

# Sequin database triggers

> This guide will show you how to trigger tasks from database changes using Sequin

[Sequin](https://sequinstream.com) allows you to trigger tasks from database changes. Sequin captures every insert, update, and delete on a table and then ensures a task is triggered for each change.

Often, task runs coincide with database changes. For instance, you might want to use a Trigger.dev task to generate an embedding for each post in your database:

<img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2b47f798eae889e5ae4273368ee9cdc1" alt="Sequin and Trigger.dev Overview" data-og-width="1773" width="1773" data-og-height="492" height="492" data-path="images/sequin-intro.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=9c9196f7d3a2a2a9fdf874702460c059 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ce2fe0003447192821d6ddafe872ffe8 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f1bfbbc8c685ff84061f57d0a0312aca 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=51d4acaeaa75050b0327cd77220ca814 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8320b585fc6fb4446a46f3c2913fc831 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-intro.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e533eec55e2c3ae56d5a99bcb6bbd7db 2500w" />

In this guide, you'll learn how to use Sequin to trigger Trigger.dev tasks from database changes.

## Prerequisites

You are about to create a [regular Trigger.dev task](/tasks-regular) that you will execute when ever a post is inserted or updated in your database. Sequin will detect all the changes on the `posts` table and then send the payload of the post to an API endpoint that will call `tasks.trigger()` to create the embedding and update the database.

As long as you create an HTTP endpoint that Sequin can deliver webhooks to, you can use any web framework or edge function (e.g. Supabase Edge Functions, Vercel Functions, Cloudflare Workers, etc.) to invoke your Trigger.dev task. In this guide, we'll show you how to setup Trigger.dev tasks using Next.js API Routes.

You'll need the following to follow this guide:

* A Next.js project with [Trigger.dev](https://trigger.dev) installed
  <Info>
    If you don't have one already, follow [Trigger.dev's Next.js setup
    guide](/guides/frameworks/nextjs) to setup your project. You can return to this guide when
    you're ready to write your first Trigger.dev task.
  </Info>
* A [Sequin](https://console.sequinstream.com/register) account
* A Postgres database (Sequin works with any Postgres database version 12 and up) with a `posts` table.

## Create a Trigger.dev task

Start by creating a new Trigger.dev task that takes in a Sequin change event as a payload, creates an embedding, and then inserts the embedding into the database:

<Steps titleSize="h3">
  <Step title="Create a `create-embedding-for-post` task">
    In your `src/trigger/tasks` directory, create a new file called `create-embedding-for-post.ts` and add the following code:

    <CodeGroup>
      ```ts trigger/create-embedding-for-post.ts theme={null}
      import { task } from "@trigger.dev/sdk";
      import { OpenAI } from "openai";
      import { upsertEmbedding } from "../util";

      const openai = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
      });

      export const createEmbeddingForPost = task({
      id: "create-embedding-for-post",
      run: async (payload: {
      record: {
      id: number;
      title: string;
      body: string;
      author: string;
      createdAt: string;
      embedding: string | null;
      },
      metadata: {
      table_schema: string,
      table_name: string,
      consumer: {
      id: string;
      name: string;
      };
      };
      }) => {
      // Create an embedding using the title and body of payload.record
      const content = `${payload.record.title}\n\n${payload.record.body}`;
      const embedding = (await openai.embeddings.create({
      model: "text-embedding-ada-002",
      input: content,
      })).data[0].embedding;

          // Upsert the embedding in the database. See utils.ts for the implementation -> ->
          await upsertEmbedding(embedding, payload.record.id);

          // Return the updated record
          return {
            ...payload.record,
            embedding: JSON.stringify(embedding),
          };
        }

      });

      ```

      ```ts utils.ts theme={null}
      import pg from "pg";

      export async function upsertEmbedding(embedding: number[], id: number) {
        const client = new pg.Client({
          connectionString: process.env.DATABASE_URL,
        });
        await client.connect();

        try {
          const query = `
            INSERT INTO post_embeddings (id, embedding)
            VALUES ($2, $1)
            ON CONFLICT (id)
            DO UPDATE SET embedding = $1
          `;
          const values = [JSON.stringify(embedding), id];

          const result = await client.query(query, values);
          console.log(`Updated record in database. Rows affected: ${result.rowCount}`);

          return result.rowCount;
        } catch (error) {
          console.error("Error updating record in database:", error);
          throw error;
        } finally {
          await client.end();
        }
      }
      ```
    </CodeGroup>

    This task takes in a Sequin record event, creates an embedding, and then upserts the embedding into a `post_embeddings` table.
  </Step>

  <Step title="Add the task to your Trigger.dev project">
    Register the `create-embedding-for-post` task to your Trigger.dev cloud project by running the following command:

    ```bash  theme={null}
    npx trigger.dev@latest dev
    ```

    In the Trigger.dev dashboard, you should now see the `create-embedding-for-post` task:

    <Frame>
      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=747c6f96abca5112fb406fe215e0b587" alt="Task added" data-og-width="2834" width="2834" data-og-height="482" height="482" data-path="images/sequin-register-task.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a641edafb2f279adabeb241452f97a2a 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=fea53dc47cd6fe8aa9ced24df43afa91 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=8569ed20a7843f45bd41a49062dccaaa 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f2377811f9fa930b91335a61dfe6a107 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=726d52318e2994eee969ef6f6f17dc5c 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-register-task.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2c3fd7773430f2d99da46e8de7a94dd1 2500w" />
    </Frame>
  </Step>
</Steps>

<Check>
  You've successfully created a Trigger.dev task that will create an embedding for each post in your
  database. In the next step, you'll create an API endpoint that Sequin can deliver records to.
</Check>

## Setup API route

You'll now create an API endpoint that will receive posts from Sequin and then trigger the `create-embedding-for-post` task.

<Info>
  This guide covers how to setup an API endpoint using the Next.js App Router. You can find examples
  for Next.js Server Actions and Pages Router in the [Trigger.dev
  documentation](https://trigger.dev/docs/guides/frameworks/nextjs).
</Info>

<Steps titleSize="h3">
  <Step title="Create a route handler">
    Add a route handler by creating a new `route.ts` file in a `/app/api/create-embedding-for-post` directory:

    ```ts app/api/create-embedding-for-post/route.ts theme={null}
    import type { createEmbeddingForPost } from "@/trigger/create-embedding-for-post";
    import { tasks } from "@trigger.dev/sdk";
    import { NextResponse } from "next/server";

    export async function POST(req: Request) {
      const authHeader = req.headers.get("authorization");
      if (!authHeader || authHeader !== `Bearer ${process.env.SEQUIN_WEBHOOK_SECRET}`) {
        return NextResponse.json({ error: "Unauthorized" }, { status: 401 });
      }
      const payload = await req.json();
      const handle = await tasks.trigger<typeof createEmbeddingForPost>(
        "create-embedding-for-post",
        payload
      );

      return NextResponse.json(handle);
    }
    ```

    This route handler will receive records from Sequin, parse them, and then trigger the `create-embedding-for-post` task.
  </Step>

  <Step title="Set secret keys">
    You'll need to set four secret keys in a `.env.local` file:

    ```bash  theme={null}
    SEQUIN_WEBHOOK_SECRET=your-secret-key
    TRIGGER_SECRET_KEY=secret-from-trigger-dev
    OPENAI_API_KEY=sk-proj-asdfasdfasdf
    DATABASE_URL=postgresql://
    ```

    The `SEQUIN_WEBHOOK_SECRET` ensures that only Sequin can access your API endpoint.

    The `TRIGGER_SECRET_KEY` is used to authenticate requests to Trigger.dev and can be found in the **API keys** tab of the Trigger.dev dashboard.

    The `OPENAI_API_KEY` and `DATABASE_URL` are used to create an embedding using OpenAI and connect to your database. Be sure to add these as [environment variables](https://trigger.dev/docs/deploy-environment-variables) in Trigger.dev as well.
  </Step>
</Steps>

<Check>
  You've successfully created an API endpoint that can receive record payloads from Sequin and
  trigger a Trigger.dev task. In the next step, you'll setup Sequin to trigger the endpoint.
</Check>

## Create Sequin consumer

You'll now configure Sequin to send every row in your `posts` table to your Trigger.dev task.

<Steps titleSize="h3">
  <Step title="Connect Sequin to your database">
    1. Login to your Sequin account and click the **Add New Database** button.
    2. Enter the connection details for your Postgres database.

    <Info>
      If you need to connect to a local dev database, flip the **use localhost** switch and follow the instructions to create a tunnel using the [Sequin CLI](https://sequinstream.com/docs/cli).
    </Info>

    3. Follow the instructions to create a publication and a replication slot by running two SQL commands in your database:

    ```sql  theme={null}
    create publication sequin_pub for all tables;
    select pg_create_logical_replication_slot('sequin_slot', 'pgoutput');
    ```

    4. Name your database and click the **Connect Database** button.

    Sequin will connect to your database and ensure that it's configured properly.

    <Note>
      If you need step-by-step connection instructions to connect Sequin to your database, check out our [quickstart guide](https://sequinstream.com/docs/quickstart).
    </Note>
  </Step>

  <Step title="Tunnel to your local endpoint">
    Now, create a tunnel to your local endpoint so Sequin can deliver change payloads to your local API:

    1. In the Sequin console, open the **HTTP Endpoint** tab and click the **Create HTTP Endpoint** button.
    2. Enter a name for your endpoint (i.e. `local_endpoint`) and flip the **Use localhost** switch. Follow the instructions in the Sequin console to [install the Sequin CLI](https://sequinstream.com/docs/cli), then run:

    ```bash  theme={null}
    sequin tunnel --ports=3001:local_endpoint
    ```

    3. Now, click **Add encryption header** and set the key to `Authorization` and the value to `Bearer SEQUIN_WEBHOOK_SECRET`.
    4. Click **Create HTTP Endpoint**.
  </Step>

  <Step title="Create a Push Consumer">
    Create a push consumer that will capture posts from your database and deliver them to your local endpoint:

    1. Navigate to the **Consumers** tab and click the **Create Consumer** button.
    2. Select your `posts` table (i.e `public.posts`).
    3. You want to ensure that every post receives an embedding - and that embeddings are updated as posts are updated. To do this, select to process **Rows** and click **Continue**.

    <Note>
      You can also use **changes** for this particular use case, but **rows** comes with some nice replay and backfill features.
    </Note>

    4. You'll now set the sort and filter for the consumer. For this guide, we'll sort by `updated_at` and start at the beginning of the table. We won't apply any filters:

    <Frame>
      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ff47bd808e04dc361aa45fdf353604a0" alt="Consumer Sort and Filter" data-og-width="1880" width="1880" data-og-height="980" height="980" data-path="images/sequin-sort-and-filter.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e0dc893629a4fe4e84d1a8df13dd4929 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=af076e0deed39c456fb63471a43db6de 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c273e1d361b2c1f85e6a70cdb0425a43 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=71a729303042a8388f550530d9f16cf1 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a4a7f5bbf7bea59e0fac5b8d822c3631 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-sort-and-filter.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=c7b8f9fbc1fdca8bc70dc593c4dad4f4 2500w" />
    </Frame>

    5. On the next screen, select **Push** to have Sequin send the events to your webhook URL. Click **Continue**.
    6. Now, give your consumer a name (i.e. `posts_push_consumer`) and in the **HTTP Endpoint** section select the `local_endpoint` you created above. Add the exact API route you created in the previous step (i.e. `/api/create-embedding-for-post`):

    <Frame>
      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=67defd6931a599625ba1688d920bb7e6" alt="Consumer Endpoint" data-og-width="1990" width="1990" data-og-height="1312" height="1312" data-path="images/sequin-consumer-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=57804d5d01973860174459a2c2618987 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=5cf6e70ac1cfad808bbb9a0746b61720 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=b6fcaad93ead958208e23a5ea71d8afa 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=1fe0b25fc33ed12670bb11125a68b68b 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=1db08ad9fc8923069c5e7a627f5b615f 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-consumer-config.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=20ecfe5931f428662687f3e4ab77e202 2500w" />
    </Frame>

    7. Click the **Create Consumer** button.
  </Step>
</Steps>

<Check>Your Sequin consumer is now created and ready to send events to your API endpoint.</Check>

## Test end-to-end

<Steps titleSize="h3">
  <Step title="Spin up you dev environment">
    1. The Next.js app is running: `npm run dev`
    2. The Trigger.dev dev server is running `npx trigger.dev@latest dev`
    3. The Sequin tunnel is running: `sequin tunnel --ports=3001:local_endpoint`
  </Step>

  <Step title="Create a new post in your database">
    ```sql  theme={null}
    insert into
    posts (title, body, author)
    values
      (
        'The Future of AI',
        'An insightful look into how artificial intelligence is shaping the future of technology and society.',
        'Alice H Johnson'
      );
    ```
  </Step>

  <Step title="Trace the change in the Sequin dashboard">
    In the Sequin console, navigate to the [**Trace**](https://console.sequinstream.com/trace) tab and confirm that Sequin delivered the event to your local endpoint:

    <Frame>
      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=dd86f0e4f083bff4921c54d15822a465" alt="Trace Event" data-og-width="2818" width="2818" data-og-height="1622" height="1622" data-path="images/sequin-trace.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e0f4b9353418a510c04ff85fe9680eb6 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=d2589ab5edb952c9a13b949e5f648bd2 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=e0363b09ab88bc159c5865888d8cf642 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=ac67708d978c528b9a6aecf8e5c9f854 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=3c90e4277c0a5aff51c11eabe5f25965 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-trace.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=f0460a55146329bd7906a1dff4032482 2500w" />
    </Frame>
  </Step>

  <Step title="Confirm the event was received by your endpoint">
    In your local terminal, you should see a `200` response in your Next.js app:

    ```bash  theme={null}
    POST /api/create-embedding-for-post 200 in 262ms
    ```
  </Step>

  <Step title="Observe the task run in the Trigger.dev dashboard">
    Finally, in the [**Trigger.dev dashboard**](https://cloud.trigger.dev/), navigate to the Runs page and confirm that the task run completed successfully:

    <Frame>
      <img src="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=2268cf3d51e4821aba5e13467a1f96ec" alt="Task run" data-og-width="3198" width="3198" data-og-height="2038" height="2038" data-path="images/sequin-final-run.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=280&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0f4001b06cba64dd3f890ee6024c0537 280w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=560&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=33721ede31a7e68c5d9c5a0f64f50cd6 560w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=840&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=cb21081fa0989a2a225bbd940eb40041 840w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=1100&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=0a33666f493cde10babf7414892cbc2b 1100w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=1650&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=bf4b50f0734948802244a669ac203773 1650w, https://mintcdn.com/trigger/5SxX7bFjJKRsidSL/images/sequin-final-run.png?w=2500&fit=max&auto=format&n=5SxX7bFjJKRsidSL&q=85&s=a0958fb3d3160984ca3ec726c7d79168 2500w" />
    </Frame>
  </Step>
</Steps>

<Check>
  Every time a post is created or updated, Sequin will deliver the row payload to your API endpoint
  and Trigger.dev will run the `create-embedding-for-post` task.
</Check>

## Next steps

With Sequin and Trigger.dev, every post in your database will now have an embedding. This is a simple example of how you can trigger long-running tasks on database changes.

From here, add error handling and deploy to production:

* Add [retries](/errors-retrying) to your Trigger.dev task to ensure that any errors are captured and logged.
* Deploy to [production](/guides/frameworks/nextjs#deploying-your-task-to-trigger-dev) and update your Sequin consumer to point to your production database and endpoint.
