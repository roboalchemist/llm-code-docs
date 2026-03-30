# Multitenancy and tenant tokens
Source: https://www.meilisearch.com/docs/learn/security/generate_tenant_token_sdk

This guide shows you the main steps when creating tenant tokens using Meilisearch's official SDKs.

There are two steps to use tenant tokens with an official SDK: generating the tenant token, and making a search request using that token.

## Requirements

* a working Meilisearch project
* an application supporting authenticated users
* one of Meilisearch's official SDKs installed

## Generate a tenant token with an official SDK

First, import the SDK. Then create a set of [search rules](/learn/security/tenant_token_reference#search-rules):

```json theme={null}
{
  "patient_medical_records": {
    "filter": "user_id = 1"
  }
}
```

Search rules must be an object where each key corresponds to an index in your instance. You may configure any number of filters for each index.

Next, find your default search API key. Query the [get an API key endpoint](/reference/api/keys#get-one-key) and inspect the `uid`  field to obtain your API key's UID:

```sh theme={null}
curl \
  -X GET 'MEILISEARCH_URL/keys/API_KEY' \
  -H 'Authorization: Bearer MASTER_KEY'
```

For maximum security, you should also define an expiry date for tenant tokens.

Finally, send this data to your chosen SDK's tenant token generator:

<CodeGroup>
  ```javascript JS theme={null}
  import { generateTenantToken } from 'meilisearch/token'

  const searchRules = {
    patient_medical_records: {
      filter: 'user_id = 1'
    }
  }
  const apiKey = 'B5KdX2MY2jV6EXfUs6scSfmC...'
  const apiKeyUid = '85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76'
  const expiresAt = new Date('2025-12-20') // optional

  const token = await generateTenantToken({ apiKey, apiKeyUid, searchRules, expiresAt })
  ```

  ```python Python theme={null}
  uid = '85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76';
  api_key = 'B5KdX2MY2jV6EXfUs6scSfmC...'
  expires_at = datetime(2025, 12, 20)
  search_rules = {
    'patient_medical_records': {
      'filter': 'user_id = 1'
    }
  }
  token = client.generate_tenant_token(api_key_uid=uid, search_rules=search_rules, api_key=api_key, expires_at=expires_at)
  ```

  ```php PHP theme={null}
  $apiKeyUid = '85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76';
  $searchRules = (object) [
    'patient_medical_records' => (object) [
      'filter' => 'user_id = 1',
    ]
  ];
  $options = [
      'apiKey' => 'B5KdX2MY2jV6EXfUs6scSfmC...',
      'expiresAt' => new DateTime('2025-12-20'),
  ];

  $token = $client->generateTenantToken($apiKeyUid, $searchRules, $options);
  ```

  ```java Java theme={null}
  Map<String, Object> filters = new HashMap<String, Object>();
  filters.put("filter", "user_id = 1");
  Map<String, Object> searchRules = new HashMap<String, Object>();
  searchRules.put("patient_medical_records", filters);

  Date expiresAt = new SimpleDateFormat("yyyy-MM-dd").parse("2025-12-20");
  TimeZone.setDefault(TimeZone.getTimeZone("UTC"));
  TenantTokenOptions options = new TenantTokenOptions();
  options.setApiKey("B5KdX2MY2jV6EXfUs6scSfmC...");
  options.setExpiresAt(expiresAt);

  String token = client.generateTenantToken("85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76", searchRules, options);
  ```

  ```ruby Ruby theme={null}
  uid = '85c3c2f9-bdd6-41f1-abd8-11fcf80e0f76'
  api_key = 'B5KdX2MY2jV6EXfUs6scSfmC...'
  expires_at = Time.new(2025, 12, 20).utc
  search_rules = {
    'patient_medical_records' => {
      'filter' => 'user_id = 1'
    }
  }

  token = client.generate_tenant_token(uid, search_rules, api_key: api_key, expires_at: expires_at)
  ```

  ```go Go theme={null}
  searchRules := map[string]interface{}{
    "patient_medical_records": map[string]string{
      "filter": "user_id = 1",
    },
  }
  options := &meilisearch.TenantTokenOptions{
    APIKey: "B5KdX2MY2jV6EXfUs6scSfmC...",
    ExpiresAt: time.Date(2025, time.December, 20, 0, 0, 0, 0, time.UTC),
  }

  token, err := client.GenerateTenantToken(searchRules, options);
  ```

  ```csharp C# theme={null}
  var apiKey = "B5KdX2MY2jV6EXfUs6scSfmC...";
  var expiresAt = new DateTime(2025, 12, 20);
  var searchRules = new TenantTokenRules(new Dictionary<string, object> {
    { "patient_medical_records", new Dictionary<string, object> { { "filter", "user_id = 1" } } }
  });

  token = client.GenerateTenantToken(
    searchRules,
    apiKey: apiKey // optional,
    expiresAt: expiresAt // optional
  );
  ```

  ```rust Rust theme={null}
  let api_key = "B5KdX2MY2jV6EXfUs6scSfmC...";
  let api_key_uid = "6062abda-a5aa-4414-ac91-ecd7944c0f8d";
  let expires_at = time::macros::datetime!(2025 - 12 - 20 00:00:00 UTC);
  let search_rules = json!({ "patient_medical_records": { "filter": "user_id = 1" } });

  let token = client
    .generate_tenant_token(api_key_uid, search_rules, api_key, expires_at)
    .unwrap();
  ```
</CodeGroup>

The SDK will return a valid tenant token.

## Make a search request using a tenant token

After creating a token, you must send it your application's front end. Exactly how to do that depends on your specific setup.

Once the tenant token is available, use it to authenticate search requests as if it were an API key:

<CodeGroup>
  ```javascript JS theme={null}
  const frontEndClient = new MeiliSearch({ host: 'http://localhost:7700', apiKey: token })
  frontEndClient.index('patient_medical_records').search('blood test')
  ```

  ```python Python theme={null}
  front_end_client = Client('http://localhost:7700', token)
  front_end_client.index('patient_medical_records').search('blood test')
  ```

  ```php PHP theme={null}
  $frontEndClient = new Client('http://localhost:7700', $token);
  $frontEndClient->index('patient_medical_records')->search('blood test');
  ```

  ```java Java theme={null}
  Client frontEndClient = new Client(new Config("http://localhost:7700", token));
  frontEndClient.index("patient_medical_records").search("blood test");
  ```

  ```ruby Ruby theme={null}
  front_end_client = MeiliSearch::Client.new('http://localhost:7700', token)

  front_end_client.index('patient_medical_records').search('blood test')
  ```

  ```go Go theme={null}
  client := meilisearch.New("http://localhost:7700", meilisearch.WithAPIKey("masterKey"))
  client.Index("patient_medical_records").Search("blood test", &meilisearch.SearchRequest{});
  ```

  ```csharp C# theme={null}
  frontEndClient = new MeilisearchClient("http://localhost:7700", token);
  var searchResult = await frontEndClient.Index("patient_medical_records").SearchAsync<Patient>("blood test");
  ```

  ```rust Rust theme={null}
  let front_end_client = Client::new("http://localhost:7700", Some(token));
  let results: SearchResults<Patient> = front_end_client
    .index("patient_medical_records")
    .search()
    .with_query("blood test")
    .execute()
    .await
    .unwrap();
  ```
</CodeGroup>

Applications may use tenant tokens and API keys interchangeably when searching. For example, the same application might use a default search API key for queries on public indexes and a tenant token for logged-in users searching on private data.