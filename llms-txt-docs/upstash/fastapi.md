# Source: https://upstash.com/docs/workflow/quickstarts/fastapi.md

# Source: https://upstash.com/docs/redis/quickstarts/fastapi.md

# Source: https://upstash.com/docs/workflow/quickstarts/fastapi.md

# FastAPI

<Card title="GitHub Repository" icon="github" href="https://github.com/upstash/workflow-py/tree/master/examples/fastapi" horizontal>
  You can find the project source code on GitHub.
</Card>

This guide provides detailed, step-by-step instructions on how to use Upstash Workflow with FastAPI. You can also explore [the source code](https://github.com/upstash/workflow-py/tree/master/examples/fastapi) for a detailed, end-to-end example and best practices.

## Prerequisites

1. An Upstash QStash API key.
2. Python and pip installed.

If you haven't obtained your QStash API key yet, you can do so by [signing up](https://console.upstash.com/login) for an Upstash account and navigating to your QStash dashboard.

## Step 1: Installation

First, create a new directory and set up a virtual environment:

```bash  theme={"system"}
python -m venv venv
source venv/bin/activate
```

Then, install the Workflow SDK and FastAPI:

```bash  theme={"system"}
pip install fastapi uvicorn upstash-workflow
```

## Step 2: Configure Environment Variables

Create a `.env` file in your project root and add your QStash token. This token is used to authenticate your application with the QStash service.

```bash Terminal theme={"system"}
touch .env
```

Upstash Workflow is powered by [QStash](/qstash/overall/getstarted), which requires access to your endpoint to execute workflows. When your app is deployed, QStash will use the app's URL. However, for local development, you have two main options: [use a local QStash server or set up a local tunnel](/workflow/howto/local-development).

### Option 1: Local QStash Server

To start the local QStash server, run:

```bash  theme={"system"}
npx @upstash/qstash-cli dev
```

Once the command runs successfully, you’ll see `QSTASH_URL` and `QSTASH_TOKEN` values in the console. Add these values to your `.env` file:

```bash .env theme={"system"}
export QSTASH_URL="http://127.0.0.1:8080"
export QSTASH_TOKEN="<QSTASH_TOKEN>"
```

This approach allows you to test workflows locally without affecting your billing. However, runs won't be logged in the Upstash Console.

### Option 2: Local Tunnel

Alternatively, you can set up a local tunnel. For this option:

1. Copy the `QSTASH_TOKEN` from the Upstash Console.
2. Update your `.env` file with the following:

```bash .env theme={"system"}
export QSTASH_TOKEN="***"
export UPSTASH_WORKFLOW_URL="<UPSTASH_WORKFLOW_URL>"
```

* Replace `***` with your actual QStash token.
* Set `UPSTASH_WORKFLOW_URL` to the public URL provided by your local tunnel.

Here’s where you can find your QStash token:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=df12ba48119bcdd13a675e53b43ab74d" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_token.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c251f0eeb0a6973ff498f9e9930aed70 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=d452c08e1a638dff258d938aa8544f25 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6b197538fe5190c7936b751ec228ef39 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=63da8b3df03c88ff0a7700af7a5db6fb 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8df98665037cf63deb6b48d5c22d3f6b 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_token.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b3ef0ab4137bdec59b7cb772550933e1 2500w" />
</Frame>

Using a local tunnel connects your endpoint to the production QStash, enabling you to view workflow logs in the Upstash Console.

## Step 3: Create a Workflow Endpoint

A workflow endpoint allows you to define a set of steps that, together, make up a workflow. Each step contains a piece of business logic that is automatically retried on failure, with easy monitoring via our visual workflow dashboard.

To define a workflow endpoint in a FastAPI project, create a `main.py` file that contains your workflow:

<Tabs>
  <Tab title="Example">
    ```python main.py theme={"system"}
    from fastapi import FastAPI
    from upstash_workflow.fastapi import Serve

    app = FastAPI()
    serve = Serve(app)


    @serve.post("/api/workflow")
    async def workflow(context) -> None:
        async def _step1() -> None:
            print("initial step ran")

        await context.run("initial-step", _step1)

        async def _step2() -> None:
            print("second step ran")

        await context.run("second-step", _step2)

    ```
  </Tab>

  <Tab title="Sleep">
    ```python main.py theme={"system"}
    from fastapi import FastAPI
    import time
    from upstash_workflow.fastapi import Serve
    from upstash_workflow import AsyncWorkflowContext

    app = FastAPI()
    serve = Serve(app)


    def some_work(input: str) -> str:
        return f"processed '{input}'"


    @serve.post("/sleep")
    async def sleep(context: AsyncWorkflowContext[str]) -> None:
        input = context.request_payload

        async def _step1() -> str:
            output = some_work(input)
            print("step 1 input", input, "output", output)
            return output

        result1: str = await context.run("step1", _step1)

        await context.sleep_until("sleep1", time.time() + 3)

        async def _step2() -> str:
            output = some_work(result1)
            print("step 2 input", result1, "output", output)
            return output

        result2: str = await context.run("step2", _step2)

        await context.sleep("sleep2", 2)

        async def _step3() -> None:
            output = some_work(result2)
            print("step 3 input", result2, "output", output)

        await context.run("step3", _step3)

    ```
  </Tab>

  <Tab title="Call">
    ```python main.py theme={"system"}
    from fastapi import FastAPI
    from typing import Dict
    from upstash_workflow.fastapi import Serve
    from upstash_workflow import AsyncWorkflowContext, CallResponse

    app = FastAPI()
    serve = Serve(app)


    def some_work(input: str) -> str:
        return f"processed '{input}'"


    @app.post("/get-data")
    async def get_data() -> Dict[str, str]:
        return {"message": "get data response"}


    @serve.post("/call")
    async def call(context: AsyncWorkflowContext[str]) -> None:
        input = context.request_payload

        async def _step1() -> str:
            output = some_work(input)
            print("step 1 input", input, "output", output)
            return output

        result1: str = await context.run("step1", _step1)

        response: CallResponse[Dict[str, str]] = await context.call(
            "get-data",
            url=f"{context.env.get('UPSTASH_WORKFLOW_URL', 'http://localhost:8000')}/get-data",
            method="POST",
            body={"message": result1},
        )

        async def _step2() -> str:
            output = some_work(response.body["message"])
            print("step 2 input", response, "output", output)
            return output

        await context.run("step2", _step2)

    ```
  </Tab>

  <Tab title="Auth">
    ```python main.py theme={"system"}
    from fastapi import FastAPI
    from upstash_workflow.fastapi import Serve
    from upstash_workflow import AsyncWorkflowContext

    app = FastAPI()
    serve = Serve(app)


    def some_work(input: str) -> str:
        return f"processed '{input}'"


    @serve.post("/auth")
    async def auth(context: AsyncWorkflowContext[str]) -> None:
        if context.headers.get("authentication") != "Bearer secret_password":
            print("Authentication failed.")
            return

        async def _step1() -> str:
            return "output 1"

        await context.run("step1", _step1)

        async def _step2() -> str:
            return "output 2"

        await context.run("step2", _step2)

    ```
  </Tab>
</Tabs>

## Step 4: Run the Workflow Endpoint

Don't forget to source your environment file to set your environment variables:

```bash Terminal theme={"system"}
source .env
```

After setting your live URL as the environment variable or `base_url` option, trigger your workflow by first starting your FastAPI app:

```bash Terminal theme={"system"}
uvicorn main:app --reload
```

and then making a POST request to your workflow endpoint. For each workflow run, a unique workflow run ID is returned:

```bash Terminal theme={"system"}
curl -X POST https://localhost:8000/api/workflow

# result: {"workflowRunId":"wfr_xxxxxx"}
```

See the [documentation on starting a workflow](/workflow/howto/start) for other ways you can start your workflow.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=4f2cbb67caa1985c680629d89c96fca4" data-og-width="1737" width="1737" data-og-height="634" height="634" data-path="img/qstash-workflow/nextjs_local_request.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f41c789c5b932b1f055c0e268e5b9605 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=22cbc44e0f95850cc384949d6f7d89ae 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=c87b767a909164536ed792b237ab7cb2 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=42d2f62728e193974c5cec61189918fa 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e1fabf80bcfe0aa313e60c593f807356 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/nextjs_local_request.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=1b5e61b1b8b06d07a84ac2f5f34810b0 2500w" />
</Frame>

If you are using a local tunnel, you can use this ID to track the workflow run and see its status in your QStash workflow dashboard. All steps are listed with their statuses, headers, and body for a detailed overview of your workflow from start to finish. Click on a step to see its detailed logs.

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d62fa91b9bcfc9c845105c42dae6f1e0" data-og-width="1656" width="1656" data-og-height="1080" height="1080" data-path="img/qstash-workflow/dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8b59e83f0dc4ac843391ad758f34f0e8 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=000f796c9f6977bd9918ffcb657fbee3 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8609b0c44963e73b7be7b1eac2f855bf 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=2a37385f1f54c7ed8597051b02dfb783 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=b2b4cdfe944c486ed4c73078c2509222 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/dashboard.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=c3a84ffafdd7cbe5b00be4e435dacf84 2500w" />
</Frame>

## Next Steps

1. Learn how to protect your workflow endpoint from unauthorized access by [securing your workflow endpoint](/workflow/howto/security).

2. Explore [the source code](https://github.com/upstash/workflow-py/tree/master/examples/fastapi) for a detailed, end-to-end example and best practices.

3. For setting up and testing your workflows in a local environment, check out our [local development guide](/workflow/howto/local-development).
