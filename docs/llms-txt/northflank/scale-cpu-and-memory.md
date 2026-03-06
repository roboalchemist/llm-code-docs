# Source: https://northflank.com/docs/v1/application/scale/scale-cpu-and-memory.md

# Scale CPU and memory

You can increase the proportion of CPU and memory dedicated to a service on the resources page, available for all Northflank services.

Increasing the CPU share, or assigning one or multiple CPUs, and memory size can be useful if builds are taking a long time or if your service is handling intensive tasks.

![Selecting the compute plan for a deployment service in the Northflank application](https://assets.northflank.com/documentation/v1/application/scale/scale-cpu-and-memory-resources/scale-compute.png)

See [Northflank pricing plans](https://northflank.com/pricing) for CPU and memory resources.

## Increase Docker SHM size

You can configure the amount of available memory-backed disk space available to `/dev/shm` from the resources page of combined services, deployment services, and jobs. The default SHM size assigned to containers is 64MB.

Using `/dev/shm/` can significantly increase performance over using `/tmp` for I/O intensive processes.

Writing to `/dev/shm` will incur memory usage of the container. With insufficient container resources this may lead to out-of-memory conditions and crash your container.

## Next steps

- [Scale instances: Easily increase or decrease the amount of instances to run depending on demand for your service.](/v1/application/scale/scale-instances)
- [Increase storage: Increase the persistent storage available for your replicas.](/v1/application/scale/increase-storage)
- [Enable autoscaling: Increase availability and reduce cost by automatically responding to changes in usage of your deployments.](/v1/application/scale/autoscale-deployments)
