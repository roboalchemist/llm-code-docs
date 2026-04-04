# [Anchor](https://qdrant.tech/documentation/guides/security/\#security) Security

Please read this page carefully. Although there are various ways to secure your Qdrant instances, **they are unsecured by default**.
You need to enable security measures before production use. Otherwise, they are completely open to anyone

## [Anchor](https://qdrant.tech/documentation/guides/security/\#authentication) Authentication

_Available as of v1.2.0_

Qdrant supports a simple form of client authentication using a static API key.
This can be used to secure your instance.

To enable API key based authentication in your own Qdrant instance you must
specify a key in the configuration:

```yaml
service:
  # Set an api-key.
  # If set, all requests must include a header with the api-key.
  # example header: `api-key: <API-KEY>`
  #
  # If you enable this you should also enable TLS.
  # (Either above or via an external service like nginx.)
  # Sending an api-key over an unencrypted channel is insecure.
  api_key: your_secret_api_key_here

```

Or alternatively, you can use the environment variable:

```bash
docker run -p 6333:6333 \
    -e QDRANT__SERVICE__API_KEY=your_secret_api_key_here \
    qdrant/qdrant

```

For using API key based authentication in Qdrant Cloud see the cloud
[Authentication](https://qdrant.tech/documentation/cloud/authentication/)
section.

The API key then needs to be present in all REST or gRPC requests to your instance.
All official Qdrant clients for Python, Go, Rust, .NET and Java support the API key parameter.

bashpythontypescriptrustjavacsharpgo

```bash
curl \
  -X GET https://localhost:6333 \
  --header 'api-key: your_secret_api_key_here'

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://localhost:6333",
    api_key="your_secret_api_key_here",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  url: "http://localhost",
  port: 6333,
  apiKey: "your_secret_api_key_here",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<paste-your-api-key-here>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.eu-central.aws.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<paste-your-api-key-here>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<paste-your-api-key-here>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<paste-your-api-key-here>",
	UseTLS: true,
})

```

### [Anchor](https://qdrant.tech/documentation/guides/security/\#read-only-api-key) Read-only API key

_Available as of v1.7.0_

In addition to the regular API key, Qdrant also supports a read-only API key.
This key can be used to access read-only operations on the instance.

```yaml
service:
  read_only_api_key: your_secret_read_only_api_key_here

```

Or with the environment variable:

```bash
export QDRANT__SERVICE__READ_ONLY_API_KEY=your_secret_read_only_api_key_here

```

Both API keys can be used simultaneously.

### [Anchor](https://qdrant.tech/documentation/guides/security/\#granular-access-control-with-jwt) Granular access control with JWT

_Available as of v1.9.0_

For more complex cases, Qdrant supports granular access control with [JSON Web Tokens (JWT)](https://jwt.io/).
This allows you to create tokens which restrict access to data stored in your cluster, and build [Role-based access control (RBAC)](https://en.wikipedia.org/wiki/Role-based_access_control) on top of that.
In this way, you can define permissions for users and restrict access to sensitive endpoints.

To enable JWT-based authentication in your own Qdrant instance you need to specify the `api-key` and enable the `jwt_rbac` feature in the configuration:

```yaml
service:
  api_key: you_secret_api_key_here
  jwt_rbac: true

```

Or with the environment variables:

```bash
export QDRANT__SERVICE__API_KEY=your_secret_api_key_here
export QDRANT__SERVICE__JWT_RBAC=true

```

The `api_key` you set in the configuration will be used to encode and decode the JWTs, so –needless to say– keep it secure. If your `api_key` changes, all existing tokens will be invalid.

To use JWT-based authentication, you need to provide it as a bearer token in the `Authorization` header, or as an key in the `Api-Key` header of your requests.

httppythontypescriptrustjavacsharpgo

```http
Authorization: Bearer <JWT>

// or

Api-Key: <JWT>

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "xyz-example.eu-central.aws.cloud.qdrant.io",
    api_key="<JWT>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  apiKey: "<JWT>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<JWT>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.eu-central.aws.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<JWT>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<JWT>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<JWT>",
	UseTLS: true,
})

```

#### [Anchor](https://qdrant.tech/documentation/guides/security/\#generating-json-web-tokens) Generating JSON Web Tokens

Due to the nature of JWT, anyone who knows the `api_key` can generate tokens by using any of the existing libraries and tools, it is not necessary for them to have access to the Qdrant instance to generate them.

For convenience, we have added a JWT generation tool the Qdrant Web UI under the 🔑 tab, if you’re using the default url, it will be at `http://localhost:6333/dashboard#/jwt`.

- **JWT Header** \- Qdrant uses the `HS256` algorithm to decode the tokens.



```json
{
    "alg": "HS256",
    "typ": "JWT"
}

```

- **JWT Payload** \- You can include any combination of the [parameters available](https://qdrant.tech/documentation/guides/security/#jwt-configuration) in the payload. Keep reading for more info on each one.



```json
{
    "exp": 1640995200, // Expiration time
    "value_exists": ..., // Validate this token by looking for a point with a payload value
    "access": "r", // Define the access level.
}

```


**Signing the token** \- To confirm that the generated token is valid, it needs to be signed with the `api_key` you have set in the configuration.
That would mean, that someone who knows the `api_key` gives the authorization for the new token to be used in the Qdrant instance.
Qdrant can validate the signature, because it knows the `api_key` and can decode the token.

The process of token generation can be done on the client side offline, and doesn’t require any communication with the Qdrant instance.

Here is an example of libraries that can be used to generate JWT tokens:

- Python: [PyJWT](https://pyjwt.readthedocs.io/en/stable/)
- JavaScript: [jsonwebtoken](https://www.npmjs.com/package/jsonwebtoken)
- Rust: [jsonwebtoken](https://crates.io/crates/jsonwebtoken)

#### [Anchor](https://qdrant.tech/documentation/guides/security/\#jwt-configuration) JWT Configuration

These are the available options, or **claims** in the JWT lingo. You can use them in the JWT payload to define its functionality.

- **`exp`** \- The expiration time of the token. This is a Unix timestamp in seconds. The token will be invalid after this time. The check for this claim includes a 30-second leeway to account for clock skew.



```json
{
    "exp": 1640995200, // Expiration time
}

```

- **`value_exists`** \- This is a claim that can be used to validate the token against the data stored in a collection. Structure of this claim is as follows:



```json
{
    "value_exists": {
      "collection": "my_validation_collection",
      "matches": [\
        { "key": "my_key", "value": "value_that_must_exist" }\
      ],
    },
}

```



If this claim is present, Qdrant will check if there is a point in the collection with the specified key-values. If it does, the token is valid.

This claim is especially useful if you want to have an ability to revoke tokens without changing the `api_key`.
Consider a case where you have a collection of users, and you want to revoke access to a specific user.



```json
{
    "value_exists": {
      "collection": "users",
      "matches": [\
        { "key": "user_id", "value": "andrey" },\
        { "key": "role", "value": "manager" }\
      ],
    },
}

```



You can create a token with this claim, and when you want to revoke access, you can change the `role` of the user to something else, and the token will be invalid.

- **`access`** \- This claim defines the [access level](https://qdrant.tech/documentation/guides/security/#table-of-access) of the token. If this claim is present, Qdrant will check if the token has the required access level to perform the operation. If this claim is **not** present, **manage** access is assumed.

It can provide global access with `r` for read-only, or `m` for manage. For example:



```json
{
    "access": "r"
}

```



It can also be specific to one or more collections. The `access` level for each collection is `r` for read-only, or `rw` for read-write, like this:



```json
{
    "access": [\
      {\
        "collection": "my_collection",\
        "access": "rw"\
      }\
    ]
}

```



You can also specify which subset of the collection the user is able to access by specifying a `payload` restriction that the points must have.



```json
{
    "access": [\
      {\
        "collection": "my_collection",\
        "access": "r",\
        "payload": {\
          "user_id": "user_123456"\
        }\
      }\
    ]
}

```



This `payload` claim will be used to implicitly filter the points in the collection. It will be equivalent to appending this filter to each request:



```json
{ "filter": { "must": [{ "key": "user_id", "match": { "value": "user_123456" } }] } }

```


### [Anchor](https://qdrant.tech/documentation/guides/security/\#table-of-access) Table of access

Check out this table to see which actions are allowed or denied based on the access level.

This is also applicable to using api keys instead of tokens. In that case, `api_key` maps to **manage**, while `read_only_api_key` maps to **read-only**.

**Symbols:** ✅ Allowed \| ❌ Denied \| 🟡 Allowed, but filtered

| Action | manage | read-only | collection read-write | collection read-only | collection with payload claim (r / rw) |
| --- | --- | --- | --- | --- | --- |
| list collections | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| get collection info | ✅ | ✅ | ✅ | ✅ | ❌ |
| create collection | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete collection | ✅ | ❌ | ❌ | ❌ | ❌ |
| update collection params | ✅ | ❌ | ❌ | ❌ | ❌ |
| get collection cluster info | ✅ | ✅ | ✅ | ✅ | ❌ |
| collection exists | ✅ | ✅ | ✅ | ✅ | ✅ |
| update collection cluster setup | ✅ | ❌ | ❌ | ❌ | ❌ |
| update aliases | ✅ | ❌ | ❌ | ❌ | ❌ |
| list collection aliases | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| list aliases | ✅ | ✅ | 🟡 | 🟡 | 🟡 |
| create shard key | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete shard key | ✅ | ❌ | ❌ | ❌ | ❌ |
| create payload index | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete payload index | ✅ | ❌ | ✅ | ❌ | ❌ |
| list collection snapshots | ✅ | ✅ | ✅ | ✅ | ❌ |
| create collection snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete collection snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| download collection snapshot | ✅ | ✅ | ✅ | ✅ | ❌ |
| upload collection snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| recover collection snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| list shard snapshots | ✅ | ✅ | ✅ | ✅ | ❌ |
| create shard snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete shard snapshot | ✅ | ❌ | ✅ | ❌ | ❌ |
| download shard snapshot | ✅ | ✅ | ✅ | ✅ | ❌ |
| upload shard snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| recover shard snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| list full snapshots | ✅ | ✅ | ❌ | ❌ | ❌ |
| create full snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete full snapshot | ✅ | ❌ | ❌ | ❌ | ❌ |
| download full snapshot | ✅ | ✅ | ❌ | ❌ | ❌ |
| get cluster info | ✅ | ✅ | ❌ | ❌ | ❌ |
| recover raft state | ✅ | ❌ | ❌ | ❌ | ❌ |
| delete peer | ✅ | ❌ | ❌ | ❌ | ❌ |
| get point | ✅ | ✅ | ✅ | ✅ | ❌ |
| get points | ✅ | ✅ | ✅ | ✅ | ❌ |
| upsert points | ✅ | ❌ | ✅ | ❌ | ❌ |
| update points batch | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete points | ✅ | ❌ | ✅ | ❌ | ❌ / 🟡 |
| update vectors | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete vectors | ✅ | ❌ | ✅ | ❌ | ❌ / 🟡 |
| set payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| overwrite payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| delete payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| clear payload | ✅ | ❌ | ✅ | ❌ | ❌ |
| scroll points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| query points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| search points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| search groups | ✅ | ✅ | ✅ | ✅ | 🟡 |
| recommend points | ✅ | ✅ | ✅ | ✅ | ❌ |
| recommend groups | ✅ | ✅ | ✅ | ✅ | ❌ |
| discover points | ✅ | ✅ | ✅ | ✅ | ❌ |
| count points | ✅ | ✅ | ✅ | ✅ | 🟡 |
| version | ✅ | ✅ | ✅ | ✅ | ✅ |
| readyz, healthz, livez | ✅ | ✅ | ✅ | ✅ | ✅ |
| telemetry | ✅ | ✅ | ❌ | ❌ | ❌ |
| metrics | ✅ | ✅ | ❌ | ❌ | ❌ |
| update locks | ✅ | ❌ | ❌ | ❌ | ❌ |
| get locks | ✅ | ✅ | ❌ | ❌ | ❌ |

## [Anchor](https://qdrant.tech/documentation/guides/security/\#tls) TLS

_Available as of v1.2.0_

TLS for encrypted connections can be enabled on your Qdrant instance to secure
connections.

First make sure you have a certificate and private key for TLS, usually in
`.pem` format. On your local machine you may use
[mkcert](https://github.com/FiloSottile/mkcert#readme) to generate a self signed
certificate.

To enable TLS, set the following properties in the Qdrant configuration with the
correct paths and restart:

```yaml
service:
  # Enable HTTPS for the REST and gRPC API
  enable_tls: true