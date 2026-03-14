# Source: https://zuul-ci.org/docs/zuul/latest/tenants.html

Title: Tenant Configuration — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/tenants.html

Markdown Content:
After `zuul.conf` is configured, Zuul component servers will be able to start, but a tenant configuration is required in order for Zuul to perform any actions. The tenant configuration file specifies upon which projects Zuul should operate. These repositories are grouped into tenants. The configuration of each tenant is separate from the rest (no pipelines, jobs, etc are shared between them).

A project may appear in more than one tenant; this may be useful if you wish to use common job definitions across multiple tenants.

Actions normally available to the Zuul operator only can be performed by specific users on Zuul’s REST API if admin rules are listed for the tenant. Authorization rules are also defined in the tenant configuration file.

The tenant configuration file is specified by the [scheduler.tenant_config](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config "attr-scheduler.tenant_config") setting in `zuul.conf`. It is a YAML file which, like other Zuul configuration files, is a list of configuration objects, though only a few types of objects (described below) are supported.

Alternatively the [scheduler.tenant_config_script](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config_script "attr-scheduler.tenant_config_script") can be the path to an executable that will be executed and its stdout used as the tenant configuration. The executable must return a valid tenant YAML formatted output.

Tenant configuration is checked for updates any time a scheduler is started, and changes to it are read automatically. If the tenant configuration is altered during operation, you can signal a scheduler to read and apply the updated state in order to avoid restarting. See the section on [Reconfiguration](https://zuul-ci.org/docs/zuul/latest/operation.html#reconfiguration) for instructions. Ideally, tenant configuration deployment via configuration management should also be made to trigger a smart-reconfigure once the file is replaced.

Tenant[](https://zuul-ci.org/docs/zuul/latest/tenants.html#tenant "Link to this heading")
------------------------------------------------------------------------------------------

A tenant is a collection of projects which share a Zuul configuration. Some examples of tenant definitions are:

- tenant:
 name: my-tenant
 max-nodes-per-job: 5
 exclude-unprotected-branches: false
 source:
 gerrit:
 config-projects:
 - common-config
 - shared-jobs:
 include: job
 untrusted-projects:
 - zuul/zuul-jobs:
 shadow: common-config
 - project1
 - project2:
 exclude-unprotected-branches: true

- tenant:
 name: my-tenant
 admin-rules:
 - acl1
 - acl2
 source:
 gerrit:
 config-projects:
 - common-config
 untrusted-projects:
 - exclude:
 - job
 - semaphore
 - project
 - project-template
 - nodeset
 - secret
 projects:
 - project1
 - project2:
 exclude-unprotected-branches: true

tenant[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant "Link to this definition")

The following attributes are supported:

tenant.name(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.name "Link to this definition")

The name of the tenant. This may appear in URLs, paths, and monitoring fields, and so should be restricted to URL friendly characters (ASCII letters, numbers, hyphen and underscore) and you should avoid changing it unless necessary.

tenant.source(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.source "Link to this definition")

A dictionary of sources to consult for projects. A tenant may contain projects from multiple sources; each of those sources must be listed here, along with the projects it supports. The name of a [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) is used as the dictionary key (e.g. `gerrit` in the example above), and the value is a further dictionary containing the keys below.

The next two attributes, **config-projects** and **untrusted-projects** provide the bulk of the information for tenant configuration. They list all of the projects upon which Zuul will act.

The order of the projects listed in a tenant is important. A job which is defined in one project may not be redefined in another project; therefore, once a job appears in one project, a project listed later will be unable to define a job with that name. Further, some aspects of project configuration (such as the merge mode) may only be set on the first appearance of a project definition.

Zuul loads the configuration from all **config-projects** in the order listed, followed by all **untrusted-projects** in order.

tenant.config-projects[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.config-projects "Link to this definition")

A list of projects to be treated as [config projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project) in this tenant. The jobs in a config project are trusted, which means they run with extra privileges, do not have their configuration dynamically loaded for proposed changes, and Zuul config files are only searched for in the `master` branch.

The items in the list follow the same format described in **untrusted-projects**.

tenant.config-projects.<project>[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.config-projects.%3Cproject%3E "Link to this definition")

The config-projects have an additional config option that may be specified optionally.

tenant.config-projects.<project>.load-branch[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.config-projects.%3Cproject%3E.load-branch "Link to this definition")

Default:`master`

Define which branch is loaded from a config project. By default config projects load Zuul configuration only from the master branch.

tenant.untrusted-projects[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects "Link to this definition")

A list of projects to be treated as untrusted in this tenant. An [untrusted-project](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-untrusted-project) is the typical project operated on by Zuul. Their jobs run in a more restrictive environment, they may not define pipelines, their configuration dynamically changes in response to proposed changes, and Zuul will read configuration files in all of their branches.

tenant.untrusted-projects.<project>[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E "Link to this definition")

The items in the list may either be simple string values of the project names, or a dictionary with the project name as key and the following values:

tenant.untrusted-projects.<project>.include[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.include "Link to this definition")

Normally Zuul will load all of the [Configuration Items](https://zuul-ci.org/docs/zuul/latest/project-config.html#configuration-items) appropriate for the type of project (config or untrusted) in question. However, if you only want to load some items, the **include** attribute can be used to specify that _only_ the specified items should be loaded. Supplied as a string, or a list of strings.

The following **configuration items** are recognized:

*   pipeline

*   job

*   semaphore

*   project

*   project-template

*   nodeset

*   secret

*   image

*   flavor

*   label

*   section

*   provider

tenant.untrusted-projects.<project>.exclude[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude "Link to this definition")

A list of **configuration items** that should not be loaded.

tenant.untrusted-projects.<project>.include-provider-config[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.include-provider-config "Link to this definition")

Type:_bool_

Add the configuration items related to provider configuration to the set of items to be loaded. Normally, [untrusted projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-untrusted-project) do not load these items, but [config projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project) do. To allow an untrusted-project to do so (or to add back this set of items after using **include**), set this attribute to `true`. This takes effect after **include** and before **exclude**.

The following **configuration items** are considered **provider config**:

*   image

*   flavor

*   label

*   section

*   provider

tenant.untrusted-projects.<project>.shadow[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.shadow "Link to this definition")

Normally, only one project in Zuul may contain definitions for a given job. If a project earlier in the configuration defines a job which a later project redefines, the later definition is considered an error and is not permitted. The **shadow** attribute of a project indicates that job definitions in this project which conflict with the named projects should be ignored, and those in the named project should be used instead. The named projects must still appear earlier in the configuration. In the example above, if a job definition appears in both the `common-config` and `zuul-jobs` projects, the definition in `common-config` will be used.

tenant.untrusted-projects.<project>.exclude-unprotected-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude-unprotected-branches "Link to this definition")

Define if unprotected branches should be processed. Defaults to the tenant wide setting of exclude-unprotected-branches. This currently only affects GitHub and GitLab projects.

tenant.untrusted-projects.<project>.exclude-locked-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude-locked-branches "Link to this definition")

Define if locked branches should be processed. Defaults to the tenant wide setting of exclude-locked-branches. This currently only affects GitHub projects.

tenant.untrusted-projects.<project>.include-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.include-branches "Link to this definition")

A list of regexes matching branches which should be processed. If omitted, all branches are included. Operates after _exclude-unprotected-branches_ and _exclude-locked-branches_ and so may be used to further reduce the set of branches (but not increase it).

It has priority over _exclude-branches_.

tenant.untrusted-projects.<project>.exclude-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude-branches "Link to this definition")

A list of regexes matching branches which should be processed. If omitted, all branches are included. Operates after _exclude-unprotected-branches_ and _exclude-locked-branches_ and so may be used to further reduce the set of branches (but not increase it).

It will not exclude a branch which already matched _include-branches_.

tenant.untrusted-projects.<project>.always-dynamic-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.always-dynamic-branches "Link to this definition")

A list of regular expressions matching branches which should be treated as if every change newly proposes dynamic Zuul configuration. In other words, the only time Zuul will realize any configuration related to these branches is during the time it is running jobs for a proposed change.

This is potentially useful for situations with large numbers of rarely used feature branches, but comes at the cost of a significant reduction in Zuul features for these branches.

Every regular expression listed here will also implicitly be included in _exclude-branches_, therefore Zuul will not load any static in-repo configuration from this branch. These branches will not be available for use in overriding checkouts of repos, nor will they be included in the git repos that Zuul prepares for _required-projects_ (unless there is a change in the dependency tree for this branch).

In particular, this means that the only jobs which can be specified for these branches are pre-merge and gating jobs (such as [check](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-check) and [gate](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-gate)). No post-merge or periodic jobs will run for these branches.

Using this setting also incurs additional processing for each change submitted for these branches as Zuul must recalculate the configuration layout it uses for such a change as if it included a change to a `zuul.yaml` file, even if the change does not alter the configuration).

With all these caveats in mind, this can be useful for repos with large numbers of rarely used branches as it allows Zuul to omit their configuration in most circumstances and only calculate the configuration of a single additional branch when it is used.

tenant.untrusted-projects.<project>.implied-branch-matchers[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.implied-branch-matchers "Link to this definition")

This is a boolean, which, if set, may be used to enable (`true`) or disable (`false`) the addition of implied branch matchers to job and project-template definitions. Normally Zuul decides whether to add these based on heuristics described in [job.branches](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.branches "attr-job.branches"). This attribute overrides that behavior.

This can be useful if branch settings for this project may produce an unpredictable number of branches to load from. Setting this value explicitly here can avoid unexpected behavior changes as branches are added or removed from the load set.

The [pragma.implied-branch-matchers](https://zuul-ci.org/docs/zuul/latest/config/pragma.html#attr-pragma.implied-branch-matchers "attr-pragma.implied-branch-matchers") pragma will override the setting here if present.

Note that if a job contains an explicit branch matcher, it will be used regardless of the value supplied here.

Normally Zuul loads in-repo configuration from the first of these paths:

*   zuul.yaml

*   zuul.d/*

*   .zuul.yaml

*   .zuul.d/*

If this option is supplied then, after the normal process completes, Zuul will also load any configuration found in the files or paths supplied here. This can be a string or a list. If a list of multiple items, Zuul will load configuration from _all_ of the items in the list (it will not stop at the first extra configuration found). Directories should be listed with a trailing `/`. Example:

extra-config-paths:
 - zuul-extra.yaml
 - zuul-extra.d/

This feature may be useful to allow a project that primarily holds shared jobs or roles to include additional in-repo configuration for its own testing (which may not be relevant to other users of the project).

tenant.untrusted-projects.<project>.allow-reporter-jobs[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.allow-reporter-jobs "Link to this definition")

Type:_bool_

Set to `true` to allow this project to configure [reporter](https://zuul-ci.org/docs/zuul/latest/config/job.html#value-job.type.reporter "value-job.type.reporter") jobs to run on its changes (or the changes of other projects it is permitted to configure via [tenant.untrusted-projects.<project>.configure-projects](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.configure-projects "attr-tenant.untrusted-projects.<project>.configure-projects")). This behavior is normally reserved for for [config projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project).

tenant.untrusted-projects.<project>.configure-projects[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.configure-projects "Link to this definition")

A list of project names (or [regular expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex) to match project names) that this project is permitted to configure. The use of this setting will allow this project to specify [project](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project "attr-project") stanzas that apply to untrusted-projects specified here. This is an advanced and potentially dangerous configuration setting since it would allow one project to cause another project to run certain jobs. This behavior is normally reserved for [config projects](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-config-project).

This should only be used in situations where there is a strong trust relationship between this project and the projects it is permitted to configure.

tenant.untrusted-projects.<project-group>[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject-group%3E "Link to this definition")

The items in the list are dictionaries with the following attributes. A **configuration items** definition is applied to the list of projects.

tenant.untrusted-projects.<project-group>.include[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject-group%3E.include "Link to this definition")

A list of **configuration items** that should be loaded.

tenant.untrusted-projects.<project-group>.exclude[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject-group%3E.exclude "Link to this definition")

A list of **configuration items** that should not be loaded.

tenant.untrusted-projects.<project-group>.projects[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject-group%3E.projects "Link to this definition")

A list of **project** items.

tenant.max-dependencies[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-dependencies "Link to this definition")

This setting can be used to limit the number of dependencies that Zuul will consider when enqueuing a change in any pipeline in this tenant. If used, it should be set to a value that is higher than the highest number of dependencies that are expected to be encountered. If, when enqueuing a change, Zuul detects that the dependencies will exceed this value, Zuul will not enqueue the change and will provide no feedback to the user. This is meant only to protect the Zuul server from resource exhaustion when excessive dependencies are present. The default (unset) is no limit. Note that the value `0` does not disable this option; instead it limits Zuul to zero dependencies. This is distinct from [<gerrit connection>.max_dependencies](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.max_dependencies "attr-<gerrit connection>.max_dependencies").

tenant.max-changes-per-pipeline[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-changes-per-pipeline "Link to this definition")

The number of changes (not queue items) allowed in any individual pipeline in this tenant. Live changes, non-live changes used for dependencies, and changes that are part of a dependency cycle are all counted. If a change appears in more than one queue item, it is counted multiple times.

For example, if this value was set to 100, then Zuul would allow any of the following (but no more):

*   100 changes in individual queue items

*   1 queue item of 100 changes in a dependency cycle

*   1 queue item with 99 changes in a cycle plus one item depending on that cycle

This counts changes across all queues in the pipeline; it is therefore possible for a set of projects in one queue to affect others in the same tenant.

This value is not set by default, which means there is no limit. It is generally expected that the pipeline window configuration should be sufficient to protect against excessive resource usage. However in some circumstances with large dependency cycles, setting this value may be useful. Note that the value `0` does not disable this option; instead it limits Zuul to zero changes.

tenant.max-nodes-per-job[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-nodes-per-job "Link to this definition")

Default:`5`

The maximum number of nodes a job can request. A value of ‘-1’ value removes the limit.

tenant.max-job-timeout[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-job-timeout "Link to this definition")

Default:`10800`

The maximum timeout for jobs. A value of ‘-1’ value removes the limit.

tenant.max-oidc-ttl[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-oidc-ttl "Link to this definition")

Default:`10800`

The maximum value that can be configured for the `ttl` attribute of an OpenID Connect (OIDC) secret in this tenant. It must be a positive integer.

tenant.default-oidc-ttl[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.default-oidc-ttl "Link to this definition")

Default:`3600`

The default `ttl` value for the ID tokens if not specified in the secret configuration. It must be a positive integer and not greater than [tenant.max-oidc-ttl](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-oidc-ttl "attr-tenant.max-oidc-ttl").

tenant.allowed-oidc-issuers[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-oidc-issuers "Link to this definition")

Default:`[]`

A list of allowed issuers that can override the `iss` claim in an OIDC token in this tenant.

tenant.exclude-unprotected-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.exclude-unprotected-branches "Link to this definition")

Default:`false`

When using a branch and pull model on a shared repository there are usually one or more protected branches which are gated and a dynamic number of personal/feature branches which are the source for the pull requests. These branches can potentially include broken Zuul config and therefore break the global tenant wide configuration. In order to deal with this Zuul’s operations can be limited to the protected branches which are gated. This is a tenant wide setting and can be overridden per project. This currently only affects GitHub and GitLab projects.

tenant.exclude-locked-branches[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.exclude-locked-branches "Link to this definition")

Default:`false`

Some code review systems support read-only, or “locked” branches. Enabling this setting will cause Zuul to ignore these branches. This is a tenant wide setting and can be overridden per project. This currently only affects GitHub and GitLab projects.

tenant.default-parent[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.default-parent "Link to this definition")

Default:`base`

If a job is defined without an explicit [job.parent](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.parent "attr-job.parent") attribute, this job will be configured as the job’s parent. This allows an administrator to configure a default base job to implement local policies such as node setup and artifact publishing.

tenant.default-ansible-version[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.default-ansible-version "Link to this definition")

Default ansible version to use for jobs that doesn’t specify a version. See [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version") for details.

tenant.allowed-triggers[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-triggers "Link to this definition")

Default:`all connections`

The list of connections a tenant can trigger from. When set, this setting can be used to restrict what connections a tenant can use as trigger. Without this setting, the tenant can use any connection as a trigger.

tenant.allowed-reporters[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-reporters "Link to this definition")

Default:`all connections`

The list of connections a tenant can report to. When set, this setting can be used to restrict what connections a tenant can use as reporter. Without this setting, the tenant can report to any connection.

tenant.allowed-labels[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-labels "Link to this definition")

Default:`[]`

Note

This option is only used with Nodepool. It is deprecated and will be removed in a future version of Zuul.

The list of labels (as strings or [regular expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex)) a tenant can use in a job’s nodeset. When set, this setting can be used to restrict what labels a tenant can use. Without this setting, the tenant can use any labels.

tenant.disallowed-labels[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.disallowed-labels "Link to this definition")

Default:`[]`

Note

This option is only used with Nodepool. It is deprecated and will be removed in a future version of Zuul.

The list of labels (as strings or [regular expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex)) a tenant is forbidden to use in a job’s nodeset. When set, this setting can be used to restrict what labels a tenant can use. Without this setting, the tenant can use any labels permitted by [tenant.allowed-labels](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-labels "attr-tenant.allowed-labels"). This check is applied after the check for allowed-labels and may therefore be used to further restrict the set of permitted labels.

tenant.web-root[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.web-root "Link to this definition")

If this tenant has a whitelabeled installation of zuul-web, set its externally visible URL here (e.g., `https://tenant.example.com/`). This will override the [web.root](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.root "attr-web.root") setting when constructing URLs for this tenant.

tenant.admin-rules[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.admin-rules "Link to this definition")

Note

This option is deprecated and will be removed in a future version of Zuul. See [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") instead.

A list of authorization rules to be checked in order to grant administrative access to the tenant through Zuul’s REST API and web interface.

At least one rule in the list must match for the user to be allowed to execute privileged actions. A matching rule will also allow the user access to the tenant in general (i.e., the rule does not need to be duplicated in access-rules).

More information on tenant-scoped actions can be found in [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html#authentication).

tenant.access-rules[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.access-rules "Link to this definition")

Note

This option is deprecated and will be removed in a future version of Zuul. See [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") instead.

A list of authorization rules to be checked in order to grant read access to the tenant through Zuul’s REST API and web interface.

If no rules are listed, then anonymous access to the tenant is permitted. If any rules are present then at least one rule in the list must match for the user to be allowed to access the tenant.

More information on tenant-scoped actions can be found in [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html#authentication).

tenant.anonymous-read-access[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.anonymous-read-access "Link to this definition")

Default:`true`

Whether anonymous users are permitted read access to this tenant. If this is set to `false` then at least one entry must appear in [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") in order to grant the `read` permission.

tenant.role-mappings[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "Link to this definition")

A dictionary that maps [authorization-rule](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-authorization-rule "attr-authorization-rule") entries to one or more [role](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role "attr-role") entries. For example:

- authorization-rule:
 name: admin-user
 conditions:
 - preferred_username: admin

- authorization-rule:
 name: alice
 conditions:
 - preferred_username: alice

- authorization-rule:
 name: everyone
 conditions:
 - iss: our-institution

- role:
 name: autohold
 permissions:
 autohold: true

- role:
 name: enqueue-post
 permissions:
 enqueue:
 conditions:
 project: foo

- tenant:
 name: example
 anonymous-read-access: false
 role-mappings:
 admin-user: admin
 everyone: [read, autohold]
 alice: enqueue-post

This indicates that the admin (identified by the admin-user rule) has full administrative access (granted via the built-in admin role); all authenticated users have permissions to read and set autoholds (via the built-in read role, and the autohold role defined above); and alice additionally has permissions to enqueue items for the foo project in the post pipeline.

If any role-mappings are provided, then [tenant.admin-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.admin-rules "attr-tenant.admin-rules") and [tenant.access-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.access-rules "attr-tenant.access-rules") are disregarded.

See also [tenant.anonymous-read-access](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.anonymous-read-access "attr-tenant.anonymous-read-access") for configuring read access.

tenant.authentication-realm[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.authentication-realm "Link to this definition")

Each authenticator defined in Zuul’s configuration is associated to a realm. When authenticating through Zuul’s Web User Interface under this tenant, the Web UI will redirect the user to this realm’s authentication service. The authenticator must be of the type `OpenIDConnect`.

Note

Defining a default realm for a tenant will not invalidate access tokens issued from other configured realms. This is intended so that an operator can issue an overriding access token manually. If this is an issue, it is advised to add finer filtering to admin rules, for example, filtering by the `iss` claim (generally equal to the issuer ID).

tenant.semaphores[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.semaphores "Link to this definition")

A list of names of [global-semaphore](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-global-semaphore "attr-global-semaphore") objects to allow jobs in this tenant to access.

tenant.use-nodepool[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.use-nodepool "Link to this definition")

Default:`true`

Once a tenant has been migrated to use zuul-launcher instead of Nodepool, set this value to `false` in order to disable the Nodepool label fallback behavior. This is important since, with no Nodepool running, Zuul needs to know that any requests for nonexistent labels should be declined.

Global Semaphore[](https://zuul-ci.org/docs/zuul/latest/tenants.html#global-semaphore "Link to this heading")
--------------------------------------------------------------------------------------------------------------

Semaphores are normally defined in in-repo configuration (see [Semaphore](https://zuul-ci.org/docs/zuul/latest/config/semaphore.html#semaphore)), however to support use-cases where semaphores are used to represent constrained global resources that may be used by multiple Zuul tenants, semaphores may be defined within the main tenant configuration file.

In order for a job to use a global semaphore, the semaphore must first be defined in the tenant configuration file with [global-semaphore](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-global-semaphore "attr-global-semaphore") and then added to each tenant which should have access to it with [tenant.semaphores](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.semaphores "attr-tenant.semaphores"). Once that is done, Zuul jobs may use that semaphore in the same way they would use a normal tenant-scoped semaphore.

If any tenant which is granted access to a global semaphore also has a tenant-scoped semaphore defined with the same name, that definition will be treated as a configuration error and subsequently ignored in favor of the global semaphore.

An example definition looks similar to the normal semaphore object:

- global-semaphore:
 name: global-semaphore-foo
 max: 5

global-semaphore[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-global-semaphore "Link to this definition")

The following attributes are available:

global-semaphore.name(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-global-semaphore.name "Link to this definition")

The name of the semaphore, referenced by jobs.

global-semaphore.max[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-global-semaphore.max "Link to this definition")

Default:`1`

The maximum number of running jobs which can use this semaphore.

Authorization Rule[](https://zuul-ci.org/docs/zuul/latest/tenants.html#authorization-rule "Link to this heading")
------------------------------------------------------------------------------------------------------------------

An authorization rule is a set of conditions the claims of a user’s JWT must match in order to be allowed to perform actions at a tenant’s level.

Authorization rules may be used with the deprecated [tenant.admin-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.admin-rules "attr-tenant.admin-rules") system, in which case they grant all permissions, or via the newer [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") system, in which case they may be used to grant fine-grained permissions.

Note

Rules can be overridden by the `zuul.admin` claim in a token if if matches an authenticator configuration where allow_authz_override is set to true. See [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html#authentication) for more details.

Below are some examples of how authorization rules can be defined:

- authorization-rule:
 name: affiliate_or_admin
 conditions:
 - resources_access:
 account:
 roles: "affiliate"
 iss: external_institution
 - resources_access.account.roles: "admin"
- authorization-rule:
 name: alice_or_bob
 conditions:
 - zuul_uid: alice
 - zuul_uid: bob

Zuul previously used `admin-rule` for these definitions. That form is still permitted for backwards compatibility, but is deprecated and will be removed in a future version of Zuul.

The following attributes are supported:

authorization-rule.name(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-authorization-rule.name "Link to this definition")

The name of the rule, so that it can be referenced in the tenant’s definition. It must be unique.

authorization-rule.conditions(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-authorization-rule.conditions "Link to this definition")

This is the list of conditions that define a rule. A JWT must match **at least one** of the conditions for the rule to apply. A condition is a dictionary where keys are claims. **All** the associated values must match the claims in the user’s token; in other words the condition dictionary must be a “sub-dictionary” of the user’s JWT.

Zuul’s authorization engine will adapt matching tests depending on the nature of the claim in the token, eg:

*   if the claim is a JSON list, check that the condition value is in the claim

*   if the claim is a string or a boolean, check that the condition value is equal to the claim’s value

The claim names can also be written in the XPath format for clarity: the condition

resources_access:
 account:
 roles: "affiliate"

is equivalent to the condition

resources_access.account.roles: "affiliate"

The special `zuul_uid` claim refers to the `uid_claim` setting in an authenticator’s configuration. By default it refers to the `sub` claim of a token. For more details see the [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html#authentication).

Under the above example, the following token would match rules `affiliate_or_admin` and `alice_or_bob`:

{
 'iss': 'external_institution',
 'aud': 'my_zuul_deployment',
 'exp': 1234567890,
 'iat': 1234556780,
 'sub': 'alice',
 'resources_access': {
 'account': {
 'roles': ['affiliate', 'other_role']
 }
 },
}

And this token would only match rule `affiliate_or_admin`:

{
 'iss': 'some_other_institution',
 'aud': 'my_zuul_deployment',
 'exp': 1234567890,
 'sub': 'carol',
 'iat': 1234556780,
 'resources_access': {
 'account': {
 'roles': ['admin', 'other_role']
 }
 },
}

Authorization Rule Templating[](https://zuul-ci.org/docs/zuul/latest/tenants.html#authorization-rule-templating "Link to this heading")
----------------------------------------------------------------------------------------------------------------------------------------

The special word “{tenant.name}” can be used in conditions’ values. It will be automatically substituted for the relevant tenant when evaluating authorizations for a given set of claims. For example, consider the following rule:

- authorization-rule:
 name: tenant_in_groups
 conditions:
 - groups: "{tenant.name}"

If applied to the following tenants:

- tenant:
 name: tenant-one
 admin-rules:
 - tenant_in_groups
- tenant:
 name: tenant-two
 admin-rules:
 - tenant_in_groups

Then this set of claims will be allowed to perform protected actions on **tenant-one**:

{
 'iss': 'some_other_institution',
 'aud': 'my_zuul_deployment',
 'exp': 1234567890,
 'sub': 'carol',
 'iat': 1234556780,
 'groups': ['tenant-one', 'some-other-group'],
}

And this set of claims will be allowed to perform protected actions on **tenant-one** and **tenant-two**:

{
 'iss': 'some_other_institution',
 'aud': 'my_zuul_deployment',
 'exp': 1234567890,
 'sub': 'carol',
 'iat': 1234556780,
 'groups': ['tenant-one', 'tenant-two'],
}

Role[](https://zuul-ci.org/docs/zuul/latest/tenants.html#role "Link to this heading")
--------------------------------------------------------------------------------------

A role is used in conjunction with [authorization-rule](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-authorization-rule "attr-authorization-rule") and [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") to specify fine-grained permissions for use with authorization.

Zuul contains two built-in roles: `admin` which always grants all permissions (and will continue to do so as new permissions are added in the future), and `read` which grants only the `read` permission.

role[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role "Link to this definition")

The following attributes are supported:

role.name(required)[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.name "Link to this definition")

The name of the role, so that it can be referenced in the tenant’s definition. It must be unique.

role.permissions[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions "Link to this definition")

A dictionary where keys are the names of permissions and the values are either `true` to grant that permission, or a dictionary of conditions that the request must match in order to grant the permission.

role.permissions.read[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.read "Link to this definition")

Type:_bool_

Grant read access to the tenant. This is only effective if [tenant.anonymous-read-access](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.anonymous-read-access "attr-tenant.anonymous-read-access") is set to false. In that case, either the built-in `read` role, or a user-defined role with the `read` permission must be used.

Setting this value to `False` may not be effective.

role.permissions.promote[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.promote "Link to this definition")

Type:_bool_

Permission to promote items in any pipeline. Only accepts a boolean value.

role.permissions.set-tenant-state[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.set-tenant-state "Link to this definition")

Type:_bool_

Permission to modify the tenant state (such as disabling event processing). Only accepts a boolean value.

role.permissions.build-image[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.build-image "Link to this definition")

Type:_bool_

Permission to build any image in the tenant. Only accepts a boolean value.

role.permissions.upload-image[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.upload-image "Link to this definition")

Type:_bool_

Permission to upload any image in the tenant. Only accepts a boolean value.

role.permissions.delete-image-build-artifact[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.delete-image-build-artifact "Link to this definition")

Type:_bool_

Permission to delete any image build artifact in the tenant. Only accepts a boolean value.

role.permissions.delete-image-upload[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.delete-image-upload "Link to this definition")

Type:_bool_

Permission to delete any image upload in the tenant. Only accepts a boolean value.

role.permissions.validate-image-upload[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.validate-image-upload "Link to this definition")

Type:_bool_

Permission to validate any image upload in the tenant. Only accepts a boolean value.

role.permissions.modify-node[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.modify-node "Link to this definition")

Type:_bool_

Permission to modify any node in the tenant. Only accepts a boolean value.

role.permissions.modify-nodeset-request[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.modify-nodeset-request "Link to this definition")

Type:_bool_

Permission to modify any nodeset request in the tenant. Only accepts a boolean value.

role.permissions.autohold[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.autohold "Link to this definition")

Type:_bool_

Permission to create or delete any autohold in the tenant. Only accepts a boolean value.

role.permissions.dequeue[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.dequeue "Link to this definition")

Type:_boolean or dict_

Permission to dequeue a change. If set to `true`, permission is granted to dequeue any change.

role.permissions.dequeue.conditions[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.dequeue.conditions "Link to this definition")

Type:_dict_

Further conditions may be applied with the following attributes:

role.permissions.dequeue.conditions.project[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.dequeue.conditions.project "Link to this definition")

The name of a project.

role.permissions.dequeue.conditions.ref[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.dequeue.conditions.ref "Link to this definition")

The name of a ref (e.g., refs/heads/stable).

role.permissions.enqueue[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.enqueue "Link to this definition")

Type:_boolean or dict_

Permission to enqueue a change. If set to `true`, permission is granted to enqueue any change.

role.permissions.enqueue.conditions[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.enqueue.conditions "Link to this definition")

Type:_dict_

Further conditions may be applied with the following attributes:

role.permissions.enqueue.conditions.project[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.enqueue.conditions.project "Link to this definition")

The name of a project.

role.permissions.enqueue.conditions.ref[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role.permissions.enqueue.conditions.ref "Link to this definition")

The name of a ref (e.g., refs/heads/stable).

API Root[](https://zuul-ci.org/docs/zuul/latest/tenants.html#api-root "Link to this heading")
----------------------------------------------------------------------------------------------

Most actions in zuul-web, zuul-client, and the REST API are understood to be within the context of a specific tenant and therefore the authorization rules specified by that tenant apply. When zuul-web is deployed in a multi-tenant scenario (the default), there are a few extra actions or API methods which are outside of the context of an individual tenant (for example, listing the tenants or observing the state of Zuul system components). To control access to these methods, an api-root object can be used.

At most one api-root object may appear in the tenant configuration file. If more than one appears, it is an error. If there is no api-root object, then anonymous read-only access to the tenant list and other root-level API methods is assumed.

The `/api/info` endpoint is never protected by Zuul since it supplies the authentication information needed by the web UI.

API root access is not a pre-requisite to access tenant-specific URLs.

api-root[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-api-root "Link to this definition")

The following attributes are supported:

api-root.authentication-realm[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-api-root.authentication-realm "Link to this definition")

Each authenticator defined in Zuul’s configuration is associated to a realm. When authenticating through Zuul’s Web User Interface at the multi-tenant root, the Web UI will redirect the user to this realm’s authentication service. The authenticator must be of the type `OpenIDConnect`.

Note

Defining a default realm for the root API will not invalidate access tokens issued from other configured realms. This is intended so that an operator can issue an overriding access token manually. If this is an issue, it is advised to add finer filtering to admin rules, for example, filtering by the `iss` claim (generally equal to the issuer ID).

api-root.access-rules[](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-api-root.access-rules "Link to this definition")

A list of authorization rules to be checked in order to grant read access to the top-level (i.e., non-tenant-specific) portion of Zuul’s REST API and web interface.

If no rules are listed, then anonymous access to top-level methods is permitted. If any rules are present then at at least one rule in the list must match for the user to be allowed access.

More information on tenant-scoped actions can be found in [Authenticated Access](https://zuul-ci.org/docs/zuul/latest/authentication.html#authentication).
