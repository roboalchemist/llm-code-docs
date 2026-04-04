# Source: https://upstash.com/docs/qstash/features/background-jobs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Background Jobs

## When do you need background jobs

Background jobs are essential for executing tasks that are too time-consuming to run in the
main execution thread without affecting the user experience.

These tasks might include data processing, sending batch emails, performing scheduled maintenance,
or any other operations that are not immediately required to respond to user requests.

Utilizing background jobs allows your application to remain responsive and scalable, handling more requests simultaneously by offloading
heavy lifting to background processes.

<Note>
  In Serverless frameworks, your hosting provider will likely have a limit for how long each task can last. Try searching
  for the maximum execution time for your hosting provider to find out more.
</Note>

## How to use QStash for background jobs

QStash provides a simple and efficient way to run background jobs, you can understand it as a 2 step process:

1. **Public API** Create a public API endpoint within your application. The endpoint should contain the logic for the background job.

<Warning>
  QStash requires a public endpoint to trigger background jobs, which means it cannot directly access localhost APIs.
  To get around this, you have two options:

  * Run QStash [development server](/qstash/howto/local-development) locally
  * Set up a [local tunnel](/qstash/howto/local-tunnel) for your API
</Warning>

2. **QStash Request** Invoke QStash to start/schedule the execution of the API endpoint.

Here's what this looks like in a simple Next.js application:

<CodeGroup>
  ```tsx app/page.tsx theme={"system"}
  "use client"

  export default function Home() {
    async function handleClick() {
      // Send a request to our server to start the background job.
      // For proper error handling, refer to the quick start.
      // Note: This can also be a server action instead of a route handler
      await fetch("/api/start-email-job", {
        method: "POST",
        body: JSON.stringify({
          users: ["a@gmail.com", "b@gmail.com", "c.gmail.com"]
        }),
      })

    }

    return (
      <main>
        <button onClick={handleClick}>Run background job</button>
      </main>
    );
  }
  ```

  ```typescript app/api/start-email-job/route.ts theme={"system"}
  import { Client } from "@upstash/qstash";

  const qstashClient = new Client({
    token: "YOUR_TOKEN",
  });

  export async function POST(request: Request) {
    const body = await request.json();
    const users: string[] = body.users;
    // If you know the public URL of the email API, you can use it directly
    const rootDomain = request.url.split('/').slice(0, 3).join('/');
    const emailAPIURL = `${rootDomain}/api/send-email`; // ie: https://yourapp.com/api/send-email

    // Tell QStash to start the background job.
    // For proper error handling, refer to the quick start.
    await qstashClient.publishJSON({
      url: emailAPIURL,
      body: {
        users
      }
    });

    return new Response("Job started", { status: 200 });
  }

  ```

  ```typescript app/api/send-email/route.ts theme={"system"}
  // This is a public API endpoint that will be invoked by QStash.
  // It contains the logic for the background job and may take a long time to execute.
  import { sendEmail } from "your-email-library";

  export async function POST(request: Request) {
    const body = await request.json();
    const users: string[] = body.users;

    // Send emails to the users
    for (const user of users) {
      await sendEmail(user);
    }

    return new Response("Job started", { status: 200 });
  }
  ```
</CodeGroup>

To better understand the application, let's break it down:

1. **Client**: The client application contains a button that, when clicked, sends a request to the server to start the background job.
2. **Next.js server**: The first endpoint, `/api/start-email-job`, is invoked by the client to start the background job.
3. **QStash**: The QStash client is used to invoke the `/api/send-email` endpoint, which contains the logic for the background job.

Here is a visual representation of the process:

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=aa9487634c406fd5c7f3a2b593fc0dee" alt="Background job diagram" data-og-width="1070" width="1070" data-og-height="819" height="819" data-path="img/qstash/qstash-bgjob-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6cbaf9e2ce208d02ff0d9538aaac34d4 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3d2094dcccb410fa7535874565d53701 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=66f5862f5a040808dd16e3dd95bd598d 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6426a63ae8498a72ae057635a12cf504 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=525291d041378c2bbe375e44aa75a713 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-light.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8d580e6461ecc72241208eeef797cbcf 2500w" />

  <img className="hidden dark:block" src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1bea175814a7bad996157f57e517c113" alt="Background job diagram" data-og-width="1070" width="1070" data-og-height="819" height="819" data-path="img/qstash/qstash-bgjob-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d68d7341ceb59aee05176e2985e536d8 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8ae3bccbc31cb9fe526bf2d323c1b026 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f86bc83bb30c79844d3eedf9d0988ff9 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=050504a93d42ed7ff6c4b987a30bacf8 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=360782daae0f8c9b888742a97fa6df62 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/qstash-bgjob-dark.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=38015fa7e22e6464e45ca66f2cfca893 2500w" />
</Frame>

To view a more detailed Next.js quick start guide for setting up QStash, refer to the [quick start](/qstash/quickstarts/vercel-nextjs) guide.

It's also possible to schedule a background job to run at a later time using [schedules](/qstash/features/schedules).

If you'd like to invoke another endpoint when the background job is complete, you can use [callbacks](/qstash/features/callbacks).
