# Source: https://quarkus.io/performance

Title: Quarkus Performance

URL Source: https://quarkus.io/performance

Markdown Content:
### Designed for Fast Startup, High Throughput, and Low Resource Consumption

![Image 1: Container image](https://quarkus.io/assets/images/performance/icon-performance.svg)![Image 2: Container image](https://quarkus.io/assets/images/performance/icon-performance-dark.svg)

Quarkus is engineered to be efficient by using build-time optimizations and a reactive core to achieve fast startup times, high throughput, low response latency, reduced memory footprint, and minimal resource consumption. As a result, Quarkus is fast... real fast.

Starting fast by doing less: the build-time principle
-----------------------------------------------------

Quarkus redefines how Java applications are built and executed by shifting much of the work to the build phase ensuring that the costly work happens only once — during the build process — not at every startup. It results in faster, smaller, and more resource-efficient Java applications on both GraalVM native images and traditional JVM deployments.

For example, at build time, Quarkus reads part of the application configuration, scans the classpath for annotated classes, and constructs a model of the application. By doing this early, Quarkus has enough information to eliminate unnecessary components and compute the exact startup instructions required.

![Image 3: Quarkus Build Time Principle](https://quarkus.io/assets/images/container/build-time-principle-light.png)![Image 4: Quarkus Build Time Principle](https://quarkus.io/guides/images/build-time-principle.png)

This build-time optimization offers several key benefits:

1.   **Reduced startup time:** Quarkus performs most of the heavy work at build-time, significantly cutting startup time and allowing the app to reach peak performance faster.
2.   **Lower memory consumption:** By minimizing allocations and class loading, Quarkus reduces memory usage. Replacing reflection with build-time bytecode generation further lowers the JVM's runtime workload.
3.   **Better latency and improved throughput:** Quarkus generates highly optimized code at build time and prunes unnecessary classes and methods. For instance, it weaves layers of indirection together, enabling better JIT optimizations. These improvements result in faster code and better latency. 

High concurrency without the headaches: the reactive core
---------------------------------------------------------

Quarkus is built on reactive principles, using an efficient asynchronous, non-blocking engine based on Netty and Eclipse Vert.x. It employs a few event loops instead of a large thread pool, reducing resource usage and improving response times by optimizing for hardware behavior.

Reactive underneath does not mean you must write reactive code. Quarkus offers three development models:

1.   **Imperative model:** A traditional synchronous approach with faster execution due to an optimized I/O layer, ideal for lower concurrency. High concurrency increases memory use.
2.   **Reactive model:** Enables high concurrency with minimal resources using asynchronous, non-blocking code, but is more complex to implement and debug.
3.   **Virtual threads (JDK 21+):** Combines the benefits of imperative and reactive models, allowing imperative code to run on lightweight virtual threads for high concurrency with low memory overhead, though some limitations remain.

What happens when the build time principle and the reactive core are combined?
------------------------------------------------------------------------------

The combination of the build time optimization and reactive core makes Quarkus a highly efficient framework, excelling in several key areas:

![Image 5: Memory icon](https://quarkus.io/assets/images/performance/icon-memory.svg)![Image 6: Memory icon](https://quarkus.io/assets/images/performance/icon-memory-dark.svg)

### Reduced Memory

The build-time principle minimizes runtime memory use by eliminating unnecessary components and precomputing at build time, reducing class loading and memory allocations. The reactive core further cuts memory usage by using a few event loops instead of a large thread pool, allowing the application to handle higher loads with a smaller memory footprint and enabling high deployment density.

![Image 7: Startup icon](https://quarkus.io/assets/images/performance/icon-startup.svg)![Image 8: Startup icon](https://quarkus.io/assets/images/performance/icon-startup-dark.svg)

### Fast Startup Time

Thanks to the build-time optimizations, most of the application’s heavy lifting, such as classpath scanning, configuration loading, and dependency injection setup, happens before the application even starts. This significantly reduces the time it takes to get the application up and ready to serve. The reactive core contributes to this by ensuring that I/O operations are handled with minimal blocking, further reducing the startup latency. The efficient startup process means the application can respond to new load conditions more quickly. This combination supports implementing LightSwitchOps patterns, enabling elasticity while controlling costs.

![Image 9: Throughput icon](https://quarkus.io/assets/images/performance/icon-throughput.svg)![Image 10: Throughput icon](https://quarkus.io/assets/images/performance/icon-throughput-dark.svg)

### High Throughput

Build-time optimizations ensure tasks like classpath scanning, configuration loading, and dependency injection are completed before startup, greatly reducing startup time. This efficient startup enables quicker responses to load changes and supports LightSwitchOps patterns for cost-effective elasticity. The reactive core minimizes blocking in I/O operations, further lowering latency and allowing handling a large number of concurrent tasks.

![Image 11: Disk footprint icon](https://quarkus.io/assets/images/performance/icon-diskspace.svg)![Image 12: Disk footprint icon](https://quarkus.io/assets/images/performance/icon-diskspace-dark.svg)

### Optimized Resource Consumption

The build-time principle and reactive core optimize CPU, memory, and system resource use, enabling high performance with fewer resources. This lowers operational costs in cloud environments and offers sustainability benefits through reduced resource consumption.
