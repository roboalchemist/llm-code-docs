# Source: https://docs.socket.dev/docs/socket-scan-github.md

# socket scan github

Additional options to create Socket scans for Github repos

Create Socket security scans directly from GitHub repositories

```
socket scan github --help

  Create a scan for given GitHub repo

  Usage
    $ socket scan github [options] [CWD=.]

  API Token Requirements
    - Quota: 1 unit
    - Permissions: full-scans:create

  This is similar to the `socket scan create` command except it pulls the files
  from GitHub. See the help for that command for more details.

  A GitHub Personal Access Token (PAT) will at least need read access to the repo
  ("contents", read-only) for this command to work.

  Note: This command cannot run the `socket manifest auto` things because that
  requires local access to the repo while this command runs entirely through the
  GitHub for file access.

  You can use `socket scan setup` to configure certain repo flag defaults.

  Options
    --all               Apply for all known repositories reported by the Socket API. Supersedes `repos`.
    --github-api-url    Base URL of the GitHub API (default: https://api.github.com)
    --github-token      Required GitHub token for authentication.
                        May set environment variable GITHUB_TOKEN or SOCKET_CLI_GITHUB_TOKEN instead.
    --interactive       Allow for interactive elements, asking for input. Use --no-interactive to prevent any input questions, defaulting them to cancel/no.
    --json              Output as JSON
    --markdown          Output as Markdown
    --org               Force override the organization slug, overrides the default org from config
    --org-github        Alternate GitHub Org if the name is different than the Socket Org
    --repos             List of repos to target in a comma-separated format (e.g., repo1,repo2). If not specified, the script will pull the list from Socket and ask you to pick one. Use --all to use them all.

  Examples
    $ socket scan github
    $ socket scan github ./proj
```

<br />

The `socket scan github` command allows you to create security scans for repositories hosted on GitHub without needing to clone them locally. Additionally, `socket scan github` can be used to trigger Socket scans across multiple GitHub repositories.

## How it works

Unlike `socket scan create` which requires local files, `socket scan github` pulls files directly from GitHub using the GitHub API.

The command analyzes your project's dependencies by reading manifest files directly from GitHub rather than running `socket scan create` in a local copy of the GitHub repository.

**Important limitation**: Because this command accesses files remotely through GitHub's API, it cannot run local tools like `socket manifest auto` that require direct filesystem access. If you need those capabilities, use `socket scan create` with a locally cloned repository instead.

## Prerequisites

### 1. Socket API Token

`socket scan github` command requires a Socket API token with the following permissions:

* `full-scans:create`

You can generate an API token from your Socket dashboard under **Settings > Security Policy**.

Once a Socket API Token has been generated, you can configure Socket to use the API token using either:

* **CLI:** `socket login` and following the guide
* **Environment variable:** set the `SOCKET_SECURITY_API_TOKEN` environment variable (e.g. `export SOCKET_SECURITY_API_TOKEN=your_api_token`)

### 2. GitHub Authentication

In order for Socket to be able to access your GitHub repositories, a GitHub Personal Access Token (PAT) with the following permissions will need to be created:

* `Contents: read-only`

Note: a GitHub PAT is required even for organizations that have installed the Socket GitHub application.

You can provide your GitHub token in three ways. Both `GITHUB_TOKEN` and `SOCKET_CLI_GITHUB_TOKEN` are valid environment variables to use.

1. **CLI parameter:** pass in your GitHub token using the `--github-token` flag e.g. `socket scan github --github-token REPLACE_ME`
2. **Environment variable:** set the `GITHUB_TOKEN` environment variable e.g. `export GITHUB_TOKEN=REPLACE_ME`
3. **Environment variable:** set the `SOCKET_CLI_GITHUB_TOKEN` environment variable e.g. `export SOCKET_CLI_GITHUB_TOKEN=REPLACE_ME`

## Usage

### Basic usage

Scan a single repository using an interactive guide

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github
```

Provides an interactive prompt to select which GitHub repository you wish to create a Socket scan for. from a list of available repositories known to Socket in your organization.

### Scan specific repositories

Scan one or more specific repositories by name. For multiple repos use a comma-separated format.

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --repos repo-name
socket scan github --repos repo1,repo2,repo3
```

Repository names should be just the repository name listed in GitHub (not including the organization or owner).

### Scan all repositories

Scan all known repositories reported by the Socket API. Will supersede the `--repos` flag.

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --all
```

## Options

### `--all`

Scan all repositories known to Socket in your GitHub organization. This supersedes the `--repos` option.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --all
```

### `--github-api-url`

Specify a custom base URL for the GitHub API. This is useful for GitHub Enterprise instances.

**Default:** `https://api.github.com`

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --github-api-url https://github.enterprise.com/api/v3
```

### `--github-token`

Provide your GitHub Personal Access Token (PAT) for authentication.

**Example:**

```bash
socket scan github --github-token REPLACE_ME
```

**Using environment variables:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github
```

### `--interactive` / `--no-interactive`

Control whether the command can prompt you for input.

* `--interactive` (default): Allows the CLI to ask questions and prompt for selections
* `--no-interactive`: Prevents any input prompts, defaulting them to cancel/no

The `--no-interactive` flag is particularly useful in CI/CD environments where you can't respond to prompts.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --no-interactive --repos my-repo
```

### `--json`

Output the scan results as JSON instead of the default formatted output. This is useful for piping results to other tools or scripts.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --repos my-repo --json
```

### `--markdown`

Output the scan results as Markdown. Works well for for copying into GitHub issues, pull requests, or documentation.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --repos my-repo --markdown > scan-results.md
```

### `--org`

Force override of your Socket organization slug.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --org my-other-org --repos my-repo
```

### `--org-github`

Specify an alternate GitHub organization name. Should be used when your GitHub organization name differs from your Socket organization name.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --org socket-or-name --org-github github-org-name
```

### `--repos`

Specify a comma-separated list of repository names to scan. Can be used to scan multiple GitHub repositories using the same scan settings.

**Example:**

```bash
export GITHUB_TOKEN=REPLACE_ME
socket scan github --repos repo1,repo2,repo3
```

<br />