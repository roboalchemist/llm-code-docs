# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

# Source: https://upstash.com/docs/workflow/howto/security.md

# Source: https://upstash.com/docs/redis/features/security.md

# Source: https://upstash.com/docs/qstash/features/security.md

# Source: https://upstash.com/docs/workflow/howto/security.md

# Secure a Workflow

To prevent unauthorized access to your workflow endpoint, you can add an authorization layer.
Upstash Workflow supports two approaches:

* **Built-in request verification** (recommended)
* **Custom authorization method**

### Built-in request verification (recommended)

Upstash Workflow provides a built-in mechanism to secure your workflow endpoint by verifying request signatures.
Every request to your endpoint include a valid `Upstash-Signature` header.

How it works:

1. Upstash Workflow automatically adds the `Upstash-Signature` header to every request.
   This signature is generated using your signing keys.

2. When this mechanism is enabled, the SDK verifies that the signature is valid before processing the request.

This ensures that only requests originating from Upstash Workflow are processed.

To enable this verification, set the following environment variables in your application:

```bash .env theme={"system"}
QSTASH_CURRENT_SIGNING_KEY=xxxxxxxxx
QSTASH_NEXT_SIGNING_KEY=xxxxxxxxx
```

You can find the values in Upstash Workflow dashboard.

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=80587de8e955411f9c092d3348056af3" data-og-width="1211" width="1211" data-og-height="833" height="833" data-path="img/qstash-workflow/qstash_signing_keys.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9aff13ae1e92d8e869d002ed08a9da07 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=796060edf979b7ce1e6710b9a4cdf78b 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=185f283f737442f131d8f3de95f88cc8 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=773c19bc5a6f25f3fa5f3616c7f7919f 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=cf56a1e230831d2bfdd539d8118df910 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/qstash_signing_keys.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=e42354e5503790f53e952804d7ca0ead 2500w" />
</Frame>

<Info>
  For edge cases where environment variables cannot be used, you can explicitly create and pass a `Receiver` object to verify request signatures:

  <CodeGroup>
    ```typescript TypeScript theme={"system"}
    import { Receiver } from "@upstash/qstash";
    import { serve } from "@upstash/workflow/nextjs";

    export const { POST } = serve(
      async (context) => { ... },
      {
        receiver: new Receiver({
          currentSigningKey: "<QSTASH_CURRENT_SIGNING_KEY>",
          nextSigningKey: "<QSTASH_NEXT_SIGNING_KEY>",
        }),
      }
    );
    ```

    ```python Python theme={"system"}
    from qstash import Receiver

    @serve.post(
        "/api/example",
        receiver=Receiver(
            current_signing_key=os.environ["QSTASH_CURRENT_SIGNING_KEY"],
            next_signing_key=os.environ["QSTASH_NEXT_SIGNING_KEY"],
        ),
    )
    async def example(context: AsyncWorkflowContext[str]) -> None:
        ...

    ```
  </CodeGroup>
</Info>

## Custom Authorization Method

You can implement your own authorization mechanism with Upstash Workflow.

The context object provides access to the initial request headers and payload on every workflow step.
You can use them to pass your custom authentication token to verify the requests.

<CodeGroup>
  ```typescript TypeScript theme={"system"}
  import { serve } from "@upstash/workflow/nextjs";

  export const { POST } = serve(
    async (context) => {
      // 👇 Extract Bearer token form the request headers
      const authHeader = context.headers.get("authorization");
      const bearerToken = authHeader?.split(" ")[1];

      // 👇 Use your authentication function to verify the token
      if (!isValid(bearerToken)) {
        console.error("Authentication failed.");
        return;
      }

      // Your workflow steps..
    },
    {
      failureFunction: async () => {
        // 👇 Same auth check for failure function
        const authHeader = context.headers.get("authorization");
        const bearerToken = authHeader?.split(" ")[1];

        if (!isValid(bearerToken)) {
          // ...
        }
      },
    }
  );
  ```

  ```python Python theme={"system"}
  from fastapi import FastAPI
  from upstash_workflow.fastapi import Serve
  from upstash_workflow import AsyncWorkflowContext

  app = FastAPI()
  serve = Serve(app)


  @serve.post("/api/example")
  async def example(context: AsyncWorkflowContext[str]) -> None:
      auth_header = context.headers.get("authorization")
      bearer_token = auth_header.split(" ")[1] if auth_header else None

      if not is_valid(bearer_token):
          print("Authentication failed.")
          return

      # Your workflow steps...

  ```
</CodeGroup>

<Warning>
  If you implement custom authorization in your workflow route, you should also include the same authorization check in the failure function.

  The failure function executes independently of the route function, so without this check, unauthorized requests could trigger the failure function
</Warning>
