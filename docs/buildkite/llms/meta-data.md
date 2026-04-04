# Source: https://buildkite.com/docs/agent/cli/reference/meta-data.md

# buildkite-agent meta-data

The Buildkite agent's `meta-data` command provides your build pipeline with a powerful key/value data-store that works across build steps and build agents, no matter the machine or network.

See the [Using build meta-data](/docs/pipelines/configure/build-meta-data) guide for a step-by-step example.

## Setting data

Use this command in your build scripts to save string data in the Buildkite meta-data store.

### Usage

`buildkite-agent meta-data set <key> [value] [options...]`

### Description

Set arbitrary data on a build using a basic key/value store.

You can supply the value as an argument to the command, or pipe in a file or
script output.

The value must be a non-empty string, and strings containing only whitespace
characters are not allowed.

### Example

```shell
buildkite-agent meta-data set "foo" "bar"
buildkite-agent meta-data set "foo" < ./tmp/meta-data-value
./script/meta-data-generator | buildkite-agent meta-data set "foo"
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
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Which job's build should the meta-data be set on<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="redacted-vars"><th><code>--redacted-vars value</code> <a class="Docs__attribute__link" href="#redacted-vars">#</a></th><td><p>Pattern of environment variable names containing sensitive values (default: "*_PASSWORD", "*_SECRET", "*_TOKEN", "*_PRIVATE_KEY", "*_ACCESS_KEY", "*_SECRET_KEY", "*_CONNECTION_STRING")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_REDACTED_VARS</code></p></td></tr>
</table>

Meta-data values are restricted to a maximum of 100 kilobytes. Keys and values larger than 1 kilobyte are discouraged. Please use [artifacts](/docs/agent/cli/reference/artifact) for large data which needs to uploaded and downloaded.

## Getting data

Use this command in your build scripts to get a previously saved value from the Buildkite meta-data store.

### Usage

`buildkite-agent meta-data get <key> [options...]`

### Description

Get data from a build&#39;s key/value store.

### Example

```shell
buildkite-agent meta-data get "foo"
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
<tr id="default"><th><code>--default value</code> <a class="Docs__attribute__link" href="#default">#</a></th><td><p>If the meta-data value doesn't exist return this instead</p></td></tr>
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Which job's build should the meta-data be retrieved from<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>Which build should the meta-data be retrieved from. --build will take precedence over --job<br /><strong>Environment variable</strong>: <code>$BUILDKITE_METADATA_BUILD_ID</code></p></td></tr>
</table>

## Checking if data exists

### Usage

`buildkite-agent meta-data exists <key> [options...]`

### Description

The command exits with a status of 0 if the key has been set, or it will
exit with a status of 100 if the key doesn&#39;t exist.

### Example

```shell
buildkite-agent meta-data exists "foo"
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
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Which job's build should the meta-data be checked for<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>Which build should the meta-data be retrieved from. --build will take precedence over --job<br /><strong>Environment variable</strong>: <code>$BUILDKITE_METADATA_BUILD_ID</code></p></td></tr>
</table>

## Listing keys

### Usage

`buildkite-agent meta-data keys [options...]`

### Description

Lists all meta-data keys that have been previously set, delimited by a newline
and terminated with a trailing newline.

### Example

```shell
buildkite-agent meta-data keys
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
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Which job's build should the meta-data be checked for<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>Which build should the meta-data be retrieved from. --build will take precedence over --job<br /><strong>Environment variable</strong>: <code>$BUILDKITE_METADATA_BUILD_ID</code></p></td></tr>
</table>
