# Health
Source: https://www.meilisearch.com/docs/reference/api/health

The /health route allows you to verify the status and availability of a Meilisearch instance.

The `/health` route allows you to verify the status and availability of a Meilisearch instance.

## Get health

<RouteHighlighter method="GET" />

Get health of Meilisearch server.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/health'
  ```

  ```javascript JS theme={null}
  client.health()
  ```

  ```python Python theme={null}
  client.health()
  ```

  ```php PHP theme={null}
  $client->health();
  ```

  ```java Java theme={null}
  client.health();
  ```

  ```ruby Ruby theme={null}
  client.health
  ```

  ```go Go theme={null}
  client.Health()
  ```

  ```csharp C# theme={null}
  await client.HealthAsync();
  ```

  ```rust Rust theme={null}
  // health() return an Err() if the server is not healthy, so this example would panic due to the unwrap
  client
    .health()
    .await
    .unwrap();
  ```

  ```swift Swift theme={null}
  client.health { (result) in
      switch result {
      case .success:
          print("Healthy!")
      case .failure(let error):
          print(error)
      }
  }
  ```

  ```dart Dart theme={null}
  await client.health();
  ```
</CodeGroup>

#### Response: `200 OK`

```json theme={null}
{ "status": "available" }
```