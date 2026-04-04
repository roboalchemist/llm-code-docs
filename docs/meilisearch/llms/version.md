# Version
Source: https://www.meilisearch.com/docs/reference/api/version

The /version route allows you to check the version of a running Meilisearch instance.

The `/version` route allows you to check the version of a running Meilisearch instance.

## Version object

| Name             | Description                                            |
| :--------------- | :----------------------------------------------------- |
| **`commitSha`**  | Commit identifier that tagged the `pkgVersion` release |
| **`commitDate`** | Date when the `commitSha` was created                  |
| **`pkgVersion`** | Meilisearch version                                    |

## Get version of Meilisearch

<RouteHighlighter method="GET" />

Get version of Meilisearch.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/version'
  ```

  ```javascript JS theme={null}
  client.getVersion()
  ```

  ```python Python theme={null}
  client.get_version()
  ```

  ```php PHP theme={null}
  $client->version();
  ```

  ```java Java theme={null}
  client.getVersion();
  ```

  ```ruby Ruby theme={null}
  client.version
  ```

  ```go Go theme={null}
  client.GetVersion()
  ```

  ```csharp C# theme={null}
  await client.GetVersionAsync();
  ```

  ```rust Rust theme={null}
  let version: Version = client
    .get_version()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.version { (result) in
      switch result {
      case .success(let version):
          print(version)
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.getVersion();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "commitSha": "b46889b5f0f2f8b91438a08a358ba8f05fc09fc1",
  "commitDate": "2019-11-15T09:51:54.278247+00:00",
  "pkgVersion": "0.1.1"
}
```