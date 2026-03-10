# Create a directory to store snapshots
os.makedirs("snapshots", exist_ok=True)

local_snapshot_paths = []
for snapshot_url in snapshot_urls:
    snapshot_name = os.path.basename(snapshot_url)
    local_snapshot_path = os.path.join("snapshots", snapshot_name)

    response = requests.get(
        snapshot_url, headers={"api-key": QDRANT_API_KEY}
    )
    with open(local_snapshot_path, "wb") as f:
        response.raise_for_status()
        f.write(response.content)

    local_snapshot_paths.append(local_snapshot_path)

```

Alternatively, you can use the `wget` command:

```bash
wget https://node-0.my-cluster.com:6333/collections/test_collection/snapshots/test_collection-559032209313046-2024-01-03-13-20-11.snapshot \
    --header="api-key: ${QDRANT_API_KEY}" \
    -O node-0-shapshot.snapshot

wget https://node-1.my-cluster.com:6333/collections/test_collection/snapshots/test_collection-559032209313047-2024-01-03-13-20-12.snapshot \
    --header="api-key: ${QDRANT_API_KEY}" \
    -O node-1-shapshot.snapshot

wget https://node-2.my-cluster.com:6333/collections/test_collection/snapshots/test_collection-559032209313048-2024-01-03-13-20-13.snapshot \
    --header="api-key: ${QDRANT_API_KEY}" \
    -O node-2-shapshot.snapshot

```

The snapshots are now stored locally. We can use them to restore the collection to a different Qdrant instance, or treat them as a backup. We will create another collection using the same data on the same cluster.

## [Anchor](https://qdrant.tech/documentation/database-tutorials/create-snapshot/\#restore-from-snapshot) Restore from snapshot

Our brand-new snapshot is ready to be restored. Typically, it is used to move a collection to a different Qdrant instance, but we are going to use it to create a new collection on the same cluster.
It is just going to have a different name, `test_collection_import`. We do not need to create a collection first, as it is going to be created automatically.

Restoring collection is also done separately on each node, but our Python SDK does not support it yet. We are going to use the HTTP API instead,
and send a request to each node using `requests` library.

```python
for node_url, snapshot_path in zip(QDRANT_NODES, local_snapshot_paths):
    snapshot_name = os.path.basename(snapshot_path)
    requests.post(
        f"{node_url}/collections/test_collection_import/snapshots/upload?priority=snapshot",
        headers={
            "api-key": QDRANT_API_KEY,
        },
        files={"snapshot": (snapshot_name, open(snapshot_path, "rb"))},
    )

```

Alternatively, you can use the `curl` command:

```bash
curl -X POST 'https://node-0.my-cluster.com:6333/collections/test_collection_import/snapshots/upload?priority=snapshot' \
    -H 'api-key: ${QDRANT_API_KEY}' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@node-0-shapshot.snapshot'

curl -X POST 'https://node-1.my-cluster.com:6333/collections/test_collection_import/snapshots/upload?priority=snapshot' \
    -H 'api-key: ${QDRANT_API_KEY}' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@node-1-shapshot.snapshot'

curl -X POST 'https://node-2.my-cluster.com:6333/collections/test_collection_import/snapshots/upload?priority=snapshot' \
    -H 'api-key: ${QDRANT_API_KEY}' \
    -H 'Content-Type:multipart/form-data' \
    -F 'snapshot=@node-2-shapshot.snapshot'

```

**Important:** We selected `priority=snapshot` to make sure that the snapshot is preferred over the data stored on the node. You can read mode about the priority in the [documentation](https://qdrant.tech/documentation/concepts/snapshots/#snapshot-priority).

Apart from Snapshots, Qdrant also provides the [Qdrant Migration Tool](https://github.com/qdrant/migration) that supports:

- Migration between Qdrant Cloud instances.
- Migrating vectors from other providers into Qdrant.
- Migrating from Qdrant OSS to Qdrant Cloud.

Follow our [migration guide](https://qdrant.tech/documentation/database-tutorials/migration/) to learn how to effectively use the Qdrant Migration tool.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/create-snapshot.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/database-tutorials/create-snapshot.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-183-lllmstxt|>
## agentic-rag-langgraph
- [Documentation](https://qdrant.tech/documentation/)
- Agentic RAG With LangGraph