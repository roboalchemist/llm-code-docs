# Source: https://docs.datadoghq.com/security/workload_protection/guide/ebpf-free-agent.md

# Source: https://docs.datadoghq.com/security/cloud_security_management/guide/ebpf-free-agent.md

---
title: Threat Detection for Linux Without eBPF Support
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: >-
  Docs > Datadog Security > Cloud Security > Cloud Security Guides > Threat
  Detection for Linux Without eBPF Support
---

# Threat Detection for Linux Without eBPF Support

This guide describes how to set up the Workload Protection eBPF-less solution for eBPF disabled environments, such as AWS Fargate. The eBPF-less solution uses a ptrace-based Datadog Agent.

This guide also describes some advantages of the ptrace solution.

{% alert level="info" %}
Threat Detection for Linux Without eBPF Support is in Preview. Reach out to your Datadog representative to sign up.
{% /alert %}

## Summary of Agent options{% #summary-of-agent-options %}

Workload Protection includes two Agent options for threat detection and response:

- eBPF solution
- eBPF-less solution with ptrace: This version is only available where eBPF is not (Linux kernel versions 3.4 to 4.14).

{% collapsible-section %}
#### eBPF solution

Datadog has built all its security products around [eBPF (extended Berkeley Packet Filter)](https://ebpf.io/what-is-ebpf/). Some of the benfits of eBPF are:

- eBPF improves safety by validating each program through the Linux kernel verifier. This ensures that a program can't crash, fall into infinite loops, or harm the system.
- eBPF is JIT (Just In Time) compiled and the output bytecode is executed on a eBPF VM sandbox. This prevents any kernel crash and provides competitive performance.
- Easy to debug and maintain, can dynamically load programs, and has access to all information needed to trace the user space.

The Datadog eBPF Agent code is [fully open source](https://github.com/DataDog/datadog-agent).
{% /collapsible-section %}

{% collapsible-section %}
#### eBPF-less solution with ptrace

Some environments use instances with old kernels that do not have eBPF at all. The ptrace solution is provided for these environments.

The following features are not available in the eBPF-less Agent:

- Security profiles, providing:
  - Anomaly detection
  - Auto-suppression of normal behavior for signal triaging
  - Malware detection
- Network detections

{% alert level="info" %}
The current implementation supports amd64 and arm64 architecture and ABIs, but can be extended to 32-bit ABIs.
{% /alert %}

### Advantages of ptrace solution{% #advantages-of-ptrace-solution %}

A ptrace-based solution achieves a balance between robust threat detection and unwavering service availability. Some of the advantages of the ptrace-based solution are:

- Precise process control: ptrace provides detailed inspection of memory and registers, safeguarding critical application workloads. This granular visibility is essential for identifying sophisticated threats. The Datadog procfs (Process Filesystem) scanner monitors all system-wide executions, enabling the surgical termination of malicious processes. Together, these tools protect from malicious activity.

- Operational stability: Operating in user space, ptrace avoids the complexities and risks of kernel space, providing a safer and more manageable approach. In the event of a failure, a ptrace-based agent defaults to a fail-open state at the OS layer, keeping the system unaffected, even if the application hangs.

- Performance efficiency: Recent benchmarks conducted by Datadog's engineering team demonstrate that the Datadog ptrace-based implementation shows comparable performance to kernel-based solutions. Specifically, it introduces only a minimal overhead of around 3% for PostgreSQL workloads and negligible impacts for Redis operations, making it very efficient for most use cases.

- Open source verification: Datadog has open-sourced the ptrace-based and eBPF Agent, allowing clients and the security community to verify its safety and effectiveness themselves, fostering transparency and trust in the solution.

{% /collapsible-section %}

## eBPF-less Agent setup{% #ebpf-less-agent-setup %}

You can set up the eBPF-less Agent on various platforms, including Docker and Linux hosts.

This section covers Docker and Linux hosts. For steps on setting up an Amazon Fargate environment where eBPF is disabled, see [AWS Fargate Configuration Guide for Datadog Security](https://docs.datadoghq.com/security/guide/aws_fargate_config_guide/?tab=amazonecs).

### eBPF-less Agent requirements{% #ebpf-less-agent-requirements %}

- The eBPF-less Agent is designed for environments where eBPF is disabled, using ptrace for runtime security, and supports arm64/amd64 architectures.
- Custom installation commands and configurations are required for deploying the eBPF-less Agent. Specific instructions are provided in this section for Docker and Linux host installations.

The eBPF-less solution includes two tracing modes for applications:

- Wrap mode: Traces applications from the start.
- Attach mode: Attaches to already running applications, but comes with more performance overhead and limitations.

### eBPF-less setup steps{% #ebpf-less-setup-steps %}

{% tab title="Docker" %}
An additional environment variable is required on Docker. Add the following line to your docker installation command:

```shell
-e DD_RUNTIME_SECURITY_CONFIG_EBPFLESS_ENABLED=true
```

The corresponding command should be:

```shell
docker run -d --name dd-agent \
  --cgroupns host \
  --pid host \
  --security-opt apparmor:unconfined \
  --cap-add SYS_ADMIN \
  --cap-add SYS_RESOURCE \
  --cap-add SYS_PTRACE \
  --cap-add NET_ADMIN \
  --cap-add NET_BROADCAST \
  --cap-add NET_RAW \
  --cap-add IPC_LOCK \
  --cap-add CHOWN \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /proc/:/host/proc/:ro \
  -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
  -v /etc/passwd:/etc/passwd:ro \
  -v /etc/group:/etc/group:ro \
  -v /:/host/root:ro \
  -v /sys/kernel/debug:/sys/kernel/debug \
  -v /etc/os-release:/etc/os-release \
  -e DD_COMPLIANCE_CONFIG_ENABLED=true \
  -e DD_COMPLIANCE_CONFIG_HOST_BENCHMARKS_ENABLED=true \
  -e DD_RUNTIME_SECURITY_CONFIG_ENABLED=true \
  -e DD_RUNTIME_SECURITY_CONFIG_REMOTE_CONFIGURATION_ENABLED=true \
  -e DD_RUNTIME_SECURITY_CONFIG_EBPFLESS_ENABLED=true \
  -e HOST_ROOT=/host/root \
  -e DD_API_KEY=<API KEY> \
  gcr.io/datadoghq/agent:7
```

{% /tab %}

{% tab title="Linux host" %}
To install the Agent to a Linux host, use the following install script to install the custom build:

```shell
DD_API_KEY=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX DD_SITE="datadoghq.com" \
DD_RUNTIME_SECURITY_CONFIG_ENABLED=true \
bash -c "$(curl -L https://install.datadoghq.com/scripts/install_script_agent7.sh)"
```

Next, modify the `/etc/datadog-agent/system-probe.yaml` file to enable CWS and eBPF-less mode as follow:

In the `system-probe.yaml` file:

```java
runtime_security_config:
  enabled: true
  ebpfless:
    enabled: true
```

Alternatively, to manually install the `.deb/.rmp` provided custom build packages, modify the `/etc/datadog-agent/system-probe.yaml` file to enable CWS and eBPF-less mode as follows:

In the `system-probe.yaml` file:

```java
runtime_security_config:
  enabled: true
  ebpfless:
    enabled: true
```

{% /tab %}

## Deploy eBPF-less Agent{% #deploy-ebpf-less-agent %}

Ensure you perform the following configuration requirements before deploying the Agent:

1. Customize the [Agent Installation Instructions](https://app.datadoghq.com/account/settings/agent/latest?platform=overview) before proceeding with the installation.
1. Install/update the Agent with Cloud Security enabled. For steps, see [Setting up Cloud Security on the Agent](https://docs.datadoghq.com/security/cloud_security_management/setup/agent).
1. Specify additional configurations from the previous **eBPF-less agent setup** sections to install the custom version and enable eBPF-less mode.

## Verify setup{% #verify-setup %}

To validate your Agent installation and setup, connect to your Linux host or Docker container and run:

```shell
sudo /opt/datadog-agent/embedded/bin/system-probe config|grep -A 1 ebpfless
```

You should see the output:

```
  ebpfless:
    enabled: true
```

## Set up application tracing with eBPF-less Agent{% #set-up-application-tracing-with-ebpf-less-agent %}

After the eBPF-less Agent is installed and set up to use the eBPF-Free mode, you can set up how your application is traced. This section provides you two different methods:

- **Wrap mode:** (Recommended) In this mode, your application is launched by the Datadog wrapper that traces it from the beginning using ptrace.
  - All spawned children are traced also.
  - A seccomp profile is applied to drastically reduce the ptracing overhead.
- **Attach mode:** In this mode, you can specify a list of PIDs to attach to your application processes. This should be done quickly because your application is not ptraced until this is done.
  - In this mode, a seccomp profile cannot be applied. Consequently, there is a small amount ptracing overhead.

Both modes use the **cws-instrumentation** binary packaged with the Datadog Agent, and located at `/opt/datadog-agent/embedded/bin/cws-instrumentation`.

{% alert level="info" %}
This tracer communicates with system-probe (part of the Datadog Agent) on localhost using port 5678. The system-probe address can be configured with the `--probe-addr=host:port` cws-instrumentation option. The server-side address can be updated through the runtime_security_config.ebpfless.socket option of the `/etc/datadog-agent/system-probe.yaml` Agent config file.
{% /alert %}

{% tab title="Wrap mode" %}
In wrap mode, the Datadog wrapper launchs the application. Here is an example:

```shell
sudo /opt/datadog-agent/embedded/bin/cws-instrumentation trace -- /usr/bin/your_application
```

If your application runs as non-root, specify the uid/gid as numeric values:

```shell
sudo /opt/datadog-agent/embedded/bin/cws-instrumentation trace --uid 100 --gid 100 -- /usr/bin/your_application
```

{% alert level="info" %}
An application won't start until cws-instrumentation has initialized its connection with the Datadog Agent.
{% /alert %}

The following examples show how the tracer can be integrated within applications for different deployment types.

{% alert level="info" %}
On older 3.4 kernels, the seccomp profile is not available and should be disabled with the `âdisable-seccomp` option.
{% /alert %}

#### Linux systemd service{% #linux-systemd-service %}

If you already have an init script, here is a simple example of the required changes:

```shell
   [Unit]
   Description=My application
   After=datadog-agent-sysprobe.service

   [Service]
   ExecStart=/opt/datadog-agent/embedded/bin/cws-instrumentation trace -- /usr/bin/myapp
   Restart=on-failure

   [Install]
   WantedBy=multi-user.target
```

#### Linux sysvinit service{% #linux-sysvinit-service %}

If you already have an init script, here is a simple example of the required changes:

```shell
#!/bin/sh
set -e
### BEGIN INIT INFO
# Provides:           my_app
# Required-Start:     $network
# Required-Stop:      $network
# Default-Start:      2 3 4 5
# Default-Stop:       0 1 6
# Short-Description:  My application
# Description: My application
### END INIT INFO

# Start the service
start() {
        echo "Starting my app"
        /opt/datadog-agent/embedded/bin/cws-instrumentation trace -- /usr/bin/myapp &
}


# Stop the service
stop() {
       echo "Stopping my app"
    pkill -f /usr/bin/myapp
}

### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart}"
        exit 1
esac

exit 0
```

#### Docker{% #docker %}

For Docker application deployments, you should modify your Dockerfile to wrap your application like this:

```shell
FROM gcr.io/datadoghq/agent:7 AS datadogagent

FROM ubuntu:latest

COPY --from=datadogagent /opt/datadog-agent/embedded/bin/cws-instrumentation .

ENTRYPOINT ["/cws-instrumentation", "trace", "--"]

CMD ["/bin/bash", "-c", "while true; do sleep 1; echo my app is running; done"]
```

When running your docker application, it's important to give it an additional capability by adding `--cap-add=SYS_PTRACE` to your `docker run` command.

You also have to connect the container to Datadog on port 5678 by doing one of the following:

- Launch both containers with the `--network` host option.
- Use the [Docker network][6] feature to run both containers on the same bridge network.

{% /tab %}

{% tab title="Attach mode" %}
The wrap mode is recommended because the attach mode has the following limitations:

- It misses all initialization made by the application until Datadog attaches to it.
- - When attaching, Datadog cannot set up a seccomp profile.
- More performance overhead.
- If the traced application restarts, Datadog must ensure that the tracer restarts also.

The attach mode differs from the wrap mode by attaching directly the tracer on an already running application, like this:

```shell
sudo /opt/datadog-agent/embedded/bin/cws-instrumentation trace --pid 2301
```

Several PIDs can be attached at once:

```shell
sudo /opt/datadog-agent/embedded/bin/cws-instrumentation trace --pid 2301 --pid 2302 --pid 2303
```

The following examples show how the tracer can be integrated within applications for different deployment types.

#### Linux systemd service{% #linux-systemd-service %}

If you already have an init script, here is an example of how to integrate the wrapper using a new systemd service:

```shell
[Unit]
Description=Datadog CWS instrumentation attach to my application
After=datadog-agent-sysprobe.service my-app.service

[Service]
ExecStart=/bin/bash -c "/opt/datadog-agent/embedded/bin/cws-instrumentation trace $(for pid in $(pidof myapp); do echo --pid $pid; done)"
Restart=on-failure

[Install]
WantedBy=multi-user.target
```

#### Linux sysvinit service{% #linux-sysvinit-service %}

If you already have an init script, here is an example of how to integrate the tracer using a new sysvinit service:

```shell
#!/bin/sh
set -e
### BEGIN INIT INFO
# Provides:           dd_tracing_my_app
# Required-Start:     $network
# Required-Stop:      $network
# Default-Start:      2 3 4 5
# Default-Stop:       0 1 6
# Short-Description:  Datadog tracing of my application
# Description: Datadog tracing of my application
### END INIT INFO

# Start the service
start() {
        echo "Starting tracing my app"
        /opt/datadog-agent/embedded/bin/cws-instrumentation trace $(for pid in $(pidof myapp); do echo --pid $pid; done) &
}


# Stop the service
stop() {
       echo "Stopping my app"
    pkill -f /opt/datadog-agent/embedded/bin/cws-instrumentation
}

### main logic ###
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  restart)
        stop
        start
        ;;
  *)
        echo $"Usage: $0 {start|stop|restart}"
        exit 1
esac

exit 0
```

#### Docker{% #docker %}

To attach the wrapper to a Docker image running an application, use the following Dockerfile:

```shell
FROM gcr.io/datadoghq/agent:7

ENTRYPOINT ["/opt/datadog-agent/embedded/bin/cws-instrumentation", "trace", "--pid", "$PID"]
```

Next, provide the host PID for connecting to Docker as an environment variable.

To attach to an application, you'll need the following:

- When running the Docker application, add the required capability by including `--cap-add=SYS_PTRACE` to your `docker run` command.
- Ensure the application container can reach the Datadog container on port 5678 using one of the following methods:
  - Launch both containers with the `--network` host option.
  - Use the [Docker network][6] feature to run both containers on the same bridge network.
- To ensure the application container is running on the host pid (just as the Datadog Agent does), add these options: `--cgroupns host --pid host`.

{% /tab %}
