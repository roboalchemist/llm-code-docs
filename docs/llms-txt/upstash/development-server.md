# Source: https://upstash.com/docs/workflow/howto/local-development/development-server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Development Server

Upstash Workflow is built on top of Upstash QStash.
The QStash CLI provides a local development server that performs QStash functionality locally for development and testing purposes.

<Steps>
  <Step title="Install and Start Development Server">
    Start the development server using the QStash CLI:

    ```javascript  theme={"system"}
    npx @upstash/qstash-cli dev
    ```

    The QStash CLI output will look something like this:

    ```plaintext QStash CLI Output theme={"system"}
    Upstash QStash development server is runnning at

    A default user has been created for you to authorize your requests.
    QSTASH_TOKEN=eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0=
    QSTASH_CURRENT_SIGNING_KEY=sig_7RvLjqfZBvP5KEUimQCE1pvpLuou
    QSTASH_NEXT_SIGNING_KEY=sig_7W3ZNbfKWk5NWwEs3U4ixuQ7fxwE

    Sample cURL request:
    curl -X POST http://127.0.0.1:8080/v2/publish/https://example.com -H "Authorization: Bearer eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0="

    Check out documentation for more details:
    https://upstash.com/docs/qstash/howto/local-development
    ```

    For detailed instructions on setting up the development server, see our [QStash Local Development Guide](/qstash/howto/local-development).
  </Step>

  <Step title="Enable Local Mode on Console">
    Once you start the local server, you can go to the Workflow tab on Upstash Console and enable local mode, which will allow you to monitor and debug workflow runs with the local server.

    <img src="https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=fe713991a7fd41c24edde7e1e56b5f7e" data-og-width="2042" width="2042" data-og-height="1668" height="1668" data-path="img/workflow/local-mode-workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=280&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=46b588d9eb3784bc997c411756341b0e 280w, https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=560&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=1147a5e8df93dbca1035c77e0385c9f3 560w, https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=840&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=fa937e0edc160893bad21263d72e6d7b 840w, https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=1100&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=72811c595a9c144b2cac4e4e3bea0403 1100w, https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=1650&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=ad8a59a80b1001738a16a92b1723a9c9 1650w, https://mintcdn.com/upstash/0HG5ARygt5BXCm9S/img/workflow/local-mode-workflow.png?w=2500&fit=max&auto=format&n=0HG5ARygt5BXCm9S&q=85&s=c7f0612a6ea8e13dd808c9703b548820 2500w" />
  </Step>

  <Step title="Update Environment Variables">
    Once your development server is running, update your environment variables to route QStash requests to your local server.

    ```env  theme={"system"}
    QSTASH_URL="http://127.0.0.1:8080"
    QSTASH_TOKEN="eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0="
    QSTASH_CURRENT_SIGNING_KEY="sig_7RvLjqfZBvP5KEUimQCE1pvpLuou"
    QSTASH_NEXT_SIGNING_KEY="sig_7W3ZNbfKWk5NWwEs3U4ixuQ7fxwE"
    ```
  </Step>

  <Step title="Use local addresses">
    It's all set up 🎉

    Now, you can use your local address when triggering the workflow runs.

    ```javascript  theme={"system"}
    import { Client } from "@upstash/workflow";

    const client = Client()

    const { workflowRunId } = await client.trigger({
        url: `http://localhost:3000/api/workflow`,
        retries: 3
    });
    ```

    <Tip>
      Inside the `trigger()` call, you need to provide the URL of your workflow endpoint:

      * Local development → use the URL where your app is running, for example: [http://localhost:3000/api/PATH](http://localhost:3000/api/PATH)
      * Production → use the URL of your deployed app, for example: [https://yourapp.com/api/PATH](https://yourapp.com/api/PATH)

      To avoid hardcoding URLs, you can define a `BASE_URL` constant and set it based on the environment.
      A common pattern is to check an environment variable that only exists in production:

      ```javascript  theme={"system"}
      const BASE_URL = process.env.VERCEL_URL
        ? `https://${process.env.VERCEL_URL}`
        : `http://localhost:3000`

      const { workflowRunId } = await client.trigger({
          url: `${BASE_URL}/api/workflow`,
          retries: 3
      });
      ```
    </Tip>
  </Step>
</Steps>
