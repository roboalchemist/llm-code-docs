# Source: https://docs.socket.dev/docs/socket-ci.md

# socket ci

Get feedback on state of the code health in an automated environment

```
$ socket ci --help

  Create a new scan and report whether it passes your security policy

  Usage
    $ socket ci [options]

  Options
    --autoManifest    Auto generate manifest files where detected? See autoManifest flag in `socket scan create`

  This command is intended to use in CI runs to allow automated systems to
  accept or reject a current build. When the scan does not pass your security
  policy, the exit code will be non-zero.

  It will use the default org for the set API token.

  The --autoManifest flag does the same as the one from `socket scan create`
  but is not enabled by default since the CI is less likely to be set up with
  all the necessary dev tooling. Enable it if you want the scan to include
  locally generated manifests like for gradle and sbt.

  Examples
    $ socket ci
    $ socket ci --autoManifest
```

This is basically an alias to `socket scan create --report`. It will create a regular scan, wait for the results, generate a report (similar to `socket scan report`), and give you a "health" check. If the Scan is not "healthy", ie. it has alerts that violate your security or license policy, then the exit code will be non-zero. This should signal your CI environment that the build failed.

Useful to eg. quick and easily automate Socket checks in your Continuous Integration runs.

You can pre-configure certain pieces of information with `socket scan setup` which will be stored in `socket.json` in your project root ([more details](https://docs.socket.dev/docs/socketjson)).

### Exit Code Behavior

#### Code `0`

The CLI will exit with a status code of `0` under the following conditions:

* The command executes successfully without encountering unexpected errors. The report passes your organization security policy and license policy.

#### Non-Zero Exit Code

The CLI will return a non-zero exit code in the following scenarios:

* The generated report returns `"healthy": false`
* An unexpected error occurs during execution.