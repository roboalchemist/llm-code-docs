# Source: https://docs.cortexlabs.com/start.md

# Source: https://docs.cortexlabs.com/0.41/start.md

# Get started

## Create a cluster on your AWS account

```bash
# install the CLI
bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/v0.41.0/get-cli.sh)"

# create a cluster
cortex cluster up cluster.yaml
```

* [Client installation](https://docs.cortexlabs.com/0.41/clients/install) - customize your client installation.
* [Cluster configuration](https://docs.cortexlabs.com/0.41/clusters/management/create) - optimize your cluster for your workloads.
* [Environments](https://docs.cortexlabs.com/0.41/clusters/management/environments) - manage multiple clusters.

## Build scalable APIs

```bash
# deploy APIs
cortex deploy apis.yaml
```

* [Realtime](https://docs.cortexlabs.com/0.41/workloads/realtime/example) - create APIs that respond to requests in real-time.
* [Async](https://docs.cortexlabs.com/0.41/workloads/async/example) - create APIs that respond to requests asynchronously.
* [Batch](https://docs.cortexlabs.com/0.41/workloads/batch/example) - create APIs that run distributed batch jobs.
* [Task](https://docs.cortexlabs.com/0.41/workloads/task/example) - create APIs that run jobs on-demand.
