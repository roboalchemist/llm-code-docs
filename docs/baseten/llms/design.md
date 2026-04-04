# Source: https://docs.baseten.co/development/chain/design.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Architecture and design

> How to structure your Chainlets

A Chain is composed of multiple connected Chainlets working together to perform
a task.

For example, the Chain in the diagram below takes a large audio file as input.
Then it splits it into smaller chunks, transcribes each chunk in parallel
(reducing the end-to-end latency), and finally aggregates and returns the
results.

<Frame>
  <img src="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=135870ba1fc2e86cf319815eafe14441" data-og-width="1280" width="1280" data-og-height="155" height="155" data-path="development/chain/images/audio-transcription.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=280&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=349246b63271305875316013222b8c90 280w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=560&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=3cd50bb5fff404036b210ff33feebc53 560w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=840&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=839c92448e904237050e9dc56f19a1e7 840w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=1100&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=5ed90d4e49b2a27c35f35706cf53cfa7 1100w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=1650&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=35ab233489e8de235bf7cd390ba5963d 1650w, https://mintcdn.com/baseten-preview/W3NbEem9OZkF5rdB/development/chain/images/audio-transcription.svg?w=2500&fit=max&auto=format&n=W3NbEem9OZkF5rdB&q=85&s=ed9e02564abf1e48ec71fdd4c60fd034 2500w" />
</Frame>

To build an efficient Chain, we recommend drafting your high level
structure as a flowchart or diagram. This can help you identifying
parallelizable units of work and steps that need different (model/hardware)
resources.

If one Chainlet creates many "sub-tasks" by calling other dependency
Chainlets (e.g. in a loop over partial work items),
these calls should be done as `aynscio`-tasks that run concurrently.
That way you get the most out of the parallelism that Chains offers. This
design pattern is extensively used in the
[audio transcription example](/examples/chains-audio-transcription).

<Warning>
  While using `asyncio` is essential for performance, it can also be tricky.
  Here are a few caveats to look out for:

  * Executing operations in an async function that block the event loop for
    more than a fraction of a second. This hinders the "flow" of processing
    requests concurrently and starting RPCs to other Chainlets. Ideally use
    native async APIs. Frameworks like vLLM or triton server offer such APIs,
    similarly file downloads can be made async and you might find
    [`AsyncBatcher`](https://github.com/hussein-awala/async-batcher) useful.
    If there is no async support, consider running blocking code in a
    thread/process pool (as an attribute of a Chainlet).
  * Creating async tasks (e.g. with `asyncio.ensure_future`) does not start
    the task *immediately*. In particular, when starting several tasks in a loop,
    `ensure_future` must be alternated with operations that yield to the event
    loop that, so the task can be started. If the loop is not `async for` or
    contains other `await` statements, a "dummy" await can be added, for example
    `await asyncio.sleep(0)`. This allows the tasks to be started concurrently.
</Warning>
