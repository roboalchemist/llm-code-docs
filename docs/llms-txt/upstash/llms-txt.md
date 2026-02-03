# Source: https://upstash.com/docs/workflow/llms-txt.md

# Source: https://upstash.com/docs/vector/overall/llms-txt.md

# Source: https://upstash.com/docs/redis/overall/llms-txt.md

# Source: https://upstash.com/docs/qstash/overall/llms-txt.md

### Install and Run Next.js App with QStash

Source: https://upstash.com/docs/qstash/overall/llms-txt

This snippet covers the initial setup of a Next.js project, including installation of the QStash package and running the development server. It requires Node.js and npm to be installed.

```APIDOC
## Install and Run Next.js App with QStash

### Description
This snippet covers the initial setup of a Next.js project, including installation of the QStash package and running the development server. It requires Node.js and npm to be installed.

### Method
Shell Commands

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
npx create-next-app@latest qstash-bg-job
cd qstash-bg-job
npm install @upstash/qstash
npm run dev
```

### Response
N/A
```

--------------------------------

### Initialize Next.js App and Install QStash

Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs

This snippet shows the commands to create a new Next.js application, navigate into its directory, install the Upstash QStash npm package, and start the development server. Ensure Node.js is installed before running these commands.

```bash
npx create-next-app@latest qstash-bg-job
cd qstash-bg-job
npm install @upstash/qstash
npm run dev
```

--------------------------------

### Project Setup with C3 CLI (npm)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initiates a new Cloudflare worker project using the create-cloudflare-cli (C3) with npm. Guides through project configuration and installs Wrangler.

```APIDOC
## Project Setup with C3 CLI (npm)

### Description
Initiates a new Cloudflare worker project using the create-cloudflare-cli (C3) with npm. Guides through project configuration and installs Wrangler.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```shell
npm create cloudflare@latest
```

### Response
N/A
```

--------------------------------

### Project Setup with C3 CLI (yarn)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initiates a new Cloudflare worker project using the create-cloudflare-cli (C3) with yarn. Guides through project configuration and installs Wrangler.

```APIDOC
## Project Setup with C3 CLI (yarn)

### Description
Initiates a new Cloudflare worker project using the create-cloudflare-cli (C3) with yarn. Guides through project configuration and installs Wrangler.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```shell
yarn create cloudflare@latest
```

### Response
N/A
```

--------------------------------

### Project Setup with C3 (npm)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This command uses npm to initiate a new Cloudflare worker project using the create-cloudflare-cli (C3). It guides the user through project configuration, including directory, template, and language selection. C3 also installs Wrangler for testing and deployment.

```APIDOC
## Project Setup with C3 (npm)

### Description
This command uses npm to initiate a new Cloudflare worker project using the create-cloudflare-cli (C3). It guides the user through project configuration, including directory, template, and language selection. C3 also installs Wrangler for testing and deployment.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```shell
npm create cloudflare@latest
```

### Response
N/A
```

--------------------------------

### Fly.io Application Initialization Command

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Launches a new application on fly.io, prompting the user for configuration details such as app name and region. It automatically detects the Go application and sets up the necessary `fly.toml` configuration file. The command provides options to skip database setup and immediate deployment.

```bash
$ flyctl launch
Creating app in /Users/andreasthomas/github/upstash/qstash-examples/fly.io/go
Scanning source code
Detected a Go app
Using the following build configuration:
        Builder: paketobuildpacks/builder:base
        Buildpacks: gcr.io/paketo-buildpacks/go
? App Name (leave blank to use an auto-generated name):
Automatically selected personal organization: Andreas Thomas
? Select region: fra (Frankfurt, Germany)
Created app winer-cherry-9545 in organization personal
Wrote config file fly.toml
? Would you like to setup a Postgresql database now? No
? Would you like to deploy now? No
Your app is ready. Deploy with `flyctl deploy`
```

--------------------------------

### Project Setup with C3 (yarn)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This command uses yarn to initiate a new Cloudflare worker project using the create-cloudflare-cli (C3). It guides the user through project configuration, including directory, template, and language selection. C3 also installs Wrangler for testing and deployment.

```APIDOC
## Project Setup with C3 (yarn)

### Description
This command uses yarn to initiate a new Cloudflare worker project using the create-cloudflare-cli (C3). It guides the user through project configuration, including directory, template, and language selection. C3 also installs Wrangler for testing and deployment.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```shell
yarn create cloudflare@latest
```

### Response
N/A
```

--------------------------------

### Get Queue Details Response Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example success response for retrieving queue details. Includes the queue name and its current parallelism setting.

```json
{
  "queueName": "my-queue",
  "parallelism": 5
}
```

--------------------------------

### Create Schedule (SDK Examples)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Examples of creating a schedule using QStash SDKs for TypeScript and Python, including query parameters for destination and cron, and an optional request body.

```APIDOC
## POST /v2/schedules

### Description
Creates a new schedule to send a message at a specific time or on a recurring basis.

### Method
POST

### Endpoint
/v2/schedules

### Parameters
#### Query Parameters
- **destination** (string) - Required - The URL to which the task will be sent.
- **cron** (string) - Required - The cron expression defining the schedule. Use `CRON_TZ=[Timezone]` prefix to specify a timezone (e.g., `CRON_TZ=America/New_York 0 4 * * *`).

#### Request Body
- **body** (object) - Optional - The payload to send with the request.
  - **field** (any) - Description

### Request Example
#### TypeScript
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  cron: "CRON_TZ=America/New_York 0 4 * * *",
});
```

#### Python
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="https://example.com",
    cron="CRON_TZ=America/New_York 0 4 * * *",
)
```

#### cURL
```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Cron: CRON_TZ=America/New_York 0 4 * * *" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

### Response
#### Success Response (200)
- **scheduleId** (string) - The unique identifier for the created schedule.

#### Response Example
```json
{
  "scheduleId": "schedule_abc123"
}
```
```

--------------------------------

### Create and Get Queue with Parallelism (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Shows how to create or update a queue with a specific parallelism level using the QStash Python client, then retrieve and print its configuration. Assumes the QStash client is installed and a valid QSTASH_TOKEN is available.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")

queue_name = "upstash-queue"
client.queue.upsert(queue_name, parallelism=2)

print(client.queue.get(queue_name))
```

--------------------------------

### Start Background Job API Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

An example of a Next.js API route handler that receives user data and publishes a JSON message to a QStash endpoint for background job processing. It dynamically constructs the background job endpoint URL.

```APIDOC
## POST /api/start-background-job

### Description
Starts a background job by publishing a JSON message to a QStash endpoint.

### Method
POST

### Endpoint
/api/start-background-job

### Parameters
#### Request Body
- **users** (string[]) - Required - A list of user identifiers.

### Request Example
```json
{
  "users": ["user1", "user2"]
}
```

### Response
#### Success Response (200)
- **message** (string) - Indicates that the job has been started.

#### Response Example
```json
"Job started"
```
```

--------------------------------

### Initialize AWS CDK Project and Install Dependencies

Source: https://upstash.com/docs/qstash/overall/llms-txt

This snippet demonstrates the bash commands to create a new AWS CDK project using TypeScript, install the Upstash QStash SDK, and set up the basic file structure for a Lambda function.

```APIDOC
## Initialize AWS CDK Project and Install Dependencies

### Description
This snippet demonstrates the bash commands to create a new AWS CDK project using TypeScript, install the Upstash QStash SDK, and set up the basic file structure for a Lambda function.

### Method
Project Initialization (Bash)

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
mkdir my-app
cd my-app
cdk init app -l typescript
npm i esbuild @upstash/qstash
mkdir lambda
touch lambda/index.ts
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### Install QStash Python Package

Source: https://upstash.com/docs/qstash/sdks/py/gettingstarted

Installs the QStash Python client library using pip. This is the first step to using QStash in your Python projects.

```bash
pip install qstash
```

--------------------------------

### Install Vercel CLI

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the Vercel Command Line Interface (CLI) globally, which is used for deploying projects to Vercel.

```APIDOC
## Install Vercel CLI

### Description
Installs the Vercel Command Line Interface (CLI) globally, which is used for deploying projects to Vercel.

### Method
Installation (Bash)

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
npm install -g vercel
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### Project Setup

Source: https://upstash.com/docs/qstash/overall/llms-txt

Commands to initialize a new directory for a Python application and navigate into it, setting up the basic project structure.

```APIDOC
## Project Setup

### Description
Initializes a new directory for the Python application and navigates into it.

### Method
Shell Commands

### Endpoint
N/A

### Parameters
None

### Request Example (Bash)
```bash
mkdir aws-lambda
cd aws-lambda
touch lambda_function.py
```
```

--------------------------------

### Create Python Project Directory

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

Creates a new directory for the Python application and navigates into it. This is the initial setup step for the project.

```bash
mkdir clean-db-cron
cd clean-db-cron
```

--------------------------------

### Install @upstash/qstash via NPM

Source: https://upstash.com/docs/qstash/overall/llms-txt

This command installs the Upstash QStash SDK using npm. Ensure you have Node.js and npm installed on your system.

```APIDOC
## Install @upstash/qstash via NPM

### Description
This command installs the Upstash QStash SDK using npm. Ensure you have Node.js and npm installed on your system.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
npm install @upstash/qstash
```

### Response
N/A
```

--------------------------------

### Publish JSON with Callback and GET Method (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message to a URL, specifying a callback URL for receiving the response and a failure callback URL. The HTTP method is set to GET, and the default is POST. This is useful for long-running functions where you need to be notified of the result.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    callback="https://my-callback...",
    failure_callback="https://my-failure-callback...",
    method="GET",
)
```

--------------------------------

### Install QStash Python SDK

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the QStash Python SDK using pip. This is the first step to integrate QStash into your Python application.

```APIDOC
## Install QStash Python SDK

### Description
Installs the QStash Python SDK using pip. This is the first step to integrate QStash into your Python application.

### Method
Shell Command

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
pip install qstash
```

### Response
N/A
```

--------------------------------

### Initialize Golang Project for fly.io

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Creates a new directory and initializes a Go module for a new project. This is the first step in setting up the Golang application.

```bash
mkdir flyio-go
cd flyio-go
go mod init flyio-go
```

--------------------------------

### Install Upstash Packages

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the required Upstash QStash and Redis packages for a Node.js project.

```APIDOC
## Install Upstash Packages with npm

### Description
Installs the required Upstash QStash and Redis packages for a Node.js project. These packages enable integration with QStash for scheduled tasks and Redis for data storage.

### Method
N/A (CLI Command)

### Command
`npm install @upstash/qstash @upstash/redis`

### Usage
1. Ensure you have Node.js and npm installed.
2. Navigate to your project directory.
3. Run the install command: `npm install @upstash/qstash @upstash/redis`
```

--------------------------------

### Install Vercel CLI for deployment

Source: https://upstash.com/docs/qstash/overall/llms-txt

This bash command installs the Vercel Command Line Interface (CLI) globally on your system. The Vercel CLI is used for deploying projects to Vercel, a platform for frontend developers.

```APIDOC
## Install Vercel CLI for deployment

### Description
This bash command installs the Vercel Command Line Interface (CLI) globally on your system. The Vercel CLI is used for deploying projects to Vercel, a platform for frontend developers.

### Method
Installation (Bash)

### Endpoint
N/A

### Parameters
None

### Request Example
```bash
npm install -g vercel
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### Publish Message (Example)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of publishing a message using curl, including a placeholder for the QStash token.

```APIDOC
## GET /v2/publish

### Description
This is an example endpoint for publishing a message, demonstrating the use of query parameters and authentication.

### Method
GET

### Endpoint
/v2/publish/

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash authentication token.

### Request Example (Query Parameter)
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Notes
- Always keep your token secure.
- Reset your token if you suspect it has been compromised.
```

--------------------------------

### Flow Control Key Response Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example success response for fetching Flow Control key details. Includes the key name and the current waitlist size.

```json
{
  "flowControlKey": "my_key",
  "waitlistSize": 5
}
```

--------------------------------

### Get Message Logs

Source: https://upstash.com/docs/qstash/overall/apiexamples

Retrieve logs for all messages that have been published. Filtering options are available to refine the results.

```APIDOC
## GET /v2/logs

### Description
Retrieves logs for published messages. Filtering can be applied to narrow down the results.

### Method
GET

### Endpoint
`/v2/logs`

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - Bearer token for authentication.

#### Query Parameters
- **(Various)** - Optional - Filtering parameters may be available (e.g., by message ID, status, date range). Refer to specific documentation for details.

### Response
#### Success Response (200)
- **(array)** - An array of log objects, each containing details about a published message.

#### Response Example
```json
[
  {
    "messageId": "msg_abc123",
    "status": "delivered",
    "timestamp": "2023-10-27T10:00:00Z"
  }
]
```
```

--------------------------------

### Create and Get a Queue with Parallelism (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This snippet demonstrates how to create or update a queue with a specified parallelism level using the QStash Python client. It then retrieves and prints the queue's configuration. Ensure you have the QStash client installed and a valid QSTASH_TOKEN.

```APIDOC
## Create and Get a Queue with Parallelism (Python)

### Description
This snippet demonstrates how to create or update a queue with a specified parallelism level using the QStash Python client. It then retrieves and prints the queue's configuration. Ensure you have the QStash client installed and a valid QSTASH_TOKEN.

### Method
Queue Management (Python)

### Endpoint
N/A

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")

queue_name = "upstash-queue"
client.queue.upsert(queue_name, parallelism=2)

print(client.queue.get(queue_name))
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### Publish a Message to QStash using cURL

Source: https://upstash.com/docs/qstash/quickstarts/deno-deploy

This bash command demonstrates how to publish a message to a QStash endpoint using cURL. It sends a POST request to a specified Deno deploy URL with the necessary Authorization header (using a QSTASH_TOKEN) and a JSON payload. This is useful for testing the webhook receiver setup.

```bash
curl --request POST "https://qstash.upstash.io/v2/publish/https://early-frog-33.deno.dev" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{ \"hello\": \"world\"}"
```

--------------------------------

### Deploy to Vercel

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

Initiates the deployment process to Vercel using the Vercel CLI. This command will guide you through the deployment steps, including selecting a project and framework.

```bash
vercel
```

--------------------------------

### Install Vercel CLI

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

Installs the Vercel Command Line Interface globally using npm. This tool is used for deploying the Python application to Vercel.

```bash
npm install -g vercel
```

--------------------------------

### GET /v2/keys

Source: https://upstash.com/docs/qstash/api-refence/signing-keys/get-signing-keys

Retrieve your current and next signing keys.

```APIDOC
## GET /v2/keys

### Description
Retrieve your current and next signing keys.

### Method
GET

### Endpoint
/v2/keys

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - QStash authentication token passed as a query parameter

### Request Example
```json
{
  "example": ""
}
```

### Response
#### Success Response (200)
- **current** (string) - The current signing key.
- **next** (string) - The next signing key.

#### Response Example
```json
{
  "current": "your_current_signing_key",
  "next": "your_next_signing_key"
}
```
```

--------------------------------

### Deploy Application to Fly.io (Bash)

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Deploys the application to the Fly.io platform using the `flyctl deploy` command. This command handles the build and deployment process for your application. Ensure your `fly.toml` configuration is set up correctly.

```bash
flyctl deploy
```

--------------------------------

### Create Schedule Example (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example using curl to create a new schedule for sending messages. It requires an Authorization header, Content-Type, an Upstash-Cron expression, and the destination URL. An optional JSON payload can be included.

```bash
curl -XPOST \
    -H 'Authorization: Bearer <QSTASH_TOKEN>'
    -H "Content-type: application/json" \
    -H "Upstash-Cron: 0 0 * * *" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

--------------------------------

### Get Queue Details Success Response Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This JSON object details a successful response when fetching information about a specific queue. It includes the queue's name, creation and update times, parallelism settings, pause status, and message lag.

```json
{
  "name": "my-queue",
  "createdAt": 1678886400000,
  "updatedAt": 1678886400000,
  "parallelism": 10,
  "paused": false,
  "lag": 0
}
```

--------------------------------

### QStash Library Installation

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the official Upstash QStash library for Node.js. This library provides the necessary tools to interact with QStash services, including receiving and verifying webhooks.

```APIDOC
## QStash Library Installation

### Description
Installs the official Upstash QStash library for Node.js. This library provides the necessary tools to interact with QStash services, including receiving and verifying webhooks.

### Command
```bash
npm install @upstash/qstash
```
```

--------------------------------

### Publish JSON Message API Example (POST /v2/publish/{url})

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides an example of publishing a simple JSON message to a specified endpoint using the QStash API. It details the HTTP method, endpoint, required parameters, request body, and expected success response.

```json
{
  "messageId": "msg_abc123"
}
```

--------------------------------

### Get Queue Details Error Response Examples (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

These JSON objects illustrate potential error responses when attempting to retrieve queue details. One indicates an invalid queue name, while the other signifies that the queue was not found.

```json
{
  "error": "Queue name is invalid. Queue names can only contain alphanumeric characters, hyphens, periods, and underscores."
}
```

```json
{
  "error": "Queue not found"
}
```

--------------------------------

### POST /v2/publish/{urlGroup}

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a message to a URL Group for fan-out delivery.

```APIDOC
## POST /v2/publish/{urlGroup}

### Description
Publish a message to a URL Group for fan-out delivery to multiple endpoints.

### Method
POST

### Endpoint
`/v2/publish/<urlGroup>`

### Parameters
#### Path Parameters
- **urlGroup** (string) - Required - The name of the URL Group.

#### Query Parameters
None

#### Request Body
- **body** (object) - Required - The JSON payload of the message.
- **delay** (string) - Optional - The delay before publishing the message (e.g., "5m").
- **headers** (object) - Optional - Custom headers to include in the request.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Setup ngrok Authentication Token (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This bash command configures ngrok with your authentication token, which is necessary for establishing secure tunnels to your local development environment.

```bash
ngrok config add-authtoken XXX
```

--------------------------------

### Start ngrok Tunnel to Local Server (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This bash command starts an ngrok tunnel, forwarding external requests to your local server running on port 3000. This allows you to expose your local application to the internet.

```bash
$ ngrok http 3000
```

--------------------------------

### POST /v2/publish/{url}

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a message to a specific endpoint URL.

```APIDOC
## POST /v2/publish/{url}

### Description
Publish a message to a specific endpoint URL.

### Method
POST

### Endpoint
`/v2/publish/<url>`

### Parameters
#### Path Parameters
- **url** (string) - Required - The endpoint URL to publish the message to.

#### Query Parameters
None

#### Request Body
- **body** (object) - Required - The JSON payload of the message.
- **delay** (string) - Optional - The delay before publishing the message (e.g., "5m").
- **headers** (object) - Optional - Custom headers to include in the request.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Deploy Python App to Vercel CLI

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the Vercel CLI globally and initiates the deployment process for a Python application. Assumes the application is set up for deployment in the current directory.

```bash
npm install -g vercel
vercel
```

--------------------------------

### Next.js Workflow API Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Illustrates a POST request example for the /api/workflow endpoint in a Next.js application using Upstash QStash Workflow. It shows the required request body parameters.

```json
{
  "userId": "user123",
  "email": "test@example.com",
  "name": "John Doe"
}
```

--------------------------------

### Publish JSON with Callback URL, Method, and Failure Callback

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a URL, specifying a callback URL for the response, a failure callback URL, and setting the HTTP method to GET. Useful for long-running functions. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  callback: "https://my-callback...",
  failureCallback: "https://my-failure-callback...",
  method: "GET",
});
```

--------------------------------

### List All Schedules

Source: https://upstash.com/docs/qstash/overall/apiexamples

Retrieves a list of all scheduled messages.

```APIDOC
## GET /v2/schedules

### Description
Retrieves a list of all schedules for published messages.

### Method
GET

### Endpoint
`/v2/schedules`

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - Bearer token for authentication.

### Response
#### Success Response (200)
- **(array)** - An array of schedule objects, each containing details about a scheduled message.

#### Response Example
```json
[
  {
    "scheduleId": "sch_xyz789",
    "cronSyntax": "0 0 * * *",
    "message": {
      "url": "https://example.com",
      "body": {"hello": "world"}
    }
  }
]
```
```

--------------------------------

### Create Schedule Example (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example using curl to create a new schedule for sending messages. It requires an Authorization header with a Bearer token, a Content-Type, an Upstash-Cron expression for scheduling, and the destination URL. An optional JSON payload can be included in the request body.

```APIDOC
## Create Schedule Example (Bash)

Example using curl to create a new schedule for sending messages. It requires an Authorization header with a Bearer token, a Content-Type, an Upstash-Cron expression for scheduling, and the destination URL. An optional JSON payload can be included in the request body.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/schedules/<destination_url>`

### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Content-type** (string) - Required - `application/json`.
- **Upstash-Cron** (string) - Required - Cron expression for scheduling (e.g., `0 0 * * *`).

### Request Body
- **(Optional)** JSON payload to send with the scheduled message.

### Request Example
```bash
curl -XPOST \
    -H 'Authorization: Bearer <QSTASH_TOKEN>'
    -H "Content-type: application/json" \
    -H "Upstash-Cron: 0 0 * * *" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```
```

--------------------------------

### Publish Message Request Examples (cURL, TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to publish a JSON message to QStash using cURL for direct API interaction and the TypeScript SDK for programmatic access. Both examples include setting authorization, content type, and optional callback URLs.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Callback: https://example.com/callback" \
    -H "Upstash-Failure-Callback: https://example.com/failure" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  callback: "https://example.com/callback",
  failureCallback: "https://example.com/failure",
});
```

--------------------------------

### QStash Batch Request Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of a JSON payload for making a batch request to QStash. This payload consists of an array of objects, where each object specifies a destination URL.

```APIDOC
## QStash Batch Request Example

### Description
Example of a JSON payload for making a batch request to QStash. This payload consists of an array of objects, where each object specifies a destination URL.

### Request Example
```json
[
  {
    "destination": "https://example.com/destination1"
  },
  {
    "destination": "https://example.com/destination2"
  }
]
```
```

--------------------------------

### QStash LLM Batch Request Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

An example JSON payload demonstrating how to structure a batch request to the QStash API for LLM (Large Language Model) tasks. Each object in the array specifies the API to call, the provider (e.g., Anthropic) with its token, the message body for the LLM, and a callback URL for receiving the results.

```APIDOC
## QStash LLM Batch Request Example

### Description
An example JSON payload demonstrating how to structure a batch request to the QStash API for LLM (Large Language Model) tasks. Each object in the array specifies the API to call, the provider (e.g., Anthropic) with its token, the message body for the LLM, and a callback URL for receiving the results.

### Request Example
```json
[
  {
    "api": {
      "name": "llm",
      "provider": {
        "name": "anthropic",
        "token": "<ANTHROPIC_TOKEN>"
      }
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "messages": [{"role": "user", "content": "Describe the latest in AI research."}]
    },
    "callback": "https://example.com/callback1"
  },
  {
    "api": {
      "name": "llm",
      "provider": {
        "name": "anthropic",
        "token": "<ANTHROPIC_TOKEN>"
      }
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "messages": [{"role": "user", "content": "Outline the future of remote work."}]
    },
    "callback": "https://example.com/callback2"
  }
]
```
```

--------------------------------

### Install Upstash Redis Package (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Installs the necessary Python package 'upstash-redis' to interact with Upstash Redis databases. This package provides the client for database operations.

```bash
pip install upstash-redis

```

--------------------------------

### Get QStash Message Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve logs for published messages, with optional filtering capabilities. This allows monitoring message delivery and processing. The examples demonstrate how to fetch logs using curl, a TypeScript client, and a Python client.

```APIDOC
## Get QStash Message Logs

### Description
Retrieve logs for published messages, with optional filtering capabilities. This allows monitoring message delivery and processing. The examples demonstrate how to fetch logs using curl, a TypeScript client, and a Python client.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/logs`

### Parameters
#### Query Parameters
- **limit** (integer) - Optional - The maximum number of logs to return.
- **offset** (integer) - Optional - The number of logs to skip.
- **from** (integer) - Optional - Unix timestamp to filter logs from.
- **to** (integer) - Optional - Unix timestamp to filter logs until.

### Request Example
```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.event.list()
# Async version is also available
```

### Response
#### Success Response (200)
- **data** (array) - An array of log objects.
- **nextCursor** (string) - A cursor for fetching the next page of results.

#### Response Example
```json
{
  "data": [
    {
      "messageId": "msg_123",
      "status": "delivered",
      "createdAt": 1678886400,
      "url": "https://example.com/destination1"
    }
  ],
  "nextCursor": "cursor_abc"
}
```
```

--------------------------------

### Get QStash Message Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve logs for published messages, with optional filtering capabilities. This allows monitoring message delivery and processing. The examples demonstrate how to fetch logs using curl, a TypeScript client, and a Python client.

```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.event.list()
# Async version is also available
```

--------------------------------

### Publish Message with Custom Header using QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a JSON message with custom headers using QStash. Examples for cURL, Typescript, and Python SDKs are provided. Custom headers are prefixed with 'Upstash-Forward-' in cURL.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H 'Upstash-Forward-My-Header: my-value' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  headers: {
    "My-Header": "my-value",
  },
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    headers={
        "My-Header": "my-value",
    },
)
# Async version is also available
```

--------------------------------

### Install Upstash Redis Package

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

Installs the necessary Python package 'upstash-redis' to interact with the Upstash Redis database. This package handles the connection and operations.

```bash
pip install upstash-redis
```

--------------------------------

### Publish with Callback, Failure Callback, and GET Method

Source: https://upstash.com/docs/qstash/overall/llms-txt

Illustrates publishing a message with specified callback and failure callback URLs, and changing the HTTP method from POST to GET.

```APIDOC
## Publish with Callback, Failure Callback, and GET Method

### Description
This snippet illustrates publishing a message with specified callback and failure callback URLs. It also demonstrates changing the HTTP method from the default POST to GET. This is useful for long-running functions where QStash needs to return the response to a callback URL.

### Method
GET (or POST, PUT, DELETE, etc. as specified)

### Endpoint
`https://qstash.upstash.io/v2/publish/<URL>`

### Parameters
#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

#### Request Body (if applicable, depends on method)
- **body** (object) - Required - The JSON payload to send.

### Request Example (TypeScript)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  callback: "https://my-callback...",
  failureCallback: "https://my-failure-callback...",
  method: "GET",
});
```

### Response
#### Success Response (200)
(Response details depend on the specific endpoint and method being called)

#### Response Example
(Response example depends on the specific endpoint and method being called)
```

--------------------------------

### Publish Message to URL Group using QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a JSON message to a URL Group for fan-out delivery using QStash. Examples provided for cURL, Typescript, and Python SDKs. Requires authentication and a URL group name.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/myUrlGroup'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  urlGroup: "myUrlGroup",
  body: {
    hello: "world",
  },
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url_group="my-url-group",
    body={
        "hello": "world",
    },
)
# Async version is also available
```

--------------------------------

### Flow Control Key Not Found Error Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example error response when a Flow Control key is not found. Returns an error message indicating the key was not found.

```json
{
  "error": "Flow Control key not found"
}
```

--------------------------------

### QStash Publish Message Request Example (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of publishing a JSON message to a specified URL using the Upstash QStash TypeScript SDK. This shows how to configure the client and call the publishJSON method with message details and callback URLs.

```APIDOC
## QStash Publish Message Request Example (TypeScript)

### Description
Example of publishing a JSON message to a specified URL using the Upstash QStash TypeScript SDK. This shows how to configure the client and call the publishJSON method with message details and callback URLs.

### Request Example
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  callback: "https://example.com/callback",
  failureCallback: "https://example.com/failure",
});
```
```

--------------------------------

### Publish Message with Callback URLs

Source: https://upstash.com/docs/qstash/overall/apiexamples

Configure callback URLs to receive a response from the endpoint or to be notified of delivery failures.

```APIDOC
## POST /v2/publish/:url

### Description
Publishes a message to a specified URL and configures callback URLs for success and failure notifications.

### Method
POST

### Endpoint
`/v2/publish/:url`

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - Bearer token for authentication.
- **Content-type** (string) - Required - Specifies the content type of the request body, typically `application/json`.
- **Upstash-Callback** (string) - Optional - The URL to send the response to upon successful delivery.
- **Upstash-Failure-Callback** (string) - Optional - The URL to send the response to if delivery fails.

#### Request Body
- **(object)** - Required - The payload of the message to be published.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **(object)** - Details about the published message, including its ID.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Create Workflow with Steps (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Illustrates creating and executing a workflow with defined steps using the Upstash Workflow SDK for Python. This example involves sending emails and managing workflow context within a FastAPI application.

```python
# This is a conceptual example and requires the Upstash Workflow SDK setup.
# The actual implementation would involve defining workflow steps and execution logic.
# Example request body for creating a workflow:
# {
#   "userId": "user123",
#   "email": "user@example.com",
#   "name": "John Doe"
# }
```

--------------------------------

### Get Message Details using QStash API (cURL)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details for a specific message using its ID. This functionality is available only while the message is being processed by QStash. Requires authentication and the message ID as a path parameter. An example using cURL is provided.

```shell
curl https://qstash.upstash.io/v2/messages/msg_123 \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

--------------------------------

### Set up ngrok Tunnel and Publish Message

Source: https://upstash.com/docs/qstash/howto/local-tunnel

ngrok provides a public endpoint for your localhost. After signing up and configuring the authtoken, start an HTTP tunnel to your application's port. The 'Forwarding' URL can then be used as the QStash destination, with your API path appended. Debugging is available via the ngrok web interface.

```bash
ngrok config add-authtoken XXX
```

```bash
$ ngrok http 3000
```

```bash
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://e02f-2a02-810d-af40-5284-b139-58cc-89df-b740.eu.ngrok.io/api/webhooks'
```

--------------------------------

### Publish Message with Custom Retry Delay

Source: https://upstash.com/docs/qstash/overall/apiexamples

Configure the delay between retry attempts when message delivery fails. By default, QStash uses exponential backoff. You can customize this using mathematical expressions with the special variable `retried` (current retry attempt count starting from 0).

```APIDOC
## POST /v2/publish/:url

### Description
Publishes a message to a specified URL with custom retry delay configuration.

### Method
POST

### Endpoint
`/v2/publish/:url`

### Parameters
#### Header Parameters
- **Authorization** (string) - Required - Bearer token for authentication.
- **Upstash-Retries** (integer) - Optional - The number of times to retry sending the message.
- **Upstash-Retry-Delay** (string) - Optional - A mathematical expression defining the delay between retries. Supports `pow`, `sqrt`, `abs`, `exp`, `floor`, `ceil`, `round`, `min`, `max` and the variable `retried`.
- **Content-type** (string) - Required - Specifies the content type of the request body, typically `application/json`.

#### Request Body
- **(object)** - Required - The payload of the message to be published.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **(object)** - Details about the published message, including its ID.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Run QStash CLI Dev Server with Docker

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides instructions for running the QStash CLI development server locally using Docker. This involves pulling the latest QStash Docker image and then starting a container mapped to the host's port 8080.

```APIDOC
## Local Development with Docker

### Description
This section provides instructions on how to run the QStash CLI development server locally using Docker. This is useful for testing and development purposes.

### Steps

1.  **Pull the QStash Docker Image**
    *   **Command**: `docker pull public.ecr.aws/upstash/qstash:latest`
    *   **Description**: Fetches the latest QStash Docker image from the public ECR repository.

2.  **Run the Docker Container**
    *   **Command**: `docker run -p 8080:8080 public.ecr.aws/upstash/qstash:latest qstash dev`
    *   **Description**: Starts a QStash development server container. The `-p 8080:8080` flag maps port 8080 on your host machine to port 8080 inside the container, making the development server accessible.
```

--------------------------------

### Schedule Daily Task

Source: https://upstash.com/docs/qstash/overall/llms-txt

Examples for scheduling a daily task using QStash. This involves setting a cron schedule for a specific destination URL. Examples are provided for cURL, TypeScript, and Python.

```APIDOC
## Schedule Daily Task with QStash

### Description
This section provides examples for scheduling a task to run once a day using QStash. The cron syntax `0 0 * * *` ensures the task executes at midnight every day. Replace placeholders with your actual token and target URL.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/schedules/<destination_url>`

### Parameters
#### Request Headers
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`
- **Upstash-Cron** (string) - Required - Cron syntax for scheduling (e.g., `0 0 * * *` for daily at midnight)
- **Content-type** (string) - Required - `application/json`

#### Request Body
- **(JSON Object)** - Required - The payload for your task.

### Request Example (cURL)
```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Upstash-Cron: 0 0 * * *" \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

### Request Example (TypeScript SDK)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  cron: "0 0 * * *",
});
```

### Request Example (Python SDK)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="https://example.com",
    cron="0 0 * * *",
)
# Async version is also available
```

### Response
(Response details depend on the specific operation)
```

--------------------------------

### Initialize and Use Synchronous QStash Client (Python)

Source: https://upstash.com/docs/qstash/sdks/py/gettingstarted

Demonstrates how to initialize a synchronous QStash client with an authentication token and publish a JSON message. Requires the 'qstash' library.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(...)
```

--------------------------------

### POST /v2/batch

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish multiple messages in a single request. This is efficient for sending many messages at once.

```APIDOC
## POST /v2/batch

### Description
Send multiple messages in a single API request. This optimizes throughput for high-volume message sending.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/batch`

### Parameters
#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Content-type** (string) - Required - Must be `application/json`.

#### Request Body
- **(array)** - Required - An array of message objects, each with a `destination` field.
  - **destination** (string) - Required - The URL for each message.

### Request Example
```json
[
  {
    "destination": "https://example.com/destination1"
  },
  {
    "destination": "https://example.com/destination2"
  }
]
```

### Response
#### Success Response (200)
- **(array)** - An array of message IDs for the batch.

#### Response Example
```json
[
  "<message_id_1>",
  "<message_id_2>"
]
```
```

--------------------------------

### Initialize AWS Lambda Project with QStash (Bash)

Source: https://upstash.com/docs/qstash/quickstarts/aws-lambda/nodejs

This snippet demonstrates the initial steps to set up a new AWS Lambda project using the AWS CDK, including creating a directory, initializing a TypeScript application, and installing necessary npm packages like @upstash/qstash.

```bash
mkdir my-app
cd my-app
cdk init app -l typescript
npm i esbuild @upstash/qstash
mkdir lambda
touch lambda/index.ts
```

--------------------------------

### Get Queue Details (HTTP)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Shows how to retrieve the configuration details for a specific QStash queue using an HTTP GET request. This includes information like the queue's name and its current parallelism setting.

```http
GET /v2/queues/{queueName}
```

--------------------------------

### Install Upstash Packages with npm

Source: https://upstash.com/docs/qstash/recipes/periodic-data-updates

Installs the necessary Upstash packages for QStash and Redis. These packages enable integration with Upstash services for messaging and data storage.

```bash
npm install @upstash/qstash @upstash/redis
```

--------------------------------

### Deploy Golang App on fly.io (Bash)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Launches a new application on fly.io, automatically detecting the Go environment. This command generates a `fly.toml` configuration file and prompts for necessary application details such as name and region. It advises setting up environment variables before deployment.

```bash
$ flyctl launch
Creating app in /Users/andreasthomas/github/upstash/qstash-examples/fly.io/go
Scanning source code
Detected a Go app
Using the following build configuration:
        Builder: paketobuildpacks/builder:base
        Buildpacks: gcr.io/paketo-buildpacks/go
? App Name (leave blank to use an auto-generated name):
Automatically selected personal organization: Andreas Thomas
? Select region: fra (Frankfurt, Germany)
Created app winer-cherry-9545 in organization personal
Wrote config file fly.toml
? Would you like to setup a Postgresql database now? No
? Would you like to deploy now? No
Your app is ready. Deploy with `flyctl deploy`

```

--------------------------------

### Get Signing Keys OpenAPI Specification

Source: https://upstash.com/docs/qstash/api-refence/signing-keys/get-signing-keys

This OpenAPI 3.1.0 specification defines the '/v2/keys' endpoint for the QStash REST API. It outlines the GET request to retrieve current and next signing keys, including response schemas and authentication methods.

```yaml
openapi: 3.1.0
info:
  title: QStash REST API
  description: |
    QStash is a message queue and scheduler built on top of Upstash Redis.
  version: 2.0.0
  contact:
    name: Upstash
    url: https://upstash.com
servers:
  - url: https://qstash.upstash.io
security:
  - bearerAuth: []
  - bearerAuthQuery: []
tags:
  - name: Messages
    description: Publish and manage messages
  - name: Queues
    description: Manage message queues
  - name: Schedules
    description: Create and manage scheduled messages
  - name: URL Groups
    description: Manage URL groups and endpoints
  - name: DLQ
    description: Dead Letter Queue operations
  - name: Logs
    description: Log operations
  - name: Signing Keys
    description: Manage signing keys
  - name: Flow Control
    description: Monitor flow control keys
paths:
  /v2/keys:
    get:
      tags:
        - Signing Keys
      summary: Get Signing Keys
      description: Retrieve your current and next signing keys
      responses:
        '200':
          description: Signing keys retrieved successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/SigningKeys'
components:
  schemas:
    SigningKeys:
      type: object
      properties:
        current:
          type: string
          description: The current signing key.
        next:
          type: string
          description: The next signing key.
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: QStash authentication token
    bearerAuthQuery:
      type: apiKey
      in: query
      name: qstash_token
      description: QStash authentication token passed as a query parameter

```

--------------------------------

### List All QStash Schedules

Source: https://upstash.com/docs/qstash/overall/apiexamples

Retrieve a list of all schedules configured within QStash. This allows for management and overview of scheduled message tasks.

```shell
curl https://qstash.upstash.io/v2/schedules \
    -H "Authorization: Bearer XXX"
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const scheds = await client.schedules.list();
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.list()
# Async version is also available
```

--------------------------------

### GET /v2/logs - Get Message Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve logs for all published messages. Filtering options may be available. Requires authentication.

```APIDOC
## GET /v2/logs

### Description
Retrieve logs for all published messages. Filtering options may be available.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/logs`

### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript SDK)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

### Response
#### Success Response (200)
- **logs** (array) - An array of log objects, each containing message details and status.

#### Response Example
```json
{
  "logs": [
    {
      "messageId": "msg_abc123",
      "url": "https://example.com",
      "status": "delivered",
      "timestamp": 1678886400
    }
  ]
}
```
```

--------------------------------

### Create Schedule with QStash Python SDK

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

This snippet shows how to use the QStash Python SDK to create a new scheduled job. You need to provide your QStash token, the destination URL for the job, and a cron expression to define the schedule. Ensure you have the 'qstash' library installed.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="https://YOUR_URL.vercel.app/api",
    cron="0 12 * * *",
)
```

--------------------------------

### QStash Retry Delay Examples (API Reference)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Illustrates various methods for customizing retry delay in QStash using mathematical expressions. The 'retried' variable signifies the number of previous retry attempts. These examples are useful for API-level configuration.

```text
- 1000: Fixed 1 second delay
- 1000 * (1 + retried): Linear backoff
- pow(2, retried) * 1000: Exponential backoff
- max(1000, pow(2, retried) * 100): Exponential with minimum 1s delay
```

--------------------------------

### Run QStash CLI Dev Server

Source: https://upstash.com/docs/qstash/overall/llms-txt

Instructions for running the QStash CLI development server locally using NPX or a downloaded binary.

```APIDOC
## Run QStash CLI Dev Server

### Description
Use NPX to run the QStash CLI development server. This command starts the server locally, allowing you to test QStash features. You can specify a different port using the -port flag. This method is convenient for quick local testing.

### Command
```bash
npx @upstash/qstash-cli dev

# Start on a different port
npx @upstash/qstash-cli dev -port=8081
```

### Description
Instructions for running the QStash CLI development server after downloading the binary directly. Extract the archive file and then execute the 'qstash dev' command from your terminal. This method bypasses package managers.

### Command
```bash
$ ./qstash dev
```
```

--------------------------------

### Handling Callbacks in Next.js

Source: https://upstash.com/docs/qstash/overall/llms-txt

This example demonstrates how to handle QStash callbacks within a Next.js API route, including the necessary steps for decoding the payload and verifying the signature.

```APIDOC
## Handling Callbacks in Next.js

### Description
Example code demonstrating how to handle QStash callbacks in a Next.js API route, including decoding the base64 body and verifying the signature.

### Method
POST

### Endpoint
`/api/callback` (Example)

### Parameters
#### Request Body
- **body** (string) - The raw request body from QStash, containing the base64 encoded callback payload.

### Request Example
```javascript
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // responses from qstash are base64-encoded
  const decoded = atob(req.body.body);
  console.log(decoded);

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false,
  },
};
```

### Note
Remember to verify the signature of incoming callback requests to ensure their authenticity. See [Request Signing](/qstash/features/security/#request-signing-optional) for more details.
```

--------------------------------

### QStash Retry Delay Examples

Source: https://upstash.com/docs/qstash/overall/llms-txt

Examples demonstrating how to customize retry delay using mathematical expressions. The 'retried' variable represents the number of previous retry attempts (0 for the first retry).

```APIDOC
## QStash Retry Delay Examples

### Description
Examples demonstrating how to customize retry delay using mathematical expressions. The 'retried' variable represents the number of previous retry attempts (0 for the first retry).

### Method
Configuration

### Endpoint
N/A

### Parameters
None

### Request Example
```text
- 1000: Fixed 1 second delay
- 1000 * (1 + retried): Linear backoff
- pow(2, retried) * 1000: Exponential backoff
- max(1000, pow(2, retried) * 100): Exponential with minimum 1s delay
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### Local Tunneling with ngrok and Publishing Message

Source: https://upstash.com/docs/qstash/overall/llms-txt

Guides on setting up ngrok for local development and publishing messages to a tunneled endpoint.

```APIDOC
## Local Tunneling with ngrok and Publishing Message

### Description
This section explains how to set up an ngrok tunnel to your local server and then publish a message to that tunneled endpoint using QStash.

### Setup ngrok
1. **Add ngrok authentication token:**
   ```bash
   ngrok config add-authtoken XXX
   ```
2. **Start an ngrok tunnel:**
   ```bash
   $ ngrok http 3000
   ```

### Publish Message via Tunnel
Use the ngrok-provided URL to publish a message.

### Method
POST

### Endpoint
`https://<your-ngrok-subdomain>.ngrok.io/api/webhooks` (Replace with your actual ngrok URL)

### Headers
- **Authorization**: `Bearer <QSTASH_TOKEN>`
- **Content-type**: `application/json`

### Request Body
- **body** (object) - Required - The message body to send
  - **hello** (string) - Example field

### Request Example (cURL)
```bash
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://e02f-2a02-810d-af40-5284-b139-58cc-89df-b740.eu.ngrok.io/api/webhooks'
```
```

--------------------------------

### QStash API Authentication using Query Parameter (Messages Get)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Explains how to use the `qstash_token` query parameter for authentication when header authentication is not feasible, specifically for the messages get endpoint. This method applies generally to other API endpoints as well.

```shell
curl https://qstash.upstash.io/v2/messages/...?qstash_token=<QSTASH_TOKEN>
```

--------------------------------

### Create Python Project Directory

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes a new directory for the Python application and navigates into it. This is the first step in setting up the project structure.

```APIDOC
## Create Python Project Directory

### Description
Initializes a new directory for the Python application and navigates into it. This is the first step in setting up the project structure.

### Commands
```bash
mkdir clean-db-cron
cd clean-db-cron
```
```

--------------------------------

### GET /v2/logs - Get Message Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve logs for all published messages. Filtering options may be available. This endpoint requires authentication.

```APIDOC
## GET /v2/logs

### Description
Retrieve logs for all published messages. Filtering options may be available. This endpoint requires authentication.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/logs`

### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript SDK)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

### Response
#### Success Response (200)
- **logs** (array) - An array of log objects, each containing message details and status.

#### Response Example
```json
{
  "logs": [
    {
      "messageId": "msg_abc123",
      "status": "delivered",
      "ts": 1678886400
    }
  ]
}
```
```

--------------------------------

### QStash JWT Payload Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides an example of the JWT payload used for signature verification within the 'Upstash-Signature' header in QStash requests. It includes details like issuer, subject, and expiration.

```apidoc
## JWT Payload Example

### Description
An example of the JWT payload used for signature verification in QStash requests.
```

--------------------------------

### POST /v2/enqueue/<queue_name>

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish messages to a FIFO queue. This ensures messages are processed in the order they are enqueued.

```APIDOC
## POST /v2/enqueue/<queue_name>

### Description
Enqueue a message to a specific queue for FIFO processing. This is useful when message order is critical.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/enqueue/<queue_name>/<destination_url>`

### Parameters
#### Path Parameters
- **queue_name** (string) - Required - The name of the queue.
- **destination_url** (string) - Required - The URL to send the message to.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Content-type** (string) - Required - Must be `application/json`.

#### Request Body
- **(object)** - Required - The JSON payload of the message.

### Request Example
```json
{
  "message": "Hello, World!"
}
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the enqueued message.

#### Response Example
```json
{
  "messageId": "<message_id>"
}
```
```

--------------------------------

### Run QStash CLI Dev Server from Binary

Source: https://upstash.com/docs/qstash/howto/local-development

Execute the QStash CLI development server by downloading and running the binary directly. After extracting the downloaded archive, navigate to the directory and run the executable with the 'dev' command.

```bash
$ ./qstash dev
```

--------------------------------

### Get Flow Control Key Details (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details of a specific Flow Control key, including its current waitlist size. This is a GET request with no request body.

```json
{
  "example": "No request body needed for this GET request."
}
```

--------------------------------

### Start QStash Background Job with Upstash Client (Next.js)

Source: https://upstash.com/docs/qstash/features/background-jobs

This server-side Next.js route handler (`/api/start-email-job`) receives a request from the client and uses the Upstash QStash client to publish a message. It constructs the URL for the actual job execution endpoint and sends the necessary data to QStash for asynchronous processing. Requires an Upstash token.

```typescript
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

--------------------------------

### Initialize QStash Client (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes the QStash client using the Python SDK. Both synchronous and asynchronous client versions are available.

```APIDOC
## QStash Client Initialization (Python)

### Description
Initializes the QStash client using the Python SDK. The SDK handles retries internally. Both synchronous and asynchronous client versions are available.

### Method
N/A (Initialization)

### Endpoint
N/A

### Parameters
#### Initialization Parameters
- **token** (string) - Required - Your QStash API token.

### Request Example
```python
from qstash import QStash

# Python SDK handles retries internally
client = QStash("<QSTASH-TOKEN>")

# Both sync and async versions available
from qstash import AsyncQStash

async_client = AsyncQStash("<QSTASH-TOKEN>")
```

### Response
N/A (Initialization)

### Error Handling
- **AuthenticationError**: If the provided token is invalid.
- **NetworkError**: If there are issues connecting to the QStash service.
```

--------------------------------

### Set Up ngrok Tunnel and Publish Message

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates setting up an ngrok tunnel to a local server and publishing a message to it via QStash.

```APIDOC
## Set Up ngrok Tunnel and Publish Message

### Description
ngrok is a powerful tool for creating secure tunnels to your local server. This snippet shows how to set up ngrok with your authentication token, start a tunnel to your application's port, and then use curl to publish a message to your tunneled endpoint via QStash.

### Setup ngrok

```bash
ngrok config add-authtoken XXX
```

### Start ngrok Tunnel

```bash
$ ngrok http 3000
```
```

--------------------------------

### Install Upstash QStash Library

Source: https://upstash.com/docs/qstash/quickstarts/cloudflare-workers

Installs the official Upstash QStash library for Node.js using npm. This library provides tools for interacting with QStash services, including webhook signature verification.

```bash
npm install @upstash/qstash
```

--------------------------------

### Deploy AWS CDK Stack

Source: https://upstash.com/docs/qstash/overall/llms-txt

Deploys your AWS CDK stack to the cloud. Requires the AWS CDK CLI to be installed and configured.

```APIDOC
## Deploy AWS CDK Stack

### Description
This command deploys your AWS CDK stack to the cloud. It requires the AWS CDK CLI to be installed and configured. Running this command will provision or update AWS resources defined in your CDK stack. You may be prompted to confirm necessary permissions.

### Method
N/A (CLI Command)

### Endpoint
N/A (CLI Command)

### Command
```bash
cdk deploy
```

### Usage
Run this command in the root directory of your AWS CDK project.
```

--------------------------------

### Verify JWT Signature (Golang)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example using the QStash SDK for Golang to verify the JWT signature of an incoming request. It demonstrates initializing the receiver and the verification process.

```go
import "github.com/qstash/qstash-go"

// Initialize receiver with signing keys
receiver := qstash.NewReceiver("<CURRENT_SIGNING_KEY>", "<NEXT_SIGNING_KEY>")

// Inside your request handler:
// Assuming 'req' is your http.Request object
signature := req.Header.Get("Upstash-Signature")
bodyBytes, err := io.ReadAll(req.Body)
// Handle err
bodyString := string(bodyBytes)

// Verify the signature
err := receiver.Verify(qstash.VerifyOptions{
    Signature: signature,
    Body:      bodyString,
    Url:       "YOUR-SITE-URL", // Optional: specify your site URL
})
// Handle err: If err is not nil, the signature is invalid.

```

--------------------------------

### Initialize Upstash QStash Client (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes the Upstash QStash client with your QStash token. This is the basic setup required to interact with the QStash API.

```APIDOC
## Initialize Upstash QStash Client (TypeScript)

### Description
Initializes the Upstash QStash client with your QStash token. This is the basic setup required to interact with the QStash API.

### Method
Initialization

### Endpoint
N/A

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({
  token: "<QSTASH_TOKEN>",
});
```

### Response
None

#### Success Response (200)
None

#### Response Example
None
```

--------------------------------

### QStash Signature Verification via SDK (TypeScript, Python, Go)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Details how to use QStash SDKs to verify incoming request signatures. Provides code examples for TypeScript, Python, and Go, utilizing the Receiver type for simplified verification.

```typescript
import { Receiver } from "@upstash/qstash";

const receiver = new Receiver({
  currentSigningKey: "YOUR_CURRENT_SIGNING_KEY",
  nextSigningKey: "YOUR_NEXT_SIGNING_KEY",
});

// ... in your request handler

const signature = req.headers["Upstash-Signature"];
const body = req.body;

const isValid = await receiver.verify({
  body,
  signature,
  url: "YOUR-SITE-URL",
});
```

```python
from qstash import Receiver

receiver = Receiver(
    current_signing_key="YOUR_CURRENT_SIGNING_KEY",
    next_signing_key="YOUR_NEXT_SIGNING_KEY",
)

# ... in your request handler

signature, body = req.headers["Upstash-Signature"], req.body

receiver.verify(
    body=body,
    signature=signature,
    url="YOUR-SITE-URL",
)
```

```go
import "github.com/qstash/qstash-go"

receiver := qstash.NewReceiver("<CURRENT_SIGNING_KEY>", "NEXT_SIGNING_KEY")

// ... in your request handler

signature := req.Header.Get("Upstash-Signature")
body, err := io.ReadAll(req.Body)
// handle err

err := receiver.Verify(qstash.VerifyOptions{
    Signature: signature,
    Body:      string(body),
    Url:       "YOUR-SITE-URL", // optional
})
// handle err
```

--------------------------------

### Handling Callbacks in Next.js

Source: https://upstash.com/docs/qstash/features/callbacks

Example code for handling incoming callback requests in a Next.js API route, including signature verification.

```APIDOC
## Handling Callbacks in Next.js

### Description
This example shows how to set up an API route in Next.js to receive and process callback notifications from QStash, including verifying the request's authenticity.

### Method
POST

### Endpoint
`/pages/api/callback.js` (or your chosen API route path)

### Parameters
#### Request Body
- **body** (string) - Required - The base64 encoded payload of the callback notification.

### Request Example (Next.js API Route)
```javascript
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // QStash callback bodies are base64-encoded
  const decodedBody = atob(req.body.body);
  console.log("Decoded callback body:", decodedBody);

  // Process the decodedBody here...

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false, // Disable default body parsing to handle raw body for signature verification
  },
};
```

### Notes
- Ensure your Next.js application is configured to allow raw body parsing for the API route handling the callback, as shown in `export const config`.
- The `verifySignature` middleware automatically verifies the `Upstash-Signature` header.
```

--------------------------------

### QStash API Authentication with Query Parameter

Source: https://upstash.com/docs/qstash/api/messages

This section explains how to authenticate API requests using the `qstash_token` query parameter when setting headers is not possible.

```APIDOC
## QStash API Authentication with Query Parameter

### Description
If you cannot set the `Authorization` header, you can authenticate your requests by appending the `qstash_token` query parameter to your request URL with your `QSTASH_TOKEN`.

### Method
All HTTP methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*?qstash_token=<QSTASH_TOKEN>`

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash authentication token.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the operation.

#### Response Example
```json
{
  "message": "Request processed successfully"
}
```
```

--------------------------------

### Publish HTML Content to URL

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes raw HTML content to a specified URL. The 'Content-Type' header is set to 'text/html'. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publish({
  url: "https://my-api...",
  body: "<html><body><h1>Hello World</h1></body></html>",
  headers: {
    "Content-Type": "text/html",
  },
});
```

--------------------------------

### QStash Signature Verification via SDK

Source: https://upstash.com/docs/qstash/overall/llms-txt

This section details how to use the QStash SDKs to verify incoming request signatures. It provides code examples for TypeScript, Python, and Go.

```APIDOC
## QStash Signature Verification via SDK

QStash SDKs provide a `Receiver` type that simplifies signature verification.

### Request Example (TypeScript)
```typescript
import { Receiver } from "@upstash/qstash";

const receiver = new Receiver({
  currentSigningKey: "YOUR_CURRENT_SIGNING_KEY",
  nextSigningKey: "YOUR_NEXT_SIGNING_KEY",
});

// ... in your request handler

const signature = req.headers["Upstash-Signature"];
const body = req.body;

const isValid = await receiver.verify({
  body,
  signature,
  url: "YOUR-SITE-URL",
});
```

### Request Example (Python)
```python
from qstash import Receiver

receiver = Receiver(
    current_signing_key="YOUR_CURRENT_SIGNING_KEY",
    next_signing_key="YOUR_NEXT_SIGNING_KEY",
)

# ... in your request handler

signature, body = req.headers["Upstash-Signature"], req.body

receiver.verify(
    body=body,
    signature=signature,
    url="YOUR-SITE-URL",
)
```

### Request Example (Golang)
```go
import "github.com/qstash/qstash-go"

receiver := qstash.NewReceiver("<CURRENT_SIGNING_KEY>", "NEXT_SIGNING_KEY")

// ... in your request handler

signature := req.Header.Get("Upstash-Signature")
body, err := io.ReadAll(req.Body)
// handle err

err := receiver.Verify(qstash.VerifyOptions{
    Signature: signature,
    Body:      string(body),
    Url:       "YOUR-SITE-URL", // optional
})
// handle err
```

<Warning>Depending on the environment, the body might be parsed into an object by the HTTP handler if it is JSON. Ensure you use the raw body string as is. For example, converting the parsed object back to a string (e.g., JSON.stringify(object)) may cause inconsistencies and result in verification failure.</Warning>
```

--------------------------------

### Create or Update Queue API Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

Defines the API endpoint for creating or updating a QStash queue with specified configurations, including parallelism. It outlines the request body parameters and expected success response.

```APIDOC
## POST /v2/queues/

### Description
Creates or updates a queue with specified configuration, including parallelism.

### Method
POST

### Endpoint
`/v2/queues/`

### Parameters
#### Request Body
- **queueName** (string) - Required - The name of the queue to create or update.
- **parallelism** (integer) - Optional - The number of concurrent messages to process. Defaults to 1.

### Request Example
```json
{
  "queueName": "my-queue",
  "parallelism": 5
}
```

### Response
#### Success Response (200)
- **message** (string) - Confirmation message indicating the queue was updated.

#### Response Example
```json
{
  "message": "Queue updated successfully"
}
```
```

--------------------------------

### QStash Success Response Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

A JSON object representing a successful response from a QStash batch operation.

```APIDOC
## QStash Batch Operation Success Response

### Description
A JSON object representing a successful response from a QStash batch operation.

### Method
(N/A - Response format)

### Endpoint
(N/A - Response format)

### Parameters
None

### Request Example
None

### Response
#### Success Response (200)
- **batchId** (string) - A string identifier for the completed batch operation.

### Response Example
```json
{
  "batchId": "batch_ghi789"
}
```
```

--------------------------------

### QStash Development Server Environment Variables (JavaScript)

Source: https://upstash.com/docs/qstash/howto/local-development

Provides example environment variables for connecting to the QStash development server using JavaScript. These variables include the server URL, authentication token, and signing keys necessary for making requests.

```javascript
QSTASH_URL="http://localhost:8080"
QSTASH_TOKEN="eyJVc2VySUQiOiJkZWZhdWx0VXNlciIsIlBhc3N3b3JkIjoiZGVmYXVsdFBhc3N3b3JkIn0="
QSTASH_CURRENT_SIGNING_KEY="sig_7kYjw48mhY7kAjqNGcy6cr29RJ6r"
QSTASH_NEXT_SIGNING_KEY="sig_5ZB6DVzB1wjE8S6rZ7eenA8Pdnhs"
```

```javascript
QSTASH_URL="http://localhost:8080"
QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjEiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
QSTASH_CURRENT_SIGNING_KEY="sig_7GVPjvuwsfqF65iC8fSrs1dfYruM"
QSTASH_NEXT_SIGNING_KEY="sig_5NoELc3EFnZn4DVS5bDs2Nk4b7Ua"
```

```javascript
QSTASH_URL="http://localhost:8080"
QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjIiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
QSTASH_CURRENT_SIGNING_KEY="sig_6jWGaWRxHsw4vMSPJprXadyvrybF"
QSTASH_NEXT_SIGNING_KEY="sig_7qHbvhmahe5GwfePDiS5Lg3pi6Qx"
```

```javascript
QSTASH_URL="http://localhost:8080"
QSTASH_TOKEN="eyJVc2VySUQiOiJ0ZXN0VXNlcjMiLCJQYXNzd29yZCI6InRlc3RQYXNzd29yZCJ9"
QSTASH_CURRENT_SIGNING_KEY="sig_5T8FcSsynBjn9mMLBsXhpacRovJf"
QSTASH_NEXT_SIGNING_KEY="sig_7GFR4YaDshFcqsxWRZpRB161jguD"
```

--------------------------------

### Start Background Job with QStash API in TypeScript

Source: https://upstash.com/docs/qstash/overall/llms-txt

This Next.js API route handler in TypeScript publishes a JSON message to Upstash QStash to start a background job. It dynamically constructs the background job endpoint URL and requires a QStash token for authentication. The job logic resides in a separate API endpoint.

```typescript
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

--------------------------------

### Publish JSON to URL with Delay, Headers, and Body

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a specified URL with a 3-second delay, custom headers, and a JSON body. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  headers: { "test-header": "test-value" },
  delay: "3s",
});
```

--------------------------------

### Publish JSON to URL with Delay, Headers, and Body (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message to a specified URL with a 3-second delay. It also demonstrates how to include custom headers and a request body. This function requires the `qstash` library and a QStash client initialized with an API token.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
res = client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    headers={
        "test-header": "test-value",
    },
    delay="3s",
)

print(res.message_id)
```

--------------------------------

### POST /v2/publish

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a message with a configurable retry count. This allows control over how many times QStash attempts to deliver a message.

```APIDOC
## POST /v2/publish

### Description
Publish a single message to a specified endpoint with a configurable number of retries. This helps ensure message delivery even if the endpoint is temporarily unavailable.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/publish/<destination_url>`

### Parameters
#### Path Parameters
- **destination_url** (string) - Required - The URL to send the message to.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Upstash-Retries** (string) - Optional - The maximum number of retries (e.g., "3"). Defaults to a system-defined value if not provided.
- **Content-type** (string) - Required - Must be `application/json`.

#### Request Body
- **(object)** - Required - The JSON payload of the message.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.

#### Response Example
```json
{
  "messageId": "<message_id>"
}
```
```

--------------------------------

### Retrieve QStash Message Logs

Source: https://upstash.com/docs/qstash/overall/apiexamples

Fetch logs for all published messages, with support for filtering. This is useful for monitoring message delivery and debugging.

```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.event.list()
# Async version is also available
```

--------------------------------

### Get a Schedule

Source: https://upstash.com/docs/qstash/api-refence/schedules/get-a-schedule

Retrieves details of a specific schedule within Upstash QStash.

```APIDOC
## GET /v2/schedules/{scheduleId}

### Description
Retrieves details of a specific schedule.

### Method
GET

### Endpoint
/v2/schedules/{scheduleId}

### Parameters
#### Path Parameters
- **scheduleId** (string) - Required - The unique identifier of the schedule to retrieve.

### Request Example
(No request body for GET requests)

### Response
#### Success Response (200)
- **scheduleId** (string) - The unique identifier of the schedule.
- **cronExpression** (string) - The cron expression defining the schedule.
- **createdAt** (string) - The timestamp when the schedule was created.
- **nextRunAt** (string) - The timestamp of the next scheduled run.
- **messagesPerSecond** (integer) - The maximum number of messages to send per second.
- **totalMessages** (integer) - The total number of messages scheduled.
- **tags** (array) - An array of tags associated with the schedule.

#### Response Example
```json
{
  "scheduleId": "sch_abcdef123456",
  "cronExpression": "* * * * *",
  "createdAt": "2023-10-27T10:00:00Z",
  "nextRunAt": "2023-10-27T10:01:00Z",
  "messagesPerSecond": 100,
  "totalMessages": 1000,
  "tags": ["important", "daily"]
}
```
```

--------------------------------

### Run QStash CLI Dev Server

Source: https://upstash.com/docs/qstash/overall/llms-txt

Instructions for running the QStash CLI development server directly after downloading the binary. This bypasses package managers and involves executing the 'qstash dev' command from the terminal.

```APIDOC
## Run QStash CLI Dev Server

### Description
Instructions for running the QStash CLI development server directly after downloading the binary. This bypasses package managers and involves executing the 'qstash dev' command from the terminal.

### Method
CLI Command

### Endpoint
Not applicable

### Parameters
None

### Request Example
```bash
$ ./qstash dev
```

### Response
(This is a command-line instruction, not an API response.)
```

--------------------------------

### Bundle and Zip Lambda Function (Makefile)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Automates the installation of Python dependencies, copying Lambda function code, and creating a zip archive for AWS deployment using a Makefile. It ensures all necessary components are bundled correctly.

```yaml
zip:
    rm -rf dist
	pip3 install --target ./dist pyjwt
	cp lambda_function.py ./dist/lambda_function.py
	cd dist && zip -r lambda.zip .
	mv ./dist/lambda.zip ./

```

--------------------------------

### Handling Callbacks in Next.js

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of a Next.js API route for handling incoming callbacks from Upstash QStash, including signature verification to ensure authenticity.

```APIDOC
## Handling Callbacks in Next.js

### Description
This example demonstrates how to set up a Next.js API route to handle incoming callbacks from Upstash QStash. It includes decoding the base64-encoded message body and verifying the request's authenticity using `verifySignature`.

### Method
POST (typically for callbacks)

### Endpoint
`/pages/api/callback.js` (within your Next.js project)

### Parameters
(No explicit parameters; handles incoming request body)

### Request Example (Conceptual)
(Incoming request body from Qstash)

### Response
#### Success Response (200)
- **Status** (integer) - 200 - Indicates successful handling of the callback.

### Code Example
```javascript
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // responses from qstash are base64-encoded
  const decoded = atob(req.body.body);
  console.log(decoded);

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false,
  },
};
```
```

--------------------------------

### Receive and Verify QStash Webhooks in Deno Deploy

Source: https://upstash.com/docs/qstash/quickstarts/deno-deploy

This TypeScript code snippet demonstrates how to set up a Deno deploy server to receive webhook requests from QStash. It utilizes the Upstash QStash SDK to verify the request signature using provided signing keys stored as environment variables. The handler logs whether the signature is valid and returns an appropriate HTTP response.

```typescript
import { serve } from "https://deno.land/std@0.142.0/http/server.ts";
import { Receiver } from "https://deno.land/x/upstash_qstash@v0.1.4/mod.ts";

serve(async (req: Request) => {
  const r = new Receiver({
    currentSigningKey: Deno.env.get("QSTASH_CURRENT_SIGNING_KEY")!,
    nextSigningKey: Deno.env.get("QSTASH_NEXT_SIGNING_KEY")!,
  });

  const isValid = await r
    .verify({
      signature: req.headers.get("Upstash-Signature")!,
      body: await req.text(),
    })
    .catch((err: Error) => {
      console.error(err);
      return false;
    });

  if (!isValid) {
    return new Response("Invalid signature", { status: 401 });
  }

  console.log("The signature was valid");

  // do work

  return new Response("OK", { status: 200 });
});
```

--------------------------------

### Handle Callback Request in Next.js

Source: https://upstash.com/docs/qstash/features/callbacks

Provides a Next.js API route example for handling incoming callback requests from Upstash QStash. It includes decoding the base64-encoded body and verifying the request signature using `@upstash/qstash/nextjs`. Ensure `bodyParser` is disabled for the API route.

```javascript
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // responses from qstash are base64-encoded
  const decoded = atob(req.body.body);
  console.log(decoded);

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false,
  },
};

```

--------------------------------

### Create Python Project Directory

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes a new directory for a Python application and navigates into it. This is a fundamental step for organizing project files and setting up the development environment.

```bash
mkdir my-python-app
cd my-python-app
```

--------------------------------

### POST /v2/schedules

Source: https://upstash.com/docs/qstash/overall/apiexamples

Schedule a message to be run once a day. This endpoint allows you to set a cron schedule for a specific destination URL.

```APIDOC
## POST /v2/schedules

### Description
Schedule a message to run at a specific time interval, defined by a cron expression. This is useful for daily or recurring tasks.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/schedules/<destination_url>`

### Parameters
#### Path Parameters
- **destination_url** (string) - Required - The URL to send the scheduled message to.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Upstash-Cron** (string) - Required - Cron expression defining the schedule (e.g., "0 0 * * *").
- **Content-type** (string) - Required - Must be `application/json`.

#### Request Body
- **(object)** - Optional - The JSON payload to send with the message.

### Request Example
```json
{
  "hello": "world"
}
```

### Response
#### Success Response (200)
- **(object)** - Details about the created schedule.

#### Response Example
```json
{
  "messageId": "<message_id>",
  "scheduleId": "<schedule_id>"
}
```
```

--------------------------------

### GET /v2/schedules

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve a list of all schedules that have been created within the QStash service.

```APIDOC
## List QStash Schedules

### Description
Retrieve a list of all schedules that have been created within the QStash service. This is useful for managing scheduled messages.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/schedules`

### Parameters
#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/schedules \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const scheds = await client.schedules.list();
```

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.list()
# Async version is also available
```

### Response
#### Success Response (200)
(Response details depend on the specific endpoint being called, typically a list of schedule objects)

#### Response Example
(Response example depends on the specific endpoint being called)
```

--------------------------------

### Get Message Details (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details for a specific message using its ID with the Upstash QStash SDK for Python. The client is initialized with a QStash token, and the get method fetches message information. Includes error handling for unavailable messages.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")

try:
    message = client.message.get("msg_123")
    print(f"Message {message['messageId']} to {message['url']}")
    print(f"Body: {message['body']}")
except Exception as e:
    print("Message already delivered or not found")
```

--------------------------------

### Run QStash CLI Dev Server with NPX

Source: https://upstash.com/docs/qstash/howto/local-development

Execute the QStash CLI development server using NPX. This command starts a local server for testing QStash features. You can specify a different port using the -port flag.

```bash
npx @upstash/qstash-cli dev

# Start on a different port
npx @upstash/qstash-cli dev -port=8081
```

--------------------------------

### Golang HTTP Server for QStash Webhook Reception

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Sets up an HTTP server to listen for incoming requests on a specified port (defaulting to 8080). It reads the request body and Upstash-Signature header, then calls the `verify` function to validate the signature using current and next signing keys from environment variables. If verification succeeds, it proceeds with business logic; otherwise, it returns an unauthorized error.

```go
func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		defer r.Body.Close()

		currentSigningKey := os.Getenv("QSTASH_CURRENT_SIGNING_KEY")
		nextSigningKey := os.Getenv("QSTASH_NEXT_SIGNING_KEY")
	
tokenString := r.Header.Get("Upstash-Signature")

	body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		err = verify(body, tokenString, currentSigningKey)
		if err != nil {
			fmt.Printf("Unable to verify signature with current signing key: %v", err)
			err = verify(body, tokenString, nextSigningKey)
		}

		if err != nil {
			http.Error(w, err.Error(), http.StatusUnauthorized)
			return
		}

		// handle your business logic here

		w.WriteHeader(http.StatusOK)

	})

	fmt.Println("listening on", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		panic(err)
	}
}
```

--------------------------------

### Get Queue Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve the current configuration details for a specific queue, including its parallelism settings.

```APIDOC
## GET /v2/queues/{queueName}

### Description
Retrieves the details of a specific queue.

### Method
GET

### Endpoint
`/v2/queues/{queueName}`

### Parameters
#### Path Parameters
- **queueName** (string) - Required - The name of the queue to retrieve details for.

### Response
#### Success Response (200)
- **queueName** (string) - The name of the queue.
- **parallelism** (integer) - The current parallelism setting for the queue.

#### Response Example
```json
{
  "queueName": "my-queue",
  "parallelism": 5
}
```
```

--------------------------------

### Create Webhook

Source: https://upstash.com/docs/qstash/api-refence/dlq/get-a-dlq-message

Create a webhook to receive messages from a QStash topic.

```APIDOC
## POST /v2/webhook

### Description
Creates a new webhook subscription to receive messages from a specified QStash topic. Incoming messages will be sent as POST requests to the provided URL.

### Method
POST

### Endpoint
/v2/webhook

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **body** (object) - Required - Configuration for the webhook.
  - **url** (string) - Required - The URL to send messages to.
  - **topic** (string) - Required - The topic to subscribe to.
  - **filter** (string) - Optional - A filter expression to only receive messages matching certain criteria.
  - **forwardHeaders** (array) - Optional - A list of headers to forward from the original message.
  - **forwardBody** (boolean) - Optional - Whether to forward the message body. Defaults to true.
  - **forwardQuery** (boolean) - Optional - Whether to forward query parameters. Defaults to true.

### Request Example
```json
{
  "url": "https://example.com/webhook-receiver",
  "topic": "notifications",
  "filter": "event = 'user_created'",
  "forwardHeaders": ["X-Request-ID"],
  "forwardBody": true
}
```

### Response
#### Success Response (200)
- **webhookId** (string) - The unique identifier for the created webhook.
- **url** (string) - The URL of the webhook.
- **topic** (string) - The topic subscribed to.

#### Response Example
```json
{
  "webhookId": "wh_abc789",
  "url": "https://example.com/webhook-receiver",
  "topic": "notifications"
}
```
```

--------------------------------

### GET /v2/schedules/{scheduleId}

Source: https://upstash.com/docs/qstash/api-refence/schedules/get-a-schedule

Retrieves the details of a specific schedule by its ID.

```APIDOC
## GET /v2/schedules/{scheduleId}

### Description
Get details of a specific schedule.

### Method
GET

### Endpoint
/v2/schedules/{scheduleId}

#### Path Parameters
- **scheduleId** (string) - Required - The ID of the schedule to retrieve.

### Request Example
(No request body for GET requests)

### Response
#### Success Response (200)
- **scheduleId** (string) - Unique identifier for the schedule
- **cron** (string) - The cron expression used to schedule the message
- **destination** (string) - The destination URL or URL Group name
- **createdAt** (integer) - The creation timestamp of the schedule in unix milliseconds
- **method** (string) - The HTTP method used for the scheduled message
- **header** (object) - Map of header names to arrays of header values
- **body** (string) - The body of the scheduled message
- **retries** (integer) - The number of retries for the scheduled message
- **delay** (integer) - The delay in seconds before the scheduled message is sent
- **callback** (string) - The callback URL for the scheduled message
- **failureCallback** (string) - The failure callback URL for the scheduled message
- **callerIp** (string) - The IP address of the client that created the schedule
- **isPaused** (boolean) - Whether the schedule is paused
- **flowControlKey** (string) - The flow control key used for rate limiting
- **parallelism** (integer) - The parallelism value used for flow control
- **rate** (integer) - The rate value used for flow control
- **period** (integer) - The period value used for flow control
- **retryDelayExpression** (string) - The retry delay expression used for calculating retry delays
- **label** (string) - The label assigned to the scheduled message
- **lastScheduleTime** (integer) - The last time the schedule was triggered in unix milliseconds
- **nextScheduleTime** (integer) - The next scheduled trigger time in unix milliseconds
- **lastScheduleStates** (object) - The states of the last scheduled messages

#### Error Response (404)
- **error** (string) - Error message

#### Response Example
```json
{
  "scheduleId": "sch_abc123",
  "cron": "* * * * *",
  "destination": "https://example.com/webhook",
  "createdAt": 1678886400000,
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"message\": \"Hello, QStash!\"}",
  "retries": 3,
  "delay": 60,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure",
  "callerIp": "192.168.1.1",
  "isPaused": false,
  "flowControlKey": "fc_key_xyz",
  "parallelism": 10,
  "rate": 100,
  "period": 60,
  "retryDelayExpression": "exponential",
  "label": "my-schedule",
  "lastScheduleTime": 1678886400000,
  "nextScheduleTime": 1678886460000,
  "lastScheduleStates": {
    "status": "success"
  }
}
```
```

--------------------------------

### Publish Messages in Batch with QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish multiple messages in a single request to optimize throughput. This feature allows sending several messages efficiently. Supports cURL, TypeScript, and Python.

```shell
curl -XPOST https://qstash.upstash.io/v2/batch \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -d '
     [
      {
        "destination": "https://example.com/destination1"
      },
      {
        "destination": "https://example.com/destination2"
      }
     ]'
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.batchJSON([
  {
    url: "https://example.com/destination1",
  },
  {
    url: "https://example.com/destination2",
  },
]);
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.batch_json(
    [
        {
            "url": "https://example.com/destination1",
        },
        {
            "url": "https://example.com/destination2",
        },
    ]
)
# Async version is also available
```

--------------------------------

### Expose Local Server with localtunnel.me

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides instructions on how to use localtunnel.me to create a public URL for a local development server, useful for testing QStash integrations.

```APIDOC
## Expose Local Server with localtunnel.me

### Description
Use localtunnel.me to create a public URL for your local development server. This tool is simple to use and requires only the port your application is running on. It's useful for quickly testing QStash integrations.

### Command Example
```bash
npx localtunnel --port 3000
```
```

--------------------------------

### Publish Message to Endpoint using QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a JSON message to a specified endpoint using QStash. Supports cURL, Typescript, and Python SDKs. Requires authentication token and endpoint URL.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
)
# Async version is also available
```

--------------------------------

### Get Queue Information

Source: https://upstash.com/docs/qstash/features/queues

Retrieves the current configuration and status of a specific queue, including its parallelism setting.

```APIDOC
## GET /v2/queues/{queueName}

### Description
Retrieves the current configuration and status of a specific queue, including its parallelism setting.

### Method
GET

### Endpoint
`/v2/queues/{queueName}`

### Parameters
#### Path Parameters
- **queueName** (string) - Required - The name of the queue to retrieve information for.

### Response
#### Success Response (200)
- **queueName** (string) - The name of the queue.
- **parallelism** (integer) - The current parallelism setting for the queue.

#### Response Example
```json
{
  "queueName": "my-queue",
  "parallelism": 5
}
```
```

--------------------------------

### Get Flow Control Key Details - OpenAPI Spec

Source: https://upstash.com/docs/qstash/overall/llms-txt

This OpenAPI specification defines the GET endpoint for retrieving details of a specific Flow Control key. It includes path parameters, response schemas for success (200 OK) and errors (404 Not Found), and authentication methods.

```yaml
openapi: 3.1.0
info:
  title: QStash REST API
  description: |
    QStash is a message queue and scheduler built on top of Upstash Redis.
  version: 2.0.0
  contact:
    name: Upstash
    url: https://upstash.com
servers:
  - url: https://qstash.upstash.io
security:
  - bearerAuth: []
  - bearerAuthQuery: []
tags:
  - name: Messages
    description: Publish and manage messages
  - name: Queues
    description: Manage message queues
  - name: Schedules
    description: Create and manage scheduled messages
  - name: URL Groups
    description: Manage URL groups and endpoints
  - name: DLQ
    description: Dead Letter Queue operations
  - name: Logs
    description: Log operations
  - name: Signing Keys
    description: Manage signing keys
  - name: Flow Control
    description: Monitor flow control keys
paths:
  /v2/flowControl/{flowControlKey}:
    get:
      tags:
        - Flow Control
      summary: Get Flow Control Key
      description: Get details of a specific Flow Control key
      parameters:
        - name: flowControlKey
          in: path
          required: true
          schema:
            type: string
          description: The Flow Control key to retrieve
      responses:
        '200':
          description: Flow control key details
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FlowControlKey'
        '404':
          description: Flow Control key not found
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Error'
components:
  schemas:
    FlowControlKey:
      type: object
      properties:
        flowControlKey:
          type: string
          description: The flow control key name
        waitlistSize:
          type: integer
          description: The number of messages waiting due to flow control configuration.
    Error:
      type: object
      required:
        - error
      properties:
        error:
          type: string
          description: Error message
  securitySchemes:
    bearerAuth:
      type: http
      scheme: bearer
      bearerFormat: JWT
      description: QStash authentication token
    bearerAuthQuery:
      type: apiKey
      in: query
      name: qstash_token
      description: QStash authentication token passed as a query parameter

```

--------------------------------

### Publish Messages to FIFO Queue with QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish messages to a FIFO queue for ordered processing. This ensures messages are processed in the order they are enqueued. Supports cURL, TypeScript, and Python.

```shell
curl -XPOST -H 'Authorization: Bearer XXX' \
                -H "Content-type: application/json" \
                'https://qstash.upstash.io/v2/enqueue/my-queue/https://example.com' 
                -d '{"message":"Hello, World!"}'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });

const queue = client.queue({
  queueName: "my-queue"
})

await queue.enqueueJSON({
  url: "https://example.com",
  body: {
    "Hello": "World"
  }
})
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.enqueue_json(
    queue="my-queue",
    url="https://example.com",
    body={
        "Hello": "World",
    },
)
# Async version is also available
```

--------------------------------

### Publish JSON Message using Upstash QStash SDK (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides a TypeScript example using the Upstash QStash client to publish a JSON message. It shows how to initialize the client with a token, specify the destination URL, the message body as a JavaScript object, and custom headers.

```APIDOC
## Publish JSON Message using Upstash QStash SDK (TypeScript)

### Description
Provides a TypeScript example using the Upstash QStash client to publish a JSON message. It shows how to initialize the client with a token, specify the destination URL, the message body as a JavaScript object, and custom headers. The SDK abstracts the HTTP request details.

### Method
POST

### Endpoint
(Client-side abstraction, maps to `/publish`)

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **url** (string) - Required - The URL of the destination.
- **body** (object) - Required - The JSON payload of the message.
- **headers** (object) - Optional - Key-value pairs for custom headers to be forwarded.

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
    url: "https://example.com",
    body: { "hello": "world" },
    headers: { "my-header": "my-value" },
});
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Initialize QStash Client (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes the QStash client using the Python SDK, which includes internal retry mechanisms. Both synchronous and asynchronous client versions are available.

```python
from qstash import QStash

# Python SDK handles retries internally
client = QStash("<QSTASH_TOKEN>")

# Both sync and async versions available
from qstash import AsyncQStash

async_client = AsyncQStash("<QSTASH_TOKEN>")
```

--------------------------------

### Get Signing Keys

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves your current and next signing keys for QStash. This is useful for verifying message signatures.

```APIDOC
## GET /v2/keys

### Description
Retrieve your current and next signing keys.

### Method
GET

### Endpoint
/v2/keys

### Parameters

#### Query Parameters
- **qstash_token** (string) - Required - QStash authentication token passed as a query parameter.

### Request Example
```http
GET /v2/keys?qstash_token=YOUR_QSTASH_TOKEN
```

### Response
#### Success Response (200)
- **current** (string) - The current signing key.
- **next** (string) - The next signing key.

#### Response Example
```json
{
  "current": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJjdXJyZW50Ijp0cnVlfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c",
  "next": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyLCJuZXh0Ijp0cnVlfQ.g6z_W7tNlQyUf7Y9r2wV0mQ6dJ8sX3zP5w7uY9v1Z0k"
}
```
```

--------------------------------

### QStash API Authentication - Query Parameter

Source: https://upstash.com/docs/qstash/api/queues/upsert

This section explains how to authenticate QStash API requests using the `qstash_token` query parameter when header authentication is not possible.

```APIDOC
## QStash API Authentication - Query Parameter

### Description
When setting the `Authorization` header is not feasible, authenticate QStash API requests by appending the `qstash_token` query parameter to your request URL.

### Method
N/A (Applies to all methods)

### Endpoint
N/A (Applies to all endpoints)

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash authentication token.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
No specific response for authentication, but subsequent requests will be authorized.
```

--------------------------------

### Get Message Details

Source: https://upstash.com/docs/qstash/api-refence/dlq/get-a-dlq-message

Retrieve details about a specific message, including its status and content.

```APIDOC
## GET /v2/messages/{messageId}

### Description
Retrieves the details of a specific message using its unique message ID. This allows you to inspect message content, status, and delivery information.

### Method
GET

### Endpoint
/v2/messages/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The unique identifier of the message to retrieve.

#### Query Parameters
None

#### Request Body
None

### Request Example
(No request body for GET requests)

### Response
#### Success Response (200)
- **messageId** (string) - The unique identifier of the message.
- **topic** (string) - The topic the message belongs to.
- **status** (string) - The current status of the message (e.g., `sent`, `delivered`, `failed`).
- **createdAt** (integer) - Unix timestamp indicating when the message was created.
- **sentAt** (integer) - Unix timestamp indicating when the message was sent.
- **deliveredAt** (integer) - Unix timestamp indicating when the message was delivered.
- **body** (object) - The content of the message.
- **headers** (object) - The headers associated with the message.

#### Response Example
```json
{
  "messageId": "msg_abc123",
  "topic": "my-topic",
  "status": "delivered",
  "createdAt": 1678886400,
  "sentAt": 1678886405,
  "deliveredAt": 1678886410,
  "body": {
    "content": "Hello, QStash!",
    "contentType": "text/plain"
  },
  "headers": {
    "X-Custom-Header": "value"
  }
}
```
```

--------------------------------

### Schedule Daily Task with QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Schedule a task to run once a day using QStash. This involves setting a cron expression for daily execution. Supports cURL, TypeScript, and Python.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Upstash-Cron: 0 0 * * *" \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  cron: "0 0 * * *",
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="https://example.com",
    cron="0 0 * * *",
)
# Async version is also available
```

--------------------------------

### GET /v2/dlq/{dlqId} API Reference

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves a specific message from the Dead Letter Queue (DLQ) using its unique DLQ ID. This is useful for inspecting messages that failed delivery and may require manual intervention or re-processing. The API endpoint is GET /v2/dlq/{dlqId}.

```APIDOC
## GET /v2/dlq/{dlqId}

### Description
Get a specific message from the DLQ.

### Method
GET

### Endpoint
/v2/dlq/{dlqId}

### Parameters
#### Path Parameters
- **dlqId** (string) - Required - The DLQ ID of the message you want to retrieve.

### Response
#### Success Response (200)
- **messageId** (string) - Unique identifier for the message
- **url** (string) - The URL to which the message should be delivered.
- **topicName** (string) - The URL Group (a.k.a. topic) name if this message was sent to a URL Group.
- **endpointName** (string) - The endpoint name of the message if the endpoint is given a name within the URL group.
- **method** (string) - The HTTP method to use for the message.
- **header** (object) - The HTTP headers sent to your API.
- **body** (string) - The body of the message if it is composed of utf8 chars only, empty otherwise.
- **bodyBase64** (string) - The base64 encoded body if the body contains a non-utf8 char only, empty otherwise.
- **maxRetries** (integer) - The number of retries that should be attempted in case of delivery failure.
- **notBefore** (integer) - The unix timestamp in milliseconds before which the message should not be delivered.
- **createdAt** (integer) - The unix timestamp in milliseconds when the message was created.
- **callback** (string) - The url where we send a callback each time the message is attempted to be delivered.
- **failureCallback** (string) - The url where we send a callback to after the message is failed
- **queueName** (string) - The name of the queue if the message is enqueued to a queue.
- **scheduleId** (string) - The scheduleId of the message if the message is triggered by a schedule
- **callerIP** (string) - IP address of the publisher of this message.
- **label** (string) - The label of the message assigned by the user.
- **flowControlKey** (string) - The flow control key used for rate limiting.
- **rate** (integer) - The rate value used for flow control.
- **period** (integer) - The period value used for flow control.
- **parallelism** (integer) - The parallelism value used for flow control.
- **responseStatus** (integer) - The HTTP status code received from the destination API.
- **responseHeader** (object) -
```

--------------------------------

### GET /v2/logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves logs with pagination support using a cursor. This is useful for handling large numbers of logs efficiently.

```APIDOC
## GET /v2/logs

### Description
Retrieves logs with pagination support using a cursor. This is useful for handling large numbers of logs efficiently.

### Method
GET

### Endpoint
/v2/logs

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - The cursor to fetch the next set of logs.

### Request Example
(No request body for GET)

### Response
#### Success Response (200)
- **logs** (array) - An array of log objects.
- **cursor** (string) - The cursor for the next page of results, or null if there are no more logs.

#### Response Example
{
  "logs": [
    {
      "messageId": "msg_abc123",
      "status": "DELIVERED",
      "tag": "email-campaign",
      "createdAt": 1678886400,
      "deduplicationId": "dedup_xyz789"
    }
  ],
  "cursor": "next_cursor_value"
}
```

--------------------------------

### GET /v2/messages/{messageId}

Source: https://upstash.com/docs/qstash/api-refence/messages/get-a-message

Retrieve details of a specific message using its unique identifier.

```APIDOC
## GET /v2/messages/{messageId}

### Description
Retrieve details of a specific message.

### Method
GET

### Endpoint
/v2/messages/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The identifier of the message to retrieve.

### Response
#### Success Response (200)
- **messageId** (string) - Unique identifier for the message
- **url** (string) - The URL to which the message should be delivered.
- **topicName** (string) - The URL Group (a.k.a. topic) name if this message was sent to a URL Group.
- **endpointName** (string) - The endpoint name of the message if the endpoint is given a name within the URL group.
- **method** (string) - The HTTP method to use for the message.
- **header** (object) - The HTTP headers sent to your API.
- **body** (string) - The body of the message if it is composed of utf8 chars only, empty otherwise.
- **bodyBase64** (string) - The base64 encoded body if the body contains a non-utf8 char only, empty otherwise.
- **maxRetries** (integer) - The number of retries that should be attempted in case of delivery failure.
- **notBefore** (integer) - The unix timestamp in milliseconds before which the message should not be delivered.
- **createdAt** (integer) - The unix timestamp in milliseconds when the message was created.
- **callback** (string) - The url where we send a callback each time the message is attempted to be delivered.
- **failureCallback** (string) - The url where we send a callback to after the message is failed
- **queueName** (string) - The name of the queue if the message is enqueued to a queue.
- **scheduleId** (string) - The scheduleId of the message if the message is triggered by a schedule
- **callerIP** (string) - IP address of the publisher of this message.
- **label** (string) - The label of the message assigned by the user.
- **flowControlKey** (string) - The flow control key used for rate limiting.
- **rate** (integer) - The rate value used for flow control.
- **period** (integer) - The period value used for flow control.
- **parallelism** (integer) - The parallelism value used for flow control.

#### Error Response (404)
- **error** (string) - Error message

#### Response Example
```json
{
  "messageId": "msg_abc123",
  "url": "https://example.com/webhook",
  "topicName": "my-topic",
  "endpointName": "default",
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"key\": \"value\"}",
  "bodyBase64": "",
  "maxRetries": 3,
  "notBefore": 1678886400000,
  "createdAt": 1678886300000,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure-callback",
  "queueName": "my-queue",
  "scheduleId": "sch_xyz789",
  "callerIP": "192.168.1.1",
  "label": "my-message-label",
  "flowControlKey": "fc_key_123",
  "rate": 10,
  "period": 60,
  "parallelism": 5
}
```
```

--------------------------------

### GET /v2/schedules - List All Schedules

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve a list of all scheduled messages. This endpoint requires authentication.

```APIDOC
## GET /v2/schedules

### Description
Retrieve a list of all scheduled messages. This endpoint requires authentication.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/schedules`

### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/schedules \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript SDK)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const scheds = await client.schedules.list();
```

### Response
#### Success Response (200)
- **schedules** (array) - An array of schedule objects.

#### Response Example
```json
{
  "schedules": [
    {
      "id": "sch_abc123",
      "cron": "* * * * *",
      "url": "https://example.com",
      "createdAt": 1678886400
    }
  ]
}
```
```

--------------------------------

### Run QStash CLI Dev Server with Bash

Source: https://upstash.com/docs/qstash/overall/llms-txt

Instructions for running the QStash CLI development server directly after downloading the binary. This bypasses package managers and involves executing the 'qstash dev' command from the terminal.

```bash
$ ./qstash dev

```

--------------------------------

### Get a Queue

Source: https://upstash.com/docs/qstash/api-refence/queues/get-a-queue

Retrieves details of a specific queue by its name. This endpoint is part of the Queues management API.

```APIDOC
## GET /v2/queues/{queueName}

### Description
Get details of a specific queue.

### Method
GET

### Endpoint
/v2/queues/{queueName}

### Parameters
#### Path Parameters
- **queueName** (string) - Required - The name of the queue to retrieve.

### Response
#### Success Response (200)
- **name** (string) - The name of the queue.
- **createdAt** (integer) - The creation timestamp of the queue in Unix milliseconds.
- **updatedAt** (integer) - The last update timestamp of the queue in Unix milliseconds.
- **parallelism** (integer) - The number of parallel consumers consuming from the queue.
- **paused** (boolean) - Whether the queue is paused.
- **lag** (integer) - The number of unprocessed messages that exist in the queue.

#### Error Response (400)
- **error** (string) - Queue name is invalid. Queue names can only contain alphanumeric characters, hyphens, periods, and underscores.

#### Error Response (404)
- **error** (string) - Queue not found.
```

--------------------------------

### Retrieve Signing Keys (HTTP)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Shows how to make an HTTP GET request to retrieve the current and next signing keys for QStash. This is essential for verifying the authenticity of incoming messages.

```http
GET /v2/keys?qstash_token=YOUR_QSTASH_TOKEN
```

--------------------------------

### Get Schedule Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves detailed information about a specific schedule, including its configuration, retry settings, and timing.

```APIDOC
## GET /v2/schedules/{scheduleId}

### Description
Get details of a specific schedule.

### Method
GET

### Endpoint
/v2/schedules/{scheduleId}

### Parameters
#### Path Parameters
- **scheduleId** (string) - Required - The ID of the schedule to retrieve.

### Request Example
```json
{
  "example": "No request body for GET request."
}
```

### Response
#### Success Response (200)
- **scheduleId** (string) - Unique identifier for the schedule
- **cron** (string) - The cron expression used to schedule the message
- **destination** (string) - The destination URL or URL Group name
- **createdAt** (integer) - The creation timestamp of the schedule in unix milliseconds
- **method** (string) - The HTTP method used for the scheduled message
- **header** (object) - Map of header names to arrays of header values
- **body** (string) - The body of the scheduled message
- **retries** (integer) - The number of retries for the scheduled message
- **delay** (integer) - The delay in seconds before the scheduled message is sent
- **callback** (string) - The callback URL for the scheduled message
- **failureCallback** (string) - The failure callback URL for the scheduled message
- **callerIp** (string) - The IP address of the client that created the schedule
- **isPaused** (boolean) - Whether the schedule is paused
- **flowControlKey** (string) - The flow control key used for rate limiting
- **parallelism** (integer) - The parallelism value used for flow control
- **rate** (integer) - The rate value used for flow control
- **period** (integer) - The period value used for flow control
- **retryDelayExpression** (string) - The retry delay expression used for calculating retry delays
- **label** (string) - The label assigned to the scheduled message
- **lastScheduleTime** (integer) - The last time the schedule was triggered in unix milliseconds
- **nextScheduleTime** (integer) - The next scheduled trigger time in unix milliseconds
- **lastScheduleStates** (object) - The states of the last scheduled messages

#### Response Example
```json
{
  "scheduleId": "sched_123",
  "cron": "* * * * *",
  "destination": "https://example.com/webhook",
  "createdAt": 1678886400000,
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"message\": \"Hello World\"}",
  "retries": 3,
  "delay": 0,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure",
  "callerIp": "192.168.1.1",
  "isPaused": false,
  "flowControlKey": "flow_abc",
  "parallelism": 10,
  "rate": 100,
  "period": 60,
  "retryDelayExpression": "$random(1,5)",
  "label": "my-schedule",
  "lastScheduleTime": 1678886400000,
  "nextScheduleTime": 1678886460000,
  "lastScheduleStates": {
    "status": "success"
  }
}
```

#### Error Response (404)
- **error** (string) - Schedule not found
```

--------------------------------

### Publishing Messages

Source: https://upstash.com/docs/qstash/overall/llms-txt

This section details how to publish messages to QStash. It includes the endpoint, required parameters, and examples for making requests.

```APIDOC
## POST /v2/publish/...

### Description
Publish messages to a QStash topic or queue.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>`

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash token.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
#### Success Response (200)
(Response details depend on the specific endpoint being called)

#### Response Example
(Response example depends on the specific endpoint being called)
```

--------------------------------

### Publish HTML Content to URL (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes raw HTML content to a specified URL instead of JSON. The `content_type` must be set to `text/html` to ensure the receiver interprets the body correctly. This is useful for sending non-JSON payloads.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.publish(
    url="https://my-api...",
    body="<html><body><h1>Hello World</h1></body></html>",
    content_type="text/html",
)
```

--------------------------------

### Publish JSON with Configured Retries (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message to a URL and configures the number of retries. The maximum number of retries is dependent on the QStash plan. The delay between retries defaults to exponential backoff, but can be customized.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    retries=1,
)
```

--------------------------------

### Initialize and Use Asynchronous QStash Client (Python)

Source: https://upstash.com/docs/qstash/sdks/py/gettingstarted

Shows how to initialize an asynchronous QStash client and publish a JSON message within an asyncio event loop. This is suitable for non-blocking operations.

```python
import asyncio

from qstash import AsyncQStash


async def main():
    client = AsyncQStash("<QSTASH_TOKEN>")
    await client.message.publish_json(...)

asyncio.run(main())
```

--------------------------------

### Batch Messages with Headers and Body (Python)

Source: https://upstash.com/docs/qstash/features/batch

This Python example utilizes the `qstash` library to send a batch of messages. The `client.message.batch_json` method accepts a list of dictionaries, where each dictionary represents a message with optional `url_group`, `url`, `delay`, `body`, and `headers`.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.batch_json(
      [
          {
              "url_group": "my-url-group",
              "delay": "5s",
              "body": {"hello": "world"},
              "headers": {"random": "header"},
          },
          {
              "url": "https://example.com/destination1",
              "delay": "1m",
          },
          {
              "url": "https://example.com/destination2",
              "body": {"hello": "again"},
          },
      ]
  )
  
```

--------------------------------

### Run QStash CLI Dev Server with Docker

Source: https://upstash.com/docs/qstash/overall/llms-txt

Instructions for running the QStash CLI development server locally using Docker. This involves pulling the QStash Docker image and running it with port mapping.

```bash
# Pull the image
docker pull public.ecr.aws/upstash/qstash:latest

# Run the image
docker run -p 8080:8080 public.ecr.aws/upstash/qstash:latest qstash dev
```

--------------------------------

### GET /v2/messages/{messageId}

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve details of a specific message by its unique identifier.

```APIDOC
## GET /v2/messages/{messageId}

### Description
Retrieve details of a specific message.

### Method
GET

### Endpoint
/v2/messages/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The identifier of the message to retrieve.

### Response
#### Success Response (200)
- **messageId** (string) - Unique identifier for the message
- **url** (string) - The URL to which the message should be delivered.
- **topicName** (string) - The URL Group (a.k.a. topic) name if this message was sent to a URL Group.
- **endpointName** (string) - The endpoint name of the message if the endpoint is given a name within the URL group.
- **method** (string) - The HTTP method to use for the message.
- **header** (object) - The HTTP headers sent to your API.
- **body** (string) - The body of the message if it is composed of utf8 chars only, empty otherwise.
- **bodyBase64** (string) - The base64 encoded body if the body contains a non-utf8 char only, empty otherwise.
- **maxRetries** (integer) - The number of retries that should be attempted in case of delivery failure.
- **notBefore** (integer) - The unix timestamp in milliseconds before which the message should not be delivered.
- **createdAt** (integer) - The unix timestamp in milliseconds when the message was created.
- **callback** (string) - The url where we send a callback each time the message is attempted to be delivered.
- **failureCallback** (string) - The url where we send a callback to after the message is failed
- **queueName** (string) - The name of the queue if the message is enqueued to a queue.
- **scheduleId** (string) - The scheduleId of the message if the message is triggered by a schedule
- **callerIP** (string) - IP address of the publisher of this message.
- **label** (string) - The label of the message assigned by the user.
- **flowControlKey** (string) - The flow control key used for rate limiting.
- **rate** (integer) - The rate value used for flow control.
- **period** (integer) - The period value used for flow control.
- **parallelism** (integer) - The parallelism value used for flow control.

#### Error Response (404)
- **error** (string) - Error message

### Response Example
#### Success Response (200)
```json
{
  "messageId": "msg_xxxxxx",
  "url": "https://example.com/webhook",
  "topicName": "my-topic",
  "endpointName": "default",
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"key\": \"value\"}",
  "bodyBase64": "",
  "maxRetries": 3,
  "notBefore": 1678886400000,
  "createdAt": 1678886000000,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure-callback",
  "queueName": "my-queue",
  "scheduleId": "sch_yyyyyy",
  "callerIP": "192.168.1.1",
  "label": "my-message-label",
  "flowControlKey": "fc_key_zzzzzz",
  "rate": 10,
  "period": 60,
  "parallelism": 5
}
```
#### Error Response (404)
```json
{
  "error": "Message not found"
}
```
```

--------------------------------

### Publish Message

Source: https://upstash.com/docs/qstash/overall/llms-txt

Publishes a message to a specified URL using a cURL example. Requires authentication and sets the content type.

```APIDOC
## POST /v2/publish/:url

### Description
Publishes a message to a specified URL. This endpoint is used for sending one-time messages.

### Method
POST

### Endpoint
`/v2/publish/:url`

### Parameters
#### Path Parameters
- **url** (string) - Required - The destination URL where the message will be published.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication (e.g., `Bearer <QSTASH_TOKEN>`)
- **Content-Type** (string) - Required - Specifies the format of the request body (e.g., `application/json`)

#### Request Body
- **body** (object) - Required - The content of the message to be published. The structure depends on the `Content-Type`.

### Request Example
```bash
curl --request POST "https://qstash.upstash.io/v2/publish/https://winter-cherry-9545.fly.dev" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{\"hello\": \"world\"}"
```

### Response
#### Success Response (200 OK)
Indicates the message was successfully published.

#### Response Example
```json
{
  "messageId": "msg_xxxxxx"
}
```
```

--------------------------------

### Schedule to a Queue

Source: https://upstash.com/docs/qstash/features/schedules

This example illustrates scheduling an item to be added to a specific queue at a defined time. It involves specifying the destination URL, the cron schedule, and the queue name using the `Upstash-Queue-Name` header or a `queueName` parameter.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  cron: "* * * * *",
  queueName: "yourQueueName",
});
```

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Cron: * * * * *" \
    -H "Upstash-Queue-Name: yourQueueName" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

--------------------------------

### Get Queue Details (cURL, TypeScript, Python)

Source: https://upstash.com/docs/qstash/features/queues

Retrieves the configuration details for a specific QStash queue, including its parallelism settings. Requires QStash authentication.

```bash
curl https://qstash.upstash.io/v2/queues/my-queue \
    -H "Authorization: Bearer <token>"
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });

  const queue = client.queue({
    queueName: "my-queue"
  })

  const res = await queue.get()
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.queue.get("my-queue")
```

--------------------------------

### QStash Schedule Success Response Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This JSON object represents a successful response when retrieving schedule details. It includes various properties defining the schedule's configuration and status.

```json
{
  "scheduleId": "sched_123",
  "cron": "* * * * *",
  "destination": "https://example.com/webhook",
  "createdAt": 1678886400000,
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"message\": \"Hello World\"}",
  "retries": 3,
  "delay": 0,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure",
  "callerIp": "192.168.1.1",
  "isPaused": false,
  "flowControlKey": "flow_abc",
  "parallelism": 10,
  "rate": 100,
  "period": 60,
  "retryDelayExpression": "$random(1,5)",
  "label": "my-schedule",
  "lastScheduleTime": 1678886400000,
  "nextScheduleTime": 1678886460000,
  "lastScheduleStates": {
    "status": "success"
  }
}
```

--------------------------------

### GET /v2/message/{messageId}

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve details for a specific message using its unique identifier.

```APIDOC
## GET /v2/message/{messageId}

### Description
Retrieve details for a specific message using its ID.

### Method
GET

### Endpoint
`/v2/message/{messageId}`

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The unique identifier of the message.

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")

try:
    message = client.message.get("msg_123")
    print(f"Message {message['messageId']} to {message['url']}")
    print(f"Body: {message['body']}")
except Exception as e:
    print("Message already delivered or not found")
```

### Response
#### Success Response (200)
- **messageId** (string) - The unique identifier of the message.
- **url** (string) - The target URL the message was sent to.
- **body** (object) - The content of the message.
```

--------------------------------

### GET /schedules/{scheduleId}

Source: https://upstash.com/docs/qstash/sdks/ts/examples/schedules

Retrieves details of a specific schedule using its unique ID.

```APIDOC
## GET /schedules/{scheduleId}

### Description
Retrieves the details of a specific schedule by its ID.

### Method
GET

### Endpoint
/v1/schedules/{scheduleId}

### Parameters
#### Path Parameters
- **scheduleId** (string) - Required - The unique identifier of the schedule to retrieve.

### Response
#### Success Response (200)
- **scheduleId** (string) - The ID of the schedule.
- **cron** (string) - The cron expression used for the schedule.
- **destination** (string) - The destination URL.
- **callback** (string) - The callback URL.
- **failureCallback** (string) - The failure callback URL.
- **isPaused** (boolean) - Indicates if the schedule is paused.

#### Response Example
```json
{
  "scheduleId": "schedule-123",
  "cron": "*/5 * * * *",
  "destination": "https://my-api...",
  "callback": "https://my-callback...",
  "failureCallback": "https://my-failure-callback...",
  "isPaused": false
}
```
```

--------------------------------

### Publish JSON with Timeout

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a URL with a specified timeout for the request. The timeout value is in seconds. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  timeout: "30s" // 30 seconds timeout
});
```

--------------------------------

### Get All DLQ Messages with Pagination

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves all messages from the Dead Letter Queue (DLQ) using cursor-based pagination.

```APIDOC
## GET /dlq

### Description
Retrieve all messages from the Dead Letter Queue (DLQ) with pagination.

### Method
GET

### Endpoint
/dlq

### Query Parameters
- **cursor** (string) - Optional - The cursor for pagination. If omitted, fetches the first page.

### Response
#### Success Response (200)
- **messages** (array) - An array of DLQ messages.
  - **message** (object) - A DLQ message object.
- **cursor** (string) - The cursor for the next page of results. `null` if there are no more pages.

#### Response Example
```json
{
  "messages": [
    {
      "message": {
        "body": "{\"hello\": \"world\"}",
        "headers": {},
        "messageId": "msg_abc123xyz",
        "url": "https://example.com"
      },
      "nextRunAt": "2023-10-27T10:00:00Z",
      "attemptCount": 3
    }
  ],
  "cursor": "next_cursor_string"
}
```
```

--------------------------------

### Verify Request via QStash SDK (TypeScript)

Source: https://upstash.com/docs/qstash/howto/signature

This example demonstrates how to use the QStash SDK for TypeScript to verify the signature of an incoming request. It requires your current and next signing keys.

```APIDOC
## POST /your-api-endpoint

### Description
Verifies an incoming request from QStash using the provided JWT signature.

### Method
POST

### Endpoint
/your-api-endpoint

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
* **body** (string) - Required - The raw request body received from QStash.
* **signature** (string) - Required - The `Upstash-Signature` header value.
* **url** (string) - Required - The URL of your API endpoint.

### Request Example
```typescript
import { Receiver } from "@upstash/qstash";

const receiver = new Receiver({
  currentSigningKey: "YOUR_CURRENT_SIGNING_KEY",
  nextSigningKey: "YOUR_NEXT_SIGNING_KEY",
});

// Assuming 'req' is your incoming request object
const signature = req.headers["Upstash-Signature"];
const body = req.body; // Ensure this is the raw request body string

const isValid = await receiver.verify({
  body,
  signature,
  url: "YOUR-SITE-URL",
});

if (isValid) {
  // Process the request
} else {
  // Handle invalid signature
}
```

### Response
#### Success Response (200)
Indicates the request signature was valid and the request can be processed.

#### Response Example
(No specific response body is defined for a successful verification, the action is to proceed with processing the request.)

#### Error Response (401 or other)
Indicates the request signature was invalid.
```

--------------------------------

### Create and Execute Workflow with FastAPI (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Defines and executes a workflow using the Upstash Workflow SDK for Python integrated with FastAPI. This example shows sequential steps like sending emails and using sleep timers within an asynchronous endpoint. It requires a QSTASH_TOKEN.

```python
# main.py (FastAPI)
from upstash_workflow import Workflow, WorkflowContext
from fastapi import FastAPI

app = FastAPI()
workflow = Workflow(qstash_token="<QSTASH_TOKEN>")

@app.post("/workflow")
async def workflow_endpoint(request: dict):
    async def workflow_logic(context: WorkflowContext):
        user_id = request["userId"]
        email = request["email"]
        name = request["name"]

        # Step 1: Send welcome email
        await context.run("send-welcome-email", lambda: send_email(email, "Welcome!"))

        # Step 2: Wait for 3 days
        await context.sleep("sleep-until-follow-up", 60 * 60 * 24 * 3)

        # Step 3: Send follow-up
        await context.run("send-follow-up", lambda: send_email(email, "How are you?"))

    return await workflow.execute(workflow_logic)
```

--------------------------------

### GET /v2/dlq/{dlqId}

Source: https://upstash.com/docs/qstash/api-refence/dlq/get-a-dlq-message

Retrieves a specific message from the Dead Letter Queue (DLQ) using its DLQ ID.

```APIDOC
## GET /v2/dlq/{dlqId}

### Description
Get a specific message from the DLQ.

### Method
GET

### Endpoint
/v2/dlq/{dlqId}

### Parameters
#### Path Parameters
- **dlqId** (string) - Required - The DLQ ID of the message you want to retrieve.

### Response
#### Success Response (200)
- **messageId** (string) - Unique identifier for the message
- **url** (string) - The URL to which the message should be delivered.
- **topicName** (string) - The URL Group (a.k.a. topic) name if this message was sent to a URL Group.
- **endpointName** (string) - The endpoint name of the message if the endpoint is given a name within the URL group.
- **method** (string) - The HTTP method to use for the message.
- **header** (object) - The HTTP headers sent to your API.
- **body** (string) - The body of the message if it is composed of utf8 chars only, empty otherwise.
- **bodyBase64** (string) - The base64 encoded body if the body contains a non-utf8 char only, empty otherwise.
- **maxRetries** (integer) - The number of retries that should be attempted in case of delivery failure.
- **notBefore** (integer) - The unix timestamp in milliseconds before which the message should not be delivered.
- **createdAt** (integer) - The unix timestamp in milliseconds when the message was created.
- **callback** (string) - The url where we send a callback each time the message is attempted to be delivered.
- **failureCallback** (string) - The url where we send a callback to after the message is failed
- **queueName** (string) - The name of the queue if the message is enqueued to a queue.
- **scheduleId** (string) - The scheduleId of the message if the message is triggered by a schedule
- **callerIP** (string) - IP address of the publisher of this message.
- **label** (string) - The label of the message assigned by the user.
- **flowControlKey** (string) - The flow control key used for rate limiting.
- **rate** (integer) - The rate value used for flow control.
- **period** (integer) - The period value used for flow control.
- **parallelism** (integer) - The parallelism value used for flow control.
- **responseStatus** (integer) - The HTTP status code received from the destination API.
- **responseHeader** (object) - 

#### Response Example
{
  "messageId": "msg_abc123",
  "url": "https://example.com/webhook",
  "topicName": "my-topic",
  "endpointName": "main-endpoint",
  "method": "POST",
  "header": {
    "Content-Type": ["application/json"]
  },
  "body": "{\"key\": \"value\"}",
  "bodyBase64": "",
  "maxRetries": 3,
  "notBefore": 1678886400000,
  "createdAt": 1678886000000,
  "callback": "https://example.com/callback",
  "failureCallback": "https://example.com/failure-callback",
  "queueName": "my-queue",
  "scheduleId": "sch_xyz789",
  "callerIP": "192.168.1.1",
  "label": "important-message",
  "flowControlKey": "fc_key_123",
  "rate": 100,
  "period": 60,
  "parallelism": 10,
  "responseStatus": 200,
  "responseHeader": {
    "X-Custom-Header": ["Value"]
  }
}

#### Error Response (404)
Description: If the message is not found in the DLQ, (either is has been removed by you, or automatically), the endpoint returns a 404 status code.
Content: application/json schema: $ref: '#/components/schemas/Error'
```

--------------------------------

### Publish Message with Custom Headers (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of publishing a JSON message with custom headers using the Upstash QStash Python client.

```APIDOC
## Publish Message with Custom Headers (Python)

### Description
Example of publishing a JSON message with custom headers using the Upstash QStash Python client.

### Method
POST (Implicitly via client library)

### Endpoint
N/A (Client Library Function)

### Parameters
#### Request Body (Implicit)
- **queue** (string) - Required - The name of the queue to send the message to.
- **url** (string) - Required - The URL to send the message to.
- **body** (object) - Required - The JSON payload of the message.
- **headers** (object) - Optional - Custom headers to include with the message.

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.enqueue_json(
    queue="my-queue",
    url="https://example.com",
    body={
        "key": "value",
    },
    headers={
        "X-Custom-Header": "custom-value",
    },
)
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the enqueued message.
```

--------------------------------

### Publish Message with Custom Header

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to publish a message to QStash with a custom header. This allows you to pass additional metadata to your target endpoint. Examples are provided for cURL, TypeScript, and Python.

```APIDOC
## Publish Message with Custom Header

### Description
Publish a message to QStash and include a custom header for additional metadata. This example uses cURL to send a JSON payload with a custom header.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/publish/<destination_url>`

### Parameters
#### Request Headers
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`
- **Upstash-Forward-My-Header** (string) - Required - The custom header key and value (e.g., `My-Header: my-value`)
- **Content-type** (string) - Required - `application/json`

#### Request Body
- **(JSON Object)** - Required - The payload of the message.

### Request Example (cURL)
```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H 'Upstash-Forward-My-Header: my-value' \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

### Request Example (TypeScript SDK)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  headers: {
    "My-Header": "my-value",
  },
});
```

### Request Example (Python SDK)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    headers={
        "My-Header": "my-value",
    },
)
# Async version is also available
```

### Response
(Response details depend on the specific operation and target endpoint.)
```

--------------------------------

### QStash Retry-After Header Examples

Source: https://upstash.com/docs/qstash/features/retry

Demonstrates various ways to set the Retry-After header to control when QStash should retry a message. Supports seconds, duration format, and RFC1123 date format. Retries are capped at one day.

```text
Retry-After: 0
Retry-After: 10
Retry-After: 6m5s
Retry-After: Sun, 27 Jun 2024 12:16:24 GMT
```

--------------------------------

### QStash API Authentication Methods

Source: https://upstash.com/docs/qstash/api/events/list

This section details how to authenticate your API requests to QStash, either by including your QSTASH_TOKEN in the Authorization header or as a query parameter.

```APIDOC
## QStash API Authentication

### Description
Authenticate your requests to the QStash API by providing your `QSTASH_TOKEN`.

### Method
Authentication can be performed using either the `Authorization` header or a query parameter.

### Endpoint
N/A (Applies to all QStash API endpoints)

### Parameters
#### Request Header
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

#### Query Parameters
- **qstash_token** (string) - Required - Your `QSTASH_TOKEN`

### Request Example (Bearer Token)
```bash
curl https://qstash.upstash.io/v2/publish/\n  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Request Example (Query Parameter)
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
Authentication is verified before the actual endpoint response is returned. If authentication fails, an appropriate error response will be provided by the API.
```

--------------------------------

### Resume Queue

Source: https://upstash.com/docs/qstash/api-refence/queues/resume-queue

Resumes a queue to start the delivery of enqueued messages. If the queue is already active, this action has no effect.

```APIDOC
## POST /v2/queues/{queueName}/resume

### Description
Resumes a queue to start the delivery of enqueued messages, beginning with the earliest undelivered message. If the queue is already active, this action has no effect.

<Warning>
  Resuming or creating a queue may take up to a minute. Therefore, it is not recommended to pause or delete a queue during critical operations.
</Warning>

### Method
POST

### Endpoint
/v2/queues/{queueName}/resume

### Parameters
#### Path Parameters
- **queueName** (string) - Required - The name of the queue to resume.

### Request Example
```json
{
  "example": "No request body needed for this endpoint."
}
```

### Response
#### Success Response (200)
- **message** (string) - Indicates that the queue was resumed successfully.

#### Response Example
```json
{
  "message": "Queue resumed successfully"
}
```

#### Error Response (400)
- **error** (string) - Describes the error, e.g., "Queue name is invalid. Queue names can only contain alphanumeric characters, hyphens, periods, and underscores."

#### Error Response Example
```json
{
  "error": "Queue name is invalid. Queue names can only contain alphanumeric characters, hyphens, periods, and underscores."
}
```
```

--------------------------------

### Initialize QStash Client (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes the QStash client using the Python SDK. The SDK handles retries internally, and both synchronous and asynchronous versions are available.

```APIDOC
## Initialize QStash Client (Python)

### Description
Initializes the QStash client using the Python SDK. The Python SDK handles retries internally, abstracting this complexity from the developer. Both synchronous and asynchronous client versions are available.

### Code
```python
from qstash import QStash

# Python SDK handles retries internally
client = QStash("<QSTASH_TOKEN>")

# Both sync and async versions available
from qstash import AsyncQStash

async_client = AsyncQStash("<QSTASH_TOKEN>")
```
```

--------------------------------

### Publish Message with Delay using QStash

Source: https://upstash.com/docs/qstash/overall/apiexamples

Publish a JSON message with a specified delay before delivery using QStash. Supports cURL, Typescript, and Python SDKs. The delay is specified in minutes (e.g., '5m').

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Delay: 5m" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  delay: 300,
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    delay="5m",
)
# Async version is also available
```

--------------------------------

### Get Message Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve details for a specific message by its ID. This endpoint is only available while the message is being processed.

```APIDOC
## GET /v2/messages/{messageId}

### Description
Retrieve details for a specific message by its ID. This is only available while the message is being processed.

### Method
GET

### Endpoint
`/v2/messages/{messageId}`

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The ID of the message to retrieve.

#### Query Parameters
None

#### Request Body
None

### Request Example
```bash
curl https://qstash.upstash.io/v2/messages/msg_123 \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Response
#### Success Response (200)
- **messageId** (string) - The unique identifier of the message.
- **url** (string) - The URL the message was sent to.
- **createdAt** (integer) - The timestamp when the message was created.
- **body** (string) - The content of the message.

#### Response Example
```json
{
  "messageId": "msg_123",
  "url": "https://example.com/webhook",
  "createdAt": 1678886400,
  "body": "{\"key\": \"value\"}"
}
```
```

--------------------------------

### Golang Imports for QStash Webhook Handling

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Imports necessary Go packages for handling HTTP requests, reading request bodies, cryptographic operations (SHA256, Base64), JWT parsing, and environment variable access. These are required for processing QStash webhooks.

```go
package main

import (
	"crypto/sha256"
	"encoding/base64"
	"fmt"
	"github.com/golang-jwt/jwt/v4"
	"io"
	"net/http"
	"os"
	"time"
)
```

--------------------------------

### Publish Message with Custom Headers (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Example of publishing a JSON message with custom headers using the Upstash QStash TypeScript client.

```APIDOC
## Publish Message with Custom Headers (TypeScript)

### Description
This example shows how to publish a JSON message with custom headers using the Upstash QStash TypeScript client.

### Method
POST

### Endpoint
(Client-side abstraction, maps to `/publish`)

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **url** (string) - Required - The URL of the destination.
- **body** (object) - Required - The JSON payload of the message.
- **headers** (object) - Optional - Key-value pairs for custom headers to be forwarded.

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://example.com",
  body: { "hello": "world" },
  headers: { "my-header": "my-value" },
});
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.

#### Response Example
```json
{
  "messageId": "msg_abc123"
}
```
```

--------------------------------

### Get QStash Queue Configuration

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves the configuration details for a specified QStash queue, including its parallelism settings. This allows users to inspect the current settings of an existing queue.

```APIDOC
## Get QStash Queue Configuration

Retrieves the configuration details for a specified QStash queue, including its parallelism settings. This allows users to inspect the current settings of an existing queue.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/queues/<queue_name>`

### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```bash
curl https://qstash.upstash.io/v2/queues/my-queue \
    -H "Authorization: Bearer <token>"
```

### Request Example (TypeScript)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const queue = client.queue({
  queueName: "my-queue"
})

const res = await queue.get()
```

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.queue.get("my-queue")
```
```

--------------------------------

### Publish Messages to FIFO Queue using cURL and TypeScript SDK

Source: https://upstash.com/docs/qstash/overall/llms-txt

Examples for publishing messages to a First-In, First-Out (FIFO) queue in Upstash QStash using cURL and the TypeScript SDK. Requires specifying the queue name and destination URL.

```shell
curl -XPOST -H 'Authorization: Bearer XXX' \
                -H "Content-type: application/json" \
                'https://qstash.upstash.io/v2/enqueue/my-queue/https://example.com' \
                -d '{"message":"Hello, World!"}'
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const queue = client.queue({
  queueName: "my-queue"
})

await queue.enqueueJSON({
  url: "https://example.com",
  body: {
    "Hello": "World"
  }
})
```

--------------------------------

### Get Flow Control Status

Source: https://upstash.com/docs/qstash/features/flowcontrol

Retrieve information about messages waiting for flow control limits to be met.

```APIDOC
## GET /v2/flow-control/:key

### Description
Get the number of messages waiting for flow control limits for a given key.

### Method
GET

### Endpoint
`/v2/flow-control/:key`

### Parameters
#### Path Parameters
- **key** (string) - Required - The flow control key to query.

### Response
#### Success Response (200)
- **pending** (integer) - The number of messages pending due to flow control.

#### Response Example
```json
{
  "pending": 5
}
```
```

--------------------------------

### Verifying Incoming Requests

Source: https://upstash.com/docs/qstash/howto/multi-region

This section details how to verify incoming requests to your QStash endpoints. It explains the use of the `upstash-region` header for multi-region support and provides a TypeScript example using the `Receiver` class.

```APIDOC
## Verifying Incoming Requests

QStash includes an `upstash-region` header with every request to indicate the source region.

```
upstash-region: US-EAST-1
```

With this header, the SDK can determine which signing keys to use when verifying the request if `QSTASH_REGION` is set. For this to work correctly, the value of the `upstash-region` header should be passed to the `verify` method.

### Method
POST

### Endpoint
(Not specified, assumed to be handled by your application)

### Parameters
#### Request Body
(The request body is processed by `request.text()`)

#### Headers
- **upstash-signature** (string) - Required - The signature of the incoming request.
- **upstash-region** (string) - Optional - The region from which the request originated. If not provided, it defaults to `undefined`.

### Request Example
```typescript
import { Receiver } from "@upstash/qstash";

// Initialize receiver (works in both modes)
const receiver = new Receiver();

// Verify the incoming request
await receiver.verify({
  signature: request.headers.get("upstash-signature")!,
  body: await request.text(),
  // Pass the region header for multi-region support
  upstashRegion: request.headers.get("upstash-region") ?? undefined,
});
```

### Response
(The response is handled by your application logic after verification.)
```

--------------------------------

### Fly.io Deployment

Source: https://upstash.com/docs/qstash/overall/llms-txt

Deploys the application to the Fly.io platform using the `flyctl` command.

```APIDOC
## Deploy Application with Flyctl

### Description
Deploys the application to the Fly.io platform. This command assumes the Fly.io CLI is installed and configured.

### Method
N/A (CLI Command)

### Command
`flyctl deploy`

### Usage
1. Ensure you have the Fly.io CLI installed and authenticated.
2. Navigate to your project directory.
3. Run the deploy command: `flyctl deploy`

### Notes
- The `flyctl deploy` command will build your application image and deploy it to Fly.io. Follow any prompts for configuration.
```

--------------------------------

### Set Environment Variables for QStash Signing Keys (Bash)

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Sets the current and next signing keys for QStash as environment variables using the `flyctl secrets set` command. This is crucial for secure communication with QStash. Ensure you have obtained your keys from the Upstash Console.

```bash
flyctl secrets set QSTASH_CURRENT_SIGNING_KEY=...
flyctl secrets set QSTASH_NEXT_SIGNING_KEY=...
```

--------------------------------

### QStash Publish Webhook URL Configuration

Source: https://upstash.com/docs/qstash/howto/webhook

This example shows how to configure your webhook URL as a QStash publish request. QStash acts as an intermediary, forwarding the request to your specified endpoint. Configuration options like retries and timeouts can be set via HTTP headers or query parameters.

```URL
https://qstash.upstash.io/v2/publish/https://example.com/api/webhook?qstash_token=<QSTASH_TOKEN>
```

--------------------------------

### QStash Upstash-Retried Header Example

Source: https://upstash.com/docs/qstash/features/retry

Shows the format of the Upstash-Retried header, which QStash adds to requests sent to your API to indicate the number of previous retry attempts.

```text
Upstash-Retried: 0
Upstash-Retried: 1
Upstash-Retried: 2
```

--------------------------------

### Create Project Directory and File (Bash)

Source: https://upstash.com/docs/qstash/quickstarts/aws-lambda/python

Initializes a new project directory for AWS Lambda and creates the main Python file for the handler function. This sets up the basic file structure for the project.

```bash
mkdir aws-lambda
cd aws-lambda
touch lambda_function.py
```

--------------------------------

### Create a Schedule to a URL Group

Source: https://upstash.com/docs/qstash/overall/llms-txt

This code illustrates how to schedule messages to be published to a URL Group using its name or ID. The examples are provided for TypeScript, Python, and cURL, enabling flexible integration into different projects.

```APIDOC
## POST /v2/schedules/{URL_GROUP_ID_OR_NAME}

### Description
Create a schedule to publish messages to a URL Group.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/schedules/<URL_GROUP_ID_OR_NAME>`

### Parameters
#### Path Parameters
- **URL_GROUP_ID_OR_NAME** (string) - Required - The ID or name of the URL Group.

#### Query Parameters
None

#### Request Headers
- **Authorization** (string) - Required - Bearer token (`Bearer <QSTASH_TOKEN>`).
- **Content-type** (string) - Required - `application/json`.
- **Upstash-Cron** (string) - Required - The cron expression for scheduling (e.g., `* * * * *`).

#### Request Body
- **hello** (string) - Required - Example message content.

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "urlGroupName",
  cron: "* * * * *",
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="url-group-name",
    cron="* * * * *",
)
```

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Cron: * * * * *" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/<URL_GROUP_ID_OR_NAME>'
```

### Response
#### Success Response (200)
- **scheduleId** (string) - The ID of the created schedule.
```

--------------------------------

### Schedule Daily Task with QStash

Source: https://upstash.com/docs/qstash/overall/llms-txt

Provides examples for scheduling a task to run daily at midnight using QStash. The cron syntax '0 0 * * *' is used for daily execution. This requires authentication, the destination URL, and the cron schedule.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Upstash-Cron: 0 0 * * *" \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  cron: "0 0 * * *",
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.create(
    destination="https://example.com",
    cron="0 0 * * *",
)
# Async version is also available
```

--------------------------------

### QStash API Authentication - Query Parameter

Source: https://upstash.com/docs/qstash/api/schedules/create

Authenticate QStash API requests by including your QSTASH_TOKEN as a query parameter when headers cannot be used.

```APIDOC
## QStash API Authentication - Query Parameter

### Description
This method shows how to authenticate API requests by providing your `QSTASH_TOKEN` as a query parameter. This is useful in environments where setting request headers is not possible.

### Method
All HTTP Methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*`

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your `QSTASH_TOKEN`

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/some-topic?qstash_token=<YOUR_QSTASH_TOKEN>
```

### Response
#### Success Response (200)
Responses vary based on the specific endpoint called.

#### Response Example
(Example depends on the specific endpoint)
```

--------------------------------

### Initializing QStash Receiver (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Initializes a new Receiver instance with provided signing keys from environment variables for verifying incoming webhook signatures.

```APIDOC
## Initializing QStash Receiver

### Description
Initializes a new `Receiver` instance with the provided signing keys from the environment variables. This instance will be used to verify incoming webhook signatures.

### Method
Not Applicable (Client-side initialization)

### Endpoint
Not Applicable

### Parameters
#### Environment Variables
- **QSTASH_CURRENT_SIGNING_KEY** (string) - Required - The current signing key for QStash webhooks.
- **QSTASH_NEXT_SIGNING_KEY** (string) - Optional - The next signing key for QStash webhooks.

### Request Example
```typescript
const receiver = new Receiver({
  currentSigningKey: env.QSTASH_CURRENT_SIGNING_KEY,
  nextSigningKey: env.QSTASH_NEXT_SIGNING_KEY,
});
```

### Response
Not Applicable (Client-side initialization)
```

--------------------------------

### Get Flow Control Key Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details of a specific Flow Control key using the QStash API.

```APIDOC
## GET /v2/flowControl/{flowControlKey}

### Description
Get details of a specific Flow Control key.

### Method
GET

### Endpoint
`/v2/flowControl/{flowControlKey}`

### Parameters
#### Path Parameters
- **flowControlKey** (string) - Required - The Flow Control key to retrieve

### Responses
#### Success Response (200)
- **flowControlKey** (string) - The flow control key name
- **waitlistSize** (integer) - The number of messages waiting due to flow control configuration.

#### Error Response (404)
- **error** (string) - Error message
```

--------------------------------

### Python HTTP Server for QStash Endpoint

Source: https://upstash.com/docs/qstash/quickstarts/python-vercel

Creates a simple Python HTTP server using the 'http.server' module to expose the database cleanup logic as a public POST endpoint. This allows QStash to invoke the cleanup function remotely. Replace placeholders with your Upstash Redis credentials.

```python
from http.server import BaseHTTPRequestHandler
from upstash_redis import Redis

redis = Redis(url="https://YOUR_REDIS_URL", token="YOUR_TOKEN")

def delete_all_entries():
  keys = redis.keys("*") # Match all keys
  redis.delete(*keys)


class handler(BaseHTTPRequestHandler):
  def do_POST(self):
    delete_all_entries()
    self.send_response(200)
    self.end_headers()
```

--------------------------------

### Get Flow Control Key

Source: https://upstash.com/docs/qstash/api-refence/flow-control/get-flow-control-key

Retrieves details of a specific Flow Control key by its identifier. This endpoint is part of the QStash REST API.

```APIDOC
## GET /v2/flowControl/{flowControlKey}

### Description
Get details of a specific Flow Control key.

### Method
GET

### Endpoint
/v2/flowControl/{flowControlKey}

### Parameters
#### Path Parameters
- **flowControlKey** (string) - Required - The Flow Control key to retrieve

### Response
#### Success Response (200)
- **flowControlKey** (string) - The flow control key name
- **waitlistSize** (integer) - The number of messages waiting due to flow control configuration.

#### Response Example
```json
{
  "flowControlKey": "my-key",
  "waitlistSize": 10
}
```

#### Error Response (404)
- **error** (string) - Error message

#### Response Example
```json
{
  "error": "Flow Control key not found"
}
```
```

--------------------------------

### Publish JSON to URL Group with Delay, Headers, and Body

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a URL group with a 3-second delay, custom headers, and a JSON body. URL groups must be pre-configured. The response is an array of message IDs for each URL in the group. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  urlGroup: "my-url-group",
  body: { hello: "world" },
  headers: { "test-header": "test-value" },
  delay: "3s",
});

// When publishing to a URL Group, the response is an array of messages for each URL in the URL Group
console.log(res[0].messageId);
```

--------------------------------

### GET /v2/dlq

Source: https://upstash.com/docs/qstash/api-refence/dlq/list-dlq-messages

List and paginate through all messages currently in the Dead Letter Queue (DLQ). Supports filtering by various criteria.

```APIDOC
## GET /v2/dlq

### Description
List and paginate through all messages currently in the DLQ. Supports filtering by message ID, destination URL, topic name, schedule ID, queue name, date range, response status, caller IP, and labels.

### Method
GET

### Endpoint
/v2/dlq

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - By providing a cursor you can paginate through all of the messages in the DLQ
- **messageId** (string) - Optional - Filter DLQ messages by message ID
- **url** (string) - Optional - Filter DLQ messages by destination URL
- **topicName** (string) - Optional - Filter DLQ messages by URL Group name
- **scheduleId** (string) - Optional - Filter DLQ messages by schedule ID
- **queueName** (string) - Optional - Filter DLQ messages by queue name
- **fromDate** (integer) - Optional - Filter DLQ messages by starting date, in milliseconds (Unix timestamp). This is inclusive.
- **toDate** (integer) - Optional - Filter DLQ messages by ending date, in milliseconds (Unix timestamp). This is inclusive.
- **responseStatus** (integer) - Optional - Filter DLQ messages by HTTP response status code of the last delivery attempt
- **callerIp** (string) - Optional - Filter DLQ messages by IP address of the publisher
- **label** (string) - Optional - Filter DLQ messages by the label of the message assigned by the user
- **count** (integer) - Optional - The number of messages to return. Defaults to 100, maximum 100.
- **order** (string) - Optional - The sorting order of DLQ messages by timestamp. Enum: `latestFirst`, `earliestFirst`. Defaults to `latestFirst`.

### Response
#### Success Response (200)
- **cursor** (string) - A cursor which you can use in subsequent requests to paginate through all messages. If no cursor is returned, you have reached the end of the messages.
- **messages** (array) - An array of DLQMessage objects.

##### DLQMessage Object
- **messageId** (string) - Unique identifier for the message
- **url** (string) - The URL to which the message should be delivered.
- **topicName** (string) - The URL Group (a.k.a. topic) name if this message was sent to a URL Group.
- **endpointName** (string) - The endpoint name of the message if the endpoint is given a name within the URL group.
- **method** (string) - The HTTP method to use for the message.
- **header** (object) - The headers of the message.

#### Response Example
```json
{
  "cursor": "some_cursor_string",
  "messages": [
    {
      "messageId": "msg_123",
      "url": "https://example.com/webhook",
      "topicName": "my-topic",
      "endpointName": "default",
      "method": "POST",
      "header": {
        "Content-Type": "application/json"
      }
    }
  ]
}
```
```

--------------------------------

### Overwrite Existing QStash Schedule

Source: https://upstash.com/docs/qstash/overall/llms-txt

Updates an existing QStash schedule by providing its `scheduleId`. Examples are provided for TypeScript and cURL.

```APIDOC
## PUT /v2/schedules/:url

### Description
Updates an existing QStash schedule by providing its `scheduleId`. This operation allows modification of the schedule's configuration or destination.

### Method
PUT (via SDK) or POST (via cURL with specific headers)

### Endpoint
`/v2/schedules/:url` (for cURL)
(Handled by SDK for TypeScript)

### Parameters
#### Path Parameters
- **url** (string) - Required - The URL associated with the schedule.

#### Query Parameters
None

#### Request Body
- **body** (object) - Optional - The payload to be sent when the schedule triggers.

#### Headers (for cURL)
- **Authorization** (string) - Required - Bearer token for authentication.
- **Content-type** (string) - Required - Set to `application/json`.
- **Upstash-Cron** (string) - Required - The new cron expression for the schedule.
- **Upstash-Schedule-Id** (string) - Required - The ID of the schedule to overwrite.

#### SDK Parameters (TypeScript)
- **destination** (string) - Required - The URL the schedule will send messages to.
- **scheduleId** (string) - Required - The ID of the schedule to overwrite.
- **cron** (string) - Required - The cron expression defining the schedule's interval.
- **body** (object) - Optional - The payload to be sent when the schedule triggers.

### Request Example (TypeScript)
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.schedules.create({
  destination: "https://example.com",
  scheduleId: "existingScheduleId",
  cron: "* * * * *",
});
```

### Request Example (cURL)
```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Cron: * * * * *" \
    -H "Upstash-Schedule-Id: existingScheduleId" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/schedules/https://example.com'
```

### Response
#### Success Response (200)
(Typically returns an empty response or a confirmation of the update.)
```

--------------------------------

### QStash API Authentication - Query Parameter

Source: https://upstash.com/docs/qstash/api/flow-control/list

This section explains how to authenticate your API requests using the `qstash_token` query parameter. This method is useful in environments where setting request headers is not feasible.

```APIDOC
## QStash API Authentication - Query Parameter

### Description
Authenticate your API requests by including your `QSTASH_TOKEN` as a query parameter named `qstash_token`. This method is an alternative for environments where modifying request headers is not possible.

### Method
All HTTP Methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*?qstash_token=<QSTASH_TOKEN>`

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash authentication token.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
#### Success Response (200)
Responses will vary based on the specific endpoint called.

#### Response Example
(Example varies by endpoint)
```

--------------------------------

### Publish JSON Message with Custom Headers (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

An example illustrating how to publish a JSON message along with custom headers using the Upstash QStash Python client. This allows for additional metadata or control over the message delivery.

```python
# This is a placeholder for the actual Python code snippet.
# The provided text only contains the title and description for this example.
```

--------------------------------

### Publish Message to QStash (Bash)

Source: https://upstash.com/docs/qstash/quickstarts/fly-io/go

Publishes a JSON message to QStash using `curl`. The destination URL is your Fly.io application's public URL. Requires a QStash token for authorization and specifies the content type as JSON.

```bash
curl --request POST "https://qstash.upstash.io/v2/publish/https://winter-cherry-9545.fly.dev" \
     -H "Authorization: Bearer <QSTASH_TOKEN>" \
     -H "Content-Type: application/json" \
     -d "{ \"hello\": \"world\"}"
```

--------------------------------

### Publish JSON Message using cURL and TypeScript SDK

Source: https://upstash.com/docs/qstash/overall/llms-txt

Examples for publishing a JSON message to Upstash QStash using cURL and the TypeScript SDK. Includes setting authorization, retry headers, and the message body.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Upstash-Retries: 3" \
    -H "Upstash-Retry-Delay: pow(2, retried) * 1000" \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  retries: 3,
  retryDelay: "pow(2, retried) * 1000", // 2^retried * 1000ms
});
```

--------------------------------

### GET /v2/messages/{messageId}

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details for a specific message using its ID. This functionality is available only while the message is being processed by QStash.

```APIDOC
## Get Message Details using QStash API

### Description
Retrieves details for a specific message using its ID. This functionality is available only while the message is being processed by QStash. Requires authentication and the message ID as a path parameter. An example using cURL is provided.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/messages/{messageId}`

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The ID of the message to retrieve.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/messages/msg_123 \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Response
#### Success Response (200)
- **iss** (string) - Issuer of the JWT.
- **sub** (string) - Subject of the JWT (e.g., the endpoint URL).
- **exp** (integer) - Expiration time of the JWT.
- **nbf** (integer) - Not before time of the JWT.
- **iat** (integer) - Issued at time of the JWT.
- **jti** (string) - JWT ID.
- **body** (string) - Base64 encoded hash of the request body.

#### Response Example
```json
{
  "iss": "Upstash",
  "sub": "https://qstash-remote.requestcatcher.com/test",
  "exp": 1656580612,
  "nbf": 1656580312,
  "iat": 1656580312,
  "jti": "jwt_67kxXD6UBAk7DqU6hzuHMDdXFXfP",
  "body": "qK78N0k3pNKI8zN62Fq2Gm-_LtWkJk1z9ykio3zZvY4="
}
```
```

--------------------------------

### Get a Message

Source: https://upstash.com/docs/qstash/api-refence/messages/get-a-message

Retrieve details of a specific message. Note that messages are removed shortly after delivery, so this endpoint is primarily for messages in the process of being delivered or retried.

```APIDOC
## GET /v2/messages/{messageId}

### Description
Retrieve details of a specific message using its unique ID. This endpoint is intended for accessing messages that are currently being delivered or are in a retry state, as messages are typically removed from the database shortly after successful delivery.

### Method
GET

### Endpoint
/v2/messages/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The unique identifier of the message to retrieve.

### Request Example
```json
{
  "example": "No request body needed for GET request."
}
```

### Response
#### Success Response (200)
- **messageId** (string) - The unique identifier of the message.
- **provider** (string) - The message provider.
- **to** (string) - The recipient of the message.
- **from** (string) - The sender of the message.
- **body** (string) - The content of the message.
- **headers** (object) - Additional headers associated with the message.
- **status** (string) - The current status of the message (e.g., 'pending', 'delivered', 'failed').
- **createdAt** (string) - The timestamp when the message was created.
- **nextAttemptAt** (string) - The timestamp for the next delivery attempt, if applicable.

#### Response Example
```json
{
  "messageId": "msg_abc123",
  "provider": "smtp",
  "to": "recipient@example.com",
  "from": "sender@example.com",
  "body": "Hello, this is a test message.",
  "headers": {
    "Content-Type": "text/plain"
  },
  "status": "pending",
  "createdAt": "2023-10-27T10:00:00Z",
  "nextAttemptAt": "2023-10-27T10:05:00Z"
}
```
```

--------------------------------

### QStash API Authentication with Bearer Token

Source: https://upstash.com/docs/qstash/api/messages

This section details how to authenticate API requests using the Bearer Token method by including your QSTASH_TOKEN in the Authorization header.

```APIDOC
## QStash API Authentication with Bearer Token

### Description
Authenticate your requests to the QStash API by including your `QSTASH_TOKEN` in the `Authorization` header as a Bearer Token. This is the recommended method for authentication.

### Method
All HTTP methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*`

### Parameters
#### Request Headers
- **Authorization** (string) - Required - The authentication token in the format `Bearer <QSTASH_TOKEN>`.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/... \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Response
#### Success Response (200)
- **status** (string) - Indicates the success of the operation.

#### Response Example
```json
{
  "message": "Request processed successfully"
}
```
```

--------------------------------

### Publishing with Helicone Analytics (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to publish a JSON message with Helicone analytics enabled for LLM usage monitoring. This requires a QStash client and custom provider setup, passing the Helicone API key via environment variables.

```APIDOC
## POST /publishJSON (with Helicone Analytics)

### Description
Publish a JSON message with Helicone analytics enabled for LLM usage monitoring. This requires a QStash client and custom provider setup, passing the Helicone API key via environment variables.

### Method
POST

### Endpoint
(Client-side abstraction, maps to `/publish`)

### Parameters
#### Request Body
- **api** (object) - Optional - Configuration for API integration.
  - **name** (string) - Required - The name of the API integration (e.g., `llm`).
  - **provider** (object) - Required - Custom provider configuration.
    - **token** (string) - Required - The provider's API token.
    - **baseUrl** (string) - Required - The base URL of the provider.
  - **analytics** (object) - Optional - Analytics configuration.
    - **name** (string) - Required - The name of the analytics service (e.g., `helicone`).
    - **token** (string) - Required - The analytics service token (e.g., `process.env.HELICONE_API_KEY`).
- **body** (object) - Required - The JSON payload of the message.
- **callback** (string) - Optional - The URL to send completion notifications to.

### Request Example
```typescript
import { Client, custom } from "@upstash/qstash";

const client = new Client({
  token: "<QSTASH_TOKEN>",
});

await client.publishJSON({
  api: {
    name: "llm",
    provider: custom({
      token: "XXX",
      baseUrl: "https://api.together.xyz",
    }),
    analytics: { name: "helicone", token: process.env.HELICONE_API_KEY! },
  },
  body: {
    model: "meta-llama/Llama-3-8b-chat-hf",
    messages: [
      {
        role: "user",
        content: "hello",
      },
    ],
  },
  callback: "https://oz.requestcatcher.com/",
});
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.
```

--------------------------------

### QStash API Authentication - Bearer Token

Source: https://upstash.com/docs/qstash/api/queues/upsert

This section describes how to authenticate QStash API requests using a Bearer Token in the Authorization header.

```APIDOC
## QStash API Authentication - Bearer Token

### Description
Authenticate QStash API requests by including your `QSTASH_TOKEN` in the `Authorization` header as a Bearer token.

### Method
N/A (Applies to all methods)

### Endpoint
N/A (Applies to all endpoints)

### Parameters
#### Request Headers
- **Authorization** (string) - Required - The authentication token in the format `Bearer <QSTASH_TOKEN>`.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/\n  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Response
No specific response for authentication, but subsequent requests will be authorized.
```

--------------------------------

### Get QStash Message Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve logs for published messages, with optional filtering capabilities. Allows monitoring message delivery and processing.

```APIDOC
## Get QStash Message Logs

### Description
Retrieve logs for published messages, with optional filtering capabilities. This allows monitoring message delivery and processing.

### Method
GET

### Endpoint
`https://qstash.upstash.io/v2/logs`

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
None

### Request Example (cURL)
```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

### Request Example (TypeScript)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.event.list()
# Async version is also available
```

### Response
#### Success Response (200)
- **logs** (array) - A list of message logs.
  - **messageId** (string) - The ID of the message.
  - **status** (string) - The status of the message (e.g., 'delivered', 'failed').
  - **timestamp** (string) - The timestamp of the log entry.

#### Response Example
```json
{
  "logs": [
    {
      "messageId": "msg_abc123",
      "status": "delivered",
      "timestamp": "2023-10-27T10:00:00Z"
    }
  ]
}
```
```

--------------------------------

### Publish JSON to URL Group with Delay, Headers, and Body (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message to a URL group with a 3-second delay, custom headers, and a request body. URL groups can be created in the QStash console or via the API. When publishing to a group, the response is an array of message IDs, one for each URL in the group.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
res = client.message.publish_json(
    url_group="my-url-group",
    body={
        "hello": "world",
    },
    headers={
        "test-header": "test-value",
    },
    delay="3s",
)

# When publishing to a URL group, the response is an array of messages for each URL in the group
print(res[0].message_id)
```

--------------------------------

### QStash API Authentication

Source: https://upstash.com/docs/qstash/api/messages/get

This section details the two primary methods for authenticating with the QStash API: using a Bearer Token in the Authorization header or as a query parameter.

```APIDOC
## QStash API Authentication

### Description

To access any endpoints in the QStash API, you must authenticate your requests. This guide explains the two methods for authentication: using a Bearer Token in the `Authorization` header or as a `qstash_token` query parameter.

### Method 1: Bearer Token

This is the recommended method for authentication. You will need your `QSTASH_TOKEN`, which can be found in the QStash console. Add this token to the `Authorization` header of your request.

### Endpoint

`https://qstash.upstash.io/v2/publish/...`

### Parameters

#### Request Headers

- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

### Request Example (cURL)

```bash
curl https://qstash.upstash.io/v2/publish/ப்புகளை \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Method 2: Query Parameter

If setting the `Authorization` header is not possible in your environment, you can use the `qstash_token` query parameter instead.

### Endpoint

`https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>`

### Parameters

#### Query Parameters

- **qstash_token** (string) - Required - Your QStash token.

### Request Example (cURL)

```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Security Recommendation

Always keep your token safe and reset it if you suspect it has been compromised.
```

--------------------------------

### Publish with Content-Based Deduplication

Source: https://upstash.com/docs/qstash/overall/llms-txt

This example shows how to enable content-based deduplication for published messages. When enabled, QStash will prevent duplicate messages with the same body content from being processed within a certain timeframe.

```APIDOC
## Publish Message with Content-Based Deduplication

### Description
Publishes a message with content-based deduplication enabled. QStash will prevent duplicate messages with the same body content from being processed within a certain timeframe.

### Method
POST

### Endpoint
`/v2/publish`

### Parameters
#### Request Body
- **url** (string) - Required - The URL to send the message to.
- **body** (object) - Required - The message body.
- **contentBasedDeduplication** (boolean) - Optional - Enables content-based deduplication. Defaults to false.

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  contentBasedDeduplication: true,
});
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.
```

--------------------------------

### Get Message Logs (QStash API)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves logs for all published messages using the QStash API. Requires an Authorization header with a Bearer token.

```shell
curl https://qstash.upstash.io/v2/logs \
    -H "Authorization: Bearer XXX"
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
const logs = await client.logs()
```

--------------------------------

### Publish Messages in Batch

Source: https://upstash.com/docs/qstash/overall/llms-txt

Publish multiple messages in a single request using QStash's batch functionality. This example shows how to send a batch of messages via cURL, TypeScript SDK, or Python SDK.

```APIDOC
## POST /v2/batch

### Description
Publish multiple messages in a single request using QStash's batch functionality.

### Method
POST

### Endpoint
`https://qstash.upstash.io/v2/batch`

### Parameters
#### Path Parameters
None

#### Query Parameters
None

#### Request Body
- **body** (array) - Required - An array of message objects to be published in batch.
  - Each object in the array should contain at least a `destination` (string) field.

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication (e.g., `Bearer XXX`).
- **Content-type** (string) - Required - Should be set to `application/json`.

### Request Example
```json
[
  {
    "destination": "https://example.com/destination1"
  },
  {
    "destination": "https://example.com/destination2"
  }
]
```

### Response
#### Success Response (200)
(Response details not provided in the source text, but typically includes confirmation of batch processing.)

#### Response Example
(Not provided in the source text)
```

--------------------------------

### Create QStash Schedule with Callbacks (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Shows how to create a QStash schedule with a specified cron interval, destination, and optional callback URLs for success and failure notifications using the Python client.

```APIDOC
## Create QStash Schedule with Callbacks (Python)

### Description
Creates a QStash schedule with specified cron interval, destination, and optional callback URLs for success and failure notifications. This allows for asynchronous handling of schedule execution outcomes.

### Code Example
```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.schedule.create(
    destination="https://my-api...",
    cron="0 * * * *",
    callback="https://my-callback...",
    failure_callback="https://my-failure-callback...",
)
```
```

--------------------------------

### Publish JSON with Configured Number of Retries

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a URL and configures the number of retries. The maximum retries depend on the QStash plan. The delay between retries defaults to exponential backoff but can be customized. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  retries: 1,
});
```

--------------------------------

### QStash API Authentication

Source: https://upstash.com/docs/qstash/api/dlq/listMessages

This section details the two primary methods for authenticating with the QStash API: using an Authorization header with a Bearer Token or including the token as a query parameter.

```APIDOC
## QStash API Authentication

### Description
Authenticate your requests to the QStash API using your `QSTASH_TOKEN`.

### Method
Authentication can be done via:
1. **Authorization Header**: Using `Authorization: Bearer <QSTASH_TOKEN>`
2. **Query Parameter**: Using `?qstash_token=<QSTASH_TOKEN>`

### Endpoint
All QStash API endpoints.

### Parameters
#### Header Parameter
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

#### Query Parameter
- **qstash_token** (string) - Required - Your QStash token.

### Request Example (Header)
```bash
curl https://qstash.upstash.io/v2/publish/...
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Request Example (Query Parameter)
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Response
Authentication is required for all QStash API endpoints. Successful authentication will allow access to the requested resource. Error responses will indicate authentication failures.

#### Success Response (200)
- **status** (string) - Indicates success.
- **message** (string) - A confirmation message.

#### Response Example
```json
{
  "status": "success",
  "message": "Request authenticated successfully."
}
```

#### Error Response (401)
- **error** (string) - Indicates an authentication error.
- **message** (string) - Details about the authentication failure.

#### Error Response Example
```json
{
  "error": "Unauthorized",
  "message": "Invalid or missing authentication token."
}
```
```

--------------------------------

### Publish JSON with Timeout (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message to a URL with a specified timeout value. This timeout applies to the request made by QStash to the target URL. The value is a string representing a duration, e.g., '30s'.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    timeout="30s",
)
```

--------------------------------

### Expose Local Server with localtunnel.me

Source: https://upstash.com/docs/qstash/howto/local-tunnel

Use localtunnel.me to create a public URL for your local development server. Replace '3000' with your application's port. This public URL can then be used as your QStash URL. If needed, set the 'Upstash-Forward-bypass-tunnel-reminder' header to bypass reminder messages.

```bash
npx localtunnel --port 3000
```

--------------------------------

### QStash Success Response Example

Source: https://upstash.com/docs/qstash/overall/llms-txt

A JSON object representing a successful response from a QStash batch operation. It contains a single field, `batchId`, which is a string identifier for the completed batch.

```json
{
  "batchId": "batch_ghi789"
}
```

--------------------------------

### QStash Schedule Error Response Example (JSON)

Source: https://upstash.com/docs/qstash/overall/llms-txt

This JSON object represents an error response, typically when a requested schedule is not found. It contains a single 'error' field with a descriptive message.

```json
{
  "error": "Schedule not found"
}
```

--------------------------------

### QStash API Authentication - Bearer Token

Source: https://upstash.com/docs/qstash/api/schedules/create

Authenticate QStash API requests by including your QSTASH_TOKEN in the Authorization header as a Bearer Token.

```APIDOC
## QStash API Authentication - Bearer Token

### Description
This method shows how to authenticate API requests by providing your `QSTASH_TOKEN` in the `Authorization` header.

### Method
All HTTP Methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*`

### Parameters
#### Request Headers
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/some-topic \
  -H "Authorization: Bearer <YOUR_QSTASH_TOKEN>"
```

### Response
#### Success Response (200)
Responses vary based on the specific endpoint called.

#### Response Example
(Example depends on the specific endpoint)
```

--------------------------------

### Get all messages with pagination using cursor

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves all messages from the Dead Letter Queue (DLQ) with pagination support using a cursor. This is useful for handling large DLQs.

```APIDOC
## GET /v2/dlq

### Description
Retrieves all messages from the Dead Letter Queue (DLQ) with pagination support using a cursor. This is useful for handling large DLQs.

### Method
GET

### Endpoint
/v2/dlq

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - The cursor to use for pagination. If not provided, the first page of results is returned.

### Request Example
```python
from qstash import QStash

client = QStash ("<QSTASH-TOKEN>")

all_messages = []
cursor = None
while True:
    res = client.dlq.list(cursor=cursor)
    all_messages.extend(res.messages)
    cursor = res.cursor
    if cursor is None:
        break
```

### Response
#### Success Response (200)
- **messages** (array) - A list of messages in the DLQ.
- **cursor** (string) - The cursor for the next page of results. Will be null if there are no more pages.
```

--------------------------------

### Get QStash Schedule by ID

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details of a specific schedule using its unique identifier. This is useful for inspecting the configuration or status of an existing schedule.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const res = await client.schedules.get("scheduleId");
console.log(res.cron);
```

```python
from qstash import Qstash

client = Qstash("<QSTASH-TOKEN>")
schedule = client.schedule.get("<schedule-id>")

print(schedule.cron)
```

--------------------------------

### QStash URL Group Webhook Configuration

Source: https://upstash.com/docs/qstash/howto/webhook

This example demonstrates configuring a QStash URL Group to manage webhook requests. URL Groups allow server-side templates for publishing, enabling default headers and defining multiple endpoints for fan-out. The provided cURL command shows how to set forwarding and retry headers for a URL Group.

```cURL
curl -X PATCH https://qstash.upstash.io/v2/topics/<URL_GROUP_NAME> \
    -H "Authorization: Bearer <QSTASH_TOKEN>" \
    -d '{
        "headers": {
            "Upstash-Header-Forward": ["true"],
            "Upstash-Retries": "3"
        }
    }'
```

--------------------------------

### Set Callback URLs for QStash Message Responses

Source: https://upstash.com/docs/qstash/overall/apiexamples

Configure success and failure callback URLs to receive responses from message endpoints. If an endpoint doesn't respond, QStash sends the response to the failure callback URL.

```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Content-type: application/json" \
    -H "Upstash-Callback: https://example.com/callback" \
    -H "Upstash-Failure-Callback: https://example.com/failure" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  callback: "https://example.com/callback",
  failureCallback: "https://example.com/failure",
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    callback="https://example.com/callback",
    failure_callback="https://example.com/failure",
)
# Async version is also available
```

--------------------------------

### List QStash Schedules (cURL, TypeScript, Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieve a list of all schedules that have been created within the QStash service. This is useful for managing scheduled messages. Examples are provided for cURL, TypeScript SDK, and Python SDK.

```shell
curl https://qstash.upstash.io/v2/schedules \
    -H "Authorization: Bearer XXX"
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const scheds = await client.schedules.list();
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.schedule.list()
# Async version is also available
```

--------------------------------

### GET /v2/dlq/{messageId}

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves a specific message from the Dead Letter Queue (DLQ) by its ID. This is useful for inspecting failed messages.

```APIDOC
## GET /v2/dlq/{messageId}

### Description
Retrieves a specific message from the Dead Letter Queue (DLQ) by its ID.

### Method
GET

### Endpoint
/v2/dlq/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The ID of the message to retrieve.

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
msg = client.dlq.get("<dlq-id>")
```

### Response
#### Success Response (200)
- **message** (object) - The message object details.
```

--------------------------------

### POST /workflow - Create Workflow with Steps

Source: https://upstash.com/docs/qstash/overall/llms-txt

Create and execute a workflow with defined steps using the Upstash Workflow SDK for Python.

```APIDOC
## POST /workflow

### Description
Create and execute a workflow with defined steps using the Upstash Workflow SDK for Python.

### Method
POST

### Endpoint
`/workflow`

### Parameters
#### Request Body
- **userId** (string) - Required - The ID of the user for the workflow.
- **email** (string) - Required - The email address for the user.
- **name** (string) - Required - The name of the user.

### Request Example
```json
{
  "userId": "user123",
  "email": "user@example.com",
  "name": "John Doe"
}
```

### Response
#### Success Response (200)
- **workflowId** (string) - The ID of the executed workflow.
- **status** (string) - The status of the workflow execution.
```

--------------------------------

### Configure QStash Retry Delay

Source: https://upstash.com/docs/qstash/overall/llms-txt

Explains how to customize the delay between message delivery retries using mathematical expressions, supporting strategies like exponential backoff. Examples provided for cURL, TypeScript, and Python.

```APIDOC
## Configure QStash Retry Delay

### Description
Customize the delay between message delivery retries using mathematical expressions with QStash. This supports advanced strategies like exponential backoff. The examples show how to set the number of retries and the retry delay expression.

### Method
POST

### Endpoint
`/v2/publish/{url}`

### Parameters
#### Path Parameters
- **url** (string) - Required - The URL to which the message will be published.

#### Query Parameters
None

#### Headers
- **Authorization** (string) - Required - Bearer token for authentication.
- **Upstash-Retries** (integer) - Optional - The number of times to retry the message delivery. Defaults to exponential backoff strategy if not specified.
- **Upstash-Retry-Delay** (string) - Optional - A mathematical expression defining the delay between retries in milliseconds. Example: `pow(2, retried) * 1000` for exponential backoff.
- **Content-type** (string) - Required - Specifies the content type of the request body, e.g., `application/json`.

#### Request Body
- **(any)** - Required - The message payload to be sent.

### Request Example (cURL)
```shell
curl -XPOST \
    -H 'Authorization: Bearer XXX' \
    -H "Upstash-Retries: 3" \
    -H "Upstash-Retry-Delay: pow(2, retried) * 1000" \
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

### Request Example (TypeScript)
```typescript
const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  retries: 3,
  retryDelay: "pow(2, retried) * 1000", // 2^retried * 1000ms
});
```

### Request Example (Python)
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    retries=3,
    retry_delay="pow(2, retried) * 1000",  # 2^retried * 1000ms
)
# Async version is also available
```

### Response
#### Success Response (200)
- **messageId** (string) - The ID of the published message.
```

--------------------------------

### Get a schedule by ID in TypeScript

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details of a specific schedule using its unique identifier. This is useful for inspecting the configuration or status of an existing schedule.

```APIDOC
## Get Schedule by ID

### Description
Retrieves details of a specific schedule using its unique identifier. This is useful for inspecting the configuration or status of an existing schedule.

### Method
GET

### Endpoint
`/v2/schedules/{scheduleId}`

### Parameters
#### Path Parameters
- **scheduleId** (string) - Required - The unique identifier of the schedule.

### Request Example
```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });

const res = await client.schedules.get("scheduleId");
console.log(res.cron);
```

### Response
#### Success Response (200)
- **cron** (string) - The cron expression for the schedule.
- **destination** (string) - The URL where the message will be sent.
- **id** (string) - The unique identifier of the schedule.
- **createdAt** (string) - The timestamp when the schedule was created.
- **updatedAt** (string) - The timestamp when the schedule was last updated.
```

--------------------------------

### QStash URL Group Publish Request

Source: https://upstash.com/docs/qstash/howto/webhook

This example shows how to publish a message to a QStash URL Group, which then forwards it to the configured endpoints. This method is useful for fanning out a single webhook call to multiple destinations.

```URL
https://qstash.upstash.io/v2/publish/<URL_GROUP_NAME>?qstash_token=<QSTASH_TOKEN>
```

--------------------------------

### Handle QStash Callbacks with Signature Verification in Next.js

Source: https://upstash.com/docs/qstash/overall/llms-txt

This Next.js API route example demonstrates how to handle incoming callbacks from Upstash QStash, including decoding the base64-encoded message body and verifying the request's authenticity using `verifySignature`. It requires the `@upstash/qstash/nextjs` package.

```javascript
// pages/api/callback.js

import { verifySignature } from "@upstash/qstash/nextjs";

function handler(req, res) {
  // responses from qstash are base64-encoded
  const decoded = atob(req.body.body);
  console.log(decoded);

  return res.status(200).end();
}

export default verifySignature(handler);

export const config = {
  api: {
    bodyParser: false,
  },
};
```

--------------------------------

### Events API - Get all events with pagination

Source: https://upstash.com/docs/qstash/overall/llms-txt

Fetches a paginated list of events from QStash using a cursor for managing large result sets. The loop continues until all events are retrieved.

```APIDOC
## GET /v1/events

### Description
Fetches a paginated list of events. Use the `cursor` parameter to paginate through results.

### Method
GET

### Endpoint
/v1/events

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - The cursor to retrieve the next page of events.

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")

all_events = []
cursor = None
while True:
    res = client.event.list(cursor=cursor)
    all_events.extend(res.events)
    cursor = res.cursor
    if cursor is None:
        break
```

### Response
#### Success Response (200)
- **events** (array) - A list of event objects.
- **cursor** (string) - The cursor for the next page of results. Null if this is the last page.

#### Response Example
```json
{
  "events": [
    {
      "messageId": "msg_abc123",
      "deduplicationId": "dedup_xyz789",
      "providerSenderId": "snd_123",
      "topic": "my-topic",
      "insertedAt": 1678886400,
      "attempts": 1,
      "nextAttemptAt": 1678886400,
      "url": "https://example.com/webhook",
      "body": {
        "key": "value"
      },
      "headers": {
        "Content-Type": "application/json"
      },
      "tags": ["tag1", "tag2"]
    }
  ],
  "cursor": "next_cursor_value"
}
```
```

--------------------------------

### Retrieve Signing Keys with Python

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to retrieve your current and next signing keys using the `qstash` Python library. Requires your QStash API token for authentication.

```APIDOC
## GET /signing-keys

### Description
Retrieves the current and next signing keys for QStash authentication.

### Method
GET

### Endpoint
/signing-keys

### Parameters
#### Query Parameters
None

#### Request Body
None

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
signing_key = client.signing_key.get()

print(signing_key.current, signing_key.next)
```

### Response
#### Success Response (200)
- **current** (string) - The current signing key.
- **next** (string) - The next upcoming signing key.

#### Response Example
```json
{
  "current": "<current-signing-key>",
  "next": "<next-signing-key>"
}
```
```

--------------------------------

### Get Queue Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Fetches details for a specified queue by its name. This includes information like creation date, last update, parallelism settings, pause status, and message lag.

```APIDOC
## GET /v2/queues/{queueName}

### Description
Get details of a specific queue.

### Method
GET

### Endpoint
/v2/queues/{queueName}

### Parameters
#### Path Parameters
- **queueName** (string) - Required - The name of the queue to retrieve.

### Request Example
```json
{
  "example": "No request body for GET request."
}
```

### Response
#### Success Response (200)
- **name** (string) - The name of the queue.
- **createdAt** (integer) - The creation timestamp of the queue in Unix milliseconds.
- **updatedAt** (integer) - The last update timestamp of the queue in Unix milliseconds.
- **parallelism** (integer) - The number of parallel consumers consuming from the queue.
- **paused** (boolean) - Whether the queue is paused.
- **lag** (integer) - The number of unprocessed messages that exist in the queue.

#### Response Example
```json
{
  "name": "my-queue",
  "createdAt": 1678886400000,
  "updatedAt": 1678886400000,
  "parallelism": 10,
  "paused": false,
  "lag": 0
}
```

#### Error Response (400)
- **error** (string) - Queue name is invalid. Queue names can only contain alphanumeric characters, hyphens, periods, and underscores.

#### Error Response (404)
- **error** (string) - Queue not found
```

--------------------------------

### QStash Batch Request JSON Payload

Source: https://upstash.com/docs/qstash/overall/llms-txt

An example JSON payload for making a batch request to QStash. This payload consists of an array of objects, where each object specifies a destination URL.

```json
[
  {
    "destination": "https://example.com/destination1"
  },
  {
    "destination": "https://example.com/destination2"
  }
]
```

--------------------------------

### QStash API Authentication - Bearer Token

Source: https://upstash.com/docs/qstash/api/flow-control/list

This section details how to authenticate your API requests using a Bearer Token in the Authorization header. This is the recommended method for securing your requests.

```APIDOC
## QStash API Authentication - Bearer Token

### Description
Authenticate your API requests by including your `QSTASH_TOKEN` in the `Authorization` header as a Bearer Token. This is the standard and recommended method for authenticating with the QStash API.

### Method
All HTTP Methods (GET, POST, PUT, DELETE, etc.)

### Endpoint
`https://qstash.upstash.io/v2/*`

### Parameters
#### Headers
- **Authorization** (string) - Required - The authentication token in the format `Bearer <QSTASH_TOKEN>`.

### Request Example
```bash
curl https://qstash.upstash.io/v2/publish/ \ 
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Response
#### Success Response (200)
Responses will vary based on the specific endpoint called.

#### Response Example
(Example varies by endpoint)
```

--------------------------------

### QStash Python SDK Synchronous Client Usage

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to initialize and use the synchronous QStash client in Python. This client is suitable for straightforward API calls where immediate responses are expected.

```APIDOC
## QStash Python SDK Synchronous Client Usage

### Description
Demonstrates how to initialize and use the synchronous QStash client in Python. This client is suitable for straightforward API calls where immediate responses are expected.

### Method
Python Code

### Endpoint
N/A

### Parameters
- **QSTASH_TOKEN** (string) - Required - Your QStash API token.

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(...)
```

### Response
N/A
```

--------------------------------

### QStash API Authentication

Source: https://upstash.com/docs/qstash/api/publish

This section details the two primary methods for authenticating requests to the QStash API: using a Bearer Token in the Authorization header or as a query parameter.

```APIDOC
## QStash API Authentication

### Description

To access any endpoints in the QStash API, you must authenticate your requests using your `QSTASH_TOKEN`. This token can be found in the QStash console. There are two recommended methods for including your token in API requests.

### Method 1: Bearer Token in Header

This is the recommended method for authentication. Include your `QSTASH_TOKEN` in the `Authorization` header as a Bearer token.

### Endpoint

`https://qstash.upstash.io/v2/publish/...` (Example endpoint, replace with actual endpoint)

### Parameters

#### Request Headers

- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

### Request Example

```bash
curl https://qstash.upstash.io/v2/publish/வுகளை\n  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### Method 2: Query Parameter

If setting the `Authorization` header is not possible in your environment, you can use the `qstash_token` query parameter.

### Endpoint

`https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>` (Example endpoint, replace with actual endpoint)

### Parameters

#### Query Parameters

- **qstash_token** (string) - Required - Your QStash token.

### Request Example

```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Security Recommendation

Always keep your token safe. If you suspect your token has been compromised, reset it immediately in the QStash console.
```

--------------------------------

### QStash API Authentication

Source: https://upstash.com/docs/qstash/api/enqueue

This section details the two primary methods for authenticating requests to the QStash API: using a Bearer Token in the Authorization header or as a query parameter.

```APIDOC
## QStash API Authentication

### Description
This guide explains how to authenticate your requests to the QStash API. You will need your `QSTASH_TOKEN` to access the endpoints.

### Authentication Methods

There are two main ways to authenticate:

1.  **Bearer Token in Header**
2.  **Query Parameter**

### 1. Bearer Token Authentication

This is the recommended method for authentication. You include your `QSTASH_TOKEN` in the `Authorization` header as a Bearer token.

#### Method
`POST` (or other HTTP methods depending on the endpoint)

#### Endpoint
`https://qstash.upstash.io/v2/publish/...` (example endpoint)

#### Parameters

##### Headers
- **Authorization** (string) - Required - `Bearer <QSTASH_TOKEN>`

#### Request Example (cURL)
```bash
curl https://qstash.upstash.io/v2/publish/...
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

### 2. Query Parameter Authentication

This method can be used in environments where setting request headers is not possible.

#### Method
`POST` (or other HTTP methods depending on the endpoint)

#### Endpoint
`https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>` (example endpoint)

#### Parameters

##### Query Parameters
- **qstash_token** (string) - Required - Your QStash token.

#### Request Example (cURL)
```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

### Security Recommendation

Always keep your token safe and reset it if you suspect it has been compromised.
```

--------------------------------

### GET /v2/logs - List Logs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves a paginated list of logs for published messages. Supports filtering by various parameters like message ID, state, URL, and time range.

```APIDOC
## GET /v2/logs

### Description
Paginate through logs of published messages. Supports filtering by various parameters.

### Method
GET

### Endpoint
/v2/logs

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - By providing a cursor you can paginate through all of the logs
- **messageId** (string) - Optional - Filter logs by message ID
- **state** (string) - Optional - Filter logs by message state. Possible values: CREATED, ACTIVE, RETRY, ERROR, IN_PROGRESS, DELIVERED, FAILED, CANCEL_REQUESTED, CANCELLED.
- **url** (string) - Optional - Filter logs by destination URL
- **topicName** (string) - Optional - Filter logs by URL Group name
- **scheduleId** (string) - Optional - Filter logs by schedule ID
- **queueName** (string) - Optional - Filter logs by queue name
- **fromDate** (integer) - Optional - Filter logs by starting date, in milliseconds (Unix timestamp). This is inclusive.
- **toDate** (integer) - Optional - Filter logs by ending date, in milliseconds (Unix timestamp). This is inclusive.
- **count** (integer) - Optional - The number of log entries to return. Defaults to 100. Maximum is 100.
- **order** (string) - Optional - The sorting order of logs by timestamp. Possible values: latestFirst, earliestFirst. Defaults to latestFirst.
- **label** (string) - Optional - Filter logs by the label of the message assigned by the user

### Response
#### Success Response (200)
- **cursor** (string) - A cursor which you can use in subsequent requests to paginate through all logs. If no cursor is returned, you have reached the end of the logs.
- **logs** (array) - An array of LogEntry objects.

##### LogEntry Object
- **time** (integer) - The timestamp of the log entry in Unix milliseconds
- **messageId** (string) - The ID of the message

#### Response Example
```json
{
  "cursor": "some_cursor_string",
  "logs": [
    {
      "time": 1678886400000,
      "messageId": "msg_123"
    }
  ]
}
```
```

--------------------------------

### Publish Message using cURL

Source: https://upstash.com/docs/qstash/overall/getstarted

This snippet demonstrates how to publish a JSON message to a specified endpoint using cURL. It includes setting the authorization token, content type, and the message payload. The example targets a generic Upstash endpoint and a RequestCatcher URL for testing.

```bash
curl -XPOST \
    -H 'Authorization: Bearer <QSTASH_TOKEN>'
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://<your-api-url>'
```

```bash
curl -XPOST \
    -H 'Authorization: Bearer <QSTASH_TOKEN>'
    -H "Content-type: application/json" \
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://firstqstashmessage.requestcatcher.com/test'
```

--------------------------------

### Trigger Upstash Workflow API Request Example (cURL)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Triggers an Upstash Workflow execution via a POST request to the QStash API. Requires the workflow URL, authentication token, and content type. Optional headers include Run ID and retry count for managing workflow executions.

```bash
curl -XPOST https://qstash.upstash.io/v2/publish/https://my-app.example.com/api/workflow \
  -H "Authorization: Bearer <QSTASH_TOKEN>" \
  -H "Content-Type: application/json" \
  -H "Upstash-Workflow-RunId: onboarding-user-123" \
  -H "Upstash-Retries: 3" \
  -d '{
    "userId": "user_123",
    "email": "user@example.com",
    "name": "John Doe"
  }'
```

--------------------------------

### Get QStash Queue Configuration (TypeScript)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves the current configuration, including parallelism settings, for a specified QStash queue using the Upstash QStash client library for TypeScript. Requires a QStash token and the queue name.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const queue = client.queue({
  queueName: "my-queue"
});
const res = await queue.get();
```

--------------------------------

### Publish JSON with Content-Based Deduplication

Source: https://upstash.com/docs/qstash/sdks/ts/examples/publish

Publishes a JSON message to a URL with content-based deduplication enabled. This prevents duplicate messages if the same content is published within a certain timeframe. Requires the '@upstash/qstash' SDK and a QSTASH_TOKEN.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const res = await client.publishJSON({
  url: "https://my-api...",
  body: { hello: "world" },
  contentBasedDeduplication: true,
});
```

--------------------------------

### Get Message Details

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details for a specific message using its ID. This function is available via the QStash SDK for TypeScript and requires an initialized QStash client.

```APIDOC
## GET /messages/{messageId}

### Description
Retrieve details for a specific message using its ID.

### Method
GET

### Endpoint
/messages/{messageId}

### Parameters
#### Path Parameters
- **messageId** (string) - Required - The unique identifier of the message.

#### Query Parameters
- **qstash_token** (string) - Required - QStash authentication token passed as a query parameter.

### Response
#### Success Response (200)
- **messageId** (string) - The unique identifier of the message.
- **url** (string) - The URL the message was sent to.
- **createdAt** (integer) - Timestamp when the message was created.
- **body** (object) - The message payload.

#### Response Example
```json
{
  "messageId": "msg_123",
  "url": "https://example.com/webhook",
  "createdAt": 1678886400,
  "body": {
    "hello": "world"
  }
}
```
```

--------------------------------

### Enable Helicone Analytics for LLM API Calls (TypeScript)

Source: https://upstash.com/docs/qstash/integrations/llm

This TypeScript snippet shows how to integrate Helicone for observability with Upstash QStash LLM API calls. By providing the Helicone API key during model initialization, you can gain insights into your LLM usage. This example uses a custom model provider but also applies to OpenAI.

```typescript
import { Client, custom } from "@upstash/qstash";

const client = new Client({
  token: "<QSTASH_TOKEN>",
});

await client.publishJSON({
  api: {
    name: "llm",
    provider: custom({
      token: "XXX",
      baseUrl: "https://api.together.xyz",
    }),
    analytics: { name: "helicone", token: process.env.HELICONE_API_KEY! },
  },
  body: {
    model: "meta-llama/Llama-3-8b-chat-hf",
    messages: [
      {
        role: "user",
        content: "hello",
      },
    ],
  },
  callback: "https://oz.requestcatcher.com/",
});
```

--------------------------------

### Next.js Frontend: Start Background Job Button

Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs

This React component provides a button to trigger a background job. It uses the `useState` hook to manage loading and message states. The `startBackgroundJob` function from `./actions` is called upon button click to initiate the process. It handles UI feedback for loading and success/failure messages.

```tsx
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

--------------------------------

### React Component to Start Background Job

Source: https://upstash.com/docs/qstash/quickstarts/vercel-nextjs

A client-side React component that provides a button to trigger a background job. It uses the `useState` hook to manage loading and message states, and calls the `startBackgroundJob` function upon button click. The UI provides visual feedback for the loading state and displays the result of the job initiation.

```typescript
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

--------------------------------

### Configure Message Retries with Custom Backoff (Bash, TypeScript, Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates publishing a JSON message with custom retry configurations, including the maximum number of retries and a delay expression for exponential backoff. This example showcases the usage in Bash, TypeScript, and Python, requiring a QStash token and target URL.

```bash
curl -XPOST \
    -H 'Authorization: Bearer <QSTASH_TOKEN>'
    -H "Content-type: application/json"
    -H "Upstash-Retries: 3"
    -H "Upstash-Retry-Delay: pow(2, retried) * 1000"
    -d '{ "hello": "world" }' \
    'https://qstash.upstash.io/v2/publish/https://example.com'
```

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
await client.publishJSON({
  url: "https://example.com",
  body: {
    hello: "world",
  },
  retries: 3,
  retryDelay: "pow(2, retried) * 1000", // Exponential backoff: 1s, 2s, 4s, 8s
});
```

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://example.com",
    body={
        "hello": "world",
    },
    retries=3,
    retry_delay="pow(2, retried) * 1000",
)
```

--------------------------------

### Example Message Body and Headers for Upstash QStash

Source: https://upstash.com/docs/qstash/howto/publishing

Illustrates the structure of the message body and headers that Upstash QStash will deliver to the destination API when a message is published. This includes the forwarded headers and the content type.

```json
// body
{ "hello": "world" }

// headers
My-Header:	my-value
Content-Type:	application/json
```

--------------------------------

### QStash CLI 'dev' command help

Source: https://upstash.com/docs/qstash/howto/local-development

Displays the usage information for the 'dev' command in the QStash CLI. It outlines available flags such as '-port' for setting the HTTP server port and '-quota' for configuring user quota types.

```bash
#!/bin/bash
$ ./qstash dev --help
Usage of dev:
  -port int
        The port to start HTTP server at [env QSTASH_DEV_PORT] (default 8080)
  -quota string
        The quota of users [env QSTASH_DEV_QUOTA] (default "payg")
```

--------------------------------

### Get QStash Schedule by ID (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves details of a specific QStash schedule using its unique schedule ID. This function allows inspecting the configuration of an existing schedule.

```APIDOC
## Get Schedule by ID (Python)

### Description
Retrieves details of a specific QStash schedule using its unique schedule ID. This function allows inspecting the configuration of an existing schedule.

### Method
GET

### Endpoint
`/v2/schedules/{scheduleId}`

### Parameters
#### Path Parameters
- **scheduleId** (string) - Required - The unique identifier of the schedule.

### Request Example
```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
schedule = client.schedule.get("<schedule-id>")

print(schedule.cron)
```

### Response
#### Success Response (200)
- **cron** (string) - The cron expression for the schedule.
- **destination** (string) - The URL where the message will be sent.
- **id** (string) - The unique identifier of the schedule.
- **createdAt** (string) - The timestamp when the schedule was created.
- **updatedAt** (string) - The timestamp when the schedule was last updated.
```

--------------------------------

### Deno - Receive and Verify QStash Webhooks

Source: https://upstash.com/docs/qstash/overall/llms-txt

This TypeScript code snippet demonstrates how to set up an HTTP server in a Deno deploy project to receive webhooks from QStash. It utilizes the Upstash QStash SDK to verify the incoming request's signature using provided signing keys stored as environment variables.

```APIDOC
## Deno - Receive and Verify QStash Webhooks

### Description
This TypeScript code snippet demonstrates how to set up an HTTP server in a Deno deploy project to receive webhooks from QStash. It utilizes the Upstash QStash SDK to verify the incoming request's signature using provided signing keys stored as environment variables. The handler logs whether the signature is valid and returns an appropriate HTTP response. Dependencies include Deno's standard HTTP server and the Upstash QStash SDK.

### Method
POST

### Endpoint
`/` (Root endpoint for the Deno server)

### Parameters
#### Environment Variables
- **QSTASH_CURRENT_SIGNING_KEY** (string) - Required - The current signing key for webhook verification.
- **QSTASH_NEXT_SIGNING_KEY** (string) - Required - The next signing key for webhook verification.

#### Request Headers
- **Upstash-Signature** (string) - Required - The signature of the incoming webhook request.

### Request Example
```typescript
import { serve } from "https://deno.land/std@0.142.0/http/server.ts";
import { Receiver } from "https://deno.land/x/upstash_qstash@v0.1.4/mod.ts";

serve(async (req: Request) => {
  const r = new Receiver({
    currentSigningKey: Deno.env.get("QSTASH_CURRENT_SIGNING_KEY")!,
    nextSigningKey: Deno.env.get("QSTASH_NEXT_SIGNING_KEY")!,
  });

  const isValid = await r
    .verify({
      signature: req.headers.get("Upstash-Signature")!,
      body: await req.text(),
    })
    .catch((err: Error) => {
      console.error(err);
      return false;
    });

  if (!isValid) {
    return new Response("Invalid signature", { status: 401 });
  }

  console.log("The signature was valid");

  // do work

  return new Response("OK", { status: 200 });
});
```

### Response
#### Success Response (200)
- **Body** (string) - "OK" indicating successful verification and processing.

#### Error Response (401)
- **Body** (string) - "Invalid signature" if the webhook signature is not valid.

#### Response Example
```
OK
```
```

--------------------------------

### Retrieve All Logs with Pagination

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves all logs from QStash, implementing pagination using a cursor to handle large result sets efficiently. This GET request to the `/v2/logs` endpoint returns an array of log objects and a cursor for fetching the next page.

```json
{
  "logs": [
    {
      "messageId": "msg_abc123",
      "status": "DELIVERED",
      "tag": "email-campaign",
      "createdAt": 1678886400,
      "deduplicationId": "dedup_xyz789"
    }
  ],
  "cursor": "next_cursor_value"
}
```

--------------------------------

### Authenticate with Query Parameter using cURL

Source: https://upstash.com/docs/qstash/api/messages/get

This snippet shows how to authenticate QStash API requests by appending the qstash_token as a query parameter. This method is useful in environments where setting request headers is not feasible.

```bash
curl https://qstash.upstash.io/v2/publish/...?qstash_token=<QSTASH_TOKEN>
```

--------------------------------

### Get URL Group by Name

Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups

Retrieves the details of a specific URL group identified by its name. This includes the group's name and the list of endpoints associated with it.

```APIDOC
## GET /v2/urlgroup/{url_group}

### Description
Fetches a specific URL group by its name.

### Method
GET

### Endpoint
`/v2/urlgroup/{url_group}`

### Parameters
#### Path Parameters
- **url_group** (string) - Required - The name of the URL group to retrieve.

### Response
#### Success Response (200)
- **name** (string) - The name of the URL group.
- **endpoints** (array[object]) - A list of endpoint objects within the URL group.
  - **url** (string) - The URL of the endpoint.

#### Response Example
```json
{
  "name": "my-url-group",
  "endpoints": [
    {"url": "https://my-endpoint-1"},
    {"url": "https://my-endpoint-2"}
  ]
}
```
```

--------------------------------

### Authenticate with Bearer Token using cURL

Source: https://upstash.com/docs/qstash/api/messages/get

This snippet demonstrates how to include your QStash token in the Authorization header when making a cURL request to the QStash API. This is the recommended method for authentication.

```bash
curl https://qstash.upstash.io/v2/publish/\
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

--------------------------------

### Authenticate with Bearer Token using cURL

Source: https://upstash.com/docs/qstash/api/dlq/listMessages

This snippet demonstrates how to include your QStash token in the Authorization header for API requests using cURL. It's the recommended method for authentication.

```curl
curl https://qstash.upstash.io/v2/publish/... \
  -H "Authorization: Bearer <QSTASH_TOKEN>"
```

--------------------------------

### QStash Authentication

Source: https://upstash.com/docs/qstash/api-refence/dlq/bulk-retry-dlq-messages

Details on how to authenticate with the QStash API by passing an authentication token as a query parameter.

```APIDOC
## GET /some/endpoint

### Description
This endpoint requires authentication using a QStash token passed as a query parameter.

### Method
GET

### Endpoint
/some/endpoint

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - QStash authentication token.

### Request Example
```
GET /some/endpoint?qstash_token=YOUR_AUTH_TOKEN
```

### Response
#### Success Response (200)
- **message** (string) - A success message.

#### Response Example
```json
{
  "message": "Successfully authenticated and processed request."
}
```
```

--------------------------------

### Get URL Group by Name (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/url-groups

Retrieves a specific URL group by its name. Returns the group's name and its associated endpoints. Requires a QStash token.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
url_group = client.url_group.get("my-url-group")

print(url_group.name, url_group.endpoints)
```

--------------------------------

### GET /v2/logs

Source: https://upstash.com/docs/qstash/api-refence/logs/list-logs

Paginate through logs of published messages. This endpoint allows filtering logs by various criteria such as message ID, state, URL, topic name, schedule ID, queue name, and date range.

```APIDOC
## GET /v2/logs

### Description
Paginate through logs of published messages. This endpoint allows filtering logs by various criteria such as message ID, state, URL, topic name, schedule ID, queue name, and date range.

### Method
GET

### Endpoint
/v2/logs

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - By providing a cursor you can paginate through all of the logs
- **messageId** (string) - Optional - Filter logs by message ID
- **state** (string) - Optional - Filter logs by message state. Possible values: CREATED, ACTIVE, RETRY, ERROR, IN_PROGRESS, DELIVERED, CANCEL_REQUESTED, CANCELLED.
- **url** (string) - Optional - Filter logs by destination URL
- **topicName** (string) - Optional - Filter logs by URL Group name
- **scheduleId** (string) - Optional - Filter logs by schedule ID
- **queueName** (string) - Optional - Filter logs by queue name
- **fromDate** (integer) - Optional - Filter logs by starting date, in milliseconds (Unix timestamp). This is inclusive.
- **toDate** (integer) - Optional - Filter logs by ending date, in milliseconds (Unix timestamp). This is inclusive.
- **count** (integer) - Optional - The number of log entries to return. Defaults to 100. Maximum is 100.
- **order** (string) - Optional - The sorting order of logs by timestamp. Possible values: latestFirst, earliestFirst. Defaults to latestFirst.
- **label** (string) - Optional - Filter logs by the label of the message assigned by the user

### Response
#### Success Response (200)
- **cursor** (string) - A cursor which you can use in subsequent requests to paginate through all logs. If no cursor is returned, you have reached the end of the logs.
- **logs** (array) - An array of LogEntry objects.

#### Response Example
```json
{
  "cursor": "some_cursor_string",
  "logs": [
    {
      "time": 1678886400000,
      "messageId": "msg_123"
    }
  ]
}
```
```

--------------------------------

### Publish JSON with Content-Based Deduplication (Python)

Source: https://upstash.com/docs/qstash/sdks/py/examples/publish

Publishes a JSON message with content-based deduplication enabled. This feature prevents duplicate messages from being processed if they have the same content within a specified time window. It requires the `qstash` library and a QStash client.

```python
from qstash import QStash

client = QStash("<QSTASH-TOKEN>")
client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    content_based_deduplication=True,
)
```

--------------------------------

### Handle QStash Webhook and Verify Signature in Go

Source: https://upstash.com/docs/qstash/overall/llms-txt

This Go code sets up an HTTP server to listen for incoming webhooks from QStash. It retrieves the request body, signing keys, and signature from the headers. The `verify` function validates the request signature. Upon successful verification, it executes business logic.

```go
func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		defer r.Body.Close()

		currentSigningKey := os.Getenv("QSTASH_CURRENT_SIGNING_KEY")
		nextSigningKey := os.Getenv("QSTASH_NEXT_SIGNING_KEY")
		tokenString := r.Header.Get("Upstash-Signature")

		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		err = verify(body, tokenString, currentSigningKey)
		if err != nil {
			fmt.Printf("Unable to verify signature with current signing key: %v", err)
			err = verify(body, tokenString, nextSigningKey)
		}

		if err != nil {
			http.Error(w, err.Error(), http.StatusUnauthorized)
			return
		}

		// handle your business logic here

		w.WriteHeader(http.StatusOK)

	})

	fmt.Println("listening on", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		panic(err)
	}
}
```

--------------------------------

### List Logs (API Reference)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves a paginated list of logs for published messages via the GET /v2/logs API endpoint. Supports filtering by various parameters like message ID, state, URL, and time range.

```http
GET /v2/logs

### Description
Paginate through logs of published messages. Supports filtering by various parameters.

### Method
GET

### Endpoint
/v2/logs

### Parameters
#### Query Parameters
- **cursor** (string) - Optional - By providing a cursor you can paginate through all of the logs
- **messageId** (string) - Optional - Filter logs by message ID
- **state** (string) - Optional - Filter logs by message state. Possible values: CREATED, ACTIVE, RETRY, ERROR, IN_PROGRESS, DELIVERED, FAILED, CANCEL_REQUESTED, CANCELLED.
- **url** (string) - Optional - Filter logs by destination URL
- **topicName** (string) - Optional - Filter logs by URL Group name
- **scheduleId** (string) - Optional - Filter logs by schedule ID
- **queueName** (string) - Optional - Filter logs by queue name
- **fromDate** (integer) - Optional - Filter logs by starting date, in milliseconds (Unix timestamp). This is inclusive.
- **toDate** (integer) - Optional - Filter logs by ending date, in milliseconds (Unix timestamp). This is inclusive.
- **count** (integer) - Optional - The number of log entries to return. Defaults to 100. Maximum is 100.
- **order** (string) - Optional - The sorting order of logs by timestamp. Possible values: latestFirst, earliestFirst. Defaults to latestFirst.
- **label** (string) - Optional - Filter logs by the label of the message assigned by the user

### Response
#### Success Response (200)
- **cursor** (string) - A cursor which you can use in subsequent requests to paginate through all logs. If no cursor is returned, you have reached the end of the logs.
- **logs** (array) - An array of LogEntry objects.

##### LogEntry Object
- **time** (integer) - The timestamp of the log entry in Unix milliseconds
- **messageId** (string) - The ID of the message

#### Response Example
```json
{
  "cursor": "some_cursor_string",
  "logs": [
    {
      "time": 1678886400000,
      "messageId": "msg_123"
    }
  ]
}
```
```

--------------------------------

### QStash API Authentication using Query Parameter

Source: https://upstash.com/docs/qstash/overall/llms-txt

Explains how to use the `qstash_token` query parameter for authentication when header authentication is not feasible.

```APIDOC
## QStash API Authentication using Query Parameter (Messages Get)

### Description
When setting the `Authorization` header is not feasible, you can authenticate your QStash API requests by including your `QSTASH_TOKEN` as the `qstash_token` query parameter. This example focuses on the messages get endpoint but applies generally.

### Method
This example uses cURL, but the principle applies to any HTTP client.

### Endpoint
`https://qstash.upstash.io/v2/messages/...?qstash_token=<QSTASH_TOKEN>` (Example endpoint for getting messages)

### Parameters
#### Query Parameters
- **qstash_token** (string) - Required - Your QStash token.

### Request Example
```bash
curl https://qstash.upstash.io/v2/messages/...?qstash_token=<QSTASH_TOKEN>
```

### Response
#### Success Response (200)
(Response details depend on the specific endpoint being called)

#### Response Example
(Response example depends on the specific endpoint being called)
```

--------------------------------

### Get QStash Queue Configuration (Python)

Source: https://upstash.com/docs/qstash/overall/llms-txt

Retrieves the current configuration for a specified QStash queue using the QStash Python client. This function requires your QStash API token and the name of the queue you wish to inspect.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.queue.get("my-queue")
```

--------------------------------

### Verify QStash Message Signature with Python SDK

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates how to initialize the QStash Receiver and verify the signature of an incoming message using the Python SDK.

```APIDOC
## Receiver Verification

### Description
This snippet demonstrates how to initialize the QStash Receiver and verify the signature of an incoming message. It requires your current and next signing keys, and the request URL. The function takes the message body and signature from the request headers as input.

### Method
N/A (This is a server-side verification process within your application)

### Endpoint
N/A (This code runs within your webhook handler)

### Parameters
#### Initialization Parameters
- **current_signing_key** (string) - Required - Your current QStash signing key.
- **next_signing_key** (string) - Required - Your next QStash signing key.

#### Verification Parameters (within request handler)
- **body** (string) - Required - The raw body of the incoming request.
- **signature** (string) - Required - The `Upstash-Signature` value from the request headers.
- **url** (string) - Required - The URL of your webhook endpoint.

### Request Example (Python)
```python
from qstash import Receiver

receiver = Receiver(
    current_signing_key="YOUR_CURRENT_SIGNING_KEY",
    next_signing_key="YOUR_NEXT_SIGNING_KEY",
)

# ... in your request handler

signature, body = req.headers["Upstash-Signature"], req.body

receiver.verify(
    body=body,
    signature=signature,
    url="YOUR-SITE-URL",
)
```

### Response
#### Success Response
No explicit response is returned by `receiver.verify()`. If the signature is valid, the function completes without raising an error. If the signature is invalid, it will raise an exception (e.g., `ValueError`).

#### Error Response
- **ValueError** - Raised if the message signature is invalid.
```

--------------------------------

### QStash Non-Retryable Error Header Example

Source: https://upstash.com/docs/qstash/features/retry

Illustrates how to use the Upstash-NonRetryable-Error header with a 489 status code to explicitly disable retries for a specific message, causing it to be sent to the Dead Letter Queue.

```text
Status: 489
Upstash-NonRetryable-Error: true
```

--------------------------------

### QStash API Endpoint to Start Background Job

Source: https://upstash.com/docs/qstash/overall/llms-txt

This Next.js API route handler, written in TypeScript, receives user data and uses the Upstash QStash client to publish a JSON message. This message invokes a separate API endpoint that contains the actual background job logic. It dynamically constructs the URL for the background job endpoint. Requires your QStash token.

```APIDOC
## POST /api/send-email (Example)

### Description
Starts a background job by publishing a JSON message to a specified URL using the Upstash QStash client.

### Method
POST

### Endpoint
`/api/send-email` (within your Next.js application)

### Parameters
#### Request Body
- **users** (array<string>) - Required - A list of user identifiers.

### Request Example
```json
{
  "users": ["user1@example.com", "user2@example.com"]
}
```

### Response
#### Success Response (200)
- **Message** (string) - Indicates that the job has been started.

### Code Example
```typescript
import { Client } from "@upstash/qstash";

const qstashClient = new Client({
  token: "YOUR_TOKEN",
});

export async function POST(request: Request) {
  const body = await request.json();
  const users: string[] = body.users;
  const rootDomain = request.url.split('/').slice(0, 3).join('/');
  const emailAPIURL = `${rootDomain}/api/send-email`; 

  await qstashClient.publishJSON({
    url: emailAPIURL,
    body: {
      users
    }
  });

  return new Response("Job started", { status: 200 });
}
```
```

--------------------------------

### QStash Python SDK Asynchronous Client Usage

Source: https://upstash.com/docs/qstash/overall/llms-txt

Demonstrates setting up and utilizing the asynchronous QStash client in Python for non-blocking operations. This approach is beneficial for applications requiring concurrent handling of multiple operations without sequential waiting.

```python
import asyncio

from qstash import AsyncQStash


async def main():
    client = AsyncQStash("<QSTASH_TOKEN>")
    await client.message.publish_json(...) 


asyncio.run(main())
```

--------------------------------

### Publish JSON Message with Upstash QStash Python SDK

Source: https://upstash.com/docs/qstash/howto/publishing

Provides an example of publishing a JSON message using the Upstash QStash Python client. It illustrates initializing the client with a token and using the message.publish_json method with URL, body, and headers.

```python
from qstash import QStash

client = QStash("<QSTASH_TOKEN>")
client.message.publish_json(
    url="https://my-api...",
    body={
        "hello": "world",
    },
    headers={
        "my-header": "my-value",
    },
)
```

--------------------------------

### POST /v2/publish/:url - Publish Message with Callback URLs

Source: https://upstash.com/docs/qstash/overall/llms-txt

Publishes a JSON message to a specified URL and configures callback URLs for success and failure notifications. Requires an Authorization header and Content-Type. Optional Upstash-Callback and Upstash-Failure-Callback headers can be provided.

```bash
# Example usage (conceptual, actual implementation depends on client library)
# POST https://qstash.upstash.io/v2/publish/<url>
# Headers:
# Authorization: Bearer <token>
# Content-type: application/json
# Upstash-Callback: <success_url>
# Upstash-Failure-Callback: <failure_url>
# Body:
# { "key": "value" }
```

--------------------------------

### List Schedules

Source: https://upstash.com/docs/qstash/api-refence/schedules/list-schedules

Retrieves a list of all schedules configured in QStash.

```APIDOC
## GET /v2/schedules

### Description
List all schedules.

### Method
GET

### Endpoint
/v2/schedules

### Parameters
#### Query Parameters
- **limit** (integer) - Optional - The maximum number of schedules to return.
- **offset** (integer) - Optional - The number of schedules to skip before returning results.
- **search** (string) - Optional - A search term to filter schedules by.

### Request Example
```json
{
  "example": "No request body needed for GET request."
}
```

### Response
#### Success Response (200)
- **scheduleId** (string) - Unique identifier for the schedule
- **cron** (string) - The cron expression used to schedule the message
- **destination** (string) - The destination URL or URL Group name
- **createdAt** (integer) - The creation timestamp of the schedule in unix milliseconds
- **method** (string) - The HTTP method used for the scheduled message
- **header** (object) - Map of header names to arrays of header values
- **body** (string) - The body of the scheduled message
- **retries** (integer) - The number of retries for the scheduled message
- **delay** (integer) - The delay in seconds before the scheduled message is sent
- **callback** (string) - The callback URL for the scheduled message
- **failureCallback** (string) - The failure callback URL for the scheduled message
- **callerIp** (string) - The IP address of the client that created the schedule
- **isPaused** (boolean) - Whether the schedule is paused
- **flowControlKey** (string) - The flow control key used for rate limiting
- **parallelism** (integer) - The parallelism value used for flow control
- **rate** (integer) - The rate value used for flow control
- **period** (integer) - The period value used for flow control
- **retryDelayExpression** (string) - The retry delay expression used for calculating retry delays
- **label** (string) - The label assigned to the scheduled message
- **lastScheduleTime** (integer) - The last time the schedule was triggered in unix milliseconds
- **nextScheduleTime** (integer) - The next scheduled trigger time in unix milliseconds
- **lastScheduleStates** (object) - The states of the last scheduled messages

#### Response Example
```json
[
  {
    "scheduleId": "sch_abc123",
    "cron": "* * * * *",
    "destination": "https://example.com/webhook",
    "createdAt": 1678886400000,
    "method": "POST",
    "header": {
      "Content-Type": ["application/json"]
    },
    "body": "{\"message\": \"Hello World\"}",
    "retries": 3,
    "delay": 60,
    "callback": "https://example.com/callback",
    "failureCallback": "https://example.com/failure",
    "callerIp": "192.168.1.1",
    "isPaused": false,
    "flowControlKey": "my-flow-key",
    "parallelism": 10,
    "rate": 100,
    "period": 60,
    "retryDelayExpression": "exponential",
    "label": "my-schedule",
    "lastScheduleTime": 1678886400000,
    "nextScheduleTime": 1678886460000,
    "lastScheduleStates": {
      "status": "success"
    }
  }
]
```
```

--------------------------------

### QStash LLM Batch Request JSON Payload

Source: https://upstash.com/docs/qstash/overall/llms-txt

An example JSON payload demonstrating how to structure a batch request to the QStash API for LLM (Large Language Model) tasks. Each object in the array specifies the API to call, the provider (e.g., Anthropic) with its token, the message body for the LLM, and a callback URL for receiving the results.

```json
[
  {
    "api": {
      "name": "llm",
      "provider": {
        "name": "anthropic",
        "token": "<ANTHROPIC_TOKEN>"
      }
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "messages": [{"role": "user", "content": "Describe the latest in AI research."}]
    },
    "callback": "https://example.com/callback1"
  },
  {
    "api": {
      "name": "llm",
      "provider": {
        "name": "anthropic",
        "token": "<ANTHROPIC_TOKEN>"
      }
    },
    "body": {
      "model": "claude-3-5-sonnet-20241022",
      "messages": [{"role": "user", "content": "Outline the future of remote work."}]
    },
    "callback": "https://example.com/callback2"
  }
]
```

--------------------------------

### Get URL Group by Name (TypeScript)

Source: https://upstash.com/docs/qstash/sdks/ts/examples/url-groups

Retrieves a specific URL Group by its name. It logs the group's name and its associated endpoints to the console. Requires a QStash client.

```typescript
import { Client } from "@upstash/qstash";

const client = new Client({ token: "<QSTASH_TOKEN>" });
const urlGroups = client.urlGroups;
const urlGroup = await urlGroups.get("urlGroupName");
console.log(urlGroup.name, urlGroup.endpoints);
```

--------------------------------

### Get a URL Group

Source: https://upstash.com/docs/qstash/api-refence/url-groups/get-a-url-group

Retrieve details of a specific URL Group by its name. This endpoint allows you to fetch information about a URL Group, including its creation and update timestamps, and associated endpoints.

```APIDOC
## GET /v2/topics/{urlGroupName}

### Description
Retrieve details of a specific URL Group.

### Method
GET

### Endpoint
/v2/topics/{urlGroupName}

### Parameters
#### Path Parameters
- **urlGroupName** (string) - Required - The name of the URL Group to retrieve.

### Response
#### Success Response (200)
- **name** (string) - URL Group name
- **createdAt** (integer) - Creation timestamp of URL Group in Unix milliseconds
- **updatedAt** (integer) - Last update timestamp of URL Group in Unix milliseconds
- **endpoints** (array) - List of endpoints associated with the URL Group
  - **name** (string) - The name of the endpoint
  - **url** (string) - The URL of the endpoint

#### Error Response (404)
- **error** (string) - Error message

### Request Example
```json
{
  "example": "No request body needed for GET request."
}
```

### Response Example
```json
{
  "name": "my-url-group",
  "createdAt": 1678886400000,
  "updatedAt": 1678886400000,
  "endpoints": [
    {
      "name": "primary",
      "url": "https://example.com/webhook"
    }
  ]
}
```
```

--------------------------------

### Golang QStash Webhook Handler and Verification

Source: https://upstash.com/docs/qstash/overall/llms-txt

Sets up an HTTP server in Golang to listen for QStash webhooks. It verifies the request signature using provided signing keys and handles potential errors. Dependencies include standard Go libraries for HTTP and I/O. The function takes the request body, signature, and signing keys as input.

```go
func main() {
	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		defer r.Body.Close()

		currentSigningKey := os.Getenv("QSTASH_CURRENT_SIGNING_KEY")
		nextSigningKey := os.Getenv("QSTASH_NEXT_SIGNING_KEY")
	
tokenString := r.Header.Get("Upstash-Signature")

		body, err := io.ReadAll(r.Body)
		if err != nil {
			http.Error(w, err.Error(), http.StatusInternalServerError)
			return
		}

		err = verify(body, tokenString, currentSigningKey)
		if err != nil {
			fmt.Printf("Unable to verify signature with current signing key: %v", err)
			err = verify(body, tokenString, nextSigningKey)
		}

		if err != nil {
			http.Error(w, err.Error(), http.StatusUnauthorized)
			return
		}

		// handle your business logic here

		w.WriteHeader(http.StatusOK)

	})

	fmt.Println("listening on", port)
	err := http.ListenAndServe(":"+port, nil)
	if err != nil {
		panic(err)
	}
}
```