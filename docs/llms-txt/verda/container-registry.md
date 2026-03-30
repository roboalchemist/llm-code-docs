<!-- Source: https://docs.verda.com/storage/container-registry.md -->

# Container registry

Container Registry is a secure, private repository for your container images. It provides a central location to manage the software building blocks used across your project.

## Getting Started

All registries are private by default. To begin pushing or pulling images, you must first establish authentication between your local environment and the registry.

Image URLs follow this format:

`vccr.io/<PROJECT_ID>/<IMAGE_NAME>:<TAG>`

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>Quickstart</td><td><a href="container-registry/quickstart">quickstart</a></td></tr></tbody></table>

## Image Protection & Lifecycle

Manage the stability and footprint of your repositories through automated policies:

<table data-view="cards"><thead><tr><th></th><th data-hidden data-card-target data-type="content-ref">Target</th></tr></thead><tbody><tr><td>Tag immutability rules</td><td><a href="container-registry/tag-immutability-rules">tag-immutability-rules</a></td></tr><tr><td>Tag retention rules &#x26; retention runs</td><td><a href="container-registry/tag-retention-rules-and-retention-runs">tag-retention-rules-and-retention-runs</a></td></tr><tr><td>Tag rules syntax</td><td><a href="container-registry/tag-rules-syntax">tag-rules-syntax</a></td></tr></tbody></table>

## Optimized Integration

Deploying images within the Verda ecosystem provides significant performance and security advantages for Serverless Containers and Batch Job deployments.
