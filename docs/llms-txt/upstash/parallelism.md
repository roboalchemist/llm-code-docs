# Source: https://upstash.com/docs/workflow/features/flow-control/parallelism.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Parallelism

The parallelism limit controls the maximum number of calls that can be executed concurrently.
Unlike rate limiting (which works per time window), parallelism enforces concurrency control with a token-based system.

```typescript Configure Retry Attempt Count theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  flowControl: {
    key: "user-signup",
    parallelism: 10,
  }
})
```

**Example**:
If `parallelism = 3`, at most 3 requests can run concurrently.

When tokens are available, requests acquire one and start execution:

<Frame caption="A failing step is automatically retried three times">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=33f44e2266b0d43208369e82f8e61553" data-og-width="2342" width="2342" data-og-height="1126" height="1126" data-path="img/workflow/parallelism_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=008ec116f9e04594fa858e425c27fec0 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=dd4f3549250155403b639dc2d057c460 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=6654cd13e6065d0c88b258b03619bf85 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=c56a93e6e50fb5320b4592307fab8247 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=376ac3452ec940edcf08b08818d33a5c 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_1.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d4df5ca83676cacbe16447f6b1a20a36 2500w" />
</Frame>

When all tokens are in use, additional requests are not failed — they’re queued in a **waitlist**:

<Frame caption="A failing step is automatically retried three times">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=9ab65cc92230f2b03e40fb7743887aea" data-og-width="2342" width="2342" data-og-height="1126" height="1126" data-path="img/workflow/parallelism_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=af67f3f0cc95401d6bf5a0f59a1561a0 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=b4a72c08bd218232155931064aed17bd 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=8bb78014f2abf6529283605d2d288695 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=f001934c7f0993919bd60023593921f8 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=2d3471320aebf7d6550f7665f852f5dd 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_2.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=5fd70480fd5bdc5877784273a2d4e3f8 2500w" />
</Frame>

The step in the waitlist will wait for a step to complete and hand off it's token to a pending request:

<Tip>
  Token handoff does not guarantee strict ordering.
  A later request in the waitlist may acquire a token before an earlier one.
</Tip>

<Frame caption="A failing step is automatically retried three times">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=e9d284cf4ed9a0a8fcbe20f1cdefbedf" data-og-width="2342" width="2342" data-og-height="1126" height="1126" data-path="img/workflow/parallelism_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=cea665805f66c25cd546f71faddf26c8 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=1eddc37c697205d2502a9e8365410fd5 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=6f3c09fffa80698a3a0f308563e60401 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=b669d35cb7827b3de34c934b9777be35 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=10623e574cbe4312d1351f525e013ccd 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/parallelism_3.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=19fc76d5912e823bfa437217c7492c1d 2500w" />
</Frame>
