# Source: https://docs.baseten.co/reference/cli/truss/init.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss init

> Create a new Truss project.

```sh  theme={"system"}
truss init [OPTIONS] TARGET_DIRECTORY
```

Creates a new Truss project in the specified directory with the standard file structure.

### Options

<ParamField body="-b, --backend" type="TrussServer | TRT_LLM">
  Server type to create. Default: `TrussServer`.
</ParamField>

<ParamField body="-n, --name" type="TEXT">
  The value assigned to `model_name` in `config.yaml`.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT" required>
  Directory where the Truss project is created.
</ParamField>

**Example:**

To create a new Truss project, use the following:

```sh  theme={"system"}
truss init my-model
```

To create a Truss with a custom name, use the following:

```sh  theme={"system"}
truss init --name "My Model" my-model
```

To create a Truss with TRT\_LLM backend, use the following:

```sh  theme={"system"}
truss init --backend TRT_LLM my-trt-model
```
