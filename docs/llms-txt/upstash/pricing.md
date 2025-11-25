# Source: https://upstash.com/docs/workflow/pricing.md

# Source: https://upstash.com/docs/vector/overall/pricing.md

# Source: https://upstash.com/docs/search/overall/pricing.md

# Source: https://upstash.com/docs/redis/overall/pricing.md

# Source: https://upstash.com/docs/qstash/overall/pricing.md

# Source: https://upstash.com/docs/workflow/pricing.md

# Source: https://upstash.com/docs/vector/overall/pricing.md

# Source: https://upstash.com/docs/search/overall/pricing.md

# Source: https://upstash.com/docs/redis/overall/pricing.md

# Source: https://upstash.com/docs/qstash/overall/pricing.md

# Source: https://upstash.com/docs/workflow/pricing.md

# Source: https://upstash.com/docs/vector/overall/pricing.md

# Source: https://upstash.com/docs/search/overall/pricing.md

# Source: https://upstash.com/docs/redis/overall/pricing.md

# Source: https://upstash.com/docs/qstash/overall/pricing.md

# Source: https://upstash.com/docs/workflow/pricing.md

# Pricing

Upstash Workflow is based on QStash and uses a "pay-as-you-go" pricing model. You only incur costs when your app receives traffic, meaning there's no charge when it's not in use. Click [here](https://upstash.com/pricing/workflow) to view the pricing.

A workflow run consists of several QStash messages, with the total cost determined by the number of messages used.

You can track your current message usage and associated costs in the [Overview tab of the console](https://console.upstash.com/qstash?tab=details).

<Frame>
  <img src="https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=87f8e5ad70e6b84bf131fe4d681ea33d" data-og-width="1962" width="1962" data-og-height="956" height="956" data-path="img/qstash/message_cost.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=280&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=847ec477e510538e4b832fd60f48e78b 280w, https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=560&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=90552de39d3caf419425a3b22bae650c 560w, https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=840&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=ed22633e5fe15edca00a02ec3388e46a 840w, https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=1100&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=45e43cc65aeae17a139596e0e6313eff 1100w, https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=1650&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=402d24ff3531ddcfdcf7d81261b82c96 1650w, https://mintcdn.com/upstash/P7f-vmkf9yuOavEy/img/qstash/message_cost.png?w=2500&fit=max&auto=format&n=P7f-vmkf9yuOavEy&q=85&s=b10ff096e02b745252e5229afbae3cc3 2500w" />
</Frame>

For detailed pricing information based on different plans, visit our [Workflow pricing page](https://upstash.com/pricing/workflow).

### Message Usage per Workflow Run

* [context.run](/workflow/basics/context#context-run), [context.sleep](/workflow/basics/context#context-sleep), [context.sleepUntil](/workflow/basics/context#context-sleepuntil), or [context.waitForEvent](/workflow/basics/context#context-waitforevent) commands generate a single message.
* The [context.call](/workflow/basics/context#context-call) command generates two messages.
* Each step in a [parallel run](/workflow/howto/parallel-runs) costs 1 extra message.
* If the workflow endpoint or URL in [context.call](/workflow/basics/context#context-call) returns an error or is unreachable, the workflow SDK will retry the call (up to 3 times by default). Each retry counts as a new message.
