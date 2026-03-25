# Source: https://docs.anyscale.com/release-notes/platform/2026/february.md

# Anyscale platform release notes - February 2026

[View Markdown](/release-notes/platform/2026/february.md)

# Anyscale platform release notes - February 2026

Use this page to learn about new features and improvements to the Anyscale platform released in February 2026, including the Anyscale console, CLI, and SDK.

To learn about new features added as part of Ray releases, see [Ray release highlights](https://github.com/ray-project/ray/releases).

To learn about Python and system libraries installed in each Anyscale base image, see [Anyscale base images](/reference/base-images.md).

To view platform release notes from other months, see [All platform release notes](/release-notes.md#all-platform).

## Declarative compute configs for VM-based clouds (beta)[​](#declarative-compute-configs-for-vm-based-clouds-beta "Direct link to Declarative compute configs for VM-based clouds (beta)")

**February 27, 2026**

You can now use declarative compute configs for Anyscale clouds backed by AWS EC2 or GCP GCE. Specify CPU, memory, and GPU requirements with `required_resources` and optional `required_labels` for head and worker nodes; Anyscale selects and provisions VM instance types that match. This feature is in beta release. See [Declarative compute configs](/configuration/compute/declarative.md).

## Anyscale CLI version 0.26.87 released[​](#anyscale-cli-version-02687-released "Direct link to Anyscale CLI version 0.26.87 released")

**February 19, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.87 release notes](/release-notes/cli-sdk.md#0-26-87).

## Anyscale operator for Kubernetes version 1.4.1 released[​](#anyscale-operator-for-kubernetes-version-141-released "Direct link to Anyscale operator for Kubernetes version 1.4.1 released")

**February 19, 2026**

Anyscale has released version 1.4.1 of the Anyscale operator for Kubernetes. For release details, see the [Anyscale operator GitHub page](https://github.com/anyscale/helm-charts/releases/tag/anyscale-operator-1.4.1).

**Changes in 1.4.1:**

* **AWS credential mount:** You can now specify the signature version to use for S3 in the AWS credential mounting utility. This applies to the operator and all workloads.

* **Bug fixes:**

  * Fixes a bug where the operator presented its client ID instead of its principal ID when verifying an Azure cloud with the Anyscale CLI.
  * Fixes a race condition with Kueue integration where the operator would be unable to remove the workload custom resource.

## Ray 2.54.0 released[​](#ray-2540-released "Direct link to Ray 2.54.0 released")

**February 17, 2026**

Ray 2.54.0 has released and is available as an Anyscale base image.

See [Ray 2.54.0 release highlights](https://github.com/ray-project/ray/releases/tag/ray-2.54.0).

For all Python and system dependencies, see [Anyscale base images](/reference/base-images.md).

## Anyscale CLI version 0.26.86 released[​](#anyscale-cli-version-02686-released "Direct link to Anyscale CLI version 0.26.86 released")

**February 17, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.86 release notes](/release-notes/cli-sdk.md#0-26-86).

## Support for Nvidia RTX Pro on AWS G7e instances[​](#support-for-nvidia-rtx-pro-on-aws-g7e-instances "Direct link to Support for Nvidia RTX Pro on AWS G7e instances")

**February 17, 2026**

Anyscale now supports G7e instance types on AWS clouds backed by VMs or EKS. These instances use Nvidia RTX Pro GPUs. See [Compute configuration on Anyscale](/configuration/compute.md) and [pricing details for supported machine types](https://www.anyscale.com/pricing-detail#supported-machine-types).

## Anyscale operator configuration for `SYS_PTRACE`[​](#anyscale-operator-configuration-for-sys_ptrace "Direct link to anyscale-operator-configuration-for-sys_ptrace")

**February 11, 2026**

warning

**Process tracing (potential breaking change):** Starting with Anyscale operator version 1.4.0, `SYS_PTRACE` is enabled by default for all Ray containers for profiling Ray processes and viewing actor flamegraphs and stack traces. If your cluster disallows `SYS_PTRACE`, pod creation will fail and disrupt workloads when autoscaling adds pods. Set `workloads.enableProcessTracing: false` in your Helm values to disable. See [Workload features](/k8s/helm-ref.md#workload-features).

## Anyscale operator for Kubernetes version 1.4.0 released[​](#anyscale-operator-for-kubernetes-version-140-released "Direct link to Anyscale operator for Kubernetes version 1.4.0 released")

**February 11, 2026**

Anyscale has released version 1.4.0 of the Anyscale operator for Kubernetes. For release details, see the [Anyscale operator GitHub page](https://github.com/anyscale/helm-charts/releases/tag/anyscale-operator-1.4.0).

**Changes in 1.4.0:**

* **AWS credential mount:** Specify the S3 addressing style via the AWS credential mount; the setting applies to the operator and all workloads. See [AWS credential mounting](/k8s/helm-ref.md#aws-credential-mounting).
* **Kueue:** Fixes for pods being recreated while waiting in the LocalQueue with multiple regions in the compute config, and for pods stuck in terminating (force-delete requires permissions to delete Kueue Workload CRs).
* **Other:** Workload name label sanitization for invalid label values; fix for service token validation and header-based service version canary with the Gateway API.

## Anyscale CLI version 0.26.85 released[​](#anyscale-cli-version-02685-released "Direct link to Anyscale CLI version 0.26.85 released")

**February 11, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.85 release notes](/release-notes/cli-sdk.md#0-26-85).

## Removal of additional deprecated CLI and SDK commands[​](#removal-of-additional-deprecated-cli-and-sdk-commands "Direct link to Removal of additional deprecated CLI and SDK commands")

**February 11, 2026**

Anyscale CLI version 0.26.85 removes the legacy machine CLI and several legacy SDK methods. See [Methods removed in version 0.26.85](/archive/ref.md#02685) for migration guidance.

## Restrict collaborator permissions on container images[​](#restrict-collaborator-permissions-on-container-images "Direct link to Restrict collaborator permissions on container images")

**February 9, 2026**

Organization owners can now restrict permissions on container images for collaborators. This feature is in beta release and you must request access. Use new roles to prevent users from creating images or to deny deploying clusters with Anyscale base images. See [Container image roles](/administration/organization/permissions.md#container-image).

## Anyscale CLI version 0.26.84 released[​](#anyscale-cli-version-02684-released "Direct link to Anyscale CLI version 0.26.84 released")

**February 6, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.84 release notes](/release-notes/cli-sdk.md#0-26-84).

## New directories excluded from Anyscale working directories[​](#new-directories-excluded-from-anyscale-working-directories "Direct link to New directories excluded from Anyscale working directories")

**February 4, 2026**

Anyscale now excludes the following directories when uploading files in the `working_dir` for Ray workloads: `.git`, `.venv`, `venv`, and `__pycache__`. Set `RAY_OVERRIDE_RUNTIME_ENV_DEFAULT_EXCLUDES=''` to include all directories. This change establishes parity between Anyscale and Ray default behaviors.

## Update cloud default system storage to use enhanced CORS[​](#update-cloud-default-system-storage-to-use-enhanced-cors "Direct link to Update cloud default system storage to use enhanced CORS")

**February 4, 2026**

Anyscale has released a new CLI command to update the default system storage container configured for an Anyscale cloud to enhance CORS support. Anyscale uses these settings for an optimized file viewer experience. New clouds deployed with `anyscale cloud setup` use this setting by default. See [Update CORS settings for default system storage](/storage/configure.md#update-cors).

## Anyscale CLI version 0.26.83 released[​](#anyscale-cli-version-02683-released "Direct link to Anyscale CLI version 0.26.83 released")

**February 4, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.83 release notes](/release-notes/cli-sdk.md#0-26-83).

## Removal of deprecated CLI and SDK commands[​](#removal-of-deprecated-cli-and-sdk-commands "Direct link to Removal of deprecated CLI and SDK commands")

**February 4, 2026**

Anyscale CLI version 0.26.83 removes support for a number of legacy commands. See [Methods removed in version 0.26.83](/archive/ref.md#02683).

## Deprecated support for concurrency job runs with job queues[​](#deprecated-support-for-concurrency-job-runs-with-job-queues "Direct link to Deprecated support for concurrency job runs with job queues")

**February 3, 2026**

Anyscale has deprecated support for setting `max_concurrency` greater than one for job queues and has turned off this setting by default in clouds not using this feature. See [Concurrent jobs in job queues](/jobs/queues.md#concurrency).

## New user and IAM management experience in the Anyscale console[​](#new-user-and-iam-management-experience-in-the-anyscale-console "Direct link to New user and IAM management experience in the Anyscale console")

**February 2, 2026**

Organization owners can now use a unified UI to manage users and permissions in the Anyscale console. Click on your user icon and select **Users & IAM**. See [Roles and permissions](/administration/organization/permissions.md).
