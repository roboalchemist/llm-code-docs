# Source: https://docs.base44.com/developers/references/cli/commands/logs.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# logs

> View function logs

View logs from your [backend functions](/developers/backend/resources/backend-functions/overview) in the terminal. By default the command returns the 50 most recent log entries across all functions in your project. Use flags to filter by function name, time range, or adjust the number of results.

## Usage

```bash  theme={null}
base44 logs
```

This command must be run from your project directory. The CLI reads your `.app.jsonc` file to determine which app to fetch logs for. There's no flag to specify an app ID directly, so if you manage multiple projects, navigate to the correct one first.

## Flags

| Flag                 | Description                                                                                                  |
| -------------------- | ------------------------------------------------------------------------------------------------------------ |
| `--function <names>` | Filter by function name. Accepts a comma-separated list. If omitted, fetches logs for all project functions. |
| `--since <datetime>` | Show logs from this time onward. Accepts [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.          |
| `--until <datetime>` | Show logs up to this time. Accepts [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.                |
| `-n, --limit <n>`    | Maximum number of results to return, between `1` and `1000`. Defaults to `50`.                               |
| `--order <order>`    | Sort order: `asc` or `desc`. Defaults to `desc`.                                                             |

## Output format

The output is a list of log entries sorted by time.

Each entry shows the timestamp, level, function name in brackets, and log message. For example:

```
Showing 4 function log entries

2026-02-24 08:23:37 ERROR [send-email] Failed to deliver to user@example.com: connection timed out
2026-02-24 08:23:37 INFO  [send-email] Sending welcome email to user@example.com
2026-02-24 08:23:36 INFO  [process-order] Order #1042 processed successfully
2026-02-24 08:23:36 DEBUG [process-order] isolate start time: 350.47 ms (user time: 69.32 ms)
```

The log level reflects the console method used in your function code:

| Console method  | Log level |
| --------------- | --------- |
| `console.log`   | `INFO`    |
| `console.info`  | `INFO`    |
| `console.error` | `ERROR`   |
| `console.warn`  | `WARNING` |
| `console.debug` | `DEBUG`   |

The output also includes system-level entries from Deno Deploy, such as isolate startup times. The log level for these entries is assigned by Deno Deploy.

## See also

* [Backend Functions](/developers/backend/resources/backend-functions/overview): Learn about serverless functions
* [`deploy`](/developers/references/cli/commands/deploy): Deploy all project resources to Base44
* [`functions deploy`](/developers/references/cli/commands/functions-deploy): Deploy local functions to Base44


Built with [Mintlify](https://mintlify.com).