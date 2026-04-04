# Alternatively, you can use the `Authorization` header with the `Bearer` prefix
curl \
  -X GET https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6333 \
  --header 'Authorization: Bearer <provide-your-own-key>'

```

```python
from qdrant_client import QdrantClient

qdrant_client = QdrantClient(
    "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
    api_key="<paste-your-api-key-here>",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({
  host: "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
  apiKey: "<paste-your-api-key-here>",
});

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("https://xyz-example.cloud-region.cloud-provider.cloud.qdrant.io:6334")
    .api_key("<paste-your-api-key-here>")
    .build()?;

```

```java
import io.qdrant.client.QdrantClient;
import io.qdrant.client.QdrantGrpcClient;

QdrantClient client =
    new QdrantClient(
        QdrantGrpcClient.newBuilder(
                "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
                6334,
                true)
            .withApiKey("<paste-your-api-key-here>")
            .build());

```

```csharp
using Qdrant.Client;

var client = new QdrantClient(
  host: "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
  https: true,
  apiKey: "<paste-your-api-key-here>"
);

```

```go
import "github.com/qdrant/go-client/qdrant"

client, err := qdrant.NewClient(&qdrant.Config{
	Host:   "xyz-example.cloud-region.cloud-provider.cloud.qdrant.io",
	Port:   6334,
	APIKey: "<paste-your-api-key-here>",
	UseTLS: true,
})

```

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/authentication.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/cloud/authentication.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-49-lllmstxt|>
## web-ui-gsoc
- [Articles](https://qdrant.tech/articles/)
- Google Summer of Code 2023 - Web UI for Visualization and Exploration

[Back to Ecosystem](https://qdrant.tech/articles/ecosystem/)