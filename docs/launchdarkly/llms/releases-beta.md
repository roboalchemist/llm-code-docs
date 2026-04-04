# Source: https://launchdarkly.com/docs/api/releases-beta.md

> ### This feature is in beta
>
> To use this feature, pass in a header including the `LD-API-Version` key with value set to `beta`. Use this header with each call. To learn more, read [Beta resources](https://launchdarkly.com/docs/api#beta-resources).
>
> Resources that are in beta are still undergoing testing and development. They may change without notice, including becoming backwards incompatible.

Release pipelines standardize and automate the release process for feature flags across a series of phases, where each phase consists of one or more environments and audiences. When you add a flag to an existing release pipeline, you create a "release" to automate that flag's progress through the pipeline. 

Use the releases API to add a flag to an existing release pipeline, or to monitor or update an ongoing release for a flag. Updating an ongoing release generally involves the following steps:

1. Obtain the release phases associated with the release. The `phases` field provides an ordered list of all pipeline phases associated with the flag's release. `phases` is returned in the response when you [Create a new release for a flag](https://launchdarkly.com/docs/api/releases-beta/create-release-for-flag) or [Get the release for a flag](https://launchdarkly.com/docs/api/releases-beta/get-release-by-flag-key).

2. Determine the `_id` of the phase you want to start. Release pipeline phases take place in their configured order, so find the first incomplete, unstarted phase in the `phases` list. For example, in a newly-created release the first phase in the `phases` list has both the `complete` and `started` fields set to `false`.

3. Use the phase `_id` value with the [Update phase status for release](https://launchdarkly.com/docs/api/releases-beta/update-phase-status) endpoint to start the release phase. At a minimum, you must provide `{"status": active}` in the request object to start a pipeline phase. If the phase requires approvals or guarded rollouts, provide the additional required information in the `audiences` list.

### Configuring release pipelines

Use the related [release pipelines API](https://launchdarkly.com/docs/api/release-pipelines-beta) to view, create, update, and delete release pipelines, or to view the progress of all ongoing releases across all flags in a project for a given release pipeline. 
