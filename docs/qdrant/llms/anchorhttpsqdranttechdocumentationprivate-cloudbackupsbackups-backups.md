# [Anchor](https://qdrant.tech/documentation/private-cloud/backups/\#backups) Backups

To create a one-time backup, create a `QdrantClusterSnapshot` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterSnapshot
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  retention: 1h

```

You can also create a recurring backup with the `QdrantClusterScheduledSnapshot` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterScheduledSnapshot
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  scheduleShortId: a7d8d973
  cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
  # every hour
  schedule: "0 * * * *"
  retention: 1h

```

To resture from a backup, create a `QdrantClusterRestore` resource:

```yaml
apiVersion: qdrant.io/v1
kind: QdrantClusterRestore
metadata:
  name: "qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-restore-01"
  labels:
    cluster-id: "a7d8d973-0cc5-42de-8d7b-c29d14d24840"
    customer-id: "acme-industries"
spec:
  source:
    snapshotName: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840-snapshot-timestamp
    namespace: qdrant-private-cloud
  destination:
    name: qdrant-a7d8d973-0cc5-42de-8d7b-c29d14d24840
    namespace: qdrant-private-cloud

```

Note that with all resources `cluster-id` and `customer-id` label must be set to the values of the corresponding `QdrantCluster` resource.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/backups.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/private-cloud/backups.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-2-lllmstxt|>
## benchmark-faq