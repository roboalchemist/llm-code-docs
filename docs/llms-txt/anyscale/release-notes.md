# Source: https://docs.anyscale.com/release-notes.md

# Anyscale release notes and support lifecycle

[View Markdown](/release-notes.md)

# Anyscale release notes and support lifecycle

Discover new feature and products available on Anyscale and learn about the support lifecycle for Anyscale features and Ray versions.

Use the following table to find information about new Anyscale products and Ray versions:

| Resource                                                                              | Description                                                                                                                                                                                                                                                                 |
| ------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Anyscale platform release notes - March 2026](/release-notes/platform/2026/march.md) | Anyscale platform release notes. Includes updates on new features in the Anyscale console, cloud configurations, and other Anyscale products.                                                                                                                               |
| [Anyscale CLI and SDK release notes](/release-notes/cli-sdk.md)                       | Anyscale CLI and SDK release notes. Includes new commands, parameters, behavior changes, and bug fixes.                                                                                                                                                                     |
| [Anyscale base images](/reference/base-images.md)                                     | Lists all of the base images of Ray tested, built, and released by Anyscale. Use this resource to learn about Python and system libraries installed in each image.                                                                                                          |
| [Ray release highlights](https://github.com/ray-project/ray/releases)                 | Provides an overview of new features available in each Ray version. The Ray community contributes these release notes. While most features added to Ray are generally available on Anyscale, Anyscale doesn't recommend or guarantee support for all features added to Ray. |

## Feature release maturity[​](#feature-release-maturity "Direct link to Feature release maturity")

Anyscale works actively with the Ray community and Anyscale customers to develop new features and products. The following table describes the support for release levels on Anyscale:

note

Ray is an open source project and community members frequently contribute new features. Contact [Anyscale support](mailto:support@anyscale.com) if you have questions about the release level of newly introduced Ray features.

| Release level        | Description                                                                                                                                                                                                                                                                                                                             |
| -------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Beta                 | Beta features are in active development. Beta features have established general functionality and use cases, but might still undergo significant changes around nuanced behaviors, APIs, options, or parameters. Use beta features to test out new product features. Anyscale doesn't recommend beta features for production workloads. |
| General availability | Generally available features are stable and recommended for production use. Anyscale proactively communicates with customers if generally available platform features undergo breaking changes. Anyscale works with the Ray community to ensure stability for generally available features in Ray.                                      |

# Ray on Anyscale support lifecycle

Anyscale builds and release base images for each version of Ray. Anyscale also provides nightly builds for users to develop and test Ray features in active development.

The following table describes the stages of support and support policies for Ray on Anyscale.

Workloads on unsupported versions might continue to run, but Anyscale doesn't provide support or any commitment to provide fixes or patches.

| Release status       | Description                                                                                                                                                                                                                                                                                                                                |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| General availability | Anyscale provides general support for Ray versions for six months after they become generally available. This includes building new images that backport major stability and security fixes.                                                                                                                                               |
| End-of-support       | Anyscale considers all Ray versions end-of-support after six months. Workloads running on these versions don't receive Anyscale support, and Anyscale doesn't backport any fixes. You can still access base images that are end-of-support from the Anyscale Docker Hub, but Anyscale might hide these versions from the Anyscale console. |
| End-of-life          | Anyscale considers Ray versions end-of-life after a year. Anyscale reserves the right to completely remove Anyscale base images for end-of-life Ray versions at any time without prior notice.                                                                                                                                             |
| Nightly              | Anyscale provides nightly releases for development and testing against the bleeding-edge version of Ray. Nightly releases include alpha features and don't come with customer support. Anyscale never backports to nightly releases.                                                                                                       |

## Feature deprecation and removal[​](#feature-deprecation-and-removal "Direct link to Feature deprecation and removal")

Anyscale occasionally deprecates and removes features. For generally available features, Anyscale directly communicates timelines for deprecation and removal with customers. These announcements might not appear in public documentation.

Anyscale might choose to abandon development on alpha or beta features. Anyscale works with customers that were using these features to identify new solutions to meet their needs.

Because Ray is an open source project, the community might choose to stop supporting a feature or library. Contact [Anyscale support](mailto:support@anyscale.com) if your Anyscale workloads use features that the Ray community no longer maintains.

Anyscale sometimes uses the term *legacy* to describe features. Legacy features can include features still maintained by the Ray community but not actively recommended by Anyscale. Contact [Anyscale support](mailto:support@anyscale.com) for more information on support for legacy features.

The following table describes support levels for features that Anyscale and the Ray community no longer officially support:

| Support level  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Deprecated     | Deprecated features are no longer maintained by Anyscale but are still available in the product. Anyscale works with customers to identify a timeline for full removal of deprecated features. Anyscale recommends migrating all workloads from deprecated features to stable and maintained features, libraries, and APIs. If you use deprecated features in your Anyscale workloads, contact the Anyscale team to identify migration targets and timelines. |
| End-of-support | Anyscale doesn't offer customer support on features that are end-of-support. End-of-support features might still be available through legacy Ray images or configurations.                                                                                                                                                                                                                                                                                    |
| End-of-life    | Anyscale doesn't offer customer support for features that are end-of-life. End-of-life features are removed from the Anyscale console, CLI, and SDK and no longer available in any Anyscale base images.                                                                                                                                                                                                                                                      |

## All platform release notes[​](#all-platform "Direct link to All platform release notes")

Use the following links to view past release notes for the Anyscale platform.

* [Anyscale platform release notes - March 2026](/release-notes/platform/2026/march.md)
* [Anyscale platform release notes - February 2026](/release-notes/platform/2026/february.md)
* [Anyscale platform release notes - January 2026](/release-notes/platform/2026/january.md)
* [Anyscale platform release notes - 2025](/release-notes/platform/2025.md)
