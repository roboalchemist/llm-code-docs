# Source: https://zuul-ci.org/docs/zuul/latest/drivers/github.html

Title: GitHub — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/github.html

Markdown Content:
The GitHub driver supports sources, triggers, and reporters. It can interact with the public GitHub service as well as site-local installations of GitHub enterprise.

Configure GitHub[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#configure-github "Link to this heading")
---------------------------------------------------------------------------------------------------------------------

Zuul needs to receive notification of events from GitHub, and it needs to interact with GitHub in response to those events. There are two options available for configuring these connections. A GitHub project’s owner can either manually setup a web-hook or install a GitHub Application. In the first case, the project’s owner needs to know the Zuul endpoint and the webhook secrets and configure them manually. In the second, the project (or organization) owner need only install pre-existing GitHub Application into the project or organization.

In general, the Application method is recommended. Both options are described in the following sections.

Regardless of which option is chosen, there are several types of authentication between Zuul and GitHub used for various purposes. Some are required and some are optional depending on the intended use and configuration.

In all cases Zuul needs to authenticate messages received from GitHub as being valid. To do this a webhook_token is configured.

Zuul also needs to authenticate to GitHub to make certain requests. At a high level, this is the sort of authentication that is required for various Zuul Github functionality:

> *   Reporting: Requires authentication with write access to the project so that comments can be posted.
> 
> *   Enqueuing a pull request (including Depends-On: of a pull request): The API queries needed to examine PR’s so that Zuul can enqueue them requires authentication with read access.
> 
> *   [job.required-projects](https://zuul-ci.org/docs/zuul/latest/config/job.html#attr-job.required-projects "attr-job.required-projects") listing: No authentication required. For example, you may have a project where you are only interested in testing against a specific branch of a GitHub project. In this case you do not need any authentication to have Zuul pull the project. However, note that if you will ever need to speculatively test a PR in this project, you will require authenticated read access (see note above).

There are two different ways Zuul can Authenticate its requests to GitHub. The first is the api_token. This api_token is used by the web-hook option for all authentication. When using the GitHub Application system Zuul uses an app_id and app_key which is used to generate an application token behind the scenes. But this only works against projects that have installed your application. As a fallback for interaction with projects that haven’t installed your application you can also configure an api_token when using the application system. This is particularly useful for supporting Depends-On functionality against GitHub projects.

Finally, authenticated requests receive much larger GitHub API rate limits. It is worthwhile to configure both an app_id/app_key and api_token when operating in application mode to avoid rate limits as much as possible.

### Web-Hook[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#web-hook "Link to this heading")

To configure a project’s [webhook events](https://developer.github.com/webhooks/creating/):

*   Set _Payload URL_ to `http://<zuul-hostname>:<port>/api/connection/<connection-name>/payload`.

*   Set _Content Type_ to `application/json`.

Select _Events_ you are interested in. See below for the supported events.

You will also need to have a GitHub user created for your zuul:

*   Zuul public key needs to be added to the GitHub account

*   A api_token needs to be created too, see this [article](https://help.github.com/articles/creating-an-access-token-for-command-line-use/)

Then in the zuul.conf, set webhook_token and api_token.

### Application[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#application "Link to this heading")

To create a [GitHub application](https://developer.github.com/apps/building-integrations/setting-up-and-registering-github-apps/registering-github-apps/):

*   Go to your organization settings page to create the application, e.g.: [https://github.com/organizations/my-org/settings/apps/new](https://github.com/organizations/my-org/settings/apps/new)

*   Set GitHub App name to “my-org-zuul”

*   Set Setup URL to your setup documentation, when user install the application they are redirected to this url

*   Set Webhook URL to `http://<zuul-hostname>:<port>/api/connection/<connection-name>/payload`.

*   Create a Webhook secret

*   Set permissions:

    *   Repository administration: Read

    *   Checks: Read & Write

    *   Repository contents: Read & Write (write to let zuul merge change)

    *   Issues: Read & Write

    *   Pull requests: Read & Write

    *   Commit statuses: Read & Write

*   Set events subscription:

    *   Check run

    *   Commit comment

    *   Create

    *   Push

    *   Release

    *   Issue comment

    *   Issues

    *   Label

    *   Pull request

    *   Pull request review

    *   Pull request review comment

    *   Status

*   Set Where can this GitHub App be installed to “Any account”

*   Create the App

*   Generate a Private key in the app settings page

*   Optionally configure an api_token. Please see this [article](https://help.github.com/articles/creating-an-access-token-for-command-line-use/) for more information.

Then in the zuul.conf, set webhook_token, app_id, app_key and optionally api_token. After restarting zuul-scheduler, verify in the ‘Advanced’ tab that the Ping payload works (green tick and 200 response)

Users can now install the application using its public page, e.g.: [https://github.com/apps/my-org-zuul](https://github.com/apps/my-org-zuul)

Note

GitHub Pull Requests that modify GitHub Actions workflow configuration files cannot be merged by application credentials (this is any Pull Request that edits the .github/workflows directory and its contents). These Pull Requests must be merged by a normal user account. This means that Zuul will be limited to posting test results and cannot merge these PRs automatically when they pass testing.

GitHub Actions are still in Beta and this behavior may change.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#connection-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

There are two forms of operation. Either the Zuul installation can be configured as a [Github App](https://developer.github.com/apps/) or it can be configured as a Webhook.

If the [Github App](https://developer.github.com/apps/) approach is taken, the config settings `app_id`, `app_key` and optionally `api_token` are required. If the Webhook approach is taken, the `api_token` setting is required.

The supported options in `zuul.conf` connections are:

<github connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E "Link to this definition")

<github connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.driver "Link to this definition")

github[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-%3Cgithub%20connection%3E.driver.github "Link to this definition")
The connection must set `driver=github` for GitHub connections.

<github connection>.app_id[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.app_id "Link to this definition")

App ID if you are using a _GitHub App_. Can be found under the **Public Link** on the right hand side labeled **ID**.

<github connection>.app_key[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.app_key "Link to this definition")

Path to a file containing the secret key Zuul will use to create tokens for the API interactions. In Github this is known as **Private key** and must be collected when generated.

<github connection>.api_token[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.api_token "Link to this definition")

API token for accessing GitHub if Zuul is configured with Webhooks. See [Creating an access token for command-line use](https://help.github.com/articles/creating-an-access-token-for-command-line-use/).

<github connection>.webhook_token[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.webhook_token "Link to this definition")

Required token for validating the webhook event payloads. In the GitHub App Configuration page, this is called **Webhook secret**. See [Securing your webhooks](https://developer.github.com/webhooks/securing/).

<github connection>.sshkey[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.sshkey "Link to this definition")

Default:`~/.ssh/id_rsa`

Path to SSH key to use when cloning github repositories if Zuul is configured with Webhooks.

<github connection>.server[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.server "Link to this definition")

Default:`github.com`

Hostname of the github install (such as a GitHub Enterprise).

<github connection>.canonical_hostname[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.canonical_hostname "Link to this definition")

The canonical hostname associated with the git repos on the GitHub server. Defaults to the value of [<github connection>.server](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.server "attr-<github connection>.server"). This is used to identify projects from this connection by name and in preparing repos on the filesystem for use by jobs. Note that Zuul will still only communicate with the GitHub server identified by **server**; this option is useful if users customarily use a different hostname to clone or pull git repos so that when Zuul places them in the job’s working directory, they appear under this directory name.

<github connection>.verify_ssl[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.verify_ssl "Link to this definition")

Default:`true`

Enable or disable ssl verification for GitHub Enterprise. This is useful for a connection to a test installation.

<github connection>.rate_limit_logging[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.rate_limit_logging "Link to this definition")

Default:`true`

Enable or disable GitHub rate limit logging. If rate limiting is disabled in GitHub Enterprise this can save some network round trip times.

<github connection>.repo_cache[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_cache "Link to this definition")

To configure Zuul to use a GitHub Enterprise [repository cache](https://docs.github.com/en/enterprise-server@3.3/admin/enterprise-management/caching-repositories/about-repository-caching) set this value to the hostname of the cache (e.g., `europe-ci.github.example.com`). Zuul will fetch commits as well as determine the global repo state of repositories used in jobs from this host.

This setting is incompatible with [<github connection>.sshkey](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.sshkey "attr-<github connection>.sshkey").

Because the repository cache may be several minutes behind the canonical site, enabling this setting automatically sets the default [<github connection>.repo_retry_timeout](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_retry_timeout "attr-<github connection>.repo_retry_timeout") to 600 seconds. That setting may still be overridden to specify a different value.

<github connection>.repo_retry_timeout[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_retry_timeout "Link to this definition")

This setting is only used if [<github connection>.repo_cache](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_cache "attr-<github connection>.repo_cache") is set. It specifies the amount of time in seconds that Zuul mergers and executors should spend attempting to fetch git commits which are not available from the GitHub repository cache host.

When [<github connection>.repo_cache](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.repo_cache "attr-<github connection>.repo_cache") is set, this value defaults to 600 seconds, but it can be overridden. Zuul retries git fetches every 30 seconds, and this value will be rounded up to the next highest multiple of 30 seconds.

<github connection>.max_threads_per_installation[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-%3Cgithub%20connection%3E.max_threads_per_installation "Link to this definition")

Default:`1`

The GitHub driver performs event pre-processing in parallel before forwarding the events (in the correct order) to the scheduler for processing. By default, this parallel pre-processing is restricted to a single request for each GitHub App installation that Zuul uses when interacting with GitHub. This is to avoid running afoul of GitHub’s abuse detection mechanisms. Some high-traffic installations of GitHub Enterprise may wish to increase this value to allow more parallel requests if resources permit. If GitHub Enterprise resource usage is not a concern, setting this value to `10` or greater may be reasonable.

Trigger Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#trigger-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

GitHub webhook events can be configured as triggers.

A connection name with the GitHub driver can take multiple events with the following options.

pipeline.trigger.<github source>[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E "Link to this definition")

The dictionary passed to the GitHub pipeline `trigger` attribute supports the following attributes:

pipeline.trigger.<github source>.event(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.event "Link to this definition")

Warning

While it is currently possible to list more than one event in a single trigger, that is deprecated and support will be removed in a future version. Instead, specify a single event type per trigger, and list multiple triggers as necessary to cover all intended events.

The event from github. Supported events are:

pull_request[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.pull_request "Link to this definition")pull_request_review[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.pull_request_review "Link to this definition")push[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.push "Link to this definition")check_run[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.check_run "Link to this definition")pipeline.trigger.<github source>.action[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.action "Link to this definition")

A [pull_request](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.pull_request "value-pipeline.trigger.<github source>.event.pull_request") event will have associated action(s) to trigger from. The supported actions are:

opened[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.opened "Link to this definition")
Pull request opened.

changed[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.changed "Link to this definition")
Pull request synchronized.

closed[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.closed "Link to this definition")
Pull request closed.

reopened[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.reopened "Link to this definition")
Pull request reopened.

Comment added to pull request.

labeled[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.labeled "Link to this definition")
Label added to pull request.

unlabeled[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.unlabeled "Link to this definition")
Label removed from pull request.

status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.status "Link to this definition")
Status set on commit. The syntax is `user:status:value`. This also can be a regular expression.

A [pull_request_review](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.pull_request_review "value-pipeline.trigger.<github source>.event.pull_request_review") event will have associated action(s) to trigger from. The supported actions are:

submitted[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.submitted "Link to this definition")
Pull request review added.

dismissed[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.dismissed "Link to this definition")
Pull request review removed.

A [check_run](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.check_run "value-pipeline.trigger.<github source>.event.check_run") event will have associated action(s) to trigger from. The supported actions are:

requested[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.requested "Link to this definition")

Warning

This is deprecated and will be removed in a future version. Use [rerequested](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.rerequested "value-pipeline.trigger.<github source>.action.rerequested") instead.

Deprecated alias for [rerequested](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.rerequested "value-pipeline.trigger.<github source>.action.rerequested").

rerequested[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.rerequested "Link to this definition")
A check run is rerequested.

completed[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.completed "Link to this definition")
A check run completed.

pipeline.trigger.<github source>.branch[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.branch "Link to this definition")

The branch associated with the event. Example: `master`. This field is treated as a regular expression, and multiple branches may be listed. Used for `pull_request` and `pull_request_review` events.

This is only used for `pull_request``comment` actions. It accepts a list of regexes that are searched for in the comment string. If any of these regexes matches a portion of the comment string the trigger is matched. `comment: retrigger` will match when comments containing ‘retrigger’ somewhere in the comment text are added to a pull request.

pipeline.trigger.<github source>.label[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.label "Link to this definition")

This is only used for `labeled` and `unlabeled``pull_request` actions. It accepts a list of strings each of which matches the label name in the event literally. 
```
label:
recheck
```
 will match a `labeled` action when pull request is labeled with a `recheck` label. `label: 'do not test'` will match a `unlabeled` action when a label with name 
```
do not
test
```
 is removed from the pull request.

pipeline.trigger.<github source>.permission[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.permission "Link to this definition")

If present, the account that performed the action must have this permission (or permissions) to match. The available values are `read`, `write`, and `admin`.

pipeline.trigger.<github source>.state[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.state "Link to this definition")

This is only used for `pull_request_review` events. It accepts a list of strings each of which is matched to the review state, which can be one of `approved`, `commented`, `changes_requested`, `dismissed`, or `pending`.

pipeline.trigger.<github source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.status "Link to this definition")

This is used for `pull_request` and `status` actions. It accepts a list of strings each of which matches the user setting the status, the status context, and the status itself in the format of `user:context:status`. For example, `zuul_github_ci_bot:check_pipeline:success`.

pipeline.trigger.<github source>.check[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.check "Link to this definition")

This is only used for `check_run` events. It works similar to the `status` attribute and accepts a list of strings each of which matches the app requesting or updating the check run, the check run’s name and the conclusion in the format of `app:name::conclusion`. To make Zuul properly interact with Github’s checks API, each pipeline that is using the checks API should have at least one trigger that matches the pipeline’s name regardless of the result, e.g. `zuul:cool-pipeline:.*`. This will enable the cool-pipeline to trigger whenever a user requests the `cool-pipeline` check run as part of the `zuul` check suite. Additionally, one could use `.*:success` to trigger a pipeline whenever a successful check run is reported (e.g. useful for gating).

pipeline.trigger.<github source>.ref[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.ref "Link to this definition")

This is only used for `push` events. This field is treated as a regular expression and multiple refs may be listed. GitHub always sends full ref name, eg. `refs/tags/bar` and this string is matched against the regular expression.

pipeline.trigger.<github source>.require-status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require-status "Link to this definition")

Warning

This is deprecated and will be removed in a future version. Use [pipeline.trigger.<github source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require "attr-pipeline.trigger.<github source>.require") instead.

This may be used for any event. It requires that a certain kind of status be present for the PR (the status could be added by the event in question). It follows the same syntax as [pipeline.require.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.status "attr-pipeline.require.<github source>.status"). For each specified criteria there must exist a matching status.

This is ignored if the [pipeline.trigger.<github source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require "attr-pipeline.trigger.<github source>.require") attribute is present.

pipeline.trigger.<github source>.require[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require "Link to this definition")

This may be used for any event. It describes conditions that must be met by the PR in order for the trigger event to match. Those conditions may be satisfied by the event in question. It follows the same syntax as [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-requirements).

pipeline.trigger.<github source>.reject[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.reject "Link to this definition")

This may be used for any event and is the mirror of [pipeline.trigger.<github source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.require "attr-pipeline.trigger.<github source>.require"). It describes conditions that when met by the PR cause the trigger event not to match. Those conditions may be satisfied by the event in question. It follows the same syntax as [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-requirements).

pipeline.trigger.<github source>.debug[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.trigger.%3Cgithub%20source%3E.debug "Link to this definition")

Default:`false`

When set to true, this will cause debug messages to be included when the queue item is reported. These debug messages may be used to help diagnose why certain jobs did or did not run, and in many cases, why the item was not ultimately enqueued into the pipeline.

Setting this value also effectively sets [project.<pipeline>.debug](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.%3Cpipeline%3E.debug "attr-project.<pipeline>.debug") for affected queue items.

This only applies to items that arrive at a pipeline via this particular trigger. Since the output is very verbose and typically not needed or desired, this allows for a configuration where typical pipeline triggers omit the debug output, but triggers that match certain specific criteria may be used to request debug information.

Reporter Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reporter-configuration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

Zuul reports back to GitHub via GitHub API. Available reports include a PR comment containing the build results, a commit status on start, success and failure, an issue label addition/removal on the PR, and a merge of the PR itself. Status name, description, and context is taken from the pipeline.

pipeline.<reporter>.<github source>[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E "Link to this definition")

To report to GitHub, the dictionaries passed to any of the pipeline [reporter](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#reporters) attributes support the following attributes:

pipeline.<reporter>.<github source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status "Link to this definition")

Default:`None`

Type:_str_

Report status via the Github [status API](https://docs.github.com/v3/repos/statuses/). Set to one of

pending[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status.pending "Link to this definition")success[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status.success "Link to this definition")failure[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status.failure "Link to this definition")
This is usually mutually exclusive with a value set in [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check"), since this reports similar results via a different API. This API is older and results do not show up on the “checks” tab in the Github UI. It is recommended to use check unless you have a specific reason to use the status API.

pipeline.<reporter>.<github source>.check[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "Link to this definition")

Type:_string_

Report status via the Github [checks API](https://docs.github.com/v3/checks/). Set to one of

queued[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.queued "Link to this definition")cancelled[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.cancelled "Link to this definition")failure[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.failure "Link to this definition")in_progress[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.in_progress "Link to this definition")neutral[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.neutral "Link to this definition")skipped[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.skipped "Link to this definition")success[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check.success "Link to this definition")
This is usually mutually exclusive with a value set in [pipeline.<reporter>.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status "attr-pipeline.<reporter>.<github source>.status"), since this reports similar results via a different API.

Boolean value that determines if the reporter should add a comment to the pipeline status to the github pull request. Only used for Pull Request based items.

pipeline.<reporter>.<github source>.review[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.review "Link to this definition")

One of approve, comment, or request-changes that causes the reporter to submit a review with the specified status on Pull Request based items. Has no effect on other items.

pipeline.<reporter>.<github source>.review-body[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.review-body "Link to this definition")

Text that will be submitted as the body of the review. Required if review is set to comment or request-changes.

pipeline.<reporter>.<github source>.merge[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.merge "Link to this definition")

Default:`false`

Boolean value that determines if the reporter should merge the pull request. Only used for Pull Request based items.

pipeline.<reporter>.<github source>.label[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.label "Link to this definition")

List of strings each representing an exact label name which should be added to the pull request by reporter. Only used for Pull Request based items.

pipeline.<reporter>.<github source>.unlabel[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.unlabel "Link to this definition")

List of strings each representing an exact label name which should be removed from the pull request by reporter. Only used for Pull Request based items.

Requirements Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#requirements-configuration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

As described in [pipeline.require](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.require "attr-pipeline.require") and [pipeline.reject](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.reject "attr-pipeline.reject"), pipelines may specify that items meet certain conditions in order to be enqueued into the pipeline. These conditions vary according to the source of the project in question. To supply requirements for changes from a GitHub source named `github`, create a configuration such as the following:

pipeline:
  require:
    github:
      review:
        - type: approved

This indicates that changes originating from the GitHub connection named `github` must have an approved code review in order to be enqueued into the pipeline.

pipeline.require.<github source>[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E "Link to this definition")

The dictionary passed to the GitHub pipeline require attribute supports the following attributes:

pipeline.require.<github source>.review[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review "Link to this definition")

This requires that a certain kind of code review be present for the pull request (it could be added by the event in question). It takes several sub-parameters, all of which are optional and are combined together so that there must be a code review matching all specified requirements.

pipeline.require.<github source>.review.username[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.username "Link to this definition")

If present, a code review from this username matches. It is treated as a regular expression.

pipeline.require.<github source>.review.email[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.email "Link to this definition")

If present, a code review with this email address matches. It is treated as a regular expression.

pipeline.require.<github source>.review.older-than[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.older-than "Link to this definition")

If present, the code review must be older than this amount of time to match. Provide a time interval as a number with a suffix of “w” (weeks), “d” (days), “h” (hours), “m” (minutes), “s” (seconds). Example `48h` or `2d`.

pipeline.require.<github source>.review.newer-than[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.newer-than "Link to this definition")

If present, the code review must be newer than this amount of time to match. Same format as “older-than”.

pipeline.require.<github source>.review.type[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.type "Link to this definition")

If present, the code review must match this type (or types).

pipeline.require.<github source>.review.permission[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.review.permission "Link to this definition")

If present, the author of the code review must have this permission (or permissions) to match. The available values are `read`, `write`, and `admin`.

pipeline.require.<github source>.open[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.open "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be open or closed in order to be enqueued.

pipeline.require.<github source>.merged[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.merged "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be merged or not in order to be enqueued.

pipeline.require.<github source>.current-patchset[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.current-patchset "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the item must be associated with the latest commit in the pull request in order to be enqueued.

pipeline.require.<github source>.draft[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.draft "Link to this definition")

A boolean value (`true` or `false`) that indicates whether or not the change must be marked as a draft in GitHub in order to be enqueued.

pipeline.require.<github source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.status "Link to this definition")

A string value that corresponds with the status of the pull request. The syntax is `user:status:value`. This can also be a regular expression.

Zuul does not differentiate between a status reported via status API or via checks API (which is also how Github behaves in terms of branch protection and [status checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks#types-of-status-checks-on-github)). Thus, the status could be reported by a [pipeline.<reporter>.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status "attr-pipeline.<reporter>.<github source>.status") or a [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check").

When a status is reported via the status API, Github will add a `[bot]` to the name of the app that reported the status, resulting in something like `user[bot]:status:value`. For a status reported via the checks API, the app’s slug will be used as is.

pipeline.require.<github source>.label[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.require.%3Cgithub%20source%3E.label "Link to this definition")

A string value indicating that the pull request must have the indicated label (or labels).

pipeline.reject.<github source>[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E "Link to this definition")

The reject attribute is the mirror of the require attribute and is used to specify pull requests which should not be enqueued into a pipeline. It accepts a dictionary under the connection name and with the following attributes:

pipeline.reject.<github source>.review[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review "Link to this definition")

This requires that a certain kind of code review be absent for the pull request (it could be removed by the event in question). It takes several sub-parameters, all of which are optional and are combined together so that there must not be a code review matching all specified requirements.

pipeline.reject.<github source>.review.username[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.username "Link to this definition")

If present, a code review from this username matches. It is treated as a regular expression.

pipeline.reject.<github source>.review.email[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.email "Link to this definition")

If present, a code review with this email address matches. It is treated as a regular expression.

pipeline.reject.<github source>.review.older-than[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.older-than "Link to this definition")

If present, the code review must be older than this amount of time to match. Provide a time interval as a number with a suffix of “w” (weeks), “d” (days), “h” (hours), “m” (minutes), “s” (seconds). Example `48h` or `2d`.

pipeline.reject.<github source>.review.newer-than[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.newer-than "Link to this definition")

If present, the code review must be newer than this amount of time to match. Same format as “older-than”.

pipeline.reject.<github source>.review.type[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.type "Link to this definition")

If present, the code review must match this type (or types).

pipeline.reject.<github source>.review.permission[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.review.permission "Link to this definition")

If present, the author of the code review must have this permission (or permissions) to match. The available values are `read`, `write`, and `admin`.

pipeline.reject.<github source>.open[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.open "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be open or closed in order to be rejected.

pipeline.reject.<github source>.merged[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.merged "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be merged or not in order to be rejected.

pipeline.reject.<github source>.current-patchset[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.current-patchset "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the item must be associated with the latest commit in the pull request in order to be rejected.

pipeline.reject.<github source>.draft[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.draft "Link to this definition")

A boolean value (`true` or `false`) that indicates whether or not the change must be marked as a draft in GitHub in order to be rejected.

pipeline.reject.<github source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.status "Link to this definition")

A string value that corresponds with the status of the pull request. The syntax is `user:status:value`. This can also be a regular expression.

Zuul does not differentiate between a status reported via status API or via checks API (which is also how Github behaves in terms of branch protection and [status checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks#types-of-status-checks-on-github)). Thus, the status could be reported by a [pipeline.<reporter>.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status "attr-pipeline.<reporter>.<github source>.status") or a [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check").

When a status is reported via the status API, Github will add a `[bot]` to the name of the app that reported the status, resulting in something like `user[bot]:status:value`. For a status reported via the checks API, the app’s slug will be used as is.

pipeline.reject.<github source>.label[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.reject.%3Cgithub%20source%3E.label "Link to this definition")

A string value indicating that the pull request must not have the indicated label (or labels).

Reference pipelines configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reference-pipelines-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### Branch protection rules[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#branch-protection-rules "Link to this heading")

The rules prevent Pull requests to be merged on defined branches if they are not met. For instance a branch might require that specific status are marked as `success` before allowing the merge of the Pull request.

Zuul provides the attribute [tenant.untrusted-projects.<project>.exclude-unprotected-branches](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude-unprotected-branches "attr-tenant.untrusted-projects.<project>.exclude-unprotected-branches"). This attribute is by default set to `false` but we recommend to set it to `true` for the whole tenant. By doing so Zuul will benefit from:

> *   excluding in-repo development branches used to open Pull requests. This will prevent Zuul to fetch and read useless branches data to find Zuul configuration files.
> 
> *   reading protection rules configuration from the Github API for a given branch to define whether a Pull request must enter the gate pipeline. As of now Zuul only takes in account “Require status checks to pass before merging” and the checked status checkboxes.

Likewise, it is recommended to set the [tenant.untrusted-projects.<project>.exclude-locked-branches](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.untrusted-projects.%3Cproject%3E.exclude-locked-branches "attr-tenant.untrusted-projects.<project>.exclude-locked-branches") setting to avoid expending resources on read-only branches.

With the use of the reference pipelines below, the Zuul project recommends to set the minimum following settings:

> *   attribute tenant.untrusted-projects.exclude-unprotected-branches to `true` in the tenant (main.yaml) configuration file.
> 
> *   on each Github repository, activate the branch protections rules and configure the name of the protected branches. Furthermore set “Require status checks to pass before merging” and check the status labels checkboxes (at least ``<tenant>/check``) that must be marked as success in order for Zuul to make the Pull request enter the gate pipeline to be merged.

### Reference pipelines[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reference-pipelines "Link to this heading")

Here is an example of standard pipelines you may want to define:

- pipeline:
 name: check
 description: |
 Newly uploaded patchsets enter this pipeline to receive an
 initial check status.
 manager: independent
 trigger:
 github:
 # Run this pipeline on new/changed pull requests
 - event: pull_request
 action:
 - opened
 - changed
 - reopened
 # Run in response to a pull request comment "recheck"
 - event: pull_request
 action: comment
 comment: (?i)^\s*recheck\s*$
 # When using the checks API to report results, failed runs
 # will have a "re-run" button which emits this event.
 - event: check_run
 action: rerequested
 check: .*/check:.*
 start:
 github:
 check: in_progress
 comment: false
 # It is recommended to use the checks API for consistency with
 # other common CI tools that integrate with Github. Results
 # will appear on the "checks" tab of PR and changes. There is
 # generally no need to have Zuul leave comments when using the
 # checks API.
 #
 # The older status API appears inline with the PR and can be
 # enabled by uncommenting the "status:" in the various
 # sections below. You should choose one or the other
 # depending on project preferences.
 #
 #status: pending
 #comment: false
 success:
 github:
 check: success
 comment: false
 #status: success
 failure:
 github:
 check: failure
 comment: false
 #status: failure
 dequeue:
 github:
 check: cancelled
 comment: false

- pipeline:
 name: gate
 description: |
 Changes that have been approved by core developers are enqueued
 in order in this pipeline, and if they pass tests, will be
 merged.
 manager: dependent
 precedence: high
 supercedes: check
 require:
 github:
 review:
 # Require an approval from user with write access (e.g. core-reviewer)
 - permission: write
 type: approved
 # Require label
 label: gate
 open: True
 current-patchset: True
 trigger:
 github:
 - event: pull_request_review
 action: submitted
 state: approved
 - event: pull_request
 action: comment
 comment: (?i)^\s*regate\s*$
 - event: pull_request_review
 action: dismissed
 state: changes_requested
 - event: pull_request
 action: status
 status: ".*:success"
 - event: check_run
 action: rerequested
 check: .*/gate:.*
 - event: pull_request
 action: labeled
 label:
 - gate
 enqueue:
 github:
 check: queued
 comment: false
 start:
 github:
 check: in_progress
 comment: false
 #status: pending
 success:
 github:
 check: success
 comment: false
 #status: success
 merge: true
 failure:
 github:
 check: failure
 #status: failure
 comment: false
 no-jobs:
 github:
 check: skipped
 comment: false
 dequeue:
 github:
 check: cancelled
 comment: false
 window-floor: 20
 window-increase-factor: 2

- pipeline:
 name: post
 post-review: true
 description: This pipeline runs jobs that operate after each change is merged.
 manager: independent
 precedence: low
 trigger:
 github:
 - event: push
 ref: ^refs/heads/.*$

- pipeline:
 name: tag
 description: This pipeline runs jobs in response to any tag event.
 manager: independent
 precedence: high
 post-review: True
 trigger:
 github:
 - event: push
 ref: ^refs/tags/.*$

Github Checks API[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#github-checks-api "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------

Github provides two distinct methods for reporting results; a “checks” and a “status” API.

The [checks API](https://docs.github.com/v3/checks/) provides some additional features compared to the [status API](https://docs.github.com/v3/repos/statuses/) like file comments and custom actions (e.g. cancel a running build).

Either can be chosen when configuring Zuul to report for your Github project. However, there are some considerations to take into account when choosing the API.

### Design decisions[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#design-decisions "Link to this heading")

The Github checks API defines the concepts of [Check Suites](https://docs.github.com/v3/checks/suites/) and [Check Runs](https://docs.github.com/v3/checks/runs/). _Check suites_ are a collection of _check runs_ for a specific commit and summarize a final status

A priori the check suite appears to be a good mapping for a pipeline execution in Zuul, where a check run maps to a single job execution that is part of the pipeline run. Unfortunately, there are a few problematic restrictions mapping between Github and Zuul concepts.

Github check suites are opaque and the current status, duration and the overall conclusion are all calculated and set automatically whenever an included check run is updated. Most importantly, there can only be one check suite per commit SHA, per app. Thus there is no facility for Zuul to create multiple check suite results for a change, e.g. one check suite for each pipeline such as check and gate.

The Github check suite thus does not map well to Zuul’s concept of multiple pipelines for a single change. Since a check suite is unique and global for the change, it can not be used to flag the status of arbitrary pipelines. This makes the check suite API insufficient for recording details that Zuul needs such as “the check pipeline has passed but the gate pipeline has failed”.

Another issue is that Zuul only reports on the results of the whole pipeline, not individual jobs. Reporting each Zuul job as a separate check is problematic for a number of reasons.

Zuul often runs the same job for the same change multiple times; for example in the check and gate pipeline. There is no facility for these runs to be reported differently in the single check suite for the Github change.

When configuring branch protection in Github, only a _check run_ can be selected as required status check. This is in conflict with managing jobs in pipelines with Zuul. For example, to implement branch protection on GitHub would mean listing each job as a dedicated check, leading to a check run list that is not kept in sync with the project’s Zuul pipeline configuration. Additionally, you lose some of Zuul’s features like non-voting jobs as Github branch protections has no concept of a non-voting job.

Thus Zuul can integrate with the checks API, but only at a pipeline level. Each pipeline execution will map to a check-run result reported to Github.

### Behaviour in Zuul[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#behaviour-in-zuul "Link to this heading")

#### Reporting[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#reporting "Link to this heading")

The Github reporter is able to report both a status [pipeline.<reporter>.<github source>.status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.status "attr-pipeline.<reporter>.<github source>.status") or a check [pipeline.<reporter>.<github source>.check](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#attr-pipeline.%3Creporter%3E.%3Cgithub%20source%3E.check "attr-pipeline.<reporter>.<github source>.check"). While it’s possible to configure a Github reporter to report both, it’s recommended to use only one. Reporting both might result in duplicated status check entries in the Github PR (the section below the comments).

#### Trigger[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#trigger "Link to this heading")

The Github driver is able to trigger on a reported check ([check_run](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.event.check_run "value-pipeline.trigger.<github source>.event.check_run")) similar to a reported status ([status](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.status "value-pipeline.trigger.<github source>.action.status")).

#### Requirements[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#requirements "Link to this heading")

While trigger and reporter differentiates between status and check, the Github driver does not differentiate between them when it comes to pipeline requirements. This is mainly because Github also doesn’t differentiate between both in terms of branch protection and [status checks](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/about-status-checks#types-of-status-checks-on-github).

### Actions / Events[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#actions-events "Link to this heading")

Github provides a set of default actions for check suites and check runs. Those actions are available as buttons in the Github UI. Clicking on those buttons will emit webhook events which will be handled by Zuul.

These actions are only available on failed check runs / check suites. So far, a running or successful check suite / check run does not provide any action from Github side.

Available actions are:

Re-run all checks
Github emits a webhook event with type `check_suite` and action `rerequested` that is meant to re-run all check-runs contained in this check suite. Github does not provide the list of check-runs in that case, so it’s up to the Github app what should run.

Re-run failed checks
Github emits a webhook event with type `check_run` and action `rerequested` for each failed check run contained in this suite.

Re-run
Github emits a webhook event with type `check_run` and action `rerequested` for the specific check run.

Zuul will handle all events except for the Re-run all checks event; it does not make sense in the Zuul model to trigger all pipelines to run simultaneously.

These events are unable to be customized in Github. Github will always report “You have successfully requested …” despite nothing listening to the event. Therefore, it might be a solution to handle the Re-run all checks event in Zuul similar to Re-run failed checks just to not do anything while Github makes the user believe an action was really triggered.

### Restrictions and Recommendations[](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#restrictions-and-recommendations "Link to this heading")

Although both the checks API and the status API can be activated for a Github reporter at the same time, it’s not recommended to do so as this might result in multiple status checks to be reported to the PR for the same pipeline execution (which would result in duplicated entries in the status section below the comments of a PR).

In case the update on a check run fails (e.g. request timeout when reporting success or failure to Github), the check run will stay in status “in_progress” and there will be no way to re-run the check run via the Github UI as the predefined actions are only available on failed check runs. Thus, it’s recommended to configure a [comment](https://zuul-ci.org/docs/zuul/latest/drivers/github.html#value-pipeline.trigger.%3Cgithub%20source%3E.action.comment "value-pipeline.trigger.<github source>.action.comment") trigger on the pipeline to still be able to trigger re-run of the stuck check run via e.g. “recheck”.

The check suite will only list check runs that were reported by Zuul. If the requirements for a certain pipeline are not met and it is not run, the check run for this pipeline won’t be listed in the check suite. However, this does not affect the required status checks. If the check run is enabled as required, Github will still show it in the list of required status checks - even if it didn’t run yet - just not in the check suite.
