# Source: https://buildkite.com/docs/agent/cli/reference/env.md

# buildkite-agent env

The Buildkite agent's `env` subcommands provide the ability to inspect environment variables.

From version 3.115.2 of the Buildkite agent, jobs can inspect and modify their environment variables using the `get`, `set`, and `unset` sub-commands. These provide an alternative to using shell commands to inspect and modify environment variables.

## Printing env

This command is used internally by the agent and isn't recommended for use in your builds.

### Usage

`buildkite-agent env dump [options]`

### Description

Prints out the environment of the current process as a JSON object, easily
parsable by other programs. Used when executing hooks to discover changes
that hooks make to the environment.

### Example

```shell
buildkite-agent env dump --format json-pretty
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>Output format; json or json-pretty (default: "json")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_DUMP_FORMAT</code></p></td></tr>
</table>

## Getting a job's environment variables

### Usage

`buildkite-agent env get [variables]`

### Description

Retrieves environment variables and their current values from the current job
execution environment.

Changes to the job environment only apply to the environments of subsequent
phases of the job. However, `env get` can be used to inspect the changes made
with `env set` and `env unset`.

### Examples

Getting all variables in key=value format:

```shell
$ buildkite-agent env get
ALPACA=Geronimo the Incredible
BUILDKITE=true
LLAMA=Kuzco
...
```

Getting the value of one variable:

```shell
$ buildkite-agent env get LLAMA
Kuzco
```

Getting multiple specific variables:

```shell
$ buildkite-agent env get LLAMA ALPACA
ALPACA=Geronimo the Incredible
LLAMA=Kuzco
```

Getting variables as a JSON object:

```shell
$ buildkite-agent env get --format=json-pretty
{
  "ALPACA": "Geronimo the Incredible",
  "BUILDKITE": "true",
  "LLAMA": "Kuzco",
  ...
}
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>Output format: plain, json, or json-pretty (default: "plain")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_GET_FORMAT</code></p></td></tr>
</table>

## Setting a job's environment variables

### Usage

`buildkite-agent env set [variable]`

### Description

Sets environment variables in the current job execution environment.
Changes to the job environment variables only apply to subsequent phases of the job.
This command cannot unset Buildkite read-only variables.

To read the new values of variables from within the current phase, use `env get`.

### Examples

Setting the variables `LLAMA` and `ALPACA`:

```shell
$ buildkite-agent env set LLAMA=Kuzco "ALPACA=Geronimo the Incredible"
Added:
+ LLAMA
Updated:
~ ALPACA
```

Setting the variables `LLAMA` and `ALPACA` using a JSON object supplied over standard input:

```shell
$ echo '{"ALPACA":"Geronimo the Incredible","LLAMA":"Kuzco"}' | \
    buildkite-agent env set --input-format=json --output-format=quiet -
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="input-format"><th><code>--input-format value</code> <a class="Docs__attribute__link" href="#input-format">#</a></th><td><p>Input format: plain or json (default: "plain")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_SET_INPUT_FORMAT</code></p></td></tr>
<tr id="output-format"><th><code>--output-format value</code> <a class="Docs__attribute__link" href="#output-format">#</a></th><td><p>Output format: quiet (no output), plain, json, or json-pretty (default: "plain")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_SET_OUTPUT_FORMAT</code></p></td></tr>
</table>

## Removing environment variables from a job

### Usage

`buildkite-agent env unset [variables]`

### Description

Unsets environment variables in the current job execution environment.
Changes to the job environment variables only apply to subsequent phases of the job.
This command cannot unset Buildkite read-only variables.

To read the new values of variables from within the current phase, use `env get`.

### Examples

Unsetting the variables `LLAMA` and `ALPACA`:

```shell
$ buildkite-agent env unset LLAMA ALPACA
Unset:
- ALPACA
- LLAMA
```

Unsetting the variables `LLAMA` and `ALPACA` with a JSON list supplied over standard input

```shell
$ echo '["LLAMA","ALPACA"]' | \
    buildkite-agent env unset --input-format=json --output-format=quiet -
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="input-format"><th><code>--input-format value</code> <a class="Docs__attribute__link" href="#input-format">#</a></th><td><p>Input format: plain or json (default: "plain")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_UNSET_INPUT_FORMAT</code></p></td></tr>
<tr id="output-format"><th><code>--output-format value</code> <a class="Docs__attribute__link" href="#output-format">#</a></th><td><p>Output format: quiet (no output), plain, json, or json-pretty (default: "plain")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENV_UNSET_OUTPUT_FORMAT</code></p></td></tr>
</table>
