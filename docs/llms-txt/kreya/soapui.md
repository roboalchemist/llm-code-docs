# Source: https://kreya.app/comparisons/soapui.md

# What makes Kreya a good SoapUI alternative

SoapUI, created by Smartbear, has been around for ages. It was one of the earliest GUI programs for testing APIs and mainly focused on SOAP (hence the name). A while ago, Smartbear released ReadyAPI as the commercial (and very expensive) alternative to the free SoapUI. ReadyAPI isn't covered in this comparison.

Here is why Kreya is a good SoapUI alternative and why you should consider switching from SoapUI to Kreya.

![Screenshot of Kreya](/assets/ideal-img/main.4c1860b.400.png)

## Kreya vs SoapUI comparison: What are the differences?[​](#kreya-vs-soapui-comparison-what-are-the-differences "Direct link to Kreya vs SoapUI comparison: What are the differences?")

### Overview[​](#overview "Direct link to Overview")

| Feature / topic             | SoapUI               | Kreya |
| --------------------------- | -------------------- | ----- |
| Modern UI                   | ❌                   | ✅    |
| gRPC support                | ❌                   | ✅    |
| REST support                | ✅                   | ✅    |
| GraphQL support             | ✅                   | ✅    |
| SOAP support                | ✅                   | ❌    |
| Environments and templating | ❌                   | ✅    |
| Directory settings          | ❌                   | ✅    |
| Reusing authentication      | (<!-- -->❌<!-- -->) | ✅    |
| Directory settings          | ❌                   | ✅    |
| CLI                         | ❌                   | ✅    |
| Storing data locally        | ✅                   | ✅    |
| Snapshot assertions         | ❌                   | ✅    |
| Data previews               | ❌                   | ✅    |
| Free plan                   | ✅                   | ✅    |

### Modern tooling[​](#modern-tooling "Direct link to Modern tooling")

SoapUI still runs on Java 1.8 and it shows. The UI looks and fells like every outdated Java application. The usage of Java 1.8 also hinders the usage of modern protocols. For example, SoapUI does not support HTTP/2.

It also shows the mindset of Smartbear that SoapUI is no longer a priority, as that has shifted to the commercial ReadyAPI version. Feature requests, such as importing OpenAPI 3, are ignored for years and probably will never be implemented.

### No gRPC support[​](#no-grpc-support "Direct link to No gRPC support")

Users looking to test gRPC APIs with SoapUI will be disappointed. SoapUI does not support gRPC, only REST, GraphQL, and SOAP. SOAP usage is in decline, while gRPC is rising in popularity.

### Environments and templating[​](#environments-and-templating "Direct link to Environments and templating")

Switching between different environments is a core feature of most popular API testing clients. However, SoapUI does not support this feature. This makes testing different environments of the same API (for example Test and Production) difficult.

Kreya does support environments. In combination with the powerful templating language Scriban, this makes switching between testing different environments very easy.

### Authentication[​](#authentication "Direct link to Authentication")

[Kreya supports several authentication mechanisms such as OAuth2 or Windows authentication](/docs/authentication.md), which SoapUI also supports. Reusing the same authentication configuration in Kreya is easy, as there is no need to duplicate authentication information for different requests. Comparing this with SoapUI, it is much more of a hassle to reuse the same authentication configuration for multiple requests, as the authentication parameters must be copied each time.

### Directory settings[​](#directory-settings "Direct link to Directory settings")

A feature that makes Kreya a joy to use are the directory settings. It allows users to specify default settings for multiple operations in a folder or the whole project. For example, if all operations in a project use the same host or the same authentication configuration, it only needs to be specified once. This even supports templating and environment specific values, so switching between environments works flawlessly after the initial configuration. SoapUI does not have a comparable feature.

### Data previews and visualizations[​](#data-previews-and-visualizations "Direct link to Data previews and visualizations")

Kreya allows you to create custom data visualizations and previews directly from your API responses. With the [`kreya.preview` API](/docs/scripting-and-tests/previews.md), you can render charts, HTML, PDFs, and more, making it easy to interpret and share results visually. This is especially useful for debugging, reporting, or sharing insights with your team.

SoapUI does not support custom data previews or visualizations.

Learn more in the [data previews documentation](/docs/scripting-and-tests/previews.md).

### Snapshot assertions[​](#snapshot-assertions "Direct link to Snapshot assertions")

Snapshot assertions are a powerful way to ensure your API responses remain consistent over time. Kreya supports snapshot testing out of the box, allowing you to automatically capture and compare API responses with no coding required. This makes it easy to detect unexpected changes and maintain confidence in your APIs.

SoapUI does not support snapshot assertions. If you want to use snapshot-based testing to catch regressions or review changes in API responses, Kreya is the better choice.

Learn more in the [snapshot testing documentation](/docs/scripting-and-tests/tests.md).
