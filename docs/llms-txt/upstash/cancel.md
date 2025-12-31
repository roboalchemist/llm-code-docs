# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

# Source: https://upstash.com/docs/qstash/api/messages/cancel.md

# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

# Source: https://upstash.com/docs/qstash/api/messages/cancel.md

# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

# Source: https://upstash.com/docs/qstash/api/messages/cancel.md

# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Cancel Workflow

> Stop a running workflow run

Cancelling a workflow run will remove it from QStash and stop it from being delivered
in the future.

## Request

<ParamField path="workflowRunId" type="string" required>
  The id of the message to cancel.
</ParamField>

## Response

This endpoint returns

* `200 OK` when successful.
* `404 NOT FOUND` when a workflow run is not found with the given id.
* `500 INTERNAL SERVER` when an unexpected error occurs.

<RequestExample>
  ```sh curl theme={"system"}
  curl -XDELETE https://qstash.upstash.io/v2/workflows/runs/wfr_TzazoUCuZmFGp2u9cdy5K \
    -H "Authorization: Bearer <token>"
  ```

  ```js Workflow SDK theme={"system"}
  import { Client } from "@upstash/workflow";

  const client = new Client({ token: "<QSTASH_TOKEN>" })
  await client.cancel({ workflowRunId: "<WORKFLOW_RUN_ID>" })
  ```

  ```js Node theme={"system"}
  const response = await fetch('https://qstash.upstash.io/v2/workflows/runs/wfr_TzazoUCuZmFGp2u9cdy5K', {
    method: 'DELETE',
    headers: {
      'Authorization': 'Bearer <token>'
    }
  });
  ```

  ```python Python theme={"system"}
  import requests

  headers = {
      'Authorization': 'Bearer <token>',
  }

  response = requests.delete(
    'https://qstash.upstash.io/v2/workflows/runs/wfr_TzazoUCuZmFGp2u9cdy5K', 
    headers=headers
  )
  ```

  ```go Go theme={"system"}
  req, err := http.NewRequest("DELETE", "https://qstash.upstash.io/v2/workflows/runs/wfr_TzazoUCuZmFGp2u9cdy5K", nil)
  if err != nil {
    log.Fatal(err)
  }
  req.Header.Set("Authorization", "Bearer <token>")
  resp, err := http.DefaultClient.Do(req)
  if err != nil {
    log.Fatal(err)
  }
  defer resp.Body.Close()
  ```
</RequestExample>

<ResponseExample>
  ```text 200 OK theme={"system"}
  OK
  ```
</ResponseExample>
