# Source: https://developer.1password.com/docs/cli/shell-plugins/contribute

On this page

# Build your own shell plugins (beta)

If you don\'t see your favorite command-line tool [listed in the 1Password Shell Plugin registry](/docs/cli/shell-plugins/), you can write your own plugin.

1Password CLI allows you to build and test shell plugins locally, so you can add support for authenticating your favorite CLI using a credential you saved in 1Password.

If you want to make your plugin available to others, you can [create a pull request in the shell plugins GitHub repository](https://github.com/1Password/shell-plugins).

## Requirements[â€‹](#requirements "Direct link to Requirements") 

- [Sign up for 1Password](https://1password.com/pricing/password-manager).
- Install and sign in to 1Password for [Mac](https://1password.com/downloads/mac) or [Linux](https://1password.com/downloads/linux).
- Install [1Password CLI](/docs/cli/get-started/) and turn on the [desktop app integration](/docs/cli/get-started#step-2-turn-on-the-1password-desktop-app-integration).
- Install [Go 1.18 or later](https://go.dev/doc/install).
- Install [Git](https://git-scm.com/).
- Install [GNU Make](https://www.gnu.org/software/make/).

## Concepts[â€‹](#concepts "Direct link to Concepts") 

A 1Password Shell Plugin should describe the following:

- The **credential** offered by a platform
- The CLI or **executable** offered by a platform
- How the credential should be **provisioned** for the respective CLI to authenticate
- Which commands for the respective CLI **need authentication**
- How credentials stored on the local filesystem can be **imported** into 1Password

Shell plugins are written in Go and consist of a set of Go structs in a package that together make up the plugin for a certain platform, service, or product. Don\'t worry if you\'re not a Go expert â€" there are [lots of examples](https://github.com/1Password/shell-plugins/tree/main/plugins) you can learn from to build your plugin!

## Step 1: Use the plugin template[â€‹](#step-1-use-the-plugin-template "Direct link to Step 1: Use the plugin template") 

First, clone or fork the [1Password Shell Plugins repository](https://github.com/1Password/shell-plugins) on GitHub. It contains the current plugin registry, as well as the SDK needed to contribute.

To get started with those, use the following Makefile command:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

You\'ll be prompted to enter the following information:

- **Plugin name:** Lowercase identifier for the platform, e.g. `aws`, `github`, `digitalocean`, `azure`. This will also be used as the name of the Go package.
- **Plaform display name:** The display name of the platform, e.g `AWS`, `GitHub`, `DigitalOcean`, `Azure`.
- **Credential name:** The credentials the platform offers, e.g. `Personal Access Token`, `API Key`, `Auth Token`.
- **Executable name:** The command to invoke, e.g. `aws`, `gh`, `doctl`, `az`.

After filling in the form, you\'ll see a Go package created in the `plugins` directory, with separate files for the plugin, credential, and executable. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To save you some time, the generated files will be stubbed out with information that\'s derived from the Makefile prompts on a best-effort basis. It contains *TODO* comments in the code to steer you in the direction of what to change or validate for correctness.

## Step 2: Edit the plugin definition[â€‹](#step-2-edit-the-plugin-definition "Direct link to Step 2: Edit the plugin definition") 

The `plugin.go` file contains basic information about the plugin and the platform it represents, including which credential types and executables make up the plugin.

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMEM1LjM3MSAwIDAgNS41MDcgMCAxMi4zMDNjMCA1LjQzNSAzLjQzOCAxMC4wNDggOC4yMDcgMTEuNjc0LjYwMi4xMTMuODItLjI2NC44Mi0uNTkyIDAtLjI5My0uMDExLTEuMDY2LS4wMTUtMi4wOS0zLjM0Ljc0LTQuMDQzLTEuNjUtNC4wNDMtMS42NS0uNTQ3LTEuNDIzLTEuMzMyLTEuODAzLTEuMzMyLTEuODAzLTEuMDktLjc2MS4wODItLjc0NS4wODItLjc0NSAxLjIwMy4wODggMS44MzYgMS4yNjYgMS44MzYgMS4yNjYgMS4wNyAxLjg4MiAyLjgwOCAxLjMzNyAzLjQ5MiAxLjAyNS4xMS0uNzk3LjQyMi0xLjMzOC43NjItMS42NDYtMi42NjQtLjMwOS01LjQ2NS0xLjM2Ni01LjQ2NS02LjA4IDAtMS4zNDUuNDY4LTIuNDQzIDEuMjM0LTMuMzA0LS4xMjEtLjMwOC0uNTM1LTEuNTYyLjExNy0zLjI1NiAwIDAgMS4wMDgtLjMyOCAzLjMwMSAxLjI2MkExMS4yMjIgMTEuMjIyIDAgMCAxIDEyIDUuOTVjMS4wMi4wMDQgMi4wNDcuMTQgMy4wMDQuNDEzIDIuMjkzLTEuNTkgMy4yOTctMS4yNjIgMy4yOTctMS4yNjIuNjU2IDEuNjk0LjI0NiAyLjk0OC4xMiAzLjI1Ni43Ny44NjEgMS4yMzEgMS45NTkgMS4yMzEgMy4zMDQgMCA0LjcyNi0yLjgwNCA1Ljc2My01LjQ3NiA2LjA3Mi40My4zNzYuODEyIDEuMTMuODEyIDIuMjc1IDAgMS42NDYtLjAxMSAyLjk3MS0uMDExIDMuMzc2IDAgLjMyOC4yMTQuNzEzLjgyNC41OTJDMjAuNTY2IDIyLjM0NyAyNCAxNy43MzcgMjQgMTIuMzAzIDI0IDUuNTA3IDE4LjYyOSAwIDEyIDB6IiBmaWxsPSIjOGU5OGIzIiAvPjwvc3ZnPg==)]Plugin Examples

- [AWS](https://github.com/1Password/shell-plugins/blob/main/plugins/aws/plugin.go)
- [GitHub](https://github.com/1Password/shell-plugins/blob/main/plugins/github/plugin.go)
- [Heroku](https://github.com/1Password/shell-plugins/blob/main/plugins/heroku/plugin.go)

## Step 3: Edit the credential definition[â€‹](#step-3-edit-the-credential-definition "Direct link to Step 3: Edit the credential definition") 

The credential definition file describes the schema of the credential, how the credential should get provisioned to executables, and how the credential can be imported into 1Password.

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMEM1LjM3MSAwIDAgNS41MDcgMCAxMi4zMDNjMCA1LjQzNSAzLjQzOCAxMC4wNDggOC4yMDcgMTEuNjc0LjYwMi4xMTMuODItLjI2NC44Mi0uNTkyIDAtLjI5My0uMDExLTEuMDY2LS4wMTUtMi4wOS0zLjM0Ljc0LTQuMDQzLTEuNjUtNC4wNDMtMS42NS0uNTQ3LTEuNDIzLTEuMzMyLTEuODAzLTEuMzMyLTEuODAzLTEuMDktLjc2MS4wODItLjc0NS4wODItLjc0NSAxLjIwMy4wODggMS44MzYgMS4yNjYgMS44MzYgMS4yNjYgMS4wNyAxLjg4MiAyLjgwOCAxLjMzNyAzLjQ5MiAxLjAyNS4xMS0uNzk3LjQyMi0xLjMzOC43NjItMS42NDYtMi42NjQtLjMwOS01LjQ2NS0xLjM2Ni01LjQ2NS02LjA4IDAtMS4zNDUuNDY4LTIuNDQzIDEuMjM0LTMuMzA0LS4xMjEtLjMwOC0uNTM1LTEuNTYyLjExNy0zLjI1NiAwIDAgMS4wMDgtLjMyOCAzLjMwMSAxLjI2MkExMS4yMjIgMTEuMjIyIDAgMCAxIDEyIDUuOTVjMS4wMi4wMDQgMi4wNDcuMTQgMy4wMDQuNDEzIDIuMjkzLTEuNTkgMy4yOTctMS4yNjIgMy4yOTctMS4yNjIuNjU2IDEuNjk0LjI0NiAyLjk0OC4xMiAzLjI1Ni43Ny44NjEgMS4yMzEgMS45NTkgMS4yMzEgMy4zMDQgMCA0LjcyNi0yLjgwNCA1Ljc2My01LjQ3NiA2LjA3Mi40My4zNzYuODEyIDEuMTMuODEyIDIuMjc1IDAgMS42NDYtLjAxMSAyLjk3MS0uMDExIDMuMzc2IDAgLjMyOC4yMTQuNzEzLjgyNC41OTJDMjAuNTY2IDIyLjM0NyAyNCAxNy43MzcgMjQgMTIuMzAzIDI0IDUuNTA3IDE4LjYyOSAwIDEyIDB6IiBmaWxsPSIjOGU5OGIzIiAvPjwvc3ZnPg==)]Credential Examples

- [AWS Access Key](https://github.com/1Password/shell-plugins/blob/main/plugins/aws/access_key.go)
- [GitHub Personal Access Token](https://github.com/1Password/shell-plugins/blob/main/plugins/github/personal_access_token.go)
- [Heroku API Key](https://github.com/1Password/shell-plugins/blob/main/plugins/heroku/api_key.go)

### Credential information and schema[â€‹](#credential-information-and-schema "Direct link to Credential information and schema") 

The first section of the credential definition is where you can add information about the credential:

- The **name** of the credential, as the platform calls it.
- The **documentation URL** provided by the platform that describes the credential. *(optional)*
- The **management URL** on the platform where the credential can be created and revoked. This is usually a URL to the dashboard, console, or authentication settings of the platform. *(optional)*

The next section is where you define the schema of the credential. This is segmented into fields. Many credentials consist of just a single secret field, but you can add more fields to add more details to the 1Password item that are related to authentication, even if the fields are not secret.

Examples of additional fields are: the host, username, account ID, and all other things that are needed to authenticate and make sense to include in the 1Password item for the credential type. All fields you declare here will also show up in the end user\'s 1Password item.

Here\'s what you can specify per **field**:

- The **field name**, titlecased. *(required)*
- A short **description** of the field. This supports markdown. *(required)*
- Whether the field is **optional**. Defaults to false.
- Whether the field is **secret**, and should be concealed in the 1Password GUI. Defaults to not secret.\
  [Note: The credential schema is expected to contain at least 1 secret field.]
- What the actual credential **value is composed of**. The length, character set, and whether it contains a fixed prefix.

### Provisioner[â€‹](#provisioner "Direct link to Provisioner") 

The credential definition also specifies how the credential is usually provisioned to exectuables, in order for them to use the credential for authentication.

Provisioners are in essence hooks that get executed before the executable is run by 1Password CLI, and after the executable exits in case any cleanup is needed. In those hooks, provisioners can do all the setup required for the executable to authenticate, including setting environment variables, creating files, adding command-line arguments, or even generating temporary credentials. After the executable exits, there should be no trace of the credentials on the user\'s filesystem.

The SDK provides a few common provisioners out of the box, so in most cases you don\'t have to care about the provisioning internals.

- Environment variables
- Files
- Other

We currently recommend using environment variables as your provisioning method.

Environment variables are the most ubiquitous way to provision secrets. They only live in memory, and almost every CLI allows you to authenticate with them.

Here\'s how you can use the environment variable provisioner provided by the SDK:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Specify the 1Password field name and the environment variable name it should be placed in.

To figure out what environment variable the underlying CLI reads, here are a few tips:

- Search the platform\'s CLI documentation website for a getting started guide, authentication guide, or CLI reference docs.
- Look at the CLI\'s help text or manpage.
- If the CLI or the underlying SDK it uses is open source, scan the source code to see if it accepts environment variables for authentication.

Some CLIs only support reading credentials from files on disk. In that case, you can use the file provisioner provided by the SDK. The file provisioner takes care of creating the file in a temporary directory and deleting it afterwards.

For security purposes, the file created by the file provisioner can only be read **once** by the executable. If that limitation does not work for your use case, you can file an [issue on GitHub](https://github.com/1Password/shell-plugins/issues).

Here are a few examples on how you can use the file provisioner to provision a temporary JSON file and pass the generated path to the executable:

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)Create a file provisioner and pass output path as \--config-file

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)Create a file provisioner and set output path as CONFIG_FILE_PATH

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)Create a file provisioner and pass output path as Java property

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiPjxwYXRoIGQ9Ik0xNSwzLjQxNDIxMzU2IEwxNSw3IEwxOC41ODU3ODY0LDcgTDE1LDMuNDE0MjEzNTYgWiBNMTksOSBMMTUsOSBDMTMuODk1NDMwNSw5IDEzLDguMTA0NTY5NSAxMyw3IEwxMywzIEw1LDMgTDUsMjEgTDE5LDIxIEwxOSw5IFogTTUsMSBMMTUuNDE0MjEzNiwxIEwyMSw2LjU4NTc4NjQ0IEwyMSwyMSBDMjEsMjIuMTA0NTY5NSAyMC4xMDQ1Njk1LDIzIDE5LDIzIEw1LDIzIEMzLjg5NTQzMDUsMjMgMywyMi4xMDQ1Njk1IDMsMjEgTDMsMyBDMywxLjg5NTQzMDUgMy44OTU0MzA1LDEgNSwxIFogTTExLjcwNzEwNjgsMTUuMjkyODkzMiBMMTAuMjkyODkzMiwxNi43MDcxMDY4IEw2LjU4NTc4NjQ0LDEzIEwxMC4yOTI4OTMyLDkuMjkyODkzMjIgTDExLjcwNzEwNjgsMTAuNzA3MTA2OCBMOS40MTQyMTM1NiwxMyBMMTEuNzA3MTA2OCwxNS4yOTI4OTMyIFogTTEyLjI5Mjg5MzIsMTIuNzA3MTA2OCBMMTMuNzA3MTA2OCwxMS4yOTI4OTMyIEwxNy40MTQyMTM2LDE1IEwxMy43MDcxMDY4LDE4LjcwNzEwNjggTDEyLjI5Mjg5MzIsMTcuMjkyODkzMiBMMTQuNTg1Nzg2NCwxNSBMMTIuMjkyODkzMiwxMi43MDcxMDY4IFoiIGZpbGwtcnVsZT0iZXZlbm9kZCIgLz48L3N2Zz4=)Code to generate JSON file contents

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If the standard provisioners included in the SDK are not enough to authenticate the executable, you can also write your own provisioner. You can do so by implementing the [`sdk.Provisioner` interface](https://github.com/1Password/shell-plugins/blob/main/sdk/provisioner.go).

A good example of a custom provisioner is the [AWS STS provisioner](https://github.com/1Password/shell-plugins/blob/main/plugins/aws/sts_provisioner.go) that generates temporary credentials based on a one-time password code loaded from 1Password.

### Importer[â€‹](#importer "Direct link to Importer") 

The credential definition also lets you specify importers. Importers are responsible for scanning the user\'s environment and file system for any occurrences of the needed credentials. 1Password CLI will run the importer and prompt the user to import their credentials one by one into 1Password.

It\'s very common for CLIs to write authentication data to disk, most commonly in a hidden config file in your home directory. This is not always documented by the CLI, so here are some tips to figure out if such a config file exists:

- Check the platform\'s documentation for mentions of config files.
- See if the CLI offers a `login`, `auth`, `configure`, or `setup` command that covers authentication. If it does, it\'s pretty likely there\'s a credential being stored in your home directory after completing such a flow.
- If the CLI is open source, check the source code to see if such a file exists.
- Look at your own home directory or `~/.config` directory to see if there are files related to the platform. Here\'s an example command to find local `aws` configuration files:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

The SDK provides helper functions to load files, parse files, and scan environment variables to make writing an importer for your credential type easier.

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMEM1LjM3MSAwIDAgNS41MDcgMCAxMi4zMDNjMCA1LjQzNSAzLjQzOCAxMC4wNDggOC4yMDcgMTEuNjc0LjYwMi4xMTMuODItLjI2NC44Mi0uNTkyIDAtLjI5My0uMDExLTEuMDY2LS4wMTUtMi4wOS0zLjM0Ljc0LTQuMDQzLTEuNjUtNC4wNDMtMS42NS0uNTQ3LTEuNDIzLTEuMzMyLTEuODAzLTEuMzMyLTEuODAzLTEuMDktLjc2MS4wODItLjc0NS4wODItLjc0NSAxLjIwMy4wODggMS44MzYgMS4yNjYgMS44MzYgMS4yNjYgMS4wNyAxLjg4MiAyLjgwOCAxLjMzNyAzLjQ5MiAxLjAyNS4xMS0uNzk3LjQyMi0xLjMzOC43NjItMS42NDYtMi42NjQtLjMwOS01LjQ2NS0xLjM2Ni01LjQ2NS02LjA4IDAtMS4zNDUuNDY4LTIuNDQzIDEuMjM0LTMuMzA0LS4xMjEtLjMwOC0uNTM1LTEuNTYyLjExNy0zLjI1NiAwIDAgMS4wMDgtLjMyOCAzLjMwMSAxLjI2MkExMS4yMjIgMTEuMjIyIDAgMCAxIDEyIDUuOTVjMS4wMi4wMDQgMi4wNDcuMTQgMy4wMDQuNDEzIDIuMjkzLTEuNTkgMy4yOTctMS4yNjIgMy4yOTctMS4yNjIuNjU2IDEuNjk0LjI0NiAyLjk0OC4xMiAzLjI1Ni43Ny44NjEgMS4yMzEgMS45NTkgMS4yMzEgMy4zMDQgMCA0LjcyNi0yLjgwNCA1Ljc2My01LjQ3NiA2LjA3Mi40My4zNzYuODEyIDEuMTMuODEyIDIuMjc1IDAgMS42NDYtLjAxMSAyLjk3MS0uMDExIDMuMzc2IDAgLjMyOC4yMTQuNzEzLjgyNC41OTJDMjAuNTY2IDIyLjM0NyAyNCAxNy43MzcgMjQgMTIuMzAzIDI0IDUuNTA3IDE4LjYyOSAwIDEyIDB6IiBmaWxsPSIjOGU5OGIzIiAvPjwvc3ZnPg==)]Importer Examples

- [AWS Access Key](https://github.com/1Password/shell-plugins/blob/main/plugins/aws/access_key.go) (`~/.aws/credentials`)
- [CircleCI Personal API Token](https://github.com/1Password/shell-plugins/blob/main/plugins/circleci/personal_api_token.go) (`~/.circleci/cli.yml`)
- [Heroku API Key](https://github.com/1Password/shell-plugins/blob/main/plugins/heroku/api_key.go) (`~/.netrc`)

If you already have a shell plugin configured for a tool, and you want to generate an example configuration tile to test an importer, reference the tool by its full path rather than by its name. This makes sure you invoke the the tool without the plugin.

## Step 4: Edit the executable definition[â€‹](#step-4-edit-the-executable-definition "Direct link to Step 4: Edit the executable definition") 

The last thing the plugin is responsible for is to define the CLI or executable that you\'d like 1Password to handle authentication for. This is the final piece that glues everything together.

The executable definition describes the following:

- The **command** that should get executed by the 1Password CLI.
- The display **name** of the CLI, as the platform calls it.
- The **documentation URL** provided by the platform that describes the executable. *(optional)*
- When the executable **needs authentication**. For example, many CLIs don\'t require authentication when the `--help` or `--version` flags are present.
- The **credentials** that the executable uses.

[![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMEM1LjM3MSAwIDAgNS41MDcgMCAxMi4zMDNjMCA1LjQzNSAzLjQzOCAxMC4wNDggOC4yMDcgMTEuNjc0LjYwMi4xMTMuODItLjI2NC44Mi0uNTkyIDAtLjI5My0uMDExLTEuMDY2LS4wMTUtMi4wOS0zLjM0Ljc0LTQuMDQzLTEuNjUtNC4wNDMtMS42NS0uNTQ3LTEuNDIzLTEuMzMyLTEuODAzLTEuMzMyLTEuODAzLTEuMDktLjc2MS4wODItLjc0NS4wODItLjc0NSAxLjIwMy4wODggMS44MzYgMS4yNjYgMS44MzYgMS4yNjYgMS4wNyAxLjg4MiAyLjgwOCAxLjMzNyAzLjQ5MiAxLjAyNS4xMS0uNzk3LjQyMi0xLjMzOC43NjItMS42NDYtMi42NjQtLjMwOS01LjQ2NS0xLjM2Ni01LjQ2NS02LjA4IDAtMS4zNDUuNDY4LTIuNDQzIDEuMjM0LTMuMzA0LS4xMjEtLjMwOC0uNTM1LTEuNTYyLjExNy0zLjI1NiAwIDAgMS4wMDgtLjMyOCAzLjMwMSAxLjI2MkExMS4yMjIgMTEuMjIyIDAgMCAxIDEyIDUuOTVjMS4wMi4wMDQgMi4wNDcuMTQgMy4wMDQuNDEzIDIuMjkzLTEuNTkgMy4yOTctMS4yNjIgMy4yOTctMS4yNjIuNjU2IDEuNjk0LjI0NiAyLjk0OC4xMiAzLjI1Ni43Ny44NjEgMS4yMzEgMS45NTkgMS4yMzEgMy4zMDQgMCA0LjcyNi0yLjgwNCA1Ljc2My01LjQ3NiA2LjA3Mi40My4zNzYuODEyIDEuMTMuODEyIDIuMjc1IDAgMS42NDYtLjAxMSAyLjk3MS0uMDExIDMuMzc2IDAgLjMyOC4yMTQuNzEzLjgyNC41OTJDMjAuNTY2IDIyLjM0NyAyNCAxNy43MzcgMjQgMTIuMzAzIDI0IDUuNTA3IDE4LjYyOSAwIDEyIDB6IiBmaWxsPSIjOGU5OGIzIiAvPjwvc3ZnPg==)]Executable Examples

- [AWS CLI](https://github.com/1Password/shell-plugins/blob/main/plugins/aws/aws.go) (`aws`)
- [GitHub CLI](https://github.com/1Password/shell-plugins/blob/main/plugins/github/gh.go) (`gh`)
- [Heroku CLI](https://github.com/1Password/shell-plugins/blob/main/plugins/heroku/heroku.go) (`heroku`)

## Step 5: Build and test your plugin locally[â€‹](#step-5-build-and-test-your-plugin-locally "Direct link to Step 5: Build and test your plugin locally") 

To see if you\'ve properly filled out the plugin, credential, and executable defintions, you can run the following Makefile command to validate the definitions:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

If that succeeds, it\'s now time to locally build and test your plugin! You can do so using the following command:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

The build artifact will be placed in `~/.op/plugins/local`. It should show up in `op` if you run the following command:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

To see it in action, you can use the `op plugin init` command:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48cGF0aCBkPSJNMTIgMEM1LjM3MSAwIDAgNS41MDcgMCAxMi4zMDNjMCA1LjQzNSAzLjQzOCAxMC4wNDggOC4yMDcgMTEuNjc0LjYwMi4xMTMuODItLjI2NC44Mi0uNTkyIDAtLjI5My0uMDExLTEuMDY2LS4wMTUtMi4wOS0zLjM0Ljc0LTQuMDQzLTEuNjUtNC4wNDMtMS42NS0uNTQ3LTEuNDIzLTEuMzMyLTEuODAzLTEuMzMyLTEuODAzLTEuMDktLjc2MS4wODItLjc0NS4wODItLjc0NSAxLjIwMy4wODggMS44MzYgMS4yNjYgMS44MzYgMS4yNjYgMS4wNyAxLjg4MiAyLjgwOCAxLjMzNyAzLjQ5MiAxLjAyNS4xMS0uNzk3LjQyMi0xLjMzOC43NjItMS42NDYtMi42NjQtLjMwOS01LjQ2NS0xLjM2Ni01LjQ2NS02LjA4IDAtMS4zNDUuNDY4LTIuNDQzIDEuMjM0LTMuMzA0LS4xMjEtLjMwOC0uNTM1LTEuNTYyLjExNy0zLjI1NiAwIDAgMS4wMDgtLjMyOCAzLjMwMSAxLjI2MkExMS4yMjIgMTEuMjIyIDAgMCAxIDEyIDUuOTVjMS4wMi4wMDQgMi4wNDcuMTQgMy4wMDQuNDEzIDIuMjkzLTEuNTkgMy4yOTctMS4yNjIgMy4yOTctMS4yNjIuNjU2IDEuNjk0LjI0NiAyLjk0OC4xMiAzLjI1Ni43Ny44NjEgMS4yMzEgMS45NTkgMS4yMzEgMy4zMDQgMCA0LjcyNi0yLjgwNCA1Ljc2My01LjQ3NiA2LjA3Mi40My4zNzYuODEyIDEuMTMuODEyIDIuMjc1IDAgMS42NDYtLjAxMSAyLjk3MS0uMDExIDMuMzc2IDAgLjMyOC4yMTQuNzEzLjgyNC41OTJDMjAuNTY2IDIyLjM0NyAyNCAxNy43MzcgMjQgMTIuMzAzIDI0IDUuNTA3IDE4LjYyOSAwIDEyIDB6IiBmaWxsPSIjOGU5OGIzIiAvPjwvc3ZnPg==) Submit a PR[â€‹](#-submit-a-pr "Direct link to -submit-a-pr") 

While you\'re free to keep on using the plugin locally, we\'d encourage you to submit a PR on the [main registry on GitHub](https://github.com/1Password/shell-plugins) so others can use it too!

Before doing so, be sure to read the [CONTRIBUTING.md](https://github.com/1Password/shell-plugins/blob/main/CONTRIBUTING.md) file on GitHub.

If you feel that the SDK does not serve your use case well, reach out to us by creating an [issue on GitHub](https://github.com/1Password/shell-plugins/issues) or by joining our [Developer Slack workspace](https://developer.1password.com/joinslack) to tell us about your plugin proposal. We can advise you on the most suitable approach for your use case.

## Learn more[â€‹](#learn-more "Direct link to Learn more") 

- [Shell plugins troubleshooting](/docs/cli/shell-plugins/troubleshooting/)
- [Join our Developer Slack workspace](https://developer.1password.com/joinslack)