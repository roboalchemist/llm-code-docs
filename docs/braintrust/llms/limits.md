# Source: https://braintrust.dev/docs/reference/limits.md

> ## Documentation Index
> Fetch the complete documentation index at: https://braintrust.dev/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Limits

> General limits per plan and platform-wide system limits

## General limits

Usage quotas determine how much data you can log, score, and retain based on your pricing plan. Exceeding these quotas requires upgrading your plan or paying for additional usage.

<Tip>
  For detailed pricing and to estimate your monthly costs, see [Pricing](https://www.braintrust.dev/pricing).
</Tip>

| Limit                                                                                                                                                                                                                                                                                                       | Free              | Pro                                   | Enterprise |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | ------------------------------------- | ---------- |
| <Tooltip tip="The fundamental units of observability in your logged traces. Each span represents a discrete operation in your application like an LLM call, prompt rendering, or evaluation step." cta="Logs" href="/observe/view-logs">Trace spans</Tooltip>                                               | 1,000,000 / month | Unlimited                             | Custom     |
| <Tooltip tip="The total bytes of data ingested across logs, experiments, and datasets. Includes inputs, outputs, prompts, metadata, traces and spans, datasets, attachments, and any other related information." href="/observe/view-logs">Processed data</Tooltip>                                         | 1 GB / month      | 5 GB / month<br />(\$3/GB after)      | Custom     |
| <Tooltip tip="The number of evaluation scores recorded across offline and online evaluations." cta="Scorers" href="/evaluate/write-scorers">Scores</Tooltip>                                                                                                                                                | 10,000 / month    | 50,000 / month<br />(\$1.50/1k after) | Custom     |
| <Tooltip tip="How long logs, experiments, and traces are stored before automatic deletion. After this period, data is permanently removed unless you configure custom retention policies." cta="Configure retention" href="/admin/automations/data-management#configure-retention">Data retention</Tooltip> | 14 days           | 1 month<br />(\$3/GB retained after)  | Custom     |

## System limits

System limits include rate limits and other technical constraints that apply to all users regardless of plan. These limits ensure platform stability, prevent timeouts, and maintain performance for everyone.

<Note>
  [Self-hosted customers](/admin/self-hosting) can adjust some system limits. [Contact Braintrust](mailto:support@braintrust.dev) for details.
</Note>

| Limit                                                                                                                                                                                                                                                                                                          | Value                         |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
| <Tooltip tip="This rate limit applies to API calls that execute prompts, scorers, tools, and other custom code functions. Exceeding this limit returns an HTTP 429 error response." cta="Functions" href="/deploy/functions">Function executions</Tooltip>                                                     | 100 operations per 10 seconds |
| <Tooltip tip="Git metadata helps track which code version generated experiment results. Git metadata larger than this is truncated. This affects only the metadata attached to experiments, not your actual data." cta="Configure" href="/admin/organizations#set-git-metadata-logging">Git metadata</Tooltip> | 64 KB maximum                 |
| <Tooltip tip="SQL/BTQL queries to analyze logs, experiments, datasets, etc." cta="SQL reference" href="/reference/sql">Query timeout</Tooltip>                                                                                                                                                                 | 30 seconds                    |
| <Tooltip tip="Custom code written directly in Braintrust (prompts, scorers, tools) for simple, self-contained logic without external dependencies.">Inline code function timeout</Tooltip>                                                                                                                     | 240 seconds (4 minutes)       |
| <Tooltip tip="Custom code uploaded with dependencies and external libraries for more complex functions that require npm packages, pip packages, etc.">Bundled code function timeout</Tooltip>                                                                                                                  | 30 seconds (by default)       |
| <Tooltip tip="Signed URLs for uploading or downloading attachments (images, audio, files) expire after 24 hours. Attachments remain stored permanently; only the access URLs expire." cta="Attachments" href="/instrument/attachments">Attachment URL expiration</Tooltip>                                     | 1 day                         |
