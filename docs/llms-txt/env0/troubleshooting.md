# Source: https://docs.envzero.com/guides/admin-guide/self-hosted-kubernetes-agent/troubleshooting.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Troubleshoot common issues with the env zero self-hosted Kubernetes agent, including SIGABRT errors

# Deploy failed with signal SIGABRT

If your deployment failed with this error message it means the pod got `SIGABRT` signal from the k8s cluster it runs on - It usually indicates a crash due to memory limitation.

In this case, we suggest defining `requests` and `limits` for the pod size as described in [Custom/Optional Configuration](/guides/admin-guide/self-hosted-kubernetes-agent/#customoptional-configuration).

Built with [Mintlify](https://mintlify.com).
