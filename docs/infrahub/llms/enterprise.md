# Source: https://docs.infrahub.app/demo-dc/enterprise.md

# Using Infrahub Enterprise

This guide explains how to configure the demo environment to use Infrahub Enterprise edition instead of the Community edition. Enterprise edition provides additional features including increased performance, enhanced security, and enterprise support.

## Understanding the editions[​](#understanding-the-editions "Direct link to Understanding the editions")

Infrahub is available in two editions:

* **Community edition** - The standard open-source version with core functionality
* **Enterprise edition** - The commercial version with additional enterprise features

The demo environment supports both editions and can be switched between them with a single configuration change.

## Configuration[​](#configuration "Direct link to Configuration")

Edition selection is controlled by environment variables in the `.env` file at the root of the demo repository. The key variable is `INFRAHUB_ENTERPRISE`:

```
# Community edition (default)
export INFRAHUB_ENTERPRISE="false"

# Enterprise edition
export INFRAHUB_ENTERPRISE="true"
```

### Environment variables reference[​](#environment-variables-reference "Direct link to Environment variables reference")

| Variable              | Default                 | Description                                                         |
| --------------------- | ----------------------- | ------------------------------------------------------------------- |
| `INFRAHUB_ENTERPRISE` | `false`                 | Set to `true` to use Enterprise edition                             |
| `INFRAHUB_VERSION`    | `stable`                | Infrahub version to use (for example, `1.5.1`, `stable`, `develop`) |
| `INFRAHUB_ADDRESS`    | `http://localhost:8000` | Infrahub API address                                                |
| `INFRAHUB_API_TOKEN`  | (demo token)            | API authentication token                                            |

## Switching to Enterprise edition[​](#switching-to-enterprise-edition "Direct link to Switching to Enterprise edition")

To switch from Community to Enterprise edition:

### Step 1: update the configuration[​](#step-1-update-the-configuration "Direct link to Step 1: update the configuration")

Edit the `.env` file in the root of the demo repository:

```
# Change this line from "false" to "true"
export INFRAHUB_ENTERPRISE="true"
```

### Step 2: source the environment file[​](#step-2-source-the-environment-file "Direct link to Step 2: source the environment file")

For the changes to take effect, source the environment file:

```
source .env
```

### Step 3: verify the configuration[​](#step-3-verify-the-configuration "Direct link to Step 3: verify the configuration")

Check that the Enterprise edition will be used:

```
uv run invoke info
```

You should see output similar to:

```
Infrahub Edition: Enterprise
Version: 1.5.1
Command: curl -s https://infrahub.opsmill.io/enterprise/1.5.1 | ...
```

### Step 4: restart Infrahub[​](#step-4-restart-infrahub "Direct link to Step 4: restart Infrahub")

To apply the change, destroy the existing environment and start fresh:

```
# Stop and remove all containers and volumes
uv run invoke destroy

# Start with Enterprise edition
uv run invoke start
```

tip

The `destroy` command removes all containers and data volumes. If you have data you want to preserve, consider exporting it first using `infrahubctl`.

### Step 5: reload your data[​](#step-5-reload-your-data "Direct link to Step 5: reload your data")

After switching editions, you'll need to reload your schemas and data:

```
uv run invoke bootstrap
```

## Switching back to Community edition[​](#switching-back-to-community-edition "Direct link to Switching back to Community edition")

To switch from Enterprise back to Community edition, follow the same process but set `INFRAHUB_ENTERPRISE="false"`:

```
# Edit .env and change to "false"
source .env

# Verify configuration
uv run invoke info

# Restart
uv run invoke destroy
uv run invoke start
```

## How it works[​](#how-it-works "Direct link to How it works")

When you run `uv run invoke start`, the system constructs the appropriate Docker Compose command based on your configuration:

**Community edition URL pattern:**

```
https://infrahub.opsmill.io/{VERSION}
```

**Enterprise edition URL pattern:**

```
https://infrahub.opsmill.io/enterprise/{VERSION}
```

The invoke tasks in `tasks.py` automatically detect the `INFRAHUB_ENTERPRISE` setting and use the correct URL to download the appropriate Docker Compose configuration.

## Checking your current edition[​](#checking-your-current-edition "Direct link to Checking your current edition")

At any time, you can check which edition you're configured to use:

```
source .env && uv run invoke info
```

This displays:

* The edition (Community or Enterprise)
* The version being used
* The full Docker Compose command

## Enterprise features[​](#enterprise-features "Direct link to Enterprise features")

Enterprise edition includes additional capabilities not available in Community edition. For details on specific enterprise features, refer to the [Infrahub documentation](https://docs.infrahub.app).

info

Enterprise edition requires valid licensing for production usage. Contact OpsMill for enterprise licensing information.

## Troubleshooting[​](#troubleshooting "Direct link to Troubleshooting")

### Changes not taking effect[​](#changes-not-taking-effect "Direct link to Changes not taking effect")

If you change the `INFRAHUB_ENTERPRISE` setting but the wrong edition starts:

1. Ensure you sourced the `.env` file: `source .env`
2. Verify the setting with `uv run invoke info`
3. Make sure you destroyed the old environment before starting: `uv run invoke destroy`

### Environment file not found[​](#environment-file-not-found "Direct link to Environment file not found")

If you get errors about missing environment variables:

1. Ensure the `.env` file exists in the root of the demo repository
2. Make sure you're running commands from the demo repository root
3. Source the file explicitly: `source .env`

## Best practices[​](#best-practices "Direct link to Best practices")

* **Use explicit versions** - Instead of `stable`, specify exact versions like `1.5.1` for reproducible environments
* **Document your choice** - Note which edition you're using in project documentation
* **Test on Community first** - Validate your schemas and generators on Community edition before deploying to Enterprise
* **Keep configurations in sync** - If working in a team, ensure everyone uses the same edition for consistency

## Additional resources[​](#additional-resources "Direct link to Additional resources")

* [Infrahub documentation](https://docs.infrahub.app)
* [OpsMill website](https://opsmill.com)
* [Enterprise edition details](https://opsmill.com/pricing)
