# Source: https://buildkite.com/docs/apis/api-differences.md

# API differences between REST and GraphQL

Buildkite provides both a [REST API](/docs/apis/rest-api) and [GraphQL API](/docs/apis/graphql-api), but there are some differences between the two. Some tasks can only be achieved using the GraphQL API or the REST API. For example, REST API is a good choice for Organization-level tasks and it also allows using granular access permissions, while GraphQL is more comprehensive and often can help you achieve things a single user would want to do in the Buildkite UI. We recommend using a mixture of both when required.

The strengths of the GraphQL API are in complex data queries, and the strengths of the REST API are in creating and modifying records.

On this page, we've collected the known limitation where some API features are only available with either REST or GraphQL.

## Features only available in the REST API

- <span class="pill pill--access-token pill--medium">ACCESS TOKEN</span> [Granular access permissions](/docs/apis/managing-api-tokens#token-scopes).
- <span class="pill pill--access-token pill--medium">ACCESS TOKEN</span> [Display the information about the access token currently in use](/docs/apis/rest-api/access-token#get-the-current-token).
- <span class="pill pill--access-token pill--medium">ACCESS TOKEN</span> [Revoke the current access token](/docs/apis/rest-api/access-token#revoke-the-current-token).
- <span class="pill pill--builds pill--medium">BUILDS</span> [Delete annotations on a build](/docs/apis/rest-api/annotations#delete-an-annotation-on-a-build).
- <span class="pill pill--builds pill--medium">BUILDS</span> [Get the `group_key` field for jobs that belong to group steps](/docs/apis/rest-api/builds#get-a-build) (only available through builds endpoints, not individual job endpoints).
- <span class="pill pill--jobs pill--medium">JOBS</span> [Get an output of job logs](/docs/apis/rest-api/jobs#get-a-jobs-log-output).
- <span class="pill pill--jobs pill--medium">JOBS</span> [Retry data for jobs](/docs/apis/rest-api/jobs#retry-a-job).
- <span class="pill pill--meta pill--medium">META</span> [Get a list of IPs from which Buildkite sends webhooks](/docs/apis/rest-api/meta#get-meta-information).
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> [Set provider properties](/docs/apis/rest-api/pipelines#provider-settings-properties) `provider_settings` allow configuring how the pipeline is triggered based on the source code provider's events; available on pipeline for all the pipeline inputs on pipeline create.

## Features only available in the GraphQL API

- <span class="pill pill--agents pill--medium">AGENTS</span> [Get a list of agent token IDs (agent tokens are currently only available via GraphQL)](/docs/apis/graphql/cookbooks/agents#get-a-list-of-unclustered-agent-token-ids).
- <span class="pill pill--builds pill--medium">BUILDS</span> [Get all environment variables set on a build](/docs/apis/graphql/cookbooks/builds#get-environment-variables-set-on-a-build).
- <span class="pill pill--builds pill--medium">BUILDS</span> [Increase the next build number](/docs/apis/graphql/cookbooks/builds#increase-the-next-build-number).
- <span class="pill pill--builds pill--medium">BUILDS</span> [Get build info by ID](/docs/apis/graphql/cookbooks/builds#get-build-info-by-id).
- <span class="pill pill--jobs pill--medium">JOBS</span> [Get all jobs in a given queue for a given timeframe](/docs/apis/graphql/cookbooks/jobs#get-all-jobs-in-a-given-queue-for-a-given-timeframe).
- <span class="pill pill--jobs pill--medium">JOBS</span> [Get all jobs in a particular concurrency group](/docs/apis/graphql/cookbooks/jobs#get-all-jobs-in-a-particular-concurrency-group).
- <span class="pill pill--jobs pill--medium">JOBS</span> list job events.
- <span class="pill pill--jobs pill--medium">JOBS</span> [Cancel a job](/docs/apis/graphql/schemas/mutation/jobtypecommandcancel).
- <span class="pill pill--organizations pill--medium">ORGANIZATIONS</span> [Remove users from an organization](/docs/apis/graphql/cookbooks/organizations#delete-an-organization-member).
- <span class="pill pill--organizations pill--medium">ORGANIZATIONS</span> [Set up SSO](/docs/platform/sso/sso-setup-with-graphql).
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> [Get all the pipeline metrics from the dashboard from the API](/docs/apis/graphql/cookbooks/pipelines#get-pipeline-metrics).
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> [Get the creation date of the most recent build in every pipeline](/docs/apis/graphql/cookbooks/builds#get-the-creation-date-of-the-most-recent-build-in-every-pipeline).
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> [Count the number of builds on a branch](/docs/apis/graphql/cookbooks/builds#count-the-number-of-builds-on-a-branch).
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> Filter results from pipeline listings.
- <span class="pill pill--pipelines pill--medium">PIPELINES</span> Create and manage pipeline schedules.
- <span class="pill pill--users pill--medium">USERS</span> [Invite a user into a specific team with a specific role and permissions set](/docs/apis/graphql/cookbooks/organizations#create-a-user-add-them-to-a-team-and-set-user-permissions).
