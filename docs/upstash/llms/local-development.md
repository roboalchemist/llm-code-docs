# Source: https://upstash.com/docs/qstash/howto/local-development.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Local Development

QStash requires a publicly available API to send messages to.
During development when applications are not yet deployed, developers typically need to expose their local API by creating a public tunnel.
While local tunneling works seamlessly, it requires code changes between development and production environments and increase friction for developers.
To simplify the development process, Upstash provides QStash CLI, which allows you to run a development server locally for testing and development.

<Check>The development server fully supports all QStash features including Schedules, URL Groups, Workflows, and Event Logs.</Check>

<Note>Since the development server operates entirely in-memory, all data is reset when the server restarts.</Note>

You can download and run the QStash CLI executable binary in several ways:

## NPX (Node Package Executable)

Install the binary via the `@upstash/qstash-cli` NPM package:

```javascript  theme={"system"}
npx @upstash/qstash-cli dev

// Start on a different port
npx @upstash/qstash-cli dev -port=8081
```

Once you start the local server, you can go to the QStash tab on Upstash Console and enable local mode, which will allow you to publish requests and monitor messages with the local server.

<img src="https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=58fbc8985876843b0cd09c538db3c5a7" data-og-width="2042" width="2042" data-og-height="1668" height="1668" data-path="img/qstash/local-mode-qstash.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=280&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=fb1253979246bb92a20f80df959a3bb2 280w, https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=560&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=84bd6595b419e2a24bcb961eb08fc89b 560w, https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=840&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=af4475a102e034d7d1871d16472c0be4 840w, https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=1100&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=fb29733b83d961e5b3cdefbd8baa9a80 1100w, https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=1650&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=e903480c4783cce05f0f9d37017d277e 1650w, https://mintcdn.com/upstash/HUgsoYK-cQi-Kk4T/img/qstash/local-mode-qstash.png?w=2500&fit=max&auto=format&n=HUgsoYK-cQi-Kk4T&q=85&s=f928845a2f61badf0802f55df38ca04f 2500w" />

## Docker

QStash CLI is available as a Docker image through our public AWS ECR repository:

```javascript  theme={"system"}
// Pull the image
docker pull public.ecr.aws/upstash/qstash:latest

// Run the image
docker run -p 8080:8080 public.ecr.aws/upstash/qstash:latest qstash dev
```

## Artifact Repository

You can download the binary directly from our artifact repository without using a package manager:

[https://artifacts.upstash.com/#qstash/versions/](https://artifacts.upstash.com/#qstash/versions/)

Select the appropriate version, architecture, and operating system for your platform.
After extracting the archive file, run the executable:

```
$ ./qstash dev
```

## QStash CLI

Currently, the only available command for QStash CLI is `dev`, which starts a development server instance.

```
$ ./qstash dev --help
Usage of dev:
  -port int
        The port to start HTTP server at [env QSTASH_DEV_PORT] (default 8080)
  -quota string
        The quota of users [env QSTASH_DEV_QUOTA] (default "payg")
```

There are predefined test users available. You can configure the quota type of users using the `-quota` option, with available options being `payg` and `pro`.
These quotas don't affect performance but allow you to simulate different server limits based on the subscription tier.

After starting the development server using any of the methods above, it will display the necessary environment variables.
Select and copy the credentials from one of the following test users:

<CodeGroup>
  ```javascript User 1 theme={"system"}
  QSTASH_URL="http://localhost:8080"
  QSTASH_TOKEN="eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0="
  QSTASH_CURRENT_SIGNING_KEY="sig_7kYjw48mhY7kAjqNGcy6cr29RJ6r"
  QSTASH_NEXT_SIGNING_KEY="sig_5ZB6DVzB1wjE8S6rZ7eenA8Pdnhs"
  ```

  ```javascript User 2 theme={"system"}
  QSTASH_URL="http://localhost:8080"
  QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjEiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
  QSTASH_CURRENT_SIGNING_KEY="sig_7GVPjvuwsfqF65iC8fSrs1dfYruM"
  QSTASH_NEXT_SIGNING_KEY="sig_5NoELc3EFnZn4DVS5bDs2Nk4b7Ua"
  ```

  ```javascript User 3 theme={"system"}
  QSTASH_URL="http://localhost:8080"
  QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjIiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
  QSTASH_CURRENT_SIGNING_KEY="sig_6jWGaWRxHsw4vMSPJprXadyvrybF"
  QSTASH_NEXT_SIGNING_KEY="sig_7qHbvhmahe5GwfePDiS5Lg3pi6Qx"
  ```

  ```javascript User 4 theme={"system"}
  QSTASH_URL="http://localhost:8080"
  QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjMiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
  QSTASH_CURRENT_SIGNING_KEY="sig_5T8FcSsynBjn9mMLBsXhpacRovJf"
  QSTASH_NEXT_SIGNING_KEY="sig_7GFR4YaDshFcqsxWRZpRB161jguD"
  ```
</CodeGroup>

<Info>Currently, there is no GUI client available for the development server. You can use QStash SDKs to fetch resources like event logs.</Info>

## License

The QStash development server is licensed under the [Development Server License](/qstash/misc/license), which restricts its use to development and testing purposes only.
It is not permitted to use it in production environments. Please refer to the full license text for details.
