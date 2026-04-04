# Source: https://kreya.app/comparisons/swaggerui.md

# What makes Kreya a good Swagger UI alternative for API testing

Swagger UI is a tool for visualizing and interacting with REST APIs. It is also often used to quickly test APIs.

Here is why Kreya is a good Swagger UI alternative and why you should consider switching from Swagger UI to Kreya for API testing.

![Screenshot of Kreya](/assets/ideal-img/main.4c1860b.400.png)

## Kreya vs Swagger UI comparison: What are the differences?[​](#kreya-vs-swagger-ui-comparison-what-are-the-differences "Direct link to Kreya vs Swagger UI comparison: What are the differences?")

### Overview[​](#overview "Direct link to Overview")

| Feature / topic               | Swagger UI           | Kreya                |
| ----------------------------- | -------------------- | -------------------- |
| Tests and snapshot assertions | ❌                   | ✅                   |
| Suited for documenting APIs   | ✅                   | (<!-- -->✅<!-- -->) |
| Works with OpenAPI            | ✅                   | ✅                   |
| gRPC support                  | ❌                   | ✅                   |
| GraphQL support               | ❌                   | ✅                   |
| WebSocket support             | ❌                   | ✅                   |
| Environments and templating   | ❌                   | ✅                   |
| Directory settings            | ❌                   | ✅                   |
| Reusing authentication        | (<!-- -->✅<!-- -->) | ✅                   |
| Directory settings            | ❌                   | ✅                   |
| Data previews                 | ❌                   | ✅                   |
| CLI                           | ❌                   | ✅                   |
| Free plan                     | ✅                   | ✅                   |

### Testing tool[​](#testing-tool "Direct link to Testing tool")

Swagger UI is a wonderful tool to explore and document REST APIs. It is also often used to quickly test APIs. However, Swagger UI is not made to often and repeatedly test the same API.

Kreya is much better suited for that, as it allows to store the test data, share common values such as headers between requests and more.

### No gRPC support[​](#no-grpc-support "Direct link to No gRPC support")

As Swagger UI is specific to REST, other protocols such as gRPC or GraphQL cannot be tested with Swagger UI.

### Environments and templating[​](#environments-and-templating "Direct link to Environments and templating")

Switching between different environments is a core feature of most popular API testing clients. However, Swagger UI does not support this feature. This makes testing different environments of the same API (for example Test and Production) difficult.

Kreya does support environments. In combination with the powerful templating language Scriban, this makes switching between testing different environments very easy.

### Directory settings[​](#directory-settings "Direct link to Directory settings")

A feature that makes Kreya a joy to use are the directory settings. It allows users to specify default settings for multiple operations in a folder or the whole project. For example, if all operations in a project use the same host or the same authentication configuration, it only needs to be specified once. This even supports templating and environment specific values, so switching between environments works flawlessly after the initial configuration. Swagger UI does not have a comparable feature.

### Data previews and visualizations[​](#data-previews-and-visualizations "Direct link to Data previews and visualizations")

Kreya allows you to create custom data visualizations and previews directly from your API responses. With the [`kreya.preview` API](/docs/scripting-and-tests/previews.md), you can render charts, HTML, PDFs, and more, making it easy to interpret and share results visually. This is especially useful for debugging, reporting, or sharing insights with your team.

SwaggerUI does not support custom data previews or visualizations.

Learn more in the [data previews documentation](/docs/scripting-and-tests/previews.md).

### Pricing[​](#pricing "Direct link to Pricing")

SwaggerUI is completely free to use. Although Kreya has paid plans, almost all features are also available in the free version. In fact, all features that SwaggerUI implements plus many more are usable in Kreya without paying or creating an account.
