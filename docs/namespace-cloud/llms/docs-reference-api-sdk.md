<!-- Source: https://namespace.so/docs/reference/api-sdk -->

# Namespace API & SDK

Namespace exposes a public API to allow building integrations on top of our platform.
In addition to our detailed [API Documentation](https://buf.build/namespace/cloud),
there are ready-to-use [SDKs](https://buf.build/namespace/cloud/sdks) for over 15 languages.

## API Reference

Our API reference can be found at [buf.build/namespace/cloud](https://buf.build/namespace/cloud).
It details what endpoints to use, and how to authenticate to them.
For each service, available procedures as well as their request and response types are listed:

[![Screenshot of available procedures for the Builders service of Namespaces API](/_next/static/media/buf-builders-api.e45a1b07.png)](https://buf.build/namespace/cloud/docs/main:namespace.cloud.builder.v1beta#namespace.cloud.builder.v1beta.BuilderService)

When clicking through to a request or response type, the contents of this type are described.
All available fields including their types and intended use are displayed:

[![Screenshot of the field descriptions of a request and response message](/_next/static/media/buf-request-response.88671108.png)](https://buf.build/namespace/cloud/docs/main:namespace.cloud.builder.v1beta#namespace.cloud.builder.v1beta.GetBuilderUsageRequest)

## SDKs

### Go SDK

Namespace maintains an SDK for use in Go projects that provides ready-to-use clients including authentication and examples.
The Go implementation is the most mature SDK and is used in production by multiple integrations.

The Go SDK can be found at [github.com/namespacelabs/integrations](https://github.com/namespacelabs/integrations)

### TypeScript SDK

Namespace maintains a TypeScript/JavaScript SDK that provides authentication, client management, and type-safe API access.
It supports both ESM and CommonJS, and follows similar patterns to the Go SDK.

The TypeScript SDK can be found at [github.com/namespacelabs/typescript-sdk](https://github.com/namespacelabs/typescript-sdk)

### Elixir

If you are using Elixir, check out the [reference implementation](https://github.com/tuist/tuist/blob/401ab9e171311d8428ec4793f46ea4eb4dab64a7/server/lib/tuist/namespace.ex) provided by [Tuist](https://tuist.dev).
The integration demonstrates how to manage tenants, create instances, ensure readiness, and gain programmatic instance access via SSH.

### Other languages

For many languages, generated SDKs are available to quickly get started with Namespaces API.
These SDKs include all available procedures and request/response types to support autocompletion in your IDE.

SDKs are available for many languages including Go, Python, Javascript, TypeScript, Rust, and more.

To get started, visit the [SDKs page](https://buf.build/namespace/cloud/sdks) and install the SDK for your language.

![Some of the SDKs available for Namespaces API](/_next/static/media/buf-sdks.3539b72b.png)

Some of the available SDKs

## Examples

Working examples in Go, TypeScript, and Python are available at [github.com/namespacelabs/examples](https://github.com/namespacelabs/examples).
They cover instance creation, Kubernetes clusters, container deployment, builds, IAM, and more — including no-SDK approaches using raw HTTP requests.

## IAM Integration

In order to create and manage multiple workspaces programatically, you can integrate with [Namespace IAM](https://buf.build/namespace/cloud/docs/main:namespace.cloud.iam.v1beta).
Namespace relies on trust relationships using public-key cryptography and the OpenID Connect standard to verify the tokens instead of pre-shared keys which are more easily compromised.

Last updated March 20, 2026
