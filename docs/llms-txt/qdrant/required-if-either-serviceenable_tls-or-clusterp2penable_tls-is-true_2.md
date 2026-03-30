# Required if either service.enable_tls or cluster.p2p.enable_tls is true.
tls:
  # Server certificate chain file
  cert: ./tls/cert.pem

  # Server private key file
  key: ./tls/key.pem

```

For internal communication when running cluster mode, TLS can be enabled with:

```yaml
cluster:
  # Configuration of the inter-cluster communication
  p2p:
    # Use TLS for communication between peers
    enable_tls: true

```

With TLS enabled, you must start using HTTPS connections. For example:

bashpythontypescriptrust

```bash
curl -X GET https://localhost:6333

```

```python
from qdrant_client import QdrantClient

client = QdrantClient(
    url="https://localhost:6333",
)

```

```typescript
import { QdrantClient } from "@qdrant/js-client-rest";

const client = new QdrantClient({ url: "https://localhost", port: 6333 });

```

```rust
use qdrant_client::Qdrant;

let client = Qdrant::from_url("http://localhost:6334").build()?;

```

Certificate rotation is enabled with a default refresh time of one hour. This
reloads certificate files every hour while Qdrant is running. This way changed
certificates are picked up when they get updated externally. The refresh time
can be tuned by changing the `tls.cert_ttl` setting. You can leave this on, even
if you don’t plan to update your certificates. Currently this is only supported
for the REST API.

Optionally, you can enable client certificate validation on the server against a
local certificate authority. Set the following properties and restart:

```yaml
service:
  # Check user HTTPS client certificate against CA file specified in tls config
  verify_https_client_certificate: false