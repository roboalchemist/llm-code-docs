# Source: https://upstash.com/docs/workflow/features/invoke.md

# Source: https://upstash.com/docs/workflow/basics/context/invoke.md

# Source: https://upstash.com/docs/workflow/features/invoke.md

# Source: https://upstash.com/docs/workflow/basics/context/invoke.md

# Source: https://upstash.com/docs/workflow/features/invoke.md

# Overview

You can start another workflow run inside a workflow and await its execution to complete.
This allows to orchestrate multiple workflows together without external synchronization.

When you use `context.invoke`, invoking workflow will wait until the invoked workflow finishes before running the next step.

```typescript  theme={"system"}
const {
  body,      // response from the invoked workflow
  isFailed,  // whether the invoked workflow was canceled
  isCanceled // whether the invoked workflow failed
} = await context.invoke(
  "analyze-content",
  {
    workflow: analyzeContent,
    body: "test",
    header: {...}, // headers to pass to anotherWorkflow (optional)
    retries,       // number of retries (optional, default: 3)
    flowControl,   // flow control settings (optional)
    workflowRunId  // workflowRunId to set (optional)
  }
)
```

You can return a response from a workflow, which will be delivered to invoker workflow run.

<Frame caption="You can navigate between the invoker and invoked workflow runs on the dashboard">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=be3ca055f5f46e428c84a7983c2402e5" data-og-width="2658" width="2658" data-og-height="1976" height="1976" data-path="img/workflow/invoke.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=95507fbe673befccc3556d4b4a6f718e 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=2bc7e59da157da8dd232093b4146f369 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=5bf2affd5061997df74054dd6b00694b 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=ac40691a971029998a0c40983295084f 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d057f384353c6dc8921c9df3b053becb 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/invoke.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d20b0e49e253ef8b825838fa14adf619 2500w" />
</Frame>

<Note>
  You cannot create an infinite chain of workflow invocations. If you set up an 'invoke loop' where workflows continuously invoke each other, the process will fail once it reaches a depth of 100.
</Note>
