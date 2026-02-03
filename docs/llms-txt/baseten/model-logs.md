# Source: https://docs.baseten.co/reference/cli/truss/model-logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss model-logs

> Fetch logs for a deployed model.

```sh  theme={"system"}
truss model-logs [OPTIONS]
```

Fetches logs for a deployed model. Use this command to debug issues or monitor model behavior in production.

### Options

<ParamField body="--model-id" type="TEXT" required>
  The ID of the model to fetch logs from.
</ParamField>

<ParamField body="--deployment-id" type="TEXT" required>
  The ID of the deployment to fetch logs from.
</ParamField>

<ParamField body="--tail">
  Tail for ongoing logs. Streams new log entries as they arrive.
</ParamField>

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to fetch logs from.
</ParamField>

**Example:**

To fetch logs for a specific deployment, use the following:

```sh  theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID
```

To stream logs in real-time, use the following:

```sh  theme={"system"}
truss model-logs --model-id YOUR_MODEL_ID --deployment-id YOUR_DEPLOYMENT_ID --tail
```
