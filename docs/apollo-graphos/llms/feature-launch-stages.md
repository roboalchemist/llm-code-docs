# Source: https://www.apollographql.com/docs/graphos/resources/feature-launch-stages.md

# Apollo Feature Launch Stages

Apollo releases features in various phases of development. This page describes the launch stages of a feature as it progresses through Apollo’s product development lifecycle.

A feature doesn’t necessarily go through all the launch stages.

## Apollo feature release stages

### Experimental

Experimental features make available potentially new features that we want to test with and gather feedback from developers. These features might not be complete, they might have breaking changes at any time, and they might be removed from a product or an incremental version of a release without notice.

### Preview

Preview features are a near-complete implementation of associated functionality. They may be announced publicly or made available privately to a select set of customers. Preview features might contain bugs or undergo iteration, but are fully supported by Apollo. You are encouraged to try Preview versions of a feature to familiarize yourself with upcoming functionality and give us feedback.

### General availability

Generally available (GA) features are ready for use in production environments and are fully supported by Apollo. Features may be released directly as GA without an Experimental or Preview release period. Features are assumed to be GA unless they are otherwise designated (Experimental, Deprecated, etc.).

## Apollo feature retirement stages

When Apollo decides to end support for a product, feature, or open-source release, we will first mark the product or feature as deprecated to give customers time to migrate to an alternative solution. Once the Deprecated period is complete, Apollo will declare the feature end-of-life. The duration of the Deprecated period will vary based on the feature in question.

### Deprecated

Deprecated features are supported by Apollo until the end of the Deprecation period. They continue to receive security patches and updates to address major regressions. An end-of-life date is provided alongside the deprecation announcement, after which support ends.

### End-of-Life (EOL)

Features that reach End-of-Life (EOL) are no longer supported or maintained by Apollo. They no longer receive updates, security patches, or remediation for regressions. Apollo makes no commitment to release further versions and no guarantee that the most recent version will continue to work. EOL features are not suitable for production use.

## Feature lifecycle in releases

A feature can be introduced in any release lifecycle phase that’s under active feature development:

* For GraphOS Router, features can launch in [Developer Preview and Active phases](https://www.apollographql.com/docs/graphos/reference/router-release-lifecycle)
* For Apollo open-source, features can launch in [Alpha/Beta and GA phases](https://www.apollographql.com/docs/graphos/reference/client-library-release-lifecycle)

After launch, a feature can be deprecated in any release phase.
