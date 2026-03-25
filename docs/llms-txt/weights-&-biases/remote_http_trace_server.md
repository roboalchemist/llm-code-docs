# Source: https://docs.wandb.ai/weave/reference/python-sdk/trace_server_bindings/remote_http_trace_server.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wandb.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# remote_http_trace_server

> Python SDK reference for weave.trace_server_bindings.remote_http_trace_server

export const SourceLink = ({url}) => <a href={url} target="_blank" rel="noopener noreferrer" className="source-link">
    Source
  </a>;

# API Overview

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L46" />

## <kbd>class</kbd> `RemoteHTTPTraceServer`

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L50" />

### <kbd>method</kbd> `__init__`

```python  theme={null}
__init__(
    trace_server_url: str,
    should_batch: bool = False,
    remote_request_bytes_limit: int = 32505856,
    auth: tuple[str, str] | None = None,
    extra_headers: dict[str, str] | None = None
)
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L630" />

### <kbd>method</kbd> `actions_execute_batch`

```python  theme={null}
actions_execute_batch(req: ActionsExecuteBatchReq) → ActionsExecuteBatchRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L733" />

### <kbd>method</kbd> `annotation_queue_add_calls`

```python  theme={null}
annotation_queue_add_calls(
    req: AnnotationQueueAddCallsReq
) → AnnotationQueueAddCallsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L701" />

### <kbd>method</kbd> `annotation_queue_create`

```python  theme={null}
annotation_queue_create(
    req: AnnotationQueueCreateReq
) → AnnotationQueueCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L749" />

### <kbd>method</kbd> `annotation_queue_items_query`

```python  theme={null}
annotation_queue_items_query(
    req: AnnotationQueueItemsQueryReq
) → AnnotationQueueItemsQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L721" />

### <kbd>method</kbd> `annotation_queue_read`

```python  theme={null}
annotation_queue_read(req: AnnotationQueueReadReq) → AnnotationQueueReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L711" />

### <kbd>method</kbd> `annotation_queues_query_stream`

```python  theme={null}
annotation_queues_query_stream(
    req: AnnotationQueuesQueryReq
) → Iterator[AnnotationQueueSchema]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L768" />

### <kbd>method</kbd> `annotation_queues_stats`

```python  theme={null}
annotation_queues_stats(
    req: AnnotationQueuesStatsReq
) → AnnotationQueuesStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L778" />

### <kbd>method</kbd> `annotator_queue_items_progress_update`

```python  theme={null}
annotator_queue_items_progress_update(
    req: AnnotatorQueueItemsProgressUpdateReq
) → AnnotatorQueueItemsProgressUpdateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L399" />

### <kbd>method</kbd> `call_end`

```python  theme={null}
call_end(req: CallEndReq) → CallEndRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L408" />

### <kbd>method</kbd> `call_read`

```python  theme={null}
call_read(req: CallReadReq) → CallReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L379" />

### <kbd>method</kbd> `call_start`

```python  theme={null}
call_start(req: CallStartReq) → CallStartRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L394" />

### <kbd>method</kbd> `call_start_batch`

```python  theme={null}
call_start_batch(req: CallCreateBatchReq) → CallCreateBatchRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L437" />

### <kbd>method</kbd> `call_update`

```python  theme={null}
call_update(req: CallUpdateReq) → CallUpdateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L431" />

### <kbd>method</kbd> `calls_delete`

```python  theme={null}
calls_delete(req: CallsDeleteReq) → CallsDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L414" />

### <kbd>method</kbd> `calls_query`

```python  theme={null}
calls_query(req: CallsQueryReq) → CallsQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L425" />

### <kbd>method</kbd> `calls_query_stats`

```python  theme={null}
calls_query_stats(req: CallsQueryStatsReq) → CallsQueryStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L419" />

### <kbd>method</kbd> `calls_query_stream`

```python  theme={null}
calls_query_stream(req: CallsQueryReq) → Iterator[CallSchema]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L660" />

### <kbd>method</kbd> `completions_create`

```python  theme={null}
completions_create(req: CompletionsCreateReq) → CompletionsCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L670" />

### <kbd>method</kbd> `completions_create_stream`

```python  theme={null}
completions_create_stream(req: CompletionsCreateReq) → Iterator[dict[str, Any]]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L648" />

### <kbd>method</kbd> `cost_create`

```python  theme={null}
cost_create(req: CostCreateReq) → CostCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L654" />

### <kbd>method</kbd> `cost_purge`

```python  theme={null}
cost_purge(req: CostPurgeReq) → CostPurgeRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L642" />

### <kbd>method</kbd> `cost_query`

```python  theme={null}
cost_query(req: CostQueryReq) → CostQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L869" />

### <kbd>method</kbd> `dataset_create`

```python  theme={null}
dataset_create(req: DatasetCreateReq) → DatasetCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L915" />

### <kbd>method</kbd> `dataset_delete`

```python  theme={null}
dataset_delete(req: DatasetDeleteReq) → DatasetDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L896" />

### <kbd>method</kbd> `dataset_list`

```python  theme={null}
dataset_list(req: DatasetListReq) → Iterator[DatasetReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L884" />

### <kbd>method</kbd> `dataset_read`

```python  theme={null}
dataset_read(req: DatasetReadReq) → DatasetReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L124" />

### <kbd>method</kbd> `delete`

```python  theme={null}
delete(url: str, *args: Any, **kwargs: Any) → Response
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L79" />

### <kbd>method</kbd> `ensure_project_exists`

```python  theme={null}
ensure_project_exists(entity: str, project: str) → EnsureProjectExistsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L794" />

### <kbd>method</kbd> `evaluate_model`

```python  theme={null}
evaluate_model(req: EvaluateModelReq) → EvaluateModelRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L995" />

### <kbd>method</kbd> `evaluation_create`

```python  theme={null}
evaluation_create(req: EvaluationCreateReq) → EvaluationCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1047" />

### <kbd>method</kbd> `evaluation_delete`

```python  theme={null}
evaluation_delete(req: EvaluationDeleteReq) → EvaluationDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1026" />

### <kbd>method</kbd> `evaluation_list`

```python  theme={null}
evaluation_list(req: EvaluationListReq) → Iterator[EvaluationReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1012" />

### <kbd>method</kbd> `evaluation_read`

```python  theme={null}
evaluation_read(req: EvaluationReadReq) → EvaluationReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1131" />

### <kbd>method</kbd> `evaluation_run_create`

```python  theme={null}
evaluation_run_create(req: EvaluationRunCreateReq) → EvaluationRunCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1189" />

### <kbd>method</kbd> `evaluation_run_delete`

```python  theme={null}
evaluation_run_delete(req: EvaluationRunDeleteReq) → EvaluationRunDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1206" />

### <kbd>method</kbd> `evaluation_run_finish`

```python  theme={null}
evaluation_run_finish(req: EvaluationRunFinishReq) → EvaluationRunFinishRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1161" />

### <kbd>method</kbd> `evaluation_run_list`

```python  theme={null}
evaluation_run_list(req: EvaluationRunListReq) → Iterator[EvaluationRunReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1147" />

### <kbd>method</kbd> `evaluation_run_read`

```python  theme={null}
evaluation_run_read(req: EvaluationRunReadReq) → EvaluationRunReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L797" />

### <kbd>method</kbd> `evaluation_status`

```python  theme={null}
evaluation_status(req: EvaluationStatusReq) → EvaluationStatusRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L581" />

### <kbd>method</kbd> `feedback_create`

```python  theme={null}
feedback_create(req: FeedbackCreateReq) → FeedbackCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L602" />

### <kbd>method</kbd> `feedback_create_batch`

```python  theme={null}
feedback_create_batch(req: FeedbackCreateBatchReq) → FeedbackCreateBatchRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L618" />

### <kbd>method</kbd> `feedback_purge`

```python  theme={null}
feedback_purge(req: FeedbackPurgeReq) → FeedbackPurgeRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L612" />

### <kbd>method</kbd> `feedback_query`

```python  theme={null}
feedback_query(req: FeedbackQueryReq) → FeedbackQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L624" />

### <kbd>method</kbd> `feedback_replace`

```python  theme={null}
feedback_replace(req: FeedbackReplaceReq) → FeedbackReplaceRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/utils/retry.py#L563" />

### <kbd>method</kbd> `file_content_read`

```python  theme={null}
file_content_read(req: FileContentReadReq) → FileContentReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/utils/retry.py#L553" />

### <kbd>method</kbd> `file_create`

```python  theme={null}
file_create(req: FileCreateReq) → FileCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L576" />

### <kbd>method</kbd> `files_stats`

```python  theme={null}
files_stats(req: FilesStatsReq) → FilesStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L88" />

### <kbd>classmethod</kbd> `from_env`

```python  theme={null}
from_env(should_batch: bool = False) → Self
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L102" />

### <kbd>method</kbd> `get`

```python  theme={null}
get(url: str, *args: Any, **kwargs: Any) → Response
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L186" />

### <kbd>method</kbd> `get_call_processor`

```python  theme={null}
get_call_processor() → AsyncBatchProcessor | None
```

Custom method not defined on the formal TraceServerInterface to expose the underlying call processor. Should be formalized in a client-side interface.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L274" />

### <kbd>method</kbd> `get_feedback_processor`

```python  theme={null}
get_feedback_processor() → AsyncBatchProcessor | None
```

Custom method not defined on the formal TraceServerInterface to expose the underlying feedback processor. Should be formalized in a client-side interface.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L678" />

### <kbd>method</kbd> `image_create`

```python  theme={null}
image_create(req: ImageGenerationCreateReq) → ImageGenerationCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1068" />

### <kbd>method</kbd> `model_create`

```python  theme={null}
model_create(req: ModelCreateReq) → ModelCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1114" />

### <kbd>method</kbd> `model_delete`

```python  theme={null}
model_delete(req: ModelDeleteReq) → ModelDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1095" />

### <kbd>method</kbd> `model_list`

```python  theme={null}
model_list(req: ModelListReq) → Iterator[ModelReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1083" />

### <kbd>method</kbd> `model_read`

```python  theme={null}
model_read(req: ModelReadReq) → ModelReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L445" />

### <kbd>method</kbd> `obj_create`

```python  theme={null}
obj_create(req: ObjCreateReq) → ObjCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L461" />

### <kbd>method</kbd> `obj_delete`

```python  theme={null}
obj_delete(req: ObjDeleteReq) → ObjDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L451" />

### <kbd>method</kbd> `obj_read`

```python  theme={null}
obj_read(req: ObjReadReq) → ObjReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L455" />

### <kbd>method</kbd> `objs_query`

```python  theme={null}
objs_query(req: ObjQueryReq) → ObjQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L804" />

### <kbd>method</kbd> `op_create`

```python  theme={null}
op_create(req: OpCreateReq) → OpCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L852" />

### <kbd>method</kbd> `op_delete`

```python  theme={null}
op_delete(req: OpDeleteReq) → OpDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L831" />

### <kbd>method</kbd> `op_list`

```python  theme={null}
op_list(req: OpListReq) → Iterator[OpReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L819" />

### <kbd>method</kbd> `op_read`

```python  theme={null}
op_read(req: OpReadReq) → OpReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L374" />

### <kbd>method</kbd> `otel_export`

```python  theme={null}
otel_export(req: OtelExportReq) → OtelExportRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L113" />

### <kbd>method</kbd> `post`

```python  theme={null}
post(url: str, *args: Any, **kwargs: Any) → Response
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1222" />

### <kbd>method</kbd> `prediction_create`

```python  theme={null}
prediction_create(req: PredictionCreateReq) → PredictionCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1274" />

### <kbd>method</kbd> `prediction_delete`

```python  theme={null}
prediction_delete(req: PredictionDeleteReq) → PredictionDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1291" />

### <kbd>method</kbd> `prediction_finish`

```python  theme={null}
prediction_finish(req: PredictionFinishReq) → PredictionFinishRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1251" />

### <kbd>method</kbd> `prediction_list`

```python  theme={null}
prediction_list(req: PredictionListReq) → Iterator[PredictionReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1239" />

### <kbd>method</kbd> `prediction_read`

```python  theme={null}
prediction_read(req: PredictionReadReq) → PredictionReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L688" />

### <kbd>method</kbd> `project_stats`

```python  theme={null}
project_stats(req: ProjectStatsReq) → ProjectStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L547" />

### <kbd>method</kbd> `refs_read_batch`

```python  theme={null}
refs_read_batch(req: RefsReadBatchReq) → RefsReadBatchRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1307" />

### <kbd>method</kbd> `score_create`

```python  theme={null}
score_create(req: ScoreCreateReq) → ScoreCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1355" />

### <kbd>method</kbd> `score_delete`

```python  theme={null}
score_delete(req: ScoreDeleteReq) → ScoreDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1334" />

### <kbd>method</kbd> `score_list`

```python  theme={null}
score_list(req: ScoreListReq) → Iterator[ScoreReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L1322" />

### <kbd>method</kbd> `score_read`

```python  theme={null}
score_read(req: ScoreReadReq) → ScoreReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L932" />

### <kbd>method</kbd> `scorer_create`

```python  theme={null}
scorer_create(req: ScorerCreateReq) → ScorerCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L978" />

### <kbd>method</kbd> `scorer_delete`

```python  theme={null}
scorer_delete(req: ScorerDeleteReq) → ScorerDeleteRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L959" />

### <kbd>method</kbd> `scorer_list`

```python  theme={null}
scorer_list(req: ScorerListReq) → Iterator[ScorerReadRes]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L947" />

### <kbd>method</kbd> `scorer_read`

```python  theme={null}
scorer_read(req: ScorerReadReq) → ScorerReadRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/utils/retry.py#L366" />

### <kbd>method</kbd> `server_info`

```python  theme={null}
server_info() → ServerInfoRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L92" />

### <kbd>method</kbd> `set_auth`

```python  theme={null}
set_auth(auth: tuple[str, str]) → None
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L466" />

### <kbd>method</kbd> `table_create`

```python  theme={null}
table_create(req: TableCreateReq) → TableCreateRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L524" />

### <kbd>method</kbd> `table_create_from_digests`

```python  theme={null}
table_create_from_digests(
    req: TableCreateFromDigestsReq
) → TableCreateFromDigestsRes
```

Create a table by specifying row digests instead of actual rows.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L504" />

### <kbd>method</kbd> `table_query`

```python  theme={null}
table_query(req: TableQueryReq) → TableQueryRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L518" />

### <kbd>method</kbd> `table_query_stats`

```python  theme={null}
table_query_stats(req: TableQueryStatsReq) → TableQueryStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L536" />

### <kbd>method</kbd> `table_query_stats_batch`

```python  theme={null}
table_query_stats_batch(req: TableQueryStatsReq) → TableQueryStatsRes
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L510" />

### <kbd>method</kbd> `table_query_stream`

```python  theme={null}
table_query_stream(req: TableQueryReq) → Iterator[TableRowSchema]
```

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/pydantic/_internal/_validate_call.py#L472" />

### <kbd>method</kbd> `table_update`

```python  theme={null}
table_update(req: TableUpdateReq) → TableUpdateRes
```

Similar to `calls/batch_upsert`, we can dynamically adjust the payload size due to the property that table updates can be decomposed into a series of updates.

***

<SourceLink url="https://github.com/wandb/weave/blob/v0.52.24/weave/trace_server_bindings/remote_http_trace_server.py#L693" />

### <kbd>method</kbd> `threads_query_stream`

```python  theme={null}
threads_query_stream(req: ThreadsQueryReq) → Iterator[ThreadSchema]
```
