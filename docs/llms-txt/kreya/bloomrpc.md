# Source: https://kreya.app/comparisons/bloomrpc.md

# What makes Kreya the best BloomRPC alternative

BloomRPC was the first gRPC GUI client to emerge. Lacking competition, it quickly gained a lot of adoption. Here is why Kreya is the best BloomRPC alternative and why you should consider switching from BloomRPC to Kreya.

caution

BloomRPC has been deprecated and the GitHub repository was archived. Consider switching to Kreya.

![Screenshot of Kreya](/assets/ideal-img/main.4c1860b.400.png)

## Kreya vs BloomRPC comparison: What are the differences?[​](#kreya-vs-bloomrpc-comparison-what-are-the-differences "Direct link to Kreya vs BloomRPC comparison: What are the differences?")

### Overview[​](#overview "Direct link to Overview")

| Feature / topic     | BloomRPC                | Kreya               |
| ------------------- | ----------------------- | ------------------- |
| Response metadata   | ❌                      | ✅                  |
| Server reflection   | ❌                      | ✅                  |
| Actively maintained | ❌<!-- --> (deprecated) | ✅                  |
| REST support        | ❌                      | ✅                  |
| GraphQL support     | ❌                      | ✅                  |
| WebSocket support   | ❌                      | ✅                  |
| Authentication      | ❌                      | ✅                  |
| Sharing projects    | ❌                      | ✅                  |
| Snapshot assertions | ❌                      | ✅                  |
| Data previews       | ❌                      | ✅                  |
| Pricing             | Free                    | Free and paid plans |

### Lack of features[​](#lack-of-features "Direct link to Lack of features")

BloomRPC is a very basic gRPC GUI client. It supports the different gRPC operation types (unary, client-streaming, server-streaming and duplex), request metadata and gRPC-web. Several key features, such as response metadata or server reflection are not implemented. Since BloomRPC has been deprecated, these features will never be implemented. Meanwhile, Kreya supports all features that BloomRPC implements (and many more) while keeping the simplicity.

### REST support[​](#rest-support "Direct link to REST support")

Unlike Kreya, BloomRPC does not support REST or GraphQL. This may prove annoying for projects that use both gRPC and REST (eg. for file uploads), as users would have to switch between two different programs.

### Authentication[​](#authentication "Direct link to Authentication")

Kreya supports several authentication mechanisms such as OAuth2 or Windows authentication. Reusing the same authentication configuration with Kreya is easy, there is no need to duplicate authentication information for different requests. In addition, Kreya also supports client TLS certificates. With BloomRPC, authentication information must be manually provided via gRPC metadata. There is no out of the box support for OAuth2 or other authentication mechanisms.

### Data storage and sharing[​](#data-storage-and-sharing "Direct link to Data storage and sharing")

BloomRPC stores the data in a single JSON file in the appdata directory. This makes it difficult to share BloomRPC "projects" with other users. In contrast, Kreya explicitly stores the data in a format that is easy to sync with for example git. Case in point is that Kreya does not store stringified JSON (which could cause a lot of merge conflicts) and allows users to choose where the data is stored.

### Data previews and visualizations[​](#data-previews-and-visualizations "Direct link to Data previews and visualizations")

Kreya allows you to create custom data visualizations and previews directly from your API responses. With the [`kreya.preview` API](/docs/scripting-and-tests/previews.md), you can render charts, HTML, PDFs, and more, making it easy to interpret and share results visually. This is especially useful for debugging, reporting, or sharing insights with your team.

BloomRPC does not support custom data previews or visualizations.

Learn more in the [data previews documentation](/docs/scripting-and-tests/previews.md).

### Snapshot assertions[​](#snapshot-assertions "Direct link to Snapshot assertions")

Snapshot assertions are a powerful way to ensure your API responses remain consistent over time. Kreya supports snapshot testing out of the box, allowing you to automatically capture and compare API responses with no coding required. This makes it easy to detect unexpected changes and maintain confidence in your APIs.

BloomRPC does not support snapshot assertions. If you want to use snapshot-based testing to catch regressions or review changes in API responses, Kreya is the better choice.

Learn more in the [snapshot testing documentation](/docs/scripting-and-tests/tests.md).

### Pricing[​](#pricing "Direct link to Pricing")

BloomRPC is completely free to use. Although Kreya has paid plans, almost all features are also available in the free version. In fact, all features that BloomRPC implements plus many more are usable in Kreya without paying or creating an account.
