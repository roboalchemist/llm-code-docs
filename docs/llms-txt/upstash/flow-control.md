# Source: https://upstash.com/docs/workflow/howto/flow-control.md

# Source: https://upstash.com/docs/workflow/features/flow-control.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

Flow Control allows you to limit how many workflow steps are executed by delaying and queuing their delivery.

This feature helps to:

* Manage resource consumption
* Prevent violations of external API rate limits
* Ensure workflows run within defined system constraints

## How Flow Control Works

When defined limits are exceeded, Flow Control automatically queues and delays step executions instead of rejecting them.
This guarantees that all steps are eventually processed while staying within configured thresholds.

To configure Flow Control, you define a flow control key, a unique identifier used to group related steps under the same rate and parallelism limits.
The steps that has the same flow control key respect the same constraints.

There are two main parameters to configure:

* [Rate and Period](/workflow/features/flow-control/rate-period): Maximum number of steps that may start within a time window
* [Parallelism](/workflow/features/flow-control/parallelism): Maximum number of steps allowed to run concurrently

These parameters can be combined for fine‑grained control.
For example, you can allow up to 10 steps per minute but restrict concurrency
to 5 steps in parallel, ensuring more predictable load patterns.

## Example

Suppose you have the following workflow:

```typescript  theme={"system"}
export const { POST } = serve<{ topic: string }>(async (context) => {
  const payload = context.requestPayload

  await context.run("step-1", () => { ... });

  await context.run("step-2", () => { ... });

  await context.run("step-3", () => { ... });
})
```

Now imagine you trigger **N workflow runs** for this workflow with the following configuration:

```typescript  theme={"system"}
const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  flowControl: {
    key: "fw_example",
    parallelism: 7,
    rate: 3,
    period: "1m",
  }
})
```

Without Flow Control, all workflow runs immediately execute their steps as soon as possible.
If the workflow calls an external API in a step, this would likely result in \~N concurrent requests being fired in a very short timeframe, potentially overloading services or breaching API limits.

<Frame caption="Workflow simplified by step types">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=00abee01364d02ee0de0885c718fd41f" data-og-width="658" width="658" data-og-height="241" height="241" data-path="img/workflow/flow_control_ex_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=c648645fabc40fccc428cd0a1d32a24a 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d3be1762f6ea88fce8e17f8315f5ee55 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=dd39cf7e6f01ad6ce9cc64c95a47eecd 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=7b76d616e49442c2ddcb81677230da08 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=f2f179932b85ee72b568bb84b6302263 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_3.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=ac25a92a95fd2346bb665326dfee5da7 2500w" />
</Frame>

With the configuration above:

* **Rate:** At most 3 steps per minute can start across all workflow runs.
* **Parallelism:** At most 7 steps can be running at the same time.

Steps that exceed these limits are automatically queued and executed later.

<Frame caption="Steps are enqueued for execution">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=bf64d6a7f4b4bb560d0de92e876bc0c9" data-og-width="1091" width="1091" data-og-height="451" height="451" data-path="img/workflow/flow_control_ex_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=6c029a364026f6a282cc6b0c8e8d7f6f 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=27f0c274948a17838028fa3b94bc01b3 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=07f6fa5c98e41cda83bc912e42e7b96f 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=32c239dba69eedbc277e08708e0a8f42 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=0e44ab27623808fd41999f763df36c34 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_2.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=8fb65f9e8a519387da080b6e5a502d84 2500w" />
</Frame>

Note that each step above corresponds to a separate workflow run.
Because this workflow is sequential, each workflow run has only one pending step at a time.
In workflows with **parallel branches**, multiple steps from the same workflow run may appear in the schedule simultaneously.

Parallelism slots are consumed by running steps.
If no slots are available, new steps enter the **waitlist** until resources free up:

<Frame caption="Parallelism waitlist for the flow-control">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=297f424a8fef25787e7e5d986cbd990b" data-og-width="1091" width="1091" data-og-height="491" height="491" data-path="img/workflow/flow_control_ex_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=efbb88dcc4080e7db40872181e7f75a7 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=f831c8483222d7ba121a971a5b57c5c8 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=8292d0d265fbb91ec8483e9c2383a830 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=c0076acee733bce0a253d3822b59c989 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=13c17407ffc2d6289761b5ec4266d624 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/flow_control_ex_1.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=eeb48b7cd2095685320971227712e2ab 2500w" />
</Frame>

<Note>
  Upstash Workflow does not support per-step level configuration. Meaning that you can attach a flow-control configuration
  to the workflow run and all the steps will inherit to the same limits.
  Following the analogy above, you cannot enforce parallelism limit on "green" steps natively.

  The context.call and context.invoke steps are exception this to this rule and accept their own flow control configuration:

  * [context.call](/workflow/basics/context/call) – lets you run external HTTP requests under a separate key, so you can throttle third‑party API calls independently of your workflow logic.
  * [context.invoke](/workflow/basics/context/invoke) – starts a new workflow run with its own flow control configuration. This allows the invoked workflow to run under different limits than the parent workflow, giving you more precise control.

  If you want to throttle a specific `context.run` step, the recommended approach is to **extract it into a separate workflow** and call it using `context.invoke()` with its own flow control configuration with a stricter limits.
</Note>

## Configuration

You can configure flow control when starting a workflow run:

```typescript Configure Retry Attempt Count theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  flowControl: {
    key: "user-signup",
    parallelism: 1,
    rate: 10,
    period: 100,
  }
})
```

All steps within a workflow run will adhere to the specified flow control configuration.

<Warning>
  Keep in mind that rate/period and parallelism info are kept on each step separately.
  If you change the rate/period or parallelism on a new deployment, the old fired ones will not be affected.
  They will keep their flow control configuration.

  During the period that old steps have not been delivered but there are also steps with new rates, Upstash Workflow will effectively allow the highest rate/period or highest parallelism. Eventually (after the old publishes are delivered), the new rate/period and parallelism will be used.
</Warning>
