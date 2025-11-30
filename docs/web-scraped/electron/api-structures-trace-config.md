# Source: https://www.electronjs.org/docs/latest/api/structures/trace-config

# TraceConfig Object

- `recording_mode` string (optional) - Can be `record-until-full`, `record-continuously`, `record-as-much-as-possible` or `trace-to-console`. Defaults to `record-until-full`.
- `trace_buffer_size_in_kb` number (optional) - maximum size of the trace recording buffer in kilobytes. Defaults to 100MB.
- `trace_buffer_size_in_events` number (optional) - maximum size of the trace recording buffer in events.
- `enable_argument_filter` boolean (optional) - if true, filter event data according to a specific list of events that have been manually vetted to not include any PII. See [the implementation in Chromium](https://chromium.googlesource.com/chromium/src/+/main/services/tracing/public/cpp/trace_event_args_allowlist.cc) for specifics.
- `included_categories` string\[\] (optional) - a list of tracing categories to include. Can include glob-like patterns using `*` at the end of the category name. See [tracing categories](https://chromium.googlesource.com/chromium/src/+/main/base/trace_event/builtin_categories.h) for the list of categories.
- `excluded_categories` string\[\] (optional) - a list of tracing categories to exclude. Can include glob-like patterns using `*` at the end of the category name. See [tracing categories](https://chromium.googlesource.com/chromium/src/+/main/base/trace_event/builtin_categories.h) for the list of categories.
- `included_process_ids` number\[\] (optional) - a list of process IDs to include in the trace. If not specified, trace all processes.
- `histogram_names` string\[\] (optional) - a list of [histogram](https://chromium.googlesource.com/chromium/src.git/+/HEAD/tools/metrics/histograms/README.md) names to report with the trace.
- `memory_dump_config` Record\<string, any\> (optional) - if the `disabled-by-default-memory-infra` category is enabled, this contains optional additional configuration for data collection. See the [Chromium memory-infra docs](https://chromium.googlesource.com/chromium/src/+/main/docs/memory-infra/memory_infra_startup_tracing.md#the-advanced-way) for more information.

An example TraceConfig that roughly matches what Chrome DevTools records:

``` 

```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/structures/trace-config.md)