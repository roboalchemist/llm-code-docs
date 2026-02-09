# Source: https://docs.datadoghq.com/profiler/profile_types.md

---
title: Profile Types
description: Datadog, the leading service for cloud-scale monitoring.
breadcrumbs: Docs > Continuous Profiler > Profile Types
---

# Profile Types

In the **Profiles** tab, you can see all profile types available for a given language. Depending on the language and version, the information collected about your profile differs.

{% tab title="Java" %}
Once profiling is enabled, the following profile types are collected for [supported Java versions](https://docs.datadoghq.com/profiler/enabling/java/#requirements):

{% dl %}

{% dt %}
CPU
{% /dt %}

{% dd %}
The time each method spent running on the CPU. It includes your code that runs in the JVM (for example, Java, Kotlin), but not JVM operations or native code called from within the JVM.
{% /dd %}

{% dt %}
Allocations
{% /dt %}

{% dd %}
The number of heap allocations made by each method, including allocations which were subsequently freed.*Requires: Java 11*
{% /dd %}

{% dt %}
Allocated Memory
{% /dt %}

{% dd %}
The amount of heap memory allocated by each method, including allocations which were subsequently freed.*Requires: Java 11*
{% /dd %}

{% dt %}
Heap Live Objects (in Preview, 1.17.0+)
{% /dt %}

{% dd %}
The number of objects allocated by each method in heap memory that have not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.*Requires: Java 11*
{% /dd %}

{% dt %}
Heap Live Size (in Preview, 1.39.0+)
{% /dt %}

{% dd %}
The amount of heap memory allocated by each method that has not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.*Requires: Java 11.0.23+, 17.0.11+, 21.0.3+ or 22+*
{% /dd %}

{% dt %}
Wall Time in Native Code
{% /dt %}

{% dd %}
The elapsed time spent by each method. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the method is running.
{% /dd %}

{% dt %}
Class Load
{% /dt %}

{% dd %}
The number of classes loaded by each method.
{% /dd %}

{% dt %}
Thrown Exceptions
{% /dt %}

{% dd %}
The number of errors and exceptions thrown by each method, as well as their type.
{% /dd %}

{% dt %}
File I/O
{% /dt %}

{% dd %}
The time each method spent reading from and writing to files.
{% /dd %}

{% dt %}
Lock
{% /dt %}

{% dd %}
The time each method spent waiting for a lock.
{% /dd %}

{% dt %}
Socket I/O
{% /dt %}

{% dd %}
The time each method spent reading from and writing to socket I/O.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Python" %}
Once profiling is enabled, the following profile types are collected, depending on your [Python version](https://docs.datadoghq.com/profiler/enabling/python/#requirements) as noted:

{% dl %}

{% dt %}
Wall Time
{% /dt %}

{% dd %}
The elapsed time used by each function. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the function is running.*Requires: Python 2.7+*
{% /dd %}

{% dt %}
Lock Wait Time
{% /dt %}

{% dd %}
The time each function spent waiting for a lock.*Requires: Python 2.7+*
{% /dd %}

{% dt %}
Locked Time
{% /dt %}

{% dd %}
The time each function spent holding a lock.*Requires: Python 2.7+*
{% /dd %}

{% dt %}
Lock Acquires
{% /dt %}

{% dd %}
The number of times each function acquired a lock.*Requires: Python 2.7+*
{% /dd %}

{% dt %}
Lock Releases
{% /dt %}

{% dd %}
The number of times each function released a lock.*Requires: Python 2.7+*
{% /dd %}

{% dt %}
CPU
{% /dt %}

{% dd %}
The time each function spent running on the CPU, including Python and native code.*Requires: Python 2.7+, POSIX platform*
{% /dd %}

{% dt %}
Heap Live Size
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function that has not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.*Requires: Python 3.5+*
{% /dd %}

{% dt %}
Allocated Memory
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function, including allocations which were subsequently freed.*Requires: Python 3.5+*
{% /dd %}

{% dt %}
Allocations
{% /dt %}

{% dd %}
The number of heap allocations made by each function, including allocations which were subsequently freed.*Requires: Python 3.5+*
{% /dd %}

{% dt %}
Thrown Exceptions
{% /dt %}

{% dd %}
The number of caught or uncaught exceptions raised by each function, as well as their type.*Requires: Python 3.7+, POSIX platform*
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Go" %}
Once profiling is enabled, the following profile types are collected for supported [Go versions](https://docs.datadoghq.com/profiler/enabling/go#requirements):

{% dl %}

{% dt %}
CPU Time
{% /dt %}

{% dd %}
The time each function spent running on the CPU. Off-CPU time such as waiting for Networking, Channels, Mutexes, and Sleep are not captured in this profile. See Mutex and Block profiles.
{% /dd %}

{% dt %}
Allocations
{% /dt %}

{% dd %}
The number of objects allocated by each function in heap memory during the profiling period (default: 60s), including allocations which were subsequently freed. Go calls this `alloc_objects`. Stack allocations are not tracked. This is useful for investigating garbage collection load. See also the note about how this measure changes in version `1.33.0` in Delta profiles.
{% /dd %}

{% dt %}
Allocated Memory
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function during the profiling period (default: 60s), including allocations which were subsequently freed. Go calls this `alloc_space`. Stack allocations are not tracked. This is useful for investigating garbage collection load. See also the note about how this measure changes in version `1.33.0` in Delta profiles.
{% /dd %}

{% dt %}
Heap Live Objects
{% /dt %}

{% dd %}
The number of objects allocated by each function in heap memory that remain in use after garbage collection. Go calls this `inuse_objects`. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.
{% /dd %}

{% dt %}
Heap Live Size
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function that remains in use after garbage collection. Under default settings (GOGC=100), this will typically represent ~50% of the RSS usage of the process. Go calls this `inuse_space`. Use this metric to review memory consumption and [diagnose leaks](https://docs.datadoghq.com/profiler/guide/solve-memory-leaks). For more details about how Go manages memory, see [Go memory metrics demystified](https://www.datadoghq.com/blog/go-memory-metrics/) and [A Guide to the Go Garbage Collector](https://go.dev/doc/gc-guide).
{% /dd %}

{% dt %}
Mutex
{% /dt %}

{% dd %}
The time functions have been waiting on mutexes during the profiling period (default: 60s). The stack traces in this profile point the `Unlock()` operation that allowed another goroutine blocked on the mutex to proceed. Short mutex contentions using spinlocks are not captured by this profile, but can be seen in the CPU profile. See also the note about how this measure changes in version `1.33.0` in Delta profiles.
{% /dd %}

{% dt %}
Block
{% /dt %}

{% dd %}
The time functions have been waiting on mutexes and channel operations during the profiling period (default: 60s). Sleep, GC, Network, and Syscall operations are not captured by this profile. Blocking operations are only captured after they become unblocked, so this profile cannot be used to debug applications that appear to be stuck. For mutex contentions, the stack traces in this profile point to blocked `Lock()` operations. This tells you where your program is getting blocked, while the mutex profile tells you what part of your program is causing the contention. See Datadog's [Block Profiling in Go](https://github.com/DataDog/go-profiler-notes/blob/main/block.md) research for more in-depth information. See also the note about how this measure changes in version `1.33.0` in Delta profiles. **Note**: The block profiler can cause noticeable overhead for production workloads. If enabling it in production, prefer high rates (such as `100000000`, which is 100 milliseconds) and look for signs of increased latency or CPU utilization.
{% /dd %}

{% dt %}
Goroutines
{% /dt %}

{% dd %}
A snapshot of the number of goroutines currently executing the same functions (both on-CPU and waiting off-CPU). An increasing number of goroutines between snapshots can indicate that the program is leaking goroutines. In most healthy applications this profile is dominated by worker pools and the number of goroutines they use. Applications that are extremely latency-sensitive and use a large number of goroutines (> 10.000) should be aware that enabling this profile requires stop-the-world pauses. The pauses occur only once every profiling period (default 60s) and normally last for around `1Âµsec` per goroutine. Typical applications with a p99 latency SLO of around `100ms` can generally ignore this warning. See Datadog's [Goroutine Profiling in Go](https://github.com/DataDog/go-profiler-notes/blob/main/goroutine.md) research for more in-depth information.
{% /dd %}

{% /dl %}

#### Delta profiles{% #delta-profiles %}

{% alert level="info" %}
In Go profiler versions before `1.33.0`, Allocations, Allocated Memory, Mutex, and Block metrics are shown as measures *accumulated since the process was started*, as opposed to *during the profiling period*. The change to delta profiles in version `1.33.0` lets you see how these measures are changing instead of accumulating. Delta profiling is on by default. Profiler version `1.35.0` allows you to disable delta profiles using the `WithDeltaProfiles` option.As of profiler version `1.37.0`, accumulated profiles are no longer uploaded when delta profiling is enabled to reduce upload bandwidth usage. [Contact Support](https://docs.datadoghq.com/help/) to discuss your use case if you rely on the full accumulated profiles.
{% /alert %}

{% /tab %}

{% tab title="Ruby" %}
Once profiling is enabled, the following profile types are collected for [supported Ruby versions](https://docs.datadoghq.com/profiler/enabling/ruby/#requirements):

{% dl %}

{% dt %}
CPU
{% /dt %}

{% dd %}
The time each function spent running on the CPU, including Ruby and native code.
{% /dd %}

{% dt %}
Wall Time
{% /dt %}

{% dd %}
The elapsed time used by each function. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the function is running.
{% /dd %}

{% dt %}
Allocations (v2.3.0+)
{% /dt %}

{% dd %}
The number of objects allocated by each method during the profiling period (default: 60s), including allocations which were subsequently freed. This is useful for investigating garbage collection load.*Requires:* [Manual enablement](https://docs.datadoghq.com/profiler/enabling/ruby/#configuration)
{% /dd %}

{% dt %}
Heap Live Objects (Preview, v2.18.0+)
{% /dt %}

{% dd %}
The number of objects allocated by each method in heap memory that have not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.*Requires: Ruby 3.1+* and [manual enablement](https://docs.datadoghq.com/profiler/enabling/ruby/#configuration) (Not yet compatible with Ruby 4)
{% /dd %}

{% dt %}
Heap Live Size (Preview, v2.18.0+)
{% /dt %}

{% dd %}
The amount of heap memory allocated by each method that has not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.*Requires: Ruby 3.1+* and [manual enablement](https://docs.datadoghq.com/profiler/enabling/ruby/#configuration) (Not yet compatible with Ruby 4)
{% /dd %}

{% dt %}
GVL profiling (in Timeline) (v2.11.0+)
{% /dt %}

{% dd %}
Records time when threads are prevented from working by other "noisy neighbor" threads, including background threads. This is useful for investigating latency spikes in the application when using the timeline visualization.*Requires: Ruby 3.2+*
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Node.js" %}
Once profiling is enabled, the following profile types are collected for [supported Node.js versions](https://docs.datadoghq.com/profiler/enabling/nodejs/#requirements):

{% dl %}

{% dt %}
CPU
{% /dt %}

{% dd %}
The time each function spent running on the CPU, including JavaScript and native code.
{% /dd %}

{% dd %}
CPU profiling is available on Linux and macOS. The feature is not available on Windows.
{% /dd %}

{% dt %}
Wall Time
{% /dt %}

{% dd %}
The elapsed time used by each function. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the function is running.
{% /dd %}

{% dt %}
Heap Live Size
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function that has not yet been garbage collected. This is useful for investigating the overall memory usage of your service and identifying potential memory leaks.
{% /dd %}

{% dd %}
Deep stack traces in Heap Live Size profiles are truncated to 64 frames.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title=".NET" %}
Once profiling is enabled, the following profile types are collected for [supported .NET versions](https://docs.datadoghq.com/profiler/enabling/dotnet/#requirements):

{% dl %}

{% dt %}
Wall Time
{% /dt %}

{% dd %}
The elapsed time spent in managed methods. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the method is running.
{% /dd %}

{% dt %}
CPU (v2.15+)
{% /dt %}

{% dd %}
The time each method spent running on the CPU.
{% /dd %}

{% dt %}
Thrown Exceptions (v2.31+)
{% /dt %}

{% dd %}
The number of caught or uncaught exceptions raised by each method, as well as their type and message.
{% /dd %}

{% dt %}
Allocations (v3.28+)
{% /dt %}

{% dd %}
The number and size of allocated objects by each method, as well as their type. For .NET Framework, the size is not available._Requires: .NET Framework (with Datadog Agent 7.51+ and v3.2+) / .NET 6+, but Datadog recommends .NET 10+ for more accurate sampling.
{% /dd %}

{% dt %}
Lock (v2.49+)
{% /dt %}

{% dd %}
The number of times threads are waiting for a lock and for how long.*Requires: .NET Framework (requires Datadog Agent 7.51+) / .NET 5+*
{% /dd %}

{% dt %}
Live Heap (v3.28+)
{% /dt %}

{% dd %}
A subset of the allocated objects (with their class name) that are still in memory._Requires: .NET 7+ but Datadog recommends .NET 10+ for more accurate sampling.
{% /dd %}

{% dt %}
Outgoing HTTP requests (in Timeline) (in beta v3.19+)
{% /dt %}

{% dd %}
Start and end of outgoing HTTP requests with the duration of the different phases (DNS, security handshake, socket, request/response) and possible unexpected redirections.*Requires: .NET 7+*
{% /dd %}

{% dt %}
Thread lifetime (in Timeline) (v3.19+)
{% /dt %}

{% dd %}
Start and end of threads life to easily detect ThreadPool starvation and short lived threads.*Requires: .NET Framework (with Datadog Agent 7.51+ and v3.2+) / .NET 5+*
{% /dd %}

{% dt %}
Garbage Collector CPU consumption (v3.19+)
{% /dt %}

{% dd %}
The time garbage collector's threads spent running on the CPU.*Requires: .NET Framework (with Datadog Agent 7.51+ and v3.2+) / .NET 5+*
{% /dd %}

{% /dl %}

**Note**: Before .NET 10, **Allocations** and **Live Heap** profiling might show bigger objects more than smaller ones due to the sampling algorithm used by the .NET runtime. Datadog recommends using .NET 10+ for more statistically correct results.
{% /tab %}

{% tab title="PHP" %}
Once profiling is enabled, the following profile types are collected for [supported PHP versions](https://docs.datadoghq.com/profiler/enabling/php/#requirements):

{% dl %}

{% dt %}
Wall Time
{% /dt %}

{% dd %}
The elapsed time used by each function. Elapsed time includes time when code is running on CPU, waiting for I/O, and anything else that happens while the function is running.
{% /dd %}

{% dt %}
CPU
{% /dt %}

{% dd %}
Shows the time each function spent running on the CPU.
{% /dd %}

{% dt %}
Allocations (v0.88+)
{% /dt %}

{% dd %}
The number of allocations by each function during the profiling period (default: 67s), including allocations which were subsequently freed. Stack allocations are not tracked.*Note: Not available when JIT is active on PHP `8.0.0`-`8.1.20` and `8.2.0`-`8.2.7`*
{% /dd %}

{% dt %}
Allocated memory (v0.88+)
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function during the profiling period (default: 67s), including allocations which were subsequently freed. Stack allocations are not tracked.*Note: Not available when JIT is active on PHP `8.0.0`-`8.1.20` and `8.2.0`-`8.2.7`*
{% /dd %}

{% dt %}
Thrown Exceptions (v0.92+)
{% /dt %}

{% dd %}
The number of caught or uncaught exceptions raised by each method, as well as their type.
{% /dd %}

{% dt %}
File I/O (in beta, v1.7.2+)
{% /dt %}

{% dd %}
The time each method spent reading from and writing to files, as well as the amount of bytes read from and written to files.
{% /dd %}

{% dt %}
Socket I/O (in beta, v1.7.2+)
{% /dt %}

{% dd %}
The time each method spent reading from and writing to a socket, as well as the amount of bytes read from and written to sockets.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Rust/C/C++" %}
Once profiling is enabled, the following profile types are collected for [supported languages and versions](https://docs.datadoghq.com/profiler/enabling/ddprof/):

{% dl %}

{% dt %}
CPU
{% /dt %}

{% dd %}
The time each function spent running on the CPU.
{% /dd %}

{% dt %}
Allocations
{% /dt %}

{% dd %}
The number of allocations by each function during the profiling period (default: 59s), including allocations which were subsequently freed. Stack allocations are not tracked.
{% /dd %}

{% dt %}
Allocated memory
{% /dt %}

{% dd %}
The amount of heap memory allocated by each function during the profiling period (default: 59s), including allocations which were subsequently freed. Stack allocations are not tracked.
{% /dd %}

{% /dl %}

{% /tab %}

{% tab title="Full Host" %}
Once profiling is enabled, the following profile types are collected for [supported languages and versions](https://docs.datadoghq.com/profiler/enabling/full_host/):

{% dl %}

{% dt %}
CPU Time (eBPF)
{% /dt %}

{% dd %}
Time each method or function spent running on the CPU. In multi-threaded programs, CPU time can be greater than elapsed time: if 2 threads are running during 45s each, you'd see "eBPF CPU Time, 1m 30s per minute".
{% /dd %}

{% /dl %}

{% /tab %}

## Further Reading{% #further-reading %}

- [Enable continuous profiler for your application](https://docs.datadoghq.com/profiler/enabling)
- [Getting Started with Profiler](https://docs.datadoghq.com/getting_started/profiler)
- [Introducing always-on production profiling in Datadog](https://www.datadoghq.com/blog/introducing-datadog-profiling/)
