# Source: https://launchdarkly.com/docs/api/release-pipelines-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

Release pipelines standardize and automate the release process for feature flags across a series of phases, where each phase consists of one or more environments and audiences. Each phase can use an immediate or guarded rollout to a designated audience, and can require approvals for selected environments. You can use release pipelines to ensure that you correctly roll out a flag in one environment before moving on to the next. To learn more, read [Release pipelines](https://launchdarkly.com/docs/home/releases/release-pipelines).

Use the release pipelines API to view, create, update, and delete release pipelines. You can also use this API to view the progress of all ongoing releases across all flags in a project for a given release pipeline. 

### Creating releases and updating release phases

When you add a flag to a release pipeline, you create a new "release" to automate that flag's progress through phases in the pipeline.

Use the related [releases API](https://launchdarkly.com/docs/api/releases-beta) to create a new release, or to view or update a release for a given flag. For example, you can use the releases API to add a flag to an existing release pipeline, or to start the next phase of a flag's ongoing release.
