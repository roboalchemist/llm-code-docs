# Network
Source: https://www.meilisearch.com/docs/reference/api/network

Use the `/network` route to create a network of Meilisearch instances.

Use the `/network` route to create a network of Meilisearch instances. This is particularly useful when used together with federated search to implement horizontal database partition strategies such as sharding.

<Note>
  This is an experimental feature. Use the Meilisearch Cloud UI or the experimental features endpoint to activate it:

  ```sh theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/experimental-features/' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "network": true
    }'
  ```
</Note>

<Warning>
  If an attribute is both:

  * not on the `displayedAttributes` list
  * present on the `sortableAttributes`

  It is possible its value becomes publicly accessible via the `/network` endpoint.

  Do not enable the `network` feature if you rely on the value of attributes not present in `displayedAttributes` to remain hidden at all times.
</Warning>

## The network object

```json theme={null}
{
  "self": "ms-00",
  "sharding": false,
  "remotes": {
    "ms-00": {
      "url": "http://ms-1235.example.meilisearch.io",
      "searchApiKey": "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas",
      "writeApiKey": "O2OaIHgwGuHNx9duH6kSe1YJ55Bh0dXvLhbr8FQVvr3vRVViBO"
    },
    "ms-01": {
      "url": "http://ms-4242.example.meilisearch.io",
      "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
      "writeApiKey": "bd1ldDoFlfyeoFDe8f3GVNiE8AHX86chmFuzOW7nWYUbPa7ww3"
    }
  }
}
```

### `self`

**Type**: String<br />
**Default value**: `null`<br />
**Description**: A string indicating the name of the current instance

### `sharding`

**Type**: Boolean<br />
**Default value**: `false`<br />
**Description**: A boolean indicating whether sharding should be enabled on the network

### `remotes`

**Type**: Object<br />
**Default value**: `{}`<br />
**Description**: An object containing [remote objects](#the-remote-object). The key of each remote object indicates the name of the remote instance

#### The remote object

```json theme={null}
"ms-00": {
  "url": "http://ms-1235.example.meilisearch.io",
  "searchApiKey": "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas",
  "writeApiKey": "O2OaIHgwGuHNx9duH6kSe1YJ55Bh0dXvLhbr8FQVvr3vRVViBO"
}
```

##### `url`

**Type**: String<br />
**Default value**: `null`<br />
**Description**: URL indicating the address of a Meilisearch instance. This URL does not need to be public, but must be accessible to all instances in the network. Required

##### `searchApiKey`

**Type**: String<br />
**Default value**: `null`<br />
**Description**: An API key with search permissions

##### `writeApiKey`

**Type**: String<br />
**Default value**: `null`<br />
**Description**: An API key with `documents.*` permissions

## Get the network object

<RouteHighlighter method="GET" />

Returns the current value of the instance's network object.

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X GET 'MEILISEARCH_URL/network'
  ```

  ```python Python theme={null}
  client.get_all_networks()
  ```

  ```php PHP theme={null}
  $client->getNetwork();
  ```

  ```go Go theme={null}
  client.GetNetwork();
  ```

  ```rust Rust theme={null}
  let network = client
    .get_network_state()
    .await
    .unwrap();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "self": "ms-00",
  "sharding": false,
  "remotes": {
    "ms-00": {
      "url": "http://ms-1235.example.meilisearch.io",
      "searchApiKey": "Ecd1SDDi4pqdJD6qYLxD3y7VZAEb4d9j6LJgt4d6xas",
      "writeApiKey": "O2OaIHgwGuHNx9duH6kSe1YJ55Bh0dXvLhbr8FQVvr3vRVViBO"
    },
    "ms-01": {
      "url": "http://ms-4242.example.meilisearch.io",
      "searchApiKey": "hrVu-OMcjPGElK7692K7bwriBoGyHXTMvB5NmZkMKqQ",
      "writeApiKey": "bd1ldDoFlfyeoFDe8f3GVNiE8AHX86chmFuzOW7nWYUbPa7ww3"
    }
  }
}
```

## Update the network object

<RouteHighlighter method="PATCH" />

Update the `self` and `remotes` fields of the network object.

Updates to the network object are **partial**. Only provide the fields you intend to update. Fields not present in the payload will remain unchanged.

To reset `self`, `sharding` and `remotes` to their original value, set them to `null`. To remove a single `remote` from your network, set the value of its name to `null`.

### Body

| Name                        | Type    | Default value | Description                                                          |
| :-------------------------- | :------ | :------------ | :------------------------------------------------------------------- |
| **[`self`](#self)**         | String  | `null`        | The name of the current instance                                     |
| **[`sharding`](#sharding)** | Boolean | `false`       | Whether sharding should be enabled on the network                    |
| **[`remotes`](#remotes)**   | String  | `null`        | A list of remote objects describing accessible Meilisearch instances |

### Example

<CodeGroup>
  ```bash cURL theme={null}
  curl \
    -X PATCH 'MEILISEARCH_URL/network' \
    -H 'Content-Type: application/json' \
    --data-binary '{
      "self": "ms-00",
      "remotes": {
        "ms-00": {
          "url": "http://INSTANCE_URL",
          "searchApiKey": "INSTANCE_API_KEY"
        },
        "ms-01": {
          "url": "http://ANOTHER_INSTANCE_URL",
          "searchApiKey": "ANOTHER_INSTANCE_API_KEY"
        }
      }
    }'
  ```

  ```python Python theme={null}
  client.add_or_update_networks({
      "remotes": {
          "http://localhost:7700": {
              "searchApiKey": "masterKey"
          }
      },
      "leader": None
  })
  ```

  ```php PHP theme={null}
  $client->updateNetwork([
    'self' => 'ms-00',
    'leader' => 'ms-00',
    'remotes' => [
      'ms-00' => [
        'url' => 'http://INSTANCE_URL',
        'searchApiKey' => 'INSTANCE_API_KEY',
        'writeApiKey' => 'INSTANCE_WRITE_API_KEY'
      ],
      'ms-01' => [
        'url' => 'http://ANOTHER_INSTANCE_URL',
        'searchApiKey' => 'ANOTHER_INSTANCE_API_KEY',
        'writeApiKey' => 'ANOTHER_INSTANCE_WRITE_API_KEY'
      ]
    ]
  ]);
  ```

  ```go Go theme={null}
  client.UpdateNetwork(&meilisearch.UpdateNetworkRequest{
    Self: meilisearch.String("ms-00"),
    Leader: meilisearch.String("ms-00"),
    Remotes: meilisearch.NewOpt(map[string]meilisearch.Opt[meilisearch.Remote]{
      "ms-00": meilisearch.NewOpt(meilisearch.Remote{
        URL:          meilisearch.String("https://meilisearch.com"),
        SearchAPIKey: meilisearch.String("ReadKey"),
        WriteAPIKey: meilisearch.String("WriteKey"),
      },
    },
  });
  ```

  ```rust Rust theme={null}
  let mut remotes = std::collections::HashMap::new();
  remotes.insert(String::from("ms-01"), Some(meilisearch_sdk::network::RemoteConfig {
    url: "https://ms-01.enterprise.meilisearch.com".to_string(),
    search_api_key: "SEARCH_API_KEY".to_string(),
    write_api_key: Some("WRITE_API_KEY".to_string()),
  }));
  // Remove ms-00 from the topology
  remotes.insert(String::from("ms-00"), None);

  let update = meilisearch_sdk::network::NetworkUpdate {
    leader: Some("ms-01".to_string()),
    remotes: Some(remotes),
    ..meilisearch_sdk::network::NetworkUpdate::default()
  };

  let task: TaskInfo = client
    .update_network_state(&update)
    .await
    .unwrap();
  ```
</CodeGroup>

#### Response: `200 Ok`

```json theme={null}
{
  "self": "ms-00",
  "sharding": true,
  "remotes": {
    "ms-00": {
      "url": "http://INSTANCE_URL",
      "searchApiKey": "INSTANCE_API_KEY",
      "writeApiKey": "INSTANCE_WRITE_API_KEY"
    },
    "ms-01": {
      "url": "http://ANOTHER_INSTANCE_URL",
      "searchApiKey": "ANOTHER_INSTANCE_API_KEY",
      "writeApiKey": "ANOTHER_INSTANCE_WRITE_API_KEY"
    }
  }
}
```