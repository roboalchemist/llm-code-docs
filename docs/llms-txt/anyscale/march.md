# Source: https://docs.anyscale.com/release-notes/platform/2026/march.md

# Anyscale platform release notes - March 2026

[View Markdown](/release-notes/platform/2026/march.md)

# Anyscale platform release notes - March 2026

Use this page to learn about new features and improvements to the Anyscale platform released in March 2026, including the Anyscale console, CLI, and SDK.

To learn about new features added as part of Ray releases, see [Ray release highlights](https://github.com/ray-project/ray/releases).

To learn about Python and system libraries installed in each Anyscale base image, see [Anyscale base images](/reference/base-images.md).

To view platform release notes from other months, see [All platform release notes](/release-notes.md#all-platform).

## Anyscale CLI version 0.26.90 released[​](#anyscale-cli-version-02690-released "Direct link to Anyscale CLI version 0.26.90 released")

**March 9, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.90 release notes](/release-notes/cli-sdk.md#0-26-90).

## Update Anyscale clouds backed by Google Cloud VMs[​](#update-anyscale-clouds-backed-by-google-cloud-vms "Direct link to Update Anyscale clouds backed by Google Cloud VMs")

**March 9, 2026**

Anyscale clouds deployed on Google Cloud VMs using `anyscale cloud setup` or `anyscale cloud resource setup` might have a dependency on Google Deployment Manager, which will retire on June 30, 2026. Update your cloud today to ensure Anyscale can clean up resources in your Google Cloud account. See [Update Anyscale clouds deployed with Deployment Manager](/admin/cloud/configure-google-cloud.md#deployment-manager).

## Anyscale CLI version 0.26.89 released[​](#anyscale-cli-version-02689-released "Direct link to Anyscale CLI version 0.26.89 released")

**March 4, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.89 release notes](/release-notes/cli-sdk.md#0-26-89).

## Deprecation of legacy GPU instances[​](#deprecation-of-legacy-gpu-instances "Direct link to Deprecation of legacy GPU instances")

**March 2, 2026**

Anyscale has adopted Linux open GPU kernel modules for VM images, which don't support the following accelerator types: `K80`, `M60`, `V100 16GB`, and `V100 32GB`. Instances types using these GPUs are now deprecated for Anyscale clouds on the VM stack. For AWS, the `g3s`, `g3`, `p3`, and `p3dn` families are deprecated. For Google Cloud, instance types in the `n1` family that use `nvidia-k80` or `nvidia-v100` are deprecated.

## Anyscale CLI version 0.26.88 released[​](#anyscale-cli-version-02688-released "Direct link to Anyscale CLI version 0.26.88 released")

**March 2, 2026**

A new version of the Anyscale CLI and SDK is now available. See [Version 0.26.88 release notes](/release-notes/cli-sdk.md#0-26-88).

## Removal of deprecated SDK methods[​](#removal-of-deprecated-sdk-methods "Direct link to Removal of deprecated SDK methods")

**March 2, 2026**

Anyscale CLI version 0.26.88 removes support for legacy job, schedule, cluster, and image SDK methods on `AnyscaleSDK`. Use the modern `anyscale.job.*`, `anyscale.schedule.*`, workspace, and API client alternatives. See [Methods removed in version 0.26.88](/archive/ref.md#02688) for migration guidance.

## Declarative compute configs for VM-based clouds (beta)[​](#declarative-compute-configs-for-vm-based-clouds-beta "Direct link to Declarative compute configs for VM-based clouds (beta)")

**March 2, 2026**

You can now use declarative compute configs for Anyscale clouds backed by AWS EC2 or GCP GCE. Specify CPU, memory, and GPU requirements with `required_resources` and optional `required_labels` for head and worker nodes; Anyscale selects and provisions VM instance types that match. This feature is in beta release. See [Declarative compute configs](/configuration/compute/declarative.md).
