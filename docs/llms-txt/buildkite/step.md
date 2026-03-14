# Source: https://buildkite.com/docs/agent/cli/reference/step.md

# buildkite-agent step

The Buildkite agent's `step` command provides the ability to retrieve and update the attributes of steps in your `pipeline.yml` files.

## Updating a step

Use this command in your build scripts to update the step attributes. The following attributes can be updated:

* `label`
* `notify`
* `priority`

### Usage

`buildkite-agent step update <attribute> <value> [options...]`

### Description

Update an attribute of a step in the build

Note that step labels are used in commit status updates, so if you change the
label of a running step, you may end up with an &#39;orphaned&#39; status update
under the old label, as well as new ones using the updated label.

To avoid orphaned status updates, in your Pipeline Settings &gt; GitHub:

* Make sure Update commit statuses is not selected. Note that this prevents
Buildkite from automatically creating and sending statuses for this pipeline,
meaning you will have to handle all commit statuses through the pipeline.yml

### Example

```shell
buildkite-agent step update "label" "New Label"
buildkite-agent step update "label" " (add to end of label)" --append
buildkite-agent step update "label" < ./tmp/some-new-label
./script/label-generator | buildkite-agent step update "label"
buildkite-agent step update "priority" 10 --step "my-step-key"
buildkite-agent step update "notify" '[{"github_commit_status": {"context": "my-context"}}]' --append
buildkite-agent step update "notify" '[{"slack": "my-slack-workspace#my-channel"}]' --append
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
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>The step to update. Can be either its ID (BUILDKITE_STEP_ID) or key (BUILDKITE_STEP_KEY)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_ID</code></p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>The build to look for the step in. Only required when targeting a step using its key (BUILDKITE_STEP_KEY)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_BUILD_ID</code></p></td></tr>
<tr id="append"><th><code>--append </code> <a class="Docs__attribute__link" href="#append">#</a></th><td><p>Append to current attribute instead of replacing it (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_UPDATE_APPEND</code></p></td></tr>
<tr id="redacted-vars"><th><code>--redacted-vars value</code> <a class="Docs__attribute__link" href="#redacted-vars">#</a></th><td><p>Pattern of environment variable names containing sensitive values (default: "*_PASSWORD", "*_SECRET", "*_TOKEN", "*_PRIVATE_KEY", "*_ACCESS_KEY", "*_SECRET_KEY", "*_CONNECTION_STRING")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_REDACTED_VARS</code></p></td></tr>
</table>

## Getting a step

Use this command in your build scripts to get the value of a particular attribute from a step. The following attributes values can be retrieved:

* `agents`
* `command`
* `concurrency_key`
* `concurrency_limit`
* `depends_on`
* `env`
* `if`
* `key`
* `label`
* `notify`
* `outcome`
* `parallelism`
* `state`
* `timeout`
* `type`

### Usage

`buildkite-agent step get <attribute> [options...]`

### Description

Retrieve the value of an attribute in a step. If no attribute is passed, the
entire step will be returned.

In the event a complex object is returned (an object or an array),
you&#39;ll need to supply the --format option to tell the agent how it should
output the data (currently only JSON is supported).

### Example

```shell
buildkite-agent step get "label" --step "key"
buildkite-agent step get --format json
buildkite-agent step get "state" --step "my-other-step"
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
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>The step to get. Can be either its ID (BUILDKITE_STEP_ID) or key (BUILDKITE_STEP_KEY)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_ID</code></p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>The build to look for the step in. Only required when targeting a step using its key (BUILDKITE_STEP_KEY)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_BUILD_ID</code></p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>The format to output the attribute value in (currently only JSON is supported)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_GET_FORMAT</code></p></td></tr>
</table>

## Getting the outcome of a step

If you're only interested in whether a step passed or failed, perhaps to use conditional logic inside your build script, you can use the same approach as above in [Getting a step](#getting-a-step).

For example, the following pipeline has one step that fails (`one`), and another that passes (`two`). After the `wait`, the next two steps print the `outcome` attribute of steps `one` and `two`, and the last step [annotates the build](/docs/agent/cli/reference/annotate) if step `one` fails. Note that `step get` needs the `key` of the step to identify it, not the `label`.

The `outcome` is `passed`, `hard_failed`, `soft_failed`, or `errored`. A "hard fail" is a non-zero exit status that fails the build. A ["soft fail"](/docs/pipelines/configure/step-types/command-step#soft-fail-attributes) is a non-zero exit status that does not fail the build. An "errored" step outcome is reserved for infrastructure issues, such as timeouts, cancellations or expired jobs.

```yaml
steps:
  - label: 'Step 1'
    command: "false"
    key: 'one'
  - label: 'Step 2'
    command: "true"
    key: 'two'

  - wait:
    continue_on_failure: true

  - label: 'Step 3'
    command: 'echo `buildkite-agent step get "outcome" --step "one"`'
  - label: 'Step 4'
    command: 'echo `buildkite-agent step get "outcome" --step "two"`'
  - label: 'Step 5'
    command: |
      if [ $(buildkite-agent step get "outcome" --step "one") == "hard_failed" ]; then
        buildkite-agent annotate 'this build failed' --style 'error'
      fi
```

## Understanding step states vs job states

The `buildkite-agent step get` command returns _step_ `state` and `outcome` values. The [REST](/docs/apis/rest-api) and [GraphQL](/docs/apis/graphql-api) APIs return [_job_ states](/docs/pipelines/configure/defining-steps#job-states). For more information regarding the difference between these values, see the definitions of [step](/docs/pipelines/glossary#step) and [job](/docs/pipelines/glossary#job).

## Canceling a step

Use this command to programmatically cancel all jobs for a step. It is possible to issue graceful and forced cancel commands.

Force canceling a step can be used to cancel lost or hung jobs before their agents would otherwise be marked as lost.

### Usage

`buildkite-agent step cancel [options...]`

### Description

Cancel all unfinished jobs for a step

### Example

```shell
buildkite-agent step cancel --step "key"
buildkite-agent step cancel --step "key" --force
buildkite-agent step cancel --step "key" --force --force-grace-period-seconds 30
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
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>The step to cancel. Can be either its ID (BUILDKITE_STEP_ID) or key (BUILDKITE_STEP_KEY)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_ID</code></p></td></tr>
<tr id="force"><th><code>--force </code> <a class="Docs__attribute__link" href="#force">#</a></th><td><p>Transition unfinished jobs to a canceled state instead of waiting for jobs to finish uploading artifacts (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_CANCEL_FORCE</code></p></td></tr>
<tr id="force-grace-period-seconds"><th><code>--force-grace-period-seconds value</code> <a class="Docs__attribute__link" href="#force-grace-period-seconds">#</a></th><td><p>The number of seconds to wait for agents to finish uploading artifacts before transitioning unfinished jobs to a canceled state. `--force` must also be supplied for this to take affect (default: 10) [$BUILDKITE_STEP_CANCEL_FORCE_GRACE_PERIOD_SECONDS, $BUILDKITE_CANCEL_GRACE_PERIOD]<br /><strong>Environment variable</strong>: <code>$BUILDKITE_STEP_CANCEL_FORCE_GRACE_PERIOD_SECONDS</code></p></td></tr>
</table>
