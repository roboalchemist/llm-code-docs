# nsc list

Display all instances in your current workspace.

## Basic Usage

```bash
nsc list [-o <plain|json>]
```

## Description

Print the list of all your instances from the current workspace where you're logged in.

## Output Information

The command generates a table with:

- Instance ID
- CPU and memory allocation
- Architecture (amd64 or arm64)
- Creation timestamp
- Time-to-live remaining
- Instance purpose/origin

## Example Output

Running `nsc list` produces a formatted table showing instances with details like:

- A manually created instance with 4 CPUs and 4 GiB memory
- A GitHub Actions build machine with 16 CPUs and 32 GiB memory
- Development instances with various specifications

## Options

**-o <type>**: Control output format

- `plain` (default): Human-readable table format
- `json`: Machine-readable format with extended details

The JSON output includes additional metadata like cluster IDs, creation times, deadlines, Kubernetes distribution info, and GitHub workflow details when applicable.

## Example Usage

```bash
nsc list

nsc list -o plain

nsc list -o json
```
