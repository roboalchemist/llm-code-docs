# Source: https://docs.anyscale.com/get-started/next-steps.md

# Next steps

[View Markdown](/get-started/next-steps.md)

# Next steps

You now know how to use Anyscale workspaces to launch a cluster and run workloads. Anyscale recommends the following resources.

## Bring your workload to production[​](#production "Direct link to Bring your workload to production")

While workspaces provide an excellent remote development environment, some users choose to develop in a local environment and run the workload remotely. For this approach, you can rely on Anyscale jobs and services. When paired with CI/CD and monitoring, they're also Anyscale's recommended method for bringing workloads to production.

### Anyscale jobs[​](#anyscale-jobs "Direct link to Anyscale jobs")

Jobs provide features like automated failure handling, email alerting, and persisted outputs and logs. While Anyscale jobs are similar to Ray Jobs, Anyscale jobs don't require an active cluster for submission. Instead, each individual job spins up its own cluster and executes your Python code (unless you're using a Job Queue, in which case Anyscale reuses clusters).

The lifecycle of an Anyscale job includes:

1. Starting a cluster.
2. Running your Python code.
3. Restarting any failed nodes.
4. Terminating the cluster.

See [What are Anyscale jobs?](/jobs.md).

### Anyscale services[​](#anyscale-services "Direct link to Anyscale services")

Anyscale services give you a scalable, fault-tolerant API endpoint for your online inference workloads. They support autoscaling, observability through Grafana dashboards, high-availability, and zero downtime upgrades.

The lifecycle of an Anyscale service includes:

1. Creating a cluster.

2. Creating a load balancer (1 per Anyscale cloud).

3. Running your Ray Serve Python application.

4. Dealing with any node failures (see [here](/administration/resource-management/head-node-fault-tolerance.md) on how to set up HA for the head node).

5. Rolling out new versions of your application.

   <!-- -->

   * New versions will start a new cluster.
   * Place the new cluster behind the load balancer.
   * Once the new version is healthy, shift traffic over to the new version over a couple of minutes.
   * Terminate the old version's cluster.

See [Get started with services](/services/tutorial.md).

## Create your own cluster configuration[​](#cluster-config "Direct link to Create your own cluster configuration")

Thus far, you've used a workspace with the default cluster configuration. Anyscale provides extensive capabilities to shape the cluster to your needs. To get started with container images and compute configurations, you can follow the documentation in [Configuration overview](/configuration.md). The configuration section also provides details on the different kinds of storage that clusters use.

## Explore templates[​](#templates "Direct link to Explore templates")

On the homepage of the Anyscale console, you find many different templates to explore. With two clicks you can spin up a workspace with step-by-step instructions that show how to build different Ray applications.

![A few examples of Anyscale templates](/assets/images/next-steps-templates-a21637d59943f69588a65fc4cd43114e.png)

Understanding Anyscale

[Development concepts](/get-started/development-concepts.md) - Learn the fundamental concepts and mental models for building distributed AI applications with Ray and Anyscale.
