# Source: https://buildkite.com/docs/apis/webhooks/package-registries.md

# Source: https://buildkite.com/docs/package-registries.md

# Buildkite Package Registries

Scale out asset management for faster builds and deployments across any ecosystem with _Buildkite Package Registries_. Secure your supply chain and avoid the bottlenecks of poorly managed and insecure dependencies.

Package Registries allows you to:

- Manage artifacts and packages from [Buildkite Pipelines](/docs/pipelines), as well as other CI/CD applications that require artifact management.

- Provide registries to store your [packages and other package-like file formats](/docs/package-registries/background) such as container images and Terraform modules.

As well as storing a collection of packages, a registry also surfaces metadata or attributes associated with a package, such as the package's description, version, contents (files and directories), checksum details, distribution type, dependencies, and so on.

> 📘
> Customers on legacy Buildkite plans can enable [Package Registries](https://buildkite.com/platform/package-registries) through the [**Organization Settings** page](/docs/package-registries/security/permissions#enabling-buildkite-packages).

## Get started

Run through the [Getting started](/docs/package-registries/getting-started) tutorial for a step-by-step guide on how to use Buildkite Package Registries.

If you're familiar with the basics, explore how to use registries for each of Buildkite Package Registries' supported package ecosystems:

<div class="ButtonGroup">
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/alpine">:alpine: Alpine (apk)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/oci">:docker: OCI (Docker)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/debian">:debian: Debian/Ubuntu (deb)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/files">:package: Files (generic)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/helm-oci">:helm: Helm (OCI)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/helm">:helm: Helm</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/hugging-face">:hugging_face: Hugging Face (models)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/maven">:maven: Java (Maven)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/gradle-kotlin">:gradle: Java (Gradle)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/javascript">:node: JavaScript (npm)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/nuget">:nuget: NuGet</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/python">:python: Python (PyPI)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/red-hat">:redhat: Red Hat (RPM)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/ruby">:ruby: Ruby (RubyGems)</a>
  <a class="Button Button--default" href="/docs/package-registries/ecosystems/terraform">:terraform: Terraform (modules)</a>
</div>

## Core features

<section class="Tiles"><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/package-registries/registries/manage">Manage source registries</a></h2><p class="TileItem__desc">Create and manage private or public registries to securely store and share packages within your organization.</p><a class="TileItem__learn-more" href="/docs/package-registries/registries/manage">Learn more</a></article><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/package-registries/security/permissions">Access control</a></h2><p class="TileItem__desc">Granular user and team permissions to control who can access and manage your registries.</p><a class="TileItem__learn-more" href="/docs/package-registries/security/permissions">Learn more</a></article><article class="TileItem"><h2 class="TileItem__title"><a class="TileItem__title-link" href="/docs/package-registries/registries/private-storage-link">Private storage options</a></h2><p class="TileItem__desc">Configure your own private storage backend for Buildkite Package Registries, including support for AWS S3 and Google Cloud Storage.</p><a class="TileItem__learn-more" href="/docs/package-registries/registries/private-storage-link">Learn more</a></article></section>

## API & references

Learn more about:

- Package Registries' APIs through the:
  - [REST API documentation](/docs/apis/rest-api), and related endpoints, starting with [registries](/docs/apis/rest-api/package-registries/registries).
  - [GraphQL documentation](/docs/apis/graphql-api) and its [registries](/docs/apis/graphql/cookbooks/registries)-related queries, as well as [portals](/docs/apis/graphql/portals).
- Package Registries' [webhooks](/docs/apis/webhooks/package-registries).
