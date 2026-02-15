# Source: https://developers.cloudflare.com/workers/examples/fetch-html/index.md

---

title: Fetch HTML · Cloudflare Workers docs
description: Send a request to a remote server, read HTML from the response, and
  serve that HTML.
lastUpdated: 2025-08-20T18:47:44.000Z
chatbotDeprioritize: false
tags: JavaScript,TypeScript,Python
source_url:
  html: https://developers.cloudflare.com/workers/examples/fetch-html/
  md: https://developers.cloudflare.com/workers/examples/fetch-html/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/fetch-html)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

* JavaScript

  ```js
  export default {
    async fetch(request) {
      /**
       * Replace `remote` with the host you wish to send requests to
       */
      const remote = "https://example.com";


      return await fetch(remote, request);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwB2YQBZhggBwBWAIwyAzHIBcLFm2Ac4XGnwEjxk2QuUBYAFABhdFQgBTO9gAiUAM4x0bqNFsqSmngExCRUcMD2DABEUDT2AB4AdABWblGkqFBgjuGRMXFJqVGWNnaOENgAKnQw9v5wMDBgfARQtsjJcABucG68CLAQANTA6Ljg9paWCZ5IJLj2qHDgECQA3hYkJL10VLwB9hC8ABYAFAj2AI4g9m4QAJTrm1skyABUb88vbyQASvZNOC8ewkAAGF1GDlBJAA7j5jiQIMcQccvKs6JRYe4ERB0CQ3I5cCQLtdbhA3Ij0F8tm9kNTeLY7sT7JCQQwSFFjhAIDA3CpkMgEuEmvZEgzgOkLNSLhAQAgqNsYXAfAcjmcIegHAAaZmku73IjPAC+WosRqIlnUzE02l0PH4QlEEmk8iUchKtgcTlcHi8PjaVH8gW0pDCEWiEUI2nSASyOXDUTIYHQZGK1k95SqNTq20azV4rXaqVsUwsayiwGVVAA+qNxtkoip8gtCmkjZarTbgnb9I6jC7THJmJYgA)

* TypeScript

  ```ts
  export default {
    async fetch(request: Request): Promise<Response> {
      /**
       * Replace `remote` with the host you wish to send requests to
       */
      const remote = "https://example.com";


      return await fetch(remote, request);
    },
  };
  ```

* Python

  ```py
  from workers import WorkerEntrypoint
  from js import fetch


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          # Replace `remote` with the host you wish to send requests to
          remote = "https://example.com"
          return await fetch(remote, request)
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", async (c) => {
    /**
     * Replace `remote` with the host you wish to send requests to
     */
    const remote = "https://example.com";


    // Forward the request to the remote server
    return await fetch(remote, c.req.raw);
  });


  export default app;
  ```
