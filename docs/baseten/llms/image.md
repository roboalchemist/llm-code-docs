# Source: https://docs.baseten.co/reference/cli/truss/image.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss image

> Build and manage Truss Docker images.

```sh  theme={"system"}
truss image [OPTIONS] COMMAND [ARGS]...
```

Build and manage Docker images for your Truss.

***

## `build`

Build the Docker image for a Truss.

```sh  theme={"system"}
truss image build [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField body="--tag" type="TEXT">
  Docker image tag.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

<ParamField body="BUILD_DIR" type="TEXT">
  Image context directory. If not provided, a temp directory is created.
</ParamField>

**Example:**

To build a Docker image for your Truss, use the following:

```sh  theme={"system"}
truss image build
```

To build with a custom tag, use the following:

```sh  theme={"system"}
truss image build --tag my-model:v1
```

***

## `build-context`

Create a Docker build context for a Truss without building the image.

```sh  theme={"system"}
truss image build-context [OPTIONS] BUILD_DIR [TARGET_DIRECTORY]
```

### Arguments

<ParamField body="BUILD_DIR" type="TEXT" required>
  Directory where image context is created.
</ParamField>

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To create a build context in a specific directory, use the following:

```sh  theme={"system"}
truss image build-context ./build-context
```

***

## `run`

Run the Docker image for a Truss locally.

```sh  theme={"system"}
truss image run [OPTIONS] [TARGET_DIRECTORY] [BUILD_DIR]
```

### Options

<ParamField body="--tag" type="TEXT">
  Docker image tag to run.
</ParamField>

<ParamField body="--port" type="INTEGER">
  Local port to expose the model on.
</ParamField>

<ParamField body="--attach">
  Attach to the container process.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

<ParamField body="BUILD_DIR" type="TEXT">
  Image context directory. If not provided, a temp directory is created.
</ParamField>

**Example:**

To build and run a Truss locally, use the following:

```sh  theme={"system"}
truss image run
```

To run on a specific port, use the following:

```sh  theme={"system"}
truss image run --port 8080
```

To run in attached mode, use the following:

```sh  theme={"system"}
truss image run --attach
```
