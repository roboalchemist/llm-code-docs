<!-- Source: https://namespace.so/docs/reference/cli/instance-history -->

# nsc instance history

History of your previous running instances.

`instance history` lists your previously created Namespace instances.

## Usage

```
nsc instance history [--since <duration>] [--label <key=value>]
```

### Example

```
$ nsc instance history
Instance ID      CPU  Memory    Arch    Created       Duration
85a32emcg99ii    4    16 GiB    arm64   2 hours ago   1h52m
h9am86n6gi25m    8    32 GiB    amd64   1 day ago     23h45m
```

## Options

### --output, -o <format>

Output format. One of `plain` or `json`. Default is `plain`.

### --label <key=value>

Constrain list to the specified labels.

### --since <duration>

Constrain list to the selected duration. Default is `168h` (7 days).

### --all

If set, return all instances, not just manually created ones.

### --max\_entries <count>

Maximum number of instances to return. Default is `100`.

Last updated February 13, 2026
