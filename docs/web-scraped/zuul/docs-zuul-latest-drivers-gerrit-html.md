# Source: https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html

Title: Gerrit — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html

Markdown Content:
[Gerrit](https://www.gerritcodereview.com/) is a code review system. The Gerrit driver supports sources, triggers, and reporters.

Zuul will need access to a Gerrit user.

Give that user whatever permissions will be needed on the projects you want Zuul to report on. For instance, you may want to grant `Verified +/-1` and `Submit` to the user. Additional categories or values may be added to Gerrit. Zuul is very flexible and can take advantage of those.

If `change.submitWholeTopic` is configured in Gerrit, Zuul will honor this by enqueuing changes with the same topic as circular dependencies. However, it is still necessary to enable circular dependency support in any pipeline queues where such changes may appear. See [queue.allow-circular-dependencies](https://zuul-ci.org/docs/zuul/latest/config/queue.html#attr-queue.allow-circular-dependencies "attr-queue.allow-circular-dependencies") for information on how to configure this.

Zuul interacts with Gerrit in up to three ways:

*   Receiving trigger events

*   Fetching source code

*   Reporting results

Trigger events arrive over an event stream, either SSH (via the `gerrit stream-events` command) or other protocols such as Kafka, AWS Kinesis, or Google Cloud Pub/Sub.

Fetching source code may happen over SSH or HTTP.

Reporting may happen over SSH or HTTP (strongly preferred).

The appropriate connection methods must be configured to satisfy the interactions Zuul will have with Gerrit. The recommended configuration is to configure both SSH and HTTP access.

The section below describes common configuration settings. Specific settings for different connection methods follow.

Note

If Gerrit is upgraded, or the value of `change.submitWholeTopic` is changed while Zuul is running, all running Zuul schedulers should be restarted in order to see the change.

Note

Since Gerrit 3.7 it has been possible to import projects and their changes from one Gerrit server to another. Doing so may result in change number collisions (change numbers that do not uniquely identify a single change). Zuul’s Gerrit driver is not currently expected to work with non unique change numbers.

Connection Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#connection-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------

The supported options in `zuul.conf` connections are:

<gerrit connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E "Link to this definition")

<gerrit connection>.driver(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.driver "Link to this definition")

gerrit[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#value-%3Cgerrit%20connection%3E.driver.gerrit "Link to this definition")
The connection must set `driver=gerrit` for Gerrit connections.

<gerrit connection>.server(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.server "Link to this definition")

Fully qualified domain name of Gerrit server.

<gerrit connection>.canonical_hostname[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.canonical_hostname "Link to this definition")

The canonical hostname associated with the git repos on the Gerrit server. Defaults to the value of [<gerrit connection>.server](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.server "attr-<gerrit connection>.server"). This is used to identify projects from this connection by name and in preparing repos on the filesystem for use by jobs. Note that Zuul will still only communicate with the Gerrit server identified by `server`; this option is useful if users customarily use a different hostname to clone or pull git repos so that when Zuul places them in the job’s working directory, they appear under this directory name.

<gerrit connection>.baseurl[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.baseurl "Link to this definition")

Default:`https://{server}`

Path to Gerrit web interface. Omit the trailing `/`.

<gerrit connection>.gitweb_url_template[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.gitweb_url_template "Link to this definition")

Default:`{baseurl}/gitweb?p={project.name}.git;a=commitdiff;h={sha}`

Url template for links to specific git shas. By default this will point at Gerrit’s built in gitweb but you can customize this value to point elsewhere (like cgit or github).

The three values available for string interpolation are baseurl which points back to Gerrit, project and all of its safe attributes, and sha which is the git sha1.

<gerrit connection>.max_dependencies[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.max_dependencies "Link to this definition")

This setting can be used to limit the number of dependencies that Zuul will consider when processing events from Gerrit. If used, it should be set to a value that is higher than the highest number of dependencies that are expected to be encountered. If, when processing an event from Gerrit, Zuul detects that the dependencies will exceed this value, Zuul will ignore the event with no feedback to the user. This is meant only to protect the Zuul server from resource exhaustion when excessive dependencies are present. The default (unset) is no limit. Note that the value `0` does not disable this option; instead it limits Zuul to zero dependencies. This is distinct from [tenant.max-dependencies](https://zuul-ci.org/docs/zuul/latest/tenants.html#attr-tenant.max-dependencies "attr-tenant.max-dependencies").

<gerrit connection>.user[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.user "Link to this definition")

Default:`zuul`

User name to use when accessing Gerrit.

<gerrit connection>.replication_delay[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20connection%3E.replication_delay "Link to this definition")

Default:`0`

Some Gerrit installations consist of multiple servers with various strategies for keeping these servers in sync (push replication, pull replication, multi-master, shared storage, etc.). Since there is currently no reliable method to determine when all servers are updated, this setting may be used to introduce a delay in event processing. Zuul will ensure that at least this amount of time (in seconds) has passed before processing the corresponding event.

### SSH Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#ssh-configuration "Link to this heading")

To prepare for SSH access, create an SSH keypair for Zuul to use if there isn’t one already, and create a Gerrit user with that key:

cat ~/id_rsa.pub | ssh -p29418 review.example.com gerrit create-account --ssh-key - --full-name Zuul zuul

Note

If you use an RSA key, ensure it is encoded in the PEM format (use the `-t rsa -m PEM` arguments to ssh-keygen).

If using Gerrit 2.7 or later, make sure the user is a member of a group that is granted the `Stream Events` permission, otherwise it will not be able to invoke the `gerrit stream-events` command over SSH.

<gerrit ssh connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E "Link to this definition")

<gerrit ssh connection>.ssh_server[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.ssh_server "Link to this definition")

If SSH access to the Gerrit server should be via a different hostname than web access, set this value to the hostname to use for SSH connections.

<gerrit ssh connection>.port[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.port "Link to this definition")

Default:`29418`

Gerrit SSH server port.

<gerrit ssh connection>.sshkey[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.sshkey "Link to this definition")

Default:`~zuul/.ssh/id_rsa`

Path to SSH key to use when logging into Gerrit.

<gerrit ssh connection>.keepalive[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.keepalive "Link to this definition")

Default:`60`

SSH connection keepalive timeout; `0` disables.

<gerrit ssh connection>.git_over_ssh[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.git_over_ssh "Link to this definition")

Default:`false`

This forces git operation over SSH even if the `password` attribute is set. This allow REST API access to the Gerrit server even when git-over-http operation is disabled on the server.

### HTTP Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#http-configuration "Link to this heading")

<gerrit ssh connection>

<gerrit ssh connection>.password[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.password "Link to this definition")

The HTTP authentication password for the user. This is optional, but if it is provided, Zuul will report to Gerrit via HTTP rather than SSH. It is required in order for file and line comments to reported (the Gerrit SSH API only supports review messages). Retrieve this password from the `HTTP Password` section of the `Settings` page in Gerrit.

<gerrit ssh connection>.auth_type[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.auth_type "Link to this definition")

Default:`basic`

The HTTP authentication mechanism.

basic[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#value-%3Cgerrit%20ssh%20connection%3E.auth_type.basic "Link to this definition")
HTTP Basic authentication; the default for most Gerrit installations.

digest[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#value-%3Cgerrit%20ssh%20connection%3E.auth_type.digest "Link to this definition")
HTTP Digest authentication; only used in versions of Gerrit prior to 2.15.

form[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#value-%3Cgerrit%20ssh%20connection%3E.auth_type.form "Link to this definition")
Zuul will submit a username and password to a form in order to authenticate.

gcloud_service[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#value-%3Cgerrit%20ssh%20connection%3E.auth_type.gcloud_service "Link to this definition")
Only valid when running in Google Cloud. This will use the default service account to authenticate to Gerrit. Note that this will only be used for interacting with the Gerrit API; anonymous HTTP access will be used to access the git repositories, therefore private repos or draft changes will not be available.

<gerrit ssh connection>.verify_ssl[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20ssh%20connection%3E.verify_ssl "Link to this definition")

Default:`true`

When using a self-signed certificate, this may be set to `false` to disable SSL certificate verification.

### Kafka Event Support[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#kafka-event-support "Link to this heading")

Zuul includes support for Gerrit’s events-kafka plugin. This may be used as an alternative to SSH for receiving trigger events.

Kafka does provide event delivery guarantees, so unlike SSH, if all Zuul schedulers are unable to communicate with Gerrit or Kafka, they will eventually receive queued events on reconnection.

All Zuul schedulers will attempt to connect to Kafka brokers. There are some implications for event delivery:

*   All events will be delivered to Zuul at least once. In the case of a disrupted connection, Zuul may receive duplicate events.

*   Events should generally arrive in order, however some events in rapid succession may be received by Zuul out of order.

<gerrit kafka connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E "Link to this definition")

<gerrit kafka connection>.kafka_bootstrap_servers(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_bootstrap_servers "Link to this definition")

A comma-separated list of Kafka servers (optionally including port separated with :).

<gerrit kafka connection>.kafka_topic[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_topic "Link to this definition")

Default:`gerrit`

The Kafka topic to which Zuul should subscribe.

<gerrit kafka connection>.kafka_client_id[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_client_id "Link to this definition")

Default:`zuul`

The Kafka client ID.

<gerrit kafka connection>.kafka_group_id[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_group_id "Link to this definition")

Default:`zuul`

The Kafka group ID.

<gerrit kafka connection>.kafka_tls_cert[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_tls_cert "Link to this definition")

Path to TLS certificate to use when connecting to a Kafka broker.

<gerrit kafka connection>.kafka_tls_key[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_tls_key "Link to this definition")

Path to TLS certificate key to use when connecting to a Kafka broker.

<gerrit kafka connection>.kafka_tls_ca[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20kafka%20connection%3E.kafka_tls_ca "Link to this definition")

Path to TLS CA certificate to use when connecting to a Kafka broker.

### AWS Kinesis Event Support[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#aws-kinesis-event-support "Link to this heading")

Zuul includes support for Gerrit’s events-aws-kinesis plugin. This may be used as an alternative to SSH for receiving trigger events.

Kinesis does provide event delivery guarantees, so unlike SSH, if all Zuul schedulers are unable to communicate with Gerrit or AWS, they will eventually receive queued events on reconnection.

All Zuul schedulers will attempt to connect to AWS Kinesis, but only one scheduler will process a given Kinesis shard at a time. There are some implications for event delivery:

*   All events will be delivered to Zuul at least once. In the case of a disrupted connection, Zuul may receive duplicate events.

*   If a connection is disrupted longer than the Kinesis retention period for a shard, Zuul may skip to the latest event ignoring all previous events.

*   Because shard processing happens in parallel, events may not arrive in order.

*   If a long period with no events elapses and a connection is disrupted, it may take Zuul some time to catch up to the latest events.

<gerrit aws kinesis connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20aws%20kinesis%20connection%3E "Link to this definition")

<gerrit aws kinesis connection>.aws_kinesis_region(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20aws%20kinesis%20connection%3E.aws_kinesis_region "Link to this definition")

The AWS region name in which the Kinesis stream is located.

<gerrit aws kinesis connection>.aws_kinesis_stream[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20aws%20kinesis%20connection%3E.aws_kinesis_stream "Link to this definition")

Default:`gerrit`

The AWS Kinesis stream name.

<gerrit aws kinesis connection>.aws_kinesis_access_key[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20aws%20kinesis%20connection%3E.aws_kinesis_access_key "Link to this definition")

The AWS access key to use.

<gerrit aws kinesis connection>.aws_kinesis_secret_key[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20aws%20kinesis%20connection%3E.aws_kinesis_secret_key "Link to this definition")

The AWS secret key to use.

### Google Cloud Pub/Sub Event Support[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#google-cloud-pub-sub-event-support "Link to this heading")

Zuul includes support for Gerrit’s events-gcloud-pubsub plugin. This may be used as an alternative to SSH for receiving trigger events.

Google Cloud Pub/Sub does provide event delivery guarantees, so unlike SSH, if all Zuul schedulers are unable to communicate with Gerrit or Google Cloud Pub/Sub, they will eventually receive queued events on reconnection.

All Zuul schedulers will attempt to connect to Google Cloud Pub/Sub. There are some implications for event delivery:

*   All events will be delivered to Zuul at least once. In the case of a disrupted connection, Zuul may receive duplicate events.

*   Because the events-gcloud-pubsub plugin does not at the time of this writing specify that messages are ordered, events may be received by Zuul out of order. Since this behavior is under the control of the Gerrit plugin, it may change in the future.

<gerrit gcloud pubsub connection>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20gcloud%20pubsub%20connection%3E "Link to this definition")

<gerrit gcloud pubsub connection>.gcloud_pubsub_project(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20gcloud%20pubsub%20connection%3E.gcloud_pubsub_project "Link to this definition")

The Google Cloud project name to use.

<gerrit gcloud pubsub connection>.gcloud_pubsub_topic[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20gcloud%20pubsub%20connection%3E.gcloud_pubsub_topic "Link to this definition")

Default:`gerrit`

The Google Cloud Pub/Sub topic to which Zuul should subscribe.

<gerrit gcloud pubsub connection>.gcloud_pubsub_subscription_id[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20gcloud%20pubsub%20connection%3E.gcloud_pubsub_subscription_id "Link to this definition")

Default:`zuul`

The ID of the Google Cloud Pub/Sub subscription to use. If the subscription does not exist, it will be created.

<gerrit gcloud pubsub connection>.gcloud_pubsub_private_key[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-%3Cgerrit%20gcloud%20pubsub%20connection%3E.gcloud_pubsub_private_key "Link to this definition")

Path to a file containing the JSON encoded key of a service account. If not provided, then Google Cloud local auth is used. If Zuul is not running in the same Google Cloud project as Gerrit, this is required.

Trigger Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#trigger-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------

pipeline.trigger.<gerrit source>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E "Link to this definition")

The dictionary passed to the Gerrit pipeline `trigger` attribute supports the following attributes:

pipeline.trigger.<gerrit source>.event(required)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.event "Link to this definition")

The event name from gerrit. Examples: `patchset-created`, `comment-added`, `ref-updated`. This field is treated as a regular expression.

pipeline.trigger.<gerrit source>.branch[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.branch "Link to this definition")

The branch associated with the event. Example: `master`. This field is treated as a regular expression, and multiple branches may be listed.

pipeline.trigger.<gerrit source>.ref[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.ref "Link to this definition")

On ref-updated events, the branch parameter is not used, instead the ref is provided. Currently Gerrit has the somewhat idiosyncratic behavior of specifying bare refs for branch names (e.g., `master`), but full ref names for other kinds of refs (e.g., `refs/tags/foo`). Zuul matches this value exactly against what Gerrit provides. This field is treated as a regular expression, and multiple refs may be listed.

pipeline.trigger.<gerrit source>.ignore-deletes[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.ignore-deletes "Link to this definition")

Default:`true`

When a branch is deleted, a ref-updated event is emitted with a newrev of all zeros specified. The `ignore-deletes` field is a boolean value that describes whether or not these newrevs trigger ref-updated events.

pipeline.trigger.<gerrit source>.approval[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.approval "Link to this definition")

This is only used for `comment-added` events. It only matches if the event has a matching approval associated with it. Example: `Code-Review: 2` matches a `+2` vote on the code review category. Multiple approvals may be listed.

pipeline.trigger.<gerrit source>.approval-change[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.approval-change "Link to this definition")

This is only used for `comment-added` events. It works the same way as `approval`, with the additional requirement that the approval value must have changed from its previous value. This means that it only matches when a user modifies an approval score instead of any comment where the score is present.

pipeline.trigger.<gerrit source>.email[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.email "Link to this definition")

This is used for any event. It takes a regex applied on the performer email, i.e. Gerrit account email address. If you want to specify several email filters, you must use a YAML list. Make sure to use non greedy matchers and to escapes dots! Example: `email: ^.*?@example\.org$`.

pipeline.trigger.<gerrit source>.username[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.username "Link to this definition")

This is used for any event. It takes a regex applied on the performer username, i.e. Gerrit account name. If you want to specify several username filters, you must use a YAML list. Make sure to use non greedy matchers and to escapes dots. Example: `username: ^zuul$`.

This is only used for `comment-added` events. It accepts a list of regexes that are searched for in the comment string. If any of these regexes matches a portion of the comment string the trigger is matched. `comment: retrigger` will match when comments containing `retrigger` somewhere in the comment text are added to a change.

pipeline.trigger.<gerrit source>.added[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.added "Link to this definition")

This is only used for `hashtags-changed` events. It accepts a regex or list of regexes that are searched for in the list of hashtags added to the change in this event. If any of these regexes match a portion of any of the added hashtags, the trigger is matched.

pipeline.trigger.<gerrit source>.removed[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.removed "Link to this definition")

This is only used for `hashtags-changed` events. It accepts a regex or list of regexes that are searched for in the list of hashtags removed from the change in this event. If any of these regexes match a portion of any of the removed hashtags, the trigger is matched.

pipeline.trigger.<gerrit source>.require-approval[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require-approval "Link to this definition")

Warning

This is deprecated and will be removed in a future version. Use [pipeline.trigger.<gerrit source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require "attr-pipeline.trigger.<gerrit source>.require") instead.

This may be used for any event. It requires that a certain kind of approval be present for the current patchset of the change (the approval could be added by the event in question). It follows the same syntax as [pipeline.require.<gerrit source>.approval](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval "attr-pipeline.require.<gerrit source>.approval"). For each specified criteria there must exist a matching approval.

This is ignored if the [pipeline.trigger.<gerrit source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require "attr-pipeline.trigger.<gerrit source>.require") attribute is present.

pipeline.trigger.<gerrit source>.reject-approval[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.reject-approval "Link to this definition")

Warning

This is deprecated and will be removed in a future version. Use [pipeline.trigger.<gerrit source>.reject](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.reject "attr-pipeline.trigger.<gerrit source>.reject") instead.

This takes a list of approvals in the same format as [pipeline.trigger.<gerrit source>.require-approval](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require-approval "attr-pipeline.trigger.<gerrit source>.require-approval") but the item will fail to enter the pipeline if there is a matching approval.

This is ignored if the [pipeline.trigger.<gerrit source>.reject](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.reject "attr-pipeline.trigger.<gerrit source>.reject") attribute is present.

pipeline.trigger.<gerrit source>.require[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require "Link to this definition")

This may be used for any event. It describes conditions that must be met by the change in order for the trigger event to match. Those conditions may be satisfied by the event in question. It follows the same syntax as [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#gerrit-requirements).

pipeline.trigger.<gerrit source>.reject[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.reject "Link to this definition")

This may be used for any event and is the mirror of [pipeline.trigger.<gerrit source>.require](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.require "attr-pipeline.trigger.<gerrit source>.require"). It describes conditions that when met by the change cause the trigger event not to match. Those conditions may be satisfied by the event in question. It follows the same syntax as [Requirements Configuration](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#gerrit-requirements).

pipeline.trigger.<gerrit source>.debug[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.trigger.%3Cgerrit%20source%3E.debug "Link to this definition")

Default:`false`

When set to true, this will cause debug messages to be included when the queue item is reported. These debug messages may be used to help diagnose why certain jobs did or did not run, and in many cases, why the item was not ultimately enqueued into the pipeline.

Setting this value also effectively sets [project.<pipeline>.debug](https://zuul-ci.org/docs/zuul/latest/config/project.html#attr-project.%3Cpipeline%3E.debug "attr-project.<pipeline>.debug") for affected queue items.

This only applies to items that arrive at a pipeline via this particular trigger. Since the output is very verbose and typically not needed or desired, this allows for a configuration where typical pipeline triggers omit the debug output, but triggers that match certain specific criteria may be used to request debug information.

Reporter Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#reporter-configuration "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------

pipeline.reporter.<gerrit reporter>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reporter.%3Cgerrit%20reporter%3E "Link to this definition")

The dictionary passed to the Gerrit reporter is used to provide label values to Gerrit. To set the Verified label to 1, add 
```
verified:
1
```
 to the dictionary.

The following additional keys are recognized:

pipeline.reporter.<gerrit reporter>.submit[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reporter.%3Cgerrit%20reporter%3E.submit "Link to this definition")

Default:`False`

Set this to `True` to submit (merge) the change.

If this is true (the default), Zuul will leave review messages on the change (including job results). Set this to false to disable this behavior (file and line commands will still be sent if present).

pipeline.reporter.<gerrit reporter>.notify[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reporter.%3Cgerrit%20reporter%3E.notify "Link to this definition")

If this is set to a notify handling value then send notifications at the specified level. If not, use the default specified by the gerrit api. Some possible values include `ALL` and `NONE`. See the gerrit api for available options and default value:

[https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#review-input](https://gerrit-review.googlesource.com/Documentation/rest-api-changes.html#review-input)

A [connection](https://zuul-ci.org/docs/zuul/latest/configuration.html#connections) that uses the gerrit driver must be supplied to the trigger.

Requirements Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#requirements-configuration "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------

As described in [pipeline.require](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.require "attr-pipeline.require") and [pipeline.reject](https://zuul-ci.org/docs/zuul/latest/config/pipeline.html#attr-pipeline.reject "attr-pipeline.reject"), pipelines may specify that items meet certain conditions in order to be enqueued into the pipeline. These conditions vary according to the source of the project in question. To supply requirements for changes from a Gerrit source named `gerrit`, create a configuration such as the following:

pipeline:
 require:
 gerrit:
 approval:
 - Code-Review: 2

This indicates that changes originating from the Gerrit connection named `gerrit` must have a `Code-Review` vote of `+2` in order to be enqueued into the pipeline.

pipeline.require.<gerrit source>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E "Link to this definition")

The dictionary passed to the Gerrit pipeline require attribute supports the following attributes:

pipeline.require.<gerrit source>.approval[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval "Link to this definition")

This requires that a certain kind of approval be present for the current patchset of the change (the approval could be added by the event in question). Approval is a dictionary or a list of dictionaries with attributes listed below, all of which are optional and are combined together so that there must be an approval matching all specified requirements.

pipeline.require.<gerrit source>.approval.username[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval.username "Link to this definition")

If present, an approval from this username is required. It is treated as a regular expression.

pipeline.require.<gerrit source>.approval.email[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval.email "Link to this definition")

If present, an approval with this email address is required. It is treated as a regular expression.

pipeline.require.<gerrit source>.approval.older-than[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval.older-than "Link to this definition")

If present, the approval must be older than this amount of time to match. Provide a time interval as a number with a suffix of “w” (weeks), “d” (days), “h” (hours), “m” (minutes), “s” (seconds). Example `48h` or `2d`.

pipeline.require.<gerrit source>.approval.newer-than[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.approval.newer-than "Link to this definition")

If present, the approval must be newer than this amount of time to match. Same format as “older-than”.

Any other field is interpreted as a review category and value pair. For example `Verified: 1` would require that the approval be for a +1 vote in the “Verified” column. The value may either be a single value or a list: `Verified: [1, 2]` would match either a +1 or +2 vote.

pipeline.require.<gerrit source>.open[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.open "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be open or closed in order to be enqueued.

pipeline.require.<gerrit source>.current-patchset[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.current-patchset "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be the current patchset in order to be enqueued.

pipeline.require.<gerrit source>.wip[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.wip "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be wip or not wip in order to be enqueued.

pipeline.require.<gerrit source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.status "Link to this definition")

A string value that corresponds with the status of the change reported by Gerrit.

pipeline.require.<gerrit source>.hashtags[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.require.%3Cgerrit%20source%3E.hashtags "Link to this definition")

A regex or list of regexes. Each of these must match at least one of the hashtags present on the change in order for the change to be enqueued.

pipeline.reject.<gerrit source>[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E "Link to this definition")

The reject attribute is the mirror of the require attribute. It also accepts a dictionary under the connection name. This dictionary supports the following attributes:

pipeline.reject.<gerrit source>.approval[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.approval "Link to this definition")

This requires that a certain kind of approval not be present for the current patchset of the change (the approval could be added by the event in question). Approval is a dictionary or a list of dictionaries with attributes listed below, all of which are optional and are combined together so that there must be no approvals matching all specified requirements.

Example to reject a change with any negative vote:

reject:
 gerrit:
 approval:
 - Code-Review: [-1, -2]

pipeline.reject.<gerrit source>.approval.username[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.approval.username "Link to this definition")

If present, an approval from this username is required. It is treated as a regular expression.

pipeline.reject.<gerrit source>.approval.email[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.approval.email "Link to this definition")

If present, an approval with this email address is required. It is treated as a regular expression.

pipeline.reject.<gerrit source>.approval.older-than[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.approval.older-than "Link to this definition")

If present, the approval must be older than this amount of time to match. Provide a time interval as a number with a suffix of “w” (weeks), “d” (days), “h” (hours), “m” (minutes), “s” (seconds). Example `48h` or `2d`.

pipeline.reject.<gerrit source>.approval.newer-than[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.approval.newer-than "Link to this definition")

If present, the approval must be newer than this amount of time to match. Same format as “older-than”.

Any other field is interpreted as a review category and value pair. For example `Verified: 1` would require that the approval be for a +1 vote in the “Verified” column. The value may either be a single value or a list: `Verified: [1, 2]` would match either a +1 or +2 vote.

pipeline.reject.<gerrit source>.open[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.open "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be open or closed in order to be rejected.

pipeline.reject.<gerrit source>.current-patchset[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.current-patchset "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be the current patchset in order to be rejected.

pipeline.reject.<gerrit source>.wip[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.wip "Link to this definition")

A boolean value (`true` or `false`) that indicates whether the change must be wip or not wip in order to be rejected.

pipeline.reject.<gerrit source>.status[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.status "Link to this definition")

A string value that corresponds with the status of the change reported by Gerrit.

pipeline.reject.<gerrit source>.hashtags[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#attr-pipeline.reject.%3Cgerrit%20source%3E.hashtags "Link to this definition")

A regex or list of regexes. If any of these match at least one of the hashtags present on the change, it will be rejected.

Reference Pipelines Configuration[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#reference-pipelines-configuration "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

Here is an example of standard pipelines you may want to define:

- pipeline:
 name: check
 description: |
 Newly uploaded patchsets enter this pipeline to receive an
 initial +/-1 Verified vote.
 manager: independent
 precedence: low
 require:
 gerrit:
 open: True
 current-patchset: True
 trigger:
 gerrit:
 - event: patchset-created
 - event: change-restored
 - event: comment-added
 comment: (?i)^(Patch Set [0-9]+:)?( [\w\\+-]*)*(\n\n)?\s*recheck
 success:
 gerrit:
 # Note that gerrit keywords are case-sensitive.
 Verified: 1
 failure:
 gerrit:
 Verified: -1

- pipeline:
 name: gate
 description: |
 Changes that have been approved by core reviewers are enqueued
 in order in this pipeline, and if they pass tests, will be
 merged. For documentation on how gating with Zuul works, please see
 https://zuul-ci.org/docs/zuul/latest/gating.html
 manager: dependent
 precedence: normal
 supercedes: check
 post-review: True
 require:
 gerrit:
 open: True
 current-patchset: True
 approval:
 - Workflow: 1
 trigger:
 gerrit:
 - event: comment-added
 approval:
 - Workflow: 1
 start:
 gerrit:
 Verified: 0
 success:
 gerrit:
 Verified: 2
 submit: true
 failure:
 gerrit:
 Verified: -2
 window-floor: 20
 window-increase-factor: 2

- pipeline:
 name: post
 description: |
 This pipeline runs jobs that operate after each change is
 merged. Queue items are identified by the abbreviated hash (git
 log --format=%h) of the merge commit.
 manager: supercedent
 precedence: high
 post-review: True
 trigger:
 gerrit:
 - event: ref-updated
 ref: ^refs/heads/.*$

- pipeline:
 name: promote
 description: |
 This pipeline runs jobs that operate after each change is merged
 in order to promote artifacts generated in the gate
 pipeline.
 manager: supercedent
 precedence: high
 post-review: True
 trigger:
 gerrit:
 - event: change-merged
 success:
 gerrit: {}
 failure:
 gerrit: {}

- pipeline:
 name: deploy
 description: |
 This pipeline runs jobs that operate after each change is merged
 in order to deploy to production.
 manager: serial
 precedence: high
 post-review: True
 trigger:
 gerrit:
 - event: change-merged
 success:
 gerrit: {}
 failure:
 gerrit: {}

- pipeline:
 name: release
 description: |
 When a commit is tagged as a release, this pipeline runs jobs
 that publish archives and documentation.
 manager: independent
 precedence: high
 post-review: True
 trigger:
 gerrit:
 - event: ref-updated
 ref: ^refs/tags/[0-9]+(\.[0-9]+)*$

- pipeline:
 name: tag
 post-review: true
 description: This pipeline runs jobs in response to any tag event.
 manager: independent
 precedence: high
 trigger:
 gerrit:
 - event: ref-updated
 ref: ^refs/tags/.*$

Checks Plugin Support (Deprecated)[](https://zuul-ci.org/docs/zuul/latest/drivers/gerrit.html#checks-plugin-support-deprecated "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

The Gerrit driver has support for Gerrit’s checks plugin. Due to the deprecation of the checks plugin in Gerrit, support in Zuul is also deprecated and likely to be removed in a future version. It is not recommended for use.

Caveats include (but are not limited to):

*   This documentation is brief.

*   Access control for the checks API in Gerrit depends on a single global administrative permission, `administrateCheckers`. This is required in order to use the checks API and can not be restricted by project. This means that any system using the checks API can interfere with any other.

*   Checkers are restricted to a single project. This means that a system with many projects will require many checkers to be defined in Gerrit – one for each project+pipeline.

*   No support is provided for attaching checks to tags or commits, meaning that tag, release, and post pipelines are unable to be used with the checks API and must rely on stream-events.

*   Sub-checks are not implemented yet, so in order to see the results of individual jobs on a change, users must either follow the buildset link, or the pipeline must be configured to leave a traditional comment.

*   Familiarity with the checks API is recommended.

*   Checkers may not be permanently deleted from Gerrit (only “soft-deleted” so they no longer apply), so any experiments you perform on a production system will leave data there forever.

In order to use the checks API, you must have HTTP access configured in zuul.conf.

There are two ways to configure a pipeline for the checks API: directly referencing the checker UUID, or referencing it’s scheme. It is hoped that once multi-repository checks are supported, that an administrator will be able to configure a single checker in Gerrit for each Zuul pipeline, and those checkers can apply to all repositories. If and when that happens, we will be able to reference the checker UUID directly in Zuul’s pipeline configuration. If you only have a single project, you may find this approach acceptable now.

To use this approach, create a checker named `zuul:check` and configure a pipeline like this:

- pipeline:
 name: check
 manager: independent
 trigger:
 gerrit:
 - event: pending-check
 uuid: 'zuul:check'
 enqueue:
 gerrit:
 checks-api:
 uuid: 'zuul:check'
 state: SCHEDULED
 message: 'Change has been enqueued in check'
 start:
 gerrit:
 checks-api:
 uuid: 'zuul:check'
 state: RUNNING
 message: 'Jobs have started running'
 no-jobs:
 gerrit:
 checks-api:
 uuid: 'zuul:check'
 state: NOT_RELEVANT
 message: 'Change has no jobs configured'
 success:
 gerrit:
 checks-api:
 uuid: 'zuul:check'
 state: SUCCESSFUL
 message: 'Change passed all voting jobs'
 failure:
 gerrit:
 checks-api:
 uuid: 'zuul:check'
 state: FAILED
 message: 'Change failed'

For a system with multiple repositories and one or more checkers for each repository, the scheme approach is recommended. To use this, create a checker for each pipeline in each repository. Give them names such as `zuul_check:project1`, `zuul_gate:project1`, `zuul_check:project2`, etc. The part before the `:` is the scheme. Then create a pipeline like this:

- pipeline:
 name: check
 manager: independent
 trigger:
 gerrit:
 - event: pending-check
 scheme: 'zuul_check'
 enqueue:
 gerrit:
 checks-api:
 scheme: 'zuul_check'
 state: SCHEDULED
 message: 'Change has been enqueued in check'
 start:
 gerrit:
 checks-api:
 scheme: 'zuul_check'
 state: RUNNING
 message: 'Jobs have started running'
 no-jobs:
 gerrit:
 checks-api:
 scheme: 'zuul_check'
 state: NOT_RELEVANT
 message: 'Change has no jobs configured'
 success:
 gerrit:
 checks-api:
 scheme: 'zuul_check'
 state: SUCCESSFUL
 message: 'Change passed all voting jobs'
 failure:
 gerrit:
 checks-api:
 scheme: 'zuul_check'
 state: FAILED
 message: 'Change failed'

This will match and report to the appropriate checker for a given repository based on the scheme you provided.
