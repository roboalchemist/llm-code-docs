# Source: https://buildkite.com/docs/agent/cli/reference/lock.md

# buildkite-agent lock

The Buildkite agent's `lock` subcommands provide the ability to coordinate multiple concurrent builds on the same host that access shared resources.

With the `lock` command, processes can acquire and release a lock using the `acquire` and `release` subcommands. For the special case of performing setup once for the life of the agent (and waiting until it is complete), there are the `do` and `done` subcommands. These provide an alternative to using `flock` or OS-dependent locking mechanisms.

Each type of `lock` subcommand makes use of a `[key]` value, which is an arbitrary name (for example, `my-key-value`) that you choose to identify your lock. A key does not reference any predefined value, and can be any name of your choosing, but it is recommended using a descriptive name that clearly indicates what resource or operation is being protected. All builds using the same lock key will coordinate with each other on the same host.

> 📘 Flock file locks
> The Buildkite agent also has an internal `flock` file locking mechanism, which is an automatic feature that's unrelated to the locking feature provided by these agent `lock` commands. The `flock` mechanism is used for Git mirror and SSH `known_hosts` handling, and these locks are automatically released when the process is completed, including when the process terminates abnormally, for example, when an agent is not cleanly shut down.

## Inspecting the state of a lock

### Usage

`buildkite-agent lock get [key]`

### Description

Retrieves the value of a lock key. Any key not in use returns an empty
string.

Note that this subcommand is only available when an agent has been started
with the `agent-api` experiment enabled.

`lock get` is generally only useful for inspecting lock state, as the value
can change concurrently. To acquire or release a lock, use `lock acquire` and
`lock release`.

### Examples

```shell
$ buildkite-agent lock get llama
Kuzco
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="lock-scope"><th><code>--lock-scope value</code> <a class="Docs__attribute__link" href="#lock-scope">#</a></th><td><p>The scope for locks used in this operation. Currently only 'machine' scope is supported (default: "machine")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_SCOPE</code></p></td></tr>
<tr id="sockets-path"><th><code>--sockets-path value</code> <a class="Docs__attribute__link" href="#sockets-path">#</a></th><td><p>Directory where the agent will place sockets (default: "$HOME/.buildkite-agent/sockets")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_SOCKETS_PATH</code></p></td></tr>
</table>

## Acquiring a lock

### Usage

`buildkite-agent lock acquire [key]`

### Description

Acquires the lock for the given key. `lock acquire` will wait (potentially
forever) until it can acquire the lock, if the lock is already held by
another process. If multiple processes are waiting for the same lock, there
is no ordering guarantee of which one will be given the lock next.

To prevent separate processes unlocking each other, the output from `lock
acquire` should be stored, and passed to `lock release`.

Note that this subcommand is only available when an agent has been started
with the `agent-api` experiment enabled.

### Examples

```shell
#!/usr/bin/env bash
token=$(buildkite-agent lock acquire llama)
# your critical section here...
buildkite-agent lock release llama "${token}"
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="lock-scope"><th><code>--lock-scope value</code> <a class="Docs__attribute__link" href="#lock-scope">#</a></th><td><p>The scope for locks used in this operation. Currently only 'machine' scope is supported (default: "machine")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_SCOPE</code></p></td></tr>
<tr id="sockets-path"><th><code>--sockets-path value</code> <a class="Docs__attribute__link" href="#sockets-path">#</a></th><td><p>Directory where the agent will place sockets (default: "$HOME/.buildkite-agent/sockets")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_SOCKETS_PATH</code></p></td></tr>
<tr id="lock-wait-timeout"><th><code>--lock-wait-timeout value</code> <a class="Docs__attribute__link" href="#lock-wait-timeout">#</a></th><td><p>Sets a maximum duration to wait for a lock before giving up (default: 0s)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_WAIT_TIMEOUT</code></p></td></tr>
</table>

## Releasing a previously-acquired lock

### Usage

`buildkite-agent lock release [key] [token]`

### Description

Releases the lock for the given key. This should only be called by the
process that acquired the lock. To help prevent different processes unlocking
each other unintentionally, the output from `lock acquire` is required as the
second argument, namely, the `token` in the Usage section above.

Note that this subcommand is only available when an agent has been started
with the `agent-api` experiment enabled.

### Examples

```shell
#!/usr/bin/env bash
token=$(buildkite-agent lock acquire llama)
# your critical section here...
buildkite-agent lock release llama "${token}"
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="lock-scope"><th><code>--lock-scope value</code> <a class="Docs__attribute__link" href="#lock-scope">#</a></th><td><p>The scope for locks used in this operation. Currently only 'machine' scope is supported (default: "machine")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_SCOPE</code></p></td></tr>
<tr id="sockets-path"><th><code>--sockets-path value</code> <a class="Docs__attribute__link" href="#sockets-path">#</a></th><td><p>Directory where the agent will place sockets (default: "$HOME/.buildkite-agent/sockets")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_SOCKETS_PATH</code></p></td></tr>
</table>

## Starting a do-once section

### Usage

`buildkite-agent lock do [key]`

### Description

Begins a do-once lock. Do-once can be used by multiple processes to
wait for completion of some shared work, where only one process should do
the work.

Note that this subcommand is only available when an agent has been started
with the `agent-api` experiment enabled.

`lock do` will do one of two things:

- Print &#39;do&#39;. The calling process should proceed to do the work and then
call `lock done`.
- Wait until the work is marked as done (with `lock done`) and print &#39;done&#39;.

If `lock do` prints &#39;done&#39; immediately, the work was already done.

### Examples

```shell
#!/usr/bin/env bash
if [[ $(buildkite-agent lock do llama) == 'do' ]]; then
  # your critical section here...
  buildkite-agent lock done llama
fi
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="lock-scope"><th><code>--lock-scope value</code> <a class="Docs__attribute__link" href="#lock-scope">#</a></th><td><p>The scope for locks used in this operation. Currently only 'machine' scope is supported (default: "machine")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_SCOPE</code></p></td></tr>
<tr id="sockets-path"><th><code>--sockets-path value</code> <a class="Docs__attribute__link" href="#sockets-path">#</a></th><td><p>Directory where the agent will place sockets (default: "$HOME/.buildkite-agent/sockets")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_SOCKETS_PATH</code></p></td></tr>
<tr id="lock-wait-timeout"><th><code>--lock-wait-timeout value</code> <a class="Docs__attribute__link" href="#lock-wait-timeout">#</a></th><td><p>Sets a maximum duration to wait for a lock before giving up (default: 0s)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_WAIT_TIMEOUT</code></p></td></tr>
</table>

## Completing a do-once section

### Usage

`buildkite-agent lock done [key]`

### Description

Completes a do-once lock. This should only be used by the process performing
the work.

Note that this subcommand is only available when an agent has been started
with the `agent-api` experiment enabled.

### Examples

```shell
#!/usr/bin/env bash
if [[ $(buildkite-agent lock do llama) == 'do' ]]; then
  # your critical section here...
  buildkite-agent lock done llama
fi
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="lock-scope"><th><code>--lock-scope value</code> <a class="Docs__attribute__link" href="#lock-scope">#</a></th><td><p>The scope for locks used in this operation. Currently only 'machine' scope is supported (default: "machine")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_LOCK_SCOPE</code></p></td></tr>
<tr id="sockets-path"><th><code>--sockets-path value</code> <a class="Docs__attribute__link" href="#sockets-path">#</a></th><td><p>Directory where the agent will place sockets (default: "$HOME/.buildkite-agent/sockets")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_SOCKETS_PATH</code></p></td></tr>
</table>

## Usage within a pipeline

Locks help coordinate access to shared resources when multiple agents run concurrently on the same host, such as when `--spawn` is used to create multiple agents.

### Coordinating sequential access

Use [`acquire`](#acquiring-a-lock) and [`release`](#releasing-a-previously-acquired-lock) when multiple builds need to run the same operation sequentially to prevent conflicts. Each build will execute the task, but only one at a time. This coordination works across multiple pipelines when they use the same lock key and the jobs run on the same host. Unlike [`do`](#starting-a-do-once-section) and [`done`](#completing-a-do-once-section), each build still performs the work—locks just ensure they don't interfere with each other.

#### Sequential locks example

In the following example, the key `db-migration-lock` ensures that database migrations run sequentially across multiple builds on the same host.

```yml
steps:
  - label: "Install Dependencies"
    commands:
      - "echo '+++ Installing dependencies'"
      - "bundle install"
      - "npm ci"
    key: "install"

  - label: "Migrate DB Schema"
    commands:
      - "echo '+++ Running DB migration with lock'"
      - "token=$(buildkite-agent lock acquire db-migration-lock)"
      - "bundle exec rake db:migrate"
      - "buildkite-agent lock release db-migration-lock '$${token}'"
    plugins:
      - vault-secrets#v2.2.1:
        server: "https://my-vault-server"
        path: "data/buildkite/postgres"
        auth:
          method: "approle"
          role-id: "my-role-id"
          secret-env: "VAULT_SECRET_ID"
    env:
      RAILS_ENV: "development"
    depends_on: "install"
    key: "migrate-db"
```

{: codeblock-file="pipeline.yml"}

This lock only controls access to the `bundle exec rake db:migrate` process itself, and does not lock access to the vault server defined by the plugin, or any subsequent commands following the `buildkite-agent lock release db-migration-lock '$${token}'` command. Only processes that occur between the `lock acquire` and `lock release` commands are the ones which are locked.

Multiple builds can still retrieve secrets from the vault concurrently, but only one can execute the actual database migration at a time, as long as all builds use the same lock key.

### One-time locks

When running parallel jobs on the same host that need a shared setup, [`do`](#starting-a-do-once-section) and [`done`](#completing-a-do-once-section) ensure expensive operations happen only once. For instance, one agent performs the setup (for example, downloading datasets, generating certificates, starting services, etc.), while others wait and then proceed. This saves time and resources compared to each parallel job repeating the same work. Once marked as `done`, the lock remains completed for all subsequent jobs on the host unless it is restarted.

#### One-time locks example

In the following example, they key `test-env-setup` ensures that the test environment setup happens only once across multiple parallel jobs on the same host.

```yml
steps:
  - label: "Install Dependencies"
    commands:
      - "echo '+++ Installing dependencies'"
      - "bundle install"
      - "npm ci"
    key: "install"

  - label: "Setup Test Environment"
    command: "setup_test.sh"
    depends_on: "install"
    key: "prep"
    parallelism: 5

  - label: "Run Tests"
    commands:
      - "echo '+++ Running tests'"
      - "bundle exec rspec"
    depends_on: "prep"
    parallelism: 10
```

{: codeblock-file="pipeline.yml"}

```bash
#!/usr/bin/env bash
echo "+++ Setting up shared test environment"
if [[ $(buildkite-agent lock do test-env-setup) == 'do' ]]; then
  echo "Downloading assets..."
  curl -o /tmp/test-data.zip https://releases.example.com/data.zip
  unzip /tmp/test-data.zip -d /tmp/shared-test-files/
  buildkite-agent lock done test-env-setup
else
  echo "Assets have already been pulled and unarchived"
fi
```

{: codeblock-file="setup_test.sh"}

The first job to reach the `buildkite-agent lock do test-env-setup` command receives a response of `do` and executes the setup work (downloading and extracting test data). All other parallel jobs will wait and then receive a response of `done`. These jobs will skip the `if` statement in this example bash script and output `Assets have already been pulled and unarchived`.

Unlike the `acquire`/`release` pattern, this lock is performed only once and subsequent jobs benefit from the completed work without repeating it.
