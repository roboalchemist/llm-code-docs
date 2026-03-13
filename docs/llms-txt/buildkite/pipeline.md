# Source: https://buildkite.com/docs/platform/cli/reference/pipeline.md

# Source: https://buildkite.com/docs/agent/cli/reference/pipeline.md

# buildkite-agent pipeline

The Buildkite agent's `pipeline` command allows you to add and replace build steps in the running build. The steps are defined using YAML or JSON and can be read from a file or streamed from the output of a script.

See the [Defining your pipeline steps](/docs/pipelines/configure/defining-steps) guide for a step-by-step example and list of step types.

## Uploading pipelines

> 🚧 Processing of a single pipeline file
> In versions of the Buildkite agent prior to 3.104.0, the `buildkite-agent pipeline upload` command only processes a single pipeline file. If multiple files are passed into a command (including using a wildcard `*` in the filename), only the first pipeline file will be processed, and any additional pipeline files provided as arguments are ignored. Later versions of the Buildkite agent do support multiple pipeline file uploads. See [Uploading multiple pipelines](#uploading-multiple-pipelines) for more information.

### Usage

`buildkite-agent pipeline upload [file] [options...]`

### Description

Allows you to change the pipeline of a running build by uploading either a
YAML (recommended) or JSON configuration file. If no configuration file is
provided, the command looks for the file in the following locations:

- buildkite.yml
- buildkite.yaml
- buildkite.json
- .buildkite/pipeline.yml
- .buildkite/pipeline.yaml
- .buildkite/pipeline.json
- buildkite/pipeline.yml
- buildkite/pipeline.yaml
- buildkite/pipeline.json

You can also pipe build pipelines to the command allowing you to create
scripts that generate dynamic pipelines. The configuration file has a
limit of 500 steps per file. Configuration files with over 500 steps
must be split into multiple files and uploaded in separate steps.

### Example

```shell
buildkite-agent pipeline upload
buildkite-agent pipeline upload my-custom-pipeline.yml
./script/dynamic_step_generator | buildkite-agent pipeline upload
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="agent-access-token"><th><code>--agent-access-token value</code> <a class="Docs__attribute__link" href="#agent-access-token">#</a></th><td><p>The access token used to identify the agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ACCESS_TOKEN</code></p></td></tr>
<tr id="endpoint"><th><code>--endpoint value</code> <a class="Docs__attribute__link" href="#endpoint">#</a></th><td><p>The Agent API endpoint (default: "<code>https://agent.buildkite.com/v3</code>")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENDPOINT</code></p></td></tr>
<tr id="no-http2"><th><code>--no-http2 </code> <a class="Docs__attribute__link" href="#no-http2">#</a></th><td><p>Disable HTTP2 when communicating with the Agent API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_HTTP2</code></p></td></tr>
<tr id="debug-http"><th><code>--debug-http </code> <a class="Docs__attribute__link" href="#debug-http">#</a></th><td><p>Enable HTTP debug mode, which dumps all request and response bodies to the log (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_HTTP</code></p></td></tr>
<tr id="trace-http"><th><code>--trace-http </code> <a class="Docs__attribute__link" href="#trace-http">#</a></th><td><p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_TRACE_HTTP</code></p></td></tr>
<tr id="replace"><th><code>--replace </code> <a class="Docs__attribute__link" href="#replace">#</a></th><td><p>Replace the rest of the existing pipeline with the steps uploaded. Jobs that are already running are not removed (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PIPELINE_REPLACE</code></p></td></tr>
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>The job that is making the changes to its build<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="dry-run"><th><code>--dry-run </code> <a class="Docs__attribute__link" href="#dry-run">#</a></th><td><p>Rather than uploading the pipeline, it will be echoed to stdout (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PIPELINE_UPLOAD_DRY_RUN</code></p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>In dry-run mode, specifies the form to output the pipeline in. Must be one of: json,yaml (default: "json")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PIPELINE_UPLOAD_DRY_RUN_FORMAT</code></p></td></tr>
<tr id="no-interpolation"><th><code>--no-interpolation </code> <a class="Docs__attribute__link" href="#no-interpolation">#</a></th><td><p>Skip variable interpolation into the pipeline prior to upload (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PIPELINE_NO_INTERPOLATION</code></p></td></tr>
<tr id="reject-secrets"><th><code>--reject-secrets </code> <a class="Docs__attribute__link" href="#reject-secrets">#</a></th><td><p>When true, fail the pipeline upload early if the pipeline contains secrets (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PIPELINE_UPLOAD_REJECT_SECRETS</code></p></td></tr>
<tr id="apply-if-changed"><th><code>--apply-if-changed </code> <a class="Docs__attribute__link" href="#apply-if-changed">#</a></th><td><p>When enabled, steps containing an `if_changed` key are evaluated against the git diff. If the `if_changed` glob pattern match no files changed in the build, the step is skipped. Minimum Buildkite Agent version: v3.99 (with --apply-if-changed flag), v3.103.0 (enabled by default) (default: true) [$BUILDKITE_AGENT_APPLY_IF_CHANGED, $BUILDKITE_AGENT_APPLY_SKIP_IF_UNCHANGED]<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_APPLY_IF_CHANGED</code></p></td></tr>
<tr id="git-diff-base"><th><code>--git-diff-base value</code> <a class="Docs__attribute__link" href="#git-diff-base">#</a></th><td><p>Provides the base from which to find the git diff when processing `if_changed`, e.g. origin/main. If not provided, it uses the first valid value of {origin/$BUILDKITE_PULL_REQUEST_BASE_BRANCH, origin/$BUILDKITE_PIPELINE_DEFAULT_BRANCH, origin/main}.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PULL_REQUEST_BASE_BRANCH</code></p></td></tr>
<tr id="fetch-diff-base"><th><code>--fetch-diff-base </code> <a class="Docs__attribute__link" href="#fetch-diff-base">#</a></th><td><p>When enabled, the base for computing the git diff will be git-fetched prior to computing the diff (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_FETCH_DIFF_BASE</code></p></td></tr>
<tr id="changed-files-path"><th><code>--changed-files-path value</code> <a class="Docs__attribute__link" href="#changed-files-path">#</a></th><td><p>Path to a file containing the list of changed files (newline-separated) to use for `if_changed` evaluation. When provided, the agent skips running git commands to determine changed files.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_CHANGED_FILES_PATH</code></p></td></tr>
<tr id="jwks-file"><th><code>--jwks-file value</code> <a class="Docs__attribute__link" href="#jwks-file">#</a></th><td><p>Path to a file containing a JWKS. Passing this flag enables pipeline signing<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_JWKS_FILE</code></p></td></tr>
<tr id="jwks-key-id"><th><code>--jwks-key-id value</code> <a class="Docs__attribute__link" href="#jwks-key-id">#</a></th><td><p>The JWKS key ID to use when signing the pipeline. Required when using a JWKS<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_JWKS_KEY_ID</code></p></td></tr>
<tr id="signing-aws-kms-key"><th><code>--signing-aws-kms-key value</code> <a class="Docs__attribute__link" href="#signing-aws-kms-key">#</a></th><td><p>The AWS KMS key identifier which is used to sign pipelines.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_AWS_KMS_KEY</code></p></td></tr>
<tr id="debug-signing"><th><code>--debug-signing </code> <a class="Docs__attribute__link" href="#debug-signing">#</a></th><td><p>Enable debug logging for pipeline signing. This can potentially leak secrets to the logs as it prints each step in full before signing. Requires debug logging to be enabled (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_SIGNING</code></p></td></tr>
<tr id="redacted-vars"><th><code>--redacted-vars value</code> <a class="Docs__attribute__link" href="#redacted-vars">#</a></th><td><p>Pattern of environment variable names containing sensitive values (default: "*_PASSWORD", "*_SECRET", "*_TOKEN", "*_PRIVATE_KEY", "*_ACCESS_KEY", "*_SECRET_KEY", "*_CONNECTION_STRING")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_REDACTED_VARS</code></p></td></tr>
</table>

## Pipeline format

The pipeline can be written as YAML or JSON, but YAML is more common for its readability. There are three top-level properties you can specify:

- The `agents` attribute - a map of agent characteristics such as `os` or `queue` that restrict what agents the command will run on.
- The `env` attribute - a map of [environment variables](/docs/pipelines/configure/environment-variables) to apply to all steps.
- The `steps` attribute - an array of [build pipeline steps](/docs/pipelines/configure/defining-steps).

## Insertion order

Steps are inserted immediately following the job performing the pipeline upload. Note that if you perform multiple uploads from a single step, they can appear to be in reverse order, because the later uploads are inserted earlier in the pipeline.

## Environment variable substitution

The `pipeline upload` command supports environment variable substitution using the syntax `$VAR` and `${VAR}`.

For example, the following pipeline substitutes a number of [Buildkite's default environment variables](/docs/pipelines/configure/environment-variables) into a [trigger step](/docs/pipelines/configure/step-types/trigger-step):

```yaml
- trigger: "app-deploy"
  label: "\:rocket\: Deploy"
  branches: "main"
  async: true
  build:
    message: "${BUILDKITE_MESSAGE}"
    commit: "${BUILDKITE_COMMIT}"
    branch: "${BUILDKITE_BRANCH}"
```

If you want an environment variable to be evaluated at runtime (for example, using the step's environment variables), ensure you escape the `$` character using `$$` or `\$`. For example:

```yaml
- command: "deploy.sh $$SERVER"
  env:
    SERVER: "server-a"
```

### Escaping the $ character

If you need to prevent substitution, you can escape the `$` character by using `$$` or `\$`.

For example, using `$$USD` and `\$USD` will both result in the same value: `$USD`.

### Disabling interpolation

You can disable interpolation with the `--no-interpolation` flag, which was added in v3.1.1.

### Requiring environment variables

You can set required environment variables using the syntax `${VAR?}`. If `VAR` is not set, the `pipeline upload` command will print an error and exit with a status of 1.

For example, the following step will cause the pipeline upload to error if the `SERVER` environment variable has not been set:

```yaml
- command: "deploy.sh \"${SERVER?}\""
```

You can set a custom error message after the `?` character. For example, the following prints the error message `SERVER: is not set. Please specify a server` if the environment variable has not been set:

```yaml
- command: "deploy.sh \"${SERVER?is not set. Please specify a server}\""
```

### Default, blank, and missing values

If an environment variable has not been set it will evaluate to a blank string. You can set a fallback value using the syntax `${VAR:-default-value}`.

For example, the following step will run the command `deploy.sh staging`:

```yaml
- command: "deploy.sh \"${SERVER:-staging}\""
```

<table class="responsive-table">
  <thead>
    <tr><th>Environment Variables</th><th>Syntax</th><th>Result</th></tr>
  </thead>
  <tbody>
    <tr><td><code></code></td><td><code>"${SERVER:-staging}"</code></td><td><code>"staging"</code></td></tr>
    <tr><td><code>SERVER=""</code></td><td><code>"${SERVER:-staging}"</code></td><td><code>"staging"</code></td></tr>
    <tr><td><code>SERVER="staging-5"</code></td><td><code>"${SERVER:-staging}"</code></td><td><code>"staging-5"</code></td></tr>
  </tbody>
</table>

If you need to substitute environment variables containing empty strings, you can use the syntax `${VAR-default-value}` (notice the missing `:`).

<table class="responsive-table">
  <thead>
    <tr><th>Environment Variables</th><th>Syntax</th><th>Result</th></tr>
  </thead>
  <tbody>
    <tr><td><code></code></td><td><code>"${SERVER-staging}"</code></td><td><code>"staging"</code></td></tr>
    <tr><td><code>SERVER=""</code></td><td><code>"${SERVER-staging}"</code></td><td><code>""</code></td></tr>
    <tr><td><code>SERVER="staging-5"</code></td><td><code>"${SERVER-staging}"</code></td><td><code>"staging-5"</code></td></tr>
  </tbody>
</table>

### Extracting character ranges

You can substitute a subset of characters from an environment variable by specifying a start and end range using the syntax `${VAR:start:end}`.

For example, the following step will echo the first 7 characters of the `BUILDKITE_COMMIT` environment variable:

```yaml
- command: "echo \"Short commit is: ${BUILDKITE_COMMIT:0:7}\""
```

If the environment variable has not been set, the range will return a blank string.

## Uploading multiple pipelines

From version 3.104.0 of the Buildkite agent, multiple pipelines can be uploaded by passing them as arguments to a single command:

```bash
buildkite-agent pipeline upload .buildkite/pipeline1.yml .buildkite/pipeline2.yml
````

Shell glob expansions, which are expanded by the shell into a list of files, can also be used:

```bash
buildkite-agent pipeline upload .buildkite/pipeline*.yml
````

Older agent versions only process a single file. Different approaches are available for handling the upload of multiple pipeline files for processing.

### Multiple sequential uploads

You can call `buildkite-agent pipeline upload` multiple times within the same step to upload multiple pipeline files:

```bash
buildkite-agent pipeline upload .buildkite/pipeline1.yml
buildkite-agent pipeline upload .buildkite/pipeline2.yml
```

### Pass multiple files to command

Using the `find` command, you can pipe `|` multiple file paths into the `buildkite-agent pipeline upload` command:

```bash
find .buildkite/ -type f -iname '*.yaml' -print0 | xargs -0 -n1 buildkite-agent pipeline upload
```

### Combine multiple pipeline files

Since the `buildkite-agent pipeline upload` command is also able to accept pipeline YAML, you can emit the contents of multiple pipeline files and have this combined output be processed directly from STDIN.

> 🚧 Processing of multiple pipeline files
> When passing multiple pipeline files into the pipeline upload command, include a `---` on the first line of each pipeline file to indicate the beginning of each new pipeline YAML file. This is required to ensure the `buildkite-agent` is able to correctly process multiple files that have been combined into a single input stream.

Using the following three example pipeline files:

```yaml
---
steps:
  - label: "Start of the build"
    command: ./scripts/build-start.sh
```

{: codeblock-file="pipeline-start.yml"}

```yaml
---
steps:
  - label: "Middle of the build"
    command: ./scripts/build-middle.sh
```

{: codeblock-file="pipeline-middle.yml"}

```yaml
---
steps:
  - label: "End of the build"
    command: ./scripts/build-end.sh
```

{: codeblock-file="pipeline-end.yml"}

Pass the contents of all the pipeline files that are matching the wildcard `*` file pattern into the pipeline upload command:

```bash
cat .buildkite/pipeline-*.yml | buildkite-agent pipeline upload
```

Alternatively, you can explicitly list each pipeline file to be passed into the pipeline upload command:

```bash
cat .buildkite/pipeline-start.yml .buildkite/pipeline-middle.yml .buildkite/pipeline-end.yml | buildkite-agent pipeline upload
```

## Troubleshooting

Here are some common issues that can occur when uploading a pipeline.

### Common errors

Pipeline uploads can be rejected if certain criteria are not met. Here are explanations for why your pipeline upload might be rejected.

<table class="responsive-table">
  <thead>
    <tr><th>Error</th><th>Reason</th></tr>
  </thead>
  <tbody>
    <tr><td><code>The key "duplicate-key-name" has already <br>been used by another step in this build</code></td><td>This error occurs when you try to upload a pipeline step with a <code>key</code> attribute that matches the <code>key</code> attribute of an existing step in the pipeline. <code>key</code> attributes must be unique for all steps in a build. To resolve this error, either remove the duplicate <code>key</code> or change it to a unique value.</td></tr>
    <tr><td><code>You can only change the pipeline of a <br>running build</code></td><td>This error occurs when you attempt to upload a pipeline to a build that has already finished. This typically happens when using the <code>--job</code> option with the upload command. To resolve this, ensure the build is still running before uploading, or start a new build.</td></tr>
  </tbody>
</table>
