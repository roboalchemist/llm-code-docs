# Source: https://docs.anyscale.com/monitoring/exporting-logs.md

# Exporting logs and metrics with Vector

[View Markdown](/monitoring/exporting-logs.md)

# Exporting logs and metrics with Vector

Anyscale integrates with [Vector](https://vector.dev/), a monitoring tool that supports custom querying, filtering, and alerting for logs and metrics.

## Step 0: Requirements[​](#step-0-requirements "Direct link to Step 0: Requirements")

* [Vector](https://vector.dev) is a tool for building observability pipelines. It enables you to collect, transform, and route data to and from a variety of sources. In this guide, we define Vector configuration files to scrape Ray logs and metrics and export them to your desired location.
* [SupervisorD](http://supervisord.org/) is a process control system. In this guide, we use SupervisorD to run the Vector process when the cluster starts.

## Step 1: Write a Vector configuration file[​](#step-1-write-a-vector-configuration-file "Direct link to Step 1: Write a Vector configuration file")

A Vector configuration file is a directed graph, consisting of one or more [sources, transforms, or sinks](https://vector.dev/components/).

Anyscale recommends using an Anyscale workspace to write and test a configuration file. Open VS Code and create a `vector.yaml` file. Paste in the following sample configurations:

### Source/transform configuration[​](#sourcetransform-configuration "Direct link to Source/transform configuration")

vector.yaml

```
sources:
  raw_ray_logs:
    type: file
    fingerprint:
      ignored_header_bytes: 0
      strategy: device_and_inode
    include:
      - /tmp/ray/*/logs/**/job-driver-*.*
      - /tmp/ray/*/logs/**/runtime_env_setup-*.*
      - /tmp/ray/*/logs/**/worker-*.out
      - /tmp/ray/*/logs/**/worker-*.err
      - /tmp/ray/*/logs/**/serve/*.*
    exclude:
      # The session_latest directory is a symlink to an actual session directory,
      # so we intentionally exclude it here so Vector doesn't ingest duplicates.
      - /tmp/ray/session_latest/logs/**/*.*
  raw_ray_metrics:
    type: prometheus_scrape
    endpoints:
      - "${ANYSCALE_RAY_METRICS_ENDPOINT}"
    instance_tag: ScrapeTarget
    scrape_interval_secs: 15

# These transforms add useful attributes to your log files.
transforms:
  ray_logs:
    type: remap
    inputs: ["raw_ray_logs"]
    source: |-
      .cluster_id = "${ANYSCALE_CLUSTER_ID}"
      .instance_id = "${ANYSCALE_INSTANCE_ID}"
      .node_ip = "${ANYSCALE_NODE_IP}"
      if !is_empty("${ANYSCALE_JOB_ID-}") {
        .anyscale_job_id = "${ANYSCALE_JOB_ID-}"
      }
      if !is_empty("${ANYSCALE_JOB_NAME-}") {
        .job_name = "${ANYSCALE_JOB_NAME-}"
      }
      if !is_empty("${ANYSCALE_SERVICE_ID-}") {
        .service_id = "${ANYSCALE_SERVICE_ID-}"
      }
      if !is_empty("${ANYSCALE_SERVICE_NAME-}") {
        .service_name = "${ANYSCALE_SERVICE_NAME-}"
      }
      if !is_empty("${ANYSCALE_SERVICE_VERSION_ID-}") {
        .service_version_id = "${ANYSCALE_SERVICE_VERSION_ID-}"
      }
      # For structured logs, we need to parse out the structure from the message and elevate it as fields of the root vector event.
      maybe_structured_log = parse_json(.message) ?? {}
      . = merge!(., maybe_structured_log)
      # Use the structured log's `asctime` as the timestamp for this event.
      # When not set, the timestamp defaults to the time vector ingested the log.
      if .asctime != null {
        .timestamp = parse_timestamp!(.asctime, format: "%Y-%m-%d %H:%M:%S,%3f", timezone: "UTC")
      }
  ray_metrics:
    type: remap
    inputs: ["raw_ray_metrics"]
    source: |-
      .tags.ClusterId = "${ANYSCALE_CLUSTER_ID}"
      .tags.InstanceId = "${ANYSCALE_INSTANCE_ID}"
      .tags.NodeIp = "${ANYSCALE_NODE_IP}"
      .tags.AnyscaleJobId = "${ANYSCALE_JOB_ID-}"
      .tags.JobName = "${ANYSCALE_JOB_NAME-}"
      .tags.ServiceId = "${ANYSCALE_SERVICE_ID-}"
      .tags.ServiceName = "${ANYSCALE_SERVICE_NAME-}"
      .tags.ServiceVersionId = "${ANYSCALE_SERVICE_VERSION_ID-}"
      .tags = compact(.tags, recursive: true)
  # Example for filtering metrics by name. You can also filter by metric labels.
  # filtered_metrics:
  #   type: filter
  #   inputs: ["raw_ray_metrics"]
  #   condition: "match(.name, r'^ray_.+')"
```

### Sink configuration[​](#sink-configuration "Direct link to Sink configuration")

A sink is a destination for your observability data. Choose from AWS CloudWatch, Google Cloud Monitoring, or Datadog and add it to your `vector.yaml`. A full list of available sinks can be found [here](https://vector.dev/docs/reference/configuration/sinks/).

* AWS CloudWatch
* Google Cloud Monitoring
* Datadog Logs & Metrics

warning

This section is applicable only to customer-hosted clouds. If you are using Anyscale-hosted clouds and would like to ship logs to CloudWatch, reach out to `support@anyscale.com` for more information.

AWS CloudWatch requires additional access for the Cluster IAM role. This can be modified in the AWS IAM Console. Make sure to replace `YOUR_ACCOUNT_ID` with your AWS Account ID.

IAM Cloudwatch Policy

```
{
  "Statement": [
    {
      "Action": "cloudwatch:PutMetricData",
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "CloudwatchMetricsWrite"
    },
    {
      "Action": ["logs:DescribeLogStreams", "logs:DescribeLogGroups"],
      "Effect": "Allow",
      "Resource": "*",
      "Sid": "CloudwatchLogsRead"
    },
    {
      "Action": "logs:PutLogEvents",
      "Effect": "Allow",
      "Resource": "arn:aws:logs:*:YOUR_ACCOUNT_ID:log-group:/anyscale*:*",
      "Sid": "CloudwatchLogsEventsWrite"
    },
    {
      "Action": ["logs:CreateLogStream", "logs:CreateLogGroup"],
      "Effect": "Allow",
      "Resource": "arn:aws:logs:*:YOUR_ACCOUNT_ID:log-group:/anyscale*",
      "Sid": "CloudwatchLogsWrite"
    }
  ],
  "Version": "2012-10-17"
}
```

Once the IAM Role has been updated, update `vector.yaml` to include a sink section as follows:

vector.yaml

```
sinks:
  cloudwatch_logs:
    region: us-west-2
    encoding:
      codec: json
    group_name: "/anyscale/"
    inputs: ["ray_logs"]
    # One of ANYSCALE_JOB_ID / ANYSCALE_SERVICE_ID will be set for jobs / services.
    stream_name: "${ANYSCALE_JOB_ID-}${ANYSCALE_SERVICE_ID-}/${ANYSCALE_CLUSTER_ID}"
    type: aws_cloudwatch_logs
  cloudwatch_metrics:
    region: us-west-2
    default_namespace: anyscale
    inputs: ["ray_metrics"]
    type: aws_cloudwatch_metrics
```

warning

Those setting are for customer-hosted clouds, if you are using Anyscale-hosted clouds, reach out to `support@anyscale.com` for more information.

Google Cloud Logging and Cloud Monitoring require additional roles to be added to the Anyscale Cluster Principal. This can be modified in the Google Cloud IAM Console. You need to add:

```
roles/logging.logWriter
roles/monitoring.metricWriter
```

Once the IAM Principal has been updated, update `vector.yaml` to include a sink section as follows:

vector.yaml

```
sinks:
  gcp_logs:
    encoding:
      timestamp_format: rfc3339
    inputs: ["ray_logs"]
    log_id: anyscale.ray
    project_id: INSERT_GOOGLE_PROJECT_ID_HERE
    resource:
      project_id: INSERT_GOOGLE_PROJECT_ID_HERE
      type: global
    type: gcp_stackdriver_logs

  gcp_metrics:
    inputs: ["ray_metrics"]
    project_id: INSERT_GOOGLE_PROJECT_ID_HERE
    resource:
      project_id: INSERT_GOOGLE_PROJECT_ID_HERE
      type: global
    type: gcp_stackdriver_metrics
```

warning

Putting API Keys into a Docker image isn't considered best practice. Anyscale recommends using [Vector secrets](https://vector.dev/highlights/2022-07-07-secrets-management/) in production.

Datadog offers different sites around the world. Make sure to [identify your Datadog Site](https://docs.datadoghq.com/getting_started/site/) and update the example YAML definition.

vector.yaml

```
sinks:
  datadog_logs:
    default_api_key: INSERT_DATADOG_API_KEY_HERE
    inputs: ["ray_logs"]
    site: us5.datadoghq.com # Put your specific Datadog Site here
    type: datadog_logs
  datadog_metrics:
    default_api_key: INSERT_DATADOG_API_KEY_HERE
    inputs: ["ray_metrics"]
    site: us5.datadoghq.com # Put your specific Datadog Site here
    type: datadog_metrics
```

## Step 2: Test the configuration file[​](#step-2-test-the-configuration-file "Direct link to Step 2: Test the configuration file")

With the Vector configuration file saved as `vector.yaml`, run the following commands:

```
# Install Vector.
sudo apt-get install curl -y
curl --proto '=https' --tlsv1.2 -sSfL https://sh.vector.dev | bash
source /home/ray/.profile

# Create a state directory for Vector & make it accessible.
sudo mkdir -p /var/lib/vector/
sudo chmod 777 /var/lib/vector/

# Run Vector
vector --config vector.yaml

# In a new tab, generate fake log content.
mkdir -p /tmp/ray/session_fake/logs/
for i in {1..5000}; do echo "Log Line $i" >> /tmp/ray/session_fake/logs/job-driver-fake.log && echo "Wrote line $i" && sleep 1; done

# Look for warnings / errors in Vector - if you don't see any, check upstreams to see if logs & metrics are being received.
```

note

If your configuration doesn't seem to be working, visit the [Debugging Vector](#debug-vector) section below for some tips.

## Step 3: Move to production[​](#step-3-move-to-production "Direct link to Step 3: Move to production")

* Bring your own Docker
* Use Anyscale build farm
* Run per-job using job entrypoint

To move to production, we must build a [SupervisorD](http://supervisord.org/) file to configure the Vector process to run on cluster startup and in a process manager to restart on failure. Create a file named `supervisord.conf` in the same workspace you used previously.

supervisord.conf

```
[program:vector]
user=ray
command=bash --login -c -i "sudo -E /home/ray/.vector/bin/vector --config=/etc/vector/vector.yaml"
autostart=true
autorestart=true
startsecs=0
startretries=50
stdout_logfile=/tmp/ray/vector.log
redirect_stderr=true
```

Then, follow the instructions below to package both of these configuration files into a Ray container image.

1. On your laptop (or wherever you build your Dockerfile), change directory into the directory with your Dockerfile in it.
2. Copy `vector.yaml` from your workspace into this directory.
3. Copy `supervisord.conf` from your workspace into this directory.
4. Add the following lines to your Dockerfile.

```
# Install Vector.
RUN curl --proto '=https' --tlsv1.2 -sSfL https://sh.vector.dev | bash -s -- -y

# Write the Vector config.
RUN sudo mkdir -p /etc/vector/
RUN sudo chmod 777 /etc/vector/
COPY vector.yaml /etc/vector/vector.yaml

# Write the SupervisorD config.
RUN sudo mkdir -p /etc/supervisor/customer.conf.d/
RUN sudo chmod 777 /etc/supervisor/customer.conf.d/
COPY supervisord.conf /etc/supervisor/customer.conf.d/vector.conf

# Create a state directory for Vector.
RUN sudo mkdir -p /var/lib/vector/
RUN sudo chmod 777 /var/lib/vector/
```

5. Build and push your Docker image, and start an Anyscale Job or Service using that image.

To move to production, we must build a [SupervisorD](http://supervisord.org/) file to configure the Vector process to run on cluster startup and in a process manager to restart on failure. Create a file named `supervisord.conf` in the same workspace you used previously.

supervisord.conf

```
[program:vector]
user=ray
command=bash --login -c -i "sudo -E /home/ray/.vector/bin/vector --config=/etc/vector/vector.yaml"
autostart=true
autorestart=true
startsecs=0
startretries=50
stdout_logfile=/tmp/ray/vector.log
redirect_stderr=true
```

Then, follow the instructions below to package both of these configuration files into a Ray container image.

1. On your workspace, run `cat vector.yaml | base64 -w 0`. This is the serialized Vector config.
2. On your workspace, run `cat supervisord.conf | base64 -w 0`. This is the serialized SupervisorD config.
3. Create a new container image. After choosing the base image, add the following commands:

```
# Write the Vector config.
RUN sudo mkdir -p /etc/vector/
RUN echo '<serialized vector config>' | base64 -d | sudo tee /etc/vector/vector.yaml

# Write the SupervisorD config.
RUN sudo mkdir -p /etc/supervisor/customer.conf.d/
RUN echo '<serialized supervisord config>' | base64 -d | sudo tee /etc/supervisor/customer.conf.d/supervisord.conf

# Install Vector.
RUN sudo apt-get update && sudo apt install -y curl
RUN curl --proto '=https' --tlsv1.2 -sSfL https://sh.vector.dev | bash -s -- -y

# Create a state directory for Vector.
RUN sudo mkdir -p /var/lib/vector/
RUN sudo chmod 777 /var/lib/vector/

RUN echo "Vector installed & configured to run inside supervisord."
```

4. Build the container image, and start an Anyscale Job or Service using it.

You can launch Vector with your configuration on a per-job basis by launching it before running your job.

1. Create a script that will launch Vector before your main entry point:

run\_job.sh

```
# Install Vector. You can do this ahead of time in a container image if you prefer.
curl --proto '=https' --tlsv1.2 -sSfL https://sh.vector.dev | bash -s -- -y > /dev/null 2>&1 &&
sudo mkdir -p /etc/vector/ &&
sudo chmod 777 /etc/vector/ &&
sudo mkdir -p /var/lib/vector/ &&
sudo chmod 777 /var/lib/vector/ &&
source ~/.profile &&
# Launch vector
vector --config vector.yaml > /dev/null 2>&1 &
# Run your main entry point
python main.py
```

2. Launch your job with this script as your entrypoint: `anyscale job submit -- bash run_job.sh`

## Debugging Vector[​](#debug-vector "Direct link to Debugging Vector")

If you're having trouble getting your Vector configuration working, Vector provides tools to help understand what's going on. Here are a few tips to help you debug your Vector configuration.

1. First, enable the Vector API server. This will allow you to query the state of your sources, transforms, and sinks.

```
api:
  enabled: true
  address: 127.0.0.1:8687 # 8686 is the default port, so we're using 8687 here.
```

2. Run `vector top -u http://127.0.0.1:8687/graphql` to see a summary of all your Vector sources, transforms, and sinks. Here you can see the events going into and out of each component to help see where things are going wrong.

3. Run `vector tap -u http://127.0.0.1:8687/graphql` to see a continuous stream of events going through Vector.

If you are still having trouble, visit the [Vector Troubleshooting Guide](https://vector.dev/guides/level-up/troubleshooting/) or reach out to Anyscale support.
