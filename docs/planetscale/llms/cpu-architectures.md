# Source: https://planetscale.com/docs/postgres/cluster-configuration/cpu-architectures.md

# CPU Architectures

> When deploying PostgreSQL databases, choosing the right CPU architecture is crucial for optimizing performance, cost, and efficiency. PlanetScale Postgres supports both x86-64 and ARM64 (aarch64) architectures, with ARM64 instances powered by AWS Graviton processors.

## Architecture Overview

### x86-64 (Intel/AMD)

The x86-64 architecture has been the dominant server architecture for decades. These processors offer:

* Mature ecosystem with extensive software optimization
* Wide compatibility with existing applications and tools
* High single-threaded performance
* Established performance benchmarks and tuning practices

### ARM64 (AWS Graviton)

ARM64 represents the next generation of server processors, with [AWS Graviton chips](https://aws.amazon.com/ec2/graviton/) specifically designed for cloud workloads:

* Custom silicon optimized for cloud applications
* Superior price-performance ratio
* Lower power consumption
* Built on modern 64-bit ARM architecture

## Performance Comparison

### CPU Performance

* **Single-threaded**: x86-64 processors typically offer higher single-threaded performance
* **Multi-threaded**: ARM64 Graviton processors excel in multi-threaded workloads common in database operations
* **Memory bandwidth**: Graviton processors provide higher memory bandwidth, beneficial for data-intensive PostgreSQL operations

### PostgreSQL-Specific Performance

* **OLTP workloads**: ARM64 shows 10-20% better performance per dollar for typical transaction processing
* **Analytics workloads**: Both architectures perform similarly for complex analytical queries
* **Concurrent connections**: ARM64 handles high-concurrency scenarios more efficiently
* **Background processes**: ARM64's multi-core design benefits PostgreSQL's background maintenance tasks

## Cost Considerations

### Infrastructure Costs

* **ARM64 instances**: Typically 20-40% lower cost than equivalent x86-64 instances
* **Performance per dollar**: ARM64 generally provides better price-performance ratios
* **Energy efficiency**: ARM64 processors consume less power, reducing operational costs

### Total Cost of Ownership

* **Development overhead**: x86-64 may have lower initial setup costs due to existing tooling
* **Long-term savings**: ARM64 offers significant cost savings for sustained workloads
* **Scaling costs**: ARM64 becomes more cost-effective as your database scales

## Compatibility and Ecosystem

### Software Compatibility

* **PostgreSQL**: Full native support on both architectures ([PostgreSQL supported platforms](https://www.postgresql.org/docs/current/supported-platforms.html))
* **Extensions**: Most popular PostgreSQL extensions support ARM64 ([PostgreSQL ARM64 package repository](https://www.postgresql.org/about/news/arm64-on-aptpostgresqlorg-2033/))
* **Tools**: Database administration tools work seamlessly on both platforms
* **Drivers**: All major PostgreSQL drivers support ARM64

### Migration Considerations

* **Existing applications**: Applications using standard PostgreSQL drivers require no changes
* **Binary extensions**: Custom compiled extensions may need recompilation for ARM64
* **Performance tooling**: Some x86-specific optimization tools may not be available on ARM64

## Decision Matrix

| Consideration                   | x86-64            | ARM64 (Graviton)                           |
| :------------------------------ | :---------------- | :----------------------------------------- |
| **Price-performance ratio**     | Standard          | Superior (20-40% cost savings)             |
| **Single-threaded performance** | Higher            | Good                                       |
| **Multi-threaded performance**  | Good              | Superior                                   |
| **PostgreSQL extensions**       | Universal support | Most supported, some require recompilation |
| **Energy efficiency**           | Standard          | Superior                                   |

**Choose x86-64 when:**

* Legacy applications or custom extensions require x86-64
* Maximum single-threaded performance is critical
* Strict compliance requirements mandate x86-64
* Existing monitoring infrastructure is x86-64 specific

**Choose ARM64 (Graviton) when:**

* Cost optimization is a priority
* Running concurrent, multi-threaded workloads
* Starting new projects without legacy constraints
* Environmental impact reduction is important

## Getting Started

Both architectures are available when creating new PostgreSQL databases in PlanetScale Postgres. You can specify your preferred architecture during the database creation process. For most new deployments, ARM64 provides the best combination of performance, cost-effectiveness, and future-proofing.

Consider running performance tests with your specific workload on both architectures to make the most informed decision for your use case.

<Note>
  Once you've selected your desired CPU architecture, you can not modify a launched database cluster to be mixed CPU architecture nor modify your cluster to change CPU architecture. For help in swapping your CPU architecture, please [reach out to support](https://planetscale.com/contact?initial=support).
</Note>

## CPU Architecture availability

Depending on your target region for your deployment, there may or may not be certain cluster size configurations that are available from the underlying provider. PlanetScale aims to have the most complete availability of resources for you to use and as is such may enable or disable certain configurations over time based on availability.

<Note>
  The most accurate source of this information is on the [Create a new database](https://app.planetscale.com/new) page and then selecting the desired region.

  For customers of managed deployments, please [reach out to support](https://planetscale.com/contact?initial=support) for assistance in confirming availability for your deployment.
</Note>

## Additional Resources

<Columns cols={2}>
  <Card title="AWS Graviton Performance Studies" icon="angles-right" horizontal href="https://aws.amazon.com/ec2/graviton" />

  <Card title="PostgreSQL Performance Tuning" icon="angles-right" horizontal href="https://wiki.postgresql.org/wiki/Performance_Optimization" />

  <Card title="PostgreSQL ARM64 Support Documentation" icon="angles-right" horizontal href="https://www.postgresql.org/docs/current/supported-platforms.html" />

  <Card title="AWS RDS PostgreSQL ARM64 Migration Guide" icon="angles-right" horizontal href="https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide" />
</Columns>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt