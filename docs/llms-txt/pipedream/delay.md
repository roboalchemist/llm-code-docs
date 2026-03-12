# Source: https://pipedream.com/docs/workflows/building-workflows/control-flow/delay.md

# Source: https://pipedream.com/docs/workflows/building-workflows/code/python/delay.md

# Source: https://pipedream.com/docs/workflows/building-workflows/code/nodejs/delay.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://pipedream.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Delaying A Workflow

export const DELAY_MIN_MAX_TIME = 'You can pause your workflow for as little as one millisecond, or as long as one year';

export const MAX_WORKFLOW_EXECUTION_LIMIT = '750';

<Frame>
  <iframe className="w-full aspect-video rounded-xl" src="https://www.youtube.com/embed/IBORwBnIZ-k?start=148" title="Delaying Workflow Steps" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />
</Frame>

Use `$.flow.delay` to [delay a step in a workflow](/workflows/building-workflows/control-flow/delay/).

These docs show you how to write Node.js code to handle delays. If you don’t need to write code, see [our built-in delay actions](/workflows/building-workflows/control-flow/delay/#delay-actions).

## Using `$.flow.delay`

`$.flow.delay` takes one argument: the number of **milliseconds** you’d like to pause your workflow until the next step executes. {DELAY_MIN_MAX_TIME}.

Note that [delays happen at the end of the step where they’re called](/workflows/building-workflows/code/nodejs/delay/#when-delays-happen).

```javascript  theme={null}
export default defineComponent({
  async run({ steps, $ }) {
    // Delay a workflow for 60 seconds (60,000 ms)
    $.flow.delay(60 * 1000)
 
    // Delay a workflow for 15 minutes
    $.flow.delay(15 * 60 * 1000)
 
    // Delay a workflow based on the value of incoming event data,
    // or default to 60 seconds if that variable is undefined
    $.flow.delay(steps.trigger.event?.body?.delayMs ?? 60 * 1000)
 
    // Delay a workflow a random amount of time
    $.flow.delay(Math.floor(Math.random() * 1000))
  }
});
```

<Note>
  Paused workflow state

  When `$.flow.delay` is executed in a Node.js step, the workflow itself will enter a **Paused** state.

  While the workflow is paused, it will not incur any credits towards compute time. You can also [view all paused workflows in the Event History](/workflows/event-history/#filtering-by-status).
</Note>

### Credit usage

The length of time a workflow is delayed from `$.flow.delay` does *not* impact your credit usage. For example, delaying a 256 megabyte workflow for five minutes will **not** incur ten credits.

However, using `$.flow.delay` in a workflow will incur two credits.

One credit is used to initially start the workflow, then the second credit is used when the workflow resumes after its pause period has ended.

<Note>
  Exact credit usage depends on duration and memory configuration

  If your workflow’s [execution timeout limit](/workflows/building-workflows/settings/#execution-timeout-limit) is set to longer than [default limit](/workflows/limits/#time-per-execution), it may incur more than two [credits](/pricing/#credits-and-billing) when using `pd.flow.delay`.
</Note>

## `cancel_url` and `resume_url`

Both the built-in **Delay** actions and `$.flow.delay` return a `cancel_url` and `resume_url` that lets you cancel or resume paused executions.

These URLs are specific to a single execution of your workflow. While the workflow is paused, you can load these in your browser or send an HTTP request to either:

* Hitting the `cancel_url` will immediately cancel that execution
* Hitting the `resume_url` will immediately resume that execution early

[Since Pipedream pauses your workflow at the *end* of the step where you run call `$.flow.delay`](/workflows/building-workflows/code/nodejs/delay/#when-delays-happen), you can send these URLs to third party systems, via email, or anywhere else you’d like to control the execution of your workflow.

```javascript  theme={null}
import axios from 'axios'
 
export default defineComponent({
  async run({ steps, $ }) {
    const { cancel_url, resume_url } = $.flow.delay(15 * 60 * 1000)
 
    // Send the URLs to a system you own
    await axios({
      method: "POST",
      url: `https://example.com`,
      data: { cancel_url, resume_url },
    });
 
    // Email yourself the URLs. Click on the links to cancel / resume
    $.send.email({
      subject: `Workflow execution ${steps.trigger.context.id}`,
      text: `Cancel your workflow here: ${cancel_url} . Resume early here: ${resume_url}`,
    });
  }
});
 
// Delay happens at the end of this step
```

## When delays happen

**Pipedream pauses your workflow at the *end* of the step where you call `$.flow.delay`**. This lets you [send the `cancel_url` and `resume_url` to third-party systems](/workflows/building-workflows/code/nodejs/delay/#cancel_url-and-resume_url).

```javascript  theme={null}
export default defineComponent({
  async run({ steps, $ }) {
    const { cancel_url, resume_url } = $.flow.delay(15 * 60 * 1000)
    // ... run any code you want here
  }
});
 
// Delay happens at the end of this step
```

## Delays and HTTP responses

You cannot run `$.respond` after running `$.flow.delay`. Pipedream ends the original execution of the workflow when `$.flow.delay` is called and issues the following response to the client to indicate this state:

> \$.respond() not called for this invocation

If you need to set a delay on an HTTP request triggered workflow, consider using [`setTimeout`](/workflows/building-workflows/code/nodejs/delay/#settimeout) instead.

## `setTimeout`

Alternatively, you can use `setTimeout` instead of using `$.flow.delay` to delay individual workflow steps.

However, there are some drawbacks to using `setTimeout` instead of `$.flow.delay`. `setTimeout` will count towards your workflow’s compute time, for example:

```javascript  theme={null}
export default defineComponent({
  async run({ steps, $ }) {
    // delay this step for 30 seconds
    const delay = 30000;
 
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve('timer ended')
      }, delay)
    })
  }
});
 
```

The Node.js step above will hold the workflow’s execution for this step for 30 seconds; however, 30 seconds will also *contribute* to your credit usage. Also consider that workflows have a hard limit of {MAX_WORKFLOW_EXECUTION_LIMIT} seconds.

Built with [Mintlify](https://mintlify.com).
