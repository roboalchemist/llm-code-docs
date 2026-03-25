# Source: https://docs.anyscale.com/container-image/troubleshoot.md

# Troubleshoot custom image issues

[View Markdown](/container-image/troubleshoot.md)

# Troubleshoot custom image issues

This page contains troubleshooting tips for common issues while working with custom container images on Anyscale.

## Clusters or nodes fail to start[​](#clusters-fail "Direct link to Clusters or nodes fail to start")

If your cluster fails to start or you can't attach a node, review the cluster's event log to identify issues.

Workspaces, jobs, and services use a common layout for cluster event logs. To review event logs, complete the following steps:

1. Log in to the Anyscale console.
2. Click **Workspaces**, **Jobs**, or **Services**.
3. Click the name of your Ray application.

The event logs are now visible under **Events**.

## Debug workspace utilities[​](#debug-utilities "Direct link to Debug workspace utilities")

Interactive workspace utilities sometimes fail to load properly on custom images. The following table shows where you can find the log files for each utility:

| Utility | Log path               |
| ------- | ---------------------- |
| Jupyter | `/tmp/ray/jupyter.log` |
| VS Code | `/tmp/ray/vscode.log`  |

## Run the image locally[​](#run-locally "Direct link to Run the image locally")

If you try to run your image locally using `docker run -it <your-image>`, you might get an error similar to the following:

```
Error: Format string '/home/ray/anaconda3/bin/anyscale session web_terminal_server --deploy-environment %(ENV_ANYSCALE_DEPLOY_ENVIRONMENT)s --cli-token %(ENV_ANYSCALE_CLI_TOKEN)s --host %(ENV_ANYSCALE_HOST)s --working-dir %(ENV_ANYSCALE_WORKING_DIR)s --session-id %(ENV_ANYSCALE_SESSION_ID)s' for 'program:web_terminal_server.command' contains names ('ENV_ANYSCALE_DEPLOY_ENVIRONMENT') which cannot be expanded. Available names: ENV_BUILD_DATE, ENV_HOME, ENV_HOSTNAME, ENV_LANG, ENV_LC_ALL, ENV_LOGNAME, ENV_PATH, ENV_PWD, ENV_PYTHONUSERBASE, ENV_RAY_USAGE_STATS_ENABLED, ENV_RAY_USAGE_STATS_PROMPT_ENABLED, ENV_RAY_USAGE_STATS_SOURCE, ENV_SHELL, ENV_SUDO_COMMAND, ENV_SUDO_GID, ENV_SUDO_UID, ENV_SUDO_USER, ENV_TERM, ENV_TZ, ENV_USER, group_name, here, host_node_name, process_num, program_name in section 'program:web_terminal_server' (file: '/etc/supervisor/conf.d/supervisord.conf')
```

Anyscale's custom entrypoint requires certain environment variables. You can manually override the entrypoint and get an interactive bash shell when running the image locally with the following command:

```
docker run -it --entrypoint bash <your-image>
```

## Docker write: no space left on device[​](#no-space "Direct link to Docker write: no space left on device")

If you're pulling a large image, you may run out of disk space on your nodes. You can work around this by configuring a larger volume in the cloud-specific [compute configuration options](/configuration/compute.md)'s advanced options:

The following is an example configuration to specify a 250GB volume for node-attached block storage volumes:

```
{
  "BlockDeviceMappings": [
    {
      "DeviceName": "/dev/sda1",
      "Ebs": {
        "VolumeSize": 250,
        "DeleteOnTermination": true
      }
    }
  ]
}
```

note

Always set `DeleteOnTermination` to `true` to clean up the volume after the instance terminates.
