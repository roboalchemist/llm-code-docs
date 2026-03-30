# Source: https://docs.infrahub.app/guides/configuration-changes.md

# How to configure Infrahub

This guide explains how to configure your Infrahub instance by setting environment variables that control various aspects of the system, including timeouts, security settings, and integration parameters.

## What you'll accomplish[​](#what-youll-accomplish "Direct link to What you'll accomplish")

By following this guide, you'll learn how to:

* Identify available configuration options
* Set environment variables in various deployment methods
* Apply configuration changes to a running Infrahub instance
* Verify that your changes have been applied correctly

## Prerequisites[​](#prerequisites "Direct link to Prerequisites")

Before starting, ensure you have:

* A running Infrahub instance
* Command-line access to the server running Infrahub
* Basic understanding of environment variables
* For production deployments, plan a maintenance window as services will be restarted

## Step 1: Identify the configuration option[​](#step-1-identify-the-configuration-option "Direct link to Step 1: Identify the configuration option")

Determine which configuration setting you want to change.

1. Refer to the [configuration reference](/reference/configuration.md) to find available environment variables
2. Note the exact variable name and its expected value type

info

For this guide, we'll use `INFRAHUB_HTTP_TIMEOUT` as an example. It affects how Infrahub interacts with external HTTP servers such as webhooks and OAuth2 providers. The default value is 10 seconds.

## Step 2: Set the variable[​](#step-2-set-the-variable "Direct link to Step 2: Set the variable")

Configure the variable before starting or restarting your Infrahub containers.

* Docker Compose
* Kubernetes

note

Using a `.env` file keeps your configuration organized and allows you to track changes with version control.

warning

Avoid hardcoding information directly in the `docker-compose.yml` file. Part of the upgrade process consists of replacing this file, which could lead to loss of your configuration. Avoid mixing multiple configuration methods as it can lead to confusion about which settings are applied.

### Option A: use a .env file (recommended)[​](#option-a-use-a-env-file-recommended "Direct link to Option A: use a .env file (recommended)")

Create or edit a `.env` file in the same directory as your `docker-compose.yml` file:

.env

```
INFRAHUB_HTTP_TIMEOUT=20
```

This method is preferred for persistent configuration as Docker Compose automatically loads variables from the `.env` file.

### Option B: export in your shell[​](#option-b-export-in-your-shell "Direct link to Option B: export in your shell")

Export the environment variable in your shell session:

```
export INFRAHUB_HTTP_TIMEOUT=20
```

This method works for temporary changes or testing, but the variable persists only for the current shell session.

### Option C: use a .toml file (not recommended)[​](#option-c-use-a-toml-file-not-recommended "Direct link to Option C: use a .toml file (not recommended)")

Create or edit an `infrahub.toml` file with your configuration:

infrahub.toml

```
[settings]
http_timeout = 20
```

Then reference the TOML file when starting Infrahub. The application will automatically load configuration from the TOML file.

note

TOML configuration files use lowercase with underscores for setting names (for example, `http_timeout`) rather than the uppercase environment variable format (for example, `INFRAHUB_HTTP_TIMEOUT`).

### Use Helm values[​](#use-helm-values "Direct link to Use Helm values")

Update your `values.yaml` or provide values during upgrade:

values.yaml

```
infrahubServer:
  infrahubServer:
    env:
      INFRAHUB_HTTP_TIMEOUT: "20"
infrahubTaskWorker:
  infrahubTaskWorker:
    env:
      INFRAHUB_HTTP_TIMEOUT: "20"
```

Or set directly via command line:

```
helm upgrade infrahub opsmill/infrahub \
  --set infrahubServer.infrahubServer.env.INFRAHUB_HTTP_TIMEOUT=20 --set infrahubTaskWorker.infrahubTaskWorker.env.INFRAHUB_HTTP_TIMEOUT=20 \
  -n <your-namespace>
```

## Step 3: Apply the configuration changes[​](#step-3-apply-the-configuration-changes "Direct link to Step 3: Apply the configuration changes")

Restart your Infrahub containers to apply the new configuration.

* Docker Compose
* Kubernetes

note

Depending on your setup, you might need to adjust the commands below to add options.

Recreate and restart your Docker containers to apply the changes:

```
docker compose up -d --force-recreate
```

The `--force-recreate` flag ensures that containers are recreated even if their configuration and images haven't changed, which is necessary for applying new environment variables.

warning

This command restarts all services defined in your `docker-compose.yml` file. There will be a brief service interruption during the restart.

### For Helm deployments[​](#for-helm-deployments "Direct link to For Helm deployments")

If you're using Helm, upgrade your release with the new values:

```
helm upgrade infrahub opsmill/infrahub \
  -f values.yaml \
  -n <your-namespace>
```

Or with inline values:

```
helm upgrade infrahub opsmill/infrahub \
  --set infrahubServer.infrahubServer.env.INFRAHUB_HTTP_TIMEOUT=20 --set infrahubTaskWorker.infrahubTaskWorker.env.INFRAHUB_HTTP_TIMEOUT=20 \
  -n <your-namespace>
```

warning

Rolling out changes will trigger a pod restart. Depending on your deployment configuration (replicas, rolling update strategy), there may be a brief service interruption.

## Step 4: Verify the configuration[​](#step-4-verify-the-configuration "Direct link to Step 4: Verify the configuration")

Confirm that your configuration change has been applied successfully.

* Docker Compose
* Kubernetes

note

Depending on your setup, you might need to adjust the commands below to match your container names if you are using a different project name for instance.

Check that the environment variable is set correctly inside the container:

```
docker exec infrahub-server-1 env | grep INFRAHUB_HTTP_TIMEOUT
```

You should see output similar to:

```
INFRAHUB_HTTP_TIMEOUT=20
```

success

If you see the expected value in the output, your configuration change has been applied successfully.

note

Replace `<your-namespace>` and `infrahub-server-*` with your actual namespace and pod name.

First, get the name of your Infrahub pod:

```
kubectl get pods -n <your-namespace> -l app=infrahub-server
```

Then check the environment variable inside the pod:

```
kubectl exec -n <your-namespace> <pod-name> -- env | grep INFRAHUB_HTTP_TIMEOUT
```

For example:

```
kubectl exec -n infrahub infrahub-server-7d8f9b5c6d-xyz12 -- env | grep INFRAHUB_HTTP_TIMEOUT
```

You should see output similar to:

```
INFRAHUB_HTTP_TIMEOUT=20
```

Alternatively, you can describe the pod to see all environment variables:

```
kubectl describe pod -n <your-namespace> <pod-name>
```

success

If you see the expected value in the output, your configuration change has been applied successfully.

## Related resources[​](#related-resources "Direct link to Related resources")

* [Configuration reference](/reference/configuration.md) - Complete list of available environment variables
* [Production deployment](/guides/production-deployment.md) - Best practices for deploying Infrahub
* [Installing Infrahub](/guides/installation.md) - Installation methods for Infrahub
