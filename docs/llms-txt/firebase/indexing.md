# Source: https://firebase.google.com/docs/firestore/query-data/indexing.md.txt

# Source: https://firebase.google.com/docs/firestore/enterprise/indexing.md.txt

<br />

<br />

|--------------------------------------------------------|
| *Relevant to Cloud Firestore Enterprise edition only.* |

<br />

This page describes how to manage your indexes. To learn more about indexes, see[Indexes overview](https://firebase.google.com/docs/firestore/enterprise/index-overview).

## Before you begin

Before you can create an index in Cloud Firestore with MongoDB compatibility, make sure that you are assigned any of the following roles:

- `roles/datastore.owner`
- `roles/datastore.indexAdmin`
- `roles/editor`
- `roles/owner`

To grant a role, see[Grant a single role](https://cloud.google.com/iam/docs/granting-changing-revoking-access#single-role). For more information aboutCloud Firestoreroles and associated permissions, see[Predefined roles](https://firebase.google.com/docs/firestore/enterprise/security/iam).

If you have defined custom roles, assign all of the following permissions to create indexes:

- `datastore.indexes.create`
- `datastore.indexes.delete`
- `datastore.indexes.get`
- `datastore.indexes.list`
- `datastore.indexes.update`

## Create an index

To create an index, complete the following steps:  

##### MongoDB API

Use the[`createIndex()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.createIndex/)method to create an index. For example:

-

  ```bash
    db.restaurants.createIndex({"cuisine" : 1})
    
  ```
-

  ```bash
    db.restaurants.createIndex({"cuisine" : 1}, {sparse: true})
    
  ```
- Index creation with`db.runCommand()`is also supported with at most one index.

  ```bash
    db.runCommand({"createIndexes":"restaurant", "index": [{"key": {"cuisine":1}, {"name": "cuisine_index"}]})
    
  ```

Note the following limitations:

- You can create only one index per request.`db.`<var class="readonly" translate="no">collection</var>`.createIndexes()`is not supported.
- [Audit logs](https://firebase.google.com/docs/firestore/enterprise/audit-logging)for index creation with the MongoDB API use the method name`google.firestore.admin.v1.FirestoreAdmin.CreateIndex`.
- For supported index options, see[indexes and index properties](https://firebase.google.com/docs/firestore/enterprise/supported-features-80#indexes_and_index_properties).

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Select a database from the list of databases.
3. In the**Indexes** tab, click**Create Index**.
4. Enter a**Collection ID**.
5. Add one or more field paths and select an index option for each.
6. Select a field presence option, either non-sparse or sparse.
7. Optionally, you can set the[multikey index](https://firebase.google.com/docs/firestore/enterprise/index-overview#multikey)option.
8. Click**Create**.
9. Your new index is displayed in the list of indexes and Cloud Firestore with MongoDB compatibility begins creating your index. When your index is created, you will see a green check mark next to the index. If index is not created, see[Index building errors](https://firebase.google.com/docs/firestore/enterprise/index-overview#index-building-errors)for possible causes.

##### gcloud CLI

To create an index, use the[`gcloud firestore indexes composite create`](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create)command. Set`api-scope`to`mongodb-compatible-api`.  

```scdoc
gcloud firestore indexes composite create \
--database='DATABASE_ID' \
--collection-group=COLLECTION \
--field-config=FIELD_CONFIGURATION \
--query-scope=collection-group \
--density=dense \
--api-scope=mongodb-compatible-api
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: a database ID.
- <var translate="no">COLLECTION</var>: a collection name.
- <var translate="no">FIELD_CONFIGURATION</var>: a field configuration. For each field, add`--field-config=field-path=`. For example:  

  ```text
      --field-config=field-path=user-id,order=descending \
      --field-config=field-path=score,order=descending
      
  ```

  For more information about configuring these fields, see[`--field-config`](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/create#--field-config).

To create a sparse index, set`--density=sparse-any`.

To create a multikey index, add the`--multikey`flag.

To create a unique index, add the`--unique`flag.

##### Terraform

Use the[`google_firestore_index`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/firestore_index)resource and set`api_scope`to`MONGODB_COMPATIBLE_API`and`query_scope`to`COLLECTION_GROUP`.  

```terraform
resource "google_firestore_index" "index" {
  database    = "<var translate="no">DATABASE_ID</var>"
  collection  = "<var translate="no">COLLECTION</var>"
  api_scope   = "MONGODB_COMPATIBLE_API"
  query_scope = "COLLECTION_GROUP"

  // You can include multiple field blocks
  fields {
    field_path = "<var translate="no">FIELD_PATH</var>"
    order      = "<var translate="no">ORDER</var>"
  }

  // Optional
  multikey = true
  density  = "<var translate="no">DENSITY</var>"
}
```

Replace the following:

- <var translate="no">DATABASE_ID</var>: The database ID for your chosen database
- <var translate="no">COLLECTION</var>: The name of the collection to index
- <var translate="no">FIELD_PATH</var>: The name of the field to index
- <var translate="no">ORDER</var>: One of`ASCENDING`or`DESCENDING`
- <var translate="no">DENSITY</var>: One of`SPARSE_ANY`or`DENSE`

## Delete an index

To delete an index, complete the following steps:  

##### MongoDB API

Use the[`dropIndex()`](https://www.mongodb.com/docs/manual/reference/method/db.collection.dropIndex/)method to delete an index. For example:

**Delete an index using index name**  

```bash
db.restaurants.dropIndex("cuisine_index")
```

**Delete an index using index definition**  

```bash
db.restaurants.dropIndex({"cuisine" : 1})
```

##### Firebaseconsole

1. In theFirebaseconsole, go to the**Firestore Database**page.

   [Go to Firestore Database](https://console.firebase.google.com/project/_/firestore/databases/-default-/data/)
2. Select a database from the list of databases.
3. Click the**Indexes**tab.
4. In the list of indexes, choose**Delete** from the**More** buttonmore_vertfor the index you want to delete.
5. Click**Delete Index**.

##### gcloud CLI

1. To find the name of the index, use the[`gcloud firestore indexes composite list`](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/list)command.

   ```scdoc
   gcloud firestore indexes composite list \
   --database='DATABASE_ID'
   ```

   Replace<var translate="no">DATABASE_ID</var>with the database ID.
2. To delete the index, use the[`gcloud firestore indexes composite delete`](https://cloud.google.com/sdk/gcloud/reference/firestore/indexes/composite/delete)command.

   ```scdoc
   gcloud firestore indexes composite delete INDEX_NAME \
   --database='DATABASE_ID'
   ```

   Replace the following:
   - <var translate="no">INDEX_NAME</var>: the name of an index
   - <var translate="no">DATABASE_ID</var>: a database ID

## Index build time

To build an index, Cloud Firestore with MongoDB compatibility must create the index and then backfill the index entries with existing data. The time required to create an index is determined by the following:

- The minimum build time for an index is a few minutes, even for an empty database.

- The time required to backfill index entries depends on how much existing data belongs in the new index. The more field values that match the index definition, the longer it takes to backfill the index entries.

### Manage long-running operations

Index builds are*long-running operations*. The following sections describe how to work with long-running operations for indexes.
| **Key Term:** Cloud Firestore with MongoDB compatibility supports several administrative operations that can take a long time to complete. These operations are called***long-running operations***. Cloud Firestore with MongoDB compatibility includes features to execute and manage long- running operations. Supported long-running operations include index builds and export operations.

After you start to create an index, Cloud Firestore with MongoDB compatibility assigns the operation a unique name. Operation names are prefixed with`projects/`<var translate="no">PROJECT_ID</var>`/databases/`<var translate="no">DATABASE_ID</var>`/operations/`, for example:  

```
projects/PROJECT_ID/databases/DATABASE_ID/operations/ASA1MTAwNDQxNAgadGx1YWZlZAcSeWx0aGdpbi1zYm9qLW5pbWRhEgopEg
```

You can omit the prefix when specifying an operation name for the`describe`command.

### List all long-running operations

To list long-running operations, use the[`gcloud firestore operations list`](https://cloud.google.com/sdk/gcloud/reference/firestore/operations/list)command. This command lists ongoing and recently completed operations. Operations are listed for a few days after completion:  

```
gcloud firestore operations list
```

### Check operation status

Instead of listing all long-running operations, you can list the details of a single operation:

<br />

```
gcloud firestore operations describe operation-name
```

<br />

### Estimating the completion time

As your operation runs, see the value of the[`state`field](https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.admin.v1#state)for the overall status of the operation.

A request for the status of a long-running operation also returns the metrics`workEstimated`and`workCompleted`.`workEstimated`shows the estimated total number of documents an operation will process.`workCompleted`shows the number of documents processed so far. After the operation completes,`workCompleted`reflects the total number of documents that were actually processed, which might be different than the value of`workEstimated`.

To estimate an operation's progress, divide`workCompleted`by`workEstimated`.
| **Note:** The estimate might be inaccurate because it depends on delayed statistics collection.

The following is an example of the progress of creating an index:  

```
{
  "operations": [
    {
      "name": "projects/project-id/operations/AyAyMDBiM2U5NTgwZDAtZGIyYi0zYjc0LTIzYWEtZjg1ZGdWFmZWQHEjF0c2Flc3UtcmV4ZWRuaS1uaW1kYRUKSBI",
      "metadata": {
        "@type": "type.googleapis.com/google.firestore.admin.v1.IndexOperationMetadata",
        "common": {
          "operationType": "CREATE_INDEX",
          "startTime": "2020-06-23T16:52:25.697539Z",
          "state": "PROCESSING"
        },
        "progressDocuments": {
          "workCompleted": "219327",
          "workEstimated": "2198182"
        }
       },
    },
    ...
```

When an operation completes, the operation description will contain[`"done": true`](https://cloud.google.com/firestore/docs/reference/rpc/google.longrunning#operation). See the value of the[`state`field](https://cloud.google.com/firestore/docs/reference/rpc/google.firestore.admin.v1#state)for the result of the operation. If the`done`field is not set in the response, then the operation has not completed.