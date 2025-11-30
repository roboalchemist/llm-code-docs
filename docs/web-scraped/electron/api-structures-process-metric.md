# Source: https://www.electronjs.org/docs/latest/api/structures/process-metric

# ProcessMetric Object

- `pid` Integer - Process id of the process.
- `type` string - Process type. One of the following values:
  - `Browser`
  - `Tab`
  - `Utility`
  - `Zygote`
  - `Sandbox helper`
  - `GPU`
  - `Pepper Plugin`
  - `Pepper Plugin Broker`
  - `Unknown`
- `serviceName` string (optional) - The non-localized name of the process.
- `name` string (optional) - The name of the process. Examples for utility: `Audio Service`, `Content Decryption Module Service`, `Network Service`, `Video Capture`, etc.
- `cpu` [CPUUsage](/docs/latest/api/structures/cpu-usage) - CPU usage of the process.
- `creationTime` number - Creation time for this process. The time is represented as number of milliseconds since epoch. Since the `pid` can be reused after a process dies, it is useful to use both the `pid` and the `creationTime` to uniquely identify a process.
- `memory` [MemoryInfo](/docs/latest/api/structures/memory-info) - Memory information for the process.
- `sandboxed` boolean (optional) *macOS* *Windows* - Whether the process is sandboxed on OS level.
- `integrityLevel` string (optional) *Windows* - One of the following values:
  - `untrusted`
  - `low`
  - `medium`
  - `high`
  - `unknown`

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/process-metric.md)