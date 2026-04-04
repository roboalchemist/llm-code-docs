# Source: https://developers.cloudflare.com/workers/examples/redirect/index.md

---

title: Redirect · Cloudflare Workers docs
description: Redirect requests from one URL to another or from one set of URLs
  to another set.
lastUpdated: 2026-01-27T21:11:25.000Z
chatbotDeprioritize: false
tags: Middleware,Redirects,JavaScript,TypeScript,Python,Rust
source_url:
  html: https://developers.cloudflare.com/workers/examples/redirect/
  md: https://developers.cloudflare.com/workers/examples/redirect/index.md
---

If you want to get started quickly, click on the button below.

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/docs-examples/tree/main/workers/redirect)

This creates a repository in your GitHub account and deploys the application to Cloudflare Workers.

## Redirect all requests to one URL

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const destinationURL = "https://example.com";
      const statusCode = 301;
      return Response.redirect(destinationURL, statusCode);
    },
  };
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwB2ABwA2AJyiAjOICsAZnnCAXCxZtgHOFxp8BIidLlKVAWABQAYXRUIAU3vYAIlADOMdO6jQ7qki08AmISKjhgBwYAIigaBwAPADoAK3do0lQoMCcIqNj45LToq1t7JwhsABU6GAcAuBgYMD4CKDtkFLgANzh3XgRYCABqYHRccAcrK0SvJBJcB1Q4cAgSAG9LEhI+uipeQIcIXgALAAoEBwBHEAd3CABKDa3tkl47e4W76HC-KgBVABKABkSAwSNEThAIDB3KpkMhEhFmg4ku9gBkXtt3lRPvcCCB3LZFmCSIpBDIiFiSJcICAEFQSIC7l5cajLjxLrwIGdFvc4m07EDgQAaEj4ulE8YOB5U7YAXxFlnlRCsGmYWh0eh4-CEYiksgUymEpTsjmcbk83l87SoASCOlI4UiMUihB0GUC2VyLuiZDA6DIJRsZoq1Vq9R2TRavEFVE67js00s62iwDgcQA+mMJjloqoCosiul5Wr1ZqQtqDHrjIazMJmFYgA)

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const destinationURL = "https://example.com";
      const statusCode = 301;
      return Response.redirect(destinationURL, statusCode);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response


  class Default(WorkerEntrypoint):
      def fetch(self, request):
          destinationURL = "https://example.com"
          statusCode = 301
          return Response.redirect(destinationURL, statusCode)
  ```

* Rust

  ```rs
  use worker::*;


  #[event(fetch)]
  async fn fetch(_req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let destination_url = Url::parse("https://example.com")?;
      let status_code = 301;
      Response::redirect_with_status(destination_url, status_code)
  }
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", (c) => {
    const destinationURL = "https://example.com";
    const statusCode = 301;
    return c.redirect(destinationURL, statusCode);
  });


  export default app;
  ```

## Redirect requests from one domain to another

* JavaScript

  ```js
  export default {
    async fetch(request) {
      const base = "https://example.com";
      const statusCode = 301;


      const url = new URL(request.url);
      const { pathname, search } = url;


      const destinationURL = `${base}${pathname}${search}`;
      console.log(destinationURL);


      return Response.redirect(destinationURL, statusCode);
    },
  };
  ```

* TypeScript

  ```ts
  export default {
    async fetch(request): Promise<Response> {
      const base = "https://example.com";
      const statusCode = 301;


      const url = new URL(request.url);
      const { pathname, search } = url;


      const destinationURL = `${base}${pathname}${search}`;
      console.log(destinationURL);


      return Response.redirect(destinationURL, statusCode);
    },
  } satisfies ExportedHandler;
  ```

* Python

  ```py
  from workers import WorkerEntrypoint, Response
  from urllib.parse import urlparse


  class Default(WorkerEntrypoint):
      async def fetch(self, request):
          base = "https://example.com"
          statusCode = 301


          url = urlparse(request.url)


          destinationURL = f'{base}{url.path}{url.query}'
          print(destinationURL)


          return Response.redirect(destinationURL, statusCode)
  ```

* Rust

  ```rs
  use worker::*;


  #[event(fetch)]
  async fn fetch(req: Request, _env: Env, _ctx: Context) -> Result<Response> {
      let mut base = Url::parse("https://example.com")?;
      let status_code = 301;


      let url = req.url()?;


      base.set_path(url.path());
      base.set_query(url.query());


      console_log!("{:?}", base.to_string());


      Response::redirect_with_status(base, status_code)
  }
  ```

* Hono

  ```ts
  import { Hono } from "hono";


  const app = new Hono();


  app.all("*", (c) => {
    const base = "https://example.com";
    const statusCode = 301;


    const { pathname, search } = new URL(c.req.url);


    const destinationURL = `${base}${pathname}${search}`;
    console.log(destinationURL);


    return c.redirect(destinationURL, statusCode);
  });


  export default app;
  ```
