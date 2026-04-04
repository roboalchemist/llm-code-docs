# Configuring index settings with the Meilisearch API
Source: https://www.meilisearch.com/docs/learn/configuration/configuring_index_settings_api

This tutorial shows how to check and change an index setting using the Meilisearch API.

This tutorial shows how to check and change an index setting using one of the setting subroutes of the Meilisearch API.

If you are Meilisearch Cloud user, you may also [configure index settings using the Meilisearch Cloud interface](/learn/configuration/configuring_index_settings).

## Requirements

* a new [Meilisearch Cloud](https://cloud.meilisearch.com/projects/) project or a self-hosted Meilisearch instance with at least one index
* a command-line terminal with `curl` installed

## Getting the value of a single index setting

Start by checking the value of the searchable attributes index setting.

Use the `GET` endpoint of the `/settings/searchable-attributes` subroute, replacing `INDEX_NAME` with your index:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes'
  ```

  ```rust Rust theme={null}
  let searchable_attributes: Vec<String> = index
    .get_searchable_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

Depending on your setup, you might also need to replace `localhost:7700` with the appropriate address and port.

You should receive a response immediately:

```json theme={null}
[
  "*"
]
```

If this is a new index, you should see the default value, \["\*"]. This indicates Meilisearch looks through all document attributes when searching.

## Updating an index setting

All documents include a primary key attribute. In most cases, this attribute does not contain any relevant data, so you can improve your application search experience by explicitly removing it from your searchable attributes list.

Use the `PUT` endpoint of the `/settings/searchable-attributes` subroute, replacing `INDEX_NAME` with your index and the sample attributes `"title"` and `"overview"` with attributes present in your dataset:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PUT 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes' \
    -H 'Content-Type: application/json' \
    --data-binary '[
      "title",
      "overview"
    ]'
  ```

  ```rust Rust theme={null}
  let task = index
    .set_searchable_attributes(["title", "overview"])
    .await
    .unwrap();
  ```
</CodeGroup>

This time, Meilisearch will not process your request immediately. Instead, you will receive a summarized task object while the search engine works on updating your index setting as soon as it has enough resources:

```json theme={null}
{
  "taskUid": 1,
  "indexUid": "INDEX_NAME",
  "status": "enqueued",
  "type": "settingsUpdate",
  "enqueuedAt": "2021-08-11T09:25:53.000000Z"
}
```

Processing the index setting change might take some time, depending on how many documents you have in your index. Wait a few seconds and use the task object's `taskUid` to monitor the status of your request:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/tasks/TASK_UID'
  ```

  ```rust Rust theme={null}
  let task_status = index.get_task(&task).await.unwrap();
  ```
</CodeGroup>

Meilisearch will respond with a task object:

```json theme={null}
{
  "uid": 1,
  "indexUid": "INDEX_NAME",
  "status": "succeeded",
  "type": "settingsUpdate",
  …
}
```

If `status` is `enqueued` or `processed`, wait a few more moments and check the task status again. If `status` is `failed`, make sure you have used a valid index and attributes, then try again.

If task `status` is `succeeded`, you successfully updated your index's searchable attributes. Use the subroute to check the new setting's value:

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/indexes/INDEX_NAME/settings/searchable-attributes'
  ```

  ```rust Rust theme={null}
  let searchable_attributes: Vec<String> = index
    .get_searchable_attributes()
    .await
    .unwrap();
  ```
</CodeGroup>

Meilisearch should return an array with the new values:

```json theme={null}
[
  "title",
  "overview"
]
```

## Conclusion

You have used the Meilisearch API to check the value of an index setting. This revealed an opportunity to improve your project's performance, so you updated this index setting to make your application better and more responsive.

This tutorial used the searchable attributes setting, but the procedure is the same no matter which index setting you are editing.

For a comprehensive reference of all index settings, consult the [settings API reference](/reference/api/settings).