# Source: https://docs.vllm.ai/en/stable/cli/bench/sweep/plot_pareto/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/sweep/plot_pareto.md "Edit this page")

# vllm bench sweep plot_pareto[¶](#vllm-bench-sweep-plot_pareto "Permanent link")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

-   `--json-arg '}'`
-   `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

-   `--json-arg ''`
-   `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--user-count-var`[¶](#-user-count-var "Permanent link") 

Result key that stores concurrent user count. Falls back to max_concurrent_requests if missing.

Default: `max_concurrency`

#### `--gpu-count-var`[¶](#-gpu-count-var "Permanent link") 

Result key that stores GPU count. If not provided, falls back to num_gpus/gpu_count or tensor_parallel_size \* pipeline_parallel_size.

Default: `None`

#### `--label-by`[¶](#-label-by "Permanent link") 

Comma-separated list of fields to annotate on Pareto frontier points.

Default: `max_concurrency,gpu_count`

#### `--dry-run`[¶](#-dry-run "Permanent link") 

If set, prints the figures to plot without drawing them.

Default: `False`

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 28, 2025] ]