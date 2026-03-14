# Source: https://novita.ai/docs/guides/sandbox-console.md

> ## Documentation Index
> Fetch the complete documentation index at: https://novita.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Agent Sandbox Console

Agent Sandbox console helps you view and manage sandboxes, templates, and usage statistics.

## Sandbox Management

* Display the list of currently running sandboxes.
* Support searching for a sandbox by ID.
* Support filtering sandboxes by creation time, template, vCPUs, memory, etc.

<Frame>
  <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/sandbox-console-sbx.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=666d0d76871e84223e6ad103d0ea0a7a" alt="Sandbox Management" width="1200" data-path="guides/images/sandbox-console-sbx.png" />
</Frame>

## Template Management

* Display the list of available templates, including official templates provided by Novita official and your [custom templates](/guides/sandbox-template).
* Support searching for a template by ID.
* Support filtering templates by visibility (public, private, or all), vCPUs, and memory.

<Frame>
  <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/sandbox-console-template.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=871b288b80b453634576fc1d5d395c96" alt="Sandbox Management" width="1200" data-path="guides/images/sandbox-console-template.png" />
</Frame>

## Usage Statistics

Console provides daily resource usage and cost analysis to help you monitor your consumption and optimize your usage.

* **vCPU Hours**
  * Display the total vCPU usage time for all sandboxes on the current day (unit: hours).
  * This data can be accurate to the second, and can be used to evaluate the current computing resource usage.

* **Memory Hours**
  * Display the total memory usage time for all sandboxes on the current day (unit: GB·hours).
  * The system calculates the memory allocation and usage time for each sandbox during runtime.

* **Usage Costs**
  * Display the total cost of resources on the current day (unit: USD).
  * Includes the total cost of all vCPUs and memory. The storage space and templates are currently free to use.

<Tip>
  - All resources are billed by the second, and displayed in daily granularity.
  - The chart shows the trend of the past 30 days, which can be used to monitor the trend of usage changes.
  - This data may not include the latest usage, which may be slightly different from the bill. The final settlement is based on the <Link href="https://novita.ai/billing/details" target="_blank">billing details</Link> page.
</Tip>

<Frame>
  <img src="https://mintcdn.com/novitaai/H3Kjvdvlhgt0Aohj/guides/images/sandbox-console-usage.png?fit=max&auto=format&n=H3Kjvdvlhgt0Aohj&q=85&s=d84389096cf07b5d7289164dfcde8eb0" alt="Sandbox Management" width="1200" data-path="guides/images/sandbox-console-usage.png" />
</Frame>


Built with [Mintlify](https://mintlify.com).