# Source: https://docs.verda.com/welcome-to-verda/release-notes.md

# Release Notes

## March 2026

### Improvements

#### Cross-datacenter volume cloning now available for all customers

<div align="left"><figure><img src="https://2529223994-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FYO2RW7i8v8Hs8UzxSAdO%2Fuploads%2F0ucm3pmybDtObkycIX6P%2Fimage.png?alt=media&#x26;token=7afd77a8-b0b4-4270-97d4-6acca1d4c280" alt="CRoss datacenter cloning dialog" width="314"><figcaption></figcaption></figure></div>

You can now clone your OS and data volumes across datacenters. This makes it easy to replicate your environment in a different location. [Read more about block volume cloning.](https://docs.verda.com/storage/block-volumes/cloning-a-block-volume)

## February 2026

### New Features

#### **Instant GPU Clusters Generally Available**

The Beta label has been removed from clusters, marking their general availability. Users can also now transfer clusters between projects, matching the flexibility that already existed for instances.

### Updates

#### **Spot Eviction Storage Behaviour Controls**

Users can now configure what happens to their attached storage when a spot instance is evicted — for example, whether volumes are retained or released. This gives teams more control over data safety and cost when running interruptible workloads. [See API notes here.](https://api.verda.com/v1/docs#description/2026-02-03-spot-instance-volume-policy)

{% hint style="info" icon="list-radio" %}
2026-03-03 Introduced changes to API\
2026-03-05 Python SDK improved (v1.20.0)
{% endhint %}

#### **SFS Share Settings Improved**

The shared filesystem (SFS storage) share settings modal received a round of UX improvements, and the displayed mount command was updated to reflect the latest syntax — ensuring users copy the correct command when attaching volumes to instances.

## January 2026

### New Releases

#### **Terraform Provider for Verda Infrastructure (GA)**

Users can now manage their entire Verda infrastructure as code (IaC) using the official Terraform provider, enabling reproducible deployments, version-controlled configurations, and seamless integration with existing IaC workflows. For more information, check out the [official documentation](https://docs.verda.com/infrastructure-as-code/terraform) or visit the [GitHub repository](https://github.com/verda-cloud/terraform-provider-verda).

#### **Container Registry (Limited Beta)**

A built-in container registry that lets users store, manage, and deploy container images directly within the platform, eliminating the need for third-party registry services.

#### **Cluster Auto-scaler for Kubernetes (Under review)**

An auto-scaler integration currently under review by the official Kubernetes project that would allow Verda-based clusters to automatically scale node pools up and down based on workload demand, optimizing both performance and cost.

### Enhancements

#### Unified Top-Up Page

Combines One-time top-up, Automatic top-up, and Credit coupon forms into a single, streamlined page, simplifying the payment experience.

#### Transfer Money Between Projects

Users can now move funds between their projects, adding important flexibility to multi-project billing workflows.

**Around \~90 other smaller improvements and bug-fixes across 27 releases to Cloud Platform.**
