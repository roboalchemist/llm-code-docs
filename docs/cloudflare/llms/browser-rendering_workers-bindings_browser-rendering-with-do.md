# Source: https://developers.cloudflare.com/browser-rendering/workers-bindings/browser-rendering-with-do/index.md

---

title: Deploy a Browser Rendering Worker with Durable Objects · Cloudflare
  Browser Rendering docs
description: Use the Browser Rendering API along with Durable Objects to take
  screenshots from web pages and store them in R2.
lastUpdated: 2026-02-02T18:38:11.000Z
chatbotDeprioritize: false
tags: JavaScript
source_url:
  html: https://developers.cloudflare.com/browser-rendering/workers-bindings/browser-rendering-with-do/
  md: https://developers.cloudflare.com/browser-rendering/workers-bindings/browser-rendering-with-do/index.md
---

By following this guide, you will create a Worker that uses the Browser Rendering API along with [Durable Objects](https://developers.cloudflare.com/durable-objects/) to take screenshots from web pages and store them in [R2](https://developers.cloudflare.com/r2/).

Using Durable Objects to persist browser sessions improves performance by eliminating the time that it takes to spin up a new browser session. Since Durable Objects re-uses sessions, it reduces the number of concurrent sessions needed.

1. Sign up for a [Cloudflare account](https://dash.cloudflare.com/sign-up/workers-and-pages).
2. Install [`Node.js`](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm).

Node.js version manager

Use a Node version manager like [Volta](https://volta.sh/) or [nvm](https://github.com/nvm-sh/nvm) to avoid permission issues and change Node.js versions. [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/), discussed later in this guide, requires a Node version of `16.17.0` or later.

## 1. Create a Worker project

[Cloudflare Workers](https://developers.cloudflare.com/workers/) provides a serverless execution environment that allows you to create new applications or augment existing ones without configuring or maintaining infrastructure. Your Worker application is a container to interact with a headless browser to do actions, such as taking screenshots.

Create a new Worker project named `browser-worker` by running:

* npm

  ```sh
  npm create cloudflare@latest -- browser-worker
  ```

* yarn

  ```sh
  yarn create cloudflare browser-worker
  ```

* pnpm

  ```sh
  pnpm create cloudflare@latest browser-worker
  ```

## 2. Install Puppeteer

In your `browser-worker` directory, install Cloudflare’s [fork of Puppeteer](https://developers.cloudflare.com/browser-rendering/puppeteer/):

* npm

  ```sh
  npm i -D @cloudflare/puppeteer
  ```

* yarn

  ```sh
  yarn add -D @cloudflare/puppeteer
  ```

* pnpm

  ```sh
  pnpm add -D @cloudflare/puppeteer
  ```

## 3. Create a R2 bucket

Create two R2 buckets, one for production, and one for development.

Note that bucket names must be lowercase and can only contain dashes.

```sh
wrangler r2 bucket create screenshots
wrangler r2 bucket create screenshots-test
```

To check that your buckets were created, run:

```sh
wrangler r2 bucket list
```

After running the `list` command, you will see all bucket names, including the ones you have just created.

## 4. Configure your Wrangler configuration file

Configure your `browser-worker` project's [Wrangler configuration file](https://developers.cloudflare.com/workers/wrangler/configuration/) by adding a browser [binding](https://developers.cloudflare.com/workers/runtime-apis/bindings/) and a [Node.js compatibility flag](https://developers.cloudflare.com/workers/configuration/compatibility-flags/#nodejs-compatibility-flag). Browser bindings allow for communication between a Worker and a headless browser which allows you to do actions such as taking a screenshot, generating a PDF and more.

Update your Wrangler configuration file with the Browser Rendering API binding, the R2 bucket you created and a Durable Object:

Note

Your Worker configuration must include the `nodejs_compat` compatibility flag and a `compatibility_date` of 2025-09-15 or later.

* wrangler.jsonc

  ```jsonc
  {
    "$schema": "./node_modules/wrangler/config-schema.json",
    "name": "rendering-api-demo",
    "main": "src/index.js",
    "compatibility_date": "2026-02-14",
    "compatibility_flags": [
      "nodejs_compat"
    ],
    "account_id": "<ACCOUNT_ID>",
    // Browser Rendering API binding
    "browser": {
      "binding": "MYBROWSER"
    },
    // Bind an R2 Bucket
    "r2_buckets": [
      {
        "binding": "BUCKET",
        "bucket_name": "screenshots",
        "preview_bucket_name": "screenshots-test"
      }
    ],
    // Binding to a Durable Object
    "durable_objects": {
      "bindings": [
        {
          "name": "BROWSER",
          "class_name": "Browser"
        }
      ]
    },
    "migrations": [
      {
        "tag": "v1", // Should be unique for each entry
        "new_sqlite_classes": [ // Array of new classes
          "Browser"
        ]
      }
    ]
  }
  ```

* wrangler.toml

  ```toml
  "$schema" = "./node_modules/wrangler/config-schema.json"
  name = "rendering-api-demo"
  main = "src/index.js"
  compatibility_date = "2026-02-14"
  compatibility_flags = [ "nodejs_compat" ]
  account_id = "<ACCOUNT_ID>"


  [browser]
  binding = "MYBROWSER"


  [[r2_buckets]]
  binding = "BUCKET"
  bucket_name = "screenshots"
  preview_bucket_name = "screenshots-test"


  [[durable_objects.bindings]]
  name = "BROWSER"
  class_name = "Browser"


  [[migrations]]
  tag = "v1"
  new_sqlite_classes = [ "Browser" ]
  ```

## 5. Code

The code below uses Durable Object to instantiate a browser using Puppeteer. It then opens a series of web pages with different resolutions, takes a screenshot of each, and uploads it to R2.

The Durable Object keeps a browser session open for 60 seconds after last use. If a browser session is open, any requests will re-use the existing session rather than creating a new one. Update your Worker code by copy and pasting the following:

* JavaScript

  ```js
  import { DurableObject } from "cloudflare:workers";
  import * as puppeteer from "@cloudflare/puppeteer";


  export default {
    async fetch(request, env) {
      const obj = env.BROWSER.getByName("browser");


      // Send a request to the Durable Object, then await its response
      const resp = await obj.fetch(request);


      return resp;
    },
  };


  const KEEP_BROWSER_ALIVE_IN_SECONDS = 60;


  export class Browser extends DurableObject {
    browser;
    keptAliveInSeconds = 0;
    storage;


    constructor(state, env) {
      super(state, env);
      this.storage = state.storage;
    }


    async fetch(request) {
      // Screen resolutions to test out
      const width = [1920, 1366, 1536, 360, 414];
      const height = [1080, 768, 864, 640, 896];


      // Use the current date and time to create a folder structure for R2
      const nowDate = new Date();
      const coeff = 1000 * 60 * 5;
      const roundedDate = new Date(
        Math.round(nowDate.getTime() / coeff) * coeff,
      ).toString();
      const folder = roundedDate.split(" GMT")[0];


      // If there is a browser session open, re-use it
      if (!this.browser || !this.browser.isConnected()) {
        console.log(`Browser DO: Starting new instance`);
        try {
          this.browser = await puppeteer.launch(this.env.MYBROWSER);
        } catch (e) {
          console.log(
            `Browser DO: Could not start browser instance. Error: ${e}`,
          );
        }
      }


      // Reset keptAlive after each call to the DO
      this.keptAliveInSeconds = 0;


      // Check if browser exists before opening page
      if (!this.browser)
        return new Response("Browser launch failed", { status: 500 });


      const page = await this.browser.newPage();


      // Take screenshots of each screen size
      for (let i = 0; i < width.length; i++) {
        await page.setViewport({ width: width[i], height: height[i] });
        await page.goto("https://workers.cloudflare.com/");
        const fileName = `screenshot_${width[i]}x${height[i]}`;
        const sc = await page.screenshot();


        await this.env.BUCKET.put(`${folder}/${fileName}.jpg`, sc);
      }


      // Close tab when there is no more work to be done on the page
      await page.close();


      // Reset keptAlive after performing tasks to the DO
      this.keptAliveInSeconds = 0;


      // Set the first alarm to keep DO alive
      const currentAlarm = await this.storage.getAlarm();
      if (currentAlarm == null) {
        console.log(`Browser DO: setting alarm`);
        const TEN_SECONDS = 10 * 1000;
        await this.storage.setAlarm(Date.now() + TEN_SECONDS);
      }


      return new Response("success");
    }


    async alarm() {
      this.keptAliveInSeconds += 10;


      // Extend browser DO life
      if (this.keptAliveInSeconds < KEEP_BROWSER_ALIVE_IN_SECONDS) {
        console.log(
          `Browser DO: has been kept alive for ${this.keptAliveInSeconds} seconds. Extending lifespan.`,
        );
        await this.storage.setAlarm(Date.now() + 10 * 1000);
        // You can ensure the ws connection is kept alive by requesting something
        // or just let it close automatically when there is no work to be done
        // for example, `await this.browser.version()`
      } else {
        console.log(
          `Browser DO: exceeded life of ${KEEP_BROWSER_ALIVE_IN_SECONDS}s.`,
        );
        if (this.browser) {
          console.log(`Closing browser.`);
          await this.browser.close();
        }
      }
    }
  }
  ```

  [Run Worker in Playground](https://workers.cloudflare.com/playground#LYVwNgLglgDghgJwgegGYHsHALQBM4RwDcABAEbogB2+CAngLzbPYZb6HbW5QDGU2AAwAWYQFYxARmEA2QQGZhAdgBcLFm2Ac4XGnwEjxU2QuUBYAFABhdFQgBTO9gAiUAM4x0bqNFsqSmngExCRUcMD2DABEUDT2AB4AdABWblGkqFBgjuGRMXFJqVGWNnaOENgAKnQw9v5wMDBgfARQtsjJcABucG68CLAQANTA6Ljg9paWUMCeSCQA3iTOIAhwZNkA8mTJ9rwQJAC+AQjowCRRvGCUuKhgiHUA7pgA1vYIaUQWM3MHAFQkXokGAgRr2BzvE5nC4AASuNzuD2QILBEIQ6QsFgSvxIuHsqDg4AOCwsJEBbjoVF4AXBvAAFgAKBD2ACOIHsbggABoSI4ugBKRakskkXi2TkkdA7EgMXlULqJABCACVNgB1ADKAFFlYkAObgxV0AByuQZUTIp0ebneUX5X2FZOQyBIGscuEBJGZbI5Bwg6BIEDp9mWq3W2RI212+x5QccgMecB8JB8bi9HM8VBtjtF4oOzI8MoTSYOUuSiVQtMZ3vZnPtmJF6Ygqyo6Y8XzJhy5FkODrFWYOAGktVqAAoAfRV6u1yvHAEEADIASQAalrx0vjePtVZNsbnBqi3IHdjMAcrr004qrTaELz4g4aGmVmsNvYo3ticLLehre8OyQbwwBAc7NF09hLlQbr9rgaayoIAGcpgcAGg6ZL9pyCAgPsmAMpyBD2DyfKCiSjZuKC7x4YQDhEfK9aNkG7iJEhawGkW+EOMx-qsfYAGHA25KUtSlYQPSTKsrWEAkTmzquv09jxgW6BgCAvhZoGAYOBKlAQDmGEHI8UC4EGRYANqSAAnAATIIPKSPIMgyHZYgOTyDm2SQwjSAAugB6F5iQwZQHqdIHLK5mCAAHB5SgyJFPKRTIwg8klHmRRZMi+QJTougAqjagbBqKqzMnYuIEYCNCBjMIb+qKzIVXAATKXid6YdhzbMs1d7KlZekBVQv7OBVspUPYjzLARDL0SK+m5viqBFpIggrSQAJyGtJBiH5uYDl6lBxLgw0OEWY0Tcd9gMjmZIALIEHSiSnNwDKDY8F36uClQ1dNJAumKC2CgC-2oKg3aNvyiT+hqEADFQerTTtc0YGArVFk9h3vR4zQQOaJAAOI3ZUdqmYIWUyS6S6LXGXXuJ6P5-m1HLeLYkq1FQPLMlwBU+DmUCLQyACEjFuIk9O3iQAA+EskELdJMWL7yJO4pRjfs9i4NN0mNv5WbKfYiTXPDAAG16-uLzibP40OINAcOhONKYDnAVL2EbM0MfQQrayKwuizekKynAibJiitRogbhJUoyvt8okN0AJpTpqOruyKxy8AQ9IkAy9ha97u1uHrBvoPD13ayb-t3hb-g2OAHqDQc+HzArd6xPhLuJCQWoIKcCD+AAJAs9iHEbYP56nnY5vx5MkMqHLgoB9jAaBUDgYCqAOHe9hwFnGdgGAGmFSGFs5r7QEgWBEFQXstiwUWCHZb9LpWMGvAvCmi0t-e7gQGmZD4pgEM6A2axD1MCFC9heb81lvLSu-Iy7Mk6q2M6s8MzikulEU2DMSD3GoFnAkWR1ZRB5EsDiIA3D+DEKtQ49Z+p7XgGxQOwc-RyxFi3RIZ1RwQIRo-WSlQ4BvBIH0Zkjg3B0nQL-SUi1t5Z2EQpVs3gABekDGxsGztkA4UB76kC0QAHhIIZYyD1shwyDDooYQw86NiDiWcBBpmLghXFAcavwGRLEMUGfwHi6SmSgN5HkQUQoQH8IE0KvjvJHAnsWEOED9QSPQOaUKEAYAUOdM8BAbwPiJHhCAW49xmTZLOMgO0O0dYSkyNkU0EQixGzkaI8REBxyD28eEw48RB6hIgK0o2pSC6N2pEw2xDD9Z1KzA0nhZcbHJhjvKJUuUrDDkqIkEEOMjaD2Rq1Q4yB1mEKqcPFIMA9SjyEbwVO09GyySsNcAqhAyAGODK2amIZaaDRIKMLq6T351X-riWwQDHlFWGTmKZBxhnZOuZdWhFyXRzxtAcc+K815wA3pCWoCBNCgMDL0F4aY6pxmWJsU+rDEgIsvpBaCt84IkAfjPN0LCQyZA+AcOA+Tzh1TeEvAlgJL50IlLwEq5RQKIHOIM6ZxKWKxINBfYVPDGx82zvynugrWUylGuAMAVjZriiLobBkFczaQmrkI8EtswEsuFW7Xpc1Khai3DuPcB4lqCE2stFavSQWFSYhK+xcKhVYAZO9V6P0hgkBtXarUu59wajOY-RBLZ7YTVhZmG05pyK8F4EzEpwpzmCSpNymVmqz5LwvqvK+FKnwkCGLKZaaERSyS1A+d05BK5cuaJWKB2ci3LzJdfGCaZ9HDjHJOVUydZyLlXOuTc24I0OujV7bWGEdUlyuvnEg+rsFGrpECf+8Zz7ctLd1Egg8u0lvAuSm+T5jg2j7Z3Btj4eB2zbRmZ2iRR5lyiR6323qRngj9cAANBEOG-mDSQZaLqVqCCibJeOlBRTOzlORLq+LrS7VVmpFMaY90soPWQOg6YfSckxYXCIjE4Zl1kpgEgyRyEHA0Smc8ELASqTOK0PeYA8OPAeUfGmaZXmfMPj83AfzyMujUQkcITRCJrs-cS9h4EPhtCoNNI2U9eRgAKqRBd2rsjF1Lqu9d5tLb3gzerdWOC+ZAMWoPQdE4k4znnMuNcG5w2RoPIcEWb7vZRPlQyX2LdNWNkXTp3VRsrleExewy1ZcyQydgQahA4KvCQt6fxRsqWjg9ksOoZgmhtC6B4PwIQogJDSDkIoJQJRbCPgqK4Dw4W1L+ECNoUgYQIjRBI3AbQ6QAiENa3kDYUpijWCq+UKoNQ6iAkaM0DOakOiFyoFMCwCwojACTFQccoxxjZCiCofIeJChpEOFl7LuXgj5f0EVowpXTBKGYJYIAA)

* TypeScript

  ```ts
  import { DurableObject } from "cloudflare:workers";
  import * as puppeteer from "@cloudflare/puppeteer";


  interface Env {
    MYBROWSER: Fetcher;
    BUCKET: R2Bucket;
    BROWSER: DurableObjectNamespace;
  }


  export default {
    async fetch(request, env): Promise<Response> {
      const obj = env.BROWSER.getByName("browser");


      // Send a request to the Durable Object, then await its response
      const resp = await obj.fetch(request);


      return resp;
    },
  } satisfies ExportedHandler<Env>;


  const KEEP_BROWSER_ALIVE_IN_SECONDS = 60;


  export class Browser extends DurableObject<Env> {
    private browser?: puppeteer.Browser;
    private keptAliveInSeconds: number = 0;
    private storage: DurableObjectStorage;


    constructor(state: DurableObjectState, env: Env) {
      super(state, env);
      this.storage = state.storage;
    }


    async fetch(request: Request): Promise<Response> {
      // Screen resolutions to test out
      const width: number[] = [1920, 1366, 1536, 360, 414];
      const height: number[] = [1080, 768, 864, 640, 896];


      // Use the current date and time to create a folder structure for R2
      const nowDate = new Date();
      const coeff = 1000 * 60 * 5;
      const roundedDate = new Date(
        Math.round(nowDate.getTime() / coeff) * coeff,
      ).toString();
      const folder = roundedDate.split(" GMT")[0];


      // If there is a browser session open, re-use it
      if (!this.browser || !this.browser.isConnected()) {
        console.log(`Browser DO: Starting new instance`);
        try {
          this.browser = await puppeteer.launch(this.env.MYBROWSER);
        } catch (e) {
          console.log(
            `Browser DO: Could not start browser instance. Error: ${e}`,
          );
        }
      }


      // Reset keptAlive after each call to the DO
      this.keptAliveInSeconds = 0;


      // Check if browser exists before opening page
      if (!this.browser) return new Response("Browser launch failed", { status: 500 });


      const page = await this.browser.newPage();


      // Take screenshots of each screen size
      for (let i = 0; i < width.length; i++) {
        await page.setViewport({ width: width[i], height: height[i] });
        await page.goto("https://workers.cloudflare.com/");
        const fileName = `screenshot_${width[i]}x${height[i]}`;
        const sc = await page.screenshot();


        await this.env.BUCKET.put(`${folder}/${fileName}.jpg`, sc);
      }


      // Close tab when there is no more work to be done on the page
      await page.close();


      // Reset keptAlive after performing tasks to the DO
      this.keptAliveInSeconds = 0;


      // Set the first alarm to keep DO alive
      const currentAlarm = await this.storage.getAlarm();
      if (currentAlarm == null) {
        console.log(`Browser DO: setting alarm`);
        const TEN_SECONDS = 10 * 1000;
        await this.storage.setAlarm(Date.now() + TEN_SECONDS);
      }


      return new Response("success");
    }


    async alarm(): Promise<void> {
      this.keptAliveInSeconds += 10;


      // Extend browser DO life
      if (this.keptAliveInSeconds < KEEP_BROWSER_ALIVE_IN_SECONDS) {
        console.log(
          `Browser DO: has been kept alive for ${this.keptAliveInSeconds} seconds. Extending lifespan.`,
        );
        await this.storage.setAlarm(Date.now() + 10 * 1000);
        // You can ensure the ws connection is kept alive by requesting something
        // or just let it close automatically when there is no work to be done
        // for example, `await this.browser.version()`
      } else {
        console.log(
          `Browser DO: exceeded life of ${KEEP_BROWSER_ALIVE_IN_SECONDS}s.`,
        );
        if (this.browser) {
          console.log(`Closing browser.`);
          await this.browser.close();
        }
      }
    }
  }
  ```

## 6. Test

Run `npx wrangler dev` to test your Worker locally.

Use real headless browser during local development

To interact with a real headless browser during local development, set `"remote" : true` in the Browser binding configuration. Learn more in our [remote bindings documentation](https://developers.cloudflare.com/workers/development-testing/#remote-bindings).

## 7. Deploy

Run [`npx wrangler deploy`](https://developers.cloudflare.com/workers/wrangler/commands/#deploy) to deploy your Worker to the Cloudflare global network.

## Related resources

* Other [Puppeteer examples](https://github.com/cloudflare/puppeteer/tree/main/examples)
* Get started with [Durable Objects](https://developers.cloudflare.com/durable-objects/get-started/)
* [Using R2 from Workers](https://developers.cloudflare.com/r2/api/workers/workers-api-usage/)
