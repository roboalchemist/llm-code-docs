# Source: https://zuul-ci.org/docs/zuul/latest/releasenotes.html

Title: Release Notes — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/releasenotes.html

Markdown Content:
In Development[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#in-development "Link to this heading")
---------------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#new-features "Link to this heading")

*   The GitHub driver now supports the ability to restrict triggers to actions perfomed by accounts with certain access levels. See [pipeline.trigger.<github source>.permission](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.permission "attr-pipeline.trigger.<github source>.permission").

*   A new label attribute, [label.max-nodes](https://zuul-ci.org/docs/zuul/latest/config/label.html#attr-label.max-nodes "attr-label.max-nodes") is available to limit the number of nodes of that label available in each tenant in which it appears.

*   Fine-grained role-based access control for the API and web UI is available using the new [role](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-role "attr-role") definition and related constructs in the tenant config file.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#upgrade-notes "Link to this heading")

*   The min-ready setting on labels is now only available for top-level label objects and may not be set within a provider or section stanza.

*   The URLs used when Zuul acts as an OpenID Connect provider are changing.

The OpenID configuration URL, zuul.example.com/.well-known/openid-configuration, will remain the same. It was possible to access this data through other URLs; doing so was incorrect and probably did not work. Anything other than this URL is considered deprecated.

The URL serving the OpenID keys is changing to zuul.example.com/oidc/jwks. Other URLs for this endpoint are considered deprecated. With this version, Zuul will report that URL as the key endpoint in the OpenId configuration, so if proxy configuration is required for access, that change must be made before upgrade. Old URLs will continue to work for this version of Zuul to facilitate continued operation during the upgrade, but will be removed in the next version of Zuul.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#deprecation-notes "Link to this heading")

*   The [tenant.admin-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.admin-rules "attr-tenant.admin-rules") and [tenant.access-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.access-rules "attr-tenant.access-rules") attributes are now deprecated in favor of the new [tenant.role-mappings](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.role-mappings "attr-tenant.role-mappings") attribute.

14.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0-new-features "Link to this heading")

*   Jobs may now filter the non-required projects for their workspace. If a job is known to only operate on a certain set of projects, the [job.include-projects](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.include-projects "attr-job.include-projects") and [job.exclude-projects](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.exclude-projects "attr-job.exclude-projects") attributes may be used to instruct Zuul to skip the workspace preparation of projects that are not required by the job.

*   A new component, the Zuul [Launcher](https://zuul-ci.org/docs/zuul/latest/configuration.html#launcher), is available. Zuul-launcher is responsible for managing images and build nodes, and replaces Nodepool. Zuul supports both systems simultaneously for transitional purposes.

See [Build Nodes](https://zuul-ci.org/docs/zuul/latest/build-nodes.html#build-nodes) for an overview of the new system and information about migrating.

*   A new type of job, a “reporter” job is available. It allows users to perform an action immediately after all pipeline reporters have run for a queue item. The configuration attribute, [job.type](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.type "attr-job.type") is used to enable the feature.

*   A change has been made to the branch selection routine for role repo checkouts in jobs triggered by tags.

Previously, when checking out a role repo for a tag job, Zuul would check out the first match of the following:

> *   The project override-checkout
> 
>     *   The job override-checkout
> 
>     *   If the role project is the playbook project, then the playbook project branch
> 
>     *   The role project default branch

It is now updated to the following:

> *   The project override-checkout
> 
>     *   The job override-checkout
> 
>     *   The playbook project branch
> 
>     *   The role project default branch

This may be a change for certain jobs, but it is hoped that the new sequence is more intuitive.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-14-0-0-deprecation-notes "Link to this heading")

*   The Zuul job variables [zuul.build_refs.project.src_dir](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.build_refs.project.src_dir "var-zuul.build_refs.project.src_dir") and [zuul.buildset_refs.project.src_dir](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.buildset_refs.project.src_dir "var-zuul.buildset_refs.project.src_dir") were erroneously supplied as `zuul.build_refs.src_dir` and `zuul.buildset_refs.src_dir` respectively. The correct variables are now supplied, and any usages of the old, incorrect variables should be replaced. The old variables will be removed in a future version of Zuul.

*   The use of Nodepool is now deprecated. Support will be removed in a future version of Zuul (after a generous period where both Nodepool and Zuul-launcher are supported).

13.1.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#security-issues "Link to this heading")

*   A vulnerability in the zuul-web component could be used to obtain the contents of any file accessible on the zuul-web server (or within its container). The vulnerability is believed to have been present prior to version 4 of Zuul, and has been corrected as of version 13.1.0.

13.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0-new-features "Link to this heading")

*   A new configuration setting, `replication_delay` has been added to the Gerrit driver. Some Gerrit installations consist of multiple servers with various strategies for keeping these servers in sync (push replication, pull replication, multi-master, shared storage, etc.). Since there is currently no reliable method to determine when all servers are updated, this setting may be used to introduce a delay in event processing. Zuul will ensure that at least this amount of time (in seconds) has passed before processing the corresponding event.

*   The [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check") attribute now accepts the value of [queued](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.queued "value-pipeline.<reporter>.<github source>.check.queued") to indicate that a pull request has been enqueued into a pipeline.

*   Added support for the branch attribute in GitLab pipeline configurations triggered by merge_request events. This enables pipelines to run only for specific branches, providing precise control over branch-specific behavior.

*   A new type of job, an “initializer” job is available. It allows users to easily configure very large job graphs where all the jobs in the graph have dependencies on a single (or small number) of jobs. The configuration attribute, [job.type](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.type "attr-job.type") is available to enable the feature.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-1-0-deprecation-notes "Link to this heading")

*   The `replication_timeout` setting for the Gerrit driver is now ignored and should be removed from `zuul.conf` files. See the new `replication_delay` setting for an alternative.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#bug-fixes "Link to this heading")

*   Zuul will now record a notice in the job-output.json for Ansible playbooks that fail to do so themselves. This can happen if Ansible crashes or is forced to stop by Zuul due to timeouts. The information is minimal, but should give users an indication in the web ui console of why certain plays are not recorded.

13.0.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1-security-issues "Link to this heading")

*   Streaming log handling for the `win_command` and `win_shell` modules did not correctly observe the `no_log` directive. Previously Zuul would suppress output to the `job-output.json` file, but not output to `job-output.txt` or live log streams.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-1-bug-fixes "Link to this heading")

*   The Zuul module for ansible.builtin.command and ansible.builtin.shell now correctly handles the case when no_log: True is set. Previously the task would deadlock if the process output filled the buffer.

13.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0-new-features "Link to this heading")

*   Ansible version 11 is now available. The default Ansible version is still 9, but version 11 may be selected by using [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

*   The [authorization-rule.conditions](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-authorization-rule.conditions "attr-authorization-rule.conditions") attribute can now include conditions for boolean claims.

*   Implemented support for the reject attribute in the GitLab driver. It allows specifying Merge Requests which should not be enqueued into a pipeline. The supported conditions cover the same Merge Requests’ parameters as available in the existing require attribute – filtering whether the Merge Request must (not) be open, merged, approved or contain some labels.

*   If a change alters a file in an [job.include-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.include-vars "attr-job.include-vars"), [job.pre-run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.pre-run "attr-job.pre-run"), [job.run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.run "attr-job.run"), or [job.post-run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.post-run "attr-job.post-run") attribute of a job, then that job will run regardless of any file matchers configured on the job (unless [job.match-on-config-updates](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.match-on-config-updates "attr-job.match-on-config-updates") is disabled).

This means that jobs with file matchers should no longer need to explicitly list their playbooks or include-vars files in order to run on changes to those files.

*   The [nodeset.alternatives](https://zuul-ci.org/docs/zuul/latest/config/nodeset.html#attr-nodeset.alternatives "attr-nodeset.alternatives") feature will now be used if Ansible reports an unreachable host while running a job. This can be used to fall back to a more reliable nodeset if connectivity to the nodeset is interrupted while running.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-13-0-0-upgrade-notes "Link to this heading")

*   Support for Ansible version 8 has been removed. Migrate any existing jobs which rely on this version to Ansible version 9 before upgrading.

*   The previously deprecated `status-url` attribute of the Github and Pagure reporter has been removed.

12.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-1-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-1-0-new-features "Link to this heading")

*   Added support for OpenID Connect (OIDC) compatible workload identity federation. When configured using [secret.oidc](https://zuul-ci.org/docs/zuul/latest/config/secret.html#attr-secret.oidc "attr-secret.oidc"), Zuul will generate an OIDC ID token and supply it to the job, which can be used to authenticate to external services that trust Zuul as an OIDC Identity Provider. See [Secret](https://zuul-ci.org/docs/zuul/latest/config/secret.html#secret) for more information.

*   An option has been added to allow multiple timer-triggered queue items for the same project-branch may now be enqueued if the branch head has advanced.

Previously timer-triggered items only included information about the project and branch, and therefore if a job on such an item ran longer than the timer interval, Zuul would not enqueue a second copy of the item because it would have been seen as identical to the first (even if the underlying repo had changed.

If the new `dereference` attribute of the timer trigger is set, Zuul will now include information about the branch head SHA of the queue item, so that now if a timer trigger fires while a queue item for the same project-branch is already in the queue, the second item will be enqueued if the branch has changed since the first item was enqueued. If the SHA of the branch head is the same for both items, the second item will not be enqueued.

When set, the `newrev` is now available in the job’s `zuul` variables for such queue items.

The previous behavior remains the default, where derefence is not set, and `newrev` is not available.

*   Most pipeline triggers now accept a `debug` attribute which may be used to add a trigger to allow users to request extra debug information about why a change may or may not have been enqueued into a pipeline and why certain jobs ran or did not run.

For example, a site may add a trigger that matches the comment “check debug” to request an expanded report on a change.

*   Tenant administrators may now use the web UI or zuul-client commands to pause and unpause event processing for a tenant.

12.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-new-features "Link to this heading")

*   Jobs now have the ability to set a [job.pre-timeout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.pre-timeout "attr-job.pre-timeout") value. This timeout limits the amount of time that pre-run playbooks may consume. This timeout counts against the normal [job.timeout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.timeout "attr-job.timeout") value and if [job.pre-timeout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.pre-timeout "attr-job.pre-timeout") is unset then [job.timeout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.timeout "attr-job.timeout") is used.

*   The Zuul Executor has a new governor sensor that detects when the Executor is nearing the limit on new processes. Running Zuul jobs in the Executor requires a number of process including but not limited to: Bubblewrap, Ansible, SSH, and SSH Agent. This new governor sensor helps to avoid jobs failing due to an inability to fork one of these many processes. Instead the Executor will pause its efforts until it backs away from the process limit.

*   Live console log streaming is now available for 
```
win_shell` and
``win_command
```
 tasks on Windows hosts.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-upgrade-notes "Link to this heading")

*   When using Zuul with a MariaDB database, configure the [database.dburi](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-database.dburi "attr-database.dburi") setting to use the `mariadb` dialect with `mariadb+pymysql://`.

*   The web.status_url configuration option is no longer supported and using the status_url, change and changes string substitutions in pipeline reporter messages will result in an error.

*   Due to the addition of live console log streaming for Windows hosts, one of the following is necessary:

> *   Add the `zuul_win_console:` task to the first pre-run playbook in a base job for Windows hosts, and allow connections to port 19886 on the hosts. This will allow for automatic live log streaming in the same manner as under Posix systems.
> 
>     *   If the above is not practical on long-lived Windows hosts, set `zuul_console_disabled: True` for those hosts. This will disable writing console output to spool files on the remote hosts which would otherwise not be deleted.

Note that the Posix and Windows log streaming servers operate on different ports (19885 and 19886 respectively) in order to allow both to coexist on the same host.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-12-0-0-bug-fixes "Link to this heading")

*   Job json API responses now include the [job.post-timeout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.post-timeout "attr-job.post-timeout") configuration value for the job.

11.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0-new-features "Link to this heading")

*   Individual attributes of jobs may now be marked as final so that any attempt to override that attribute will cause an error. See [job.attribute-control](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.attribute-control "attr-job.attribute-control").

*   Zuul will now run any job that is a hard dependency of a job that is set to run.

Previously if job B had a hard dependency on job A, and job A did not run due to a file matcher, Zuul would report an error. Now it will instead ignore the file matcher on job A as long as job B is to be run.

This will allow for simpler file matchers, more intuitive behavior, and enable a new pattern for job graphs where job A might have a file matcher that never matches, but job B will cause it to run regardless.

*   A new options, [job.workspace-checkout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.workspace-checkout "attr-job.workspace-checkout") is available to disable checkouts of repositories on the Zuul executor. This may be useful to save time or space when preparing large repositories which will be unused on the executor.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-3-0-upgrade-notes "Link to this heading")

*   The Gerrit driver now has an additional option, [pipeline.reporter.<gerrit reporter>.notify](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reporter.%3Cgerrit%20reporter%3E.notify "attr-pipeline.reporter.<gerrit reporter>.notify") which configures the notification handling of reviews as noted in the [Gerrit changes API Docs](https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#review-input). used to suppress reporting job results as review comments. Due to the configuration syntax for Gerrit reporters, the word “notify” may no longer be used as a review label.

*   The maximum combined stdout and stderr output from a single Ansible task has been limited to 1GiB. In the unlikely event that an existing job legitimately exceeds this limit, a new executor configuration option, [executor.output_max_bytes](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.output_max_bytes "attr-executor.output_max_bytes"), has been provided to temporarily increase the limit. This option is likely to be removed in a future version of Zuul. To avoid this issue, Ansible tasks with large volumes of output should be adjusted to redirect that output to a file which is separately collected and processed.

*   Schedulers will no longer trigger a smart-reconfig after startup and with that also not pick up modifications to the local tenant config and system attributes in the zuul config file with a restart of a scheduler. This means that changes to the tenant config or the zuul config always require an explicit (smart) reconfiguration.

11.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0-new-features "Link to this heading")

*   The [project.<pipeline>.fail-fast](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.%3Cpipeline%3E.fail-fast "attr-project.<pipeline>.fail-fast") attribute now also applies to node failures of voting jobs.

*   Jobs may now read variables from an in-repo file using the [job.include-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.include-vars "attr-job.include-vars") job attribute. This allows jobs with many (or frequently changing) variables to load their variables from a file in order to reduce the complexity of Zuul configuration. Because these files are read when the job is executed, changes to their values will not cause Zuul tenant reconfigurations.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-2-0-upgrade-notes "Link to this heading")

*   Ansible version 8 is now deprecated in Zuul since it is unmaintaned, and it will be removed from a future version of Zuul. Ansible 9 is now the default version in Zuul.

*   Github Enterprise versions older than 2.21 are not supported.

*   Include-vars behavior has changed when running on tags. Previously, the use of [job.include-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.include-vars "attr-job.include-vars") in a job that ran on a ref (i.e., tag or branch rather than a change) would use either the override-checkout or the project default branch to source the variables file. In the case that the job is running on a ref of the include-vars project, it will now source the file from the ref checkout itself; this is expected to be more useful and intuitive for users. To restore the previous behavior, the [job.include-vars.use-ref](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.include-vars.use-ref "attr-job.include-vars.use-ref") may be used.

11.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-new-features "Link to this heading")

*   Untrusted projects may now be allowed (via explicit configuration in the tenant config file) to configure jobs that are run by certain specified other untrusted projects. This allows a “super-project” to configure the jobs run by its “sub-projects”.

See [tenant.untrusted-projects.<project>.configure-projects](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.configure-projects "attr-tenant.untrusted-projects.<project>.configure-projects") for details.

*   Project stanzas may now include an explicit branch configuration via the [project.branches](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.branches "attr-project.branches") attribute. This enables projects that configure other projects (whether the configuring projects are trusted or untrusted) to better control what jobs run on certain branches.

*   The tenant configuration may now specify the maximum number of changes that should be enqueued in a pipeline in order to protect Zuul from resource exhaustion. This is not necessary in most circumstances, so the default remains no limit.

*   Several job attributes may now have their inheritance behavior changed through “override control”. This introduces two new YAML tags, `!override` and `!inherit` which may be used to explicitly specify whether certain job attributes should inherit values from parent jobs or override them.

See the general job documentation at [Job](https://zuul-ci.org/docs/zuul/latest/config/job.html#job) and also documentation for the following individual attributes:

> *   [job.dependencies](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.dependencies "attr-job.dependencies")
> 
>     *   [job.extra-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.extra-vars "attr-job.extra-vars")
> 
>     *   [job.failure-output](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.failure-output "attr-job.failure-output")
> 
>     *   [job.files](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.files "attr-job.files")
> 
>     *   [job.group-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.group-vars "attr-job.group-vars")
> 
>     *   [job.host-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.host-vars "attr-job.host-vars")
> 
>     *   [job.irrelevant-files](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.irrelevant-files "attr-job.irrelevant-files")
> 
>     *   [job.provides](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.provides "attr-job.provides")
> 
>     *   [job.required-projects](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.required-projects "attr-job.required-projects")
> 
>     *   [job.requires](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.requires "attr-job.requires")
> 
>     *   [job.tags](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.tags "attr-job.tags")
> 
>     *   [job.vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.vars "attr-job.vars")

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-deprecation-notes "Link to this heading")

*   The `status-url` attribute of the Github and Pagure reporter is deprecated. Reporters will currently ignore this setting and automatically use the best URL for information about the item instead.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-1-0-bug-fixes "Link to this heading")

*   The zuul_return Ansible plugin will now validate the schema of the data supplied to it; particularly the data for warnings and artifacts. Previously the behavior on incorrectly structured data was undefined and ranged from being silently ignorred to causing exceptions in pipeline processing. Data format errors will now be detected while the job is running and will cause Ansible errors and (if not ignored) job failures.

11.0.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-1-bug-fixes "Link to this heading")

*   The recent security fix to run cleanup-run playbooks interleaved with post-run playbooks incorrectly caused jobs to retry if a cleanup playbook encountered an unreachable host. This has been corrected and a cleanup playbook will never cause a job to retry if it encounters an unreachable host.

11.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-upgrade-notes "Link to this heading")

*   Existing cleanup-run playbooks are now executed during the post-run phase of the job. This is a change in behavior that will run playbooks in a different order than before. Previously all cleanup-run playbooks would run after all post-run playbooks. Zuul will now run post-run, then cleanup-run playbooks at each level of the inheritance hierarchy (interleaving post-run and cleanup-run playbooks from different levels of the hierarchy).

Note that this may have an impact on some jobs. In particular, be on the lookout for jobs with post-run playbooks that assume that other, more-nested, post-run playbooks always run (for example, log collection playbooks). Ensure that log collection happens no more nested than at the job level where logs are created. Also be aware of cleanup-run playbooks that remove artifacts required by post-run playbooks. Since more-nested cleanup-run playbooks can now run before less-nested post-run playbooks, it may be necessary to move cleanup actions to less-nested levels.

To facilitate upgrades, Zuul will ignore the result of cleanup-run playbooks when specified using the old syntax, but once migrated to the new syntax using post-run, these playbooks may cause a POST_FAILURE just like any other post-run playbook.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-deprecation-notes "Link to this heading")

*   The [job.cleanup-run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.cleanup-run "attr-job.cleanup-run") attribute is deprecated. Instead, list cleanup playbooks under [job.post-run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.post-run "attr-job.post-run") and set the [job.post-run.cleanup](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.post-run.cleanup "attr-job.post-run.cleanup") flag.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-11-0-0-security-issues "Link to this heading")

*   A vulnerability was discovered which could potentially allow jobs with a malicious cleanup-run playbook to access the credentials of their parents or the nodepool ssh key.

To protect against this, cleanup-run playbooks are now executed during the post-run phase of the job, and Zuul will only execute the post-run playbooks corresponding to the inheritance level of previously-executed pre-run playbooks.

10.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-new-features "Link to this heading")

*   A new job variable, [zuul.build_refs](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.build_refs "var-zuul.build_refs"), is available to indicate for which particular refs in a circular dependency queue item a deduplicated job is being run.

*   The scheduler now accepts the argument `--disable-pipelines` which will instruct it to discard all pipeline events. This facilitaties the creation of a system with a running Zuul config that does not start any jobs or make any reports.

*   The gerrit driver now supports a new synthetic trigger, [pipeline.trigger.<gerrit source>.approval-change](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.approval-change "attr-pipeline.trigger.<gerrit source>.approval-change"). This is similar to approval, but only triggers when the value of the approval changes instead of simply being present.

*   gitlab driver now handles the merge request ‘close’ action.

*   The GitHub driver now supports excluding locked (read-only) branches with the exclude-locked-branches tenant configuration setting.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-deprecation-notes "Link to this heading")

*   The replacement fields `change`, `changes`, and `status_url` available in some pipeline reporter configurations are deprecated. Use `item_url`, which is automatically the best URL for information about the item instead.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-2-0-bug-fixes "Link to this heading")

*   The pseudo-file “/COMMIT_MSG” is not considered at all when determining whether a change matches files or irrelevant-files matchers. It was previously not considered in most cases, but in the case of a negated regular expression in an irrelevant-files stanza, it could still have an effect. This has been corrected and any regexes that explicitly mention “/COMMIT_MSG” may remove it.

*   The [job.files](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.files "attr-job.files") and [job.irrelevant-files](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.irrelevant-files "attr-job.irrelevant-files") attributes now fully support the new [regular expression](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex) syntax, including negation.

### Other Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#other-notes "Link to this heading")

*   Zuul now checks the submitWholeTopic setting in Gerrit when it starts. If this setting is changed, or Gerrit is upgraded, all running Zuul schedulers should be restarted in order to see the change.

10.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-new-features "Link to this heading")

*   The executor now monitors filesystem inode usage as well as storage usage. The threshold for accepting jobs can be configured independenty with [executor.min_avail_inodes](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.min_avail_inodes "attr-executor.min_avail_inodes"). Inode usage is also reported separately with the [zuul.executor.<executor>.pct_used_inodes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pct_used_inodes "stat-zuul.executor.<executor>.pct_used_inodes") metric.

*   The topic of a change (if any) is now reported in the [zuul.topic](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.topic "var-zuul.topic") job variable

*   Zuul now supports substring searches on the Builds and Buildsets pages on its web UI. This is supported by placing asterisk (*) placeholders anywhere in the search term, representing any characters. This is enabled for job name, branch, project, and pipeline filters.

*   Information about all of the changes (refs) associated with a circular dependency queue item is now available in the [zuul.buildset_refs](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.buildset_refs "var-zuul.buildset_refs") variable.

*   When a remote host in a job is found to be unreachable, Zuul will automatically add it to a new group named zuul_unreachable for all subsequent playbooks. This can be used to avoid running certain post-run steps on hosts already known to be unreachable.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-deprecation-notes "Link to this heading")

*   Specifying [pipeline.trigger.<github source>.event](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.event "attr-pipeline.trigger.<github source>.event") as a list is deprecated. Update any instances to specify multiple triggers each with a single associated event instead.

*   The use of [requested](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.requested "value-pipeline.trigger.<github source>.action.requested") has been deprecated for some time already. Its use will now produce a configuration syntax warning, and in a future version of Zuul, an error.

*   The use of [pipeline.trigger.<github source>.require-status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require-status "attr-pipeline.trigger.<github source>.require-status") has been deprecated for some already. Its use will now produce a configuration syntax warning, and in a future version of Zuul, an error.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-1-0-bug-fixes "Link to this heading")

*   Fixes a bug where Zuul would incorrectly enqueue a Gerrit change that could not be submitted due to missing labels in a dependent pipeline.

Specifically, if change had a score for any label that would provided by Zuul, all other missing labels would be incorrectly ignored.

*   Monitoring stats for per-branch queues are now distinct from shared-branch queues. Shared branch queue stats are at:

Per-branch queue stats are now at:

Prior to this change, per-branch queue stats for one branch queue may have overwritten the stats from another queue resulting in incomplete or incorrect data.

*   In 10.0.0, supercedent pipelines could raise exceptions when enqueing changes that were part of a dependency cycle (regardless of whether the changes merged or not). This has been corrected, and the documentation has been updated to clarify that circular dependencies are ignored in supercedent pipelines.

*   The value of [zuul.items.project.src_dir](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.items.project.src_dir "var-zuul.items.project.src_dir") did not take into account the job’s workspace scheme and was always constructed using the golang scheme. That has been corrected so that it now reflects the job’s scheme.

10.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Prelude[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#prelude "Link to this heading")

This release includes a significant refactoring of the internal handling of circular dependencies. This requires some changes for consumers of Zuul output (via some reporters or the REST API) and requires special care during upgrades. In the case of a dependency cycle between changes, Zuul pipeline queue items will now represent multiple changes rather than a single change. This allows for more intuitive behavior and information display as well as better handling of job deduplication.

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-new-features "Link to this heading")

*   Ansible version 9 is now available. The default Ansible version is still 8, but version 9 may be selected by using [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-upgrade-notes "Link to this heading")

*   Support for Ansible version 6 has been removed. Migrate any existing jobs which rely on this version to Ansible version 8 before upgrading.

*   Zuul can not be upgraded to this version while running. To upgrade:

> *   Stop all Zuul components running the previous version (stopping Nodepool is optional).
> 
>     *   On a scheduler machine or image (with the scheduler stopped) and the new version of Zuul, run the command:
> 
> 
> > zuul-admin delete-state –keep-config-cache
> 
> 
> This will delete all of the pipeline state from ZooKeeper, but it will retain the configuration cache (which contains all of the project configuration from zuul.yaml files). This will speed up the startup process.
> 
>     *   Start all Zuul components on the new version.

*   The MQTT reporter now includes a job_uuid field to correlate retry builds with final builds.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-10-0-0-deprecation-notes "Link to this heading")

*   The syntax of string substitution in pipeline reporter messages has changed. Since queue items may now represent more than one change, the {change} substitution in messages is deprecated and will be removed in a future version. To maintain backwards compatability, it currently refers to the arbitrary first change in the list of changes for a queue item. Please upgrade your usage to use the new {changes} substitution which is a list.

*   The syntax of string substitution in SMTP reporter messages has changed. Since queue items may now represent more than one change, the {change} substitution in messages is deprecated and will be removed in a future version. To maintain backwards compatability, it currently refers to the arbitrary first change in the list of changes for a queue item. Please upgrade your usage to use the new {changes} substitution which is a list.

*   The MQTT and Elasticsearch reporters now include a changes field which is a list of dictionaries representing the changes included in an item. The correspending scalar fields describing what was previously the only change associated with an item remain for backwards compatability and refer to the arbitrary first change is the list of changes for a queue item. These scalar values will be removed in a future version of Zuul. Please upgrade yur usage to use the new changes entries.

*   The zuul.bundle_id variable is deprecated and will be removed in a future version. For backwards compatability, it currently duplicates the item uuid.

9.5.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-5-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-5-0-upgrade-notes "Link to this heading")

*   Ansible versions 6 is now deprecated in Zuul since it is unmaintaned, and it will be removed from a future version of Zuul. Ansible 8 is now the default version in Zuul.

9.4.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0-new-features "Link to this heading")

*   The Gerrit driver now supports the `hashtags-changed` event as a trigger as well as using hashtags as trigger or pipeline requirements.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-4-0-bug-fixes "Link to this heading")

*   The MQTT reporter now sets the log_url for retried builds correctly. The link to the build result page is reported in a dedicated web_url field.

9.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-new-features "Link to this heading")

*   Monitoring stats for builds are now emitted for more results. Previously they were emitted for some build results such as SUCCESS, FAILURE, and ERROR but now include NODE_FAILURE and other result values.

*   Support for using Google Cloud Pub/Sub as an event source has been added to the Gerrit driver.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-upgrade-notes "Link to this heading")

*   A significant SQL schema migration is included which requires extra care when upgrading.

It is recommended to make a database backup before upgrading in case of problems. It is also recommended to test the migration with a copy of the database in a development environment first in order to ascertain expected runtime and detect any data integrity problems early.

Zuul is unable to operate as normal during the schema upgrade. The following procedure is recommended:

> *   Perform a database backup
> 
>     *   Stop all Zuul components
> 
>     *   Start one scheduler and wait for it to complete the migration and initialization
> 
>     *   Start the rest of Zuul

If the migration fails and the backing database is PostgreSQL, the migration will be rolled back and Zuul may be restarted on the previous version. If the backing database is MySQL, if the error happens early enough the migration may be rolled back (look for “Early error in schema migration, rolling back” in scheduler logs). If an error happens late in the migration, manual intervention may be required.

*   Zuul’s GitHub driver has updated the default merge mode to better align with GitHub’s default behavior. This change requires Git 2.33.0 or newer unless you explicitly override Zuul’s default merge mode for a project. Additionally, if you aren’t overriding the merge mode then the merge algorithm chosen may change depending on your Git and GitHub versions. This is expected to provide more deterministic results.

*   Input data from a parent job (return data or artifacts) no longer influences whether a child job can be deduplicated or not.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-3-0-bug-fixes "Link to this heading")

*   Correct the behavior of the timer driver to not trigger for branches configured as always-dynamic.

9.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-new-features "Link to this heading")

*   Gerrit and GitHub repositories will now automatically use the default branch as specified in their respective systems as the project’s default branch. This may still be overridden in zuul using the [project.default-branch](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.default-branch "attr-project.default-branch") setting.

*   A new job configuration option, [job.failure-output](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.failure-output "attr-job.failure-output"), has been added to allow users to specify regular expressions which, when seen in the streaming job output, will trigger the early failure detection in Zuul so that dependent pipeline gate resets may begin before the completion of a failed job.

*   Two new settings are available to protect Zuul from resource exhaustion from processing too many dependencies among changes. The Gerrit driver supports setting [<gerrit connection>.max_dependencies](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.max_dependencies "attr-<gerrit connection>.max_dependencies") to limit internal dependency processing during event processing, and a new tenant setting of [tenant.max-dependencies](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-dependencies "attr-tenant.max-dependencies") is available to limit tenant processing while enqueing changes in pipelines.

*   Additional pipeline stats for individual project queues are available at [zuul.tenant.<tenant>.pipeline.<pipeline>.queue](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.queue").

*   Configuration options which accept [regular expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex) have been updated to accept a new syntax which allows specifying that the regular expression should be treated as a negative match.

*   An upper limit on the dependent pipeline actionable window can now be specified using the [pipeline.window-ceiling](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.window-ceiling "attr-pipeline.window-ceiling") setting. The default of no upper limit remains.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-upgrade-notes "Link to this heading")

*   If using the GitHub driver in app mode, you should consider also generating and adding an `api_token`. The option is not strictly required but will increase rate limits and add functionality for projects the app is not installed in.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-2-0-deprecation-notes "Link to this heading")

*   Regular expressions using Python syntax are deprecated in favor of RE2 syntax instead, for additional speed and safety. Negative lookahead assertions may be replaced using the negate keyword. See [Regular Expressions](https://zuul-ci.org/docs/zuul/latest/project-config.html#regex) for more information.

If Zuul detects a regular expression using Python syntax that is not supported by RE2, it will register a configuration syntax warning. These may be viewed on the configuration errors page in the web interface.

A future version of Zuul will remove Python regex support completely and these warnings will become errors.

9.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-new-features "Link to this heading")

*   A new job attribute, ansible-split-streams has been added to instruct Zuul to keep stdout and stderr separate when running Ansible command tasks.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-deprecation-notes "Link to this heading")

*   Zuul is changing the behavior of its customized Ansible command module to match the standard Ansible behavior.

The previous behavior and current default is to combine stdout and stderr streams. In a later Zuul release, the ansible-split-streams default value will change from false to true in order to match the standard Ansible behavior and keep the streams separate. A further Zuul release will remove the option altogether.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-1-0-bug-fixes "Link to this heading")

*   Ansible task failures in block/rescue stanzas could cause Zuul to erroneously trigger early-failure behavior for the build, which could result in inconsistent behavior in a dependent pipeline. Task failures in Ansible blocks are no longer considered for early failure detection, and if a build encounters an early failure, it will cause the build result to be reported as a failure in all cases.

9.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-new-features "Link to this heading")

*   Ansible version 8 is now available. The default Ansible version is still 6, but version 8 may be selected by using [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

*   Support for using AWS Kinesis as an event source has been added to the Gerrit driver.

*   A new job variable, zuul.commit_id has been added. This provides a stable identifier for all types of pipeline queue items (changes, refs, tags, or branches) from any driver to identify the commit which triggered the queue item. This can be used to interface with external systems which identify changes by commit.

*   Zuul will now begin the process of aborting following jobs and re-ordering pipelines immediately after the first Ansible task fails.

*   Support for using Kafka as an event source has been added to the Gerrit driver.

*   A new tenant project configuration option, implied-branch-matchers has been added. This is useful in conjunction with the branch exclusion options which may cause Zuul to change behavior as the set of load branches switches between one and more than one. The operator can fix the appropriate behavior in the tenant config file rather than relying on the heuristic in these cases.

*   A new Zuul job variable [zuul_will_retry](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul_will_retry "var-zuul_will_retry") available in post and cleanup playbooks, which indicates whether the current job will be retried.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-upgrade-notes "Link to this heading")

*   Python 3.11 is now the only version of Python with which Zuul is tested.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-9-0-0-bug-fixes "Link to this heading")

*   Duplicate [queue](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue "attr-queue") configuration items are now permitted on multiple branches of the same project as long as their configuration is identical. Similar to secrets and semaphores, this can help avoid spurious configuration errors when branching a project with in-repo configuration.

8.3.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-1-security-issues "Link to this heading")

*   Zuul will execute bwrap with –disable-userns set if two conditions hold. 1) The version of bwrap is 0.8.0 or newer and 2) User namespaces are enabled in the zuul-executor runtime context. Doing so will prevent the zuul-executor bwrap runtimes from creating additional user namespaces which fortifies Zuul’s security position.

8.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-new-features "Link to this heading")

*   Added a new dark theme for the Zuul web interface.

*   Added theme selection for the Zuul web interface. The default theme is set to Auto which means your system/browsers preference determines if the Light or Dark theme should be used. Either can be explicitly set in the settings for the web interface by clicking the cogs in the top right.

*   Gerrit pipeline triggers now support embedded require and reject filters in order to match. Any conditions set for the pipeline in require or reject filters may also be set for event trigger filters.

This can be used to construct pipelines which trigger based on certain events but only if certain other conditions are met. It is distinct from pipeline requirements in that it only affects items that are directly enqueued whereas pipeline requirements affect dependencies as well.

*   All Gerrit “requires” filters are now available as “reject” filters as well.

*   GitHub pipeline triggers now support embedded require and reject filters in order to match. Any conditions set for the pipeline in require or reject filters may also be set for event trigger filters.

This can be used to construct pipelines which trigger based on certain events but only if certain other conditions are met. It is distinct from pipeline requirements in that it only affects items that are directly enqueued whereas pipeline requirements affect dependencies as well.

*   The [nodepool.slot](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-nodepool.slot "var-nodepool.slot") variable has been added to host vars. This is supplied by the nodepool static and metastatic drivers starting with version 8.0.0. It may be used to avoid build directory collisions on nodes that run more than one job.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-deprecation-notes "Link to this heading")

*   The Elasticsearch reporter now filters zuul data from the job returned vars. The job returned vars under the zuul key are meant for Zuul and may include large amount of data such as file comments.

*   The require-approval and reject-approval Gerrit trigger attributes are deprecated. Use [pipeline.trigger.<gerrit source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require "attr-pipeline.trigger.<gerrit source>.require") and [pipeline.trigger.<gerrit source>.reject](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.reject "attr-pipeline.trigger.<gerrit source>.reject") instead.

*   The require-status GitHub trigger attribute is deprecated. Use [pipeline.trigger.<github source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require "attr-pipeline.trigger.<github source>.require") instead.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-3-0-bug-fixes "Link to this heading")

*   The zuul-admin prune-database command did not completely delete expected data from the database. It may not have deleted all of the buildsets older than the specified cutoff time, and it may have left orphaned data in ancillary tables. This has been corrected and it should now work as expected. Additionally, a –batch-size argument has been added so that it may delete data in multiple transactions which can facilitate smoother operation when run while Zuul is operational.

Users who have previously run the command may need to manually delete rows from the zuul_build, zuul_build_event, zuul_artifact, and zuul_provides tables which do not have corresponding entries in the zuul_buildset table.

*   The cherry-pick merge mode will now silently skip commits that have already been applied to the tree when cherry-picking, instead of failing with an error.

The exception to this is if the source of the cherry-pick is an empty commit, in which case it is always kept.

Skipping commits that have already been applied is important in a pipeline triggered by the Gerrit change-merged event (like the deploy pipeline), since the scheduler would previously try to cherry-pick the change on top of the commit that just merged and fail.

*   Zuul will now attempt to honor Gerrit “submit requirements” when determining whether to enqueue a change into a dependent (i.e., “gate”) pipeline. Zuul previously honored only Gerrit’s older “submit records” feature. The new checks will avoid enqueing changes in “gate” pipelines in the cases where Zuul can unambiguously determine that there is no possibility of merging, but some non-mergable changes may still be enqueued if Zuul can not be certain whether a rule should apply or be disregarded (in these cases, Gerrit will fail to merge the change and Zuul will report the buildset as a MERGE_FAILURE).

This requires Gerrit version 3.5.0 or later, and Zuul to be configured with HTTP access for Gerrit.

8.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-new-features "Link to this heading")

*   The change message (commit message, or pull request message depending on the driver) is now available in plain text form annotated with the Ansible !unsafe tag as [zuul.change_message](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.change_message "var-zuul.change_message").

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-upgrade-notes "Link to this heading")

*   Fixes tenant.untrusted-projects.<project>.include-branches being lower priority than tenant.untrusted-projects.<project>.exclude-branches to match the documentation and expected user behavior.

This only affects projects that are using both include-branches and exclude-branches at the same time. Now, include-branches has priority over exclude-branches for any branches that match both. Practically speaking, this means that exclude-branches is ignored if include-branches is set.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-2-0-deprecation-notes "Link to this heading")

*   The base64 encoded version of the change message available as [zuul.message](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.message "var-zuul.message") is deprecated and will be removed in a future version of Zuul. Use [zuul.change_message](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.change_message "var-zuul.change_message") instead.

8.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-new-features "Link to this heading")

*   A new pipeline attribute, [pipeline.allow-other-connections](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.allow-other-connections "attr-pipeline.allow-other-connections"), has been added to ensure that only changes from connections which are mentioned in the pipeline configuration (such as triggers, reporters, or pipeline requirements) are enqueued.

*   Zuul now stores the pause and resume events for a build together with their timestamp and reports them to the SQL database and via MQTT.

*   Individual playbooks may now be wrapped by a semaphore. Zuul will start the job and proceed up to the point of a playbook which requires a semaphore and then wait until it is able to aquire the semaphore before proceeding. It releases the semaphore after the end of that individual playbook.

The same semaphore may be used for both jobs and playbooks, but an individual job may not use the same semaphore for both purposes.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-upgrade-notes "Link to this heading")

*   Additional syntax checking is performed on job configuration changes so that Zuul will report an error if a job inherits from a non-permitted parent (such as a final job, intermediate job when the child is not abstract, or a protected job in another project). Previously, these situations might only be discovered when freezing a job graph.

If any jobs currently in this situation exist, they will be reported as configuration errors.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-1-0-security-issues "Link to this heading")

*   Non-live items are now subject to pipeline requirements for independent pipelines.

Previously, an optimization for independent pipelines skipped checking that a change met the pipeline requirements. If an independent pipeline is intended only to run reviewed code, this could allow running unreviewed code by updating dependent changes.

Now both non-live and live items are subject to pipeline requirements in all pipeline managers.

*   The new allow-other-connections pipeline configuration option may now be used to ensure that only changes from connections which are mentioned in the pipeline configuration (such as triggers, reporters, or pipeline requirements) are enqueued. This allows the construction of a pipeline where, for example, code review requirements are strictly enforced, even for dependencies which are not normally directly enqueued.

8.0.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-1-bug-fixes "Link to this heading")

*   An error which prevented results from appearing in the web UI on the “Buildsets” tab has been corrected.

8.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-new-features "Link to this heading")

*   Read-level access to tenants or the tenant list may now be restricted to authorized users using the [tenant.access-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.access-rules "attr-tenant.access-rules") and [api-root.access-rules](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-api-root.access-rules "attr-api-root.access-rules") attributes.

*   The [rebase](https://zuul-ci.org/docs/zuul/latest/config/project.html#value-project.merge-mode.rebase "value-project.merge-mode.rebase") merge-mode is now supported for GitHub.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-upgrade-notes "Link to this heading")

*   Support for Ansible version 5 has been removed. Migrate any existing jobs which rely on this version to Ansible version 6 before upgrading.

*   In preparation for expanded access control features in the web interface, and REST API, the `admin-rule` tenant configuration object has been renamed to `authorization-rule`. When applied to a tenant, the tenant attribute is still `admin-rules` since it determines admin access to that tenant. This change will allow similar rules to be applied to non-admin level access in the future.

Tenant configs should now follow this example:

- authorization-rule:
 name: example-rule
- tenant:
 name: example-tenant
 admin-rules:
 - example-rule 
The old form is still permitted for backwards compatability, but will be removed in a later version of Zuul.

*   The default merge mode used by Zuul for preparing git repos was previously [merge-resolve](https://zuul-ci.org/docs/zuul/latest/config/project.html#value-project.merge-mode.merge-resolve "value-project.merge-mode.merge-resolve") in all cases, but is now [merge](https://zuul-ci.org/docs/zuul/latest/config/project.html#value-project.merge-mode.merge "value-project.merge-mode.merge") for all drivers except Gerrit, where [merge-resolve](https://zuul-ci.org/docs/zuul/latest/config/project.html#value-project.merge-mode.merge-resolve "value-project.merge-mode.merge-resolve") is still the default. This makes the merge operations performed by Zuul more closely match the operations that will be performed by the code review systems.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-8-0-0-bug-fixes "Link to this heading")

*   The use of implied branch matchers in jobs where override-checkout was specified could cause some jobs to include unintended variants. Specifically: job variants with implied branch matchers on branches which are substring matches of a branch specified in the override-checkout job attribute may have been used when not intended.

This has been corrected so that the same job variant matching process happens whether the change’s branch or the branch specified by override-checkout is used.

7.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0-new-features "Link to this heading")

*   The GitHub driver now supports specifying the draft status of a PR as a pipeline requirement. See [pipeline.require.<github source>.draft](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.draft "attr-pipeline.require.<github source>.draft").

*   Details about the configuration and current usage of semaphores are now available in the web UI under the “Semaphores” tab.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-1-0-upgrade-notes "Link to this heading")

*   Ansible versions 5 is now deprecated in Zuul since it is unmaintaned, and it will be removed from a future version of Zuul. Ansible 6 is now the default version in Zuul.

7.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0-new-features "Link to this heading")

*   The MQTT driver now supports including data returned from a job in its reports. See [pipeline.<reporter>.<mqtt>.include-returned-data](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#attr-pipeline.%3Creporter%3E.%3Cmqtt%3E.include-returned-data "attr-pipeline.<reporter>.<mqtt>.include-returned-data").

*   Nodesets may now express an ordered list of alternatives so that if Nodepool is unable to fulfill a request for certain labels, one or more alternative Nodesets may be attempted instead. See [nodeset.alternatives](https://zuul-ci.org/docs/zuul/latest/config/nodeset.html#attr-nodeset.alternatives "attr-nodeset.alternatives") for details.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-7-0-0-upgrade-notes "Link to this heading")

*   Support for Ansible versions 2.8 and 2.9 has been removed. Migrate any existing jobs which rely on these versions to Ansible version 5 or 6 before upgrading.

*   The previously deprecated `merge-failure` and `merge-failure-message` pipeline configuration options have been removed. Use `merge-conflict` and `merge-conflict-message` respectively instead.

*   The deprecated syntax of specifying project change queues on pipeline configurations has been removed. Specify queues using the project stanza now. See [queue](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue "attr-queue") for more information.

6.4.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0-new-features "Link to this heading")

*   Ansible version 6 is now available. The default Ansible version is still 5, but version 6 may be selected by using [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-4-0-upgrade-notes "Link to this heading")

*   Ansible versions 2.8 and 2.9 are now deprecated in Zuul since they are both unmaintaned. Ansible 5 is now the default version in Zuul.

6.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-3-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-3-0-new-features "Link to this heading")

*   A new [pipeline.config-error](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.config-error "attr-pipeline.config-error") pipeline reporter is available for customizing reporter actions related to Zuul configuration errors.

6.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0-new-features "Link to this heading")

*   Added build set url to Zuul comment. This provide a quick way for user to reach the build set page from Gerrit.

*   Added a new [tenant.untrusted-projects.<project>.always-dynamic-branches](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.always-dynamic-branches "attr-tenant.untrusted-projects.<project>.always-dynamic-branches") tenant project configuration option. This may be used to specify branches from which Zuul should never load static configuration and instead treat every change as if it newly proposed dynamic configuration. This is potentially useful for large numbers of rarely-used feature branches.

*   The new ssh_server option for gerrit connections may be used to specify a hostname to use for SSH connections while the normal server option specifies the hostname to use for HTTP connections.

*   Support for global (cross-tenant) semaphores has been added. See [Global Semaphore](https://zuul-ci.org/docs/zuul/latest/tenants.html#global-semaphore).

*   Pipeline timer triggers with jitter now apply the jitter to each project-branch individually (instead of to the pipeline as a whole). This can reduce the thundering herd effect on external systems for periodic pipelines with many similar jobs.

*   The scheduler now accepts an argument –wait-for-init which will cause it to wait until all tenants have been initialized before it begins processing pipelines. This may help large systems with excess scheduler capacity perform a rolling restart of schedulers more quickly.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-2-0-bug-fixes "Link to this heading")

*   Zuul now treats job dependencies that reference undefined jobs as a configuration error. Previously a job which depended on another job which did not exist would pass initial syntax validation and only cause a failure in freezing the job graph when Zuul attempted to run the job. Now incorrect or missing job dependencies are detected during configuration. This means that new config errors may be prevented from merging. It also means that existing erroneous job or project configurations will be regarded as configuration errors at startup.

6.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-new-features "Link to this heading")

*   The cherry-pick merger mode can now handle merges between branches by performing a git merge instead of git cherry-pick if the change has multiple parents. Previously, this would fail because git doesn’t allow a merge to be cherry-picked.

*   If identical jobs are run for multiple changes in a dependency cycle, Zuul may now deduplicate them under certain circumstances. See [job.deduplicate](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.deduplicate "attr-job.deduplicate") for details.

*   Added new tenant project configuration options attr:tenant.untrusted-projects.<project>.include-branches and attr:tenant.untrusted-projects.<project>.exclude-branches. Similar to _exclude-unprotected-branches_, these may be used to reduce the set of branches from which Zuul will load configuration.

*   A new command, `prune-database` has been added to zuul-admin in order to remove database entries older than a certain age.

*   The GitHub driver now has support for using a GitHub Enterprise [repository cache](https://docs.github.com/en/enterprise-server@3.3/admin/enterprise-management/caching-repositories/about-repository-caching). See [<github connection>.repo_cache](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_cache "attr-<github connection>.repo_cache") for information on how to configure it.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-upgrade-notes "Link to this heading")

*   A SQL schema migration is added in order to add an `updated` column to the buildset table which will be used by the prune-database command to determine which buildsets to delete. The migration will attempt to use the most recent timestamp associated with the buildset when initializing this column, however, if no timestamps are available, it will initialize it to 1970-01-01. Since this is considerably before Zuul’s birthdate, this means that any buildsets without timestamp information will be pruned the first time prune-database is run. It is expected that buildsets with no timestamps, even very recent ones, are typically uninteresting and therefore this should not cause a hardship. If this is not the case for your installation, you may want to inspect the database and change the `updated` column to a more recent value in these cases.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-1-0-deprecation-notes "Link to this heading")

*   The zuul CLI is renamed zuul-admin. The zuul command will remain usable until a future version, then will be phased out. Likewise, tenant-scoped, workflow affecting commands such as autohold, enqueue, dequeue, promote are deprecated from the zuul-admin CLI and will be phased out in a future version. They can still be performed via the zuul-client CLI.

6.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-new-features "Link to this heading")

*   Ansible version 5 is now available. The default Ansible version is still 2.9, but version 5 may be selected by using [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

*   Pipelines can now trigger on `wip-state-changed` and filter events on the wip state of a change with [pipeline.require.<gerrit source>.wip](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.wip "attr-pipeline.require.<gerrit source>.wip").

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-upgrade-notes "Link to this heading")

*   This is the first version of Ansible added to Zuul since the Ansible project began releasing the Ansible community package. Zuul includes the Ansible community package since it includes a wide selection of useful modules, many of which were included by default in previous versions of Ansible.

Only the major version of Ansible community is specified (e.g. `ansible-version: 5`). This corresponds to a single minor release of Ansible core (e.g., Ansible community 5 corresponds to Ansible core 2.12). Ansible releases minor versions of the community package which may contain updates to the included Ansible collections as well as micro version updates of Ansible core (e.g. Ansible community 5.6 includes ansible-core 2.12.4).

Zuul does not specify the minor version of Ansible community, therefore the latest available micro-version will be installed at build-time. If you need more control over the version of Ansible used, see the help text for `zuul-manage-ansible`.

*   Python 3.8 or newer is required to run Zuul. This change was necessary to support Ansible 5 and newer as Ansible’s minimum python requirement is 3.8.

*   The built-in support for the ARA Ansible callback plugin has been removed.

*   The restricted Ansible environment used for untrusted playbooks has been relaxed.

Zuul previously attempted to restrict the actions of playbooks running in the untrusted execution context on the executor so that users would not be able to load custom Ansible plugins, execute code on the executor, or use certain functions of built-in Ansible modules. This was done in an attempt to improve the security of the Zuul executor. However, the approach has proved laborious, prone to error, and increasingly incompatible with newer versions of Ansible.

Therefore it has been removed, and now playbooks within both the trusted and untrusted execution contexts have access to the full suite of Ansible modules. See the [Security Considerations](https://zuul-ci.org/docs/zuul/latest/configuration.html#executor-security) section for information on caveats relating to executor security.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-6-0-0-bug-fixes "Link to this heading")

*   Nodepool host variables are now available even for unreachable hosts. This is useful for network appliances which start the job in an unreachable state.

5.2.5[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-5 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-5-bug-fixes "Link to this heading")

*   Further instances of reporting NO_JOBS results to the database when not necessary have been corrected.

5.2.4[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-4 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-4-bug-fixes "Link to this heading")

*   A change in 5.2.3 began reporting NO_JOBS results to the database which was unintentional. This has been corrected and they are no longer recorded in the database.

5.2.3[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-3 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-3-bug-fixes "Link to this heading")

*   Projects and jobs on branches whose names have special characters in regular expressions could fail to match changes as intended. Implied branch matchers automatically generated from branch names are now treated as requiring exact matches. Any user-specified branch matcher (including in [job.branches](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.branches "attr-job.branches") and [pragma.implied-branches](https://zuul-ci.org/docs/zuul/latest/config/pragma.html#attr-pragma.implied-branches "attr-pragma.implied-branches")) are still treated as regular expressions.

*   Project name regex handling has been updated to return all possible matches. Previously if there were collisions with short names it was an error. The point of the regex system is to simplify configuration and apply configs to all projects that match. Collisions don’t impact this behavior so we don’t need to raise an error in these cases.

5.2.2[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-2 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-2-bug-fixes "Link to this heading")

*   An issue introduced in Zuul version 5.2.0 which could cause jobs running on Windows nodes to fail with the error Could not find imported module support code for ‘Ansible.ModuleUtils.Legacy’” has been corrected.

5.2.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-new-features "Link to this heading")

*   The [queue.dependencies-by-topic](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue.dependencies-by-topic "attr-queue.dependencies-by-topic") setting is added for Zuul users who wish to emulate the Gerrit `submitWholeTopic` behavior for some projects without enabling it site-wide in Gerrit.

*   The promote administrative action now functions with all pipeline managers. Previously it would only have an impact on dependent pipelines, but it will now re-order change queues as well as changes within any type of pipeline.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-upgrade-notes "Link to this heading")

*   The promote administrative action will no longer restart jobs for changes which have not been re-ordered within their change queue.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-1-bug-fixes "Link to this heading")

*   Fixed an issue in the Gerrit driver introduced in 5.2.0 which could cause infinite loops while querying changes.

5.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-new-features "Link to this heading")

*   Changes in dependent queues are now automatically dequeued if they no longer meet the mergability requirements set by the upstream code review system.

*   Zuul now matches Gerrit’s behavior when `change.submitWholeTopic` is set in Gerrit.

When this setting is enabled in Gerrit and a change is submitted (merged), all changes with the same topic are submitted simultaneously. Zuul will now query for changes which are set to be submitted together by Gerrit when enqueing them and treat them as if they are a set of circular dependencies.

If the projects are not part of pipeline queues which are configured to allow circular dependencies, then Zuul will report failure on enqueue. Be sure that the submitWholeTopic setting in Gerrit and the allow-circular-dependencies setting in Zuul match.

This functionality requires an HTTP connection to Gerrit. If only an SSH connection is available, then changes submitted together will be ignored.

*   The ability to configure Microsoft Login as an OpenID Connect authentication provider has been added.

*   Zuul now reports total resource usage statistics.

The following statistic is emitted:

zuul.nodepool.resources.total.tenant.{tenant}.{resource}

Gauge with the currently used resources by tenant in total, i.e., all nodes belonging to a tenant, regardles of their state.

*   It is now possible for jobs to skip retries caused by failures in ‘pre-run’ by returning retry: false:

- zuul_return:
 data:
 zuul:
 retry: false 

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-upgrade-notes "Link to this heading")

*   Zuul now reports total and in-use resource usage statics separately.

To distinquish those, the following statistics have been renamed:

    *   zuul.nodepool.resources.tenant.{tenant}.{resource}->zuul.nodepool.resources.in_use.tenant.{tenant}.{resource}

    *   zuul.nodepool.resources.project.{project}.{resource}: ->zuul.nodepool.resources.in_use.project.{tenant}.{resource}

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-2-0-security-issues "Link to this heading")

*   A vulnerability which allowed the execution of untrusted code on the executor was fixed.

Zuul restricts the Ansible modules and plugins which can be used in the untrusted security context (i.e., untrusted projects). It also prohibits running programs on the Zuul executor in the untrusted security context.

Ansible 2.8 and later versions support referencing builtin modules using the ansible.builtin.<name> alias. Playbooks which use this mechanism can bypass Zuul’s security restrictions and run arbitrary local code or otherwise restricted modules.

Zuul’s use of bubblewrap means that any commands executed via this vulnerability would still be contained within the restricted environment, meaning that they can not access files outside of the build directory or continue running longer than the playbook. But they may have been able to access files within the build directory but outside of the work/ directory, as well as potentially exploit any kernel or hypervisor privilege escalation vulnerabilities.

The Zuul team now considers the restricted Ansible environment to be ineffective as a security mechanism and is developing plans to remove the restrictions and rely entirely on bubblewrap in the future. These changes will occur in a future release of Zuul (likely 6.0.0) and will be preceded by more details about the change.

5.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-new-features "Link to this heading")

*   Added support for adding and removing merge request labels in the GitLab driver, as well as triggering pipelines on label removal (label addition was already supported).

*   A new buildset result `MERGE_FAILURE` is stored in the build database in the case where a buildset is unable to be merged by the upstream code review system.

*   The following new statsd metrics are available in order to monitor Zuul system performance:

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.event_enqueue_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_enqueue_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.event_enqueue_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.merge_request_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merge_request_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.merge_request_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.layout_generation_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.layout_generation_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.layout_generation_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.job_freeze_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.job_freeze_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.job_freeze_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.repo_state_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.repo_state_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.repo_state_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.node_request_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.node_request_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.node_request_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.job_wait_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.job_wait_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.job_wait_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.event_job_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_job_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.event_job_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.read_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.read_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.write_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.write_time")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.read_objects](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_objects "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.read_objects")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.write_objects](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_objects "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.write_objects")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.read_znodes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_znodes "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.read_znodes")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.write_znodes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_znodes "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.write_znodes")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.read_bytes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_bytes "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.read_bytes")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.write_bytes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_bytes "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.write_bytes")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.event_process](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_process "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.event_process")

    *   [zuul.tenant.<tenant>.pipeline.<pipeline>.handling](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.handling "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.handling")

    *   [zuul.tenant.<tenant>.reconfiguration_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.reconfiguration_time "stat-zuul.tenant.<tenant>.reconfiguration_time")

*   A new command `zuul-scheduler tenant-reconfigure` has been added. It allows an operator to perform a reconfiguration of a single tenant. This may be helpful in clearing up issues after connection problems with the code hosting system.

*   New monitoring metrics specific to zuul-web are available.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-upgrade-notes "Link to this heading")

*   The buildset result `MERGER_FAILURE` has been renamed to `MERGE_CONFLICT`, and the pipeline reporter configuration `merge-failure` has been renamed to `merge-conflict`.

These are more descriptive of the most common errors actually reported, and so are expected to be less confusing to users. This is also in service of a future change to support a new buildset result `MERGE_FAILURE` which will indicate that the change was unable to be merged in the upstream repository.

When upgrading, it is recommended to stop all schedulers briefly (i.e, when the first scheduler of the new version starts, there should be no schedulers running the old version). The new scheduler will perform a database migration when it starts and update all existing `MERGER_FAILURE` buildset results to `MERGE_CONFLICT`. If old schedulers are running, they may continue to add `MERGER_FAILURE` entries which will need to be manually updated in order to be visible in the web UI or rest API.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-deprecation-notes "Link to this heading")

*   The `merge-failure` and `merge-failure-message` pipeline configuration options have been renamed to `merge-conflict` and `merge-conflict-message` respectively. The old settings are retained for backwards compatibility, but will be removed in a later version. Please update your usage of them as soon as possible.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-1-0-bug-fixes "Link to this heading")

*   The labels pipeline requirement in the gitlab driver erroneously treated the labels as a boolean or but should have treated them as a boolean and (i.e., all listed labels are required). The behavior has been updated to match the documentation and other drivers.

5.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-5-0-0-upgrade-notes "Link to this heading")

*   Zuul no longer uses gearman. It is no longer required to run a Gearman server, and the Zuul scheduler no longer does so. All gearman-related settings in zuul.conf files are now ignored and may be removed.

Commands such as zuul enqueue which were previously executed via Gearman may still be used by creating an authentication token and adding a webclient section to zuul.conf.

*   Support for configuring the database as a connection in `zuul.conf` was deprecated in Zuul version 4.0 and has now been removed. Refer to [Database](https://zuul-ci.org/docs/zuul/latest/configuration.html#database) how to configure the database now.

4.12.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-12-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-12-0-upgrade-notes "Link to this heading")

*   Due to a change in the ZooKeeper data format, the following upgrade procedure is required:

> *   Stop all Zuul components
> 
>     *   Run `zuul delete-state`
> 
>     *   Start all Zuul components

*   Zuul-web now requires access to the Zookeeper keystore. Ensure that the [keystore.password](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keystore.password "attr-keystore.password") option is included in `zuul.conf` on at least the scheduler, executor, and web servers (it may be included on all components if desired).

*   Zuul-web requires information for all defined connections. Previously, zuul-web may have started without all of the connections fully defined in its config file, or with some requirements (such as keys used for connecting to remote services) present. They are now required in order for zuul-web to start.

4.11.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0-new-features "Link to this heading")

*   The new variable [zuul.playbook_context](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.playbook_context "var-zuul.playbook_context") as well as new variables under [zuul.projects](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.projects "var-zuul.projects") have been added to help debug or audit the playbooks and roles used by Ansible when running jobs.

These variables describe the repo configuration used for the playbooks and roles of each Ansible execution. These repos may have a different state than the workspace repos.

*   It is now possible to disable connection pooling in the Gitlab driver with [<gitlab connection>.disable_connection_pool](https://zuul-ci.org/docs/zuul/latest/drivers/gitlab.html#attr-%3Cgitlab%20connection%3E.disable_connection_pool "attr-<gitlab connection>.disable_connection_pool"). This option may be useful under adverse network conditions.

*   The optional prometheus service now also includes endpoints for readiness and liveness checks. See [Liveness Probes](https://zuul-ci.org/docs/zuul/latest/monitoring.html#prometheus-liveness) for details.

*   Allow an authorized user to dequeue changes from the Web UI’s status page.

*   Add authentication in the web UI. Zuul’s web UI can be configured to authenticate users against an Identity Provider supporting the OpenID Connect protocol.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-11-0-upgrade-notes "Link to this heading")

*   Users upgrading from previous versions of zuul will need to run `zuul delete-state` to delete Zuul’s ephemeral state from Zookeeper. The ephemeral state produced by older versions of zuul is not compatible with this release. This command should be run while all Zuul services are stopped to prevent writes to the Zookeeper database. More information on this command can be found in the documentation: [https://zuul-ci.org/docs/zuul/reference/client.html#delete-state](https://zuul-ci.org/docs/zuul/reference/client.html#delete-state)

*   The prometheus endpoint would previously serve metrics at any URI. It now only returns metrics on the / and /metrics URI. The latter is recommended.

4.10.4[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-4 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-4-bug-fixes "Link to this heading")

*   A fix was made to mitigate an issue where a ZooKeeper disconnect could cause too many threads to be spawned resulting in errors.

4.10.3[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-3 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-3-bug-fixes "Link to this heading")

*   A bug with the change cache cleanup routine which could have caused items to be stuck in pipelines without running jobs has been corrected.

*   Gerrit driver: Zuul error responses could overflow the default message length with large configurations leading to Gerrit rejecting the comment (and hence no notification from Zuul on the change). Such messages are now truncated to a safe length.

4.10.2[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-2 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-2-bug-fixes "Link to this heading")

*   A bug which prevented change cache cleanup (and therefore caused ZooKeeper usage to grow without limits) was fixed.

4.10.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1-new-features "Link to this heading")

*   Add support for squashing MR with gitlab.

*   On the description page of a buildset in the zuul web dashboard, a user can display a timeline of the builds making up the buildset.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-1-bug-fixes "Link to this heading")

*   Fix a bug in the cleanup routine for the new Zookeeper based change cache. Previously this caused the change cache to leak entries. Note the fixed routine will clean up the leaked entries automatically once Zuul is restarted on this new version.

*   Fix detection of the failed merge in gitlab driver.

4.10.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-10-0-upgrade-notes "Link to this heading")

*   Nodepool 4.3.0 is now required. Zuul stores additional information in node records in preparation for supporting multiple schedulers.

*   The scheduler time database has been removed. This was stored in the scheduler state directory, typically `/var/lib/zuul/times`. The entire state directory on the scheduler is no longer used and may now be removed.

Zuul now derives its estimated build duration times from the SQL database.

4.9.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0-new-features "Link to this heading")

*   The `zuul delete-state` command may be used to delete all of the ephemeral state stored by Zuul in ZooKeeper. Normally Zuul is able to detect and correct errors on its own, but in case it is unable to, this may prove a useful utility for manual recovery.

*   The new commands `zuul copy-keys` and `zuul delete-keys` may be useful when renaming projects in order to move the keys from the old to the new project names without service interruption.

*   Add new statsd gauge metrics of current open node requests exported as `zuul.nodepool.tenant.<tenant>.current_requests`. This metric tracks the currently open node requests per tenant. It drills down the overall `zuul.nodepool.current_requests` metric.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-9-0-upgrade-notes "Link to this heading")

*   Zuul no longer reads or writes project private key files from the scheduler’s filesystem. In order to load existing keys into ZooKeeper, run version 4.6.0 of the scheduler at least once, if you haven’t already.

A new command `zuul export-keys` has been added to export the encrypted keys from ZooKeeper onto the filesystem for backup. Likewise, `zuul import-keys` will load a previously-exported backup into ZooKeeper. It is recommended that you use these commands in system backup scripts.

4.8.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1-upgrade-notes "Link to this heading")

*   An error was found in a change related to Zuul’s internal configuration cache which could cause Zuul to use cached in-repo configuration files which no longer exist. If a `zuul.yaml` (or `zuul.d/*` or any related variant) file was deleted or renamed, Zuul would honor that change immediately, but would attempt to load both the old and new contents from its cache upon the next restart.

This error was introduced in version 4.8.0.

If upgrading from 4.8.0, run `zuul-scheduler full-reconfigure` in order to correctly update the cache.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-1-bug-fixes "Link to this heading")

*   Restored the job.success-message and job.failure-message functionality which was inadvertently removed.

4.8.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-8-0-new-features "Link to this heading")

*   Zuul now can route live log streams via finger gateways to make it possible to distribute executors over multiple datacenters without the possibility to directly contact every executor from within zuul-web. This is typically the case in a Kubernetes based deployment.

*   The finger gateway and executor log streaming system now supports TLS connections.

Normally zuul-web makes a direct connection to an executor in order to stream logs. With this new option, that connection can be encrypted if it crosses an untrusted network.

The ability to route log streaming connections through finger gateway servers was recently added; these will also use TLS if required.

The finger gateway server can also be used by end-users; in that case it may need a TLS certificate to use if it is required to connect to an encrypted executor or finger gateway to stream logs. An option to disable using TLS when acting as a server is provided for this case, since there are no TLS-enable finger clients.

See [fingergw.tls_cert](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-fingergw.tls_cert "attr-fingergw.tls_cert") and related options to enable encrypted connections for all three components.

4.7.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-new-features "Link to this heading")

*   The executor now honors the [executor.sigterm_method](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.sigterm_method "attr-executor.sigterm_method") configuration file setting to determine whether `SIGTERM` should be equivalent to the `graceful` command (the default) or the `stop` command.

*   The Github driver can now use ‘skipped’ and ‘neutral’ status for [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check") attribute on the Github reporter.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-upgrade-notes "Link to this heading")

*   The default behavior when an executor receives SIGTERM has been changed from immediately stopping jobs to gracefully waiting for them to finish. Set the [executor.sigterm_method](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.sigterm_method "attr-executor.sigterm_method") configuration file setting to `stop` to preserve the old behavior.

*   The zuul.scheduler.eventqueues.result gauge was removed

*   Zuul now requires at least Nodepool version of 4.2.0 due to an internal API change.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-7-0-deprecation-notes "Link to this heading")

*   The following attributes are now ignored:

> *   The `report-build-page` tenant configuration setting.
> 
>     *   The `success-url` job attribute.
> 
>     *   The `failure-url` job attribute.

The URL of the build page is now always reported for every build. This is now also true for in-progress builds, which provides for a more consistent user experience.

Since the build page is always reported as the URL, the success and failure URL job attributes are no longer useful, so this functionality has also been removed.

Zuul’s configuration syntax checker will continue to allow these settings for now (they are simply ignored) but this will be removed in version 5.0 and using them will be considered an error.

To achieve a similar result, consider returning the URL as an artifact from the job via zuul_return. This will cause a link to appear in the “Artifacts” section of the build page.

4.6.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0-new-features "Link to this heading")

*   If sensitive data must be returned from a job in order to be provided to dependent jobs, the `secret_data` attribute of `zuul_return` attribute may now be used instead of the normal `data` attribute. The data will be provided via the same mechanism as job secrets, where the data are not written to disk in the work directory. Care must still be taken to avoid displaying or storing sensitive data within the job. For example:

tasks:
 - zuul_return:
 secret_data:
 password: foobar
 data:
 this_is: not secret 

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-6-0-security-issues "Link to this heading")

*   The following connection-related variables are no longer allowed to be set in job definitions, as they may be used to circumvent security measures:

> *   ansible_connection
> 
>     *   ansible_host
> 
>     *   ansible_python_interpreter
> 
>     *   ansible_shell_executable
> 
>     *   ansible_user

They may still be set using the corresponding settings in Nodepool.

*   The ability to use Ansible Jinja templates in Zuul job variables is partially restricted.

It was found that the ability to use Jinja templates in Zuul job variables could be used to expose the contents of secrets. To remedy this, the values of Zuul job variables are frozen at the start of the job and these values are used for trusted playbooks and playbooks with secrets. The freezing action is taken without access to any secrets so they can not be exposed.

This means that Zuul job variables which reference non-secret values that are known at the start of the job (including any zuul.* variable) will continue to work as expected. Job variables which reference secrets will not work (they will be undefined). In untrusted playbooks, job variables are still dynamically evaluated and can make use of values that are set after the start of the job.

Additionally, job.extra-vars are no longer passed to Ansible using the “-e” command line options. They could be used to expose secrets because they take precedence over some internal playbook variables in some circumstances. Zuul’s extra-vars are now passed as normal inventory variables, however, they retain precedence over all other Zuul job variables (vars, host-vars, and group-vars) except secrets.

Secrets are also now passed as inventory variables as well for the same reason. They have the highest precedence of all Zuul job variables. Their values are tagged with `!unsafe` so that Ansible will not evaluate them as Jinja expressions.

If you are certain that a value contained within a secret is safe to evaluate as a Jinja expression, you may work around this limitation using the following construct in a playbook:

- set_fact:
 unsafe_var_eval: "{{ hostvars['localhost'].secret.var }}" 
This will force an explicit evaluation of the variable. This is generally safe to do in a situation where a playbook is accessing a single secret by name, with no other secrets in scope. Do not use this capability with more than one secret that is not under the control of the project where the playbook is defined.

Similarly, versions of all the original job variables tagged with `!unsafe` are available under the `unsafe_vars` variable hierarchy. For example, the job variable myvar would be available under unsafe_vars.myvar. It is not recommended to evaluate `unsafe_vars` expressions except in the most controlled of circumstances. They are almost impossible to render safely.

4.5.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-1-bug-fixes "Link to this heading")

*   The zuul tenant-conf-check command no longer needs a ZooKeeper connection to validate the tenants configuration file is valid.

4.5.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Prelude[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-5-0-prelude "Link to this heading")

This is a checkpoint release. This release contains some bugfixes and other user-invisible changes, but its main purpose is to serve as a checkpoint as we move more of Zuul’s functionality into ZooKeeper. This version has seen production use in OpenDev and we believe it to be stable and ready for wider use. Please do upgrade to it and report any issues to zuul-discuss. You may downgrade to the previous release if you do encounter any issues. Likewise, operators running the latest development builds may downgrade to this release in the case of issues.

4.4.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0-new-features "Link to this heading")

*   A new prometheus_port option for the services can be used to start the prometheus python client and exposes metrics.

*   Jobs may now request multiple semaphores and they will not start until all semaphores are acquired.

Use the new [job.semaphores](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.semaphores "attr-job.semaphores") (plural) attribute to specify them.

Note that the new attribute is additive when considering inheritance and job variants. That is to say that a job definition with a semaphores attribute will extend the list of semaphores supplied by its parent rather than overriding it (which is the behavior for the deprecated attribute).

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-4-0-deprecation-notes "Link to this heading")

*   The job attribute [job.semaphore](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.semaphore "attr-job.semaphore") (note the singular rather than plural form) job attribute is now deprecated. Use the plural form [job.semaphores](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.semaphores "attr-job.semaphores") instead. As with most list items in Zuul configuration, it also accepts a single item without the wrapping list, so to convert existing jobs, simply change the spelling of the attribute, no change to the value is required.

The singular form will be removed in Zuul 5.0.

4.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-new-features "Link to this heading")

*   The MQTT reporter now includes artifact information along with build results.

*   Jobs may now specify an alternate scheme to use when preparing repositories in the workspace. The default remains the same golang-style, but an alternate scheme called flat is now available. See [job.workspace-scheme](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.workspace-scheme "attr-job.workspace-scheme") for more details.

*   Project secrets keys and SSH keys are now stored in Zookeeper. All private data will be encrypted at rest, which requires a new mandatory setting [keystore.password](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keystore.password "attr-keystore.password") in `zuul.conf`.

For backup purposes the secrets keys and SSH keys will still exist on the local filesystem of the scheduler as before.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-upgrade-notes "Link to this heading")

*   The internal git repo caches maintained by the mergers and executors now use a new naming scheme in order to avoid collisions. When existing executors and mergers are restarted, they will remove their git repo caches and re-clone repos using the new scheme. Jobs may be slow to start until the caches are warmed again.

*   As project secrets keys and SSH keys are stored encrypted in Zookeeper the new [keystore.password](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-keystore.password "attr-keystore.password") option in `zuul.conf` is required. Please add it to your configuration for both the scheduler and executor.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-deprecation-notes "Link to this heading")

*   Zuul now correctly handles the `rerequested` action on check run trigger definitions ([check_run](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.check_run "value-pipeline.trigger.<github source>.event.check_run")) literally. This has been `requested` which doesn’t match the GitHub api. The value `requested` is now deprecated and will be removed in a later release.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-3-0-bug-fixes "Link to this heading")

*   Fixed a bug where multiple connections of the same type would not filter trigger events coming from the wrong connection.

4.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Prelude[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-2-0-prelude "Link to this heading")

This is a checkpoint release. This release contains some bugfixes and other user-invisible changes, but its main purpose is to serve as a checkpoint as we move more of Zuul’s functionality into ZooKeeper. This version has seen production use in OpenDev and we believe it to be stable and ready for wider use. Please do upgrade to it and report any issues to zuul-discuss. You may downgrade to the previous release if you do encounter any issues. Likewise, operators running the latest development builds may downgrade to this release in the case of issues.

4.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-new-features "Link to this heading")

*   Executors configured with [executor.zone](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.zone "attr-executor.zone") now can also be configured to also process jobs without a zone by enabling [executor.allow_unzoned](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.allow_unzoned "attr-executor.allow_unzoned").

*   Zuul now honors the shell-type configuration from nodepool and uses it to set ansible_shell_type, a setting that is required when connecting to Windows workers over ssh.

For Linux workers, there is a long standing ansible issue with using non-default ansible_shell_type and become, so this feature is primarily targeting Windows workers.

*   Projects can now configure change queues to queue per branch. See [queue](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue "attr-queue") for more information.

*   Circular dependencies are now optionally supported (but disabled by default). To permit dependency cycles to be enqueued, see the [queue.allow-circular-dependencies](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue.allow-circular-dependencies "attr-queue.allow-circular-dependencies") option.

*   A job now can leave warning messages on the change using zuul_return. See [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values) for examples.

*   Zuul now supports the `--validate-tenants` switch which can be used to validate the complete configuration of the listed tenants.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-upgrade-notes "Link to this heading")

*   Two sets of statsd metrics are now reported for executors: zoned and unzoned. The existing statsd keys are now deprecated; new statsd keys are available for both zoned and unzoned executors. See [zuul.executors](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors "stat-zuul.executors") for details.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-deprecation-notes "Link to this heading")

*   Shared `queues` should be configured per project now instead per pipeline. Specifying project.<pipeline>.queue is deprecated and will be removed in a future release.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-1-0-bug-fixes "Link to this heading")

*   If zoned executors were used with prior releases of Zuul, the reported executor statistics would only represent a single, unspecified zone. This has now been corrected.

4.0.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Prelude[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-prelude "Link to this heading")

This is the first 4.x release of Zuul. It requires some deployment changes by operators which have been carefully planned in order to facilitate work on Zuul version 5, which will be the first version of Zuul where every component is fault tolerant and able to scale. If you read the release notes for the last 3.x release, you may have already made all of the required changes. If not, please do so before upgrading to version 4. Every required change in version 4 is optionally supported in 3.19, so it is safe to make these changes and then upgrade. Please read all of the notes below, especially in the “Upgrading” section for details. The primary additional requirements are:

> *   TLS ZooKeeper connections
> 
> *   Network connectivity from all components to ZooKeeper
> 
> *   An SQL database

With these changes in place, it is anticipated that further upgrades to Zuul made in support of the scale-out-scheduler work will be done with minimal disruption in the course of normal releases between version 4 and 5.

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-new-features "Link to this heading")

*   The action “promote” is now available via the tenant-scoped REST API using the zuul cli.

*   Builds in the SQL reporter have a “held” attribute set to True if the build triggered a autohold request. Builds can be filtered by held status.

*   Subdirectories of `zuul.d` or `.zuul.d` can be ignored when reading configuration by placing a `.zuul.ignore` file inside them.

*   The `find` module is now allowed to run on the executor.

*   Changes can now be dequeued via the Github checks API. If a github reporter is configured to use the checks API, all running checks will provide a custom “Abort” action.

*   Zuul now respects GitHub review requirements when enqueuing into gate pipelines. This works for github.com and GitHub Enterprise starting with version 2.21.0.

*   Jobs may specify the new `intermediate` flag to note they may only be inherited by abstract jobs. This can be useful if building a job hierarchy where wish to limit where a base job is instantiated.

*   The builds/ and buildset/ API endpoints now include information about retried builds. They are called non-final as those are all builds that were retried at least once and thus weren’t visible to the user so far.

The builds/ API can filter those retried builds and you might exclude them from API result by setting `final=false` in the API request.

*   An option to use the URL of the Zuul build page when reporting has been added. This feature requires that all the pipelines in the tenant have a SQL reporter configured, and at least one of [tenant.web-root](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.web-root "attr-tenant.web-root") or [web.root](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.root "attr-web.root") must be defined.

See `tenant.report-build-page`.

*   REST API: authorizations: add a tenant-scoped endpoint at ‘/api/tenant/{tenant}/authorizations’. Calling the endpoint will return a list of admin tenants limited to the scoped tenant, if the user has admin privileges on it.

*   Host key checking is now disabled for a host in the generated Ansible inventory if `host-key-checking` is set to `False` in the corresponding nodepool config.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-upgrade-notes "Link to this heading")

*   Support for Ansible 2.7 has been removed.

*   If using a SQL reporter, the zuul_builds table will be updated with a new ‘held’ column. The zuul-scheduler and zuul-web services need to be restarted together for the change to take effect.

*   Previously the SqlReporter would record the job name in the database in place of the url if the url was empty. This has now been updated to store a null in the database for that case. Zuul will automatically run a database migration to correct old values.

*   The -d switch doesn’t enforce foreground anymore. It only enables debug logging. To start zuul in foreground please add the -f switch instead.

*   Support for running Zuul under Python 3.5 has been dropped.

*   As further integration with the web interface is planned, the [web.root](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-web.root "attr-web.root") setting in `zuul.conf` is marked required and future releases may error if it is missing. Please add it to your configuration now. See [tenant.web-root](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.web-root "attr-tenant.web-root") for additional information about whitelabel tenants.

*   The components zuul-scheduler and zuul-web now require database configuration. There is now only one supported database connection. If multiple sql connections have been configured only the first one will be used.

*   Signal based triggering of full-reconfiguration in the scheduler (deprecated since 3.3.0) has been removed. Use 
```
zuul-scheduler
full-reconfigure
```
 instead.

*   The [zookeeper](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper "attr-zookeeper") section in `zuul.conf` is required for all components, and all components must now be able to connect to ZooKeeper. Additionally, TLS is now required for all ZooKeeper connections. See [Encrypted Connections](https://zuul-ci.org/docs/zuul/latest/howtos/zookeeper.html#zk-encrypted-connections) for more details.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-deprecation-notes "Link to this heading")

*   Defining database connections using sql connection is now deprecated. Refer to [Database](https://zuul-ci.org/docs/zuul/latest/configuration.html#database) how to configure the database now.

*   REST API: authorizations: the /api/user/authorizations endpoint is deprecated in favor of the tenant-scoped endpoint. It will be removed next release.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-4-0-0-bug-fixes "Link to this heading")

*   Although the documentation states that the MQTT reporter reports the build’s log_url, this was only true as long as `tenant.report-build-page` was disabled. As soon as the setting was enabled, the MQTT reporter reported the url to the build’s result page in Zuul. As MQTT is meant to be consumed by machines, this broke use cases like log post processing.

This was fixed so that the [<mqtt schema>.buildset.builds.log_url](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#attr-%3Cmqtt%20schema%3E.buildset.builds.log_url "attr-<mqtt schema>.buildset.builds.log_url") now always contains the log url, while an additional field [<mqtt schema>.buildset.builds.web_url](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#attr-%3Cmqtt%20schema%3E.buildset.builds.web_url "attr-<mqtt schema>.buildset.builds.web_url") contains the url to the build’s result page if `tenant.report-build-page` is enabled.

3.19.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1-security-issues "Link to this heading")

*   A long-standing security vulnerability regarding executing code on the executor was corrected.

The Zuul executor was designed to prohibit executing command or shell tasks on the executor itself (i.e., localhost in Ansible) from untrusted playbooks. Tobias Henkel discovered that this check has been broken for some time, likely since June of 2018.

The use of bubblewrap means that any commands executed via this vulnerability would still be contained within the restricted environment, meaning that they can not access files outside of the build directory or continue running longer than the job. However, by executing arbitrary commands, users may have been able to connect to unprotected internal network services.

Because this bug is so long-standing, it is possible, even likely, that users may have accidentally come to rely on it. We discovered two jobs in the zuul-jobs library which did so: dco-license and promote-docker-image. The promote-docker-image job has been altered so it no longer needs to run a command on the executor. The dco-license job has been altered to run on a node. If you would prefer to run it on the exceutor, you can create a new job in a config-project that uses the validate-dco-license role.

You may want to look for other jobs in your system which may be affected by this. To aid in that, we have created a script which will examine the job-output.json files created by previous builds and output any tasks it finds which are now (once again) prohibited. This script is available here:

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-1-bug-fixes "Link to this heading")

*   The dependency on kazoo has been upgraded to 2.8.0 which has an important fix for using Zookeeper over TLS.

*   The Github access token URL has been updated in order to remove a deprecation warning.

3.19.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Prelude[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-prelude "Link to this heading")

This is expected to be the last 3.x release of Zuul (barring any unanticipated bugfix releases).

The next release of Zuul, 4.0.0, will require the following deployment changes:

> *   TLS ZooKeeper connections
> 
> *   Network connectivity from all components to ZooKeeper
> 
> *   A SQL database

These features are supported now, so it is important that you take this time to [switch your ZooKeeper connection to use TLS](https://zuul-ci.org/docs/zuul/latest/howtos/zookeeper.html#zk-encrypted-connections), and [configure a SQL connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#database). Even though only some Zuul components connect to ZooKeeper today, you should ensure that the `[zookeeper]` section is present in `zuul.conf` for all components, and that they have network connectivity to the ZooKeeper servers. Doing so will make the upgrade to 4.0.0 seamless.

These changes are in support of ongoing work to enable multiple scheduler processes for scaling and availability. After the 4.0.0 release, it is anticipated that further upgrades to Zuul made in support of this work will be done with minimal disruption in the course of normal releases.

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-new-features "Link to this heading")

*   Zuul now supports whitelisting and configuring ansible callbacks with [ansible_callback “<name>”](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-ansible_callback%20%22%3Cname%3E%22 "attr-ansible_callback \"<name>\"").

*   Pipelines now provide a [pipeline.dequeue](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.dequeue "attr-pipeline.dequeue") reporter action so that reporters may run whenever an item is dequeued. The dequeue reporters will only apply if the item wasn’t a success or failure.

*   Support for generating dynamic [Badges](https://zuul-ci.org/docs/zuul/latest/howtos/badges.html#badges) has been added.

*   The annotation levels for the file comments reported via Github checks API are now configurable in `zuul_return`. Each file comment entry can provide an optional `level` parameter `[info|warning|error]` that will be picked up by the Github reporter.

For more details on how to provide file comments from Zuul, see the documentation of the [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values).

*   The status pipeline requirements of the Github driver [pipeline.require.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.status "attr-pipeline.require.<github source>.status") now also matches on statuses reported via the Github checks API.

*   The tenant configuration now supports loading a different branch than master from config projects. See [tenant.config-projects.<project>.load-branch](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.config-projects.%3Cproject%3E.load-branch "attr-tenant.config-projects.<project>.load-branch").

*   Zuul now matches tag items against their containing branches. This makes it simpler to have release jobs in-tree. See [job.branches](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.branches "attr-job.branches") for details.

*   The zuul-executor now also pauses all merger related tasks when it’s paused. Further the zuul-merger can also be paused by running `zuul-merger pause`.

*   The [serial](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.serial "value-pipeline.manager.serial") pipeline manager has been added. It is designed to handle serialized deployment pipelines where supercedent is unsuitable in the case that not all jobs run on every merge.

*   Add new timezone selector in web interface

*   Zuul now supports a TLS secured connection to ZooKeeper.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-upgrade-notes "Link to this heading")

*   Support for Ansible 2.6 has been removed.

*   Ansible 2.7 is now deprecated since it only receives security updates and will be end of life soon.

*   Zuul now defaults to Ansible 2.9 if no version is specified.

*   With GitHub the Zuul app now requires permissions to read/write check runs.

*   The default behavior of the `tools/encrypt_secret.py` helper script is now to strip incoming input of leading and trailing whitespace. A new `--no-strip` option has been added to support people with secrets that contain valid leading or trailing whitespace.

*   Please configure your Zuul to use TLS secured connection. Running Zuul with an unsecured connection to ZooKeeper is deprecated and will be unsupported in a future release. See [zookeeper](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper "attr-zookeeper") for details.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-security-issues "Link to this heading")

*   Zuul no longer adds environment variables starting with the `ZUUL_` prefix to ansibles environment which could result in secrets being exposed.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-19-0-bug-fixes "Link to this heading")

*   In some cases (such as when an older version of kubectl is present on the executor, or the kubectl on the executor is from OpenShift), streaming logs from Kubernetes or OpenShift pods did not work. The log streaming system has been corrected to work with a wider range of kubectl versions and error logging has been improved.

3.18.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-new-features "Link to this heading")

*   The Github driver can now report file comments via Github checks API. If a github reporter is configured to use the checks API, file comments provided via `zuul_return` will automatically be reported to the pull request in Github.

For more details on how to provide file comments from Zuul, see the documentation of the [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values).

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-upgrade-notes "Link to this heading")

*   Kubectl and socat must now be installed on Zuul executors if using Kubernetes or OpenShift pod resources from Nodepool. Additionally, Nodepool version 3.12.0 or later is required, and the “start-zuul-console” role from zuul-jobs should be run in the pre-playbook of your base job.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-deprecation-notes "Link to this heading")

*   Running the zuul processes with the -d switch to enforce running in foreground is now deprecated. Switch to use -f instead for this purpose. The -d switch will change to just enable debug logging in the future.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-security-issues "Link to this heading")

*   The add_host host-vars blacklist is no longer effective for trusted playbook.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-18-0-bug-fixes "Link to this heading")

*   Previously, no output from shell or command tasks on pods was placed in the job output; that has been corrected and streaming output is now available.

3.17.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0-new-features "Link to this heading")

*   The Github driver now has a basic support for the Github checks API. To enable reporting build results via the checks API one can configure the the new [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check") attribute on the Github reporter. It’s also possible to trigger on a requested or completed [check_run](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.check_run "value-pipeline.trigger.<github source>.event.check_run").

To be able to use the checks API, zuul must be authenticated as Github app. For more information about the necessary requirements, please see the [GitHub](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-driver) driver documentation.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-17-0-security-issues "Link to this heading")

*   The add_host module attributes that can be used to bypass localhost command execution are now also blacklisted using extra-vars to prevent abuse through untrusted host_vars.

3.16.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-1-bug-fixes "Link to this heading")

*   When using GitHub app authentication the fallback to anonymous access was broken for repositories not having installed the zuul app.

3.16.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-new-features "Link to this heading")

*   A new tenant option [tenant.disallowed-labels](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.disallowed-labels "attr-tenant.disallowed-labels") (similar to [tenant.allowed-labels](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-labels "attr-tenant.allowed-labels")) can be used to restrict what labels a tenant has access to.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-upgrade-notes "Link to this heading")

*   The default for auth_type has changed from `digest` to `basic`. Digest authentication has not been supported in Gerrit since version 2.15.

If your Zuul connects to an older version of Gerrit via HTTP authentication, you may now need to explicitly set this value.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-16-0-deprecation-notes "Link to this heading")

*   Authentication: the JWT driver “RS256withJWKS” is deprecated in favor of the “OpenIDConnect” driver. The “OpenIDConnect” driver simplifies configuration for administrators and is better aligned with OIDC configuration discovery conventions.

3.15.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-15-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-15-0-bug-fixes "Link to this heading")

*   Files matcher has been fixed to act like irrelevant files matcher when no files are present in the tested change, i.e. it now matches such empty changes instead of rejecting them.

3.14.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0-new-features "Link to this heading")

*   Zuul now supports triggering a smart reconfiguration by using the command `zuul-scheduler smart-reconfigure`.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-14-0-upgrade-notes "Link to this heading")

*   Zuul no longer supports Ansible 2.5 for running jobs.

3.13.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0-new-features "Link to this heading")

*   Zuul now supports Ansible 2.9 for running jobs.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-13-0-upgrade-notes "Link to this heading")

*   The default version of Ansible used by Zuul jobs has been changed to 2.8. See [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version") for more information.

*   As a result of switching to Ansible 2.8, it is possible for the ansible_python_interpreter version of your nodeset to change to ‘auto’. This could result in your jobs now running under a different version of python than prior to this release. See [Ansible and Python 3](https://zuul-ci.org/docs/zuul/latest/operation.html#ansible-and-python-3) for additional info.

*   Ansible 2.6 for Zuul jobs has been marked deprecated and will be removed in a future release.

3.12.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-new-features "Link to this heading")

*   A new executor option [executor.merge_jobs](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.merge_jobs "attr-executor.merge_jobs") has been added to toggle global merge operations.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-upgrade-notes "Link to this heading")

*   The Gerrit driver now has an additional option, [pipeline.reporter.<gerrit reporter>.comment](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reporter.%3Cgerrit%20reporter%3E.comment "attr-pipeline.reporter.<gerrit reporter>.comment") which may be used to suppress reporting job results as review comments. Due to the configuration syntax for Gerrit reporters, the word “comment” may no longer be used as a review label.

### Other Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-12-0-other-notes "Link to this heading")

*   The –id option to both the autohold-delete and autohold-info zuul CLI commands has been removed.

3.11.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-1-bug-fixes "Link to this heading")

*   Fixed a regression where changes with a failing job with soft dependencies would remain in the queue indefinitely.

3.11.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0-new-features "Link to this heading")

*   Added the [pipeline.enqueue](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.enqueue "attr-pipeline.enqueue") reporter action so that reporters may be run when an item is enqueued into a pipeline.

*   Added the [pipeline.no-jobs](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.no-jobs "attr-pipeline.no-jobs") reporter action so that reporters may be run when an item is dequeued into a pipeline without having run any jobs.

*   A new zuul CLI command, autohold-info, has been added to retrieve full details for an existing autohold request.

*   Autohold requests are now stored in ZooKeeper, rather than in memory. As a result of this change, a new zuul CLI command, autohold-delete has been added to remove existing requests.

*   New scheduler options, max_hold_expiration and default_hold_expiration, are added to control how long nodes held for an autohold request remain available. The max_hold_expiration option defaults to 0, which means the held nodes will not automatically expire, and default_hold_expiration defaults to the value of max_hold_expiration.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-11-0-upgrade-notes "Link to this heading")

*   The Gerrit driver will now perform query actions over HTTP if an HTTP password is configured. In this situation, the SSH connection is now only used for receiving events. The HTTP password is not required, but it is recommended since it provides more reporting options (including line comments).

3.10.2[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-new-features "Link to this heading")

*   The maximum starting builds depending on cpu cores can be limited using executor.max_starting_builds configuration.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-security-issues "Link to this heading")

*   The synchronize rsh rsync_opts is now prohibited for security reasons as it could be used to circumvent executor host command execution restrictions.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-2-bug-fixes "Link to this heading")

*   Under specific conditions Zuul could fail to properly update git repos causing it to fall back to testing master. If jobs were meant to run against commits other than current master this lead to testing the wrong commit. Zuul now correctly updates repos and should test the correct commit in all cases.

Specifically this could happen if a new branch was created off a commit in an existing branch. Then the first proposed change to this new branch would be tested against master instead.

3.10.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-1 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-1-bug-fixes "Link to this heading")

*   Fixed Zuul dashboard not loading properly due to javascript dependencies missing.

3.10.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0 "Link to this heading")
--------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0-new-features "Link to this heading")

*   Allow users to perform tenant-scoped, privileged actions either through zuul-web’s REST API or zuul’s client, based on the JWT standard. The users need a valid bearer token to perform such actions; the scope is set by matching conditions on tokens’ claims; these conditions can be defined in zuul’s tenant configuration file. Zuul supports token signing and validation using the HS256 or RS256 algorithms. External JWKS are also supported for token validation only. Current tenant-scoped actions are “autohold”, “enqueue” and “dequeue”.

*   Config projects may now add any job to any project’s pipelines, regardless of the setting of allowed-projets (including the implicit setting of allowed-projects on jobs with secrets in untrusted projects).

*   It is now possible to select the merge method GitHub uses to merge a Pull Request to the base branch.

*   A new option, [tenant.untrusted-projects.<project>.extra-config-paths](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.extra-config-paths "attr-tenant.untrusted-projects.<project>.extra-config-paths") has been added to allow an admin to indicate that Zuul should load extra configuration data from a specific project in a tenant.

This feature may be useful to allow a project that primarily holds shared jobs or roles to include additional in-repo configuration for its own testing (which may not be relevant to other users of the project).

*   The merge-mode `squash-merge` is now supported for Github.

*   The [job.cleanup-run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.cleanup-run "attr-job.cleanup-run") attribute has been added to enable a new cleanup phase to be performed after a job execution.

*   Support for the Pagure code review system has been added.

*   Pipelines may now indicate that they supercede other pipelines with the [pipeline.supercedes](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.supercedes "attr-pipeline.supercedes") attribute.

When a change is enqueued in a pipeline which supercedes others, it will be removed from the other pipelines. For example, a [gate](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-gate) pipeline may supercede a [check](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-check) pipeline so that test resources are not spent running near-duplicate jobs simultaneously.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-10-0-upgrade-notes "Link to this heading")

*   If unprotected branches are excluded on a project they now also get filtered out from jobs.

*   The default value for the [executor.job_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.job_dir "attr-executor.job_dir") configuration setting has been changed from `/tmp` to `/var/lib/zuul/builds`. It is important for [executor.job_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.job_dir "attr-executor.job_dir") and [executor.git_dir](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.git_dir "attr-executor.git_dir") to be located on the same filesystem, so this change increases the chances that they end up on the same filesystem in most default configurations.

The `builds` subdirectory will be created if it does not exist, however, `/var/lib/zuul` at least must exist and be writable by the Zuul user.

*   Jobs with file matchers will now automatically match if the configuration of the job is changed. This means that the Zuul configuration file no longer needs to be included in the list of files to match in order for changes to job configuration to be self-testing.

To keep the old behavior, set [job.match-on-config-updates](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.match-on-config-updates "attr-job.match-on-config-updates") to `False`.

3.9.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-9-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-9-0-new-features "Link to this heading")

*   Zuul now supports ansible 2.8 for running jobs.

*   Zuul now supports [project.<pipeline>.fail-fast](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.%3Cpipeline%3E.fail-fast "attr-project.<pipeline>.fail-fast") to immediately report and cancel builds on the first failure in a buildset.

*   Zuul now reports resource usage statistics if they are provided by nodepool.

The following statistics are emitted:

    *   zuul.nodepool.resources.tenant.{tenant}.{resource}: Gauge with the currently used resources by tenant and counter with the summed usage by tenant. e.g. cpu seconds

    *   zuul.nodepool.resources.project.{project}.{resource}: Gauge with the currently used resources by project and counter with the summed usage by project. e.g. cpu seconds

3.8.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-1-bug-fixes "Link to this heading")

*   Fixed a memory leak introduced in 3.8.0.

3.8.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-new-features "Link to this heading")

*   The [artifacts](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-artifacts) returned by parent jobs are now also available in child jobs of the same buildset.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-security-issues "Link to this heading")

*   Fixed a bug where config (trusted) layout updates could be used pre-merge as a dynamically loaded layout. This could happen if Zuul was running with config errors that originated from outside of the config (trusted) repo. A logic error allowed code to fall through and return the trusted layout in this case.

Users should upgrade.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-8-0-bug-fixes "Link to this heading")

*   Jobs which use the [job.requires](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.requires "attr-job.requires") attribute and fail to have their requirements met are now recorded as “FAILED” rather than “SKIPPED”. This can happen if an earlier job which is expected to produce artifacts fails to do so due to an error.

3.7.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-1-bug-fixes "Link to this heading")

*   When using Ansible 2.7 the uri module crashed with a module failure.

*   The [scheduler.default_ansible_version](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.default_ansible_version "attr-scheduler.default_ansible_version") has been ignored.

3.7.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0-new-features "Link to this heading")

*   The ansible_python_interpreter variable is now whitelisted for the add_host task.

*   Zuul now supports ansible 2.6 for running jobs.

*   Zuul now supports ansible 2.7 for running jobs.

*   Jobs may now specify which ansible version is used to run them. The ansible version to use can now be specified by [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version").

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-7-0-upgrade-notes "Link to this heading")

*   The default ansible version is now 2.7. In case this breaks any jobs this can be overridden in [job.ansible-version](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.ansible-version "attr-job.ansible-version"), [tenant.default-ansible-version](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.default-ansible-version "attr-tenant.default-ansible-version") or [scheduler.default_ansible_version](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.default_ansible_version "attr-scheduler.default_ansible_version")

*   The `user` value in the `[fingergw]` configuration section previously defaulted to `zuul`, but now is unset by default, which will cause fingergw not to drop privileges. It is recommended that this value be explicitly set to an unprivileged user.

*   In order to support several ansible versions installed simultaneously Zuul now handles them itself in virtual environments. By default Zuul installs the needed ansible versions on startup so there is no further user action required. However it is recommended to pre-install the ansible environments during installation by invoking `zuul-manage-ansible`.

*   The `hosts` value in the `[zookeeper]` configuration section previously defaulted to `localhost:2181`, but now is unset by default. This value is required and must be explicitly set (and the documentation has always indicated this).

3.6.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-1-security-issues "Link to this heading")

*   The raw module had not been blocked for local tasks. This could be used to bypass protection and execute commands on the executor.

3.6.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0-new-features "Link to this heading")

*   Artifacts may now include a metadata field for storing arbitrary metadata about the artifacts in the SQL database.

*   The [job.run](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.run "attr-job.run") attribute now supports a single or list of playbooks.

*   Support for expressing artifact or other resource dependencies between jobs running on different changes with a dependency relationship (e.g., a container image built in one project and consumed in a second project) has been added via the [job.provides](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.provides "attr-job.provides") and [job.requires](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.requires "attr-job.requires") job attributes.

*   The [job.dependencies](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.dependencies "attr-job.dependencies") attribute may now be used to express “soft” dependencies – that is, to indicate a job should run after another completes, but only if it runs at all. For example, a deployment job which should always run, but depends on a build job which only runs if the source code is changed.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-6-0-upgrade-notes "Link to this heading")

*   Service Workers are now disabled by default in the Javascript dashboard. Deployers who wish to enable them need to set `REACT_APP_ENABLE_SERVICE_WORKER`

*   Zuul recently added the job variable [zuul.message](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.message "var-zuul.message"). This can contain jinja tags which can cause problems accessing the zuul variable in the job. Because of this the message is now base64 encoded and any job evaluating this variable needs to be changed from `{{ zuul.message }}` to `{{ zuul.message | b64decode }}`.

3.5.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-new-features "Link to this heading")

*   The [executor.min_avail_mem](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.min_avail_mem "attr-executor.min_avail_mem") setting now takes cgroup limits into account. There is also a new metric zuul.executor.<executor>.pct_used_ram_cgroup available.

*   The [job.secrets.pass-to-parent](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.secrets.pass-to-parent "attr-job.secrets.pass-to-parent") attribute has been added to allow secrets to be made available to playbooks in parent jobs (for example, to allow for jobs which are designed to use secrets, but leave it to child jobs to actually supply them). See also the [Secret](https://zuul-ci.org/docs/zuul/latest/config/secret.html#secret) documentation.

*   The restriction on using `known_hosts` in playbooks has been lifted.

*   The executors emit a new timer [zuul.executor.<executor>.starting_builds](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.starting_builds "stat-zuul.executor.<executor>.starting_builds") with the time jobs spent during starting.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-upgrade-notes "Link to this heading")

*   The zuul_return module has been converted to an Ansible action plugin. Job playbooks no longer need to use delegate_to or a localhost only play with this module as action plugin by default run on localhost.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-security-issues "Link to this heading")

*   Jobs with secrets in untrusted projects now automatically set allowed-projects.

It is possible to circumvent the use of allowed-projects in untrusted projects by creating a change which Depends-On a change which alters a project definition. This behavior may be unexpected, so documentation has been updated with warnings to avoid relying on it in sensitive cases.

It may have been possible to expose a secret, or use resources protected by a secret, if a job using a secret was defined in an untrusted project on a system with an independent pre-merge post-review pipeline – that is, a pipeline with post-review set to true, manager set to independent, and which operated on changes before they merged.

To prevent disclosure or use in this situation, allowed-projects is now automatically set to the current project when a secret is used in a job defined in an untrusted project, and it can not be overridden.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-5-0-bug-fixes "Link to this heading")

*   Untrusted playbooks no longer see ‘Adding hosts ssh with ansible_user to the inventory is prohibited’ when using the add_host Ansible task on localhost.

*   Fixed an issue where a trailing slash on the baseurl of a git driver connection config could cause an indefinite job hang.

3.4.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0-new-features "Link to this heading")

*   Jobs may now return artifact URLs and they will be stored in the SQL database (if configured). See [Returning artifact URLs](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-artifacts) for usage.

*   One or more zuul executors can now be added to a [executor.zone](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-executor.zone "attr-executor.zone"). This is helpful if a cloud does not have any public IP addresses for nodepool nodes. Now you’ll be able to have a zuul executor on the same private network as your nodepool nodes.

*   The Ansible inventory file now includes nodepool.host_id variable if the node was launched using the OpenStack Nodepool driver.

*   A new scheduler option, [scheduler.relative_priority](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.relative_priority "attr-scheduler.relative_priority"), can be used to instruct Nodepool to fulfull requests from less-busy projects more quickly.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-4-0-upgrade-notes "Link to this heading")

*   The zuul.nodepool statistics have been moved under zuul.nodepool.requests to allow sub-stats to work correctly. For example zuul.nodepool.requested has become zuul.nodepool.requests.requested.total. The previously missing label and size counters are now available at zuul.nodepool.requests.<state>.<size|label>. For more info see the monitoring documentation.

*   The zuul-web service now requires access to ZooKeeper, as a result you may need to update your firewall allow access from the service. Additionally, zuul.conf should now contain a [zookeeper](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-zookeeper "attr-zookeeper") configuration section.

3.3.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-new-features "Link to this heading")

*   New tenant options [tenant.allowed-triggers](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-triggers "attr-tenant.allowed-triggers") and [tenant.allowed-reporters](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-reporters "attr-tenant.allowed-reporters") can be used to restrict what connections a tenant has access to.

*   A new tenant option [tenant.allowed-labels](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.allowed-labels "attr-tenant.allowed-labels") can be used to restrict what labels a tenant has access to.

*   A job using a semaphore now can configure if it should acquire the it before requesting resources or just before running.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-upgrade-notes "Link to this heading")

*   The acquiring behavior of jobs with semaphores has been changed. Up to now a job requested resources and aquired the semaphore just before it started to run. However this could lead to a high amount of resource waste. Instead jobs now acquire the semaphore before requesting the resources by default. This behavior can be overridden by jobs using job.semaphores.resources-first if some waste of resources is acceptable.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-security-issues "Link to this heading")

*   The add_host module options are restricted to a hostname, port, user and password. Previously, malicious options could be used to bypass protection and execute tasks on the executor. Only ssh and kubectl connection are authorized.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-1-bug-fixes "Link to this heading")

*   Jobs that encountered unreachable nodes are now correctly detected and retried.

3.3.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-new-features "Link to this heading")

*   A local project key file URI (eg. `file:///path/to/key.pub`) is now supported by the encrypt_secret.py tool. This allows encrypting secrets without directly accessing the Zuul web API to retrieve the project key.

*   Zuul now supports triggering a full reconfiguration by using the command `zuul-scheduler full-reconfigure`.

*   The Gerrit driver can now (optionally) report via HTTP instead of SSH. In the future, this will be used to report file and line comments (the SSH API only supports review messages).

*   Zuul now supports leaving file comments, though currently only when using the Gerrit driver. See the documentation for `zuul_return` for details.

*   A job now can pause itself using [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values) and let the child jobs run until they are finished. This can be used to serve some service which can be used by the child jobs.

*   An SSH keypair is now generated for every project and may be used in post-review jobs to access systems which trust that project.

*   GitHub [<github connection>.rate_limit_logging](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.rate_limit_logging "attr-<github connection>.rate_limit_logging") now can be configured. If disabled this can save some network round trip times. This can be configured per connection.

*   The Zuul web dashboard has been rewritten in React.

*   The restriction on using `add_host` in playbooks has been lifted.

*   A new Build page in the web interface enable displaying a single Build information.

*   A new Notification Drawer and a ConfigErrors page in the web interface enable displaying the config-errors endpoint data.

*   A new Job page in the web interface enable browsing through job configuration.

*   Client certificate locations to be used by winrm connections can be configured now.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-upgrade-notes "Link to this heading")

*   The Zuul web dashboard is now a single index.html and static offload server needs new rewrite rules. Check the install instruction for backward compatible rewrite rules. Note that serving the web dashboard from a sub-directory requires the application to be rebuilt using the desired homepage location.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-3-0-deprecation-notes "Link to this heading")

*   Signal based triggering of a full reconfiguration via sending SIGHUP to the zuul-scheduler PID is deprecated. Use the command `zuul-scheduler full-reconfigure` now.

3.2.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0-new-features "Link to this heading")

*   Zuul client got a new command ‘tenant-conf-check’. This command validates the schema of the tenant configuration and exits -1 if errors have been detected.

*   A new Ansible inventory variable [zuul.child_jobs](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.child_jobs "var-zuul.child_jobs") which is a list of the first level child jobs to be run after a job has finished successfully.

*   Jobs are now able to use the [job.extra-vars](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.extra-vars "attr-job.extra-vars") which will use the –extra-vars flag when a job runs.

*   Project and project-templates may now create variables via a `vars` configuration entry. Jobs can access these at runtime in the same manner as job variables.

*   The [supercedent](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#value-pipeline.manager.supercedent "value-pipeline.manager.supercedent") pipeline manager has been added. It is designed to make post-merge artifact build pipelines more efficient.

*   The dequeue command has been added to the Zuul CLI. It allows operators to stop a given buildset at will.

*   It is now possible to use zuul_return to skip child jobs. You can use the [zuul.child_jobs](https://zuul-ci.org/docs/zuul/latest/job-content.html#var-zuul.child_jobs "var-zuul.child_jobs") inventory variable to get a list of child jobs configured to run, then use zuul_return to modify the list. Any child job not in zuul_return zuul.child_jobs will be skipped. See [Return Values](https://zuul-ci.org/docs/zuul/latest/job-content.html#return-values) for examples.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-2-0-bug-fixes "Link to this heading")

*   Project Templates are now branch-aware and behave more like project stanzas. If a template is defined on a branch, it will only apply to changes to that branch.

*   The timer trigger does not enqueue an event for every branch of every project anymore and it now only processes projects actually using the pipeline triggered by a timer.

3.1.0[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-new-features "Link to this heading")

*   The GitHub driver can determine the required status checks of pull requests which are needed for entering a gate pipeline. This eliminates the need to hard code required status checks in the gate pipeline and makes interoperation with other GitHub apps much more flexible.

*   Zuul is now ables to start with an invalid configuration. When reading configuration files from project repositories, if an issue is detected, Zuul will store the issue and skip the broken block of configuration. Issues are then reported in the scheduler log at the end of the configuration phase.

*   A [<mqtt connection>](https://zuul-ci.org/docs/zuul/latest/drivers/mqtt.html#attr-%3Cmqtt%20connection%3E "attr-<mqtt connection>") driver is added to feature build report over MQTT message.

*   The GitHub driver now supports the [pipeline.require.<github source>.merged](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.merged "attr-pipeline.require.<github source>.merged") requirement.

*   The json log now also contains the role name and the uuid similar to the task entry.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-upgrade-notes "Link to this heading")

*   Files (and irrelevant-files) matchers are now overridable. Zuul now uses only branch matchers to collect job variants. Once those variants are collected, they are combined, and the files and irrelevant-files attributes are inherited and overridden as any other job attribute. The final values are used to determine whether the job should ultimately run.

*   Zuul now uses Ansible 2.5.

### Security Issues[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-security-issues "Link to this heading")

*   Tobias Henkel (BMW Car IT GmbH) discovered a vulnerability which is fixed in this release. If nodes become offline during the build, the no_log attribute of a task is ignored. If the unreachable error occurred in a task used with a loop variable (e.g., with_items), the contents of the loop items would be printed in the console. This could lead to accidentally leaking credentials or secrets. MITRE has assigned CVE-2018-12557 to this vulnerability.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-1-0-bug-fixes "Link to this heading")

*   Untrusted playbooks no longer see ‘Executing local code is prohibited’ when using the zuul_return Ansible task.

3.0.3[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-new-features "Link to this heading")

*   The [project.default-branch](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.default-branch "attr-project.default-branch") option is now documented. It has been supported since version 3.0.0, but was omitted from the documentation.

*   Project stanzas now support regex matching of [project.name](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.name "attr-project.name"). This can be used to apply project pipelines to many projects at once.

### Deprecation Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-deprecation-notes "Link to this heading")

*   The `merge-mode` and `default-branch` attributes may no longer appear in a [Project Template](https://zuul-ci.org/docs/zuul/latest/config/project.html#project-template) stanza.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-3-bug-fixes "Link to this heading")

*   Configuration loading for dynamic configuration changes (i.e., changes to `zuul.yaml` files) is now significantly more CPU and memory efficient, incurring only a slight penalty compared to normal changes.

3.0.2[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-new-features "Link to this heading")

*   The GitHub trigger status filter [status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.status "value-pipeline.trigger.<github source>.action.status") and pipeline requirements [pipeline.require.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.status "attr-pipeline.require.<github source>.status") now support regular expression matching.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-upgrade-notes "Link to this heading")

*   The `fb-re2` python library is added as a dependency; this may required the installation of the `re2` library and header files in order to build.

*   The build start and end times are now stored as UTC in the database. Since there is no localization done on zuul web side, the zuul api also exposes these times as UTC now.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-2-bug-fixes "Link to this heading")

*   Story 2001441 is fixed. Failure by one Zuul reporter will not short circuit the reporting of other reporters. This ensures as much information as possible is reported for each change even if some failures occur. Note that the build set status is changed to ‘ERROR’ after the first failed reporter.

*   The zuul-changes.py script has been adapted to the new zuul-web api routes.

3.0.1[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1 "Link to this heading")
------------------------------------------------------------------------------------------------------

### New Features[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-new-features "Link to this heading")

*   Git repositories will have a `origin` remote with refs pointing to the previous change in the speculative state.

This allows jobs to determine the commits that are part of a change, which was not possible before. The remote URL is set to a bogus value which won’t work with git commands that need to talk to the remote repository.

*   PostgreSQL is now officially supported as database backend. See `sql connection` on how to configure database connections.

*   A new option for the scheduler [scheduler.tenant_config_script](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config_script "attr-scheduler.tenant_config_script") can be used to tell Zuul to execute a script and read its yaml output as the tenants configuration. The option is exclusive with the [scheduler.tenant_config](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.tenant_config "attr-scheduler.tenant_config") option.

### Upgrade Notes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-upgrade-notes "Link to this heading")

*   The alembic version table is fixed to being prefixed too. This is necessary when using `table_prefix`. However if you are already using `table_prefix` you will need to rename the table `alembic_version` to `<prefix>alembic_version` before starting Zuul. Otherwise zuul will try to create the tables again and fail. If you’re not using `table_prefix` you can safely ignore this.

### Bug Fixes[](https://zuul-ci.org/docs/zuul/latest/releasenotes.html#relnotes-3-0-1-bug-fixes "Link to this heading")

*   Zuul role repository checkouts now honor [job.override-checkout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.override-checkout "attr-job.override-checkout").

Previously, when a Zuul role was specified for a job, Zuul would usually checkout the master branch, unless that repository appeared in the dependency chain for a patch. It will now follow the usual procedure for determining the branch to check out, including honoring [job.override-checkout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.override-checkout "attr-job.override-checkout") options.

This may alter the behavior of currently existing jobs. Depending on circumstances, you may need to set [job.override-checkout](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.override-checkout "attr-job.override-checkout") or copy roles to other branches of projects.
