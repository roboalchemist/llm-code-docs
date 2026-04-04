# Source: https://developers.webflow.com/cli/command-reference.mdx

***

title: Command Reference
subtitle: Reference for all commands available in the Webflow CLI
slug: command-reference
description: Reference for all commands available in the Webflow CLI
keywords: 'webflow, cli, commands'
max-toc-depth: 3
hidden: false
-------------

## Global Options

Global options can be used with any command.

| Option            | Description                                       |
| ----------------- | ------------------------------------------------- |
| `-V`, `--version` | Display the installed version of the Webflow CLI. |
| `-h`, `--help`    | Display help information for any command.         |

***

## Authentication

### `auth login`

Authenticates the CLI with your Webflow account.

**Usage**

```bash
webflow auth login
```

This command opens your browser to complete authentication. For more details, see the [authentication documentation](./authentication).

***

## Code Components

### `library share`

Bundles and shares your Code Component library with a Webflow Workspace.

**Usage**

```bash
webflow library share [options]
```

**Options**

| Option            | Description                                         | Default                                         |
| ----------------- | --------------------------------------------------- | ----------------------------------------------- |
| `--manifest`      | Path to the `webflow.json` file.                    | Scans the current directory.                    |
| `--api-token`     | Workspace API token.                                | Uses `WEBFLOW_WORKSPACE_API_TOKEN` from `.env`. |
| `--no-input`      | Disables interactive prompts. Useful for CI/CD.     | `false`                                         |
| `--force`         | Forces bundling to complete, even with warnings.    | `false`                                         |
| `--debug-bundler` | Displays final bundler configuration for debugging. | `false`                                         |
| `--dev`           | Bundles in development mode.                        | `false`                                         |
| `--verbose`       | Displays extra information for debugging.           | `false`                                         |

**Example**

```bash
# Share the library and bypass any interactive prompts
webflow library share --no-input
```

### `library bundle`

Bundles a library of Code Components locally to a `dist` directory. This command does not share the library to Webflow.

**Usage**

```bash
webflow library bundle [options]
```

**Options**

| Option                 | Description                                         | Default  |
| ---------------------- | --------------------------------------------------- | -------- |
| `--public-path <path>` | Overrides the public path for the bundle.           |          |
| `--output-path <path>` | Overrides the output path for the bundle.           | `./dist` |
| `--force`              | Forces bundling to complete, even with warnings.    | `false`  |
| `--debug-bundler`      | Displays final bundler configuration for debugging. | `false`  |
| `--dev`                | Bundles in development mode.                        | `false`  |
| `--verbose`            | Displays extra information for debugging.           | `false`  |

**Example**

```bash
# Bundle the library and output to a 'build' folder
webflow library bundle --output-path ./build
```

### `library log`

Displays the directory and path to the latest log file.

**Usage**

```bash
webflow library log
```

***

## Webflow Cloud

### `cloud init`

Initializes a new Webflow Cloud project from a template.

**Usage**

```bash
webflow cloud init [options]
```

**Options**

| Option              | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `--framework`, `-f` | The framework to use for the project (e.g., `astro`). |
| `--mount`, `-m`     | The path to mount the project on (e.g., `/app`).      |
| `--site-id`, `-s`   | The Webflow site ID to connect to.                    |

**Example**

```bash
# Initialize a new Astro project mounted at /app on a specific site
webflow cloud init -f astro -m /app -s 1234567890
```

### `cloud list`

Lists available project templates for `cloud init`.

**Usage**

```bash
webflow cloud list
```

### `cloud deploy`

Deploys your project to Webflow Cloud.

**Usage**

```bash
webflow cloud deploy [options]
```

**Options**

| Option                    | Description                                                   |
| ------------------------- | ------------------------------------------------------------- |
| `--env`, `-e`             | The environment name to deploy to.                            |
| `--mount`, `-m`           | The path to mount the project on (e.g. `/app`).               |
| `--project-name`, `-p`    | Project name (when deploying a new project).                  |
| `--directory`, `-d`       | Project directory path if not in the root (for new projects). |
| `--description`, `-d`     | Project description (when deploying a new project).           |
| `--skip-mount-path-check` | Skips interactive prompts for mount path configuration.       |
| `--auto-publish`          | Publishes the site after deployment.                          |

<Tip title="Configuration for CI/CD pipelines">
  When used together, `--env` and `--mount` enable non-interactive deployments suitable for CI/CD pipelines. You can also use
  `--auto-publish` to publish the site after deployment so that your new environment is live.

  ```bash
  webflow cloud deploy -e production -m /app --auto-publish
  ```

  This will deploy the project to the environment named "production" and mount it at `/app`, and then publish the site so that your new environment is live.
</Tip>

***

## DevLink

### `devlink sync`

Syncs components from your Webflow site to your local project.

**Usage**

```bash
webflow devlink sync [options]
```

**Options**

| Option              | Description                                           |
| ------------------- | ----------------------------------------------------- |
| `--api-token`, `-t` | The API token to use, overriding the `.env` file.     |
| `--site-id`, `-s`   | The site ID to sync from, overriding the `.env` file. |

**Example**

```bash
# Sync components using a specific site ID and token
webflow devlink sync --site-id 1234567890 --api-token <YOUR_TOKEN>
```

***

## Designer Extensions

### `extension list`

Lists available templates for `extension init`.

**Usage**

```bash
webflow extension list
```

### `extension init`

Initializes a new Designer Extension project from a template.

**Usage**

```bash
webflow extension init <project-name> <template>
```

**Arguments**

| Argument       | Description                                                  |
| -------------- | ------------------------------------------------------------ |
| `project-name` | The name of your new project directory.                      |
| `template`     | The template to use: 'default', 'react' or 'typescript-alt'. |

**Example**

```bash
# Initialize a new React-based extension in a 'my-new-extension' folder
webflow extension init my-new-extension react
```

### `extension bundle`

Bundles your Designer Extension into a `bundle.zip` file for upload.

**Usage**

```bash
webflow extension bundle
```

### `extension serve`

Serves your Designer Extension on a local development server.

**Usage**

```bash
webflow extension serve [port]
```

**Arguments**

| Argument | Description                       | Default |
| -------- | --------------------------------- | ------- |
| `port`   | The port to serve the project on. | `1337`  |
