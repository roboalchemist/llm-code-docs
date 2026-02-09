# Source: https://upstash.com/docs/workflow/quickstarts/vercel-nextjs.md

# Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Next.js

QStash is a robust message queue and task-scheduling service that integrates perfectly with Next.js. This guide will show you how to use QStash in your Next.js projects, including a quickstart and a complete example.

## Quickstart

At its core, each QStash message contains two pieces of information:

* URL (which endpoint to call)
* Request body (e.g. IDs of items you want to process)

The following endpoint could be used to upload an image and then asynchronously queue a processing task to optimize the image in the background.

```tsx upload-image/route.ts theme={"system"}
import { Client } from "@upstash/qstash"
import { NextResponse } from "next/server"

const client = new Client({ token: process.env.QSTASH_TOKEN! })

export const POST = async (req: Request) => {
  // Image uploading logic

  // 👇 Once uploading is done, queue an image processing task
  const result = await client.publishJSON({
    url: "https://your-api-endpoint.com/process-image",
    body: { imageId: "123" },
  })

  return NextResponse.json({
    message: "Image queued for processing!",
    qstashMessageId: result.messageId,
  })
}
```

Note that the URL needs to be publicly available for QStash to call, either as a deployed project or by [developing with QStash locally](/qstash/howto/local-tunnel).

Because QStash calls our image processing task, we get automatic retries whenever the API throws an error. These retries make our function very reliable. We also let the user know immediately that their image has been successfully queued.

Now, let's **receive the QStash message** in our image processing endpoint:

```tsx process-image/route.ts theme={"system"}
import { verifySignatureAppRouter } from "@upstash/qstash/nextjs"

// 👇 Verify that this messages comes from QStash
export const POST = verifySignatureAppRouter(async (req: Request) => {
  const body = await req.json()
  const { imageId } = body as { imageId: string }

  // Image processing logic, i.e. using sharp

  return new Response(`Image with id "${imageId}" processed successfully.`)
})
```

```bash .env theme={"system"}
# Copy all three from your QStash dashboard
QSTASH_TOKEN=
QSTASH_CURRENT_SIGNING_KEY=
QSTASH_NEXT_SIGNING_KEY=
```

Just like that, we set up a reliable and asynchronous image processing system in Next.js. The same logic works for email queues, reliable webhook processing, long-running report generations and many more.

## Example project

* Create an Upstash account and get your [QStash token](https://console.upstash.com/qstash)
* Node.js installed

<Steps>
  <Step titleSize="h3" title="Create Next.js app and install QStash">
    ```bash  theme={"system"}
    npx create-next-app@latest qstash-bg-job
    ```

    ```bash  theme={"system"}
    cd qstash-bg-job
    ```

    ```bash  theme={"system"}
    npm install @upstash/qstash
    ```

    ```bash  theme={"system"}
    npm run dev
    ```
  </Step>

  <Step titleSize="h3" title="Create UI">
    After removing the default content in `src/app/page.tsx`, let's create a simple UI to trigger the background job
    using a button.

    ```tsx src/app/page.tsx theme={"system"}
    "use client"

    export default function Home() {
      return (
        <main className="flex h-lvh items-center justify-center">
          <button
            onClick={handleClick}
            className="btn btn-primary w-1/2 h-56 bg-green-500 text-xl sm:text-3xl rounded-lg hover:bg-green-600"
          >
            Start Background Job
          </button>
        </main>
      )
    }
    ```

    <Accordion title="Beautiful">
      <Frame>
        <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=db902e71fc22c50749ebfc8795aa4337" alt="Quickstart UI" data-og-width="1918" width="1918" data-og-height="1126" height="1126" data-path="img/qstash/quickstart-qstash-ui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6cffcb8f93df2c5b612bdcbcefa176cc 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1566f155c0e7e02185836f266dd6de60 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=895da26a22dc02c86dd9e7cc9816f3e5 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c8f35545af51da14f0abe4b34c6134a7 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d5110f84aed75b824851c3763c0996c4 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-ui.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0b4ab5ed36ba8de483d5ef1753edbc23 2500w" />
      </Frame>
    </Accordion>
  </Step>

  <Step titleSize="h3" title="Start Background Job">
    We can use QStash to start a background job by calling the `publishJSON` method.
    In this example, we're using Next.js server actions, but you can also use route handlers.

    Since we don't have our public API endpoint yet, we can use [Request Catcher](https://requestcatcher.com/) to test the background job.
    This will eventually be replaced with our own API endpoint.

    ```ts src/app/actions.ts theme={"system"}
    "use server"
    import { Client } from "@upstash/qstash"

    const qstashClient = new Client({
      // Add your token to a .env file
      token: process.env.QSTASH_TOKEN!,
    })

    export async function startBackgroundJob() {
      await qstashClient.publishJSON({
        url: "https://firstqstashmessage.requestcatcher.com/test",
        body: {
          hello: "world",
        },
      })
    }
    ```

    Now let's invoke the `startBackgroundJob` function when the button is clicked.

    ```tsx src/app/page.tsx theme={"system"}
    "use client"
    import { startBackgroundJob } from "@/app/actions"

    export default function Home() {
      async function handleClick() {
        await startBackgroundJob()
      }

      return (
        <main className="flex h-lvh items-center justify-center">
          <button
            onClick={handleClick}
            className="btn btn-primary w-1/2 h-56 bg-green-500 text-xl sm:text-3xl rounded-lg hover:bg-green-600"
          >
            Start Background Job
          </button>
        </main>
      )
    }
    ```

    To test the background job, click the button and check the Request Catcher for the incoming request.

    <Accordion title="Verification screenshots">
      <Frame>
        <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f68c3043856bf77c5e55786a54d57cd7" data-og-width="1456" width="1456" data-og-height="580" height="580" data-path="img/qstash/reqcatcher.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=84c76a371ea1a6af224a61c7897176e4 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=337d1aa2277b60b314a69122ba24bfa0 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f8d5a20e4e1a735bb579791f474d891b 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=2fcbc86f518555b08b306ff0d4c64045 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f5f8791bc3df089e26bac1e742505b9c 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/reqcatcher.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=26a972e97932d8f03f8183da39996063 2500w" />
      </Frame>

      You can also head over to [Upstash Console](https://console.upstash.com/qstash) and go to the
      `Logs` tab where you can see your message activities.

      <Frame>
        <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=beb5fcdfa587a89b438d2db22938f6df" data-og-width="2026" width="2026" data-og-height="660" height="660" data-path="img/qstash/log.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=acfc44f8f71fec5480334c50076ba5f6 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=46be420ad548bc8d1549ac4eb572ad46 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=506308270b92f95e63fb412cb14835ca 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b51df20dcd9047a2f1c8043db306e1b1 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5482ee85fa85b78af2d8eab873024a00 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/log.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3800e49a97e6c19fcdadef691c25dcd9 2500w" />
      </Frame>
    </Accordion>
  </Step>

  <Step titleSize="h3" title="Create your own endpoint">
    Now that we know QStash is working, let's create our own endpoint to handle a background job. This
    is the endpoint that will be invoked by QStash.

    This job will be responsible for sending 10 requests, each with a 500ms delay. Since we're deploying
    to Vercel, we have to be cautious of the [time limit for serverless functions](https://vercel.com/docs/functions/runtimes#max-duration).

    ```ts src/app/api/long-task/route.ts theme={"system"}
    export async function POST(request: Request) {
      const data = await request.json()

      for (let i = 0; i < 10; i++) {
        await fetch("https://firstqstashmessage.requestcatcher.com/test", {
          method: "POST",
          body: JSON.stringify(data),
          headers: { "Content-Type": "application/json" },
        })
        await new Promise((resolve) => setTimeout(resolve, 500))
      }

      return Response.json({ success: true })
    }
    ```

    Now let's update our `startBackgroundJob` function to use our new endpoint.

    There's 1 problem: our endpoint is not public. We need to make it public so that QStash can call it.
    We have 2 options:

    1. Deploy our application to a platform like Vercel and use the public URL.
    2. Create a [local tunnel](/qstash/howto/local-tunnel) to test the endpoint locally.

    For the purpose, of this tutorial, I'll deploy the application to Vercel, but
    feel free to use a local tunnel if you prefer.

    <Accordion title="Deploying to Vercel">
      There are many ways to [deploy to Vercel](https://vercel.com/docs/deployments/overview), but
      I'm going to use the Vercel CLI.

      ```bash  theme={"system"}
      npm install -g vercel
      ```

      ```bash  theme={"system"}
      vercel
      ```

      Once deployed, you can find the public URL in the Vercel dashboard.
    </Accordion>

    Now that we have a public URL, we can update the URL.

    ```ts src/app/actions.ts theme={"system"}
    "use server"
    import { Client } from "@upstash/qstash"

    const qstashClient = new Client({
      token: process.env.QSTASH_TOKEN!,
    })

    export async function startBackgroundJob() {
      await qstashClient.publishJSON({
        // Replace with your public URL
        url: "https://qstash-bg-job.vercel.app/api/long-task",
        body: {
          hello: "world",
        },
      })
    }
    ```

    And voila! You've created a Next.js app that calls a long-running background job using QStash.
  </Step>

  <Step title="Error catching and security">
    QStash is a great way to handle background jobs, but it's important to remember that it's a public
    API. This means that anyone can call your endpoint. Make sure to add security measures to your endpoint
    to ensure that QStash is the sender of the request.

    Luckily, our SDK provides a way to verify the sender of the request. Make sure to get your signing keys
    from the QStash console and add them to your environment variables. The `verifySignatureAppRouter` will try to
    load `QSTASH_CURRENT_SIGNING_KEY` and `QSTASH_NEXT_SIGNING_KEY` from the environment. If one of them is missing,
    an error is thrown.

    ```ts src/app/api/long-task/route.ts theme={"system"}
    import { verifySignatureAppRouter } from "@upstash/qstash/nextjs"

    async function handler(request: Request) {
      const data = await request.json()

      for (let i = 0; i < 10; i++) {
        await fetch("https://firstqstashmessage.requestcatcher.com/test", {
          method: "POST",
          body: JSON.stringify(data),
          headers: { "Content-Type": "application/json" },
        })
        await new Promise((resolve) => setTimeout(resolve, 500))
      }

      return Response.json({ success: true })
    }

    export const POST = verifySignatureAppRouter(handler)
    ```

    Let's also add error catching to our action and a loading state to our UI.

    <CodeGroup>
      ```ts src/app/actions.ts theme={"system"}
      "use server"
      import { Client } from "@upstash/qstash";

      const qstashClient = new Client({
        token: process.env.QSTASH_TOKEN!,
      });

      export async function startBackgroundJob() {
        try {
          const response = await qstashClient.publishJSON({
            "url": "https://qstash-bg-job.vercel.app/api/long-task",
            body: {
              "hello": "world"
            }
          });
          return response.messageId;
        } catch (error) {
          console.error(error);
          return null;
        }
      }
      ```

      ```tsx src/app/page.tsx theme={"system"}
      "use client"
      import { startBackgroundJob } from "@/app/actions";
      import { useState } from "react";

      export default function Home() {
        const [loading, setLoading] = useState(false);
        const [msg, setMsg] = useState("");

        async function handleClick() {
          setLoading(true);
          const messageId = await startBackgroundJob();
          if (messageId) {
            setMsg(`Started job with ID ${messageId}`);
          } else {
            setMsg("Failed to start background job");
          }
          setLoading(false);
        }

        return (
          <main className="flex flex-col h-lvh items-center justify-center">
            <button onClick={handleClick} disabled={loading} className="btn btn-primary w-1/2 h-56 bg-green-500 text-xl sm:text-3xl rounded-lg hover:bg-green-600 disabled:bg-gray-500">
              Start Background Job
            </button>

            {loading && <div className="text-2xl mt-8">Loading...</div>}
            {msg && <p className="text-center text-lg">{msg}</p>}
          </main>
        );
      }
      ```
    </CodeGroup>
  </Step>
</Steps>

## Result

We have now created a Next.js app that calls a long-running background job using QStash!
Here's the app in action:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/nextjs-quickstart-result-gif.gif?s=a49ea8f2c7d3ffdf062005939591030b" alt="Quickstart Result Gif" data-og-width="1000" width="1000" data-og-height="550" height="550" data-path="img/qstash/nextjs-quickstart-result-gif.gif" data-optimize="true" data-opv="3" />
</Frame>

We can also view the logs on Vercel and QStash

<Accordion title="Logs">
  Vercel

  <Frame>
    <img src="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=6bebdd8a99667f5859444d537ccb1a1e" alt="Vercel Logs" data-og-width="503" width="503" data-og-height="747" height="747" data-path="img/qstash/vercel-log-quickstart.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=280&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=eef02e2b49c43aee744b06431900d37d 280w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=560&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=3d27f2f8f59089ef66aefe0fc4aea1de 560w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=840&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=aa64ae73ab4daaa1532d1f0ec4b0f6f1 840w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=1100&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=d77bcfae328148308a73fb5651d53349 1100w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=1650&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=51de3010830efa5558a6a0018c0532bc 1650w, https://mintcdn.com/upstash/fy-PVAyWJaRFn1UN/img/qstash/vercel-log-quickstart.png?w=2500&fit=max&auto=format&n=fy-PVAyWJaRFn1UN&q=85&s=38c17b368f928e4e84a0266b52c9edb8 2500w" />
  </Frame>

  QStash

  <Frame>
    <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6c91cb9d180d8a4e3d6e7420e8d5f815" alt="Vercel Logs" data-og-width="2034" width="2034" data-og-height="650" height="650" data-path="img/qstash/quickstart-qstash-result.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=5197cff2e8c3726ed4e0f7a8df50ca6e 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8cd1d3456f09b96489013d93086bf552 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3dd0bf0918c3cb8f6d9999943785454b 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6942e47bcacbdd8c59c745c92eba9d47 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=649dd318670c87d30f5138616cac7350 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/quickstart-qstash-result.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=0f4a0564876d76c63c51b6b0e4cbd6b3 2500w" />
  </Frame>
</Accordion>

And the code for the 3 files we created:

<CodeGroup>
  ```tsx src/app/page.tsx theme={"system"}
  "use client"
  import { startBackgroundJob } from "@/app/actions";
  import { useState } from "react";

  export default function Home() {
  const [loading, setLoading] = useState(false);
  const [msg, setMsg] = useState("");

    async function handleClick() {
      setLoading(true);
      const messageId = await startBackgroundJob();
      if (messageId) {
        setMsg(`Started job with ID ${messageId}`);
      } else {
        setMsg("Failed to start background job");
      }
      setLoading(false);
    }

    return (
      <main className="flex flex-col h-lvh items-center justify-center">
        <button onClick={handleClick} disabled={loading} className="btn btn-primary w-1/2 h-56 bg-green-500 text-xl sm:text-3xl rounded-lg hover:bg-green-600 disabled:bg-gray-500">
          Start Background Job
        </button>

        {loading && <div className="text-2xl mt-8">Loading...</div>}
        {msg && <p className="text-center text-lg">{msg}</p>}
      </main>
    );

  }

  ```

  ```ts src/app/actions.ts theme={"system"}
  "use server"
  import { Client } from "@upstash/qstash";

  const qstashClient = new Client({
    token: process.env.QSTASH_TOKEN!,
  });

  export async function startBackgroundJob() {
    try {
      const response = await qstashClient.publishJSON({
        "url": "https://qstash-bg-job.vercel.app/api/long-task",
        body: {
          "hello": "world"
        }
      });
      return response.messageId;
    } catch (error) {
      console.error(error);
      return null;
    }
  }
  ```

  ```ts src/app/api/long-task/route.ts theme={"system"}
  import { verifySignatureAppRouter } from "@upstash/qstash/nextjs"

  async function handler(request: Request) {
    const data = await request.json()

    for (let i = 0; i < 10; i++) {
      await fetch("https://firstqstashmessage.requestcatcher.com/test", {
        method: "POST",
        body: JSON.stringify(data),
        headers: { "Content-Type": "application/json" },
      })
      await new Promise((resolve) => setTimeout(resolve, 500))
    }

    return Response.json({ success: true })
  }

  export const POST = verifySignatureAppRouter(handler)
  ```
</CodeGroup>

Now, go ahead and try it out for yourself! Try using some of the other features of QStash, like
[schedules](/qstash/features/schedules), [callbacks](/qstash/features/callbacks), and [URL Groups](/qstash/features/url-groups).
