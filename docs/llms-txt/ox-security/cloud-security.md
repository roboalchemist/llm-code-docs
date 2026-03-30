# Source: https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security.md

# Cloud Security

OX cloud security integrations link your cloud and Kubernetes environments directly to OX so you can see what is running, where it is deployed, and how security findings relate to real workloads.

By connecting [GCP](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/gcp-and-gke), [GKE](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/gcp-and-gke), [AWS](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/aws), [Azure](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/azure-cloud), and [Amazon EKS](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/eks), OX pulls cloud and runtime context into the platform. This context lets you:

* Map applications, repositories, and images to the cloud resources and clusters where they run.
* Enrich issues with deployment and runtime metadata to support prioritization.
* Filter and act on findings based on whether code, images, or workloads are actively running in your environment.

These connectors work alongside your source control and pipeline integrations. Together, they give you a full view from code and build, through deployment, to runtime in the cloud.

When you connect GKE or Amazon EKS, OX also adds [Kubernetes reachability](https://docs.ox.security/ox-integrations/3rd-party-integrations/cloud-security/kubernetes-reachability) context. This shows whether a vulnerable workload or service is exposed to cluster or external traffic, helping you prioritize findings based on real access paths rather than configuration alone.

## Supported connectors
