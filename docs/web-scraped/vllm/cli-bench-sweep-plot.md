# Source: https://docs.vllm.ai/en/stable/cli/bench/sweep/plot/

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEwIDIwSDZWNGg3djVoNXYzLjFsMi0yVjhsLTYtNkg2Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDR6bTEwLjItN2MuMSAwIC4zLjEuNC4ybDEuMyAxLjNjLjIuMi4yLjYgMCAuOGwtMSAxLTIuMS0yLjEgMS0xYy4xLS4xLjItLjIuNC0uMm0wIDMuOUwxNC4xIDIzSDEydi0yLjFsNi4xLTYuMXoiPjwvcGF0aD48L3N2Zz4=)](https://github.com/vllm-project/vllm/edit/main/docs/cli/bench/sweep/plot.md "Edit this page")

# vllm bench sweep plot[¶](#vllm-bench-sweep-plot "Permanent link")

## JSON CLI Arguments[¶](#json-cli-arguments "Permanent link")

When passing JSON CLI arguments, the following sets of arguments are equivalent:

-   `--json-arg '}'`
-   `--json-arg.key1 value1 --json-arg.key2.key3 value2`

Additionally, list elements can be passed individually using `+`:

-   `--json-arg ''`
-   `--json-arg.key4+ value3 --json-arg.key4+='value4,value5'`

## Arguments[¶](#arguments "Permanent link")

#### `--fig-dir`[¶](#-fig-dir "Permanent link") 

The directory to save the figures, relative to `OUTPUT_DIR`. By default, the same directory is used.

Default: `""`

#### `--fig-by`[¶](#-fig-by "Permanent link") 

A comma-separated list of variables, such that a separate figure is created for each combination of these variables.

Default: `""`

#### `--row-by`[¶](#-row-by "Permanent link") 

A comma-separated list of variables, such that a separate row is created for each combination of these variables.

Default: `""`

#### `--col-by`[¶](#-col-by "Permanent link") 

A comma-separated list of variables, such that a separate column is created for each combination of these variables.

Default: `""`

#### `--curve-by`[¶](#-curve-by "Permanent link") 

A comma-separated list of variables, such that a separate curve is created for each combination of these variables.

Default: `None`

#### `--var-x`[¶](#-var-x "Permanent link") 

The variable for the x-axis.

Default: `request_throughput`

#### `--var-y`[¶](#-var-y "Permanent link") 

The variable for the y-axis

Default: `p99_e2el_ms`

#### `--filter-by`[¶](#-filter-by "Permanent link") 

A comma-separated list of statements indicating values to filter by. This is useful to remove outliers. Example: `max_concurrency<1000,max_num_batched_tokens<=4096` means plot only the points where `max_concurrency` is less than 1000 and `max_num_batched_tokens` is no greater than 4096.

Default: `""`

#### `--bin-by`[¶](#-bin-by "Permanent link") 

A comma-separated list of statements indicating values to bin by. This is useful to avoid plotting points that are too close together. Example: `request_throughput%%1` means use a bin size of 1 for the `request_throughput` variable.

Default: `""`

#### `--scale-x`[¶](#-scale-x "Permanent link") 

The scale to use for the x-axis. Currently only accepts string values such as \'log\' and \'sqrt\'. See also: https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html

Default: `None`

#### `--scale-y`[¶](#-scale-y "Permanent link") 

The scale to use for the y-axis. Currently only accepts string values such as \'log\' and \'sqrt\'. See also: https://seaborn.pydata.org/generated/seaborn.objects.Plot.scale.html

Default: `None`

#### `--fig-name`[¶](#-fig-name "Permanent link") 

Name prefix for the output figure file. Group data is always appended when present. Default: \'FIGURE\'. Example: \--fig-name my_performance_plot

Default: `FIGURE`

#### `--no-error-bars`[¶](#-no-error-bars "Permanent link") 

If set, disables error bars on the plot. By default, error bars are shown.

Default: `False`

#### `--fig-height`[¶](#-fig-height "Permanent link") 

Height of each subplot in inches. Default: 6.4

Default: `6.4`

#### `--fig-dpi`[¶](#-fig-dpi "Permanent link") 

Resolution of the output figure in dots per inch. Default: 300

Default: `300`

#### `--dry-run`[¶](#-dry-run "Permanent link") 

If set, prints the information about each figure to plot, then exits without drawing them.

Default: `False`

[ [ ![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdib3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTIxIDEzLjFjLS4xIDAtLjMuMS0uNC4ybC0xIDEgMi4xIDIuMSAxLTFjLjItLjIuMi0uNiAwLS44bC0xLjMtMS4zYy0uMS0uMS0uMi0uMi0uNC0uMm0tMS45IDEuOC02LjEgNlYyM2gyLjFsNi4xLTYuMXpNMTIuNSA3djUuMmw0IDIuNC0xIDFMMTEgMTNWN3pNMTEgMjEuOWMtNS4xLS41LTktNC44LTktOS45QzIgNi41IDYuNSAyIDEyIDJjNS4zIDAgOS42IDQuMSAxMCA5LjMtLjMtLjEtLjYtLjItMS0uMnMtLjcuMS0xIC4yQzE5LjYgNy4yIDE2LjIgNCAxMiA0Yy00LjQgMC04IDMuNi04IDggMCA0LjEgMy4xIDcuNSA3LjEgNy45bC0uMS4yeiI+PC9wYXRoPjwvc3ZnPg==) ] [November 15, 2025] ]