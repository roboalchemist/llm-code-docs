# Source: https://docs.baseten.co/reference/cli/truss/container.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss container

> Run and manage Truss containers locally.

```sh  theme={"system"}
truss container [OPTIONS] COMMAND [ARGS]...
```

Manage Docker containers for your Truss.

***

## `kill`

Kill containers related to a specific Truss.

```sh  theme={"system"}
truss container kill [OPTIONS] [TARGET_DIRECTORY]
```

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To kill containers for the current Truss, use the following:

```sh  theme={"system"}
truss container kill
```

***

## `kill-all`

Kill all Truss containers that are not manually persisted.

```sh  theme={"system"}
truss container kill-all [OPTIONS]
```

**Example:**

To kill all Truss containers, use the following:

```sh  theme={"system"}
truss container kill-all
```

***

## `logs`

Get logs from a running Truss container.

```sh  theme={"system"}
truss container logs [OPTIONS] [TARGET_DIRECTORY]
```

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To view logs from the current Truss container, use the following:

```sh  theme={"system"}
truss container logs
```
