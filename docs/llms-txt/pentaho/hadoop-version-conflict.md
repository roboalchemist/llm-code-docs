# Source: https://docs.pentaho.com/install/9.3-install/pentaho-configuration/tasks-to-be-performed-by-an-it-administrator/set-up-the-adaptive-execution-layer-ael/troubleshooting-ael-cp/hadoop-version-conflict.md

# Hadoop version conflict

On an HDP cluster, if you receive the following message, your Hadoop library is in conflict and the AEL daemon along with the PDI client might stop working:

```
command hdp-select is not found, please manually *export HDP_VERSION* in spark-env.sh or current environment

```

To resolve the issue, you must export the HDP\_VERSION variable using a command like the following example:

```
export HDP_VERSION=${HDP_VERSION:-2.6.0.3-8}

```

The HDP version number should match the HDP version number of the distribution on the cluster. You can check your HDP version with the `hdp-select status hadoop-client` command.
