# Source: https://docs.baseten.co/reference/cli/truss/predict.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss predict

> Call the packaged model.

```sh  theme={"system"}
truss predict [OPTIONS] [TARGET_DIRECTORY]
```

Calls the packaged model with the provided input data. Use this to test your model locally or remotely.

### Options

<ParamField body="-d, --data" type="TEXT">
  JSON string representing the request payload.
</ParamField>

<ParamField body="-f, --file" type="PATH">
  Path to a JSON file containing the request payload.
</ParamField>

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to invoke.
</ParamField>

<ParamField body="--model" type="TEXT">
  ID of the model to invoke.
</ParamField>

<ParamField body="--model_version" type="TEXT">
  ID of the model version to invoke.
</ParamField>

<ParamField body="--published">
  Invoke the published (production) deployment.
</ParamField>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To call a model with inline JSON data, use the following:

```sh  theme={"system"}
truss predict -d '{"prompt": "What is the meaning of life?"}'
```

To call a model using a JSON file, use the following:

```sh  theme={"system"}
truss predict -f request.json
```

To call the production deployment, use the following:

```sh  theme={"system"}
truss predict --published -d '{"prompt": "Hello, world!"}'
```
