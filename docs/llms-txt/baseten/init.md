# Source: https://docs.baseten.co/reference/cli/truss/init.md

# truss init

> Create a new Truss.

```
truss init [OPTIONS] TARGET_DIRECTORY
```

## Options

<ParamField body="-b, --backend" type="TrussServer|TGI|VLLM">
  What type of server to create. Default: `TrussServer`.
</ParamField>

<ParamField body="-n, --name" type="STRING">
  The value assigned to `model_name` in `config.yaml`.
</ParamField>

<ParamField body="--help">
  Show help message and exit.
</ParamField>

## Arguments

<ParamField body="TARGET_DIRECTORY" type="str">
  A Truss is created in this directory.
</ParamField>

## Example

```
truss init my_truss_directory
```

```
truss init --name "My Truss" my_truss_directory
```
