# Source: https://docs.replit.com/billing/deployment-pricing.md

# Publishing costs

> Flexible publishing costs that scale with your app's needs. Pay only for what you use with transparent, credit-based billing.

export const AiPrompt = ({children}) => {
  return <CodeBlock className="relative block font-sans whitespace-pre-wrap break-words">
      <div className="pr-7">
        {children}
      </div>
    </CodeBlock>;
};

export const StaticDeploymentOutboundPerGiB = '$0.10';

export const DedicatedLargeVm = '$160.00';

export const DedicatedMediumVm = '$80.00';

export const DedicatedSmallVm = '$40.00';

export const SharedMediumVm = '$20.00';

export const ScheduledDeployment = '$1.00';

export const SchedulerPrice = '$0.00';

export const ScheduledComputeUnit = '$3.20';

export const AutoscaleDeployment = '$1.00';

export const AutoscaleRequests = '$1.20';

export const AutoscaleComputeUnit = '$3.20';

export const AutoscaleBaseFee = '$1';

export const TeamsCredits = '$40';

export const CoreCredits = '$25';

Replit's publishing costs are designed to scale with your app's needs. Choose from usage-based billing that charges only when your app serves requests, or predictable flat-rate options for consistent workloads.

## How billing works

All publishing costs are deducted from your monthly credits. You only pay usage-based fees after your monthly credits are fully used.

* **[Core Plan](/replit-core/replit-core)**: Includes {CoreCredits} in monthly credits
* **[Teams Plan](/category/teams)**: Includes {TeamsCredits} in monthly credits per member

<Note>
  Credits apply automatically to all publishing costs. Unused credits don't roll
  over to the next month. Learn more about [usage-based
  billing](/billing/about-usage-based-billing).
</Note>

For a hands-on understanding of publishing costs, explore our [interactive pricing calculator](https://deployment-pricing.replit.app/).

<Frame>
  <img src="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=e91449a14d21dc9680cfb524702852c3" alt="Interactive publishing costs calculator showing cost breakdown by deployment type" data-og-width="2540" width="2540" data-og-height="990" height="990" data-path="images/deployments/deployments-cost.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=280&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5d79f7c00d195fe481df4197c1867fb7 280w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=560&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=5ecf550304f8d9f39b8ae03f27dc60e9 560w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=840&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=01bbd5fab3d8098fc605be5a73f1c2c2 840w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=1100&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=138e09ad99ac5716e399baf00e2b6871 1100w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=1650&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=e611a7f721cc13307ea70791ac8aaa39 1650w, https://mintcdn.com/replit/jSmYU1wBTvl8UMyc/images/deployments/deployments-cost.png?w=2500&fit=max&auto=format&n=jSmYU1wBTvl8UMyc&q=85&s=2e0d156879229e9ae632f9df280fc8a2 2500w" />
</Frame>

## Deployment types

Choose the deployment type that best fits your app's traffic patterns and resource needs.

<AccordionGroup>
  <Accordion title="Autoscale Deployments" icon="arrows-up-down">
    Perfect for apps with variable traffic. Pay only when your app serves requests—nothing when idle.

    **Best for:** Web apps, APIs, and services with unpredictable traffic patterns

    [Learn more about Autoscale Deployments](/cloud-services/deployments/autoscale-deployments)
  </Accordion>

  <Accordion title="Reserved VM Deployments" icon="server">
    **Predictable monthly costs with dedicated resources**

    Guaranteed compute resources that run continuously. Choose shared or dedicated VMs based on your performance needs.

    **Best for:** Production apps with steady traffic or guaranteed resource requirements

    [Learn more about Reserved VM Deployments](/cloud-services/deployments/reserved-vm-deployments)
  </Accordion>

  <Accordion title="Scheduled Deployments" icon="clock">
    **Cost-effective for background tasks and automation**

    Run code on a schedule without maintaining persistent infrastructure.

    **Best for:** Background jobs, data processing, and automated tasks

    [Learn more about Scheduled Deployments](/cloud-services/deployments/scheduled-deployments)
  </Accordion>

  <Accordion title="Static Deployments" icon="globe">
    **Minimal costs for static content with global distribution**

    Publish static sites with CDN distribution and pay only for data transfer.

    **Best for:** Documentation sites, portfolios, and single-page applications

    [Learn more about Static Deployments](/cloud-services/deployments/static-deployments)
  </Accordion>
</AccordionGroup>

## Understanding request-based billing

<Tip>
  With Autoscale Deployments, you only pay when your app is actively working.
  When no one visits your app, you pay nothing.
</Tip>

Autoscale Deployments use request-based billing—you're charged only when your app serves traffic. Here's how it works:

1. **App starts up** when the first request arrives (if idle)
2. **Processes the request** using compute resources
3. **Goes idle** after 15 minutes of inactivity

**Billing time:** Often just 1-2 seconds per request, even for complex apps.

### Request-based Billing Timeline

When no one visits your app, you pay nothing. When your app is busy, you pay for the compute resources used.

Here's a timeline of what happens when someone visits your app:

<p className="text-center"> Request-based Billing Timeline </p>

<div className="grid grid-cols-[80px_1fr] gap-4 items-center">
  <div className="text-right text-sm">
    Instance
  </div>

  <div className="h-8 bg-gray-100 dark:bg-gray-800 rounded-md relative">
    <div className="absolute top-0.5 h-7 rounded bg-gray-200 dark:bg-gray-700 flex items-center justify-center text-xs text-gray-600 dark:text-gray-400" style={{ left: '13%', width: '77%' }}>
      Running
    </div>
  </div>

  <div className="text-right text-sm">Requests</div>

  <div className="h-8 bg-gray-100 dark:bg-gray-800 rounded-md relative">
    <div className="absolute top-0.5 h-3 rounded bg-blue-600" style={{ left: "15%", width: "12%" }} />

    <div className="absolute top-0.5 h-3 rounded bg-blue-600" style={{ left: "40%", width: "12%" }} />

    <div className="absolute top-4 h-3 rounded bg-blue-600" style={{ left: "46%", width: "12%" }} />

    <div className="absolute top-0.5 h-3 rounded bg-blue-600" style={{ left: "70%", width: "12%" }} />

    <div className="absolute top-4 h-3 rounded bg-blue-600" style={{ left: "76%", width: "12%" }} />
  </div>

  <div className="text-right text-sm">
    Billable
  </div>

  <div className="h-8 bg-gray-100 dark:bg-gray-800 rounded-md relative">
    <div className="absolute top-0.5 h-7 rounded bg-green-600" style={{ left: '15%', width: '12%' }} />

    <div className="absolute top-0.5 h-7 rounded bg-green-600" style={{ left: '40%', width: '18%' }} />

    <div className="absolute top-0.5 h-7 rounded bg-green-600" style={{ left: '70%', width: '18%' }} />
  </div>
</div>

<div className="grid grid-cols-[80px_1fr] gap-6 mt-2">
  <div />

  <div className="relative text-xs text-gray-500 dark:text-gray-400">
    <span className="absolute" style={{ left: "12%" }}>
      Started
    </span>

    <span className="absolute" style={{ left: "83%" }}>
      Stopped
    </span>
  </div>
</div>

First, the server starts up. Then, it processes the requests. Finally, it goes idle. You only pay for CPU and memory during request processing.

<Note>
  When multiple requests arrive simultaneously (like the stacked blue bars), they share the same compute resources.

  Your billing time extends to cover all concurrent requests, but you don't pay separately for each—just for the total time the server is working.
</Note>

The gaps between green bars represent cost savings during idle time. At the end of the session, the server shuts down.

### Compute units explained

Compute units measure the computational work your app performs:

* **CPU time**: Processing power used (1 CPU second = 18 compute units)
* **Memory time**: RAM consumed (1 GB-second = 2 compute units)
* **Duration**: How long your app works on each request

## Pricing breakdown

<AccordionGroup>
  <Accordion title="Autoscale Deployments" icon="arrows-up-down">
    Pay only when your app serves requests. Automatically scales based on demand.

    | Component                             |                  Price |
    | :------------------------------------ | ---------------------: |
    | **Base fee** (per month)              |     {AutoscaleBaseFee} |
    | **Compute units** (per million units) | {AutoscaleComputeUnit} |
    | **Requests** (per million requests)   |    {AutoscaleRequests} |
  </Accordion>

  <Accordion title="Scheduled Deployments" icon="clock">
    Execute background tasks and scheduled jobs.

    | Component                             |                  Price |
    | :------------------------------------ | ---------------------: |
    | **Base fee** (per month)              |  {ScheduledDeployment} |
    | **Compute units** (per million units) | {ScheduledComputeUnit} |
    | **Scheduler**                         |       {SchedulerPrice} |
  </Accordion>

  <Accordion title="Reserved VM Deployments" icon="server">
    Dedicated compute resources with predictable monthly costs.

    #### Shared VMs

    | Configuration | Price (per month) |
    | :------------ | ----------------: |

    \| **0.5 vCPU / 2GB RAM** | {SharedMediumVm} |

    #### Dedicated VMs

    | Configuration         |   Price (per month) |
    | :-------------------- | ------------------: |
    | **1 vCPU / 4GB RAM**  |  {DedicatedSmallVm} |
    | **2 vCPU / 8GB RAM**  | {DedicatedMediumVm} |
    | **4 vCPU / 16GB RAM** |  {DedicatedLargeVm} |
  </Accordion>

  <Accordion title="Static Deployments" icon="globe">
    Host static sites with global CDN distribution.

    | Component                  |                            Price |
    | :------------------------- | -------------------------------: |
    | **Hosting**                |                             Free |
    | **Data transfer** (per GB) | {StaticDeploymentOutboundPerGiB} |
  </Accordion>
</AccordionGroup>

## Cost examples by app type

These examples show realistic costs for different types of applications.

<AccordionGroup>
  <Accordion title="Personal blog" icon="browser">
    **Traffic:** 50 visitors/day, 3 page views each = 4,500 requests/month

    | Component         | Usage        |               Cost |
    | :---------------- | :----------- | -----------------: |
    | **Base fee**      | Monthly      | {AutoscaleBaseFee} |
    | **Compute units** | 13,500 units |           \~\$0.04 |
    | **Requests**      | 4,500        |           \~\$0.01 |
    | **Total**         |              |       **\~\$1.05** |
  </Accordion>

  <Accordion title="Small business website" icon="browser">
    **Traffic:** 500 visitors/day, 5 page views each = 75,000 requests/month

    | Component         | Usage         |               Cost |
    | :---------------- | :------------ | -----------------: |
    | **Base fee**      | Monthly       | {AutoscaleBaseFee} |
    | **Compute units** | 600,000 units |           \~\$1.92 |
    | **Requests**      | 75,000        |           \~\$0.15 |
    | **Total**         |               |       **\~\$3.07** |
  </Accordion>

  <Accordion title="API service" icon="gear">
    **Traffic:** 10,000 API calls/day = 300,000 requests/month

    | Component         | Usage       |               Cost |
    | :---------------- | :---------- | -----------------: |
    | **Base fee**      | Monthly     | {AutoscaleBaseFee} |
    | **Compute units** | 3.96M units |          \~\$12.67 |
    | **Requests**      | 300,000     |           \~\$0.60 |
    | **Total**         |             |      **\~\$14.27** |
  </Accordion>

  <Accordion title="Background processing job" icon="clock">
    **Usage:** Daily data processing with Scheduled Deployments

    | Component                | Usage        |                  Cost |
    | :----------------------- | :----------- | --------------------: |
    | **Scheduled deployment** | Base fee     | {ScheduledDeployment} |
    | **Compute units**        | 50,000 units |              \~\$0.16 |
    | **Total**                |              |          **\~\$1.16** |
  </Accordion>
</AccordionGroup>

## Monitor and control costs

<CardGroup cols={2}>
  <Card title="Set spending controls" icon="shield" href="/billing/managing-spend">
    Configure spending alerts and budgets to prevent unexpected charges.
  </Card>

  <Card title="Monitor usage" icon="chart-bar" href="https://replit.com/usage">
    Track real-time consumption and costs in your Usage dashboard.
  </Card>

  <Card title="Learn about AI billing" icon="brain" href="/billing/ai-billing">
    Understand how [Agent](/replitai/agent) and [Assistant](/replitai/assistant)
    affect your bill.
  </Card>

  <Card title="Monitor published apps" icon="chart-line" href="/cloud-services/deployments/monitoring-a-deployment">
    View logs, track performance, and monitor published app status.
  </Card>
</CardGroup>
