# Source: https://docs.baseten.co/observability/security.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.baseten.co/llms.txt
> Use this file to discover all available pages before exploring further.

# Secure model inference

> Keeping your models safe and private

Baseten maintains [SOC 2 Type II certification](https://www.baseten.co/blog/soc-2-type-2) and [HIPAA compliance](https://www.baseten.co/blog/baseten-announces-hipaa-compliance), with robust security measures beyond compliance.

## Data privacy

Baseten does not store model inputs, outputs, or weights by default.

* **Model inputs/outputs**: Inputs for [async inference](/inference/async) are temporarily stored until processed. Outputs are never stored.
* **Model weights**: Loaded dynamically from sources like Hugging Face, GCS, or S3, moving directly to GPU memory.
  * Users can enable caching via Truss. Cached weights can be permanently deleted on request.
* **Postgres data tables**: Existing users may store data in Baseten’s hosted Postgres tables, which can be deleted anytime.

Baseten’s network accelerator optimizes model downloads. [Contact support](mailto:support@baseten.co) to disable it.

## Workload security

Inference workloads are isolated to protect users and Baseten’s infrastructure.

* **Container security**:
  * No GPUs are shared across users.
  * Security tooling: Falco (Sysdig), Gatekeeper (Pod Security Policies).
  * Minimal privileges for workloads and nodes to limit incident impact.
* **Network security**:
  * Each customer has a dedicated Kubernetes namespace.
  * Isolation enforced via [Calico](https://docs.tigera.io/calico/latest/about).
  * Nodes run in a private subnet with firewall protections.
* **Pentesting**:
  * Extended pentesting by [RunSybil](https://www.runsybil.com/) (ex-OpenAI and CrowdStrike experts).
  * Malicious model deployments tested in a dedicated prod-like environment.

## Self-hosted model inference

Baseten offers single-tenant environments and self-hosted deployments. The cloud version is recommended for ease of setup, cost efficiency, and elastic GPU access.

For self-hosting, [contact support](mailto:support@baseten.co).
