# Source: https://docs.anyscale.com/get-started/development-concepts.md

# Development concepts

[View Markdown](/get-started/development-concepts.md)

# Development concepts

This page introduces the fundamental concepts and mental models you need when transitioning from single-node development to building distributed AI applications with Ray and Anyscale.

## Single-node versus distributed computing[​](#single-vs-distributed "Direct link to Single-node versus distributed computing")

When transitioning from single-node to distributed computing, several fundamental differences affect how you design and deploy applications:

**Resource coordination**: Instead of running on one machine, your code executes across multiple nodes. Ray handles the complexity of coordinating these resources, but you need to understand how to account for parallelism in your code.

**Dependency distribution**: Libraries and packages must be available on every node that executes your code. Anyscale provides multiple approaches for managing dependencies, from container images to runtime environments. See [Dependency management on Anyscale](/dependency-management.md).

**Data locality**: In distributed systems, moving computation to data is often more efficient than moving data to computation. Ray's scheduling considers data locality to minimize network overhead.

**Failure handling**: With more machines involved, partial failures become more common. Ray provides fault tolerance through automatic retries and checkpointing, but you should design your applications with failure recovery in mind.

**Debugging complexity**: Issues may occur on any node in the cluster. Anyscale provides comprehensive monitoring and logging tools to help you identify and resolve problems across distributed systems. See [Monitor and debug Anyscale workloads](/monitoring.md).

## Ray's distributed computing model[​](#ray-model "Direct link to Ray's distributed computing model")

Ray provides a unified computing framework that abstracts the complexity of distributed systems while giving you control over parallelism and resource allocation.

### Core abstractions[​](#core-abstractions "Direct link to Core abstractions")

Ray uses three primary abstractions to enable distributed computing:

**Tasks**: Stateless functions that Ray can execute in parallel across your cluster. When you decorate a function with `@ray.remote`, Ray can schedule it on any available worker node.

**Actors**: Stateful workers that maintain their own memory between method calls. Actors provide a way to manage state in distributed applications while maintaining the benefits of parallel execution.

**Objects**: Immutable values stored in Ray's distributed object store. Ray automatically manages object placement and memory across your cluster, enabling efficient data sharing between tasks and actors.

These primitives work together to enable patterns like:

* Parallel data processing across thousands of cores.
* Distributed training across multiple GPUs.
* Serving multiple models from a single cluster.
* Complex pipelines mixing CPU and GPU workloads.

For hands-on examples of these concepts, see [Ray basics](/get-started/ray-basics.md).

## Development workflows on Anyscale[​](#development-workflows "Direct link to Development workflows on Anyscale")

Anyscale supports multiple development workflows to match your preferences and requirements:

### Interactive development[​](#interactive-development "Direct link to Interactive development")

Anyscale workspaces provide cloud-hosted development environments with pre-configured Ray clusters. This approach offers:

* Immediate access to distributed compute resources.
* Integrated development tools including VS Code and JupyterLab.
* Direct iteration on code, dependencies, and cluster configuration.
* Real-time debugging with Ray dashboard and distributed debugger.

For more details, see [Workspaces](/platform/workspaces.md).

### Local development with remote execution[​](#local-development "Direct link to Local development with remote execution")

Develop in your local environment and submit workloads to Anyscale for execution. This pattern works well for:

* Teams with established local development workflows.
* Integration with existing CI/CD pipelines.
* Production deployments through jobs and services.

For implementation details, see [Develop Anyscale applications](/development.md).

## From development to production[​](#development-to-production "Direct link to From development to production")

Anyscale uses consistent configurations across development and production environments, enabling smooth transitions between stages:

**Consistent cluster definitions**: Workspaces, jobs, and services all use the same container images and compute configurations. Test configurations in development and deploy them unchanged to production.

**Progressive deployment options**:

1. Start with interactive development in workspaces.
2. Test automation with Anyscale jobs for batch workloads.
3. Deploy models with Anyscale services for online serving.
4. Scale to production with the same code and configurations.

**Environment parity**: Use the same dependencies, Ray version, and cluster configurations across all environments to minimize deployment surprises.

For detailed guidance on production deployments, see:

* [What are Anyscale jobs?](/jobs.md).
* [What are Anyscale services?](/services.md).
* [Container-driven development on Anyscale](/development/containers.md).

## Anyscale Runtime optimizations[​](#runtime "Direct link to Anyscale Runtime optimizations")

Anyscale provides the Anyscale Runtime, an optimized version of Ray that maintains API compatibility while delivering better performance:

**Transparent optimizations**: Your Ray code runs faster on Anyscale without modifications. The Anyscale Runtime optimizes the execution engine without changing APIs.

**Specific improvements** include optimizations for:

* Data processing. See [Ray Data](/runtime/data.md).
* Distributed training. See [Ray Train](/runtime/train.md).
* Model serving. See [Ray Serve on the Anyscale Runtime](/runtime/serve.md).

**Development flexibility**: Develop with open source Ray on your laptop, then deploy to Anyscale for production performance benefits.

## Common patterns and best practices[​](#patterns "Direct link to Common patterns and best practices")

As you build distributed applications with Ray and Anyscale, these patterns help you maximize efficiency:

**Start simple, scale gradually**: Begin with small-scale testing in a workspace, then increase cluster size as you validate your approach.

**Leverage Ray libraries**: Use purpose-built libraries like Ray Data, Ray Train, and Ray Serve rather than implementing distributed logic from scratch. See [What is Ray?](/get-started/what-is-ray.md).

**Design for elasticity**: Configure clusters with autoscaling to handle variable workloads efficiently. See [Compute configuration on Anyscale](/configuration/compute.md).

**Monitor resource utilization**: Use Anyscale's monitoring tools to identify bottlenecks and optimize resource allocation. See [Metrics](/monitoring/metrics.md).

## Next steps[​](#next-steps "Direct link to Next steps")

Now that you understand the conceptual foundation:

* Follow hands-on tutorials starting with [Tutorial: Create a workspace](/get-started/create-workspace.md).
* Learn about [platform architecture](/get-started/architecture.md) for deeper technical understanding.
* Review [configuration options](/configuration.md) for customizing clusters.
