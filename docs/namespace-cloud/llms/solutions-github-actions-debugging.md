<!-- Source: https://namespace.so/docs/solutions/github-actions/debugging -->

# Debugging GitHub Actions

Traditional CI debugging often involves guesswork, log parsing, and time-consuming iteration cycles.
Namespace eliminates these pain points by providing comprehensive debugging capabilities that give you direct access to your running workflows and deep visibility into their performance characteristics.

## Interactive Debugging

Get direct access to your runners while they're executing your workflows, enabling real-time debugging and investigation.

### Pause Job Execution

You can pause execution of a running job and connect to it using an interactive terminal for
command-line debugging and investigation.
This is perfect for examining file systems, running diagnostic commands, and troubleshooting build environments.

This feature is available for jobs running on Linux.

Find the target job on [Namespace dashboard](https://cloud.namespace.so/workspace/ghrunners).
If the job is currently running you will see the step the is currently runing.

![job page, current step troubleshooting](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fjob-troubleshoot-row.fe7244e1.png&w=1200&q=75)

Press the Troubleshoot button and a terminal session into the execution environment
of the current step will open:

![job troubleshoot page](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fjob-troubleshoot-page.f385646a.png&w=1200&q=75)

The execution of the current step will continue, but the workflow will not proceed to the next step until
you finish the troubleshooting session and press Resume.

If step execution is paused but no troubleshooting session is open, execution will automatically resume
after 10 minutes of inactivity.

### Setting Breakpoints

Pause your GitHub Actions workflows at any point to investigate the current state, examine variables, and debug issues interactively.
Using breakpoints eliminates the need to replicate the CI environment locally.
You can just jump into the failed state and start exploring immediately.

```
jobs:
  tests:
    runs-on: namespace-profile-default
    permissions:
      id-token: write
      contents: read
 
    steps:
      - name: Checkout the repository
        uses: actions/checkout@v4
 
      - name: Run tests
        shell: bash
        run: ...
 
      - name: Breakpoint if tests failed
        if: failure()
        uses: namespacelabs/breakpoint-action@v0
        with:
          duration: 15m
          authorized-users: <your-github-username>,<another-github-username>
```

The [`breakpoint-action`](/docs/reference/github-actions/breakpoint) will emit instructions how to access the paused runner.
The action is compatible with any runners and also available outside of Namespace.

```
▶ Run namespacelabs/breakpoint-action@v0
Connecting endpoint=rendezvous.namespace.so:5000
┌──────────────────────────────────────────────────────────────────────┐
│ Breakpoint! Running until Jun 26 09:58:26 UTC (14 minutes from now). │
└──────────────────────────────────────────────────────────────────────┘
Connect with:
ssh -p 44793 runner@rendezvous.namespace.so
```

While the breakpoint is active, you can also [VNC](#vnc-remote-display) into the runner to examine the environment, run commands manually, and understand exactly what is happening in your workflow.

Workflows with active breakpoint sessions are still "running" and continue to count towards your usage.

### Instance SSH Access

If the above methods are not available (e.g. the job is not Linux-based and you can't modify the workflow)
you can access the instance that is executing the job directly without pausing the workflow.

The simplest path to jump into an interactive terminal is through your browser with our web SSH interface.

![Runner Terminal access](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnerterminal.c8d1b4cb.png&w=1200&q=75)

Alternatively, you can jump into an SSH session from your command line.

#### Identify the runner instance id

Open the *Set up job* step in your job logs. The instance id can be found in the runner name.

`Runner name: 'nsc-runner-<instance-id>'`

You can also look up which instance ran which job in our [dashboard](https://cloud.namespace.so/workspace/actions/repos).

#### Connect to the runner

To open an SSH session, you can use our [CLI](/docs/reference/cli/installation) or connect using native SSH.

```
$ nsc ssh <instance-id>
 
$ ssh <instance-id>@ssh.<region>.namespace.so
```

SSH access is available for Linux and macOS runners, with Windows support coming soon.   
**Note:** Native SSH access is not enabled by default. Reach out to our [support team](mailto:support@namespace.so) to get enrolled.

## Remote Display

Namespace supports visual debug access through multiple options which is invaluable for debugging GUI applications, testing user interfaces, and investigating display-related issues.

### VNC Integration

Access your Mac runners through Remote Display (VNC) directly from the Namespace dashboard.

![Tahoe Remote Display](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftahoeremotedisplay.b8f208ef.png&w=1200&q=75)

You can also start a VNC session from your command line:

#### Identify the runner instance id

Open the *Set up job* step in your job logs. The instance id can be found in the runner name.

`Runner name: 'nsc-runner-<instance-id>'`

You can also look up which instance ran which job in our [dashboard](https://cloud.namespace.so/workspace/actions/repos).

#### Start a VNC session

To connect to the runner instance, you can use our [CLI](/docs/reference/cli/installation).

```
$

```
nsc vnc <instance-id>
```
```

VNC support is currently available for macOS runners. Support for other platforms is in development.

### RDP Access

To gain interactive, visual access to your Windows runners, you can rely on our RDP integration.

![Windows RDP](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fwindows-demo.338ac8f5.png&w=1200&q=75)

You can start an RDP session using our [CLI](/docs/reference/cli/installation).

#### Identify the runner instance id

Open the *Set up job* step in your job logs. The instance id can be found in the runner name.

`Runner name: 'nsc-runner-<instance-id>'`

You can also look up which instance ran which job in our [dashboard](https://cloud.namespace.so/workspace/actions/repos).

#### Start an RDP session

```
$

```
nsc rdp <instance-id>
```
```

## Job Observability

Gain comprehensive insights into your GitHub Actions performance with detailed metrics, logs, and resource monitoring.

### Performance Metrics

The dedicated job view allows correlating job steps with performance metrics and comparing a job's performance to previous runs.
This visibility helps you identify performance bottlenecks and track improvements over time.

![Runner metrics](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frunnermetrics.faf03497.png&w=1200&q=75)

- **CPU Usage**: Track processor utilization across all cores, identify CPU-intensive operations
- **Memory Consumption**: Detect memory leaks and excessive allocation
- **Disk I/O**: Understand disk read/write patterns, identify storage bottlenecks
- **Network Activity**: Track network usage, bandwidth consumption, and connection patterns

The **previous runs** panel allows you to compare the performance of the current run to the recent history of this job.

### Advanced Logging Capabilities

Access comprehensive logging that goes far beyond standard GitHub Actions logs, providing visibility into every aspect of your workflow execution.

**Container Logs**
Unlike traditional GitHub Actions, Namespace provides direct access to logs from running containers within your workflows.

![Container Logs](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Ftestcontainerlogs.f785750e.png&w=1200&q=75)

**Build logs**
Any Docker build issued from a Namespace runner is linked from the job UI, granting you direct access to the [build logs and build performance telemetry](/docs/solutions/docker-builders/tracing-and-logs).

![Container Builds](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcontainer-builds.7d9275bb.png&w=640&q=75)![Build Tracing](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbuildtrace.c35385df.png&w=828&q=75)

**Metrics correlation**
Namespace also collects and retains step logs, too. When hovering over a step, you can easily correlate it with the associated instance metrics.

![Step metric correlation](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fsteplogsmetrics.d4509a81.png&w=1200&q=75)

### Out of Memory (OOM) Detection

Memory consumption graphs can already give insights on memory leaks and excessive allocation patterns.
However, when only working with memory allocation metrics it is hard to isolate if a job was running close to a memory limit, or encountered an error when running out of memory.
Namespace's automatic OOM detection makes these conditions explicit and simple to detect.

![Job OOM Warning](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Foom-job.1dc36b91.png&w=1200&q=75)

### Crash Dump Collection

Namespace can automatically detect if your job execution crashes, collect crash dumps, and store them as [artifacts](/docs/architecture/storage/artifact-storage).
These dumps contain invaluable forensic information useful for determining the cause of the crash.
Crash dump collection is not enabled by default - reach out to [support@namespace.so](mailto:support@namespace.so) to get access.

## Investigating Queue Time

The [insights view](https://cloud.namespace.so/workspace/ghrunners/insights) offers comprehensive performance analytics of your jobs over time.
By default, the explorer displays your job durations, but you can also understand the queue time by changing the view on the top right.
If you are investigating a recent case of surprisingly long queue time, adjust the timeframe to match your investigation.

![Queue time insights](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fqueue-time.ef86e900.png&w=1200&q=75)

The most common reason for queue time is that you are hitting your concurrency limits.
You can see the concurrent resource usage in the [usage dashboard](https://cloud.namespace.so/workspace/usage/concurrency).

![Concurrent resource usage](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fconcurrent-resource-usage.5cf9bb18.png&w=1200&q=75)

If you are frequently reaching your resource limits, you may benefit from a larger plan. We'd be happy to put a custom plan together for you.
Reach out to our [Sales Team](mailto:sales@namespace.so) for custom plans that scale up to thousands of vCPUs and TBs of RAM.

## Hands-on Support

Got stuck? Need help with debugging one of your workflows? Our team is here to assist:

- **Technical Support**: Reach out to [support@namespace.so](mailto:support@namespace.so) to talk to one of our engineers.
- **Community**: Join our community [Discord](https://discord.gg/DqMzDFR6Hc) to learn about tips and best practices.

Last updated December 21, 2025
