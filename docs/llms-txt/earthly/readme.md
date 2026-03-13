# Source: https://docs.earthly.dev/readme.md

# Source: https://docs.earthly.dev/earthly-0.7/readme.md

# Source: https://docs.earthly.dev/earthly-0.6/readme.md

# Introduction

Earthly is a build automation tool from the same era as your code. It allows you to execute all your builds in containers. This makes them self-contained, repeatable, portable and parallel. You can use Earthly to create Docker images and artifacts (e.g. binaries, packages, arbitrary files).

Earthly can run on top of popular CI systems (like [Jenkins](https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/jenkins), [CircleCI](https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/circle-integration), [GitHub Actions](https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/gh-actions-integration), [AWS CodeBuild](https://docs.earthly.dev/earthly-0.6/ci-integration/vendor-specific-guides/codebuild-integration)). It is typically the layer between language-specific tooling (like maven, gradle, npm, pip, go build) and the CI build spec.

![Earthly fits between language-specific tooling and the CI](https://3490584797-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-M3I14IYwbiMH3cL5KCq%2Fuploads%2Fgit-blob-d10638e4183adfdc7fdff0f61f7aed2d2c055c99%2Fintegration-diagram-v2.png?alt=media\&token=839fbafa-63ae-49b9-92ca-b866c5e8f75b)

Earthly has a number of key features. It has a familiar syntax (it's like Dockerfile and Makefile had a baby). Everything runs on containers, so your builds run the same on your laptop as they run in CI or on your colleague's laptop. Strong isolation also gives you easy to use parallelism, with no strings attached. You can also import dependencies from other directories or other repositories with ease, making Earthly great for large [mono-repo builds](https://github.com/earthly/earthly/tree/main/examples/monorepo) that span a vast directory hierarchy; but also for [multi-repo setups](https://github.com/earthly/earthly/tree/main/examples/multirepo) where builds might depend on each other across repositories.

One of the key principles of Earthly is that the best build tooling of a specific language is built by the community of that language itself. Earthly does not intend to replace that tooling, but rather to leverage and augment it.

## Installation

See [installation instructions](https://earthly.dev/get-earthly).

For a full list of installation options see the [alternative installation page](https://docs.earthly.dev/earthly-0.6/docs/misc/alt-installation).

## Getting started

If you are new to Earthly, check out the [Basics page](https://docs.earthly.dev/earthly-0.6/basics), to get started.

A high-level overview is available on [the Earthly GitHub page](https://github.com/earthly/earthly).

## Quick Links

* [Earthly GitHub page](https://github.com/earthly/earthly)
* [Installation instructions](https://earthly.dev/get-earthly)
* [Earthly basics](https://docs.earthly.dev/earthly-0.6/basics)
* [Earthfile reference](https://docs.earthly.dev/earthly-0.6/docs/earthfile)
* [Earthly command reference](https://docs.earthly.dev/earthly-0.6/docs/earthly-command)
* [Configuration reference](https://docs.earthly.dev/earthly-0.6/docs/earthly-config)
* [Earthfile examples](https://docs.earthly.dev/earthly-0.6/docs/examples)
* [Best practices](https://docs.earthly.dev/earthly-0.6/best-practices)
