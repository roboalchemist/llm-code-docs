# Source: https://upstash.com/docs/qstash/howto/local-development.md

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

<img src="https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=20d1ab6f53a1b4b9c8f24a64af6a32d6" data-og-width="1210" width="1210" data-og-height="685" height="685" data-path="img/qstash/local-mode-qstash.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=280&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=1a0ef1c06088f89ee1fe510841972291 280w, https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=560&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=f89f092b33563c1fa6dc042e2345885f 560w, https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=840&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=8684c719b514bea30defa1691cfe7470 840w, https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=1100&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=a91cf6673fb6d2f605d3c8b8d846a970 1100w, https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=1650&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=6939a3d2fe01dc2dd65c64af8bd52d97 1650w, https://mintcdn.com/upstash/6b7_cWf_Wv8tb6kI/img/qstash/local-mode-qstash.png?w=2500&fit=max&auto=format&n=6b7_cWf_Wv8tb6kI&q=85&s=14ca23e0fd7512f4129006282380460b 2500w" />

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
