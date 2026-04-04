# Source: https://upstash.com/docs/workflow/rest/runs/cancel.md

# Source: https://upstash.com/docs/workflow/howto/cancel.md

# Source: https://upstash.com/docs/workflow/basics/context/cancel.md

# Source: https://upstash.com/docs/workflow/basics/client/cancel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# client.cancel

There are multiple ways you can cancel workflow runs:

* Pass one or more workflow run ids to cancel them
* Pass a workflow url to cancel all runs starting with this url
* cancel all pending or active workflow runs

## Arguments

<ParamField body="ids" type="array">
  The set of workflow run IDs you want to cancel
</ParamField>

<ParamField body="urlStartingWith" type="string">
  The URL address you want to filter while canceling
</ParamField>

<ParamField body="all" type="bool">
  Whether you want to cancel all workflow runs without any filter.
</ParamField>

## Usage

### Cancel a set of workflow runs

```ts  theme={"system"}
// cancel a single workflow
await client.cancel({ ids: "<WORKFLOW_RUN_ID>" });

// cancel a set of workflow runs
await client.cancel({ ids: ["<WORKFLOW_RUN_ID_1>", "<WORKFLOW_RUN_ID_2>"] });
```

### Cancel workflow runs with URL filter

If you have an endpoint called `https://your-endpoint.com` and you
want to cancel all workflow runs on it, you can use `urlStartingWith`.

Note that this will cancel workflows in all endpoints under
`https://your-endpoint.com`.

```ts  theme={"system"}
await client.cancel({ urlStartingWith: "https://your-endpoint.com" });
```

### Cancel *all* workflows

To cancel all pending and currently running workflows, you can
do it like this:

```ts  theme={"system"}
await client.cancel({ all: true });
```
