# Source: https://docs.baseten.co/reference/cli/truss/push.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# truss push

> Deploy a model to Baseten.

```sh  theme={"system"}
truss push [OPTIONS] [TARGET_DIRECTORY]
```

Deploys a Truss to Baseten. By default, creates a published deployment.

<Note>
  Use `--watch` for development deployments with live reload support. Use `--publish` to explicitly create a published deployment.
</Note>

### Options

<ParamField body="--remote" type="TEXT">
  Name of the remote in .trussrc to push to.
</ParamField>

<ParamField body="--watch">
  Push as a development deployment with live reload enabled. Use this for rapid iteration during development.
</ParamField>

<ParamField body="--publish">
  Push as a published deployment. If no production deployment exists, promote to production after deploy completes.
</ParamField>

<ParamField body="--promote">
  Push as a published deployment and promote to production, even if a production deployment already exists.
</ParamField>

<ParamField body="--environment" type="TEXT">
  Push as a published deployment and promote into the specified environment.
</ParamField>

<ParamField body="--preserve-previous-production-deployment">
  Preserve the previous production deployment's autoscaling settings. Can only be used with `--promote`.
</ParamField>

<ParamField body="--model-name" type="TEXT">
  Name of the model.
</ParamField>

<ParamField body="--deployment-name" type="TEXT">
  Name of the deployment. Can only be used with `--publish` or `--environment`. Must contain only alphanumeric, `.`, `-` or `_` characters.
</ParamField>

<ParamField body="--wait">
  Wait for deployment to complete before returning. Returns non-zero exit code if deploy or build fails.
</ParamField>

<ParamField body="--timeout-seconds" type="INTEGER">
  Maximum time to wait for deployment in seconds.
</ParamField>

<ParamField body="--team" type="TEXT">
  Name of the team to deploy to. If not specified, Truss infers the team based on your team membership and existing models, or prompts for selection when ambiguous.
</ParamField>

<Note>
  The `--team` flag is only available if your organization has teams enabled. [Contact us](mailto:support@baseten.co) to enable teams, or see [Teams](/organization/teams) for more information.
</Note>

### Arguments

<ParamField body="TARGET_DIRECTORY" type="TEXT">
  A Truss directory. Defaults to current directory.
</ParamField>

**Example:**

To deploy a development deployment with live reload from the current directory, use the following:

```sh  theme={"system"}
truss push --watch
```

To deploy a published deployment, use the following:

```sh  theme={"system"}
truss push --publish
```

To deploy and promote to production, use the following:

```sh  theme={"system"}
truss push --publish --promote
```

To deploy to a specific environment, use the following:

```sh  theme={"system"}
truss push --environment staging
```

To deploy with a custom deployment name, use the following:

```sh  theme={"system"}
truss push --publish --deployment-name my-model_v1.0
```

To deploy to a specific team, use the following:

```sh  theme={"system"}
truss push --publish --team my-team-name
```
