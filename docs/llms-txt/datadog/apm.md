# Source: https://docs.datadoghq.com/containers/kubernetes/apm.md

# Source: https://docs.datadoghq.com/containers/docker/apm.md

# Source: https://docs.datadoghq.com/containers/amazon_ecs/apm.md

---
title: Tracing ECS Applications
description: >-
  Configure APM trace collection for containerized applications running on
  Amazon ECS
breadcrumbs: Docs > Container Monitoring > Amazon ECS > Tracing ECS Applications
source_url: https://docs.datadoghq.com/amazon_ecs/apm/index.html
---

# Tracing ECS Applications

## Overview{% #overview %}

To collect traces from your ECS containers, update the Task Definitions for both your Agent and your application container as described below.

One option for doing this is to modify the previously used [Task Definition file](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#managing-the-task-definition-file) and [register your updated Task Definition](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#registering-the-task-definition). Alternatively, you can edit the Task Definition directly from the Amazon Web UI.

Once enabled, the Datadog Agent container collects the traces emitted from the other application containers on the same host as itself.

## Configure the Datadog Agent to accept traces{% #configure-the-datadog-agent-to-accept-traces %}

1. To collect all traces from your running ECS containers, update your Agent's Task Definition from the [original ECS Setup](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#setup) with the configuration below.

Use [datadog-agent-ecs-apm.json](https://docs.datadoghq.com/resources/json/datadog-agent-ecs-apm.json) as a reference point for the required base configuration. In the Task Definition for Datadog Agent container, set the `portMappings` for a host to container port on `8126` with the protocol `tcp`.

   ```json
   {
     "containerDefinitions": [
       {
         "name": "datadog-agent",
         "image": "public.ecr.aws/datadog/agent:latest",
         "cpu": 100,
         "memory": 512,
         "essential": true,
         "portMappings": [
           {
             "hostPort": 8126,
             "protocol": "tcp",
             "containerPort": 8126
           }
         ],
         (...)
       }
     ]
   }
   ```

1. For **Agent v7.17 or lower**, add the following environment variables:

   ```json
   "environment": [
     (...)
     {
       "name": "DD_APM_ENABLED",
       "value": "true"
     },
     {
       "name": "DD_APM_NON_LOCAL_TRAFFIC",
       "value": "true"
     }
   ]
   ```

1. If you are updating a local file for your Agent's Task Definition, [register your updated Task Definition](https://docs.datadoghq.com/containers/amazon_ecs/?tab=awscli#registering-the-task-definition). This creates a new revision. You can then reference this updated revision in the daemon service for the Datadog Agent.

## Configure your application container to submit traces to Datadog Agent{% #configure-your-application-container-to-submit-traces-to-datadog-agent %}

### Install the tracing library{% #install-the-tracing-library %}

Follow the [setup instructions for installing the Datadog tracing library](https://docs.datadoghq.com/tracing/trace_collection/) for your application's language. For ECS install the tracer into your application's container image.

### Provide the private IP address for the EC2 instance{% #provide-the-private-ip-address-for-the-ec2-instance %}

Provide the tracer with the private IP address of the underlying EC2 instance that the application container is running on. This address is the hostname of the tracer endpoint. The Datadog Agent container on the same host (with the host port enabled) receives these traces.

Use one of the following methods to dynamically get the private IP address:

{% tab title="EC2 metadata endpoint" %}
The [Amazon's EC2 metadata endpoint (IMDSv1)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html) allows discovery of the private IP address. To get the private IP address for each host, curl the following URL:

```
curl http://169.254.169.254/latest/meta-data/local-ipv4
```

If you are using Version 2 of the [Instance Metadata Service (IMDSv2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html):

```
TOKEN=$(curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600")
curl http://169.254.169.254/latest/meta-data/local-ipv4 -H "X-aws-ec2-metadata-token: $TOKEN"
```

{% /tab %}

{% tab title="ECS container metadata file" %}
The [Amazon's ECS container metadata file](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-metadata.html#metadata-file-format) allows discovery of the private IP address. To get the private IP address for each host, run the following command:

```
cat $ECS_CONTAINER_METADATA_FILE | jq -r .HostPrivateIPv4Address
```

{% /tab %}

Provide the result of this request to the tracer by setting the `DD_AGENT_HOST` environment variable for each application container that sends traces.

### Configure the Trace Agent endpoint{% #configure-the-trace-agent-endpoint %}

In cases where variables on your ECS application are set at launch time (Java, .NET, and PHP), you **must** set the hostname of the tracer endpoint as an environment variable with `DD_AGENT_HOST` using one of the above methods. The examples below use the IMDSv1 metadata endpoint, but the configuration can be interchanged if needed. If you have a startup script as your entry point, include this call as part of the script, otherwise add it to the ECS Task Definition's `entryPoint`.

For other supported languages (Python, JavaScript, Ruby, and Go) you can alternatively set the hostname in your application's source code.

{% tab title="Python" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following, substituting your `<Python Startup Command>`:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); <Python Startup Command>"
]
```

For Python the startup command is generally `ddtrace-run python my_app.py` but may vary depending on the framework used, for example, using [uWSGI](https://ddtrace.readthedocs.io/en/stable/advanced_usage.html#uwsgi) or instrumenting your [code manually with `patch_all`](https://ddtrace.readthedocs.io/en/stable/basic_usage.html#patch-all).
{% /tab %}

{% tab title="Node.js" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following, substituting your `<Node.js Startup Command>`:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); <Node.js Startup Command>"
]
```

#### Code{% #code %}

You can alternatively update your code to have the tracer set the hostname explicitly:

```javascript
const tracer = require('dd-trace').init();
const axios = require('axios');

(async () => {
  const { data: hostname } = await axios.get('http://169.254.169.254/latest/meta-data/local-ipv4');
  tracer.setUrl(`http://${hostname}:8126`);
})();
```

{% /tab %}

{% tab title="Ruby" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following, substituting your `<Ruby Startup Command>`:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); <Ruby Startup Command>"
]
```

#### Code{% #code %}

You can alternatively update your code to have the tracer set the hostname explicitly:

```ruby
require 'datadog' # Use 'ddtrace' if you're using v1.x
require 'net/http'

Datadog.configure do |c|
  c.agent.host = Net::HTTP.get(URI('http://169.254.169.254/latest/meta-data/local-ipv4'))
end
```

{% /tab %}

{% tab title="Go" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following, substituting your `<Go Startup Command>`:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); <Go Startup Command>"
]
```

#### Code{% #code %}

You can alternatively update your code to have the tracer set the hostname explicitly. **Note**: This documentation uses v2 of the Go tracer, which Datadog recommends for all users. If you are using v1, see the [migration guide](https://docs.datadoghq.com/tracing/trace_collection/custom_instrumentation/go/migration) to upgrade to v2.

```go
package main

import (
    "net/http"
    "io/ioutil"
    "github.com/DataDog/dd-trace-go/v2/ddtrace/tracer"
)

func main() {
    resp, err := http.Get("http://169.254.169.254/latest/meta-data/local-ipv4")
    bodyBytes, err := ioutil.ReadAll(resp.Body)
    host := string(bodyBytes)
    if err == nil {
        //set the output of the curl command to the DD_AGENT_HOST env
        os.Setenv("DD_AGENT_HOST", host)
        // tell the trace agent the host setting
        tracer.Start(tracer.WithAgentAddr(host))
        defer tracer.Stop()
    }
    //...
}
```

{% /tab %}

{% tab title="Java" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following, substituting your `<Java Startup Command>`:

```java
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); <Java Startup Command>"
]
```

The Java startup command should include your `-javaagent:/path/to/dd-java-agent.jar`, see the [Java tracing docs for adding the tracer to the JVM](https://docs.datadoghq.com/tracing/trace_collection/dd_libraries/java/?tab=containers#add-the-java-tracer-to-the-jvm) for further examples.
{% /tab %}

{% tab title=".NET" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following. Substituting your `APP_PATH` if not set:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); dotnet ${APP_PATH}"
]
```

{% /tab %}

{% tab title="PHP" %}
#### Launch time variable{% #launch-time-variable %}

Update the Task Definition's `entryPoint` with the following:

```json
"entryPoint": [
  "sh",
  "-c",
  "export DD_AGENT_HOST=$(curl http://169.254.169.254/latest/meta-data/local-ipv4); php-fpm -F"
]
```

#### Apache{% #apache %}

For Apache and `mod_php` in VirtualHost or server configuration file, use `PassEnv` to set `DD_AGENT_HOST` and other environment variables, such as the variables for [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) like the below example:

```
PassEnv DD_AGENT_HOST
PassEnv DD_SERVICE
PassEnv DD_ENV
PassEnv DD_VERSION
```

#### PHP fpm{% #php-fpm %}

When the ini param is set as `clear_env=on`, in the pool workers file `www.conf` you must also configure environment variables to be read from the host. Use this to also set `DD_AGENT_HOST` and other environment variables, such as the variables for [Unified Service Tagging](https://docs.datadoghq.com/getting_started/tagging/unified_service_tagging/) like the below example:

```
env[DD_AGENT_HOST] = $DD_AGENT_HOST
env[DD_SERVICE] = $DD_SERVICE
env[DD_ENV] = $DD_ENV
env[DD_VERSION] = $DD_VERSION
```

{% /tab %}

#### IMDSv2{% #imdsv2 %}

When using IMDSv2, the equivalent `entryPoint` configuration looks like the following. Substitute `<Startup Command>` with the appropriate command based on your language, as in the examples above.

```json
"entryPoint": [
  "sh",
  "-c",
  "export TOKEN=$(curl -X PUT \"http://169.254.169.254/latest/api/token\" -H \"X-aws-ec2-metadata-token-ttl-seconds: 21600\"); export DD_AGENT_HOST=$(curl -H \"X-aws-ec2-metadata-token: $TOKEN\" http://169.254.169.254/latest/meta-data/local-ipv4); <Startup Command>"
]
```

## Further reading{% #further-reading %}

- [Collect your application logs](https://docs.datadoghq.com/agent/amazon_ecs/logs/)
- [Assign tags to all data emitted by a container](https://docs.datadoghq.com/agent/amazon_ecs/tags/)
