# Source: https://skaffold.dev/docs/testers/custom/

Title: Custom Test

URL Source: https://skaffold.dev/docs/testers/custom/

Markdown Content:
Custom Test beta
----------------

Custom Test allows developers to run custom commands as part of their development pipeline. The command executes in the testing phase of the [Skaffold pipeline](https://skaffold.dev/docs/). It will run on the local machine where Skaffold is being executed and works with all supported Skaffold platforms. Users can opt out of running custom tests by using the `--skip-tests` flag.

Some example use cases for Custom Test are below:

*   Run unit tests
*   Run validation and security scans on images before deploying the image to a cluster for example by running [GCP Container Analysis](https://cloud.google.com/container-analysis/docs/on-demand-scanning-howto) or [Anchore Grype](https://github.com/anchore/grype#readme)

Custom tests are defined on a per image basis in the Skaffold config. Every time an artifact is rebuilt, Skaffold runs the associated custom tests as part of the Skaffold dev loop. Multiple testers can be defined per test. The Skaffold pipeline will be blocked on the custom test to complete or fail. Skaffold will block deployment when the first test fails. For ongoing test failures in the dev loop, Skaffold will stop the loop (not continue with the deploy) but will not exit the loop. Skaffold would surface the errors to the user and will keep the dev loop running. Skaffold will continue watching user specified test dependencies and re-trigger the loop whenever it detects another change.

CustomTester has a configurable timeout option to wait for the command to return. If no timeout is specified, Skaffold will wait indefinitely until the test command has completed execution.

### Contract between Skaffold and Custom command

Skaffold will pass in the environment variable `$IMAGE` to the custom command to access the image.

This variable can be set as a flag value input to the custom command `--flag=$IMAGE`.

### Configuration

To use a custom command, add a custom field to the corresponding test in the test section of the skaffold.yaml. Supported schema for CustomTest includes:

| Option | Description |
| --- | --- |
| `command` | **Required** custom command to be executed. If the command exits with a non-zero return code, the test will be considered to have failed. |
| `timeoutSeconds` | sets the wait time for skaffold for the command to complete. If unset or 0, Skaffold will wait until the command completes. |
| `dependencies` | additional test-specific file dependencies; changes to these files will re-run this test. |

### Dependencies for a Custom Test

Users can specify `dependencies` for custom tests so that skaffold knows when to retest during a dev loop. Dependencies can be specified per command. Users could list out directories and/or files (for example test scripts) to watch per command. If no dependencies are specified, only the script file (if the command is a script file) will be watched as a dependency. Test dependencies cannot trigger rebuild of an image.

Supported schema for `dependencies` include:

| Option | Description | Default |
| --- | --- | --- |
| `command` | represents a command that skaffold executes to obtain dependencies. The output of this command _must_ be a valid JSON array. |  |
| `paths` | locates the file dependencies for the command relative to workspace. Paths should be set to the file dependencies for this command, so that the skaffold file watcher knows when to retest and perform file synchronization. | `[]` |
| `ignore` | specifies the paths that should be ignored by skaffold’s file watcher. If a file exists in both `paths` and in `ignore`, it will be ignored, and will be excluded from both retest and file synchronization. Will only work in conjunction with `paths`. | `[]` |

#### Paths and Ignore

`Paths` and `Ignore` are arrays used to list dependencies. This can be a glob. Any `paths` in `Ignore` will be ignored by the skaffold file watcher, even if they are also specified in `Paths`. `Ignore` will only work in conjunction with `Paths`.

```
custom:
      - command: ./test.sh
        timeoutSeconds: 60
        dependencies:
          paths:
          -  "*_test.go"
          -  "test.sh"
```

#### Command for dependencies

Sometimes users might have a command or a script that can provide the dependencies for a given test. Custom tester can ask Skaffold to execute a custom command, which Skaffold can use to get the dependencies for the test for file watching.

The command _must_ return dependencies as a JSON array, otherwise skaffold will error out.

```
custom:
      - command: echo Hello world!!
        dependencies:
          command: echo [\"main_test.go\"]
```

> _Note: Adding a file pattern to a test dependency doesn’t automatically enable file sync on it. Refer to the [`file sync`](https://skaffold.dev/docs/filesync/) documentation, on how to set that up separately._

### Logging

`STDOUT` and `STDERR` from the custom command script will be redirected and displayed within skaffold logs.

Usage
-----

Custom tests will be automatically invoked as part of the run and dev commands, but can also be run independently by using the test subcommand.

*   To execute the custom command as an independent test command run: `skaffold test`
*   To execute custom command as part of the run command run: `skaffold run`
*   To execute custom command as part of the dev loop run: `skaffold dev`

### Example

This following example shows the `customTest` section from a `skaffold.yaml`. It instructs Skaffold to run unit tests (main_test.go) located in the local folder when the main application changes:

```
test:
  - image: custom-test-example
    custom:
      - command: ./test.sh
        timeoutSeconds: 60
        dependencies:
          paths:
          -  "*_test.go"
          -  "test.sh"
      - command: echo Hello world!!
        dependencies:
          command: echo [\"main_test.go\"]
```

A sample `test.sh` file, which runs unit tests when the test changes.

```
#!/bin/bash

set -e

echo "go custom test $@"

go test .
```
