# Source: https://docs.wandb.ai/models/artifacts/data-privacy-and-compliance.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

> Learn where W&B files are stored by default. Explore how to save, store sensitive information.

# Artifact data privacy and compliance

Files are uploaded to a Google Cloud bucket managed by W\&B when you log artifacts. The contents of the bucket are encrypted both at rest and in transit. Artifact files are only visible to users who have access to the corresponding project.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wKCrMJZKG3PxyJhv/images/artifacts/data_and_privacy_compliance_1.png?fit=max&auto=format&n=wKCrMJZKG3PxyJhv&q=85&s=645ee6add31efa23f483ec5566ba2de4" alt="GCS W&B Client Server diagram" width="960" height="720" data-path="images/artifacts/data_and_privacy_compliance_1.png" />
</Frame>

When you delete a version of an artifact, it is marked for soft deletion in our database and removed from your storage cost. When you delete an entire artifact, it is queued for permanent deletion and all of its contents are removed from the W\&B bucket. If you have specific needs around file deletion, reach out to [Customer Support](mailto:support@wandb.com).

By default, deleted artifacts are retained for 7 days and can be restored during this period, which is configurable for Dedicated Cloud. Learn more about data retention in [Multi-tenant Cloud](/platform/hosting/hosting-options/multi_tenant_cloud#data-retention-policy) or [Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud#data-retention-policy).

For sensitive datasets that cannot reside in a multi-tenant environment, you can use [W\&B Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) or [reference artifacts](/models/artifacts/track-external-files). Reference artifacts track references to private buckets without sending file contents to W\&B. Reference artifacts maintain links to files on your buckets or servers. W\&B only keeps track of the metadata associated with the files, not the files themselves.

<Frame>
  <img src="https://mintcdn.com/wb-21fd5541/wKCrMJZKG3PxyJhv/images/artifacts/data_and_privacy_compliance_2.png?fit=max&auto=format&n=wKCrMJZKG3PxyJhv&q=85&s=7274fd5854c3e17fee9a08bc86d07cd9" alt="W&B Client Server Cloud diagram" width="960" height="720" data-path="images/artifacts/data_and_privacy_compliance_2.png" />
</Frame>

For more information about deployment options, see [Dedicated Cloud](/platform/hosting/hosting-options/dedicated-cloud) or [Self-Managed](/platform/hosting/hosting-options/self-managed). To discuss your specific requirements, contact [contact@wandb.com](mailto:contact@wandb.com).
