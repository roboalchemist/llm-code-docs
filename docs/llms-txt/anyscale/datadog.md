# Source: https://docs.anyscale.com/monitoring/datadog.md

# Datadog

[View Markdown](/monitoring/datadog.md)

# Datadog

Integrate with Datadog on Anyscale using one of the following two integrations:

1. [Vector](/monitoring/exporting-logs.md) (Recommended)
2. Ray integration with Datadog Agent

The Vector integration is strongly recommended because:

* it has a one time setup
* Ray emits any new metrics without any host configuration changes
* you can [easily clone](#datadog-dashboards) the Grafana dashboards provided by Anyscale and convert them into Datadog dashboards

The Datadog Agent integration has significant limitations because:

* it requires additional configurations
* supports a [limited set of metrics](#metrics-limitations)
* it's [incompatible with Vector](#vector-incompatibility)
* you can't clone the Grafana dashboards provided by Anyscale

One of the few reasons to use the Datadog Agent integration is to get host metrics.

## Ray integration with Datadog Agent[​](#ray-integration-with-datadog-agent "Direct link to Ray integration with Datadog Agent")

Set up Anyscale clusters with the Ray integration for the [Datadog Agent](https://docs.datadoghq.com/agent), a plugin that Datadog designed to send events, metrics, and logs from Ray clusters to Datadog. It includes a dedicated dashboard.

Before you proceed with this Datadog Agent integration, consider using the recommended [Vector](/monitoring/exporting-logs.md) integration.

### Pre-requisites[​](#pre-requisites "Direct link to Pre-requisites")

* Datadog API Key. [Create a key](https://docs.datadoghq.com/account_management/api-app-keys/) for your account.

### Setup[​](#setup "Direct link to Setup")

Create a [custom container image](/container-image/build-image.md) on Anyscale to configure the Datadog Agent with Ray. You can use this image for any of your Anyscale workloads. This guide pre-configures the Datadog Agent to emit appropriate settings so you can use the Ray integration from Datadog.

#### 1. Configure scripts for agent configuration[​](#1-configure-scripts-for-agent-configuration "Direct link to 1. Configure scripts for agent configuration")

Create a script to configure the Datadog agent with appropriate settings. The script sets the hostname, enables logs, sets the metrics endpoint, and adds tags to the host.

datadog.sh

```
#/bin/bash

echo "Updating Datadog Ray integration configuration"

DD_SITE="datadoghq.com" 

# Set DD_HOSTNAME based which ANYSCALE_EXPERIMENTAL_WORKSPACE_ID,  ANYSCALE_JOB_ID or ANYSCALE_SERVICE_ID
if [ -n "$ANYSCALE_EXPERIMENTAL_WORKSPACE_ID" ]; then
    export DD_HOSTNAME=$ANYSCALE_EXPERIMENTAL_WORKSPACE_ID
elif [ -n "$ANYSCALE_JOB_ID" ]; then
    export DD_HOSTNAME=$ANYSCALE_JOB_ID
elif [ -n "$ANYSCALE_SERVICE_ID" ]; then
    export DD_HOSTNAME=$ANYSCALE_SERVICE_ID
fi

# Replace _ with - in hostname to make it RFC 1123 compliant
DD_HOSTNAME=$(echo "$DD_HOSTNAME" | sed 's/_/-/g')

# Enable logs
sudo yq ".logs_enabled = true" -i /etc/datadog-agent/datadog.yaml

# Configure hostname
sudo DD_HOSTNAME=$DD_HOSTNAME yq -i '.hostname = strenv(DD_HOSTNAME)' /etc/datadog-agent/datadog.yaml

### Add tags to DataDog host ###
# Have to initialize tags with empty strings so yq adds these as strings with quotes
# cluster_id:{ANYSCALE_CLUSTER_ID}
sudo yq -i '.tags[0] = " "' /etc/datadog-agent/datadog.yaml 
sudo ANYSCALE_CLUSTER_ID="cluster_id:${ANYSCALE_CLUSTER_ID}" yq -i '.tags[0] = strenv(ANYSCALE_CLUSTER_ID)' /etc/datadog-agent/datadog.yaml 

# instance_id:{ANYSCALE_INSTANCE_ID}
sudo yq -i '.tags[1] = " "' /etc/datadog-agent/datadog.yaml 
sudo ANYSCALE_INSTANCE_ID="instance_id:${ANYSCALE_INSTANCE_ID}" yq -i '.tags[1] = strenv(ANYSCALE_INSTANCE_ID)' /etc/datadog-agent/datadog.yaml 

# node_ip:{ANYSCALE_NODE_IP}
sudo yq -i '.tags[2] = " "' /etc/datadog-agent/datadog.yaml 
sudo ANYSCALE_NODE_IP="node_ip:${ANYSCALE_NODE_IP}" yq -i '.tags[2] = strenv(ANYSCALE_NODE_IP)' /etc/datadog-agent/datadog.yaml 

# project_id:{ANYSCALE_PROJECT_ID}
sudo yq -i '.tags[3] = " "' /etc/datadog-agent/datadog.yaml 
sudo ANYSCALE_PROJECT_ID="project_id:${ANYSCALE_PROJECT_ID}" yq -i '.tags[3] = strenv(ANYSCALE_PROJECT_ID)' /etc/datadog-agent/datadog.yaml 
# ------------------------------

# Configure Ray metrics endpoint for Ray integration
sudo ANYSCALE_RAY_METRICS_ENDPOINT=$ANYSCALE_RAY_METRICS_ENDPOINT yq -i '.instances[0].openmetrics_endpoint = env(ANYSCALE_RAY_METRICS_ENDPOINT)' /etc/datadog-agent/conf.d/ray.d/conf.yaml

### Add tags to Ray integration ###
# Have to initialize tags with empty strings so yq adds these as strings with quotes
# cluster_id:{ANYSCALE_CLUSTER_ID}
sudo yq -i '.instances[0].tags[0] = " "' /etc/datadog-agent/conf.d/ray.d/conf.yaml
sudo ANYSCALE_CLUSTER_ID="cluster_id:${ANYSCALE_CLUSTER_ID}" yq -i '.instances[0].tags[0] = strenv(ANYSCALE_CLUSTER_ID)' /etc/datadog-agent/conf.d/ray.d/conf.yaml

# instance_id:{ANYSCALE_INSTANCE_ID}
sudo yq -i '.instances[0].tags[1] = " "' /etc/datadog-agent/conf.d/ray.d/conf.yaml
sudo ANYSCALE_INSTANCE_ID="instance_id:${ANYSCALE_INSTANCE_ID}" yq -i '.instances[0].tags[1] = strenv(ANYSCALE_INSTANCE_ID)' /etc/datadog-agent/conf.d/ray.d/conf.yaml

# node_ip:{ANYSCALE_NODE_IP}
sudo yq -i '.instances[0].tags[2] = " "' /etc/datadog-agent/conf.d/ray.d/conf.yaml
sudo ANYSCALE_NODE_IP="node_ip:${ANYSCALE_NODE_IP}" yq -i '.instances[0].tags[2] = strenv(ANYSCALE_NODE_IP)' /etc/datadog-agent/conf.d/ray.d/conf.yaml

# project_id:{ANYSCALE_PROJECT_ID}
sudo yq -i '.instances[0].tags[3] = " "' /etc/datadog-agent/conf.d/ray.d/conf.yaml
sudo ANYSCALE_PROJECT_ID="project_id:${ANYSCALE_PROJECT_ID}" yq -i '.instances[0].tags[3] = strenv(ANYSCALE_PROJECT_ID)' /etc/datadog-agent/conf.d/ray.d/conf.yaml
# ---------------------------------

echo "Starting Datadog Agent"

sudo datadog-agent start
```

Serialize the script and encode it in base64.

```
cat datadog.sh | base64
```

#### 2. Write the SupervisorD config[​](#2-write-the-supervisord-config "Direct link to 2. Write the SupervisorD config")

Build a SupervisorD file to configure the `datadog-agent` process to run on cluster startup and in a process manager to restart on failure. Create a file named `supervisord.conf` with the following content:

supervisord.conf

```
[program:datadog-agent]
user=ray
command=bash --login -c -i "/anyscale/scripts/datadog.sh"
autostart=true
autorestart=true
startsecs=0
startretries=50
stdout_logfile=/tmp/ray/datadog-agent.log
redirect_stderr=true
```

Serialize the configuration and encode it in base64.

```
cat supervisord.conf | base64
```

#### 3. Create a Dockerfile[​](#3-create-a-dockerfile "Direct link to 3. Create a Dockerfile")

Finally, create a Dockerfile to create a Docker image. Choose a base image suitable for your workload and insert the Datadog API key. This image installs `datadog-agent` and swaps the placeholders with the serialized script and serialized SupervisorD config.

```
FROM <REPLACE_WITH_BASE_IMAGE_OF_YOUR_CHOICE>

# Install the Datadog agent
RUN DD_INSTALL_ONLY="true" DD_API_KEY="<REPLACE_WITH_DATADOG_API_KEY>" bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"

# Install dependencies
RUN sudo apt-get install -y jq wget

# Install yq
RUN sudo wget https://github.com/mikefarah/yq/releases/download/v4.35.1/yq_linux_amd64 -O /usr/bin/yq
RUN sudo chmod +x /usr/bin/yq

# Setup security configs to default
RUN sudo cp /etc/datadog-agent/security-agent.yaml.example /etc/datadog-agent/security-agent.yaml 

# Setup Ray config https://docs.datadoghq.com/integrations/ray/?tab=host#installation
RUN sudo cp /etc/datadog-agent/conf.d/ray.d/conf.yaml.example  /etc/datadog-agent/conf.d/ray.d/conf.yaml

# Create directory for scripts
RUN sudo mkdir -p /anyscale/scripts

# Script to configure Datadog agent configurations
RUN echo '<serialized datadog.sh>' | base64 -d | sudo tee /anyscale/scripts/datadog.sh
RUN sudo chmod +x /anyscale/scripts/datadog.sh

# Write the SupervisorD config.
RUN sudo mkdir -p /etc/supervisor/customer.conf.d/
RUN echo '<serialized supervisord.conf>' | base64 -d | sudo tee /etc/supervisor/customer.conf.d/supervisord.conf

RUN echo "datadog-agent installed & configured to run inside supervisord."
```

## Limitations on metrics[​](#metrics-limitations "Direct link to Limitations on metrics")

The Ray Datadog integration supports a very limited set of metrics. To add new metrics, customize [`ray.d/config.yaml`](https://github.com/DataDog/integrations-core/blob/master/ray/datadog_checks/ray/data/conf.yaml.example).

## Incompatibility of `vector` and the Ray Datadog integration[​](#vector-incompatibility "Direct link to vector-incompatibility")

The Ray Datadog integration expects metrics to follow a certain format where the delimiter is `.` whereas [`vector`](/monitoring/exporting-logs.md) emits metrics with the `_` delimiter, which is the Prometheus standard.

## Grafana-like dashboards in Datadog[​](#datadog-dashboards "Direct link to Grafana-like dashboards in Datadog")

If you want an Anyscale-like Grafana dashboard in Datadog, set up [`vector`](/monitoring/exporting-logs.md) in the Docker image. You can convert the Grafana dashboards to Datadog with a tool like <https://grafana-to-datadog.pages.dev>.
