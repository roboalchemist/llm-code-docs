# Source: https://docs.firehydrant.com/docs/firehydrant-cli.md

# FireHydrant CLI (fhcli)

FireHydrant provides a command line tool, `fhcli`, to easily submit changes from your existing CI or orchestration systems. You can use `fhcli` to record the creation of Docker images, deploy events in Jenkins, CI build statuses, etc.

We publish releases at [https://github.com/firehydrant/fhcli/releases](https://github.com/firehydrant/fhcli/releases), and builds are available for MacOS (darwin) and Linux (amd64) with support for more platforms planned for the future.

## Installation

1. Go to the [Releases page](https://github.com/firehydrant/fhcli/releases).

   1. **If on Linux**,  you can directly download from the page and extract the file manually. We recommend extracting to somewhere like `/usr/local/bin`.
   2. **If on macOS**, right-click and copy the link to the appropriate release for your processor. Do not directly download from the browser, otherwise your OS will block execution of the file after it is extracted. Instead, run the following in the Terminal.

   ```shell Example Terminal Commands
   cd /usr/local/bin
   sudo wget -qO- [RELEASE_URL] | sudo tar -xvz
   ```

2. Confirm the tool is installed and working with `fhcli --version`. This should yield the current latest release version.

   ```
   [14:54:42] jdoe:~ $ fhcli --version
   fhcli version 0.0.14 (74bc3e20b87e2f5c551589466f87136d9c0efc0a)
   ```

## Configuring the CLI tool

You need an API key for the controller to use for authentication. We recommend that you [create one](https://docs.firehydrant.com/docs/api-keys) specifically for this integration. Put the token in an environment variable in your CI system or export it in a setup script. If the API key is exported as `FH_API_KEY`, the `fhcli` tool will automatically use it.

You can also store your token in `~/firehydrant.cfg` or `/etc/firehydrant.cfg` and it will automatically be used. We recommend also storing the environment name there if it's the same across all invocations of `fhcli` from this system.

```yaml
apiKey: fhb-123example
environment: production
```

## Using fhcli

`fhcli` comes with a few commands for different purposes.

### init

Writes a starter configuration file to `/tmp/firehydrant.cfg`. You can edit this file and insert some default parameters.

### event

Logs a change event in your FireHydrant instance. You will need to use a specific ordering of arguments and commands, like so:

```Text Example Change Event via FHCLI
fhcli --apiKey [API_KEY_HERE] \ # if api key not in config file above, otherwise skip
    event "New deployment event via FHCLI example" \
    --labels type=deployment,author="John Doe" \
    --environment us-east-1 \
    --service iam-service
```

### execute

This is useful for executing specific actions. For example, you can record the creation of a Docker image in FireHydrant by wrapping your call to `docker build` with `fhcli`:

```shell
fhcli execute --service=railsapp -- docker build -t app .
```

This is a simple example, but we recommend sending identities for a change like the Git revision or container image URL with the `fhcli` call:

```shell
fhcli execute --service=railsapp --identities "revision=${CIRCLE_SHA1},git=${CIRCLE_REPOSITORY_URL}:${CIRCLE_SHA1},image=us.gcr.io/${GOOGLE_PROJECT_ID}/${CIRCLE_PROJECT_REPONAME}:${CIRCLE_SHA1}" -- docker build -t app .
```

This may look complicated, but it's simply adding the above-mentioned data (in this case provided by CircleCI):

* Current Git revision: `revision=${CIRCLE_SHA1}`
* Full path of Git commit: `git=${CIRCLE_REPOSITORY_URL}:${CIRCLE_SHA1}`
* Docker image: `image=us.gcr.io/${GOOGLE_PROJECT_ID}/${CIRCLE_PROJECT_REPONAME}:${CIRCLE_SHA1}`

By sending this information, you can link a GitHub pull request to an updated Pod spec in a Kubernetes deployment. Sending this level of detail is not required, but it leads to better visibility into the propagation of changes through your system.

### help

Displays all available commands and arguments.