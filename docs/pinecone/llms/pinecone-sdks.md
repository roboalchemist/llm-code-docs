# Source: https://docs.pinecone.io/reference/pinecone-sdks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.pinecone.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

## Pinecone SDKs

Official Pinecone SDKs provide convenient access to the [Pinecone APIs](/reference/api/introduction).

<CardGroup cols={3}>
  <Card title="Python SDK" icon="python" href="/reference/sdks/python/overview" />

  <Card title="Node.js SDK" icon="node-js" href="/reference/sdks/node/overview" />

  <Card title="Java SDK" icon="java" href="/reference/sdks/java/overview" />

  <Card title="Go SDK" icon="golang" href="/reference/sdks/go/overview" />

  <Card title=".NET SDK" icon="microsoft" href="/reference/sdks/dotnet/overview" />

  <Card title="Rust SDK" icon="rust" href="/reference/sdks/rust/overview" />
</CardGroup>

## SDK versions

SDK versions are pinned to specific [API versions](/reference/api/versioning). When a new API version is released, a new version of the SDK is also released.

The mappings between API versions and SDK versions are as follows:

|                                               | `2025-04` | `2025-01` | `2024-10` | `2024-07`     | `2024-04` |
| --------------------------------------------- | :-------- | :-------- | :-------- | :------------ | :-------- |
| [Python SDK](/reference/sdks/python/overview) | v7.x      | v6.x      | v5.3.x    | v5.0.x-v5.2.x | v4.x      |
| [Node.js SDK](/reference/sdks/node/overview)  | v6.x      | v5.x      | v4.x      | v3.x          | v2.x      |
| [Java SDK](/reference/sdks/java/overview)     | v5.x      | v4.x      | v3.x      | v2.x          | v1.x      |
| [Go SDK](/reference/sdks/go/overview)         | v4.x      | v3.x      | v2.x      | v1.x          | v0.x      |
| [.NET SDK](/reference/sdks/dotnet/overview)   | v4.x      | v3.x      | v2.x      | v1.x          | v0.x      |

When a new stable API version is released, you should upgrade your SDK to the latest version to ensure compatibility with the latest API changes.

<Note>
  SDKs that target API version `2025-10` will be available soon.
</Note>

## Limitations

While Pinecone tracks read unit usage with decimal precision, the Pinecone API and SDKs round these values up to the nearest whole number in query, fetch, and list responses. For example, if a query uses 0.45 read units, the API and SDKs will report it as 1 read unit.

For precise read unit reporting, see [index-level metrics](/guides/production/monitoring) or the organization-wide [Usage dashboard](/guides/manage-cost/monitor-usage-and-costs#monitor-organization-level-usage-and-costs).

## Community SDKs

Find community-contributed SDKs for Pinecone. These libraries are not supported by Pinecone.

* [Ruby SDK](https://github.com/ScotterC/pinecone) (contributed by [ScotterC](https://github.com/ScotterC))

* [Scala SDK](https://github.com/cequence-io/pinecone-scala) (contributed by [cequence-io](https://github.com/cequence-io))

* [PHP SDK](https://github.com/probots-io/pinecone-php) (contributed by [protobots-io](https://github.com/probots-io))
