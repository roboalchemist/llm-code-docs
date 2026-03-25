# Source: https://zuul-ci.org/docs/zuul/latest/monitoring.html

Title: Monitoring — Zuul documentation

URL Source: https://zuul-ci.org/docs/zuul/latest/monitoring.html

Markdown Content:
Statsd reporting[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#statsd-reporting "Link to this heading")
-----------------------------------------------------------------------------------------------------------------

Zuul comes with support for the statsd protocol, when enabled and configured (see below), the Zuul scheduler will emit raw metrics to a statsd receiver which let you in turn generate nice graphics.

### Configuration[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#configuration "Link to this heading")

Statsd support uses the `statsd` python module. Note that support is optional and Zuul will start without the statsd python module present.

Configuration is in the [statsd](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-statsd "attr-statsd") section of `zuul.conf`.

### Metrics[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#metrics "Link to this heading")

These metrics are emitted by the Zuul [Scheduler](https://zuul-ci.org/docs/zuul/latest/configuration.html#scheduler):

zuul.event.<driver>.<type>(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.event.%3Cdriver%3E.%3Ctype%3E "Link to this definition")
Zuul will report counters for each type of event it receives from each of its configured drivers.

zuul.connection.<connection>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.connection.%3Cconnection%3E "Link to this definition")
Holds metrics specific to connections. This hierarchy includes:

zuul.connection.<connection>.cache.data_size_compressed(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.connection.%3Cconnection%3E.cache.data_size_compressed "Link to this definition")
The number of bytes stored in ZooKeeper for all items in this connection’s change cache.

zuul.connection.<connection>.cache.data_size_uncompressed(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.connection.%3Cconnection%3E.cache.data_size_uncompressed "Link to this definition")
The number of bytes required to for the change cache (the decompressed value of `data_size_compressed`).

zuul.tenant.<tenant>.event_enqueue_processing_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.event_enqueue_processing_time "Link to this definition")
A timer metric reporting the time from when the scheduler receives a trigger event from a driver until the corresponding item is enqueued in a pipeline. This measures the performance of the scheduler in dispatching events.

zuul.tenant.<tenant>.event_enqueue_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.event_enqueue_time "Link to this definition")
A timer metric reporting the time from when a trigger event was received from the remote system to when the corresponding item is enqueued in a pipeline. This includes [zuul.tenant.<tenant>.event_enqueue_processing_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.event_enqueue_processing_time "stat-zuul.tenant.<tenant>.event_enqueue_processing_time") and any driver-specific pre-processing of the event.

zuul.tenant.<tenant>.management_events(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.management_events "Link to this definition")
The size of the tenant’s management event queue.

zuul.tenant.<tenant>.reconfiguration_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.reconfiguration_time "Link to this definition")
A timer metric reporting the time taken to reconfigure a tenant. This is performed by one scheduler after a tenant reconfiguration event is received. During this time, all processing of that tenant’s pipelines are halted. This measures that time.

Once the first scheduler completes a tenant reconfiguration, other schedulers may update their layout in the background without interrupting processing. That is not reported in this metric.

zuul.tenant.<tenant>.trigger_events(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.trigger_events "Link to this definition")
The size of the tenant’s trigger event queue.

zuul.tenant.<tenant>.pipeline[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline "Link to this definition")
Holds metrics specific to jobs. This hierarchy includes:

zuul.tenant.<tenant>.pipeline.<pipeline>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E "Link to this definition")
A set of metrics for each pipeline named as defined in the Zuul config.

zuul.tenant.<tenant>.pipeline.<pipeline>.event_enqueue_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_enqueue_time "Link to this definition")
The time elapsed from when a trigger event was received from the remote system to when the corresponding item is enqueued in a pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.merge_request_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merge_request_time "Link to this definition")
The amount of time spent waiting for the initial merge operation(s). This will always include a request to a Zuul merger to speculatively merge the change, but it may also include a second request submitted in parallel to identify the files altered by the change. Includes [zuul.tenant.<tenant>.pipeline.<pipeline>.merger_merge_op_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_merge_op_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.merger_merge_op_time") and [zuul.tenant.<tenant>.pipeline.<pipeline>.merger_files_changes_op_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_files_changes_op_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.merger_files_changes_op_time").

zuul.tenant.<tenant>.pipeline.<pipeline>.merger_merge_op_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_merge_op_time "Link to this definition")
The amount of time the merger spent performing a merge operation. This does not include any of the round-trip time from the scheduler to the merger, or any other merge operations.

zuul.tenant.<tenant>.pipeline.<pipeline>.merger_files_changes_op_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_files_changes_op_time "Link to this definition")
The amount of time the merger spent performing a files-changes operation to detect changed files (this is sometimes performed if the source does not provide this information). This does not include any of the round-trip time from the scheduler to the merger, or any other merge operations.

zuul.tenant.<tenant>.pipeline.<pipeline>.layout_generation_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.layout_generation_time "Link to this definition")
The amount of time spent generating a dynamic configuration layout.

zuul.tenant.<tenant>.pipeline.<pipeline>.job_freeze_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.job_freeze_time "Link to this definition")
The amount of time spent freezing the inheritance hierarchy and parameters of a job.

zuul.tenant.<tenant>.pipeline.<pipeline>.repo_state_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.repo_state_time "Link to this definition")
The amount of time waiting for a secondary Zuul merger operation to collect additional information about the repo state of required projects. Includes [zuul.tenant.<tenant>.pipeline.<pipeline>.merger_repo_state_op_time](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_repo_state_op_time "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.merger_repo_state_op_time").

zuul.tenant.<tenant>.pipeline.<pipeline>.merger_repo_state_op_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.merger_repo_state_op_time "Link to this definition")
The amount of time the merger spent performing a repo state operation to collect additional information about the repo state of required projects. This does not include any of the round-trip time from the scheduler to the merger, or any other merge operations.

zuul.tenant.<tenant>.pipeline.<pipeline>.node_request_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.node_request_time "Link to this definition")
The amount of time spent waiting for each node request to be fulfilled.

zuul.tenant.<tenant>.pipeline.<pipeline>.job_wait_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.job_wait_time "Link to this definition")
How long a job waited for an executor to start running it after the build was requested.

zuul.tenant.<tenant>.pipeline.<pipeline>.event_job_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_job_time "Link to this definition")
The total amount of time elapsed from when a trigger event was received from the remote system until the item’s first job is run. This is only emitted once per queue item, even if its buildset is reset due to a speculative execution failure.

zuul.tenant.<tenant>.pipeline.<pipeline>.all_jobs(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.all_jobs "Link to this definition")
Number of jobs triggered by the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.current_changes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.current_changes "Link to this definition")
The number of items currently being processed by this pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.window(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.window "Link to this definition")
The configured window size for the pipeline. Note that this will not change during operation. This value is used to initialize each [project queue](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-project-queue), and as changes in that queue succeed or fail, that queue’s window will adjust.

zuul.tenant.<tenant>.pipeline.<pipeline>.handling(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.handling "Link to this definition")
The total time taken to refresh and process the pipeline. This is emitted every time a scheduler examines a pipeline regardless of whether it takes any actions.

zuul.tenant.<tenant>.pipeline.<pipeline>.event_process(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.event_process "Link to this definition")
The time taken to process the event queues for the pipeline. This is emitted only if there are events to process.

zuul.tenant.<tenant>.pipeline.<pipeline>.process(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.process "Link to this definition")
The time taken to process the pipeline. This is emitted only if there were events to process.

zuul.tenant.<tenant>.pipeline.<pipeline>.data_size_compressed(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.data_size_compressed "Link to this definition")
The number of bytes stored in ZooKeeper to represent the serialized state of the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.data_size_uncompressed(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.data_size_uncompressed "Link to this definition")
The number of bytes required to represent the serialized state of the pipeline (the decompressed value of `data_size_compressed`).

zuul.tenant.<tenant>.pipeline.<pipeline>.queue[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue "Link to this definition")
This hierarchy holds more specific metrics for each [project queue](https://zuul-ci.org/docs/zuul/latest/glossary.html#term-project-queue) in the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E "Link to this definition")
The name of the queue. If the queue is automatically generated for a single project, the name of the project is used by default. Embedded `.` characters will be translated to `_`, and `/` to `.`.

If the queue is configured as per-branch, the metrics below are omitted and instead found under [zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.branch](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.branch "stat-zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.branch").

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.current_changes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.current_changes "Link to this definition")
The number of items currently in this queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.window(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.window "Link to this definition")
The window size for the queue. This will change as individual changes in the queue succeed or fail.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.resident_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.resident_time "Link to this definition")
A timer metric reporting how long each item has been in the queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.total_changes(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.total_changes "Link to this definition")
The number of changes processed by the queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.branch[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.branch "Link to this definition")
If the queue is configured as per-branch, this hierarchy will be present and will hold stats for each branch seen.

zuul.tenant.<tenant>.pipeline.<pipeline>.queue.<queue>.branch.<branch>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.queue.%3Cqueue%3E.branch.%3Cbranch%3E "Link to this definition")
The name of the branch. Embedded `.` characters will be translated to `_`, and `/` to `.`.

Underneath this key are per-branch values of the metrics above.

zuul.tenant.<tenant>.pipeline.<pipeline>.project[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project "Link to this definition")
This hierarchy holds more specific metrics for each project participating in the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E "Link to this definition")
The canonical hostname for the triggering project. Embedded `.` characters will be translated to `_`.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E "Link to this definition")
The name of the triggering project. Embedded `/` or `.` characters will be translated to `_`.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E "Link to this definition")
The name of the triggering branch. Embedded `/` or `.` characters will be translated to `_`.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.job[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.job "Link to this definition")
Subtree detailing per-project job statistics:

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.job.<jobname>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.job.%3Cjobname%3E "Link to this definition")
The triggered job name.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.job.<jobname>.<result>(counter,timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.job.%3Cjobname%3E.%3Cresult%3E "Link to this definition")
A counter for each type of result (e.g., `SUCCESS` or `FAILURE`, `ERROR`, etc.) for the job. If the result is `SUCCESS` or `FAILURE`, Zuul will additionally report the duration of the build as a timer.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.job.<jobname>.wait_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.job.%3Cjobname%3E.wait_time "Link to this definition")
How long the job waited for an executor to start running it after the build was requested.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.current_changes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.current_changes "Link to this definition")
The number of items of this project currently being processed by this pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.resident_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.resident_time "Link to this definition")
A timer metric reporting how long each item for this project has been in the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.project.<canonical_hostname>.<project>.<branch>.total_changes(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.project.%3Ccanonical_hostname%3E.%3Cproject%3E.%3Cbranch%3E.total_changes "Link to this definition")
The number of changes for this project processed by the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.read_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_time "Link to this definition")
The time spent reading data from ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.read_znodes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_znodes "Link to this definition")
The number of ZNodes read from ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.read_objects(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_objects "Link to this definition")
The number of Zuul data model objects read from ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.read_bytes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.read_bytes "Link to this definition")
The amount of data read from ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.refresh(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.refresh "Link to this definition")
The time taken to refresh the state from ZooKeeper.

zuul.tenant.<tenant>.pipeline.<pipeline>.resident_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.resident_time "Link to this definition")
A timer metric reporting how long each item has been in the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.total_changes(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.total_changes "Link to this definition")
The number of changes processed by the pipeline.

zuul.tenant.<tenant>.pipeline.<pipeline>.trigger_events(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.trigger_events "Link to this definition")
The size of the pipeline’s trigger event queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.result_events(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.result_events "Link to this definition")
The size of the pipeline’s result event queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.management_events(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.management_events "Link to this definition")
The size of the pipeline’s management event queue.

zuul.tenant.<tenant>.pipeline.<pipeline>.write_time(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_time "Link to this definition")
The time spent writing data to ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.write_znodes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_znodes "Link to this definition")
The number of ZNodes written to ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.write_objects(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_objects "Link to this definition")
The number of Zuul data model objects written to ZooKeeper during a single pipeline processing run.

zuul.tenant.<tenant>.pipeline.<pipeline>.write_bytes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.tenant.%3Ctenant%3E.pipeline.%3Cpipeline%3E.write_bytes "Link to this definition")
The amount of data written to ZooKeeper during a single pipeline processing run.

zuul.executor.<executor>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E "Link to this definition")
> Holds metrics emitted by individual executors. The `<executor>` component of the key will be replaced with the hostname of the executor.
> 
> zuul.executor.<executor>.merger.<result>(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.merger.%3Cresult%3E "Link to this definition")
> Incremented to represent the status of a Zuul executor’s merger operations. `<result>` can be either `SUCCESS` or `FAILURE`. A failed merge operation which would be accounted for as a `FAILURE` is what ends up being returned by Zuul as a `MERGE_CONFLICT`.
> 
> zuul.executor.<executor>.builds(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.builds "Link to this definition")
> Incremented each time the executor starts a build.
> 
> zuul.executor.<executor>.starting_builds(gauge,timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.starting_builds "Link to this definition")
> The number of builds starting on this executor and a timer containing how long jobs were in this state. These are builds which have not yet begun their first pre-playbook.
> 
> 
> The timer needs special thoughts when interpreting it because it aggregates all jobs. It can be useful when aggregating it over a longer period of time (maybe a day) where fast rising graphs could indicate e.g. IO problems of the machines the executors are running on. But it has to be noted that a rising graph also can indicate a higher usage of complex jobs using more required projects. Also comparing several executors might give insight if the graphs differ a lot from each other. Typically the jobs are equally distributed over all executors (in the same zone when using the zone feature) and as such the starting jobs timers (aggregated over a large enough interval) should not differ much.
> 
> zuul.executor.<executor>.running_builds(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.running_builds "Link to this definition")
> The number of builds currently running on this executor. This includes starting builds.
> 
> zuul.executor.<executor>.paused_builds(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.paused_builds "Link to this definition")
> The number of currently paused builds on this executor.
> 
> zuul.executor.<executor>.phase[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.phase "Link to this definition")
> Subtree detailing per-phase execution statistics:
> 
> zuul.executor.<executor>.phase.<phase>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.phase.%3Cphase%3E "Link to this definition")
> `<phase>` represents a phase in the execution of a job. This can be an _internal_ phase (such as `setup` or `cleanup`) as well as _job_ phases such as `pre`, `run` or `post`.
> 
> zuul.executor.<executor>.phase.<phase>.<result>(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.phase.%3Cphase%3E.%3Cresult%3E "Link to this definition")
> A counter for each type of result. These results do not, by themselves, determine the status of a build but are indicators of the exit status provided by Ansible for the execution of a particular phase.
> 
> 
> Example of possible counters for each phase are: `RESULT_NORMAL`, `RESULT_TIMED_OUT`, `RESULT_UNREACHABLE`, `RESULT_ABORTED`.
> 
> zuul.executor.<executor>.load_average(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.load_average "Link to this definition")
> The one-minute load average of this executor, multiplied by 100.
> 
> zuul.executor.<executor>.pause(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pause "Link to this definition")
> Indicates if the executor is paused. 1 means paused else 0.
> 
> zuul.executor.<executor>.pct_used_hdd(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pct_used_hdd "Link to this definition")
> The used disk on this executor, as a percentage multiplied by 100.
> 
> zuul.executor.<executor>.pct_used_inodes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pct_used_inodes "Link to this definition")
> The used inodes on this executor, as a percentage multiplied by 100.
> 
> zuul.executor.<executor>.pct_used_ram(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pct_used_ram "Link to this definition")
> The used RAM (excluding buffers and cache) on this executor, as a percentage multiplied by 100.

zuul.executor.<executor>.pct_used_ram_cgroup(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.pct_used_ram_cgroup "Link to this definition")
The used RAM (excluding buffers and cache) on this executor allowed by the cgroup, as percentage multiplied by 100.

zuul.executor.<executor>.max_process(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.max_process "Link to this definition")
The maximum amount of processes that can be running on this executor.

zuul.executor.<executor>.cur_process(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executor.%3Cexecutor%3E.cur_process "Link to this definition")
The current amount of running processes on this executor.

zuul.nodepool.requests[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.requests "Link to this definition")
Holds metrics related to Zuul requests and responses from Nodepool.

States are one of:

> _requested_
> Node request submitted by Zuul to Nodepool
> 
> _canceled_
> Node request was canceled by Zuul
> 
> _failed_
> Nodepool failed to fulfill a node request
> 
> _fulfilled_
> Nodes were assigned by Nodepool

zuul.nodepool.requests.<state>(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.requests.%3Cstate%3E "Link to this definition")
Records the elapsed time from request to completion for states failed and fulfilled. For example, `zuul.nodepool.request.fulfilled.mean` will give the average time for all fulfilled requests within each `statsd` flush interval.

A lower value for fulfilled requests is better. Ideally, there will be no failed requests.

zuul.nodepool.requests.<state>.total(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.requests.%3Cstate%3E.total "Link to this definition")
Incremented when nodes are assigned or removed as described in the states above.

zuul.nodepool.requests.<state>.size.<size>(counter,timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.requests.%3Cstate%3E.size.%3Csize%3E "Link to this definition")
Increments for the node count of each request. For example, a request for 3 nodes would use the key `zuul.nodepool.requests.requested.size.3`; fulfillment of 3 node requests can be tracked with `zuul.nodepool.requests.fulfilled.size.3`.

The timer is implemented for `fulfilled` and `failed` requests. For example, the timer `zuul.nodepool.requests.failed.size.3.mean` gives the average time of 3-node failed requests within the `statsd` flush interval. A lower value for fulfilled requests is better. Ideally, there will be no failed requests.

zuul.nodepool.requests.<state>.label.<label>(counter,timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.requests.%3Cstate%3E.label.%3Clabel%3E "Link to this definition")
Increments for the label of each request. For example, requests for centos7 nodes could be tracked with `zuul.nodepool.requests.requested.centos7`.

The timer is implemented for `fulfilled` and `failed` requests. For example, the timer `zuul.nodepool.requests.fulfilled.label.centos7.mean` gives the average time of `centos7` fulfilled requests within the `statsd` flush interval. A lower value for fulfilled requests is better. Ideally, there will be no failed requests.

zuul.nodepool[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool "Link to this definition")zuul.nodepool.current_requests(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.current_requests "Link to this definition")
The number of outstanding nodepool requests from Zuul. Ideally this will be at zero, meaning all requests are fulfilled. Persistently high values indicate more testing node resources would be helpful.

zuul.nodepool.tenant.<tenant>.current_requests(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.tenant.%3Ctenant%3E.current_requests "Link to this definition")
The number of outstanding nodepool requests from Zuul drilled down by <tenant>. If a tenant for a node request cannot be determined, it is reported as `unknown`. This relates to `zuul.nodepool.current_requests`.

zuul.nodepool.resources[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources "Link to this definition")
Holds metrics about resource usage by tenant or project if resources of nodes are reported by nodepool.

zuul.nodepool.resources.in_use[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.in_use "Link to this definition")
Holds metrics about resources currently in use by a build.

zuul.nodepool.resources.in_use.tenant[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.in_use.tenant "Link to this definition")
Holds resource usage metrics by tenant.

zuul.nodepool.resources.in_use.tenant.<tenant>.<resource>(counter,gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.in_use.tenant.%3Ctenant%3E.%3Cresource%3E "Link to this definition")
Counter with the summed usage by tenant as <resource> seconds and gauge with the currently in use resources by tenant.

zuul.nodepool.resources.in_use.project[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.in_use.project "Link to this definition")
Holds resource usage metrics by project.

zuul.nodepool.resources.in_use.project.<project>.<resource>(counter,gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.in_use.project.%3Cproject%3E.%3Cresource%3E "Link to this definition")
Counter with the summed usage by project as <resource> seconds and gauge with the currently used resources by project.

zuul.nodepool.resources.total[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.total "Link to this definition")
Holds metrics about resources allocated in total. This includes resources that are currently in use, allocated but not yet in use, and scheduled to be deleted.

zuul.nodepool.resources.total.tenant[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.total.tenant "Link to this definition")
Holds resource usage metrics by tenant.

zuul.nodepool.resources.total.tenant.<tenant>.<resource>(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.nodepool.resources.total.tenant.%3Ctenant%3E.%3Cresource%3E "Link to this definition")
Gauge with the currently used resources by tenant.

zuul.mergers[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.mergers "Link to this definition")
Holds metrics related to Zuul mergers.

zuul.mergers.online(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.mergers.online "Link to this definition")
The number of Zuul merger processes online.

zuul.mergers.jobs_running(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.mergers.jobs_running "Link to this definition")
The number of merge jobs running.

zuul.mergers.jobs_queued(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.mergers.jobs_queued "Link to this definition")
The number of merge jobs waiting for a merger. This should ideally be zero; persistent higher values indicate more merger resources would be useful.

zuul.executors[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors "Link to this definition")
Holds metrics related to unzoned executors.

This is a copy of [zuul.executors.unzoned](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned "stat-zuul.executors.unzoned"). It does not include information about zoned executors.

Warning

The metrics at this location are deprecated and will be removed in a future version. Please begin using [zuul.executors.unzoned](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned "stat-zuul.executors.unzoned") instead.

zuul.executors.online(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.online "Link to this definition")
The number of Zuul executor processes online.

zuul.executors.accepting(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.accepting "Link to this definition")
The number of Zuul executor processes accepting new jobs.

zuul.executors.jobs_running(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.jobs_running "Link to this definition")
The number of executor jobs running.

zuul.executors.jobs_queued(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.jobs_queued "Link to this definition")
The number of jobs allocated nodes, but queued waiting for an executor to run on. This should ideally be at zero; persistent higher values indicate more executor resources would be useful.

zuul.executors.unzoned[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned "Link to this definition")
Holds metrics related to unzoned executors.

zuul.executors.unzoned.online(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned.online "Link to this definition")
The number of unzoned Zuul executor processes online.

zuul.executors.unzoned.accepting(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned.accepting "Link to this definition")
The number of unzoned Zuul executor processes accepting new jobs.

zuul.executors.unzoned.jobs_running(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned.jobs_running "Link to this definition")
The number of unzoned executor jobs running.

zuul.executors.unzoned.jobs_queued(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.unzoned.jobs_queued "Link to this definition")
The number of jobs allocated nodes, but queued waiting for an unzoned executor to run on. This should ideally be at zero; persistent higher values indicate more executor resources would be useful.

zuul.executors.zone[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.zone "Link to this definition")
Holds metrics related to zoned executors.

zuul.executors.zone.<zone>.online(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.zone.%3Czone%3E.online "Link to this definition")
The number of Zuul executor processes online in this zone.

zuul.executors.zone.<zone>.accepting(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.zone.%3Czone%3E.accepting "Link to this definition")
The number of Zuul executor processes accepting new jobs in this zone.

zuul.executors.zone.<zone>.jobs_running(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.zone.%3Czone%3E.jobs_running "Link to this definition")
The number of executor jobs running in this zone.

zuul.executors.zone.<zone>.jobs_queued(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.executors.zone.%3Czone%3E.jobs_queued "Link to this definition")
The number of jobs allocated nodes, but queued waiting for an executor in this zone to run on. This should ideally be at zero; persistent higher values indicate more executor resources would be useful.

zuul.scheduler[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler "Link to this definition")
Holds metrics related to the Zuul scheduler.

zuul.scheduler.eventqueues[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler.eventqueues "Link to this definition")
Holds metrics about the event queue lengths in the Zuul scheduler.

zuul.scheduler.eventqueues.management(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler.eventqueues.management "Link to this definition")
The size of the current reconfiguration event queue.

zuul.scheduler.eventqueues.connection.<connection-name>(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler.eventqueues.connection.%3Cconnection-name%3E "Link to this definition")
The size of the current connection event queue.

zuul.scheduler.run_handler(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler.run_handler "Link to this definition")
A timer metric reporting the time taken for one scheduler run handler iteration.

zuul.scheduler.time_query(timer)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.scheduler.time_query "Link to this definition")
Each time the scheduler performs a query against the SQL database in order to determine an estimated time for a job, it emits this timer of the duration of the query. Note this is a performance metric of how long the SQL query takes; it is not the estimated time value itself.

zuul.web[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web "Link to this definition")
Holds metrics related to the Zuul web component.

zuul.web.server.<hostname>[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web.server.%3Chostname%3E "Link to this definition")
Holds metrics from a specific zuul-web server.

zuul.web.server.<hostname>.threadpool[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web.server.%3Chostname%3E.threadpool "Link to this definition")
Metrics related to the web server thread pool.

zuul.web.server.<hostname>.threadpool.idle(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web.server.%3Chostname%3E.threadpool.idle "Link to this definition")
The number of idle workers.

zuul.web.server.<hostname>.threadpool.queue(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web.server.%3Chostname%3E.threadpool.queue "Link to this definition")
The number of requests queued for workers.

zuul.web.server.<hostname>.streamers(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-zuul.web.server.%3Chostname%3E.streamers "Link to this definition")
The number of log streamers currently in operation.

As an example, given a job named myjob in mytenant triggered by a change to myproject on the master branch in the gate pipeline which took 40 seconds to build, the Zuul scheduler will emit the following statsd events:

> *   `zuul.tenant.mytenant.pipeline.gate.project.example_com.myproject.master.job.myjob.SUCCESS` +1
> 
> *   `zuul.tenant.mytenant.pipeline.gate.project.example_com.myproject.master.job.myjob.SUCCESS` 40 seconds
> 
> *   `zuul.tenant.mytenant.pipeline.gate.all_jobs` +1

Prometheus monitoring[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#prometheus-monitoring "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------

Zuul comes with support to start a [prometheus](https://prometheus.io/docs/introduction/overview/) metric server to be added as prometheus’s target.

### Configuration[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#id1 "Link to this heading")

To enable the service, set the `prometheus_port` in a service section of `zuul.conf`. For example setting [scheduler.prometheus_port](https://zuul-ci.org/docs/zuul/latest/configuration.html#attr-scheduler.prometheus_port "attr-scheduler.prometheus_port") to 9091 starts a HTTP server to expose metrics to a prometheus services at: [http://scheduler:9091/metrics](http://scheduler:9091/metrics)

### Metrics[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#id2 "Link to this heading")

These metrics are exposed by default:

process_virtual_memory_bytes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-process_virtual_memory_bytes "Link to this definition")process_resident_memory_bytes(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-process_resident_memory_bytes "Link to this definition")process_open_fds(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-process_open_fds "Link to this definition")process_start_time_seconds(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-process_start_time_seconds "Link to this definition")process_cpu_seconds_total(counter)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-process_cpu_seconds_total "Link to this definition")
On web servers the following additional metrics are exposed:

web_threadpool_idle(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-web_threadpool_idle "Link to this definition")
The number of idle workers in the thread pool.

web_threadpool_queue(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-web_threadpool_queue "Link to this definition")
The number of requests queued for thread pool workers.

web_streamers(gauge)[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#stat-web_streamers "Link to this definition")
The number of log streamers currently in operation.

### Liveness Probes[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#liveness-probes "Link to this heading")

The Prometheus server also supports liveness and ready probes at the following URIS:

/health/live[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#path-health/live "Link to this definition")

Returns 200 as long as the process is running.

/health/ready[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#path-health/ready "Link to this definition")

Returns 200 if the process is in RUNNING or PAUSED states. Otherwise, returns 503. Note that 503 is returned for INITIALIZED, so this may be used to determine when a component has completely finished loading configuration.

/health/status[](https://zuul-ci.org/docs/zuul/latest/monitoring.html#path-health/status "Link to this definition")

This always returns 200, but includes the component status as the text body of the response.
