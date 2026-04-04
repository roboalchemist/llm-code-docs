# Source: https://upstash.com/docs/workflow/features/flow-control/rate-period.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Rate and Period

The rate specifies the maximum number of requests allowed in a given period (time window).

```typescript Configure Retry Attempt Count theme={"system"}
import { Client } from "@upstash/workflow";

const client = new Client({ token: "<QSTASH_TOKEN>" })

const { workflowRunId } = await client.trigger({
  url: "https://<YOUR_WORKFLOW_ENDPOINT>/<YOUR-WORKFLOW-ROUTE>",
  flowControl: {
    key: "user-signup",
    rate: 10,
    period: 100,
  }
})
```

**Example**:
If `rate = 2` and `period = 1 minute`, then **a maximum of 2 steps** can be executed per minute.

The first 2 requests within the minute are executed immediately:

<Frame caption="Steps are executed within limit">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=416a2d089ba4026c18164a97375d69d9" data-og-width="2342" width="2342" data-og-height="848" height="848" data-path="img/workflow/rate_1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=4e3d0b9b731bc9ccad4632eaba183731 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=d861f5e56dede2b0e12af7af73ec8b94 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=434dd9eb6f00724d1bd3f10623fbe0b9 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=a9cb69cd57119b2f1fc7c5bdfc63e347 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=63dfa8c4a64ed57db37afc72e6fd121b 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_1.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=32aeff9c7f068699bc8f923711f68864 2500w" />
</Frame>

The 3rd request in the same minute is not executed immediately:

<Frame caption="A new step cannot execute immediately">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=bcf1550d87068c16aa182171bc240a97" data-og-width="2342" width="2342" data-og-height="848" height="848" data-path="img/workflow/rate_2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=22f471bf05f0bc97b183571a117dd13f 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=be6de86526d51e7f9d2a66f27aced226 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=7ac0a3ae87ca971aa992a24341d7b12d 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=4e93f27eab21f11943b2070a80970045 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=31622b3aa4c8b3d045a269208cdbfe47 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_2.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=27bfcc08a5afb8318141305805fb095a 2500w" />
</Frame>

Instead of rejecting it, Workflow schedules the request in the next available time window:

<Frame caption="The new step is moved to the next time window">
  <img src="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=cd597a831970d7fc7dd1a9af6be0e2a7" data-og-width="2342" width="2342" data-og-height="848" height="848" data-path="img/workflow/rate_3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=280&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=4131ef3ca8f884ec25c238351f3d8ff6 280w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=560&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=5fe76af569462d9c730fb478e9cc2301 560w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=840&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=9b2b574d1f5c513fae20559957862c2b 840w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=1100&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=a06a1e8a2cad1ea6be29ead79c01d8bc 1100w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=1650&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=46b7fb277625a24d63aebaabdd134c82 1650w, https://mintcdn.com/upstash/veMt3N2QLOAoUf0w/img/workflow/rate_3.png?w=2500&fit=max&auto=format&n=veMt3N2QLOAoUf0w&q=85&s=b89308e1ee820cb9fab082e923170eb7 2500w" />
</Frame>

Note that step executions may take longer than the defined period.
The rate limit only controls how many steps are **started** within each time window,
it does not limit their execution duration.
