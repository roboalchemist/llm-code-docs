# luigi.rpc

Implementation of the REST interface between the workers and the server.
rpc.py implements the client side of it, server.py implements the server side.
See Using the Central Scheduler for more info.

Classes

`RemoteScheduler`([url, connect_timeout])

Scheduler proxy object.

`RequestsFetcher`()

`URLLibFetcher`()

Exceptions

`RPCError`(message[, sub_exception])

exception luigi.rpc.RPCError(*message*, *sub_exception=None*)

class luigi.rpc.URLLibFetcher

raises = (<class 'urllib.error.URLError'>, <class 'TimeoutError'>)

fetch(*full_url*, *body*, *timeout*)

close()

class luigi.rpc.RequestsFetcher

check_pid()

fetch(*full_url*, *body*, *timeout*)

close()

class luigi.rpc.RemoteScheduler(*url='http://localhost:8082/'*, *connect_timeout=None*)

Scheduler proxy object. Talks to a RemoteSchedulerResponder.

close()

add_scheduler_message_response(*task_id*, *message_id*, *response*)

add_task(*task_id=None*, *status='PENDING'*, *runnable=True*, *deps=None*, *new_deps=None*, *expl=None*, *resources=None*, *priority=0*, *family=''*, *module=None*, *params=None*, *param_visibilities=None*, *accepts_messages=False*, *assistant=False*, *tracking_url=None*, *worker=None*, *batchable=None*, *batch_id=None*, *retry_policy_dict=None*, *owners=None*, ***kwargs*)

- 

add task identified by task_id if it doesn’t exist

- 

if deps is not None, update dependency list

- 

update status of task

- 

add additional workers/stakeholders

- 

update priority when needed

add_task_batcher(*worker*, *task_family*, *batched_args*, *max_batch_size=inf*)

add_worker(*worker*, *info*, ***kwargs*)

announce_scheduling_failure(*task_name*, *family*, *params*, *expl*, *owners*, ***kwargs*)

count_pending(*worker*)

decrease_running_task_resources(*task_id*, *decrease_resources*)

dep_graph(*task_id*, *include_done=True*, ***kwargs*)

disable_worker(*worker*)

fetch_error(*task_id*, ***kwargs*)

forgive_failures(*task_id=None*)

get_running_task_resources(*task_id*)

get_scheduler_message_response(*task_id*, *message_id*)

get_task_progress_percentage(*task_id*)

get_task_status_message(*task_id*)

get_work(*host=None*, *assistant=False*, *current_tasks=None*, *worker=None*, ***kwargs*)

graph(***kwargs*)

has_task_history()

inverse_dep_graph(*task_id*, *include_done=True*, ***kwargs*)

is_pause_enabled()

is_paused()

mark_as_done(*task_id=None*)

pause()

ping(***kwargs*)

prune()

re_enable_task(*task_id*)

report_task_statistics(*task_id*, *statistics*)

resource_list()

Resources usage info and their consumers (tasks).

send_scheduler_message(*worker*, *task*, *content*)

set_task_progress_percentage(*task_id*, *progress_percentage*)

set_task_status_message(*task_id*, *status_message*)

set_worker_processes(*worker*, *n*)

task_list(*status=''*, *upstream_status=''*, *limit=True*, *search=None*, *max_shown_tasks=None*, ***kwargs*)

Query for a subset of tasks by status.

task_search(*task_str*, ***kwargs*)

Query for a subset of tasks by task_id.

Parameters:

**task_str**

Returns:

unpause()

update_metrics_task_started(*task*)

update_resource(*resource*, *amount*)

update_resources(***resources*)

worker_list(*include_running=True*, ***kwargs*)