# Alternatively, you can use the `Authorization` header with the `Bearer` prefix
curl \
  -X GET https://xyz-example.eu-central.aws.cloud.qdrant.io:6333 \
  --header 'Authorization: Bearer <your-api-key>'

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    host="xyz-example.eu-central.aws.cloud.qdrant.io",
    api_key="<your-api-key>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  apiKey: "<your-api-key>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.eu-central.aws.cloud.qdrant.io:6334")
    .api_key("<your-api-key>")
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
            .withApiKey("<your-api-key>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.eu-central.aws.cloud.qdrant.io",
  https: true,
  apiKey: "<your-api-key>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.eu-central.aws.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<your-api-key>",
	UseTLS: true,
})

```

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#try-the-tutorial-sandbox) Try the Tutorial Sandbox

1. Open the interactive **Tutorial**. Here, you can test basic Qdrant API requests.
2. Using the **Quickstart** instructions, create a collection, add vectors and run a search.
3. The output on the right will show you some basic semantic search results.

![interactive-tutorial](https://qdrant.tech/docs/gettingstarted/gui-quickstart/interactive-tutorial.png)

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#thats-vector-search) That’s Vector Search!

You can stay in the sandbox and continue trying our different API calls.

When ready, use the Console and our complete REST API to try other operations.

## [Anchor](https://qdrant.tech/documentation/cloud-quickstart/\#whats-next) What’s Next?

Now that you have a Qdrant Cloud cluster up and running, you should [test remote access](https://qdrant.tech/documentation/cloud/authentication/#test-cluster-access) with a Qdrant Client.

For more about Qdrant Cloud, check our [dedicated documentation](https://qdrant.tech/documentation/cloud-intro/).

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-quickstart.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud-quickstart.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-60-lllmstxt|>
## documentation