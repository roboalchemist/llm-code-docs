# Source: https://docs.vllm.ai/en/stable/cli/bench/sweep/serve/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/sweep/serve.md "Edit this page")

# vllm bench sweep serve[¶](#vllm-bench-sweep-serve "Permanent link")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

-   `--json-arg '}'`
-   `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

-   `--json-arg ''`
-   `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--serve-cmd`[¶](#-serve-cmd "Permanent link") 

The command used to run the server: `vllm serve ...`

Default: `None`

#### `--bench-cmd`[¶](#-bench-cmd "Permanent link") 

The command used to run the benchmark: `vllm bench serve ...`

Default: `None`

#### `--after-bench-cmd`[¶](#-after-bench-cmd "Permanent link") 

After a benchmark run is complete, invoke this command instead of the default `ServerWrapper.clear_cache()`.

Default: `None`

#### `--show-stdout`[¶](#-show-stdout "Permanent link") 

If set, logs the standard output of subcommands. Useful for debugging but can be quite spammy.

Default: `False`

#### `--serve-params`[¶](#-serve-params "Permanent link") 

Path to JSON file containing parameter combinations for the `vllm serve` command. Can be either a list of dicts or a dict where keys are benchmark names. If both `serve_params` and `bench_params` are given, this script will iterate over their Cartesian product.

Default: `None`

#### `--bench-params`[¶](#-bench-params "Permanent link") 

Path to JSON file containing parameter combinations for the `vllm bench serve` command. Can be either a list of dicts or a dict where keys are benchmark names. If both `serve_params` and `bench_params` are given, this script will iterate over their Cartesian product.

Default: `None`

#### `-o`, `--output-dir`[¶](#-o-output-dir "Permanent link") 

The directory to which results are written.

Default: `results`

#### `--num-runs`[¶](#-num-runs "Permanent link") 

Number of runs per parameter combination.

Default: `3`

#### `--dry-run`[¶](#-dry-run "Permanent link") 

If set, prints the commands to run, then exits without executing them.

Default: `False`

#### `--resume`[¶](#-resume "Permanent link") 

Set this to the name of a directory under `output_dir` (which is a timestamp) to resume a previous execution of this script, i.e., only run parameter combinations for which there are still no output files.

Default: `None`

#### `--link-vars`[¶](#-link-vars "Permanent link") 

Comma-separated list of linked variables between serve and bench, e.g. max_num_seqs=max_concurrency,max_model_len=random_input_len

Default: `""`

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 15, 2025] ]