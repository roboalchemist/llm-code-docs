# Source: https://docs.baseten.co/reference/cli/truss/run-python.md

# truss run-python

> Subcommands for truss run-python.

```
truss run-python [OPTIONS] SCRIPT [TARGET_DIRECTORY]
```

Runs selected script in the same environment as your Truss. It builds a Docker
image matching your Truss environment, mounts the script you supply, and then
runs the script.

### Options

<ParamField body="--help">
  Show help message and exit.
</ParamField>

### Arguments

<ParamField body="SCRIPT" type="Required">
  Path to Python script to run.
</ParamField>

<ParamField body="TARGET_DIRECTORY" type="Optional">
  A Truss directory. If none, use current directory.
</ParamField>
